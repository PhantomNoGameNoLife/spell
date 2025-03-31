from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from autocorrect import Speller
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

spell = Speller(lang='en')

class TextInput(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/correct")
async def correct_text(input_data: TextInput):
    corrected_text = spell(input_data.text)
    return {"corrected_text": corrected_text}

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")