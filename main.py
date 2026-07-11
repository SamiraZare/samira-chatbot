"""
Samira Zare portfolio chatbot — FastAPI backend.

Holds the OpenAI API key server-side (never exposed to the browser) and answers
visitor questions strictly from the knowledge base in knowledge.py.

Run locally:
    export OPENAI_API_KEY="sk-..."
    uvicorn main:app --reload

Deploy: see README (Render, free tier).
"""
from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

from knowledge import BACKGROUND

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
MODEL = "gpt-4o-mini"

# The system prompt is where we constrain the bot to Samira's professional
# background only. It is told to refuse politely on anything off-topic.
SYSTEM_PROMPT = f"""You are a friendly, professional assistant on Samira Zare's \
personal portfolio website. Your only job is to answer questions from recruiters \
and visitors about Samira's professional background, research, projects, skills, \
and education.

Answer ONLY using the information below. If a question cannot be answered from \
this information — including personal questions, opinions, or anything unrelated \
to Samira's professional life — politely say you can only help with questions \
about Samira's professional background, and suggest they reach out to her directly \
at samiraaa.zare@gmail.com.

Keep answers concise (2-4 sentences), warm, and professional. Refer to her as \
"Samira". Never invent facts that are not in the information below.

--- INFORMATION ABOUT SAMIRA ---
{BACKGROUND}
--- END INFORMATION ---"""

app = FastAPI(title="Samira Zare Portfolio Chatbot")

# CORS lets your website's browser code call this backend. For production,
# replace "*" with your real domain, e.g. allow_origins=["https://samirazare.com"].
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


class ChatMessage(BaseModel):
    role: str       # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[ChatMessage] = []


class ChatResponse(BaseModel):
    reply: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Build the message list: system prompt + prior turns + the new message.
    # Sending history is what makes it a conversation rather than isolated Q&A.
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for turn in request.history[-6:]:  # keep last 6 turns to control token cost
        messages.append({"role": turn.role, "content": turn.content})
    messages.append({"role": "user", "content": request.message})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.5,
            max_tokens=300,
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI error:", e)
        reply = ("Sorry, I'm having trouble responding right now. Please email "
                 "Samira directly at samiraaa.zare@gmail.com.")

    return ChatResponse(reply=reply)
