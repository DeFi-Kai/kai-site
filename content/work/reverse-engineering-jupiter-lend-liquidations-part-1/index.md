+++
date = '2026-09-28T09:00:00-04:00'
draft = false
title = 'Reverse-Engineering Jupiter Lend Liquidations: Part 1'
slug = 'reverse-engineering-jupiter-lend-liquidations-part-1'
description = 'A guide to decoding Jupiter Lend liquidation instructions from raw Solana data using Solscan and DuneSQL.'
tags = ['Data & Methods', 'Technical Writing']
+++

During the [October 10, 2025 market selloff](https://www.fticonsulting.com/insights/articles/crypto-crash-october-2025-leverage-met-liquidity), more than $19 billion in leveraged positions were liquidated within 24 hours across derivatives markets.

This selloff raised a related question: how did [blockchain credit markets](https://www.bankofcanada.ca/2026/04/staff-analytical-paper-2026-13/) handle the same shock?

I wanted to analyze liquidations on [Jupiter Lend](https://jup.ag/lend/earn), a newly launched credit market on the Solana blockchain, to understand how many liquidations were processed, the notional value of liquidations, and the breadth of its liquidator network. 

Decoded datasets are often published on [Dune](https://dune.com/), a data platform for blockchains. However, there are no query-ready tables for Jupiter Lend yet. Moreover, Jupiter Lend's documentation is thin and the team hasn't published an [Interface Description Language (IDL)](https://www.anchor-lang.com/docs/basics/idl) file exposing how instructions and accounts are structured. 

To produce a dataset of Jupiter Lend liquidations, I reverse-engineered the program by examining its instructions on Solscan, mapping them to Dune's tables, and writing SQL queries to decode them.

This is the first part of a three-part series. In this guide, we'll walk through how to decode the relevant instructions to reverse-engineer Jupiter Lend liquidations. Part two covers building the final dataset, and part three analyzes the results of the October 10, 2025 dataset.

**The final dataset includes transaction-level liquidation records with:**
- collateral seized
- debt repaid
- collateral and borrowed assets
- liquidator
- liquidated position

![Transaction-level Jupiter Lend liquidation dataset on Dune](<images/Screenshot From 2026-09-27 18-22-49.png>)


https://dune.com/queries/8711844/12764525

This is an intermediate-to-advanced guide for analysts familiar with SQL who want to query Solana programs (written in Anchor) from scratch. The methods used in this guide serve as a generalizable approach for decoding and querying undocumented Anchor programs. 
## Using Dune to Query Data

Dune ingests and indexes Solana’s real-time activity in its data warehouse. Analysts query this data with [DuneSQL](https://docs.dune.com/query-engine/overview) to create datasets and visualizations. 

![Dune's Solana data layers](<images/Screenshot 2026-09-21 at 4.24.37 PM.png>)


Dune's data is organized into three buckets: Raw data, Decoded data, and Curated data. Raw data contains unfiltered transactions indexed directly from RPC nodes. Decoded data reveals explicit smart contract events and function calls extracted from Raw data. Finally, curated data translate the decoded tables into human-readable columns with labels corresponding to financial semantics.

![Solana data analysis guide](<images/899647ad-ce7f-46e0-8645-b7de9340e61e_1182x684.webp>)

https://read.cryptodatabytes.com/p/starter-guide-to-solana-data-analysis

Dune recommends using decoded tables for performant queries, but Jupiter Lend's program isn't decoded yet, so we'll query raw data to create a curated table. 

For this guide, we'll use the following columns from the [`solana.instruction_calls`](https://dune.com/data/solana.instruction_calls) table:

| Column                    | Data type        | Description                                  |
| ------------------------- | ---------------- | -------------------------------------------- |
| `block_time`              | `timestamp`      | Time the transaction was included in a block |
| `tx_id`                   | `varchar`        | Unique transaction identifier                |
| `outer_instruction_index` | `integer`        | Position of the outer instruction            |
| `inner_instruction_index` | `integer`        | Position of the inner instruction            |
| `executing_account`       | `varchar`        | Program executing the instruction            |
| `data`                    | `varbinary`      | Encoded instruction data                     |
| `tx_success`              | `boolean`        | Whether the transaction succeeded            |
| `account_arguments`       | `array(varchar)` | Accounts passed to the instruction           |
| `tx_signer`               | `varchar`        | Transaction signer                           |
https://dune.com/data/solana.instruction_calls

## How Jupiter Lend Liquidations Work

On Jupiter Lend, users deposit cryptocurrencies or tokenized assets as collateral and can borrow another asset up to a specified loan-to-value (LTV) ratio. Each market also has a liquidation threshold that determines when a borrowing position becomes undercollateralized enough to be eligible for liquidation.

When a position crosses its liquidation threshold, Jupiter Lend can programmatically liquidate part of the position to reduce the risk of default and bad debt for the protocol.

![Jupiter Lend liquidation flow diagram](<images/Drawing 2026-09-27 16.36.40.excalidraw.png>)


Liquidations are carried out by a permissionless network of liquidators that monitor borrowing positions. During a partial liquidation, a liquidator repays a portion of the borrower’s debt and receives collateral in return, including a liquidation penalty.
### How liquidations appear on-chain
Jupiter Lend is made up of multiple programs, each responsible for specific logic. For this walkthrough, we'll focus on the `Jupiter Lend Borrow` program, which handles the logic for borrowing and repayment activity, including liquidations.

![Jupiter Lend program diagram](<images/Image 4.png>)

Jupiter Lend Programs
[https://dev.jup.ag/docs/lend](https://dev.jup.ag/docs/lend)

A liquidation triggers a `Jupiter Lend Borrow: Liquidate` instruction that identifies the borrow position, collateral seized, debt repaid, and other details. It also triggers two `Jupiter Lend Liquidity: Operate` [cross-program invocation (CPI)](https://solana.com/docs/core/cpi) calls that transfer the debt repaid and collateral seized from the protocol-owned vaults to the liquidator.
## Mental Model for Reverse-Engineering

To reverse-engineer a program, you need an example transaction. All transactions are visible on Solscan.io, which tracks Solana's historical transactions. With an example transaction, you can inspect asset flows and instruction positioning to identify patterns. Those patterns will inform assumptions that you can test in Dune to validate other transactions as liquidations. Once we identify the relevant values, we can use SQL to filter rows and select the correct columns. 

Throughout this guide, you'll want to have three tabs open, including:
- This guide
- Solscan.io
- Dune.com

You'll need to reference all three pages to work through the examples.

Conceptually, we're building an event-level table for liquidations with the following columns:

| Column                  | Description                    |
| ----------------------- | ------------------------------ |
| `tx_id`                 | Transaction ID                 |
| `block_time`            | Time of liquidation            |
| `liquidator`            | Liquidator address             |
| `position`              | Liquidated position ID         |
| `collateral_asset`      | Collateral asset seized        |
| `debt_asset`            | Debt asset repaid              |
| `collateral_amount_usd` | USD value of collateral seized |
| `debt_amount_usd`       | USD value of debt repaid       |

The final table will include additional columns with raw values for verification and further analysis. 
### Inspecting a known liquidation transaction

To find example liquidation transactions:
1. Visit [Solscan.io](https://solscan.io/).
2. Search for the `Jupiter Lend Borrow` program using its program ID, `jupr81YtYssSyPt8jbnGuiWon5f6x9TcDEFxYe3Bdzi`.
3. Scroll down to the transaction log.
4. Click the `instruction` filter.
5. Select the `liquidate` instruction and click `filter`.
6. Open two or three transactions and compare their instruction sequences and asset flows.

![Jupiter Lend Borrow program's Solscan transaction page](<images/Screenshot 2026-09-21 at 8.13.19 PM.png>)

https://solscan.io/account/jupr81YtYssSyPt8jbnGuiWon5f6x9TcDEFxYe3Bdzi

We'll use the transaction [vaupfN...](https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR) as the canonical example for this guide. It succeeded on October 10, 2025, contained `Jupiter Lend Borrow: Liquidate` at outer instruction index 4, and repaid USDC and received WSOL. The transaction also included a flashloan, but we'll exclude the flashloan logic from this guide.

In the following sections, we'll use this transaction to identify the liquidation instruction, map accounts, and decode the liquidation amounts. We'll begin each section with observations on Solscan and then map the desired fields to SQL on Dune. 
## Identifying the liquidation instruction

The goal is to identify every `Jupiter Lend Borrow: Liquidate` instruction contained in successful transactions within the observed time period and return three fields: (1) the transaction ID, (2) the timestamp, and (3) the outer instruction index. These fields become the keys used to reconstruct each liquidation later.

We'll start by inspecting the [canonical transaction](https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR). On Solscan, scroll down to the "Instruction Details" section, and you'll notice the transaction has seven instructions. For now, we'll focus on the `Jupiter Lend Borrow: Liquidate` instruction at index 4.

`Jupiter Lend Borrow: Liquidate` instruction at index 4
![Canonical liquidation instruction at index 4 on Solscan](<images/Screenshot From 2026-09-22 15-36-21 1.png>)
https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

Dune records the index for outer instructions in the `outer_instruction_index` column. For the canonical transaction, Solscan displays the liquidation at instruction #4, and Dune returns `outer_instruction_index = 4`.

Across liquidations, the `Jupiter Lend Borrow: Liquidate` instruction can appear at different indexes, so the instruction index cannot be used as a general filter. Instead, we'll use the explicit program label and instruction name as filters.

Solscan displays the program label and instruction name together as `Jupiter Lend Borrow: Liquidate`. Dune, however, stores them seperately: the program label, `Jupiter Lend Borrow`, resolves to the program ID stored in Dune's `executing_account` column, and the `Liquidate` instruction is recorded as serialized data in the `data` column.

**For the query, we'll filter transactions using both the `Jupiter Lend Borrow` program ID and the `Liquidate` data value.**

Let's locate both of these values on Solscan.

To locate the `Jupiter Lend Borrow` program ID, click the down arrow to the right of the instruction's name to reveal the "Instruction Details" section. The ID appears in the "Interact With" column: `jupr81YtYssSyPt8jbnGuiWon5f6x9TcDEFxYe3Bdzi`.

![Jupiter Lend Borrow program ID in Solscan instruction details](<images/Screenshot From 2026-09-27 21-30-36.png>)

https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

To view the `Liquidate` instruction's serialized data, click the "Raw" toggle in the upper-right corner of an instruction. The data appears on one line next to "Instruction Data".

![Raw serialized data for the liquidation instruction](<images/Screenshot From 2026-09-23 14-36-55.png>)

https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

As mentioned above, Dune does not store the instruction name as text in `data`; instead, it records the instruction's serialized value. The raw data begins with an 8-byte discriminator followed by the serialized arguments.

```text
{
  bytes 1-8              // Anchor instruction discriminator (identifies instruction)
  bytes 9 onward         // Instruction arguments
}
```

The 8-byte discriminator is a unique identifier for the instruction within the program. If the first eight bytes of an instruction's data match the liquidation discriminator within the Jupiter Lend Borrow program, the instruction is a liquidation.

Since each byte is represented by 2 hexadecimal characters, the 8-byte discriminator for the `Liquidate` instruction appears as the first 16 characters: `dfb3e27d302e274a`. 

The next step is to locate the transaction ID and timestamp. We'll use these values along with the outer instruction index to identify each liquidation uniquely. 

At the top of the Solscan page, the first fields are the "Signature," which records the transaction's unique ID, and the "Block & Timestamp," which records the block height and UTC timestamp of the transaction. For this query, the block height won't be necessary.

![Transaction signature and timestamp on Solscan](<images/Screenshot From 2026-09-25 12-57-49.png>)

https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

Here's how each of the observed fields on Solscan maps to Dune:

| Solscan observation        | Solana interpretation                                                 | Dune representation              |
| -------------------------- | --------------------------------------------------------------------- | -------------------------------- |
| Outer instruction index    | Position of the top-level instruction in the transaction              | `outer_instruction_index`        |
| Program label              | Program account that executes the instruction                         | `executing_account` (program ID) |
| Instruction type           | Serialized instruction data identifying the Anchor instruction        | 8-byte discriminator in `data`   |
| Signature                  | Base58 transaction signature that uniquely identifies the transaction | `tx_id`                          |
| Timestamp                  | UTC time associated with the transaction's block                      | `block_time`                     |

Here's an example query for October 10, 2025. It filters `Jupiter Lend Borrow: Liquidate` instructions and selects the timestamp, outer instruction index, and transaction ID:
```sql
SELECT
    block_time,
    outer_instruction_index,
    tx_id 
FROM solana.instruction_calls
WHERE executing_account = 'jupr81YtYssSyPt8jbnGuiWon5f6x9TcDEFxYe3Bdzi'
    AND substr("data", 1, 8) = from_hex('dfb3e27d302e274a')
    AND tx_success = TRUE
    AND block_time >= TIMESTAMP '2025-10-10 00:00:00 UTC'
    AND block_time <  TIMESTAMP '2025-10-11 00:00:00 UTC'
```
https://dune.com/queries/8822100

The query isolates instruction calls to the Jupiter Lend Borrow program by filtering the `executing_account` column using its program ID: `jupr81YtYssSyPt8jbnGuiWon5f6x9TcDEFxYe3Bdzi`. 

To isolate `Liquidate` instructions of the Jupiter Lend Borrow program, it filters the `data` column using its 8-byte discriminator:

```sql
WHERE substr("data", 1, 8) = from_hex('dfb3e27d302e274a')
```

Here’s what this line is doing:
- `substr("data", 1, 8)` returns 8 bytes of instruction data, starting at position 1.
- `from_hex(...)` converts the hex string into a varbinary value that SQL can compare

Blockchains record failed and successful transactions, so the query includes `AND tx_success = TRUE` to exclude failed transactions. 

*Note: `tx_success` describes the transaction containing the instruction, not the individual instruction call.*

Lastly, to reduce compute on the query, the query confines transactions to the October 10, 2025 event using the `block_time` column and UTC timestamps.

For the transaction structures examined here, `tx_id` and `outer_instruction_index` identify the containing liquidation context and allow us to retrieve its account arguments and inner instructions. The matched `Liquidate` instruction may be top-level or nested, so its own `inner_instruction_index` may be null or non-null.
## Mapping the liquidation accounts

With liquidation events captured, the next fields to extract are the following accounts:
- Liquidator
- Supply token (collateral asset)
- Borrow token (loan asset)
- Borrow position (the borrow position being liquidated)
### Locating the liquidator account

In the dataset, I define `liquidator` as the transaction signer exposed by Dune's `tx_signer` column. 

On Solscan, the signer account appears in the overview section in the "Signer" row. In the canonical transaction, the signer supplies the repayment asset and receives the seized collateral. The debt repayment and collateral movements are visible in the "Transaction Actions" section in Summary Mode.

![Liquidator signer and transaction actions on Solscan](<images/Screenshot From 2026-09-22 17-51-54.png>)

https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

This relationship is observed across the following successful transactions:

| Transaction                                                                                                                             | Outer instruction index | Dune `tx_signer`                               | Signer repaid debt? | Signer seized collateral? |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------: | ---------------------------------------------- | ------------------- | :-----------------------: |
| [Canonical `vaupf...`](https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR)   |           4 | `3ue9E1xfztuuNtpezARKBRiZxNHSKfjaTjwNcKShSJsz` | Yes                 |            Yes            |
| [Example 1 `5guPqg...`](https://solscan.io/tx/5guPqgEj9FadRp4A2xJrn2rnBhRpRk4etLxjfYG75z16cZiFiQaqsH91q3XJvvqj3mDCWUEqHck2WG2kmCZ3xrau) |           7 | `68Z9juTBhG3ybnbMYwTHP8z4jmEJndYtxzq3dLpQMz64` | Yes                 |            Yes            |
| [Example 2 `3LrpND...`](https://solscan.io/tx/3LrpNDZVxsMAwceue1QRuGAUxa7yajryChcrSUgD7X2g8NVrzQzoZNWbBvTowfP2vJCmnZXJq2bCXN8Vg31sdBNe) |           4 | `AKKVzD8w7AqKVhNTe82DREARHoHwUhi8YHm7sB9BWGBD` | Yes                 |            Yes            |
| [Example 3 `3169fy...`](https://solscan.io/tx/3169fyF7pcfUvm2GYUu33o4VQ6BoRyiiEYXt38j4o7JxU3Uo6BMRnpX1XJN8dvdAVjWK6BAaXcV2ukz8xpuxYbdA) |           7 | `68Z9juTBhG3ybnbMYwTHP8z4jmEJndYtxzq3dLpQMz64` | Yes                 |            Yes            |


The Solscan signer maps to Dune as follows:

| Solscan observation | Solana interpretation                                    | Dune representation |
| ------------------- | -------------------------------------------------------- | ------------------- |
| Transaction signer  | Transaction-level signer associated with the transaction | `tx_signer`         |

Here's an example query that selects `tx_signer` and renames the column to `liquidator`:

```sql
SELECT
	block_time,
	tx_id,
	outer_instruction_index,
	inner_instruction_index,
	tx_signer AS liquidator
FROM solana.instruction_calls
WHERE tx_id = 'vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR'
	AND executing_account = 'jupr81YtYssSyPt8jbnGuiWon5f6x9TcDEFxYe3Bdzi'
    AND substr("data", 1, 8) = from_hex('dfb3e27d302e274a')
	AND tx_success = TRUE
```
https://dune.com/queries/8822173

This query reuses the program ID, liquidation discriminator, and success filters introduced in the previous section.
### Locating the supply token, borrow token, and borrow position

Identifying the supply and borrow mint addresses lets us label assets that were seized as collateral and repaid as debt for each liquidation. The borrow position links those asset flows to the position being liquidated. 

Each of these addresses is passed into the `Jupiter Lend Borrow: Liquidate` instruction as an argument. On Solscan, these arguments appear under "Input Accounts" when you expand an instruction. Within the canonical transaction, the supply mint, borrow mint, and borrow position address appear at the 7th, 8th, and 14th positions, respectively.

![Supply mint, borrow mint, and borrow-position accounts](<images/Screenshot From 2026-09-22 17-13-47.png>)

https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

This relationship is observable across additional example transactions:

| Transaction                                                                                                                             | Outer instruction index | `account_arguments[7]` supply mint                  | `account_arguments[8]` borrow mint                   | `account_arguments[14]` position               |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------: | --------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------- |
| [Canonical `vaupf...`](https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR)   |           4 | WSOL: `So11111111111111111111111111111111111111112` | USDC: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` | `8W2SoErPPcYvbBvfSBHZECTXsFu8ZSLSYfQkaTatxKVv` |
| [Example 1 `5guPqg...`](https://solscan.io/tx/5guPqgEj9FadRp4A2xJrn2rnBhRpRk4etLxjfYG75z16cZiFiQaqsH91q3XJvvqj3mDCWUEqHck2WG2kmCZ3xrau) |           7 | JUP: `JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN`  | USDC: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` | `227vHKagvMS9qbf8ZAD2GJceGgpKzWrGZJY69J6kA1AB` |
| [Example 2 `3LrpND...`](https://solscan.io/tx/3LrpNDZVxsMAwceue1QRuGAUxa7yajryChcrSUgD7X2g8NVrzQzoZNWbBvTowfP2vJCmnZXJq2bCXN8Vg31sdBNe) |           4 | JUP: `JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN`  | USDC: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` | `227vHKagvMS9qbf8ZAD2GJceGgpKzWrGZJY69J6kA1AB` |
| [Example 3 `3169fy...`](https://solscan.io/tx/3169fyF7pcfUvm2GYUu33o4VQ6BoRyiiEYXt38j4o7JxU3Uo6BMRnpX1XJN8dvdAVjWK6BAaXcV2ukz8xpuxYbdA) |           7 | INF: `5oVNBeEEQvYi1cX3ir8Dx5n1P7pdxydbGF2X4TxVusJm` | USDC: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` | `HuwayEtJX8tCh8VBoTnpPahqsjmxnK1uKMj4uUQ9i8Lt` |

*Note: This assumption does not automatically apply across program upgrades or different instruction definitions.*

The supply and borrow tokens have clear labels. However, account #14, labeled “Vault Borrow Position on Liquidity,” is less descriptive. To determine whether it represents the borrow position, copy its address from Solscan and search for other occurrences on the transaction page.

![Borrow-position address occurrences on Solscan](<images/Screenshot From 2026-09-22 17-28-46.png>)

https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

The same address appeared in two additional instructions labeled “User Borrow Position.” This corroborated the interpretation of account #14 as the borrow-position address in this transaction. I then checked the same account position across additional transactions before using it in the query.

Each of these accounts appears in the `account_arguments` column on Dune:

| Position | Solscan label                                                | Dune expression         | Meaning                 |
| -------: | ------------------------------------------------------------ | ----------------------- | ----------------------- |
|        7 | `Supply Token`                                               | `account_arguments[7]`  | Supply/collateral mint  |
|        8 | `Borrow Token`                                               | `account_arguments[8]`  | Borrow/debt mint        |
|       14 | `Vault Borrow Position on Liquidity`, `User Borrow Position` | `account_arguments[14]` | Borrow position account |

Here's an example query that selects the supply token, borrow token, and borrow position:
```sql
SELECT
	tx_id,
    account_arguments[7]  AS supply_mint,
    account_arguments[8]  AS borrow_mint,
    account_arguments[14] AS position
FROM solana.instruction.calls
WHERE tx_id = 'vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR'
	AND executing_account = 'jupr81YtYssSyPt8jbnGuiWon5f6x9TcDEFxYe3Bdzi'
    AND substr("data", 1, 8) = from_hex('dfb3e27d302e274a')
```
https://dune.com/queries/8822928

 `account_arguments` is an array column containing the accounts. The number within the brackets (e.g., `[7]` or `[8]`) selects an account at a specific index.

Now we have the core metadata for each liquidation.

The current query displays the mint addresses of the tokens. In the second walkthrough, we'll join the price table to translate the addresses into asset names.
## Decoding liquidation amounts

Identifying the debt repaid and collateral seized amounts will reveal the value of each liquidation. 

To locate these values, we'll begin by inspecting the transaction in "Summary Mode" on Solscan. You'll notice that the signer transfers (liquidates) tokens to Jupiter Lend in a dollar-denominated asset like USDC, and then receives (redeems) tokens in WSOL, a volatile asset.

![Debt repayment and collateral received in Solscan transaction summary](<images/Screenshot From 2026-09-22 18-43-21.png>)

https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

These transfers happen within the `Jupiter Lend Borrow: Liquidate` instruction as inner instructions.

To get a closer look at inner instructions, let's scroll down to the "Instruction Details" section and click the down arrow to the right of the instruction's name to reveal them. Inner instructions are nested instructions, commonly known as [cross-program invocations (CPI)](https://solana.com/docs/core/cpi), that complete actions related to the outer instruction call.

For the canonical example, there are six inner instructions nested within the `Jupiter Lend Borrow: Liquidate` instruction. We must locate which inner instructions expose the asset values so we can map them to their columns on Dune.

One thing to keep in mind: an asset's value is expressed in three different formats: the token amount, the raw token amount, and the USD value. Here's an example using the WSOL values from the canonical transaction:

| Representation   | Definition                                                                                                                                                   | Value                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| Raw token amount | Absolute value of the signed integer serialized in the instruction data, expressed in the token's smallest denomination (lamports for WSOL).                 | `1151768749`          |
| Token amount     | Raw token amount divided by `10^decimals` to produce the human-readable token quantity.                                                                      | `1.151768749 WSOL`    |
| USD              | Token amount multiplied by the token's historical USD price at the time of the transfer; this value is derived and is not stored in the instruction payload. | `$245.78` (estimated) |

Solscan lists the USD amounts next to the token amounts in "Summary Mode," but the program itself only outputs raw token amounts. So 246.103542, for example, will appear as 246103542 in the transaction data.

To locate these values, follow these steps:
1. Copy the raw token amount for the debt repaid (liquidate) value, making sure to remove the decimal point. In this case, it's `246103542`.
2. Expand the `#4 - Jupiter Lend Borrow: Liquidate` instruction to reveal its data and inner instructions.
3. Paste the value into the page's search function (Ctrl + F) to locate other places in the transaction where it appears.

The search reveals an inner `Jupiter Lend Liquidity: Operate` instruction containing a negative integer for the debt repaid (`borrow_amount`) and `0` for the collateral seized (`supply_amount`).

The `Jupiter Lend Liquidity: Operate` instruction revealing the debt repaid (`borrow_amount`).
![Debt repaid in a Jupiter Lend Liquidity Operate instruction](<images/Screenshot From 2026-09-22 18-35-51.png>)
https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

*Note: The debt-repaid value also appears in the `debt_amt` field of the `Jupiter Lend Borrow: Liquidate` event data. This provides an independent validation point, but event data is not exposed in the `solana.instruction_calls` table, so the query extracts the amount from the inner `Operate` instruction's `data` instead.*

When we repeat this process for the redeemed (collateral-seized) SOL value, `1151768749`, we find the integer in a subsequent `Jupiter Lend Liquidity: Operate` instruction. This time, however, there's a negative integer for collateral seized (`supply_amount`) and a `0` for the debt repaid (`borrow_amount`) field.

The `Jupiter Lend Liquidity: Operate` instruction revealing the collateral seized (`supply_amount`).
![Collateral seized in a Jupiter Lend Liquidity Operate instruction](<images/Screenshot From 2026-09-22 18-36-03.png>)
https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

This search reveals a clear pattern: debt repaid appears within a `Jupiter Lend Liquidity: Operate` instruction as a negative integer listed under `borrow_amount`, and collateral seized appears within the subsequent `Jupiter Lend Liquidity: Operate` instruction as a negative integer listed under `supply_amount`.

The same field pattern appears across several example transactions:

| Transaction | Outer instruction index | First relevant `Operate` call | Second relevant `Operate` call |
| ----------- | ----------------------: | ----------------------------- | ------------------------------ |
| [Example 1 `5guPqg...`](https://solscan.io/tx/5guPqgEj9FadRp4A2xJrn2rnBhRpRk4etLxjfYG75z16cZiFiQaqsH91q3XJvvqj3mDCWUEqHck2WG2kmCZ3xrau) | 7 | Inner index `4`: non-zero `borrow_amount`, USDC, debt repaid | Inner index `5`: non-zero `supply_amount`, JUP, collateral seized |
| [Example 2 `3LrpND...`](https://solscan.io/tx/3LrpNDZVxsMAwceue1QRuGAUxa7yajryChcrSUgD7X2g8NVrzQzoZNWbBvTowfP2vJCmnZXJq2bCXN8Vg31sdBNe) | 4 | Inner index `4`: non-zero `borrow_amount`, USDC, debt repaid | Inner index `5`: non-zero `supply_amount`, JUP, collateral seized |
| [Example 3 `3169fy...`](https://solscan.io/tx/3169fyF7pcfUvm2GYUu33o4VQ6BoRyiiEYXt38j4o7JxU3Uo6BMRnpX1XJN8dvdAVjWK6BAaXcV2ukz8xpuxYbdA) | 7 | Inner index `4`: non-zero `borrow_amount`, USDC, debt repaid | Inner index `5`: non-zero `supply_amount`, INF, collateral seized |

The two amount-bearing `Operate` calls in the canonical liquidation context are:

| Outer instruction index | Inner instruction index | Instruction                       | `supply_amount` | `borrow_amount` | Token | Economic meaning  |
| ----------------------: | ----------------------: | --------------------------------- | --------------: | --------------: | ----- | ----------------- |
|                       4 |                       4 | `Jupiter Lend Liquidity: Operate` |             `0` |    `-246103542` | USDC  | Debt repaid       |
|                       4 |                       5 | `Jupiter Lend Liquidity: Operate` |   `-1151768749` |             `0` | WSOL  | Collateral seized |

Since these are raw base unit values, `246103542` represents `246.103542 USDC`, while `1151768749` represents `1.151768749 WSOL` after applying each token's decimals.

*Note: The raw amount must be divided by `10^decimals` for the asset and then multiplied by its historical price to determine its USD value.*

These values are recorded as serialized arguments in the instruction's data payload, which appears after the 8-byte discriminator. To view the serialized payload for the instruction on Solscan, select the "Raw" toggle in the upper-right corner of each `Jupiter Lend Liquidity: Operate` instruction.

![Serialized Operate instruction payload in Solscan](<images/Screenshot From 2026-09-24 14-47-31.png>)

https://solscan.io/tx/vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR

In the canonical example, the full data payload for the `Jupiter Lend Liquidity: Operate` instruction containing debt repaid (`borrow_amount`) appears as:
`d96ad06374972a87000000000000000000000000000000000ac254f1ffffffffffffffffffffffff65f5dffd7c84af75a8a5f7bdcea1622e2b3abf87fc53a871b908561a3a8b1bde65f5dffd7c84af75a8a5f7bdcea1622e2b3abf87fc53a871b908561a3a8b1bde01`

Here are the specific bytes that each value maps to:

| Bytes  | Field           | Data type    | Size / encoding                         | Raw value                                                          |
| ------ | --------------- | ------------ | -------------------------------------- | ------------------------------------------------------------------ |
| 1-8    | `discriminator` | [u8; 8]      | 8 bytes                                | `d96ad06374972a87`                                                 |
| 9-24   | `supply_amount` | i128         | 16 bytes, little-endian signed integer | `00000000000000000000000000000000`                                 |
| 25-40  | `borrow_amount` | i128         | 16 bytes, little-endian signed         | `0ac254f1ffffffffffffffffffffffff`                                 |
| 41-72  | `withdraw_to`   | Pubkey       | 32 bytes                               | `65f5dffd7c84af75a8a5f7bdcea1622e2b3abf87fc53a871b908561a3a8b1bde` |
| 73-104 | `borrow_to`     | Pubkey       | 32 bytes                               | `65f5dffd7c84af75a8a5f7bdcea1622e2b3abf87fc53a871b908561a3a8b1bde` |
| 105    | `transfer_type` | TransferType | enum variant                           | `01`                                                               |

The `Jupiter Lend Liquidity: Operate` instruction data lives in the `data` column of the `solana.instruction_calls` table. We can filter specific byte indexes to extract the values for `supply_amount` and `borrow_amount`.

Here's how each of the observed fields from Solscan map to Dune:

| Solscan observation                                       | Solana interpretation                                             | Dune representation                                                 |
| --------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| `Jupiter Lend Liquidity` program label                    | Program that executed the inner call                              | `executing_account = 'jupeiUmn818Jg1ekPURTpr4mFo29p46vygyykFJ3wZC'` |
| `operate` instruction                                     | Anchor instruction identified by its discriminator                | First 8 bytes of `data` equal `d96ad06374972a87`                    |
| `supply_amount` field in the raw payload                  | Signed `i128` serialized in little-endian byte order              | `substr(inner_data, 9, 8)`                                          |
| `borrow_amount` field in the raw payload                  | Signed `i128` serialized in little-endian byte order              | `substr(inner_data, 25, 8)`                                         |

Here's a query that exposes the raw `operate` payloads, identifies where the `supply_amount` and `borrow_amount` fields are stored, and converts those fields to positive raw integer values:

```sql
SELECT
    block_time,
    tx_id,
    outer_instruction_index,
    inner_instruction_index,
    to_hex(substr("data", 1, 8)) AS instruction_discriminator,

    ABS(
        CAST(
            CAST(
                from_big_endian_64(
                    reverse(substr("data", 9, 8))
                ) AS DECIMAL(38, 0)
            ) AS DOUBLE
        )
    ) AS supply_amount,

    ABS(
        CAST(
            CAST(
                from_big_endian_64(
                    reverse(substr("data", 25, 8))
                ) AS DECIMAL(38, 0)
            ) AS DOUBLE
        )
    ) AS borrow_amount,

    "data" AS inner_data
FROM solana.instruction_calls
WHERE tx_id = 'vaupfNDZKX9siireKzdK63ZVpqzJMxarsw3LWeBdSZuRMHTFptd2soXiYaRq2nMgtK5X24YAniBsPyrcLYWnUpR'
  AND outer_instruction_index = 4
  AND inner_instruction_index IS NOT NULL
  AND substr("data", 1, 8) = from_hex('d96ad06374972a87')
ORDER BY inner_instruction_index;
```

The query extracts the first 8 bytes of the instruction data and displays them as the instruction discriminator.
```sql
to_hex(substr("data", 1, 8)) AS instruction_discriminator
```

Next, it extracts the first 8 bytes of the supply amount field and converts the serialized data into an integer:
```sql
    ABS(
        CAST(
            CAST(
                from_big_endian_64(
                    reverse(substr("data", 9, 8))
                ) AS DECIMAL(38, 0)
            ) AS DOUBLE
        )
    ) AS supply_amount,
```

Here's an explanation of what this is doing, starting from the innermost clause:
- `substr("data", 9, 8)` extracts the 8 bytes containing the supply amount.
- `reverse(...)` reverses the byte order because the value is stored in little-endian format.
- `from_big_endian_64(...)` reads the reversed bytes as a 64-bit integer.
- The live query reads only the lower 8 bytes of each 16-byte `i128` field. This works for the observed amounts because they fit within signed 64-bit range and the remaining bytes are sign extension; the full 16-byte fields should be inspected before applying the shortcut to larger values.
- `CAST(... AS DECIMAL(38, 0))` converts the result to a precise whole-number decimal; `38` allows up to 38 total digits and `0` allows no digits after the decimal point.
- `CAST(... AS DOUBLE)` converts the decimal to a floating-point number for later arithmetic, but floating-point conversion can lose precision for sufficiently large raw amounts.
- `ABS(...)` removes the negative sign and returns the positive amount.
- The serialized amount is signed, so the negative value must be interpreted before `ABS()` is used to present a positive analytical magnitude. The canonical transaction has a negative `borrow_amount` for debt repayment and a negative `supply_amount` for collateral leaving the lending position.
- `AS supply_amount` names the resulting column `supply_amount`.

The same process is used for the debt side, starting at byte 25:
```sql
    ABS(
        CAST(
            CAST(
                from_big_endian_64(
                    reverse(substr("data", 25, 8))
                ) AS DECIMAL(38, 0)
            ) AS DOUBLE
        )
    ) AS borrow_amount,
```

Lastly, this query keeps only inner instructions and excludes outer instruction rows.
```sql
AND inner_instruction_index IS NOT NULL
```

In part two, we rank the inner `Jupiter Lend Liquidity: Operate` instructions and join them to the token metadata from the [`prices.hour`](https://dune.com/data/prices.hour) table to capture the instruction positions and transform the raw supply amount into a USD value.
## Conclusion

This walkthrough established how to map transaction fields from Solscan to Dune's `solana.instruction_calls` table and decode signed raw amount fields from the canonical liquidation.

In part two, we'll walk through the reusable query that combines all of these components. 
