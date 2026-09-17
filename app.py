# ---------------------------------------------------
# Imports
# ---------------------------------------------------
import os

from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()


os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


def get_pdf_text(pdf_paths):
    text = ""
    for path in pdf_paths:
        pdf_reader = PdfReader(path) #Mimicing a double click on the file
        for page in pdf_reader.pages:
            text += page.extract_text() or "" #For every page in the pdf, extract text and append to text variable
    return text


def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return splitter.split_text(text)


def get_vector_store(text_chunks):
    # Initialize Hugging Face embedding model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings) #Convert the text to embeddings
    vector_store.save_local("faiss_index") #Local storage of vector DB


def get_conversational_chain():
    prompt_template = """
    Answer only in a simple, plain-text sentence.
    Use the provided context to answer the question directly.
    If the answer is not in the context, say "Answer is not available in the context."

    Context:\n{context}\n
    Question:\n{question}\n
    Answer:
    """
    # Use Gemini Flash for fast, cost-efficient responses
    #Generalised way/modularised way of prompting
    model = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = prompt | model | StrOutputParser()
    return chain


def chat_with_pdf(question):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(question)
    chain = get_conversational_chain()
    response = chain.invoke({"context": docs, "question": question})
    return response


st.title("💬 Chat with Your PDFs using Hugging Face + Gemini (RAG) + Vector db(FAISS)")

# Sidebar: File Upload
with st.sidebar:
    st.header("📄 Upload PDFs")
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    # Process PDFs button
    if st.button("Process PDFs") and uploaded_files:
        file_paths = []
        for file in uploaded_files:
            with open(file.name, "wb") as f:
                f.write(file.read())
                file_paths.append(file.name)

        raw_text = get_pdf_text(file_paths) # I am getting all the text for all the files that I uploaded
        chunks = get_text_chunks(raw_text) # chunked text
        get_vector_store(chunks)
        st.success("✅ PDFs processed and indexed successfully!")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Main input area
st.header("Ask a Question")
question = st.text_input("Your Question")

# Submit question
if st.button("Submit") and question:
    answer = chat_with_pdf(question)
    st.session_state.history.append((question, answer))

# Display Q&A
for q, a in st.session_state.history[::-1]:
    st.markdown(f"**Q:** {q}")
    st.markdown(f"**A:** {a}")
