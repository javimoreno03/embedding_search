from langchain.embeddings import HuggingFaceEmbeddings
from numpy import argsort
from sklearn.metrics.pairwise import cosine_similarity

# config
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}

# initialize huggingface
hf = HuggingFaceEmbeddings(
  model_name=model_name,
  model_kwargs=model_kwargs,
  encode_kwargs=encode_kwargs
)

def embedString(string):
  return hf.embed_query(string)

def searchFoods(textSearch, foodsEmbedding):
  queryEmbedding = embedString(textSearch)
  similarities = cosine_similarity([queryEmbedding], foodsEmbedding)
  indexes = argsort(similarities[0])
  
  sorted_indexes = indexes[::-1]
  sorted_similarities = similarities[0][sorted_indexes]
  
  return list(zip(sorted_indexes, sorted_similarities))[:5]


