import re
import time
import os
import pyautogui
import pyperclip
from dotenv import load_dotenv
from groq import Groq
import random

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MY_NAME = "Naveen"

START_X, START_Y = 409, 129
END_X, END_Y = 409, 853
PASTE_X, PASTE_Y = 743, 876

CHECK_INTERVAL = 15


def parse_whatsapp_chat(chat_text):

    pattern = re.compile(
        r'^\[(.*?)\]\s(.*?):\s(.*)$'
    )

    messages = []
    current_message = None

    lines = chat_text.splitlines()

    for line in lines:

        match = pattern.match(line)

        # New message
        if match:

            timestamp, sender, message = match.groups()

            if current_message:
                messages.append(current_message)

            current_message = {
                "timestamp": timestamp.strip(),
                "sender": sender.strip(),
                "message": message.strip()
            }

        else:
            # Multiline continuation
            if current_message:
                current_message["message"] += "\n" + line.strip()

    if current_message:
        messages.append(current_message)

    return messages


def copy_chat():

    pyautogui.moveTo(START_X, START_Y)

    pyautogui.dragTo(
        END_X,
        END_Y,
        duration=0.5,
        button='left'
    )

    time.sleep(0.2)

    pyautogui.hotkey('command', 'c')

    time.sleep(0.3)

    return pyperclip.paste()


def generate_reply(chat_text):

    prompt = f"""
You are Naveen, a warm and poetic friend.

You reply in:
- short Enlgish/Hindi/Urdu/Goan-Konkani style but text in English
- not going gym since months now
- single line only
- dont use the sender's name, use it only once in a while
- natural sounding
- emotionally smooth
- not cringe
- no timestamps
- no quotes

Chat:
{chat_text}

Generate ONLY the next reply by Naveen.
"""

    # response = client.models.generate_content(
    #     model="gemini-1.5-flash",
    #     contents=prompt
    # )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    )

    return response.choices[0].message.content

def human_type(text):
    for char in text:
        pyautogui.write(char)

        # variable delay = key to realism
        time.sleep(random.uniform(0.03, 0.06))

print("Starting in 2 seconds...")
time.sleep(2)

while True:

    try:

        copied_chat = copy_chat()

        messages = parse_whatsapp_chat(copied_chat)

        if not messages:
            print("No messages found.")
            time.sleep(CHECK_INTERVAL)
            continue

        last_message = messages[-1]

        sender = last_message["sender"]

        print("\n----------------")
        print("Last Sender:", sender)
        print("Last Message:", last_message["message"])

        if sender != MY_NAME:

            print("\nGenerating Reply...\n")

            reply = generate_reply(copied_chat)

            print(reply)

            pyperclip.copy(reply)
            time.sleep(0.2)

            pyautogui.click(PASTE_X, PASTE_Y)
            time.sleep(0.3)

            human_type(reply)

            pyautogui.hotkey('enter')

        else:
            print("\nNo reply needed.")

    except Exception as e:
        print("Error:", e)

    time.sleep(CHECK_INTERVAL)