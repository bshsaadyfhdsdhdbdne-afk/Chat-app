from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = "YOUR_OPENAI_API_KEY"

class RequestBody(BaseModel):
    prompt: str

@app.post("/ask")
def ask_ai(body: RequestBody):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=body.prompt,
        max_tokens=150
    )
    return {"answer": response.choices[0].text.strip()}