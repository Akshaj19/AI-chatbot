# 🚀 Deploy MyChat to Render.com (FREE, no credit card)

Render deploys from a **GitHub repo**. So the flow is:
1. Put your code on GitHub
2. Connect it to Render
3. Add your API key as a secret
4. Done — you get a public URL like `https://mychat.onrender.com`

---

## STEP 1 — Put your code on GitHub

### 1a. Make a GitHub account (if you don't have one)
Go to https://github.com and sign up (free).

### 1b. Create a new repository
- Click the **+** (top right) → **New repository**
- Name it `mychat`
- Keep it **Private** (recommended — your code stays yours)
- Click **Create repository**

### 1c. Upload your files
Easiest way (no Git commands needed):
- On the new empty repo page, click **"uploading an existing file"**
- Drag in the **contents** of your `mychat` folder (the `backend/`, `frontend/` folders,
  `render.yaml`, `.gitignore`, `README.md`)
- ‼️ **DO NOT upload your `.env` file** (it has your key). The `.gitignore` handles this
  if you use Git, but if uploading manually, just skip `.env` and the `venv` folder.
- Click **Commit changes**

---

## STEP 2 — Deploy on Render

### 2a. Sign up
Go to https://render.com and **sign up with your GitHub account** (free, no card).

### 2b. Create the web service
- Click **New +** → **Web Service**
- Connect your `mychat` GitHub repo
- Render will detect `render.yaml` automatically. If it asks manually, use:
  - **Root Directory:** `backend`
  - **Runtime:** Python 3
  - **Build Command:** `pip install -r requirements.txt`
  - **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
  - **Plan:** Free

### 2c. Add your secret API key ‼️ IMPORTANT
- In the service settings, go to **Environment**
- Add these variables:
  | Key | Value |
  |---|---|
  | `API_KEY` | `gsk_your_real_groq_key` |
  | `BASE_URL` | `https://api.groq.com/openai/v1` |
  | `MODEL` | `llama-3.3-70b-versatile` |
- Click **Save Changes**

### 2d. Deploy
- Click **Create Web Service** (or **Manual Deploy** → **Deploy latest commit**)
- Wait ~2–3 minutes for the build
- When it's live, you'll get a URL like **https://mychat-xxxx.onrender.com** 🎉

---

## ⚠️ Notes about the FREE plan
- Your app **sleeps after 15 min of no traffic**. The first request after sleeping
  takes ~30–50 seconds to wake up (then it's fast). This is normal for the free tier.
- Never put your real key in the code or in `render.yaml`. Only in the
  **Environment** settings (Step 2c). That keeps it secret.

## Updating your app later
Just push/upload new files to GitHub — Render auto-redeploys. 🔄
