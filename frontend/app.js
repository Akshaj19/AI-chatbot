// ---- MyChat frontend logic --------------------------------------------------
// Keeps the full conversation in memory and streams replies from the backend.

const messagesEl = document.getElementById("messages");
const form = document.getElementById("chat-form");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");
const modelBadge = document.getElementById("model-badge");
const newChatBtn = document.getElementById("new-chat");

let history = []; // [{role, content}]

// Show which model is active
fetch("/api/config")
  .then((r) => r.json())
  .then((c) => { modelBadge.textContent = c.model || "unknown"; })
  .catch(() => { modelBadge.textContent = "offline"; });

// Auto-grow the textarea
input.addEventListener("input", () => {
  input.style.height = "auto";
  input.style.height = Math.min(input.scrollHeight, 200) + "px";
});

// Enter to send, Shift+Enter for newline
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    form.requestSubmit();
  }
});

newChatBtn.addEventListener("click", () => {
  history = [];
  messagesEl.innerHTML =
    '<div class="empty"><h2>Ask me anything</h2><p>New chat started.</p></div>';
});

function addMessage(role, text) {
  const empty = messagesEl.querySelector(".empty");
  if (empty) empty.remove();

  const wrap = document.createElement("div");
  wrap.className = `msg ${role}`;
  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = role === "user" ? "🧑" : "🤖";
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  wrap.append(avatar, bubble);
  messagesEl.appendChild(wrap);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return bubble;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;

  addMessage("user", text);
  history.push({ role: "user", content: text });
  input.value = "";
  input.style.height = "auto";
  sendBtn.disabled = true;

  const botBubble = addMessage("bot", "");
  botBubble.classList.add("cursor");
  let reply = "";

  try {
    const resp = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: history }),
    });

    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      reply += decoder.decode(value, { stream: true });
      botBubble.textContent = reply;
      messagesEl.scrollTop = messagesEl.scrollHeight;
    }
  } catch (err) {
    reply = "[Error] " + err.message;
    botBubble.textContent = reply;
  }

  botBubble.classList.remove("cursor");
  history.push({ role: "assistant", content: reply });
  sendBtn.disabled = false;
  input.focus();
});
