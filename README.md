# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." --> 
My system covers debate and speech judging knowledge for WSDA-style events, especially Public Forum Debate, Original Oratory, Junior Speech, and Junior Debate. It focuses on practical judge-facing information such as round format, speech order, timing rules, preparation rules, evidence rules, scoring standards, ballot expectations, and what judges should do when unexpected procedural issues happen.

This knowledge is valuable because judges often need quick answers during or immediately after a round. Posting these questions to the tabroom/admin might take longer time to wait for a response, and add unnecessary burden to the admin/tabroom while they are processing other tasks. 

This information can be hard to find through official channels because it is often spread across long rule documents, training slides, tournament announcements, WeChat group instructions, and oral judge briefings. Some rules are also format-specific, so a judge may know the general idea but still be unsure about the exact procedure for a specific event. My system makes this knowledge easier to query by turning judge training materials into a searchable assistant that gives grounded answers from the loaded documents.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

These documents are based on publicly shared WSDA event information and judge-training materials originally distributed through WeChat posts and tournament communications. The original materials contained format rules, timing rules, scoring standards, and judge reminders for events such as Public Forum Debate, Original Oratory, Junior Speech, and Junior Debate.

I used an AI assistant to help reorganize these materials into cleaner .txt files for my RAG system. It helped translate, clarify, and restructure the original content into fixed-size-chunk-friendly documents with clear section headings, shorter paragraphs, and consistent terminology. 

Here are the original source links in Chinese:
https://mp.weixin.qq.com/s/8gyBzw-bBWOXDuxHOb7Htg
https://mp.weixin.qq.com/s/onjH7Ius5ttXO2GnR5qJFA 
https://mp.weixin.qq.com/s/L5dSO9pH90Gy9PX87Ts5uA 

| # |           Source              |   Type   |         URL or file path           |
|---|-------------------------------|----------|------------------------------------|
| 1 |  PF Format and Round Layout   | txt file |   pf_format_and_round_layout.txt   |
| 2 |PF Speech Roles & Expectations | txt file | pf_speech_roles_&_expectations.txt |
| 3 |  PF Voting and Scoring Guide  | txt file |   pf_voting_and_scoring_guide.txt  |
| 4 | PF Special Rules & Reminders  | txt file |  pf_special_rules_&_reminders.txt  |
| 5 | OO Format and Round Procedure | txt file | oo_format_and_round_procedure.txt  |
| 6 |      OO Competition Rules     | txt file |      oo_competition_rules.txt      |
| 7 | OO Scoring and Ranking Guide  | txt file |  oo_scoring_and_ranking_guide.txt  |
| 8 |Junior Speech Competition Rules| txt file | junior_speech_competition_rules.txt|
| 9 |     Junior Speech Scoring     | txt file |      junior_speech_scoring.txt     |
| 10| Junior Debate Format And Rules| txt file | junior_debate_format_and_rules.txt |
| 11|     Junior Debate Scoring     | txt file |      junior_debate_scoring.txt     |
---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size: 500 characters**

**Overlap: 100 characters**

**Why these choices fit your documents: I use fixed-size character chunking with overlap. My documents are judge-training guides rather than short reviews, so most useful answers need one specific rule plus a short explanation of how the judge should apply it. A 500 character chunk is large enough to usually keep one complete rule together, but still short enough for retrieval to stay focused.

This fits my use case because judges are usually not asking broad questions during a round. They are often unsure about one specific rule, such as whether feedback is allowed, how evidence checking works, how prep time should be handled, or how a scoring category should be applied. By writing the documents in short, direct sentences and then using fixed-size chunks, the system is more likely to retrieve the key idea of that particular rule for quick reference.

When formatting the documents, I explicitly asked the AI assistant to make them fixed-size-chunking friendly. The final .txt files use clear section headings, short paragraphs, repeated key terms, and mostly short sentences. Some rules still need slightly longer explanations, but the 100-character overlap helps preserve context when a rule continues across two chunks. **

**Final chunk count:**
266

**Sample chunks**
=== SAMPLE CHUNKS ===

---
ID: junior_debate_format_and_rules_0
Source: junior_debate_format_and_rules.txt
Length: 456
JUNIOR_DEBATE_FORMAT_AND_RULES
Document type: Judge training material
Format: WSDA Junior Extemporaneous Debate
Primary users: Junior debate judges
Purpose: Explain Junior Debate format, topic release, preparation procedure, speech order, timing, prep time, evidence use, side confirmation, and judge escalation rules.

