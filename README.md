MCP Hercules Copilot

A LangGraph-based test generation and execution framework that turns your natural language into working Gherkin tests — with optional test execution via TestZeus Hercules, powered by MCP agents and Groq/OpenAI LLMs.

Built by @Shadowcyng

Features

Generate Gherkin test cases from natural language prompts

Create project directories and test files Hercules expects

(Optionally) run tests using TestZeus Hercules (mock or real)

Chat-style Copilot UI to interact naturally

Uses MCP tools to expose agent capabilities cleanly

Full LangGraph + LangChain + Groq + FastAPI stack

Requirements

Python 3.10+

Optional: Groq API key or OpenAI API key

testzeus-hercules installed if using real test execution (optional)

I mocked the response because I did not have access to a paid OpenAI key

Project Structure

mcp-hercules/
├── copilot/
│   ├── agent.py             # LangGraph Copilot agent (MCP tool-aware)
│   ├── tools.py             # suggest_test, create_test, run_test MCP tools
│
├── server/
│   ├── main.py              # Entrypoint for MCP server
│   ├── endpoints.py         # FastAPI routes for agent invocation
│   ├── agents/              # Gherkin generator agent
│   └── nodes/               # create folder + run test logic
│
├── tests_storage/           # Where test folders and outputs are saved
│
├── .env                     # Environment variables (see below)
├── requirements.txt
└── README.md

.env File Format

# LLM to use (Groq models or OpenAI-compatible ones)
MODEL=llama3-70b-8192

# Groq API Key (required for Groq models)
GROQ_API_KEY=your_groq_key_here

# Optional: fallback to OpenAI
OPENAI_API_KEY=your_openai_key_here

Installation & Setup

git clone https://github.com/Shadowcyng/mcp-hercules.git
cd mcp-hercules

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

Run the Server

uvicorn server.main:app --reload

This exposes REST APIs at:

Endpoint

Description

POST /agent/suggest_test

Generate Gherkin from description

POST /agent/create_test

Create test + folder structure

POST /agent/run_test_from_folder

Run test via Hercules or mock

GET /get_tests?test_name=...

List tests by name

Run Agent:

python copilot/agent.pyMock vs Real Execution

The system mocks Hercules CLI by default (returns dummy HTML/XML reports). To run real tests:

Install Hercules:

pip install testzeus-hercules

In run_test_node.py, uncomment:

subprocess.run([...])

MCP Tool Summary

Tool

Arguments

Purpose

suggest_test

description: str

Generates Gherkin code

create_test

test_name, description, run

Creates project structure & test

run_test

run_id, project_path

Runs existing test from disk

These are exposed via MCP and callable from LangGraph agents or REST endpoints.

Agent Workflow

[ User Prompt ]
      ↓
[ Copilot CLI / UI ]
      ↓
[ LangGraph Agent (React-style) ]
      ↓
[ MCP Tool Server ]
   ├─ suggest_test → Generates Gherkin
   ├─ create_test  → Creates files/folders
   └─ run_test     → Runs or mocks execution

Roadmap



Credits

Built with:

LangGraph

LangChain

MCP

Streamlit (optional)

TestZeus Hercules

Groq & OpenAI LLMs

Contact

For questions, contributions, or feedback, reach out to @Shadowcyng.

