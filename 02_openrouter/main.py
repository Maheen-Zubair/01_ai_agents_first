import os
import asyncio
import nest_asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

load_dotenv()
nest_asyncio.apply()

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "google/gemini-2.0-flash-lite-preview-02-05:free"

# Ab explicitly api_key pass karna zaruri nahi, kyunki library env se read karti hai
client = AsyncOpenAI(
    base_url=BASE_URL
)

set_tracing_disabled(disabled=True)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(agent, "Tell me about recursion")
    print(result.content)

if __name__ == "__main__":
    asyncio.run(main())
