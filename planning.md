# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
My system covers debate and speech judging knowledge for WSDA-style events, especially Public Forum Debate, Original Oratory, Junior Speech, and Junior Debate. It focuses on practical judge-facing information such as round format, speech order, timing rules, preparation rules, evidence rules, scoring standards, ballot expectations, and what judges should do when unexpected procedural issues happen.

This knowledge is valuable because judges often need quick answers during or immediately after a round. Posting these questions to the tabroom/admin might take longer time to wait for a response, and add unnecessary burden to the admin/tabroom while they are processing other tasks. 

This information can be hard to find through official channels because it is often spread across long rule documents, training slides, tournament announcements, WeChat group instructions, and oral judge briefings. Some rules are also format-specific, so a judge may know the general idea but still be unsure about the exact procedure for a specific event. My system makes this knowledge easier to query by turning judge training materials into a searchable assistant that gives grounded answers from the loaded documents.
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size: 500 - 600 characters

**Overlap: 100 characters

**Reasoning: I use fixed-size character chunking with overlap. My documents are judge-training guides rather than short reviews, so most useful answers need one specific rule plus a short explanation of how the judge should apply it. A 500 character chunk is large enough to usually keep one complete rule together, but still short enough for retrieval to stay focused.

This fits my use case because judges are usually not asking broad questions during a round. They are often unsure about one specific rule, such as whether feedback is allowed, how evidence checking works, how prep time should be handled, or how a scoring category should be applied. By writing the documents in short, direct sentences and then using fixed-size chunks, the system is more likely to retrieve the key idea of that particular rule for quick reference.

When formatting the documents, I explicitly asked the AI assistant to make them fixed-size-chunking friendly. The final .txt files use clear section headings, short paragraphs, repeated key terms, and mostly short sentences. Some rules still need slightly longer explanations, but the 100-character overlap helps preserve context when a rule continues across two chunks.**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model: all-MiniLM-L6-v2 **

**Top-k: 3 **

**Production tradeoff reflection:**

If I deployed this for real users, I would mainly consider speed and multilingual support when choosing a different embedding model. Speed matters because judges may need to check something during a round or before submitting a ballot, so retrieval should be fast. Multilingual support also matters because some judges may ask questions in Chinese, so it might be helpful to get the Chinese words embedded into similar terms into English for more accuracy.
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| 1 | Question: In Junior Debate, what should the judge do if debaters enter the room and have not received the topic yet? |
Answer: The judge should confirm both debaters are in the correct room and know their assigned sides, release the topic as  instructed by the official WeChat group or tournament communication, start a 15-minute preparation timer, and begin the round when preparation time ends.

| 2 | Question: What should I do if I suspect a student is using external help or AI during a round?|
Answer: The judge should report the concern to the tabroom or tournament staff. The judge should not directly accuse the student, inspect private messages, stop the round, or make a final misconduct ruling alone unless instructed. Searching for evidence online may be allowed, but using external help or AI to generate arguments, speeches, responses, or strategy is not allowed.

| 3 | Question: What should I do during evidence checking in PF?|
Answer: Evidence checks should happen after a speech ends, not during a speech. The team providing evidence has 1 minute of free time to find and provide the evidence. If they need more time, they may use their own prep time. After the evidence is provided, the checking team’s prep time begins if they continue reviewing it. Evidence issues must be argued in a speech to matter on the ballot, and failure to find evidence does not automatically prove the argument false. |

| 4 | Question: What is the procedure for Junior Debate?|
Answer: Junior Debate is one pro debater against one con debater. The pro side always speaks first. If debaters already prepared separately, the judge should confirm the room, topic, and sides, then start the debate. If they have not received the topic, the judge should release the topic as instructed, confirm sides, start a 15-minute prep timer, and begin the round when prep time ends. The round order includes constructive speeches, cross examination, mandatory prep time, rebuttals, mandatory prep time, and final focus speeches.

| 5 | Question: A student wants to leave the room after finishing their speech. Is that allowed?| |
Answer: No, not normally. In Original Oratory, after finishing their own speech, the competitor should stay and listen to the other speakers in the group. Competitors may leave only after all speakers have finished and the judge gives permission or tournament procedure allows dismissal.
---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Wrong-event retrieval. Some rules sound similar across PF, Junior Debate, Junior Speech, and OO, but the details are different. For example, many events have timing rules, but the actual time limits are not the same. To reduce this, I used clear event names and repeated keywords in the documents.

2. Fixed-size chunking may split a rule from its explanation. For example, one chunk may include the evidence-check steps, while another chunk explains how judges should treat missing evidence. The 100-character overlap should help with this, but it may not solve every case.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

flowchart LR
    A[Document Ingestion/Python + local .txt files] --> B[Chunking/Fixed-size character chunks/500 chars + 100 overlap]
    B --> C[Embedding + Vector Store/sentence-transformers/all-MiniLM-L6-v2/ChromaDB PersistentClient]
    C --> D[Retrieval/retrieve query/top-k = 3 chunks/lowest cosine distance]
    D --> E[Generation/Groq LLM/>grounded answer using retrieved context only]
    E --> F[Query Interface/basic web UI / app.py]
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

For document preparation, I used ChatGPT to help turn public WeChat/tournament materials into clean .txt files. I gave it the original rule text and told it to keep close to the original content, only adding necessary judge-facing clarification. I also explicitly asked it to make the documents fixed-size-chunking friendly, with clear headings, short sentences, and repeated key terms. I verified the output by checking whether the rules still matched the original materials and whether each file focused on one event or rule category.

**Milestone 3 — Ingestion and chunking:**
I will use ChatGPT to help implement the document loading and chunking functions. I will give it my Architecture section and Chunking Strategy section, especially the 500–600 character chunk size, 100-character overlap, and minimum length. I expect it to produce code that loads .txt files from data/raw/, cleans extra spacing, and creates chunks with source metadata. I will verify it by printing sample chunks and checking that they are not too short, not too broad, and still include the correct source file.

**Milestone 4 — Embedding and retrieval:**

For embedding and vector storage, I will use Codex to adapt the class example. I will give it my Embedding Model section and ask it to use all-MiniLM-L6-v2 with ChromaDB. I expect it to produce code that embeds chunks, stores text and metadata, and uses a persistent local vector store. I will verify it by checking the stored chunk count and confirming that each chunk keeps its source metadata.

For retrieval, I will use ChatGPT or Codex to implement retrieve() based on my top-k decision. I will give it the Retrieval section and specify that it should return the top 3 chunks by cosine distance. I expect it to return a list of dictionaries containing chunk text, source/event metadata, and distance score. I will verify it by running my five test questions in the terminal and checking whether the retrieved chunks come from the correct event and rule document.

**Milestone 5 — Generation and interface:**

For generation, I will use ChatGPT to help design the system prompt and Codex to implement the API call. I will give it my grounding requirements and expected behavior: answer only from retrieved context, cite the event/source, and say when the answer is not found. I expect it to produce a response-generation function that sends the top 3 chunks to the Groq LLM and returns a plain string answer. I will verify it by checking that answers do not include unsupported rules and that each answer identifies the relevant source.
