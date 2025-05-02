
!pip install --quiet huggingface_hub
from huggingface_hub import notebook_login
notebook_login()  

# Cell 2: Core libraries
!pip install --quiet \
  transformers torch \
  sentence-transformers faiss-cpu \
  gradio

from collections import deque
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class MemoryManager:
    def __init__(self, embed_model_name="all-MiniLM-L6-v2"):
        self.ephemeral = deque(maxlen=3)                        
        self.embed = SentenceTransformer(embed_model_name)      
        dim = self.embed.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatL2(dim)                      
        self.texts = []                                          
    def add_message(self, text: str):
        self.ephemeral.append(text)
        emb = self.embed.encode(text, convert_to_numpy=True)
        self.index.add(np.array([emb], dtype="float32"))
        self.texts.append(text)

    def retrieve(self, query: str, k: int = 5):
        if not self.texts:
            return []
        q_emb = self.embed.encode(query, convert_to_numpy=True)
        D, I = self.index.search(np.array([q_emb], dtype="float32"), k)
        return [self.texts[i] for i in I[0] if i < len(self.texts)]


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B" 
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto",             
)


session_memories = {}  

def chat_with_memory(user_id: str, user_message: str) -> str:
    mem = session_memories.setdefault(user_id, MemoryManager())
    mem.add_message(user_message)

    short_term = list(mem.ephemeral)
    long_term  = mem.retrieve(user_message, k=5)

    prompt = "\n".join([
        "You are a helpful assistant.",
        "-- Ephemeral (last 3 messages):",
        *("  • " + m for m in short_term),
        "-- Long-term memories:",
        *("  • " + m for m in long_term),
        f"User: {user_message}",
        "Assistant:"
    ])

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    out = model.generate(
        **inputs,
        max_new_tokens=5000,
        temperature=0.7,
        top_p=0.9,
        eos_token_id=tokenizer.eos_token_id,
    )
    return tokenizer.decode(out[0, inputs.input_ids.shape[-1]:], skip_special_tokens=True)


user_id = input("Enter a user ID (any string): ").strip()
print(f"Hello, {user_id}! Type your messages below. Type 'exit' or 'quit' to stop.\n")

while True:
    msg = input(f"{user_id} >> ").strip()
    if msg.lower() in ("exit", "quit"):
        print("Goodbye!")
        break
    reply = chat_with_memory(user_id, msg)
    print(f"Bot >> {reply}\n")