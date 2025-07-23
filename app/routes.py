from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.get("/doc")
def doc():
    return {
        "message" : "restAPI documentation",
    }
