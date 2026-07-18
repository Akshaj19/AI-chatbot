# 💬 MyChat — your own Claude/ChatGPT-like platform

A minimal but real chat platform: streaming replies, conversation memory,
a clean UI, and support for **any** OpenAI-compatible model
(Gemini, Groq, OpenAI, OpenRouter, or local Ollama) — switch by editing one file.

```
mychat/
├── backend/          # FastAPI server that talks to the AI model
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example  # copy to .env and add your key
└── frontend/         # the chat website (HTML/CSS/JS)
    ├── index.html
    ├── styles.css
    └── app.js
```

---

## 🚀 Setup (5 minutes)

### 1. Get a FREE API key (pick one)
- **Groq** (fast + free, easiest): https://console.groq.com/keys
- **Google Gemini** (very smart + free): https://aistudio.google.com/apikey
- **Ollama** (100% offline, no key): install from https://ollama.com then run `ollama pull qwen2.5-coder:7b`

### 2. Install Python deps
```bash
cd mychat/backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Add your key
```bash
# copy the example env file
# Windows:
copy .env.example .env
# Mac/Linux:
cp .env.example .env
```
Open `.env`, keep the provider block you want, and paste your API_KEY.

### 4. Run it
```bash
uvicorn app:app --reload --port 8000
```
(Run this from inside the `backend/` folder.)

### 5. Open the app
Go to **http://localhost:8000** in your browser. Done! 🎉

---

## 🔧 Switch models anytime
Just edit `backend/.env` — no code changes. Comment out one block, uncomment another.

## 🧱 What to build next (grow it into a full platform)
1. **Save chat history** → add SQLite (store conversations per user).
2. **Multiple conversations** → sidebar with a list of past chats.
3. **User login** → add authentication.
4. **File uploads** → send PDFs/images to the model.
5. **Markdown rendering** → render code blocks & formatting nicely (e.g. `marked.js`).
6. **Model picker** → dropdown in the UI to switch models live.

Each of these is a small, self-contained step. Start simple, add one at a time.
