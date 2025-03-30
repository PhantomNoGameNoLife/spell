from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from textblob import TextBlob
import nltk
import uvicorn

nltk.download('punkt')

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class TextInput(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/correct")
async def correct_text(input_data: TextInput):
    blob = TextBlob(input_data.text)
    corrected_text = str(blob.correct())
    return {"corrected_text": corrected_text}

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")