from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.recommendation import router as recommendation_router
from app.database.init_db import *
from app.api.user import router as user_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)
app.include_router(recommendation_router)

@app.get("/")
def root():
    return {
        "message": "Project Recommendation System Backend is Running!"
    }