import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
from langchain_mcp_adapters.tools import load_mcp_tools   # ← MCP → LangChain bridge

CATEGORY = "tech"

async def main():
    server_params = StdioServerParameters(
        command="python3",
        args=["server_headlinenews.py"],   # make sure filename matches
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("✅ MCP session  ready: server_headlinenews.py was launched")

            # ── Discover all tools exposed by server_headlinenews.py ──
            tools = await load_mcp_tools(session)        # returns a list of LangChain Tool objects
            tool_by_name = {t.name: t for t in tools}    # index by name

            news_tool = tool_by_name["get_headlines"]    # grab the one we want

            # LangChain tools are regular callables
            #result: list[str] = await news_tool.arun(category=CATEGORY)
            # correct async call – wrap kwargs in a single dict
            result: list[str] = await news_tool.arun({"category": CATEGORY})
            # (or .run(...) for sync usage)

            print("📰 Headlines:")
            for i, h in enumerate(result, 1):
                print(f"{i}. {h}")

if __name__ == "__main__":
    asyncio.run(main())

