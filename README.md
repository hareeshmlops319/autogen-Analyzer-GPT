# Data Analyser Agent

An **AI-powered Data Analyser Agent** built to explore, analyze, and summarize digital datasets using an agent-based architecture. The agent combines LLM reasoning with programmatic execution to answer analytical questions, run computations, and generate insights interactively.

This project is designed for **data analysis, automation, and agentic workflows**, and can be run locally or in Docker with a Streamlit UI.

---

## Features

- 🤖 **Agentic architecture** (Analyzer + Code Executor)
- 📊 **Data analysis on demand** (CSV, JSON, structured data)
- 🧠 **LLM-powered reasoning** for insights and summaries
- 🧪 **Safe code execution** using isolated Docker containers
- 🌐 **Streamlit UI** for interactive analysis
- ⚡ **Async-first design** for better performance

---

## Architecture Overview

```
User (UI / CLI)
   │
   ▼
Analyzer Agent (LLM)
   │  ── decides reasoning steps
   ▼
Code Executor Agent
   │  ── runs Python safely
   ▼
Docker Container
   │
   ▼
Results → Analyzer → User
```

### Key Components

| Component | Description |
|--------|-------------|
| **Analyzer Agent** | Interprets user queries and decides actions |
| **Code Executor Agent** | Executes Python code in isolation |
| **Docker Runtime** | Ensures safe and reproducible execution |
| **Streamlit App** | UI for uploading data and asking questions |

---

## Tech Stack

- **Python 3.10+**
- **Streamlit** (UI)
- **AutoGen / AgentChat** (multi-agent orchestration)
- **OpenAI-compatible LLMs**
- **Docker** (secure code execution)
- **AsyncIO**

---

## Project Structure

```
Analyser-GPT/
│
├── agents/
│   ├── analyzer_gpt.py
│   ├── code_executor_agent.py
│
├── config/
│   ├── openai_utilities.py
│   ├── docker_utils.py
│
├── app.py              # Streamlit entry point
├── requirements.txt
├── README.md
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-org/data-analyser-agent.git
cd data-analyser-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set environment variables
```bash
export OPENAI_API_KEY="your_api_key"
```

---

## Running the Application

### Run Streamlit UI locally
```bash
streamlit run app.py
```

Open browser at:
```
http://localhost:8501
```

---

## Using the Data Analyser Agent

1. Upload a dataset (CSV / JSON)
2. Ask natural language questions like:
   - *"Summarize this dataset"*
   - *"Find correlations"*
   - *"Detect missing values"*
   - *"Plot sales trend over time"*
3. The Analyzer Agent decides whether code execution is required
4. Results are computed and explained in plain English

---

## Docker-Based Code Execution

The Code Executor Agent runs Python inside a Docker container to:
- Prevent unsafe execution
- Isolate dependencies
- Ensure reproducibility

Docker lifecycle is managed automatically:
- Container start
- Code execution
- Result capture
- Container stop

---

## Configuration

### Model Configuration
Edit `config/openai_utilities.py`:
- Model name
- Temperature
- Max tokens

### Docker Configuration
Edit `config/docker_utils.py`:
- Base image
- Resource limits

---

## Security Notes

- ⚠️ Code execution is **automatic by default**
- For production, enable **manual approval** for executor agents
- Always restrict Docker permissions

---

## Common Issues

### Docker not running
```text
Error: Cannot connect to the Docker daemon
```
➡ Start Docker Desktop

---

### Streamlit not found
```bash
pip install streamlit
```

---

## Roadmap

- [ ] Add data visualization gallery
- [ ] Approval-based code execution
- [ ] Multi-dataset comparison
- [ ] Cloud deployment (GCP / AWS)
- [ ] Persistent memory for agents

---

## Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

## License

MIT License

---

## Author

**Hareesh Yalamasetty**  
AI / MLOps / Cloud Enthusiast



