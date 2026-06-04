# PsyDuck Chatbot 🦆

PsyDuck is a locally deployed, context-aware conversational AI chatbot built with Python. Instead of relying on external paid APIs, this project leverages open-source transformers to handle natural language understanding and generation completely on-device or within private cloud environments.

## 🧠 Core Architecture & LLM Details
- **Base Model:** `facebook/blenderbot-400M-distill`
- **Model Type:** Sequence-to-Sequence (Seq2Seq) Encoder-Decoder architecture
- **Parameters:** 400 Million
- **Why this architecture?** Utilizing a distilled student model allows the application to balance conversational intelligence with rapid inference speed (low latency), making it lightweight enough to run efficiently on standard compute instances without enterprise-grade GPU requirements.

## 🛠️ Tech Stack
- **Language:** Python
- **AI Libraries:** Hugging Face `transformers`, PyTorch
- **Backend Framework:** Flask micro-framework for serving the model endpoints
- **Frontend:** HTML5, CSS3, JavaScript (Static web interface interacting via REST API)

## ⚙️ How It Works (Under the Hood)
1. **Tokenization:** Incoming text strings from the user interface are parsed and converted into numerical token IDs.
2. **Context Vector Generation:** The Transformer **Encoder** processes these tokens simultaneously to build a mathematical representation (hidden states) of the conversation's semantic meaning.
3. **Autoregressive Text Generation:** The Transformer **Decoder** ingests the context vector and predicts the response word-by-word, iteratively feeding its own output back into itself until a complete, natural reply is generated.
