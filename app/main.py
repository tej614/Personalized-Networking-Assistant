from fastapi import FastAPI
from app.routers.conversation import router

app = FastAPI(
    title="Personalized Networking Assistant",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Personalized Networking Assistant"
    }

app.include_router(router)