import openai
import numpy as np

answer = '''
Handling Big Data, enterprices deal amount da fa.
real with 
High Scalability and performance -
Real-time Analytics.- Nosql databases provide buit
time analytics.
Distributed Architectures.
large'''

scheme = '''Handling Big Data Enterprises deal with vast amounts of data generated from
various sources.
• Flexibility with Data Models - NoSQL databases offer flexible data models, allowing
enterprises to store and manipulate different types of data.
• High Scalability and Performance NoSQL databases provide horizontal scalability,
enabling enterprises to handle massive data growth and increased workloads.
Distributed Architectures Enterprises increasingly adopt distributed and cloud-based
architectures.
Real-time Analytics Many NoSQL databases provide built-in capabilities for real-time
analytics and processing.'''

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

