from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.foodService import getFoods, addNewFood
from middlewares.basicAuth import basicAuthMiddleware

class AddFood(BaseModel):
  food: str

searchRouter = APIRouter(dependencies=[Depends(basicAuthMiddleware)])

@searchRouter.get("/search", )
def get_foods(name: str = ''):
  return getFoods(name)

@searchRouter.post("/train")
def add_food(body: AddFood):
  addNewFood(body.food)
  return { "status": "ok" }