SECTION 1: WHAT JUNIOR DEBATE IS

Junior Debate is an extemporaneous debate format.

Each round has one pro debater and one con debater.

---
ID: junior_debate_format_and_rules_1
Source: junior_debate_format_and_rules.txt
Length: 460
nior Debate is an extemporaneous debate format.

Each round has one pro debater and one con debater.

The two debaters debate one resolution or topic.

The system randomly assigns each debater's side.

The pro debater supports the resolution.

The con debater opposes the resolution.

In every round, the pro debater always gives the first speech.

SECTION 2: TOPIC SELECTION

In each round and each flight, debaters will receive a different independent topic.

---
ID: junior_debate_format_and_rules_2
Source: junior_debate_format_and_rules.txt
Length: 484
TOPIC SELECTION

In each round and each flight, debaters will receive a different independent topic.

Debaters must prepare the assigned topic within the required preparation time.

The debate topic for each round will usually be announced in the judge WeChat group; if the judges are unsure about the topic, they should ask in the group to obtain clarification

To protect fairness, the extemporaneous topic should be released only 15 minutes before the official start of that round.

---
ID: junior_debate_format_and_rules_3
Source: junior_debate_format_and_rules.txt
Length: 481
the extemporaneous topic should be released only 15 minutes before the official start of that round.

SECTION 3: PREPARATION GROUPS

After an extemporaneous topic is released, both pro and con debaters have 15 minutes to prepare.

During preparation, debaters may not receive outside assistance.

After preparation groups are assigned, the side generally should not be changed.

The round cannot be changed once confirmed unless tournament staff or the tabroom instructs otherwise.

---
ID: junior_debate_format_and_rules_4
Source: junior_debate_format_and_rules.txt
Length: 457
e round cannot be changed once confirmed unless tournament staff or the tabroom instructs otherwise.

SECTION 4: WHEN DEBATERS ENTER THE ROOM

There are two possible situations when debaters enter the competition room.

In the first situation, debaters have already completed their 15-minute preparation in a separate room or preparation area. If this is the case, the judge should confirm the debaters, confirm their sides, and start the debate right away.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used: all-MiniLM-L6-v2**

**Production tradeoff reflection:**
If I deployed this for real users, I would mainly consider speed and multilingual support when choosing a different embedding model. Speed matters because judges may need to check something during a round or before submitting a ballot, so retrieval should be fast. Multilingual support also matters because some judges may ask questions in Chinese, so it might be helpful to get the Chinese words embedded into similar terms into English for more accuracy.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

My original system prompt was:

“You are a debate and speech judge-training assistant.

You must answer using ONLY the provided retrieved document context.

Rules:

* Do not use outside knowledge.
* Do not guess.
* Do not add rules that are not clearly supported by the provided context.
* If the context does not contain enough information, say: ‘I don’t have enough information on that.’
* Keep the answer clear and practical for a judge.
* Do not decide the winner of a debate round.”

This prompt is meant to stop the model from giving general debate advice or making up rules. It also tells the model to refuse when the retrieved chunks do not contain enough information. This matters because some debate questions can sound familiar to the LLM, but the system should only answer based on my judge-training documents.

**How source attribution is surfaced in the response:**
The retrieved chunks are passed into the prompt with source information, including the document name and chunk ID. In the interface, I also show the retrieved sources separately from the answer. This is done programmatically, not just by asking the LLM to cite sources.

This means the answer box gives the model’s response, and the “Retrieved from” box shows which documents were used. For example, it can show pf_special_rules_and_judge_reminders.txt and the chunk ID, so I can check whether the answer actually came from the correct source.
---
## Retrieval test results

================================================================================
QUERY: What should I do if I suspect a student is using external help or AI during a round?
================================================================================

---
Source: oo_competition_rules.txt
Chunk ID: oo_competition_rules_9
Distance: 0.501
t artificial intelligence.

Students may use generative AI to help find articles, ideas, or sources.

However, any quoted or paraphrased evidence must have an original source that can be provided if requested.

Judges should distinguish between using AI to locate sources and using AI as the source of speech text.

If a judge has a serious concern about AI misuse, the judge should report the concern to tournament staff or tabroom instead of directly accusing the student during the round.

---
Source: pf_special_rules_&_reminders.txt
Chunk ID: pf_special_rules_&_reminders_30
Distance: 0.544
rate arguments, responses, speech text, crossfire questions, weighing analysis, or strategic advice.

If a judge reasonably believes that a debater is using external help or AI assistance to prepare or deliver speech content during the round, the judge should report the concern to the tabroom or tournament staff.

