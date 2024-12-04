from fastapi import APIRouter, HTTPException
import requests
from bs4 import BeautifulSoup
from app.models.database.py import database

router = APIRouter()

@router.post("/process_url")
async def process_url(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.get_text()
        chat_id = f"url_{hash(url)}"
        database[chat_id] = content.strip()
        return {"chat_id": chat_id, "message": "URL content processed and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
