+++
date = '2026-11-16T09:00:00-05:00'
draft = false
title = 'How to Write With AI Without Letting It Write for You'

[cover]
image = 'images/writing-with-llms/cover.png'
alt = 'Screenshot of an early draft of Why I still draft in the age of AI'
hiddenInSingle = true
hiddenInList = true
+++

When ChatGPT launched in 2022, my employers encouraged us to experiment with it, so I started using it to generate first drafts. I came into it with high hopes that I could 10x my productivity. But when I read through the drafts, it didn't sound like me and I didn't agree with half the arguments. I'd edit them, and by the time I finished rewriting paragraphs, I realized I could've just written it myself. 

If AI couldn't draft for me, maybe it was a better editor? So I tried writing everything myself and using AI only for editing. But that created another problem. When I asked it to revise an entire draft in one sweep, it would strip away my ideas and change the way said things.  

My best results came when I stopped handing over entire tasks to AI. Instead of giving it a prompt and letting it run wild, I started assigning it a specific role at each stage of writing. For drafting, I found that AI could ask questions that helped me develop my own ideas. Editing was another story. I found that it worked better when I separated it into three stages: developmental editing to question my arguments, line editing to identify opportunities to improve flow, and copy editing to catch grammar and punctuation mistakes.

This approach keeps me involved in the thinking and decisions while using AI to support different parts of the writing process. It can make the process faster but it isn't a shortcut around thinking. Keep in mind that the more decisions you hand over to AI, the more likely you are to produce slop.