---
Source: pf_special_rules_&_reminders.txt
Chunk ID: pf_special_rules_&_reminders_6
Distance: 0.545
RING THE ROUND

During the round, debaters may use electronic devices to look up internet materials.

However, debaters may not receive help from anyone other than their teammate.

Debaters may not message coaches, parents, teammates outside the round, other students, or any outside person for help during the round.

Debaters may not receive outside strategic advice, arguments, evidence, translations, or responses during the round.

================================================================================
QUERY: What should I do during evidence checking in PF?
================================================================================

---
Source: pf_special_rules_&_reminders.txt
Chunk ID: pf_special_rules_&_reminders_43
Distance: 0.458
nce must include an accessible original link.

Evidence checks may be requested after a speech ends.

The team providing evidence has 1 minute of free time to find it.

After the evidence is provided, the checking team’s prep time starts if it continues reviewing.

Evidence issues must be argued in speeches to matter on the ballot.

Failure to find evidence does not automatically prove the argument is false.

Pre-elimination results must not be released immediately after the round.

---
Source: pf_special_rules_&_reminders.txt
Chunk ID: pf_special_rules_&_reminders_14
Distance: 0.489
rovides the evidence to Team A, Team A’s prep time begins if Team A continues checking the evidence.

During evidence checking, participants in the room should only review the evidence. They should not use the evidence check period to prepare new arguments, discuss strategy, or communicate about unrelated issues.

After Team B gives the evidence to Team A, Team B should not take additional actions while Team A reviews the evidence.

---
Source: pf_special_rules_&_reminders.txt
Chunk ID: pf_special_rules_&_reminders_33
Distance: 0.533
content or strategic advice, and whether the conduct seemed different from ordinary evidence lookup.

Judges should distinguish between allowed evidence searching and prohibited outside assistance. Evidence searching is used to find or verify sources. Prohibited assistance is help that creates, improves, or supplies debate content for the debater during the round.

A judge should continue evaluating the round based on the arguments made unless tournament staff gives a different instruction.

================================================================================
QUERY: What is the procedure for Junior Debate?
================================================================================

---
Source: junior_debate_format_and_rules.txt
Chunk ID: junior_debate_format_and_rules_25
Distance: 0.199
Junior Debate is one pro debater versus one con debater.

Sides are randomly assigned by the system.

The pro debater always speaks first.

If debaters already prepared in a separate room, confirm sides and start the debate.

If debaters have not received the topic, release the topic as instructed, confirm sides, start 15 minutes of preparation, and then begin the round.

The round cannot be changed once confirmed unless tournament staff instructs otherwise.

---
Source: junior_debate_format_and_rules.txt
Chunk ID: junior_debate_format_and_rules_27
Distance: 0.338
materials, electronic devices, internet lookup, or evidence lookup during preparation or the debate.

Evidence use is allowed only when tournament setting permits it, but it is not the key deciding factor in Junior Debate.

Mandatory prep time is 1 minute before rebuttals and 1 minute before final focus.

Final focus should not include new arguments.

---
Source: junior_debate_format_and_rules.txt
Chunk ID: junior_debate_format_and_rules_15
Distance: 0.360
se preparation time is limited, the use of evidence is not the key deciding factor in Junior Debate.

Evidence may be used if the format and tournament setting allow it, but judges should not treat evidence as the main evaluation factor.

Judges should focus more on analysis, reasoning, rebuttal, cross examination, delivery, and overall impact.

SECTION 9: ROUND LENGTH AND MAIN STAGES

Each Junior Debate round usually lasts about 15 to 20 minutes.

## Example Responses:
QUESTION: What is the procedure for Junior Debate?

ANSWER:
The procedure for Junior Debate is as follows: 

1. The pro debater and con debater are assigned sides randomly by the system.
2. The pro debater speaks first.
3. If debaters have not received the topic, the topic is released, sides are confirmed, and a 15-minute preparation time begins.
4. After preparation, the debate round starts.
5. During the debate, there are mandatory 1-minute preparation times before rebuttals and before the final focus.
6. The final focus should not include new arguments.
7. The round typically lasts 15 to 20 minutes.

Note: Judges should focus on evaluation factors such as analysis, reasoning, rebuttal, cross-examination, delivery, and overall impact, rather than evidence as the main deciding factor.

SOURCES:
- junior_debate_format_and_rules.txt — junior_debate_format_and_rules_25
- junior_debate_format_and_rules.txt — junior_debate_format_and_rules_27
- junior_debate_format_and_rules.txt — junior_debate_format_and_rules_15

