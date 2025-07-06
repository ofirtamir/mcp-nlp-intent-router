
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from match_intent import match_question_to_intent

app = FastAPI()

class UserInput(BaseModel):
    question: str

@app.post("/ask")
def ask(user_input: UserInput):
    matched = match_question_to_intent(user_input.question)
    if matched == "לא ידוע":
        return {"answer": "לא הצלחתי להבין את השאלה. נסה לנסח אחרת."}

    response = requests.post(
        "https://mcp-excel-5zg0.onrender.com/call",
        json={"question": matched}
    )
    return response.json()
