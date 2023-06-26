import openai
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
import faiss
from config.config import settings

marking = "A router is a networking device that connects multiple computer networks together and directs data traffic between them by determining the optimal path for data packets"
answer = " A router is a device that links different networks, such as a home network and the internet, and manages the flow of data between them, ensuring efficient communication."

embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

answer_vector = embeddings.embed_query(answer)
answer_vector = np.array([answer_vector]).astype("float32")
# create vector store
index = faiss.IndexFlatL2(1536)
# add answer vector to the vector store
index.add(answer_vector)

marking_vector = embeddings.embed_query(marking)
marking_vector = np.array([marking_vector]).astype("float32")

k = 1
distances, indices = index.search(marking_vector, k)
print(indices)




