from sentence_transformers import SentenceTransformer 
import chromadb

with open("fest_info.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(f"Your file has {len(text)} characters.")
print()
print("sample text:", text[:300])

def chunk_text(text, chunk_size = 200, overlap = 60):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks 

chunks = chunk_text(text)

model = SentenceTransformer('all-MiniLM-L6-V2')
embeddings = model.encode(chunks)

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="fest_docs")

collection.upsert(
    ids = [f"chunk_{i}" for i in range(len(chunks))],
    documents= chunks,
    embeddings = embeddings
)

print(f"Total{collection.count()} number of documents stored successfully.")

print(f"{len(chunks)} created  - > Shape of embeddings: {embeddings.shape}")

for i in range(len(embeddings)):
    print(f"emb_{i+1}: {embeddings[i][:5]}")
    print()
    print("-------------//-----------")  


question = "What are the main events?"
q_embedding = model.encode([question]).tolist()

results = collection.query(query_embeddings=q_embedding, n_results=1)

retrived = results["documents"][0]

print(retrived)