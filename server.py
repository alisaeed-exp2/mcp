
from mcp.server.mcpserver import MCPServer

# Initialize MCP server
mcp = MCPServer("Sleeping Capsule MCP Server")


@mcp.tool()
def say_hello(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}! Welcome to MCP."


@mcp.tool()
def get_available_timeslots() -> dict:
    """Return available sleeping capsule timeslots."""
    return {
        "CapsuleA": [
            "10:00-11:00",
            "11:00-12:00",
            "12:00-13:00"
        ],
        "CapsuleB": [
            "13:00-14:00",
            "14:00-15:00",
            "15:00-16:00"
        ]
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
