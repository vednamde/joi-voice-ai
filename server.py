from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai, os

openai.api_key = "Your_api_key"  # your key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow your browser to talk to it
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    user_text = data.get("messages", [])[0].get("content", "")
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Joi, caring and charming."},
            {"role": "user", "content": user_text}
        ]
    )
    return {"reply": completion.choices[0].message.content}
