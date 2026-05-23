from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Reply poetically in one line. hii whats the plan today"
        }
    ]
)

print(response.choices[0].message.content)


'''
this file has nothing to do with the main, just for demo purpose
'''