from fastapi import APIRouter, UploadFile, File, HTTPException
import pdfplumber
from app.models.database import database

router = APIRouter()

@router.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    try:
        with pdfplumber.open(file.file) as pdf:
            content = "".join(page.extract_text() for page in pdf.pages)
        chat_id = f"pdf_{hash(file.filename)}"
        database[chat_id] = content.strip()
        return {"chat_id": chat_id, "message": "PDF content processed and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
