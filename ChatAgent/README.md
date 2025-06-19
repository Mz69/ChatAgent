# 🔍 ChatAgent – AI Research Assistant with LangGraph + Firecrawl MCP

ChatAgent is an intelligent research assistant that automates technical research using:
- 🧠 OpenAI GPT-4
- 🌐 Firecrawl MCP tools (scraping, searching, deep research)
- 🔗 LangChain and LangGraph
- 🛠️ Structured agents with React-style workflows

---

## 🚀 Features

- 🔍 Automatically searches and scrapes technical tools & companies using Firecrawl
- 📊 Extracts tool names from messy content using LLMs
- 🧠 Analyzes tools for open-source status, pricing model, tech stack, and more
- 🤖 Generates final business recommendations via a LangGraph state machine
- 🧱 Modular: swap LLMs, tools, prompts, and workflows with minimal changes

---

## 🧠 How It Works

1. **User Query →** e.g., “database monitoring tools”
2. **Firecrawl Search →** Finds relevant pages
3. **Firecrawl Scrape →** Pulls markdown content
4. **LLM Tool Extraction →** Extracts company names
5. **LLM Company Analysis →** Evaluates each tool’s capabilities
6. **LLM Summary →** Delivers final recommendations

---