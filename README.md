Practice building a local ai agent that reviews the type of backend framework to use for a specific project

## Components Used

- **[Llama3.2](https://ollama.com/library/llama3)** — Main reasoning LLM (via `ollama`)
- **[mxbai-embed-large](https://ollama.com/library/mxbai-embed-large)** — Embedding model for document similarity
- **LangChain** — Framework to manage chains, retrievers, and vector stores
- **Chroma** — Lightweight vector store for local document retrieval

## How It Works

1. **Vectorization**: Reviews or documentation snippets are embedded using `mxbai-embed-large` and stored in Chroma vector DB.
2. **Retrieval**: When a user asks a question, the query is embedded and compared to stored vectors via similarity search.
3. **Reasoning**: Top relevant snippets are passed to `llama3.2` which evaluates them and responds with the recommended backend framework.

## Installation

Make sure [Ollama](https://ollama.com/download) is installed and running.

```bash
ollama pull llama3.2
ollama serve
ollama pull mxbai-embed-large
```
Set up virtual environment, activate venv, install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run Program
```bash
python3 main.py
```

