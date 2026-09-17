# 📚 Chat With Your PDFs — RAG PDF Chatbot

A simple **PDF Question-Answering application** built with **Streamlit, LangChain, Hugging Face Embeddings, FAISS, and Google Gemini**.

Upload one or multiple PDF files, process them, and ask questions about their content. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from your PDFs before generating an answer.

---

## 🚀 Features

- 📄 Upload multiple PDF files
- 🔍 Extract text from PDF documents
- ✂️ Split documents into smaller chunks
- 🧠 Generate embeddings using Hugging Face
- 🗂️ Store embeddings in a FAISS vector database
- 🔎 Perform similarity search to retrieve relevant content
- 🤖 Generate answers using Google Gemini
- 💬 Simple Streamlit chat interface
- 📝 Maintain chat history during the session

---

## 🏗️ Architecture

The application follows a basic RAG pipeline:

```text
                 ┌─────────────────┐
                 │   Upload PDFs   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Extract Text   │
                 │   using PyPDF2  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Text Splitting │
                 │ Recursive Split │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Hugging Face    │
                 │   Embeddings    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  FAISS Vector   │
                 │      Store      │
                 └────────┬────────┘
                          │
                   User Question
                          │
                          ▼
                 ┌─────────────────┐
                 │ Similarity      │
                 │    Search       │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Google Gemini   │
                 │      LLM        │
                 └────────┬────────┘
                          │
                          ▼
                    Final Answer
