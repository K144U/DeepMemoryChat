# DeepMemoryChat 🧠💬

DeepMemoryChat is an intelligent AI chatbot built using the DeepSeek-R1-Distill-Qwen-1.5B language model. It combines short-term conversational context with long-term memory retention using FAISS vector search to deliver personalized and context-aware interactions.

## 🌟 Features

- Short-term Memory: Retains the last 3 user inputs for fluid multi-turn conversations.
- Long-term Memory: Stores and retrieves past interactions and preferences using FAISS for deep contextual continuity.
- Lightweight Model: Uses DeepSeek-R1-Distill-Qwen-1.5B for efficient, high-quality response generation.
- Simple CLI Interface: Runs from the terminal with no need for web UI.

## 🚀 Getting Started

### Prerequisites

Requires Python 3.8 or higher. A GPU is recommended for faster performance, but the model can also run on CPU with reduced speed.

### Installation

1. Clone the repository and navigate into it.  
2. Install the required Python libraries: transformers, torch, sentence-transformers, faiss-cpu, and huggingface_hub.  
3. Authenticate with Hugging Face using the notebook_login() method.

### Running the Chatbot

Run the DeepMemoryChat.py script. On launch, you'll be prompted for a user ID. You can then start chatting with the bot directly in your terminal. Type 'exit' or 'quit' to end the session.

## 💻 Using in Google Colab

You can also run this project in Google Colab:

1. Open the DeepMemoryChat.ipynb notebook in Colab.  
2. Change the runtime to GPU from the Runtime menu.  
3. Run all cells sequentially.  
4. In the final cell, enter a user ID and begin chatting in the terminal-style interface.

## ⚙️ How it Works

DeepMemoryChat uses SentenceTransformers to generate embeddings for each message. These embeddings are stored in a FAISS index for long-term memory retrieval. For response generation, the chatbot uses DeepSeek-R1-Distill-Qwen-1.5B, a lightweight yet capable language model that generates high-quality text. The last 3 user messages are retained in memory for conversational fluidity, while all messages are indexed for semantic recall.

## 📁 Project Structure

DeepMemoryChat/
├── DeepMemoryChat.ipynb – Notebook version of the chatbot  
├── DeepMemoryChat.py – Script version for CLI usage  
├── README.md – Project documentation

## 🛠 Contributing

Feel free to fork this repository, make changes, and submit a pull request. Contributions are welcome.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📫 Contact

Author: Your Name  
Email: your.email@example.com  
Repository: https://github.com/your-username/DeepMemoryChat
