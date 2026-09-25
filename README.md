# NotebookLM MCP Integration & Ad Library Workspace

This workspace is fully configured with the **Google NotebookLM MCP (Model Context Protocol) Server** and supporting tools.

---

## 🛠️ What Was Installed & Configured

1. **Dedicated Python Virtual Environment (`.venv`)**:
   - `notebooklm-py` with `[mcp]`, `[browser]`, and `[cookies]` extras.
   - FastMCP & MCP Protocol (v1.30.0+).
   - Playwright Chromium browser bundle.
   - `rookie-cookies` for extracting browser session cookies if desired.
   - Pinned dependencies saved to [`requirements.txt`](file:///d:/WORK/AI/Google%20Notebook/requirements.txt).

2. **MCP Server Configurations**:
   - [`.agents/mcp_config.json`](file:///d:/WORK/AI/Google%20Notebook/.agents/mcp_config.json): Workspace-level Antigravity MCP definition.
   - [`.agents/plugins/notebooklm/plugin.json`](file:///d:/WORK/AI/Google%20Notebook/.agents/plugins/notebooklm/plugin.json) & [`.agents/plugins/notebooklm/mcp_config.json`](file:///d:/WORK/AI/Google%20Notebook/.agents/plugins/notebooklm/mcp_config.json): Plugin-level packaging.
   - [`.vscode/mcp.json`](file:///d:/WORK/AI/Google%20Notebook/.vscode/mcp.json): IDE workspace-level MCP registry.

3. **Workspace Skill & Helper Scripts**:
   - [`.agents/skills/notebooklm/SKILL.md`](file:///d:/WORK/AI/Google%20Notebook/.agents/skills/notebooklm/SKILL.md): Antigravity skill reference for NotebookLM.
   - [`ad_library.py`](file:///d:/WORK/AI/Google%20Notebook/ad_library.py): Convenient CLI helper for managing Ad Library research, sources, and queries.

---

## 🔑 One-Time Authentication

Google NotebookLM requires an authenticated Google session. Run **one** of the following in your PowerShell terminal:

### Option A: Interactive Browser Login (Recommended)
```powershell
.\.venv\Scripts\python.exe ad_library.py login
# or directly:
.\.venv\Scripts\notebooklm.exe login --browser chrome
```
*A browser window will open. Simply sign into your Google account, and your session tokens will be automatically saved locally to `~/.notebooklm/profiles/default/storage_state.json`.*

### Option B: Automatic Cookie Extraction from Installed Chrome
If you are already logged into Google NotebookLM in Google Chrome:
```powershell
.\.venv\Scripts\notebooklm.exe login --browser-cookies chrome
```

### Check Authentication Status
```powershell
.\.venv\Scripts\python.exe ad_library.py check-auth
```

---

## 🚀 Available MCP Tools (38 Tools)

Once authenticated, Antigravity and your AI agents have direct access to:

| Category | Tools | Description |
| :--- | :--- | :--- |
| **Notebooks** | `notebook_list`, `notebook_create`, `notebook_describe`, `notebook_rename`, `notebook_delete` | Manage notebook containers |
| **Sources** | `source_list`, `source_add`, `source_read`, `source_rename`, `source_delete`, `source_wait` | Ingest web URLs, files, Google Drive docs, and raw text |
| **Grounded Chat** | `chat_ask`, `chat_start`, `chat_status`, `chat_cancel`, `chat_configure`, `suggest_prompts` | Zero-hallucination queries grounded in ingested sources with citations |
| **Studio & Export** | `studio_generate`, `studio_status`, `studio_download`, `note_save` | Generate Audio Overviews (podcasts), slide decks, mind maps, quizzes, and notes |
| **Deep Research** | `research_start`, `research_status`, `research_import` | Automated web and source research workflows |

---

## 📊 Ad Library Workflow Example

To organize and analyze ads (e.g. from Meta Ad Library or competitor ad copies):

```powershell
# 1. Create a notebook for Ad Research
.\.venv\Scripts\python.exe ad_library.py create --name "Competitor Ad Library"

# 2. Select the notebook
.\.venv\Scripts\python.exe ad_library.py use "Competitor Ad Library"

# 3. Ingest ad links or competitor research pages
.\.venv\Scripts\python.exe ad_library.py add-source "https://example.com/ad-case-study"

# 4. Ask grounded marketing and creative questions
.\.venv\Scripts\python.exe ad_library.py ask "What are the core pain points, hooks, and CTAs used across these ads?"
```
