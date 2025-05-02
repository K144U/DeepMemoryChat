DeepMemoryChat 🧠💬

DeepMemoryChat is a sophisticated AI chatbot project leveraging the DeepSeek-R1-Distill-Qwen-1.5B language model. It combines short-term contextual awareness with long-term memory retention using FAISS vector storage, providing highly contextualized and personalized interactions.

🌟 Features

Short-term Memory: Maintains conversational context for the latest 3 user inputs, ensuring smooth and contextually relevant interactions.

Long-term Memory: Uses FAISS for storing and retrieving past interactions, questions, preferences, and personal details, creating a personalized and evolving chatbot experience.

Open Source Model: Built upon the efficient DeepSeek-R1-Distill-Qwen-1.5B model.

Simple Interface: Easy-to-use command-line interface for quick and straightforward interactions.

🚀 Getting Started

Prerequisites

Python 3.8+

GPU recommended (works on CPU with reduced performance)

Installation

Clone this repository:

git clone <repository-url>
cd DeepMemoryChat

Install dependencies:

pip install transformers torch sentence-transformers faiss-cpu huggingface_hub

Authenticate with Hugging Face:

from huggingface_hub import notebook_login
notebook_login()

Usage

Run the chatbot:

python DeepMemoryChat.py

Upon starting, enter your user ID and interact directly from your terminal. Type exit or quit to close the chatbot.

⚙️ How it Works

DeepMemoryChat integrates:

SentenceTransformers for generating text embeddings.

FAISS for efficient vector storage and similarity searches.

DeepSeek-R1-Distill-Qwen-1.5B model for generating natural and intelligent responses.

📁 Project Structure

DeepMemoryChat/
├── DeepMemoryChat.ipynb   # Jupyter Notebook with implementation details
├── DeepMemoryChat.py      # Standalone Python script (optional conversion from notebook)
├── README.md              # Project documentation

🛠 Contributing

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.
