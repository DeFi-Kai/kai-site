+++
date = '2026-03-15T09:00:00-05:00'
draft = false
title = 'Building a Local AI System to Stay Ahead of the Crypto News Cycle'
+++

{{< img src="images/building-local-ai-system/hero.png" alt="Local AI system overview" >}}

As a Research Analyst I've struggled to keep up with current events while working on reports.

For starters, there are so many aspects to screening a business, and deep research requires you to understand the nuances of a project from a technical, financial, and microeconomic standpoint.

Imagine splitting your time cycling through onchain data to visualize economic flow, reading whitepapers to model a project's mechanics, and comparing sector competitors. Meanwhile, Trump announces another tariff which triggers mass liquidations, or a new stablecoin bill is passed making your overall thesis invalid.

In one day (or in a matter of a few hours), the structure and sentiment of this market can drastically change.

Not to mention, if you're a brave soul that attempts to keep up with news during an active research project you might fall victim to excessive [context switching](https://pubmed.ncbi.nlm.nih.gov/11518143/), [information overload](https://www.sciencedirect.com/science/article/pii/S2667096824000508), or overall mental fatigue -- or at least that's what happens in my case.

To overcome this, I vibecoded [an AI research assistant](https://defi-kai.github.io/kai-site/briefs/latest/) to keep me up to date with the latest news in crypto and finances in around 20 minutes reading time -- down from 1-2 hours. It runs on locally hosted models including OpenAI's GPT OSS 20b, and Deepseek R1 via LM studio.

This system allows me to spend more time studying topics deeply, while keeping an eye on the broader market and any catalysts that could provide valuable context to my current project(s).

The goal isn't for AI to do the thinking for me, but rather, to surface insights (with more signal than noise) that help me stay in the know or serve as leads.

## What's included

I put a lot of thought into recalling the existing processes and resources I use to gather news, which led me to build the following sections:

- Market Overview / Hero Section
- Sentiment
- DeFi Overview
- Crypto Trading Volume
- Charts
- Headlines
- Governance Forums
- Watchlist
- Trend Analysis

### Market overview / hero section

The market overview gives me a high-level snapshot of the most important events and metrics across crypto.

For this section, GPT OSS 20b ingests news from all of the approved sources, ranks each item based on my priorities (stated within the prompt) and outputs an executive summary. While It's not possible to cover ALL news in a summary, this section is designed to improve the signal to noise ratio so I can see the most meaningful headlines early on.

{{< img src="images/building-local-ai-system/market-overview.png" alt="Market overview section" >}}

### Sentiment section

The fear & greed index has been widely used throughput the industry to get a rough gauge on how people are feeling in the market.

I take this into account with the rest of the news to see if it holds true, or if there are potential dislocations in asset prices. But, I don't use this as an end-all-be-all indicator.

{{< img src="images/building-local-ai-system/sentiment-fear-greed.png" alt="Fear and greed sentiment section" >}}

Below this, I included a Reddit sentiment section to understand sentiment of the "marginal buyer". It scrapes a list of subreddits organized by tiers, and outputs an aggregate fear & greed score.

This section is still very much a work in progress (WIP), however its helped keep me up to date with the latest happenings across subreddits I care about. In the future, I plan to improve the logic for deciding which posts to fetch, redesign the tier list of subreddits, and improve the prompts.

{{< img src="images/building-local-ai-system/reddit-sentiment.png" alt="Reddit sentiment section" >}}

### DeFi overview section

This section shows a snapshot of open interest across perp dexes and total outstanding loans across all lending markets. This helps me guage the interest on leveraged products and serves as a proxy for the markets appetite for speculation.

In addition, the top blockchains are displayed by 24 hour shifts in TVL, to keep me up to date on any sizable inflows/outflows.

{{< img src="images/building-local-ai-system/defi-overview.png" alt="DeFi overview section" >}}

Below this, the "protocol movers" section gives a quick glimpse of which DeFi protocols made or loss money. It also displays shifts in stablecoin liqudity to help me understand whether the market is growing, beyond speculation.

{{< img src="images/building-local-ai-system/protocol-movers.png" alt="Protocol movers section" >}}

### Crypto trading volume

This section tracks crypto trading volumes across CEXes and DEXes to help indicate whether speculation is growing or slowing down.

{{< img src="images/building-local-ai-system/trading-volume.png" alt="Crypto trading volume section" >}}

Below that, the DEX to CEX ratio indicates whether volume is leaning more towards onchain DEXes or CEXes. Growth in onchain DEX volume could signal a paradigm shift in the primary rails used for trading, which could re-rate some onchain businesses.

### Charts section

In a market that moves as fast as crypto a sharp rise or drop in prices of major assets, alone, can decide the sentiment of the crypto market for the day.

Personally, I lean less towards trading regularly, however, it's still important to know the prices of assets to fully understand the state of the market. To achieve this, I fetch charts using the Trading View API.

For this section, the script takes screenshots of each chart using Playwright and passes the images to Gemma 3 12b to print key price points so I can have exact prices and better understand the range assets are trading within.

The main question this helps me answer is "are people overreacting or rightfully passionate?". You can also open this tab side by side with an article for a quick reference when checking prices of assets referenced within whatever you're reading.

{{< img src="images/building-local-ai-system/charts-section.png" alt="Charts section" >}}

### Headlines

When I thought about how I usually discover news, I realized that it's either through 1) a list of bookmarked websites or 2) searching key terms on a SERP like Google.

For the first method, I simply gathered RSS feeds of all the websites in my bookmarks and setup the Python script to fetch the markdown using the Jina API. And for the second method I tried to replicate my natural process by compiling common seaches/keywords which are then served to the Brave API to fetch links. This list includes keywords like "crypto regulation", and "stablecoins".

{{< img src="images/building-local-ai-system/headlines-section.png" alt="Headlines section" >}}

### Governance forums

A project's governance forum is where important structural or financial business decisions are announced and discussed. Catching wind of an early proposal on one of these forums can help you to make decisions before crowds that rely strictly on Reddit and Twitter for new information.

{{< img src="images/building-local-ai-system/governance-forums.png" alt="Governance forums section" >}}

### Watchlist

The watchlist section takes a CSV input containing my bull & bear case scenario, and invalidation criteria for my portfolio/watchlist assets. The python script takes the inputs directly from the CSV fields, appends the text inputs to create queries, and then sends them to the Brave API to perform a SERP search.

Next, the system pulls the resulting articles as markdown, combines it with Reddit and Discourse data on the subject, and serves it to the LLM to synthesize it and output structured summaries.

For this section I used Ethereum and Solana as examples, and in the future I plan to incorporate data from DeFillama and Coingecko so I can incorporate and track figures within my theses.

In the future I plan to use a larger AI model so I can prompt it to produce search queries rather than using deterministic strings (i.e. {project name} {bull case}).

{{< img src="images/building-local-ai-system/watchlist.png" alt="Watchlist section" >}}

### Trend analysis

For this section, all summaries and titles from the above sections are ingested into a vector database via Chroma. The resulting embeddings are queried to "identify top cross-source trends" based on a prompt. The LLM returns a structured list of trends which include the category of news, the trend, and the LLMs confidence in the trend, along with sources.

{{< img src="images/building-local-ai-system/trend-analysis.png" alt="Trend analysis section" >}}

In the future I plan to extract more trends, and then run additional searches on them to pull more context about emerging trends.

## How does it work?

Everyday at 6AM ET a cron job runs multiple Python scripts that fetch content from a curated list of RSS feeds, APIs, SERP searches, and online forums. Each piece of content is converted to markdown via the Jina API and then served up to an LLM with a structured prompt to print summaries.

For some sections, like "Headlines", It processes each piece of content separately. In contrast, sections like the hero summary and "trends analysis", combine the context of multiple markdown files to produce a single output.

These scripts pull from the following sources:

- DeFillama API
- Coingecko API
- Reddit API
- Brave API
- Discourse API
- CSV input (watchlist)
- The fear & greed index API

For the content processing stage I decided to use all locally hosted models via LMStudio. This helps me ensure that any manual inputs and all outputs stay on my local machine, and only touch the internet if I need them to.

The models used in this project include:

- GPT OSS 20b by OpenAI
- Gemma 3 12b IT by Google
- Deepseek R1 0528 Qwen3 8b by Deepseek

For reference, this is my setup:

- Ryzen 7 3700x
- Nvidia RTX 3060 (12gb)
- 32 gb  DDR4 RAM
- Samsung 500gb V-NAND SSD

While it's a modest setup, it's surprisingly efficient. Using GPT OSS 20b with 100k to 150k context, can generate ~40 tokens/ second. Definitely not as fast as a model running on OpenAIs servers, but still faster than a human can read.

The result is a compact summary with all the information necessary for understanding the past 24 hours in crypto.

All runs, sources and responses are stored in an SQLite database, and persisted as embeddings via ChromaDB so that I can query in the future. This lets me inspect the results from previous entries to identify trends and other anomalies i may not have noticed otherwise.

While I am currently publishing the output publicly, this project is still in its first stages. Eventually, I intend to expand the featureset, and datasoruces of this system and keep the full output on my local machine so I don't leak alpha.

Still, this is in its early stages and there is more work to do to make it truly reliable.

## Challenges & lessons

To build this, I used Claude Opus 4.5 from Anthropic to help me draft a spec. I passed those instructions to the Codex model from OpenAI configured with OpenCode's TUI tool.

Altogether, this project took a few weeks to produce reliable outputs. Along the way, I've learned a few lessons that I will be implementing into my vibecoding process going forward. Here are a few:

- **Build a library of APIs and data sources:** AI can help you find data sources and APIs, however, this is one of the most important parts of the project to configure so you should have a good understanding of the exact data you need. Even if AI gives you suggestions, you should create a repository of all the sources and what you're able to derive from them. This helps limit token usage, gives you the knowledge to audit outputs, and ultimately helps you build it faster.
- **Prompt structuring:** Creating a structured prompt plan using an agent before you build it. Using exact names of libraries/dependencies in the prompt. Similar to databases, knowing specific tools will help put your project closer in the intended direction.
- **Documentation:** Create a rough to-do list to track all the features you'd like to implement. This serves as your road map and if you include all relevant context and details you can give this list directly to an agent.
- **Unit tests:** When you're adding a new data source prompt the agent to create separate scripts that test individual features. LLMs will confidently summarize bad data, so you won't catch ETL failures from the output alone. Test each data source's fetch, transform, and load steps independently before anything touches the model.

Although, this does not fetch from X (formerly Twitter), I tend to spend much of my free time on there already so I'm fine with reading news directly from the X app, for now.

## Closing thoughts

So far, reading this summary every morning provides a moderate foundation for staying in the loop in an industry that moves fast.

Over the next few months I want to fine tune the outputs, which could be done by adjusting different settings, including:

- The parameters of the LLM (temperature, reasoning level, context window, etc.)
- The chunking strategy, which controls how much of the markdown content is ingested into the LLM
- The prompts that are responsible for turning the input into outputs
- The news sources and rules for selecting news articles
- The news sources and rules for selecting websites

But no amount of parameter tuning matters if you don't know what good output looks like.

The most important skills a human can add to an AI workflow is oversight and the taste to curate systems & data to produce meaningful connections or insights.

Since AI agents allow you to vibecode projects in days which previously would've taken weeks, coding skills are no longer the bottleneck. Instead, the biggest hurdle is you're understanding of the problem you're solving.