================================================================================
QUESTION: What should I do if a student uses AI during the round?

ANSWER:
If a student uses AI during the round, you should distinguish between using AI to locate sources and using AI as the source of speech text. If you have a serious concern about AI misuse, report the concern to tournament staff or tabroom instead of directly accusing the student during the round.

SOURCES:
- oo_competition_rules.txt — oo_competition_rules_9
- pf_special_rules_&_reminders.txt — pf_special_rules_&_reminders_27
- pf_special_rules_&_reminders.txt — pf_special_rules_&_reminders_6

================================================================================
QUESTION: What is the best strategy to win a PF round?

ANSWER:
I don't have enough information on that. The provided context explains how judges should evaluate a PF round and what factors to consider when voting, but it does not provide a specific strategy for debaters to win a PF round. It only mentions that debaters should "research the topic, prepare arguments, collect evidence, and practice responses before competing."

SOURCES:
- pf_format_and_round_layout.txt — pf_format_and_round_layout_3
- pf_voting_and_scoring_guide.txt — pf_voting_and_scoring_guide_34
- pf_voting_and_scoring_guide.txt — pf_voting_and_scoring_guide_31


## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | 
Question: In Junior Debate, what should the judge do if debaters enter the room and have not received the topic yet?
Expected Answer: 

The judge should confirm both debaters are in the correct room and know their assigned sides, release the topic as  instructed by the official WeChat group or tournament communication, start a 15-minute preparation timer, and begin the round when preparation time ends.

System Response:

If debaters enter the room and have not received the topic yet, the judge should: 
1. Confirm that both debaters are in the correct room.
2. Confirm which debater is pro and which debater is con.
3. Release the debate topic exactly as instructed.
4. Make sure both debaters understand the topic and know which side they are debating.
5. Start a 15-minute timer for preparation.
6. Begin the round after the 15-minute preparation time is over.

Retrieval Quality: relevant
Response Accuracy: accurate





| 2 |
Question: What should I do if I suspect a student is using external help or AI during a round?
Expected Answer:
The judge should report the concern to the tabroom or tournament staff. The judge should not directly accuse the student, inspect private messages, stop the round, or make a final misconduct ruling alone unless instructed. Searching for evidence online may be allowed, but using external help or AI to generate arguments, speeches, responses, or strategy is not allowed.

System Response:

If you suspect a student is using external help or AI during a round, you should report the concern to the tournament staff or tabroom instead of directly accusing the student during the round.

Retrieval Quality: relevant
Response Accuracy: accurate


| 3 |
Question: What should I do during evidence checking in PF?
Expected Answer: 

Evidence checks should happen after a speech ends, not during a speech. The team providing evidence has 1 minute of free time to find and provide the evidence. If they need more time, they may use their own prep time. After the evidence is provided, the checking team’s prep time begins if they continue reviewing it. Evidence issues must be argued in a speech to matter on the ballot, and failure to find evidence does not automatically prove the argument false.

System Response:

During evidence checking in PF, you should only review the evidence. You should not use the evidence check period to prepare new arguments, discuss strategy, or communicate about unrelated issues. After the team providing the evidence gives it to the checking team, the providing team should not take additional actions while the checking team reviews the evidence.

Retrieval Quality: relevant
Response Accuracy: partially accurate


| 4 |
Question: What is the procedure for Junior Debate?
Expected Answer: 
Junior Debate is one pro debater against one con debater. The pro side always speaks first. If debaters already prepared separately, the judge should confirm the room, topic, and sides, then start the debate. If they have not received the topic, the judge should release the topic as instructed, confirm sides, start a 15-minute prep timer, and begin the round when prep time ends. The round order includes constructive speeches, cross examination, mandatory prep time, rebuttals, mandatory prep time, and final focus speeches.

System Response:

The procedure for Junior Debate is as follows: 

1. Sides (pro and con) are randomly assigned by the system.
2. The pro debater always speaks first.
3. If debaters have already prepared, confirm sides and start the debate.
4. If debaters haven't received the topic, release the topic, confirm sides, and provide 15 minutes of preparation time before starting the round.
5. During the round, mandatory prep time of 1 minute is allowed before rebuttals and 1 minute before final focus.
6. The final focus should not include new arguments.
7. The round typically lasts 15 to 20 minutes. 

Judges should focus on evaluation factors such as analysis, reasoning, rebuttal, cross-examination, delivery, and overall impact, rather than evidence as the main deciding factor.

