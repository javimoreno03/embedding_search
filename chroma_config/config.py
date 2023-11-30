import chromadb

chroma_client = chromadb.PersistentClient(path='chroma_config/persist-data/foods')

foodCollection = chroma_client.get_or_create_collection(name="foods", metadata={"hnsw:space": "cosine"})
