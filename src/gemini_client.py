import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="You are Naveen, I nice friend to all."
)

print(response.text)


'''
this file has nothing to do with the main, just for demo purpose
'''