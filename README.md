# Smart LLM Council MCP Server

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MCP](https://img.shields.io/badge/MCP-Protocol-blue?style=for-the-badge)
![Universal](https://img.shields.io/badge/Universal-Compatible-green?style=for-the-badge)

A smart Model Context Protocol (MCP) server that provides a 3-stage LLM deliberation council. It automatically detects its environment and configures the best available agents for the task.

## 🚀 Key Features
- **Auto-Discovery**: Scans for Antigravity, Claude Code, Codex, or Generic environments.
- **Dynamic Tiering**: Maps agents (Gemini 3.1 Pro, Sonnet 4.6, etc.) to council roles based on availability.
- **Silent Auto-Setup**: Registers itself in your `mcp_config.json` on the first run.
- **Zero-Config**: Auto-installs missing dependencies (like `mcp` library).

## 🛠️ Quick Start

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd llm-council-mcp
```

### 2. Auto-Install & Run
Just run the server once. It will register itself and install any missing dependencies:
```bash
python server.py
```

### 3. Usage
Once registered, you will have a new tool available in your agent: `deliberate`.

## 🌐 Supported Environments
- **Antigravity**: Uses Gemini 3.1 Pro (High/Low) and Flash 3.
- **Claude Code**: Uses Claude 3.5 Sonnet and Haiku.
- **Generic**: Uses OpenRouter, OpenAI, or Anthropic environment variables.

---
Created for the Antigravity Agentic Ecosystem.
