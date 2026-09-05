import chromadb
from pathlib import Path


# -----------------------------
# 1. Find our project folders
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

KNOWLEDGE_DIR = PROJECT_ROOT / "knowledge"
CHROMA_DIR = PROJECT_ROOT / ".chroma"


# -----------------------------
# 2. Create ChromaDB client
# -----------------------------

client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)


# -----------------------------
# 3. Create/get a collection
# -----------------------------

collection = client.get_or_create_collection(
    name="assignment_knowledge"
)


# -----------------------------
# 4. Read our knowledge file
# -----------------------------

file_path = KNOWLEDGE_DIR / "user_preference.txt"

text = file_path.read_text(
    encoding="utf-8"
)


# -----------------------------
# 5. Add document to Chroma
# -----------------------------

collection.upsert(
    ids=["user_preference"],
    documents=[text]
)


# -----------------------------
# 6. Ask a question
# -----------------------------

question = "What is the user's profession?"


# -----------------------------
# 7. Search ChromaDB
# -----------------------------

results = collection.query(
    query_texts=[question],
    n_results=1
)


# -----------------------------
# 8. Display retrieved result
# -----------------------------

print("\nQuestion:")
print(question)

print("\nRetrieved information:")
print(results["documents"][0][0])