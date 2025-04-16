from openai import AsyncOpenAI
from config import API_KEY

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)


async def ai_generate(text: str):
    print("asking for answer\n")
    completion = await client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )
    print("Answer:\n")
    print(completion)
    return completion.choices[0].message.content