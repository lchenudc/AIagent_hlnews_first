

#In your "server.py" file make the following changes: 

#Get and Add your news API key from https://newsapi.org

NEWSAPI_KEY = "your key"  # Get API key from env var

# Add your new function 
 
# ------------------------------------------------------------------
# Tool: get_realtime_headlines (NewsAPI + economic filter)
# ------------------------------------------------------------------
@mcp.tool()
def get_realtime_headlines(category: str = "general") -> list[str]:
    """Fetch real-time headlines and filter those impacting US economy."""
    if not NEWSAPI_KEY:
        return ["❌ NewsAPI key not configured. Set NEWSAPI_KEY env variable."]

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": category.lower(),
        "country": "us",
        "pageSize": 10,
        "apiKey": NEWSAPI_KEY,
    }

    print(f"🌐 [LiveNewsTool] Fetching headlines for: {category}")
    try:
        res = requests.get(url, params=params)
        data = res.json()
        if data.get("status") != "ok":
            return [f"❌ API error: {data.get('message')}"]

        keywords = ["science","movie","TV","economy", "inflation", "jobs", "interest rates", "Fed", "GDP", "stock", "market", "recession","general","spots"]
        filtered = [article["title"] for article in data.get("articles", [])
                    if any(k in article["title"].lower() for k in keywords)]

        return filtered if filtered else ["ℹ️ No economically relevant headlines found."]

    except Exception as e:
        return [f"❌ Error fetching real-time news: {str(e)}"]
        
----------------------------------------------------------------------------------        
        
#In your "client.py" file make the following changes: 

        
# Use the following new Main() is to call the new tool() you did in "server.py"


async def main():
    server_params = StdioServerParameters(
        command="python3",
        args=["server_hln_real.py"],   # make sure filename matches
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("✅ MCP session  ready: server_headlinenews.py was launched")

            # ── Discover all tools exposed by server_headlinenews.py ──
            tools = await load_mcp_tools(session)        # returns a list of LangChain Tool objects
            tool_by_name = {t.name: t for t in tools}    # index by name

            #news_tool = tool_by_name["get_headlines"]    # grab the one we want  ????????????? we need to do a selection if it is demo or real
            
            # Find the correct tool
            realtime_tool = [t for t in tools if t.name == "get_realtime_headlines"][0]

 
            # Call it with a category (optional)
            result: list[str] = await realtime_tool.arun({"category": "entertainment"})
            
            '''business
		entertainment
		general
		health
		science
		sports
		technology'''

            print("📢 Headlines:")
            # Safe normalization: if result is a string, wrap it into a list
            if isinstance(result, str):
                result = [result]
 
            for headline in result:
                print("•", headline)
                
            await asyncio.sleep(1.1)     
            #inflation
            result: list[str] = await realtime_tool.arun({"category": "business"})

            print("📢 Headlines:")
            for headline in result:
                print("•", headline)  
                
            await asyncio.sleep(1.1)
                
            #GDP
            result: list[str] = await realtime_tool.arun({"category": "science"})

            print("📢 Headlines:")
            for headline in result:
                print("•", headline)  

---------------------
There should not be any difficulty to make these changes. Try the simplest way without menu-selection first. 

