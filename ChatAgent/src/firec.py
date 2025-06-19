import os
from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_openai import ChatOpenAI

load_dotenv()


class FirecrawlService:
    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self.server_params = StdioServerParameters(
            command="npx",
            args=["firecrawl-mcp"],
            env={"FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY")}
        )

    async def run_agent(self):
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await load_mcp_tools(session)
                agent = create_react_agent(model=self.llm, tools=tools)
                print("✅ Available Firecrawl Tools:", [tool.name for tool in tools])
                return agent
