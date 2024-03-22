import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings

# Set up data directory
data_dir = "data"

# Load existing vector store
persist_directory = "chroma_db"
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=GPT4AllEmbeddings.from_pretrained("gpt4all-lora-quantized"))

# Add new documents
loader = DirectoryLoader(data_dir, recursive=True)
new_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
new_texts = text_splitter.split_documents(new_documents)

# Add new texts to the vector store
vectorstore.add_texts(new_texts)

# Export the vector store
vectorstore.persist()
print("Vector store updated and persisted successfully!")
