# 📚 Chat With Your PDFs — RAG PDF Chatbot

A simple **PDF Question-Answering application** built with **Streamlit, LangChain, Hugging Face Embeddings, FAISS, and Google Gemini**.

Upload one or multiple PDF files and ask questions about their content. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from your documents before generating answers.

## 🚀 Live Demo

👉 **[Try MultiPDF Chatbot](YOUR_STREAMLIT_APP_URL)**

> Replace `YOUR_STREAMLIT_APP_URL` with your deployed Streamlit URL.

## 📥 Download & Run Locally

### Option 1 — Download the Project

**[⬇️ Download MultiPDF Chatbot](https://github.com/DhamodharThyiagarajan/MultiPdf-s/archive/refs/heads/main.zip)**

Download the ZIP file, extract it, and open the project folder.

### Option 2 — Clone the Repository

```bash
git clone https://github.com/DhamodharThyiagarajan/MultiPdf-s.git

cd MultiPdf-s
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 Configure API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🚀 Features

* 📄 Upload multiple PDF files
* 🔍 Extract text from PDF documents
* ✂️ Split documents into smaller chunks
* 🧠 Generate embeddings using Hugging Face
* 🗂️ Store embeddings in a FAISS vector database
* 🔎 Perform similarity search
* 🤖 Generate answers using Google Gemini
* 💬 Interactive Streamlit chat interface
* 📝 Maintain chat history during the session

---

## 🧠 How It Works

The application follows a **Retrieval-Augmented Generation (RAG)** pipeline:

```text
                ┌─────────────────┐
                │   Upload PDFs   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Extract Text   │
                │    from PDFs    │
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
                │ FAISS Vector DB │
                └────────┬────────┘
                         │
                  User Question
                         │
                         ▼
                ┌─────────────────┐
                │ Similarity Search│
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
```

## 🛠️ Tech Stack

| Technology    | Purpose                  |
| ------------- | ------------------------ |
| Python        | Application development  |
| Streamlit     | Web interface            |
| LangChain     | RAG pipeline             |
| Hugging Face  | Text embeddings          |
| FAISS         | Vector similarity search |
| Google Gemini | AI-generated answers     |
| PyPDF2        | PDF text extraction      |

## 📂 Project Structure

```text
MultiPdf-s/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
└── ...
```

## 💡 Use Cases

* 📚 Ask questions about study materials
* 📄 Search through large PDF documents
* 📑 Analyze reports and documentation
* 🎓 Research and academic documents
* 💼 Query business documents
* 📖 Summarize and understand uploaded PDFs

## 🔐 Environment Variables

The application requires a Google Gemini API key.

```env
GOOGLE_API_KEY=your_api_key_here
```

**Never commit your `.env` file or API keys to GitHub.**

## 👨‍💻 Author

**Dhamodhar Thiyagarajan**

GitHub: [@DhamodharThyiagarajan](https://github.com/DhamodharThyiagarajan)

---

⭐ If you find this project useful, consider giving the repository a star!