Retrieval Quality: relevant
Response Accuracy: partially accurate


| 5 |
Question: A student wants to leave the room after finishing their speech. Is that allowed?
Expected Answer:
 No, not normally. In Original Oratory, after finishing their own speech, the competitor should stay and listen to the other speakers in the group. Competitors may leave only after all speakers have finished and the judge gives permission or tournament procedure allows dismissal.

System Response:

No, the student is not allowed to leave the room immediately after finishing their speech. According to the document, "A competitor should not leave immediately after giving the speech." and "All competitors may leave only after all speeches in the group have finished and the judge gives permission or tournament procedure allows dismissal." Judges are also instructed to remind competitors to remain in the room if they try to leave early.

Retrieval Quality: relevant
Response Accuracy: accurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

What should I do during evidence checking in PF?

**What the system returned:**

During evidence checking in PF, you should only review the evidence. You should not use the evidence check period to prepare new arguments, discuss strategy, or communicate about unrelated issues. After the team providing the evidence gives it to the checking team, the providing team should not take additional actions while the checking team reviews the evidence.


**Root cause (tied to a specific pipeline stage):**

This mainly failed at the generation stage. The retrieved chunk was related to evidence checking, but the model interpreted “you” as a debater instead of a judge. Because the source text includes rules about what the teams can and cannot do during evidence checking, the model turned those rules into student-facing instructions. It did not reframe the answer around the judge’s actual role, such as managing the evidence check, tracking prep time, making sure the check happens after the speech, and recording any evidence issues on the ballot.

**What you would change to fix it:**

I would first change the system prompt so the assistant always assumes the user is a judge unless the question clearly says otherwise. The prompt should say that answers need to be procedural and judge-facing, not written as advice to debaters. For example, instead of saying “you should only review the evidence,” the system should say what the judge should do: allow the evidence check after the speech, track the correct prep time, make sure teams do not use the check for unrelated strategy, and record any evidence issue on the ballot if it becomes relevant.

I would also make the answer format more structured for procedural questions. For example, when a question asks “what should I do,” the model should answer in steps: what the judge should do first, what to monitor during the process, and what to write on the ballot afterward. This would make the response more useful during a real round.

Finally, I would improve the source document itself by adding more judge-facing wording around evidence checking. The document should include phrases like “The judge should…” and “The judge should not…” so retrieval gives the model clearer procedural context instead of only student-facing rules.
---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

The planning.md helped me know what I was building before I started coding. Since I already had the pipeline written out, I could follow it step by step: load documents, chunk them, embed them, retrieve relevant chunks, and then generate an answer. It also helped me check whether the system was still matching my original goal, which is to answer judge-facing questions from the rule documents.

**One way your implementation diverged from the spec, and why:**

The main change was in the chunking method. In the original spec, I planned to use fixed-size character chunking. But after looking at the chunks, I realized that cutting only by character count could split a rule or explanation in the middle, which would make retrieval less useful.

Because of that, I changed the implementation to paragraph-aware chunking. It still keeps the target chunk size and overlap from the spec, but it tries to keep paragraphs together when possible. This made the chunks easier to understand on their own and more useful for judge-rule questions.
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
    I gave the AI my source materials for the debate and speech events, including PF, Original Oratory, Junior Speech, and Junior Debate rules. I also explained that the documents would be used in a RAG system, so they needed to be clear and easy to chunk.
- *What it produced:*
    It helped me reorganize the original materials into cleaner .txt files with headings, shorter paragraphs, and more consistent wording. The content was still based on the original rule materials, but the structure became easier for my system to load and retrieve from.
- *What I changed or overrode:*
    I checked that the rules still matched the original materials and adjusted wording when it sounded too AI-generated or too far from the source. I also made sure the documents stayed judge-facing rather than becoming general debate advice.

**Instance 2**

- *What I gave the AI:*
    I gave the AI my planning.md sections, especially the architecture diagram, chunking strategy, and retrieval approach. I asked for help thinking through how to implement ingestion, chunking, embedding, retrieval, generation, and the Gradio interface.
- *What it produced:*
    It gave me example code structures for loading .txt files, creating chunks, storing embeddings in ChromaDB, retrieving relevant chunks, connecting to Groq, and showing answers in a simple Gradio UI.
- *What I changed or overrode:*
    I did not just copy the code directly. I simplified parts of it because my documents were already .txt files and did not need HTML cleaning or scraping. I also changed the chunking method from pure fixed-size character chunking to paragraph-aware chunking, because cutting only by character count could split rules in the middle.
