from mcp.server.fastmcp import FastMCP

# Initialize MCP server with name
mcp = FastMCP("HeadlineNews")

# Define a tool to get today's headlines
@mcp.tool()
def get_headlines(category: str = "general") -> list[str]:
    """Return simulated headlines for the requested category"""
    category = category.lower()
    print(f"📰 [NewsTool] Request received for category: {category}")

    mock_news = {
        "general": [
            "Global markets rally on tech optimism",
            "Scientists develop new sustainable plastic",
            "UN calls for climate action at emergency summit"
        ],
        "sports": [
            "Local team wins regional championship",
            "Olympic committee announces new events",
            "Top athletes prepare for Paris 2024"
        ],
        "tech": [
            "Open-source AI models gain popularity",
            "Quantum computers pass new benchmark",
            "Tech giants invest in clean energy data centers"
        ]
    }

    return mock_news.get(category, ["No headlines available for this category."])

if __name__ == "__main__":
    print("🚀 HeadlineNews MCP Server running via stdio...")
    mcp.run(transport="stdio")

