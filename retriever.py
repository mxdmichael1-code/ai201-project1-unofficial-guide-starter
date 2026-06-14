from pathlib import Path
import json
import shutil

import chromadb
from sentence_transformers import SentenceTransformer


CHUNKS_PATH = Path("chunks.json")
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "judge_training"

MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 3


model = SentenceTransformer(MODEL_NAME)


def load_chunks():
    with CHUNKS_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_vector_store():
    """
    Load chunks.json, embed each chunk, and store everything in ChromaDB.
    """

    # Delete old database so we do not duplicate chunks every time
    if Path(CHROMA_PATH).exists():
        shutil.rmtree(CHROMA_PATH)

    chunks = load_chunks()

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    texts = [chunk["text"] for chunk in chunks]
    ids = [chunk["id"] for chunk in chunks]

    metadatas = [
        {
            "source": chunk["source"],
            "chunk_id": chunk["id"],
            "position": i,
        }
        for i, chunk in enumerate(chunks)
    ]

    embeddings = model.encode(texts).tolist()

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings,
    )

    print(f"Stored {collection.count()} chunks in ChromaDB.")


def retrieve(query, k=TOP_K):
    """
    Embed the query and return the top-k closest chunks.
    """

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_collection(name=COLLECTION_NAME)

    query_embedding = model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    retrieved_chunks = []

    for i in range(len(documents)):
        retrieved_chunks.append({
            "text": documents[i],
            "source": metadatas[i]["source"],
            "chunk_id": metadatas[i]["chunk_id"],
            "distance": distances[i],
        })

    return retrieved_chunks


def print_results(query):
    print("\n" + "=" * 80)
    print(f"QUERY: {query}")
    print("=" * 80)

    chunks = retrieve(query)

    for chunk in chunks:
        print("\n---")
        print(f"Source: {chunk['source']}")
        print(f"Chunk ID: {chunk['chunk_id']}")
        print(f"Distance: {chunk['distance']:.3f}")
        print(chunk["text"][:600])


if __name__ == "__main__":
    build_vector_store()

    test_queries = [
        "What should I do if I suspect a student is using external help or AI during a round?",
        "What should I do during evidence checking in PF?",
        "What is the procedure for Junior Debate?",
    ]

    for query in test_queries:
        print_results(query)