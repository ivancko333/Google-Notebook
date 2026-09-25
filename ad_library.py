"""
Ad Library & NotebookLM Helper CLI
Provides high-level helpers to manage notebooks, add ad research sources,
and query grounded insights using Google NotebookLM.
"""

import sys
import subprocess
import argparse
from pathlib import Path

VENV_PYTHON = Path(__file__).parent / ".venv" / "Scripts" / "python.exe"
VENV_NOTEBOOKLM = Path(__file__).parent / ".venv" / "Scripts" / "notebooklm.exe"

def run_cmd(args):
    """Run notebooklm CLI command and stream output."""
    cmd = [str(VENV_NOTEBOOKLM)] + args
    result = subprocess.run(cmd)
    return result.returncode

def cmd_auth_check():
    """Verify NotebookLM authentication status."""
    return run_cmd(["auth", "check"])

def cmd_login(browser="chrome"):
    """Launch interactive login."""
    return run_cmd(["login", f"--browser={browser}"])

def cmd_list_notebooks():
    """List all notebooks in your account."""
    return run_cmd(["list"])

def cmd_create_ad_notebook(name="Ad Library"):
    """Create a new notebook for Ad Library research."""
    return run_cmd(["create", name])

def cmd_add_source(url_or_path):
    """Add a source (URL, text, or file) to the current active notebook."""
    return run_cmd(["source", "add", url_or_path])

def cmd_query(prompt):
    """Query the active notebook with grounded citations."""
    return run_cmd(["ask", prompt])

def main():
    parser = argparse.ArgumentParser(description="Ad Library & NotebookLM Workspace Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Auth commands
    subparsers.add_parser("check-auth", help="Check current authentication status")
    login_parser = subparsers.add_parser("login", help="Log into Google NotebookLM via browser")
    login_parser.add_argument("--browser", default="chrome", choices=["chrome", "chromium", "msedge"], help="Browser to use for login")

    # Notebook commands
    subparsers.add_parser("list", help="List all notebooks")
    create_parser = subparsers.add_parser("create", help="Create an Ad Library notebook")
    create_parser.add_argument("--name", default="Ad Library", help="Notebook name (default: 'Ad Library')")

    use_parser = subparsers.add_parser("use", help="Select active notebook context")
    use_parser.add_argument("notebook_id", help="Notebook ID or partial name")

    # Source commands
    add_parser = subparsers.add_parser("add-source", help="Add source (URL or file) to current notebook")
    add_parser.add_argument("target", help="URL or file path to add")

    list_sources_parser = subparsers.add_parser("list-sources", help="List sources in the notebook")

    # Query command
    ask_parser = subparsers.add_parser("ask", help="Ask a question grounded in the notebook sources")
    ask_parser.add_argument("prompt", help="Question or prompt to ask")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "check-auth":
        sys.exit(cmd_auth_check())
    elif args.command == "login":
        sys.exit(cmd_login(args.browser))
    elif args.command == "list":
        sys.exit(cmd_list_notebooks())
    elif args.command == "create":
        sys.exit(cmd_create_ad_notebook(args.name))
    elif args.command == "use":
        sys.exit(run_cmd(["use", args.notebook_id]))
    elif args.command == "add-source":
        sys.exit(cmd_add_source(args.target))
    elif args.command == "list-sources":
        sys.exit(run_cmd(["source", "list"]))
    elif args.command == "ask":
        sys.exit(cmd_query(args.prompt))

if __name__ == "__main__":
    main()
