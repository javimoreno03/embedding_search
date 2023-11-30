from services.embeddingService import searchFoods, embedString

foods:list[str] = []
foodsEmbedding:list[list[float]] = []

def addNewFood(food: str):
  foodEmbedding = embedString(food)
  foods.append(food)
  foodsEmbedding.append(foodEmbedding)

def getFoods(nameToFind:str = ''):
  if len(foods) <= 0:
    return []

  response = searchFoods(nameToFind, foodsEmbedding)
  
  foodsFound = []
  
  for index, score in response:
    foodsFound.append({
      'name': foods[index],
      'score': score
    })

  return foodsFound
