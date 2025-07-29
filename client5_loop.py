import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
from langchain_mcp_adapters.tools import load_mcp_tools   # ← MCP → LangChain bridge

CATEGORY = "general"
CATEGORIES  = ["general", "sports", "tech"]

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


            while True:
                # ---- simple text menu ----
                print("Choose a category:")
                for idx, cat in enumerate(CATEGORIES, 1):
                    print(f"  {idx}. {cat.capitalize()}")
                print("  0. Exit")

                choice = input("Enter choice number ➜ ").strip()
                if choice == "0":
                    print("👋 Bye!")
                    break

                try:
                    category = CATEGORIES[int(choice) - 1]
                except (ValueError, IndexError):
                    print("⚠️  Invalid selection.\n")
                    continue

                # ---- invoke MCP tool ----
                #result = await session.invoke_tool(
                #    "get_headlines",
                #    {"category": category}
                #)


                # LangChain tools are regular callables
                #result: list[str] = await news_tool.arun(category=CATEGORY)
                # correct async call – wrap kwargs in a single dict
                result: list[str] = await news_tool.arun({"category": category})
                #result: list[str] = await news_tool.arun({"category": CATEGORY})
                # (or .run(...) for sync usage)

                print("📰 Headlines:")
                for i, h in enumerate(result, 1):
                    print(f"{i}. {h}")

if __name__ == "__main__":
    asyncio.run(main())

