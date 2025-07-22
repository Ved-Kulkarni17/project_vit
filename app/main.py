from fastapi import FastAPI
from app import routes

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to ThreatSight API"}
