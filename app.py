import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from configparser import ConfigParser
from chatbot import ChatBot

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

config = ConfigParser()
config.read('credentials.ini')
api_key = config['gemini_ai']['API_KEY']

chatbot = ChatBot(api_key=api_key)
chatbot.start_conversation()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Gemini Chatbot API"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    prompt = request.prompt

    if not prompt:
        raise HTTPException(status_code=400, detail="No prompt provided")

    try:
        response = chatbot.send_prompt(prompt)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
