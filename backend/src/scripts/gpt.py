import openai
from langchain.embeddings import FakeEmbeddings
from config.config import settings

marking_scheme = "A router is a networking device that connects multiple computer networks together and directs data traffic between them by determining the optimal path for data packets"
answer_sheet = " A router is a device that links different networks, such as a home network and the internet, and manages the flow of data between them, ensuring efficient communication."

fake_embeddings = FakeEmbeddings(size=1536)
fake_embeddings_list = []