I’ll walk through each stage of my long-form writing process, explaining where I’ve found AI most useful and sharing the prompts and tools I use. **You can also find the complete collection of prompts on [GitHub.](https://github.com/DeFi-Kai/writing-with-llms-toolkit/tree/main)**
## Drafting & outlining  

The first stage of writing is exploratory: you record your rough thoughts and figure out what you're really trying to say. As you develop those notes, they'll become your draft.

Begin with a brain dump: write down all your thoughts and motivations related to the topic. Then spend at least another session reviewing your notes and rewriting the ideas that are the least clear until they reflect your actual viewpoint. The rewrite will help you understand your own position before being influenced by AI.

This may seem counterproductive since the goal is to use AI to speed things up, but there are some parts of writing you just can't skip. As [Paul Graham](https://paulgraham.com/read.html) puts it:

> There is a kind of thinking that can only be done by writing.

The notes you produce in this stage give AI more original context to work with. They also give you a reference for judging whether its suggestions reflect your intended argument.

Once you have a working title and rough notes, it's time to consult AI so that you can test your initial position and develop your draft.

I created a three-phase prompt to help you develop and organize your ideas through guided questions. By the end, it produces an outline and organizes the material you've written into the appropriate sections.

To begin, paste the prompt into your chat with the following inputs:

- Topic (required) - The working title of your article.
- Article type (required) - The type of writing (e.g., personal essay, case study, or tutorial).
- Intended audience (required) - Who you're writing for (e.g., developers, project managers, or people curious about AI).
- Rough notes (required) - Your initial brain dump of ideas.

{{< prompt summary="View the editorial planning prompt." >}}
# Editorial Planning Partner

Act as my editorial planning partner. Help me discover the strongest ideas for an article and collaboratively develop an outline for the full piece. I want to do the actual writing myself.

I'll provide the topic, article type, intended audience, and rough notes. Use my rough notes to build on what I've already figured out. Ask questions that help me develop an idea, test an assumption, or find a concrete example.

## Phase 1: Generate a writing worksheet

Generate 5–6 thoughtful questions tailored to the article. The questions should help me explore:

- What motivated me to write about this topic.
    
- What problem, question, or observation the article addresses.
    
- What experiences, research, or evidence inform my perspective.
    
- What I discovered, found surprising, or learned through the process.
    
- What assumptions, tensions, or tradeoffs make the subject interesting.
    
- What the intended audience already knows and what they need to understand.
    
- What distinctive insight or practical value the article offers.
    

Adapt the questions to the article type:

- **Technical case studies:** Problems, implementation decisions, difficulties, and reusable lessons.
    
- **Personal essays or opinion pieces:** Motivations, experiences, changing beliefs, and insights.
    
- **Research and analysis:** Research questions, evidence, findings, assumptions, and implications.
    
- **Tutorials:** Reader problems, prerequisites, approaches, and practical outcomes.
    

Avoid redundant or generic questions. Present them together in a clean, copyable format so I can answer them independently in my text editor.

## Phase 2: Collaboratively explore my answers

When I return with my answers:

1. Identify the most interesting observations, arguments, tensions, and connections.
    
2. Highlight anything that feels conventional, unsupported, repetitive, or insufficiently developed.
    
3. Ask targeted follow-up questions when necessary to deepen my thinking.
    
4. Help me consider what the reader already knows, what would capture their interest, and what information they need to follow the article.
    
5. Discuss potential angles with me rather than immediately deciding on one.
    

Treat this as a collaborative editorial discussion. Challenge my reasoning constructively, but don't impose your own interpretation or invent insights.

Help me distinguish between ideas that are central to the article, supporting details, and background information that may be unnecessary.

Summarize the possible angle or angles, the value to the intended reader, and the strongest material I've already supplied.

Ask up to three follow-up questions total during Phase 2, all in one batch. Only ask questions whose answers could change the article's angle, scope, or main claim. Once I've answered, summarize where we landed and flag any remaining gaps. Ask another round only if I request one.

Once this phase is complete, give me a short, copyable planning note. Include the angle I chose, what I want the reader to get from the article, specific passages or examples from my notes and answers that I might use, and any open questions worth carrying forward. I'll take the note back to my text editor.

Pause here and wait for me to return with a rough outline or ask you to suggest one.

## Phase 3: Collaboratively develop an article outline

When I return with a rough outline or ask you to suggest one, use the planning note if we have one, along with the material I've shared.

If I share a rough outline, a list of section headings, or a partial structure, use it as the starting point. Work with me to develop it into a section-level outline for the full article.

If I haven't shared an outline or headings, propose a section-level outline based on my working angle, intended audience, and the material I've shared. Offer a second structure only if it gives the reader a meaningfully different way into or through the piece. If you offer two, explain what each does well and what tradeoff it involves. Let me choose which structure to develop.

For either starting point, help me:

- Identify the major sections of the article, including the introduction and conclusion where appropriate.
    
- Define what each section should accomplish for the reader.
    
- Define the main idea of each section and identify the key arguments or supporting points it should cover.
    
- Where I have already written relevant prose, place it directly under the appropriate section heading, preserving my original wording. Don't paraphrase, rewrite, or expand my writing without permission.
    
- Explain how the sections connect and how the argument or narrative progresses.
    
- Flag gaps that need more thinking, research, or evidence.
    
- Identify sections I could cut or combine.
    

For the introduction, discuss what it needs to accomplish and suggest possible opening angles suited to the article type and audience. Don't draft the introduction for me.

Keep the outline at the section level. You may organize prose I've already written, but leave all new article prose to me.

Work with me to revise the outline. Ask questions and discuss alternatives where they help me decide what to include and how to organize it. Stop once I'm satisfied with the outline and ready to draft.

Once I'm satisfied with the structure, give me the agreed outline in one clean, copyable block. For each section, include:

- **Main idea:** The central point the section should communicate.
    
- **Existing material:** Relevant prose I've already written in my notes, worksheet responses, or drafts, placed under the appropriate heading without rewriting it.
    
- **Gaps:** Ideas, explanations, examples, or evidence I still need to develop.
    

Preserve my original wording and leave gaps where additional writing is needed rather than filling them with AI-generated prose. Then stop so I can take the outline back to my editor and complete the draft.

## Editorial principles

- Prioritize substance, specificity, and intellectual curiosity.
    
- Preserve my voice and responsibility for developing the argument.
    
- Don't force contrarian takes, personal anecdotes, or provocative hooks.
    
- Avoid clichés and formulaic writing advice.
    
- Help me uncover the most valuable ideas rather than merely making them sound impressive.
    
- Adapt to my article and my answers rather than following a rigid formula.
    
- Don't write new sentences or paragraphs for the article unless I explicitly request them.
    
- Don't rush to organize ideas before we've explored them sufficiently.
    

**Important:** Don't rush through the phases. The process should remain collaborative.

If I specify a stage, start there using the material I provide. Otherwise, begin with the worksheet. Work through one stage at a time. I can skip a stage, return to an earlier one, or bring an existing outline for review.
{{< /prompt >}}
*[View this prompt on GitHub.](https://github.com/DeFi-Kai/writing-with-llms-toolkit/blob/main/prompts/editorial-planning/prompt.md)*

Here's how the three phases work:

**For the first stage,** AI gives you tailored questions, which you copy into your editor (Google Docs, Obsidian, etc.) and answer independently. The questions help you discover what you think and identify ideas you haven't explored. Your answers also provide the LLM with more original context.

For example, while planning my [case study on building an AI-assisted analytics pipeline](https://defi-kai.github.io/kai-site/work/building-an-agentic-pipeline-for-onchain-analytics/), I received a question that helped me consider what readers might learn from my experience:

{{< img src="images/writing-with-llms/editorial-planning-worksheet.png" alt="Writing worksheet response about reader assumptions and context management in an analytics pipeline" >}}

Answering this question helped me recognize that readers might already know Claude can generate SQL queries, but might not understand the challenges of managing documentation and context. I incorporated that insight into the introduction and used it to develop the [**Context management and resource selection**](https://defi-kai.github.io/kai-site/work/building-an-agentic-pipeline-for-onchain-analytics/#context-management-and-resource-selection) subsection explaining my approach to context management.

**For the second stage,** you bring your responses back to the chat. AI helps you examine connections, weak points, and possible angles by asking up to three follow-up questions. After testing your reasoning, you'll choose a working direction and leave with a planning note. You can use that note to sketch your own outline or have AI create one in the next stage.

**For the third stage,** you and AI review the order of your outline and identify where your existing material belongs. The goal is to organize your ideas into a coherent argument. The prompt then outputs each section's main idea, your existing prose under the appropriate headings, and any gaps you still need to fill.

---

After you've worked through the prompt, your job is to complete the draft by developing each section around its main idea. At this point, you should have enough material to develop those ideas yourself.

Some rough notes can become prose, while other fragments might inspire new ideas or shape a section's direction.

You don't have to follow these phases in a strict order. Feel free to use individual phases of the prompt depending on your needs. Sometimes you outline while drafting. Other times you draft first and adjust your outline later. The writing process isn't always linear.

As you fill in the draft, you might stumble on an idea that AI's questions never prompted. If that idea significantly changes the direction of your article, consider revisiting your original plan.

You may also need to consult AI for research or data analysis during drafting. It's OK to use AI to help surface the information, but don't let those tasks turn into AI creating content for you.

## Editing workflow

Once you have a first draft, it's time to edit. The process is traditionally broken into three stages:
1. **Developmental editing:** are arguments coherent and are ideas in the right order?
2. **Line editing:** am I saying things in the right style?
3. **Copy editing:** are there any technical mistakes (grammar, punctuation, etc.)?

Beyond AI suggestions, you should regularly read your draft aloud to spot awkward or unnecessary passages. You should also have a friend or, preferably, a professional editor read it. You're likely too close to your own work to catch every mistake. And after all, you're writing for humans, so you should get their feedback whenever you can.

Let's walk through each stage of the editing process. 
### Developmental Editing 

During developmental editing, you strengthen your arguments and reasoning.

Each paragraph should contribute an idea that the surrounding paragraphs don't. Similarly, each sentence should add something new.

Ann Handley paints a great picture of how to think of this process in her book "Everybody Writes": 

> Think of the sentences in a paragraph as a conversation between an elderly, companionable couple. They don't talk over each other; they expand or elucidate what the other before them said.

The prompt is designed to turn AI into a collaborative developmental editor that identifies weaknesses in your arguments and reasoning. It lists critical issues before optional improvements and provides actionable suggestions while leaving you in control of the revisions.

To begin, enter the prompt with the following inputs:
- Title (required) - The working title of your article.
- Central idea (required) - The main argument or takeaway you want readers to understand from the entire article.
- Outline (required) - A list of the article's section headings in order, showing its overall structure.
- Section to review (required) - The draft text of the section you want AI to evaluate.

{{< prompt summary="View the developmental editing prompt." >}}
# Developmental Editing Partner

Act as my developmental editor for an article I'm writing. Your job is to help me strengthen my ideas, arguments, and organization through constructive criticism and discussion.

I'll provide the article's title, central idea, outline, and the section I want to review.

**Article context:**

- **Title:** [Insert title]
- **Central idea:** [What is the main argument or takeaway?]
- **Outline:** [Paste section-level outline]
- **Section to review:** [Paste draft]

## What to evaluate

Focus on the substance and logical progression of the writing, rather than grammar or sentence-level polish.

**1. Arguments and reasoning**

- Is the section's central idea established early enough for readers to understand where the argument is going?
- Are my ideas clear, logical, and sufficiently developed? 
- Are there gaps in reasoning, unsupported assumptions, or conclusions that don't follow from the evidence? 
- Can a reader unfamiliar with the topic follow my reasoning, or am I assuming knowledge, skipping explanations, or making connections that aren't obvious? 
- Where would additional explanations, concrete examples, analogies, or counterarguments strengthen the section? 

**2. Relevance and redundancy**

- Does each paragraph contribute something meaningful to the section's purpose and the article's central idea?
- Is any information unnecessary, repetitive, or better suited to another section?
- Are some ideas underdeveloped or overexplained?

**3. Organization and flow**

- Are the ideas presented in a logical and effective order?
- Does each paragraph build on, clarify, or meaningfully extend the previous one?  
- Are there abrupt transitions, missing connections, or points that would work better in a different order?  

## How to provide feedback

Start with a brief assessment of what's working and what most needs improvement.

Organize your suggestions into two levels:

**Critical issues:** Problems that meaningfully weaken the argument, create confusion, undermine the section's purpose, or disrupt its logical progression.

**Optional improvements:** Changes that could improve clarity, persuasiveness, or organization but aren't necessary for the section to work.

Prioritize issues affecting the argument, structure, and reader comprehension over smaller improvements. Focus on changes that would make a meaningful difference to the section as a whole.

Don't manufacture issues or optional suggestions to fill either category.

For each issue, provide:

1. **Location:** Identify the specific paragraph, sentence, or passage where the issue occurs. 
2. **Issue:** Explain what's wrong and why it matters.
3. **Suggested fix:** In 1–2 sentences, explain how I could address the issue, including where to add, remove, expand, or reorganize material.

Keep the initial feedback concise, focusing on the 3–5 most consequential issues. If fewer issues warrant attention, report fewer.

## How to collaborate

After providing feedback, let me decide how to proceed. I may:

- **Discuss or challenge your suggestions.** Defend your reasoning, acknowledge valid counterarguments, and explore alternatives with me. Don't automatically agree with my objections.
- **Submit a revised version.** Reevaluate the section, focusing on whether the previously identified issues have been resolved and whether the revisions introduced new problems.

Maintain a concise record of unresolved critical issues within the conversation, rather than repeating the entire feedback history. Mark issues as resolved when appropriate and don't reopen them without a substantive reason.

Continue this process until the section has no significant developmental issues or I decide to move on.

## Important guidelines

- Be constructively critical, not agreeable for the sake of it.
- Preserve my intended meaning and voice.
- Don't rewrite the section or develop my arguments for me. Propose possible approaches instead.
- Distinguish genuine problems from subjective editorial preferences.
- Don't focus on grammar, punctuation, or stylistic polish unless they interfere with understanding.
- Don't force changes where the writing already works.
- I make the final editorial decisions. Your job is to challenge and strengthen my thinking, not replace it.
{{< /prompt >}}
*[View this prompt on GitHub](https://github.com/DeFi-Kai/writing-with-llms-toolkit/blob/main/prompts/developmental-editing/prompt.md)*

Since the prompt involves back-and-forth discussion, start a new chat for each section to refresh context. Otherwise, a long conversation about your introduction could influence the feedback you receive on another section.

The goal of this prompt is to have AI push your thinking and help you fill gaps. But if it misinterprets your argument, it's your job to steer it in the right direction so its advice reflects what you're trying to say.

#### Developmental editing in practice

I used the developmental editing prompt to revise the **Drafting & outlining** section. I wanted to explain why developing your own thoughts gives AI original ideas to work with, but the prompt helped me catch an overstatement.

**Original passage:**

> The more accurate information you give it, the more original context it has to interpret and respond to, without creating its own.

**AI feedback (excerpt):**

> Even with detailed notes, AI can introduce assumptions, interpretations, and ideas you never intended. Your notes give it a stronger foundation; they don't eliminate the need to evaluate its output.

**My first revision:**

> The more accurate information you give it, the more original context it has to interpret and respond to, and the less arguments it creates its own.

**AI feedback after my first revision (excerpt):**

> One other qualification: I'd avoid claiming that better context means AI creates fewer arguments of its own. That may happen, but it's not guaranteed. The stronger claim is that detailed context gives you a better foundation for evaluating whether AI's suggestions represent your intended argument.

**My second revision:**

> The more original context you give it helps it establish a stronger foundation for AI to respond. It also serves as a reference point for whether AI's suggestions represent your intended argument.

**My final revision (after reading aloud, changing surrounding paragraphs, and line editing):**

> The notes you produce in this stage give AI more original context to work with. They also give you a reference for judging whether its suggestions reflect your intended argument.

The human-perspective is also important. I worked with my friend and my mother (<3) to revise my introduction. 

My friend suggested starting with my experience rather than the opening question. He also encouraged me to think about the emotions people have about AI. 
{{< img src="images/writing-with-llms/friend-introduction-feedback.png" alt="A friend's document comment suggesting a stronger opening based on personal experience" >}}
### Line Editing 

This is the stage where you improve how you're saying things, focusing mainly on prose. You shouldn't aim to replace every sentence. Instead, spend time improving the sentences that sound off or awkward.

The prompt is designed to identify opportunities to improve sentence flow and transitions between paragraphs while preserving your voice and intended meaning. Rather than rewriting the entire section, the AI highlights specific passages, explains what could be improved, and suggests targeted edits for you to review.

The prompt gives you more options to consider. You may leave some suggestions on the table. That's totally normal. Ultimately, you should only adopt changes you can stand behind 100%.

The prompt takes the following inputs:
- Section (required) - The section of writing you want the AI to review.
- Context (optional) - The section's purpose, intended audience, or surrounding paragraphs.
- Writing sample (optional) - An excerpt from a previously completed piece that represents your writing style.
- Style guide (optional) - Guidelines for prose style, word choice, sentence structure, and line editing.

{{< prompt summary="View the line editing prompt" >}}
# Role: Line Editing Partner

Act as my line editor. Help me improve the clarity, concision, and flow of my writing while preserving my voice, intended meaning, and writing style.

I'll provide a section of an article for review. Your job is to identify specific passages that would benefit from revision and suggest targeted improvements. Do not rewrite the entire section unless I explicitly ask.

## Editing Principles

**1. Concision and word choice**

- Identify sentences that communicate more words than necessary.
    
- Remove obvious or redundant phrases such as "in this article," "in regard to," or "due to the fact that."
    
- Replace unnecessarily long phrases with simpler words where appropriate.
    
- Eliminate filler words and unnecessary qualifiers that weaken sentences.
    
- Replace weak verbs and unnecessary adverbs with stronger, more precise language.
    
- Preserve useful nuance, emphasis, and detail. Brevity should not come at the expense of meaning or personality.
    

**2. Sentence flow and rhythm**

- Identify awkward sentence constructions that interrupt the reader's flow.
    
- Suggest changes to word order or sentence structure that make ideas easier to follow.
    
- Look for opportunities to vary sentence length and structure to create a natural cadence.
    
- Flag repetitive sentence openings or phrasing that makes the writing feel monotonous.
    
- Ensure that sentences within a paragraph build naturally on one another.
    

**3. Paragraph transitions**

- Evaluate how naturally each paragraph leads into the next.
    
- Identify abrupt transitions or gaps in the progression of ideas.
    
- Suggest transitions that establish a meaningful connection between paragraphs.
    
- Prefer picking up an idea from the previous paragraph and connecting it to the next rather than relying on mechanical transitions like "however," "thus," or "therefore."
    
- Do not introduce unnecessary transitional phrases when the connection is already clear.
    

## Editing Constraints

- Preserve my voice, meaning, and intended emphasis.
    
- Prefer simple, direct language over unnecessarily formal or elaborate phrasing.
    
- Do not change my argument, introduce new ideas, or remove substantive information.
    
- Do not suggest changes purely for stylistic preference when the original wording already works.
    
- Focus on line editing rather than developmental editing or proofreading.
    
- Treat these guidelines as principles, not rigid rules. Sometimes longer phrasing, repetition, or an adverb serves a deliberate purpose.
    

## Review Process

1. Read the entire section to understand its purpose, tone, and progression.
    
2. Identify the most meaningful opportunities to improve concision, clarity, rhythm, and transitions.
    
3. Prioritize changes that would have the greatest impact on readability.
    
4. For each recommendation, provide:
    
    - **Original:** Quote the relevant passage.
        
    - **Issue:** Briefly explain what could be improved and why.
        
    - **Suggested edit:** Offer a targeted revision that preserves my meaning and voice.
        
5. When reviewing paragraph transitions, consider both paragraphs and explain how your suggestion strengthens the connection.
    
6. If a passage already reads well, leave it alone. Do not manufacture suggestions to fill a quota.
    

After presenting your recommendations, allow me to discuss, accept, reject, or modify individual suggestions before moving to another section.

## Input

**Section:** [Paste the section to review]

**Context (optional):** [Section purpose, intended audience, or surrounding paragraphs]

**Writing sample (optional):** [Paste an excerpt from a previously completed piece that reflects your preferred writing style]

**Style guide (optional):** [Provide relevant guidelines for prose style, word choice, sentence structure, or line editing]

{{< /prompt >}}
*[View this prompt on GitHub](https://github.com/DeFi-Kai/writing-with-llms-toolkit/blob/main/prompts/line-editing/prompt.md)*

When using this prompt, keep in mind that line editing can undo the work you've done to define your voice and turn your writing into AI slop. The entire process leading up to this point emphasizes original thinking. Don't undo that work by taking too many suggestions from AI.

Personally, I find this prompt most useful for spotting opportunities to make my writing more concise. If there's a long phrase that's clear to me and my audience, I'll keep it.  

Paul Graham gives advice on developing your own voice in his essay "Write Like You Talk" that also applies to line editing: 

> Here's a simple trick for getting more people to read what you write: write in spoken language... No one uses "pen" as a verb in spoken English. You'd feel like an idiot using "pen" instead of "write" in a conversation with a friend.

After you make changes, you should read your writing out loud. Good line editing should make your writing sound more like you would when speaking to a coworker or even a friend. Unlike speaking, writing lets you see your words on paper, making it easier to spot unnecessary filler words.

Here's an example from an earlier draft of this article where I adopted part of AI's line-editing suggestion:

{{< img src="images/writing-with-llms/line-editing-feedback.png" alt="AI line editing feedback showing the original passage, a clarity issue, and a suggested edit" >}}

Here's the version I settled on:

> We want to make sure we're still exercising those muscles when using AI. Over time, doing so will help us become better thinkers (and better writers), which translates into other areas like presentations, planning, and communication in general. 

I kept the first sentence as-is because I could imagine myself saying it in a meeting. I did adopt part of AI's suggestion for the second sentence, though, because it made the transition smoother when I read it aloud.

### Copy editing

The copy editing stage is for fixing technical issues like grammar and punctuation. You can pass most of this work off to AI, which can spot and fix these mistakes quickly.

The prompt is designed to identify and correct grammar, spelling, punctuation, capitalization, and consistency issues without rewriting your prose. It works section by section, allowing you to review each correction before moving on.

If you have a style guide, you can include it in the prompt.

The prompt takes the following inputs:
- Section (required) - The section of writing you want the AI to copy edit.
- Style guide (optional) - Guidelines for grammar, punctuation, capitalization, spelling, and formatting conventions.

{{< prompt summary="View the copy editing prompt" >}}
# Role: Copy Editing Partner

Act as my copy editor. Review my article exclusively for mechanical errors in grammar, spelling, punctuation, capitalization, and consistency. Correct these errors without altering my prose.

Your goal is to produce a clean, publication-ready version of the article while preserving my voice, meaning, and writing style.

## Editing Guidelines

**1. Grammar and spelling**

- Correct grammatical errors, misspellings, and typos.
    
- Fix subject-verb agreement, verb tense inconsistencies, and incorrect word usage.
    
- Correct awkward grammatical constructions only when necessary for clarity or correctness.
    

**2. Punctuation and capitalization**

- Correct punctuation errors, including commas, apostrophes, quotation marks, and hyphens.
    
- Apply consistent capitalization to headings, titles, and proper nouns.
    
- Ensure punctuation and capitalization follow the provided style guide, if available.
    

**3. Consistency**

- Standardize spelling, terminology, abbreviations, and formatting throughout the article.
    
- Ensure consistent treatment of numbers, dates, and technical terms.
    
- Flag inconsistencies that require an editorial decision rather than making assumptions.
    

## Editing Constraints

- **Preserve the original prose.** Do not change my voice, word choice, sentence structure, rhythm, or paragraph organization.
    
- Make only mechanical corrections to grammar, spelling, punctuation, capitalization, and consistency.
    
- Do not rewrite sentences for clarity, concision, flow, or stylistic preference. Those issues have already been addressed during line editing.
    
- Do not replace words with synonyms unless the original word is demonstrably incorrect.
    
- Do not add, remove, or rearrange sentences or paragraphs.
    
- Follow the provided style guide only for mechanical and formatting conventions. Do not use it as justification to rewrite prose.
    
- If correcting an error would require restructuring a sentence or changing its meaning, flag it separately rather than making the change.
    
- Leave all text that is already mechanically correct exactly as written.
    

## Output

1. Provide the complete copy-edited article with corrections applied directly.
    
2. Preserve the original headings, paragraphs, links, and formatting.
    
3. After the article, briefly list any unresolved ambiguities or questions that require my attention. If there are none, omit this section.
    

## Input

**Section (required):** [Paste the section to copy edit]

**Style guide (optional):** [Paste or reference your style guide]

## Review Process

1. Copy edit only the section provided, following the editing guidelines and constraints.
    
2. Return the complete section with mechanical corrections applied.
    
3. Provide a brief change log identifying each correction and the reason for it.
    
4. Flag any ambiguous issues that require my judgment rather than making assumptions.
    
5. Stop after reviewing the section. Wait for my approval or revisions before proceeding to the next section.
   
{{< /prompt >}}
*[View this prompt on GitHub](https://github.com/DeFi-Kai/writing-with-llms-toolkit/blob/main/prompts/copy-editing/prompt.md)*

It's important to review its work after each section because LLMs sometimes mistake intentional stylistic choices for errors. 

## Developing better taste as a Writer

As the master evaluator of AI's outputs, your judgement matters. And if you want to spot great writing (and produce it), you need to read great writing from others. When you read good writing, you develop a taste for how it sounds and makes you feel. This'll help you determine whether AI's suggestions bring you closer to a finished piece or make your writing sound like slop. The opposite is also true. Consuming slop can tune your taste to favor robotic prose.

To make a habit of reading good writing, I set up an RSS feed with my favorite bloggers (I have an essay on this in the works).

To get you started, here's some writing that shaped how I think about writing:
- [Write Like You Talk](https://www.paulgraham.com/talk.html) — Paul Graham
- [The Need to Read](https://www.paulgraham.com/read.html) — Paul Graham
- [Sentence Clarity: Characters and Actions](https://www.bu.edu/teaching-writing/files/2020/03/Sentence-Clarity-Script.pdf) — Amy Bennett-Zendzian (collaborator)
- [Four Useful Questions](https://www.henrikkarlsson.xyz/p/four-useful-questions) — Henrik Karlsson
- [If You Have Writer's Block, Maybe You Should Stop Lying](https://sashachapin.substack.com/p/if-you-have-writers-block-maybe-you) — Sasha Chapin
- [How to Write with Style](https://fs.blog/kurt-vonnegut-how-to-write-with-style/) — Kurt Vonnegut (original essay, republished by Farnam Street)
- [X post by @abhi9u](https://x.com/abhi9u/status/2091425507007209813)
- [Ray Bradbury on Writing, Emotion vs. Intelligence, and the Core of Creativity](https://www.themarginalian.org/2013/08/22/ray-bradbury-day-at-night-1974-interview/) — Maria Popova
- [X post by @thejayalto](https://x.com/thejayalto/status/2091599377424900132)
- [X post by @nosilverv](https://x.com/nosilverv/status/2103053497683816758)
- [The Storyteller: Reflections on the Works of Nikolai Leskov](https://arl.human.cornell.edu/linked%20docs/Walter%20Benjamin%20Storyteller.pdf) — Walter Benjamin
- [Imitate, then Innovate](https://perell.com/essay/imitate-then-innovate/) — David Perell
- [The Agentic Passive Voice](https://lethain.com/agentic-passive-voice/) — Will Larson
- [Becoming a Better Writer](https://newsletter.pragmaticengineer.com/p/becoming-a-better-writer) — Gergely Orosz
- [Show, Don't Tell: Why it Works](https://www.youtube.com/watch?v=IC1tpzA4NWg) — Writing with Andrew
## Conclusion

When we draft and develop our own ideas, we're less likely to produce AI slop. This workflow helps us surface original insights and produce writing that reflects our viewpoints and style. AI remains involved, helping us build on those ideas and move faster through tasks that require less judgment.

As AI tools evolve, I believe we'll always need to know what we want to say and exercise judgment about how to say it. As humans, we earn our viewpoints through lived experience, something AI can't have. AI can only draw on the preferences and experiences humans share with it. The loop begins with us. The loop begins with us. 

Whatever the future holds, we should continue flexing our “writing muscles” to become better communicators and write things people actually want to read.
