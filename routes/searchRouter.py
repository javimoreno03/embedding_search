from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.foodService import getFoods, addNewFood
from middlewares.basicAuth import basicAuthMiddleware

class AddFood(BaseModel):
  id: int
  food: str
  active: bool

searchRouter = APIRouter(dependencies=[Depends(basicAuthMiddleware)])

@searchRouter.get("/search", )
def get_foods(name: str = ''):
  return getFoods(name)

@searchRouter.post("/train")
def add_food(body: AddFood):
  addNewFood(body.id, body.food, body.active)
  return { "status": "ok" }
