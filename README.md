# Property Management Information Chatbot

A **sanitised portfolio demonstration** of a retrieval-augmented question-answering chatbot intended for integration into a property management company's website. No company names, confidential documents, credentials, or vector indexes are included.

## Architecture

1. Business documents are prepared and embedded into numerical vectors (index-building code is **not included**).
2. A **prebuilt local FAISS index** holds searchable vectors and associated text references.
3. LangChain retrieves relevant passages for a visitor's question.
4. OpenAI GPT-4 generates a response using retrieved context.
5. Streamlit displays the conversation and keeps session history.

**Original project infrastructure:** The project used Amazon EC2 for application execution and Amazon S3 for information storage. This public example contains the chatbot application logic only; it does not include AWS provisioning, S3 access code, the website integration, or index construction.

## Run locally

1. Create a Python virtual environment and install `pip install -r requirements.txt`.
2. Set `OPENAI_API_KEY` as an environment variable. Never commit a real API key.
3. Set `FAISS_INDEX_PATH` to a **trusted, prebuilt** FAISS index directory compatible with the embedding model. The index is not included.
4. Run `streamlit run app.py`.

The application will not answer questions without an index. `FAISS.load_local` enables pickle deserialisation, so **never load an index from an untrusted source**.

## Notes

This repository demonstrates the architecture and application code, not a turnkey deployment. The code uses legacy LangChain imports consistent with the original project; dependency versions may require adjustment for your environment. No measured accuracy or live production deployment is claimed.

## Security

- Secrets are read from environment variables.
- `.gitignore` excludes local data, vector indexes, and credentials.
- Review all files and commit history before publishing.
