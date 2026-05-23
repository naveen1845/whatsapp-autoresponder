# WhatsApp AI Reply Bot

An AI-powered desktop bot that watches your WhatsApp Web chat, understands the conversation, and generates natural, human-like replies in your voice — using Groq (LLaMA) or Google Gemini under the hood.

---

## What It Does

- Reads your open WhatsApp Web chat by screen-selecting and copying text
- Sends the conversation to an LLM to generate a contextual reply
- Types the reply with realistic, human-like keystroke timing
- Runs in a loop, checking for new messages every 15 seconds
- Replies only when the last message is **not** from you

---

## Project Structure

```
whatsapp-ai-bot/
├── src/
│   ├── main.py              # Entry point — runs the main loop
│   ├── groq_client.py       # LLaMA reply generation via Groq API
│   ├── gemini_client.py     # (Alt) Gemini reply generation via Google AI
│   └── mouse_locator.py     # Helper to find screen coordinates
├── .env                     
├── requirements.txt         # Python dependencies
├── .gitignore
└── .venv/                   # Virtual environment
```

---

## Setup

### 1. Clone & create a virtual environment

```bash
git clone https://github.com/naveen1845/whatsapp-autoresponder
cd whatsapp-autoresponder
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your `.env`

```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

Get your keys from:

- Groq → [https://console.groq.com](https://console.groq.com)
- Google AI → [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### 4. Calibrate screen coordinates

Open `src/mouse_locator.py` and run it to find the right pixel positions for your screen:

```bash
python src/mouse_locator.py
```

Then update these constants in `main.py`:

```python
START_X, START_Y = 409, 129    # Top of the chat messages area
END_X, END_Y    = 409, 853    # Bottom of the chat messages area
PASTE_X, PASTE_Y = 743, 876   # WhatsApp message input box
```

---

## 🚀 Running the Bot

1. Open **WhatsApp Web** in your browser
2. Open the chat you want to auto-reply in
3. Run the bot:

```bash
python src/main.py
```

The bot will start after a 2-second delay and begin monitoring the chat.

---

## How the AI Reply Works

The prompt instructs the model to reply as **Naveen** — a warm, casual friend who writes in a natural mix of English/Hindi/Urdu/Konkani style, keeps replies to a single line, and avoids sounding cringe or robotic.

You can fully customize the persona, tone, and language style by editing the prompt inside `groq_client.py` or `gemini_client.py`.

---

## Configuration


| Variable         | Default                   | Description                         |
| ---------------- | ------------------------- | ----------------------------------- |
| `MY_NAME`        | `"Naveen"`                | Your name as it appears in the chat |
| `CHECK_INTERVAL` | `15`                      | Seconds between each check          |
| `model`          | `llama-3.3-70b-versatile` | Groq model to use                   |


---

## Dependencies

```
groq
pyautogui
pyperclip
python-dotenv
google-generativeai   # for Gemini (optional)
```

---

## Disclaimer

This bot uses screen automation and simulates keyboard input. Use it responsibly and only on your own accounts. Automated messaging may violate WhatsApp's Terms of Service.

## Limitations

- Depends on fixed screen coordinates, so UI changes can break it
- No direct WhatsApp API or DOM access (uses screen scraping)
- Requires WhatsApp Desktop to be open and properly positioned
- May generate incorrect or unnecessary replies sometimes
- Not scalable for multiple chats or users
- Continuous polling is not very efficient

## Future Scope

- Replace screen automation with WhatsApp Web / Business API
- Add memory system for better conversation context
- Improve reply filtering (avoid unnecessary responses)
- Add sentiment/tone detection for smarter replies
- Switch to event-driven message detection instead of polling
- Support multiple chats and users
- Add safety rules and rate limiting

---

do whatever you want, just don't blame me if your crush gets a weird reply.