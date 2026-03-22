import asyncio
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.mcp import MCPServerStreamableHTTP


load_dotenv()

server = MCPServerStreamableHTTP("http://localhost:8000/mcp")
model = GoogleModel("gemini-2.5-flash")

agent = Agent(
    model=model, 
    toolsets=[server],
    instructions="""
    You are a helpful assistant.
    Do not use any bold or italic formatting in your answers.
    """,
    output_type=float,
    )


async def main() -> None:
    result = await agent.run("What is 4 times 7.5?")
    print(result.output)
    print(type(result.output))

if __name__ == "__main__":
    asyncio.run(main())
