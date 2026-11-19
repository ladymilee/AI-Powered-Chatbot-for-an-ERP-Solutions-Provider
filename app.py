"""Sanitised portfolio example of a retrieval-augmented property management chatbot.

Requires a prebuilt, trusted local FAISS index. This script does not build the index.
"""
import os
from pathlib import Path

import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

st.title("Property Management Information Assistant")

if not os.getenv("OPENAI_API_KEY"):
    st.error("Set OPENAI_API_KEY in your environment before running the application.")
    st.stop()

index_path = Path(os.getenv("FAISS_INDEX_PATH", "faiss_index"))
if not index_path.is_dir():
    st.error("A prebuilt FAISS index is required. Set FAISS_INDEX_PATH to its folder.")
    st.stop()

# Only load a FAISS index created by you or another trusted source.
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local(
    str(index_path), embeddings, allow_dangerous_deserialization=True
)
model = ChatOpenAI(model_name="gpt-4", temperature=0.5)
qa_chain = RetrievalQA.from_chain_type(
    llm=model, retriever=vectorstore.as_retriever()
)

if "history" not in st.session_state:
    st.session_state.history = []

context = (
    "You are an information assistant for a property management business. "
    "Provide clear, concise answers based on available information. "
    "If the information is unavailable, suggest visiting the business contact page. "
)

question = st.chat_input("Ask a question")
if question:
    full_prompt = f"{context} User's query: {question}"
    answer = qa_chain.run(full_prompt)
    st.session_state.history.extend([
        {"role": "user", "message": question},
        {"role": "assistant", "message": answer},
    ])

for message in st.session_state.history:
    st.chat_message(message["role"]).write(message["message"])
