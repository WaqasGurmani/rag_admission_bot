# 🎓 College Admission Counselor (RAG Chatbot)

## Project Overview
This project is a professional Retrieval-Augmented Generation (RAG) based chatbot
designed to provide accurate, document-grounded admission guidance for College.

The system works completely locally using FAISS for retrieval and Ollama-based LLMs
(Mistral / LLaMA), ensuring zero cost, privacy, and offline capability.

## Author
Waqas Gurmani
AI Engineer | RAG & LLM Specialist

## Key Features
- PDF-based knowledge ingestion
- Semantic search using FAISS
- Local LLM inference (Ollama)
- English & Roman Urdu support (single-language response)
- Interactive Streamlit chat UI
- Professional dark-themed frontend

## Tech Stack
- Python
- LangChain
- FAISS
- Sentence Transformers
- Ollama (Mistral / LLaMA)
- Streamlit

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run data preparation notebook once
3. Start UI:
   streamlit run app.py

## License
Educational & demonstration use.
