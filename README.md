# Sleeping Capsule MCP Server

A Python Model Context Protocol (MCP) server built using MCP SDK 2.x and Streamable HTTP transport.

## Features

The server provides two tools:

- `say_hello(name)` — Returns a greeting.
- `get_available_timeslots()` — Returns available sleeping capsule timeslots.

## Requirements

- Python 3.11 or later
- MCP Python SDK 2.x
- Railway hosting account

## Local Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python server.py
```

## Railway Deployment

1. Push the project to a GitHub repository.
2. Open Railway and create a new project.
3. Select **Deploy from GitHub Repo**.
4. Choose the repository.
5. Railway will detect `requirements.txt` and install the Python dependencies.
6. Railway will execute `python server.py` using the configured start command.
7. Configure the HTTP server to listen on `0.0.0.0` and Railway's `PORT` environment variable.
8. Generate a public domain under Railway's Networking settings.

## MCP Connection

Configure your MCP client to use Streamable HTTP.

Endpoint:

`https://YOUR-RAILWAY-DOMAIN/mcp`

Replace the placeholder with the actual Railway-generated domain.

## Security

The demonstration tools do not require authentication. Before adding real booking or customer-data functionality, implement authentication, authorization, and appropriate rate limiting.