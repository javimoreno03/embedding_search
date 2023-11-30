from fastapi import FastAPI
from pydantic import BaseModel
from db import addNewFood, getFoods

class AddFood(BaseModel):
  food: str

app = FastAPI()

@app.get("/foods")
def get_foods(name: str = ''):
  return getFoods(name)

@app.post("/foods")
def add_food(body: AddFood):
  addNewFood(body.food)
  return { "status": "ok" }