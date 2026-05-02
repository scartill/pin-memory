# Pin Memory

A Model Context Protocol (MCP) server for managing factoids across different scopes (global, workspace, and project).

## Features

- **Pin**: Store factoids in global, workspace-specific, or project-local storage.
- **Recall**: Retrieve factoids based on current context.
- **MCP Integration**: Exposes tools for LLMs to autonomously remember and recall information.

## Installation

Using `uv` (recommended):

```bash
# Install as a global tool
uv tool install .

# Or run directly
uv run pin-memory mcp
```

## Usage

### CLI Commands

Pin Memory provides a CLI for managing factoids:

```bash
# List all factoids
pin-memory show

# Install agent instructions to AGENTS.md
pin-memory install --workspace my-workspace

# Launch the MCP server
pin-memory mcp
```

### Scopes

- **Global**: Stored in `~/.scartill/pin`.
- **Workspace**: Stored in `~/.scartill/pin/workspaces/<workspace_name>`.
- **Project**: Stored in `.pin` in the current working directory.

## MCP Configuration

To use this with an MCP client (e.g. Claude Desktop, Gemini CLI), add it to your configuration:

```json
{
  "mcpServers": {
    "pin-memory": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/path/to/pin-memory",
        "run",
        "pin-memory",
        "mcp"
      ]
    }
  }
}
```

## MCP Tools

### `pin`

Stores a factoid in memory.

- `factoid_name`: Name of the factoid.
- `factoid`: The content of the factoid.
- `location`: "global", "project", or "workspace/<name>".

### `recall`

Recalls all pinned factoids from global, requested workspace, and local project scopes.

- `workspace`: Optional name of the workspace.

## Development

```bash
# Clone the repository
git clone https://github.com/scartill/pin-memory.git
cd pin-memory

# Sync dependencies
uv sync

# Run tests (if applicable)
uv run pytest
```
