from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routes.mainRouter import mainRouter
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(mainRouter, prefix="/api")
