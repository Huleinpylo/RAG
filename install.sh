#!/bin/bash

# Install Python and required packages
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv

# Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

# Install required Python packages
pip install langchain chroma-db gpt4all-bindings

# Download and extract GPT4All model
mkdir models
wget https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized.bin -O models/gpt4all-lora-quantized.bin

# Create data directory
mkdir -p data

echo "Installation and pre-configuration completed successfully!"
echo "Next steps:"
echo "1. Place your documents (PDFs, Word, Excel, Markdown, etc.) in the 'data' directory, organized by themes/folders."
echo "2. Run the data ingestion and indexing script to create the vector store."
echo "3. Start the RAG system and interact with it."