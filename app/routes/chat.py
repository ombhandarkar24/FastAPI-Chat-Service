from fastapi import APIRouter, HTTPException
from sentence_transformers import SentenceTransformer, util
from app.models.database import database

router = APIRouter()
model = SentenceTransformer("all-MiniLM-L6-v2")

@router.post("/chat")
async def chat(chat_id: str, question: str):
    if chat_id not in database:
        raise HTTPException(status_code=404, detail="Chat ID not found.")
    
    content = database[chat_id]
    content_embedding = model.encode(content, convert_to_tensor=True)
    question_embedding = model.encode(question, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(question_embedding, content_embedding).item()
    return {"response": f"Relevance Score: {similarity}"}
