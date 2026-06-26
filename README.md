# ResearchForge — Multi-Agent Academic Research Assistant

> **Kaggle AI Agents: Intensive Vibe Coding Capstone Project** · Freestyle Track

Ask any research question. Get a fully cited, AI-synthesized research report — in under a minute.

---

## Problem

Staying on top of academic literature is time-consuming and fragmented. A researcher must search multiple databases, read dozens of abstracts, cross-reference claims, and manually write a synthesis. ResearchForge automates this entire workflow using a coordinated pipeline of five specialized AI agents.

## Solution

ResearchForge orchestrates five Google ADK agents, each with a focused role:

| # | Agent | Role |
|---|---|---|
| 1 | **Search Agent** | Queries arXiv and the web for relevant papers and articles |
| 2 | **Reader Agent** | Extracts key findings, concepts, and gaps from raw sources |
| 3 | **Critic Agent** | Fact-checks claims and assigns an evidence reliability score |
| 4 | **Synthesis Agent** | Builds a coherent research narrative from validated findings |
| 5 | **Report Writer Agent** | Produces the final, cited, publication-ready report |

## Architecture

```
User Question
     │
     ▼
┌────────────────────────────────────────┐
│           Orchestrator                 │
│  (sequential pipeline coordinator)     │
└──┬─────────┬─────────┬────────┬───────┘
   │         │         │        │
   ▼         ▼         ▼        ▼
Search   Reader    Critic   Synthesis
Agent    Agent     Agent     Agent
   │         │         │        │
   └─────────┴────┬────┴────────┘
                  ▼
           Report Writer
                  │
                  ▼
           Final Report (Markdown)
```

Two **MCP Servers** expose the underlying tools:
- `mcp_servers/arxiv_server.py` — arXiv paper search via the `mcp` protocol
- `mcp_servers/web_search_server.py` — web search via Serper.dev

## Key Concepts Demonstrated

| Concept | Where |
|---|---|
| Multi-agent system (ADK) | `agents/` — 5 specialized agents + orchestrator |
| MCP Server | `mcp_servers/` — arxiv + web search MCP servers |
| Security features | `utils/security.py` — input sanitization, rate limiting, no key exposure |
| Deployability | Streamlit Cloud / Docker (see below) |
| Agent skills | Orchestration, tool use, sequential planning |

## Setup

### 1. Clone and install

```bash
git clone https://github.com/your-username/researchforge
cd researchforge
pip install -r requirements.txt
```

### 2. Configure environment variables

```bash
cp .env.example .env
# Edit .env and add your keys:
#   GOOGLE_API_KEY  — from https://aistudio.google.com/apikey
#   SERPER_API_KEY  — from https://serper.dev (optional, enables web search)
```

### 3. Run the app

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

### 4. Run MCP servers standalone (optional)

```bash
python mcp_servers/arxiv_server.py
python mcp_servers/web_search_server.py
```

## Deployment

### Streamlit Cloud (recommended)

1. Push to a public GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo.
3. Add `GOOGLE_API_KEY` and `SERPER_API_KEY` as secrets in the app settings.
4. Deploy — no server management required.

### Docker

```bash
docker build -t researchforge .
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY=your_key \
  -e SERPER_API_KEY=your_key \
  researchforge
```

## Security

- All user input is sanitized (control-character stripping, length cap).
- Rate limiting: max 10 pipeline runs per 60 seconds per process.
- API keys are never logged or included in agent outputs.
- MCP servers validate input before forwarding to external APIs.

## Tech Stack

- [Google ADK](https://google.github.io/adk-docs/) — agent framework
- [Gemini 2.0 Flash](https://ai.google.dev/) — underlying LLM
- [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) — tool servers
- [Streamlit](https://streamlit.io/) — web UI
- [arXiv API](https://arxiv.org/help/api/) — academic paper search
- [Serper.dev](https://serper.dev/) — web search

## Project Structure

```
researchforge/
├── app.py                    # Streamlit UI
├── requirements.txt
├── .env.example
├── agents/
│   ├── orchestrator.py       # Pipeline coordinator
│   ├── search_agent.py       # Finds sources
│   ├── reader_agent.py       # Extracts findings
│   ├── critic_agent.py       # Validates evidence
│   ├── synthesis_agent.py    # Builds narrative
│   └── report_writer.py      # Final report
├── mcp_servers/
│   ├── arxiv_server.py       # MCP: arXiv search
│   └── web_search_server.py  # MCP: web search
├── tools/
│   ├── arxiv_tools.py        # arXiv API wrapper
│   └── web_search_tools.py   # Serper API wrapper
└── utils/
    ├── security.py           # Input validation, rate limiting
    └── formatters.py         # Markdown helpers
```

---

*Built for the [Kaggle AI Agents: Intensive Vibe Coding Capstone](https://kaggle.com/competitions/vibecoding-agents-capstone-project)*
