---
name: notebooklm
description: Guide and instructions for Google NotebookLM MCP tools, CLI workflows, notebook creation, source ingestion, and grounded queries.
---

# NotebookLM MCP & CLI Guide

This workspace is integrated with Google NotebookLM (Gemini Notebook) via `notebooklm-py` and its built-in MCP server.

## Authentication (One-Time Setup)

Before querying or modifying notebooks, Google authentication must be active:

```powershell
# Interactive browser login via Chromium (opens Google sign-in)
.\.venv\Scripts\notebooklm.exe login

# Or extract existing cookies from your installed browser:
.\.venv\Scripts\notebooklm.exe login --browser-cookies chrome

# Check authentication status:
.\.venv\Scripts\notebooklm.exe auth check
```

## Available MCP Tools

Once authenticated, the following MCP tools are active:

| Tool | Description |
| :--- | :--- |
| `notebook_list` | Lists all existing notebooks with IDs and titles |
| `notebook_create` | Creates a new notebook with a title |
| `notebook_describe` | Fetches notebook AI summary and description |
| `notebook_delete` | Deletes a notebook by ID |
| `notebook_rename` | Renames an existing notebook |
| `source_list` | Lists all sources inside a notebook |
| `source_add` | Ingests URLs, raw text, or files into a notebook |
| `source_read` | Reads the content and summary of a source |
| `source_delete` | Removes a source from a notebook |
| `chat_ask` | Queries the notebook with grounded citations |
| `chat_start` / `chat_status` | Manages interactive multi-turn conversations |
| `studio_generate` | Generates Audio Overviews (podcasts), slide decks, study guides, mind maps |
| `note_save` | Saves notes and findings directly into the notebook |

## Common CLI Equivalents

You can also run commands directly in PowerShell:

```powershell
# List notebooks
.\.venv\Scripts\notebooklm.exe list

# Create a notebook
.\.venv\Scripts\notebooklm.exe create "Competitor Ad Research"

# Add a web source or link
.\.venv\Scripts\notebooklm.exe source add "<URL>"

# Ask grounded questions
.\.venv\Scripts\notebooklm.exe ask "Summarize the primary marketing angles in these ads"
```
