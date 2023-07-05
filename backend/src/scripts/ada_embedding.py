import openai
import numpy as np

answer = '''
• Load balancing.
•Improved
query Performance.
Horizontal scalability
distribution
•Data
6'''

scheme = '''Sharding in NoSQL databases plays a crucial role in achieving scalability and
performance by distributing data across multiple nodes or servers.
Horizontal scalability
• Data distribution
Load balancing
• Improved query performance'''

model = 'text-embedding-ada-002'
OPENAI_KEY = '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'

vectors = []

openai.api_key = OPENAI_KEY

answer = answer.replace("\n", " ")
scheme = scheme.replace("\n", " ")
embeddings = openai.Embedding.create(input=[answer, scheme], model=model)
answer_vector = embeddings["data"][0]["embedding"]
vectors.append(answer_vector)
scheme_vector = embeddings["data"][1]["embedding"]
vectors.append(scheme_vector)

cosine_similarity = np.dot(vectors[0], vectors[1]) / (np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1]))

print("similarity using np:", cosine_similarity)


# from openai.embeddings_utils import get_embedding, cosine_similarity

# def search_reviews(df, product_description, n=3, pprint=True):
#    embedding = get_embedding(product_description, model='text-embedding-ada-002')
#    df['similarities'] = df.ada_embedding.apply(lambda x: cosine_similarity(x, embedding))
#    res = df.sort_values('similarities', ascending=False).head(n)
#    return res

# res = search_reviews(df, 'delicious beans', n=3)

