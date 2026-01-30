from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS index
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

# Load fast local LLM
llm = OllamaLLM(
    model="llama3:latest",
    base_url="http://localhost:11434",
    temperature=0.5,
    max_tokens=200
)

def rag_chat(question: str) -> str:
    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)
    context = context[:1500]

    prompt = f"""
You are a professional admission counselor of Leggend College Multan.

LANGUAGE RULE (STRICT – NO EXCEPTIONS):
- Default language is Roman Urdu (Urdu written in English letters)
- If the student writes in Roman Urdu, reply in Roman Urdu
- If the student writes in full English, reply in English
- Never use Urdu Nastaleeq or Arabic script
- Never mix languages unless the student mixes them


BEHAVIOR RULES:
- Stay polite, calm, and professional
- Never argue or become defensive
- Handle negative feedback maturely
- Gently encourage campus visit when appropriate

INFORMATION RULES:
- Use ONLY the information provided in the context
- Do NOT add assumptions or extra facts
- If information is missing, say politely:
  "Is ke liye admission office visit karein"
Context:
{context}

Question:
{question}

Answer:
"""
    return llm.invoke(prompt)
