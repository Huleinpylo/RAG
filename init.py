import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain.chains.question_answering import RetrievalQA

# Set up data directory
data_dir = "data"

# Load documents
loader = DirectoryLoader(data_dir, recursive=True)
documents = loader.load()

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Set up embeddings
embeddings = GPT4AllEmbeddings.from_pretrained("gpt4all-lora-quantized")

# Create vector store
persist_directory = "chroma_db"
vectorstore = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)

# Initialize retriever
retriever = vectorstore.as_retriever()

# Set up question-answering chain
qa = RetrievalQA.from_chain_type(
    llm=embeddings.gpt4all,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
)

print("RAG system initialized successfully!")
