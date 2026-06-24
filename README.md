# 💬 Samira Zare — Portfolio Chatbot

An AI assistant embedded on [samirazare.com](https://samirazare.com) that answers recruiter and visitor questions about Samira's background, research, and projects — grounded strictly in my real portfolio content.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![OpenAI](https://img.shields.io/badge/API-OpenAI-412991?logo=openai)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## What it does

A floating chat widget on the portfolio site. Visitors can ask things like:

- *"What was Samira's PhD about?"*
- *"What are her publications?"*
- *"Tell me about her machine learning projects."*

The bot answers from a curated knowledge base and politely declines anything outside Samira's professional background.

---

## Architecture

```
Visitor's browser (widget.html on samirazare.com)
        │  POST /chat  { message, history }
        ▼
FastAPI backend (main.py)  ← holds the OpenAI API key (never exposed to the browser)
        │  system prompt + knowledge base + conversation history
        ▼
OpenAI gpt-4o-mini
        │
        ▼
Reply grounded only in Samira's real background
```

**Why a backend?** The OpenAI API key must stay secret. If it lived in the browser widget, anyone could view-source and steal it. The FastAPI service keeps the key server-side and is the only thing that talks to OpenAI.

---

## Project structure

```
samira-chatbot/
├── main.py            # FastAPI backend — the /chat endpoint
├── knowledge.py       # Samira's background (edit this to update what the bot knows)
├── widget.html        # Embeddable chat widget for WordPress
├── requirements.txt
├── render.yaml        # One-click deploy config for Render
└── .env.example
```

---

## Run locally

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
uvicorn main:app --reload
```

The backend runs at `http://localhost:8000`. Test it:

```bash
curl -X POST http://localhost:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "What was Samira'\''s PhD about?", "history": []}'
```

To see the widget, open `widget.html` in a browser (with `BACKEND_URL` set to `http://localhost:8000`).

---

## Deploy (free, ~10 minutes)

1. Push this repo to GitHub.
2. Create a free account at [render.com](https://render.com) and click **New → Web Service**, connecting this repo. Render reads `render.yaml` automatically.
3. In the Render dashboard, add your `OPENAI_API_KEY` as an environment variable (Settings → Environment). **Never put the key in the code.**
4. Render gives you a public URL like `https://samira-chatbot.onrender.com`.
5. In `widget.html`, set `BACKEND_URL` to that URL.
6. In WordPress, add a **Custom HTML** block (or a header/footer plugin) and paste the contents of `widget.html`. The chat button now appears on your site.

---

## Updating what the bot knows

Edit `knowledge.py` — it's plain English. Add a project, a publication, a skill; redeploy; done. The bot only ever answers from this file, so it can't make things up about Samira.

---

## Cost

Uses `gpt-4o-mini` with short context. Typical visitor conversations cost a fraction of a cent. A busy week of recruiter traffic stays well under a dollar.

---

## License

MIT
