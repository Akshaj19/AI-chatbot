<div align="center">

# 💬 MyChat

### Your own Claude / ChatGPT-like AI chat platform — self-hosted, free & private.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

**Streaming replies · conversation memory · attach web links · works with any AI model**

[Live Demo](#-live-demo) • [Features](#-features) • [Run Locally](#️-run-it-locally) • [Deploy](#️-deploy-online-free)

</div>

---

## 🌐 Live Demo

👉 **(https://ai-chatbot-ni38.onrender.com/)**

> Replace the link above with your actual Render URL.
> ⏳ Note: on Render's free tier the app sleeps after 15 min — the first load may take ~30–50 s to wake up, then it's fast.

---

## ✨ Features

- 🔥 **Streaming responses** — words appear as they generate, just like ChatGPT/Claude
- 🧠 **Conversation memory** — remembers the whole chat
- 🔗 **Attach web links** — paste a URL and the bot reads the page to answer you
- 🎨 **Clean dark UI** — message bubbles, auto-growing input, one-click new chat
- 🔌 **Works with ANY model** — Gemini, Groq, OpenAI, OpenRouter, or local Ollama
  (switch by editing one line — no code changes)
- 🚀 **Deploy anywhere** — run locally or host free on Render.com
- 🔒 **Private by design** — your API key lives on the server, never in the browser

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| **Frontend** | HTML · CSS · Vanilla JavaScript (no framework) |
| **Backend** | Python · FastAPI · httpx · BeautifulSoup |
| **AI** | Any OpenAI-compatible API (Groq / Gemini / OpenAI / Ollama) |
| **Hosting** | Render.com (free tier) |

---

## 📁 Project Structure

```
mychat/
├── backend/                # FastAPI server (talks to the AI model)
│   ├── app.py              # main server code
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # copy to .env and add your API key
├── frontend/               # the chat website
│   ├── index.html          # page structure
│   ├── styles.css          # dark theme styling
│   └── app.js              # chat logic + link attaching
├── render.yaml             # one-click Render.com deploy config
├── .gitignore              # keeps your .env / key out of Git
└── README.md               # you are here
```

---

## 🖥️ Run It Locally

### 1. Get a FREE API key
| Provider | Get key | Notes |
|---|---|---|
| **Groq** ⭐ | https://console.groq.com/keys | Fast & free — easiest to start |
| **Gemini** | https://aistudio.google.com/apikey | Very smart & free |
| **Ollama** | https://ollama.com | 100% offline, no key needed |

### 2. Install
```bash
git clone https://github.com/YOURNAME/mychat.git
cd mychat/backend

python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)

pip install -r requirements.txt
```

### 3. Add your key
```bash
copy .env.example .env         # Windows  (Mac/Linux: cp .env.example .env)
```
Open `.env` and paste your key (no quotes, no spaces around `=`):
```env
BASE_URL=https://api.groq.com/openai/v1
API_KEY=gsk_your_real_key_here
MODEL=llama-3.3-70b-versatile
```

### 4. Run
```bash
uvicorn app:app --reload --port 8000
```
Open **http://localhost:8000** 🎉

---

## 🔗 Using the Link Feature

1. Click the **🔗 button** next to the message box
2. Paste any web link (article, docs, blog…)
3. Click **Attach** — a chip shows the linked page
4. Type your question (e.g. *"summarize this"*) and **Send**

The bot downloads the page, reads it, and answers using its content.

---

## 🔄 Switching Models

Just edit `backend/.env` — no code changes:

```env
# Groq (fast + free)
BASE_URL=https://api.groq.com/openai/v1
MODEL=llama-3.3-70b-versatile

# Google Gemini
BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai
MODEL=gemini-2.5-flash

# Local Ollama (offline, no key)
BASE_URL=http://localhost:11434/v1
MODEL=qwen2.5-coder:7b
```

---

## ☁️ Deploy Online (Free)

Deploy to **Render.com** in minutes:

1. Push this repo to GitHub
2. On Render: **New + → Web Service → connect your repo**
3. Settings:
   - **Root Directory:** `backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free
4. Add environment variables `API_KEY`, `BASE_URL`, `MODEL` in the **Environment** tab
5. Deploy → get your public URL 🎉

> 🔒 Never commit your API key. Set it only as an environment variable on the host.

---

## 🧱 Roadmap

- [ ] 💾 Save chat history (SQLite) + sidebar of past conversations
- [ ] 👤 User login / accounts
- [ ] 📄 File uploads (PDFs, images)
- [ ] 📝 Markdown & syntax-highlighted code rendering
- [ ] 🔀 In-UI model picker

---

## ⚠️ Security

- **Never** put your API key in the frontend or commit it to a repo.
- Store keys as **environment variables / secrets** on your host.
- If a key leaks, **delete it** in the provider dashboard and generate a new one.

---

## 📄 License

MIT — free to use, modify, and share.

---

<div align="center">

Built with ❤️ using **FastAPI** + **vanilla JS**.

⭐ Star this repo if you found it useful!

</div>
