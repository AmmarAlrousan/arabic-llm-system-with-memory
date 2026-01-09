# ASM: Arabic LLM System Architecture with Memory and Reasoning

ASM (Arab Synthetic Mind) is a **research-oriented prototype** that explores the
design of an Arabic-focused Large Language Model (LLM) system with modular
**memory**, **reasoning guidance**, and **value alignment** layers.

This repository focuses on **LLM system architecture and prompt orchestration**,
not on building a production-ready chatbot or user interface.

---


## 🎯 Motivation
While modern LLMs demonstrate strong generative abilities, controlling:

- reasoning behavior,
- context persistence,
- ethical alignment,
- and Arabic-centric interaction

remains a challenge.

ASM addresses this by proposing a **layered architecture** that separates
high-level system concerns into independent, composable modules.

---

## 🧠 System Architecture
The system is structured around clear separation of responsibilities:

### Core
- **ASM Orchestrator**: constructs the system prompt and manages interaction with the LLM.

### Layers
- **Values Layer**: enforces ethical and cultural constraints.
- **Personality Layer**: controls tone and interaction style.
- **Reasoning Layer**: guides internal problem-solving behavior.
- **Dialogue Layer**: builds conversational context.
- **Memory Layer**: manages short-term and long-term memory persistence.

---

## 🔧 LLM Backend Configuration
ASM is **model-agnostic** and does not bundle any LLM weights.

The system communicates with a **local OpenAI-compatible LLM server**
(e.g., LM Studio, Ollama, llama.cpp server).

During development, the system was tested using **Qwen** as the backend model.

The active model is specified indirectly via the local server and referenced in:


core/config.py

```python
MODEL_NAME = "local-llm"
BASE_URL = "http://127.0.0.1:1234/v1"
```

Any compatible LLM (Qwen, LLaMA, Mistral, etc.) can be used by updating the
server configuration and model identifier.

📁 Repository Structure
asm-arabic-llm-architecture/
│

├── core/                 # LLM orchestration logic

├── layers/               # modular prompt and memory layers

├── interface/            # minimal prototype interface

├── memory/               # persistent memory storage

├── docs/                 # system overview and design notes

├── examples/             # sample conversations

├── requirements.txt

└── README.md

## 🖥 Interface

A minimal PyQt-based interface is included to demonstrate usability.

The interface is intentionally simple.
The research contribution lies in system design, not UI complexity.

## ⚙️ How to Run

Install dependencies:

  pip install -r requirements.txt


  Ensure a local OpenAI-compatible LLM server is running
  (e.g., LM Studio or Ollama).

# Run the prototype interface:

python interface/gui_pyqt.py

## 🧪 Research Context

This project serves as a system-level exploration of LLM behavior control and
human-centered AI design, particularly for Arabic language interaction.

It complements research in areas such as:

  affective computing,

  explainable AI,

  human-centered AI systems.

## 🚧 Limitations

  Prototype-level implementation.

  Not optimized for concurrency or scalability.

  Designed for experimentation and architectural exploration.

## 🔮 Future Work

  Web-based interface (e.g., Streamlit).

  Emotion-aware prompt adaptation.

  Multi-agent reasoning layers.

  Integration with perception modules (e.g., vision or emotion models).

## 📬 Contact

Ammar Alrousan
AI Student | Research-oriented
GitHub: https://github.com/AmmarAlrousan

Email: ammaraimaster@gmail.com
