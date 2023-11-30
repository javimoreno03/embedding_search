from chroma_config.config import foodCollection

def addNewFood(id: int, food: str, active: bool):
  foodCollection.add(ids=[str(id)], documents=[food], metadatas=[{ 'active': active }])

def getFoods(nameToFind:str = ''):
  res = foodCollection.query(query_texts=[nameToFind], where={ 'active': True },  n_results=5)
  
  foodsResponse = []
  for i in range(len(res['ids'][0])):
    foodsResponse.append({
      'id': res['ids'][0][i],
      'food': res['documents'][0][i],
      'active': res['metadatas'][0][i]['active'],
      'distance': res['distances'][0][i]
    })
  
  return foodsResponse
