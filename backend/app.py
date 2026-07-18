"""
MyChat - a minimal Claude/ChatGPT-like chat platform backend.

One code path works with ANY OpenAI-compatible provider:
  - Google Gemini (free tier)   -> https://generativelanguage.googleapis.com/v1beta/openai
  - Groq (free, very fast)      -> https://api.groq.com/openai/v1
  - OpenAI                      -> https://api.openai.com/v1
  - OpenRouter (many models)    -> https://openrouter.ai/api/v1
  - Local Ollama (offline)      -> http://localhost:11434/v1

Configure everything in the .env file. No code changes needed to switch providers.
"""
import json
import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

load_dotenv()

# ---- Provider config (from .env) --------------------------------------------
BASE_URL = os.getenv("BASE_URL", "https://api.groq.com/openai/v1").rstrip("/")
API_KEY = os.getenv("API_KEY", "")
MODEL = os.getenv("MODEL", "llama-3.3-70b-versatile")
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "You are MyChat, a helpful, friendly and precise AI assistant. "
    "Answer clearly and use code blocks when sharing code.",
)

app = FastAPI(title="MyChat")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class ChatRequest(BaseModel):
    # Full conversation history: [{"role": "user"/"assistant", "content": "..."}]
    messages: list[dict]


@app.get("/api/config")
async def get_config():
    """Let the frontend show which model is active."""
    return {"model": MODEL, "base_url": BASE_URL, "has_key": bool(API_KEY)}


@app.post("/api/chat")
async def chat(req: ChatRequest):
    """Stream the model's reply back token-by-token (like Claude/ChatGPT)."""

    # Prepend the system prompt so the bot has a personality/instructions.
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + req.messages

    payload = {"model": MODEL, "messages": messages, "stream": True}
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"

    async def event_stream():
        try:
            async with httpx.AsyncClient(timeout=120) as client:
                async with client.stream(
                    "POST",
                    f"{BASE_URL}/chat/completions",
                    json=payload,
                    headers=headers,
                ) as resp:
                    if resp.status_code != 200:
                        body = await resp.aread()
                        yield f"[Error {resp.status_code}] {body.decode(errors='ignore')}"
                        return
                    # OpenAI-style Server-Sent Events: lines start with "data: "
                    async for line in resp.aiter_lines():
                        if not line or not line.startswith("data: "):
                            continue
                        data = line[len("data: "):].strip()
                        if data == "[DONE]":
                            break
                        try:
                            chunk = json.loads(data)
                            delta = chunk["choices"][0]["delta"].get("content")
                            if delta:
                                yield delta
                        except (json.JSONDecodeError, KeyError, IndexError):
                            continue
        except Exception as e:  # noqa: BLE001
            yield f"[Connection error] {e}"

    return StreamingResponse(event_stream(), media_type="text/plain")


# Serve the frontend (index.html etc.) at the root URL.
# Absolute path so it works no matter where the server is started from (e.g. Render).
FRONTEND_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend"
)
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="static")
