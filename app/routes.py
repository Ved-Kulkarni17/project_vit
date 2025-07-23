from fastapi import APIRouter, Request
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "model")))

from model import ThreatModel  

router = APIRouter()
model = ThreatModel()

@router.post("/predict")
async def predict(request: Request):
    data = await request.json()
    return model.predict(data)
router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.get("/doc")
def doc():
    return {
        "message" : "restAPI documentation",
    }
