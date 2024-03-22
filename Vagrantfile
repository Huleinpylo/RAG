# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "8192"
    vb.cpus = 4
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3 python3-pip python3-venv git wget

    # Create and activate a virtual environment
    python3 -m venv /home/vagrant/env
    source /home/vagrant/env/bin/activate

    # Install required Python packages
    pip install langchain chroma-db gpt4all-bindings

    # Download and extract GPT4All model
    mkdir /home/vagrant/models
    wget https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized.bin -O /home/vagrant/models/gpt4all-lora-quantized.bin

    # Create data directory
    mkdir -p /home/vagrant/data

    # Clone the RAG system repository
    git clone https://github.com/Huleinpylo/RAG.git /home/vagrant/rag-system

    echo "Installation and pre-configuration completed successfully!"
    echo "Next steps:"
    echo "1. Place your documents (PDFs, Word, Excel, Markdown, etc.) in the '/home/vagrant/data' directory, organized by themes/folders."
    echo "2. Run the data ingestion and indexing script in '/home/vagrant/rag-system' to create the vector store."
    echo "3. Start the RAG system and interact with it."
  SHELL
end