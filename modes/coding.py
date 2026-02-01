import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def coding_agent(user_input):
    if not os.getenv("OPENAI_API_KEY"):
        return "❌ OpenAI key not loaded"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a coding instructor."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
