from groq import Groq
from dotenv import load_dotenv
import os

from retriever import retrieve


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

client = Groq(api_key=GROQ_API_KEY)


def format_context(chunks):
    context_parts = []

    for i, chunk in enumerate(chunks, start=1):
        context_parts.append(
            f"""[Source {i}]
Document: {chunk["source"]}
Chunk ID: {chunk["chunk_id"]}
Text:
{chunk["text"]}
"""
        )

    return "\n".join(context_parts)


def ask(question):
    retrieved_chunks = retrieve(question, k=3)

    if not retrieved_chunks:
        return {
            "answer": "I don't have enough information on that.",
            "sources": []
        }

    context = format_context(retrieved_chunks)

    system_prompt = """
You are a debate and speech judge-training assistant.

You must answer using ONLY the provided retrieved document context.

Rules:
- Do not use outside knowledge.
- Do not guess.
- Do not add rules that are not clearly supported by the provided context.
- If the context does not contain enough information, say: "I don't have enough information on that."
- Keep the answer clear and practical for a judge.
- Do not decide the winner of a debate round.
"""

    user_prompt = f"""
Question:
{question}

Retrieved document context:
{context}

Answer the question using only the retrieved context.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1,
    )

    answer = response.choices[0].message.content

    sources = []
    for chunk in retrieved_chunks:
        source_label = f'{chunk["source"]} — {chunk["chunk_id"]}'
        if source_label not in sources:
            sources.append(source_label)

    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":
    test_questions = [
        "What should I do during evidence checking in PF?",
        "What is the procedure for Junior Debate?",
        "What should I do if a student uses AI during the round?",
        "What is the best strategy to win a PF round?"
    ]

    for q in test_questions:
        print("\n" + "=" * 80)
        print("QUESTION:", q)
        result = ask(q)
        print("\nANSWER:")
        print(result["answer"])
        print("\nSOURCES:")
        for source in result["sources"]:
            print("-", source)