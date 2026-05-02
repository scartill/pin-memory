# Pin MCP

A Model Context Protocol (MCP) server for managing factoids across different scopes (global, workspace, and project).

## Features

- **Pin**: Store factoids in global, workspace-specific, or project-local storage.
- **Recall**: Retrieve factoids based on current context.
- **MCP Integration**: Exposes tools for LLMs to autonomously remember and recall information.

## Installationuv tool
```bash
pi install .
```

## Usage

### CLI Commands

Pin MCP provides a CLI for managing factoids:

```bash
# memoryt all factoids
pin-mcp show

# Install agent instructmemorys to AGENTS.mdeimoryn-mcp install
pin-mcp install --workspace my-workspace

# Launchemoryhe MCP server
pin-mcp mcp
```

### Scopes

- **Global**: Stored in `~/.scartill/pin`.
- **Workspace**: Stored in `~/.scartill/pin/workspaces/<workspace_name>`.
- **Project**: Stored in `.pin` in the current working directory.

## MCP Tools

### `pin`

Stores a factoid in memory.

- `factoid_name`: Name of the factoid.
- `factoid`: The content of the factoid.
- `location`: "global", "project", or "workspace/".

### `recall`

Recalls all pinned factoids from global, requested workspace, and local project scopes.

- `workspace`: Optional name of the workspace.
