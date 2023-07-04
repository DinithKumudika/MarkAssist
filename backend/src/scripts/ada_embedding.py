import openai
import numpy as np

answer = '''
●
Confidentiality: Provides protection from unauthorized access
Sensitive data.
for
• Integrity: Ensures the accuracy, consistency and
reliability of data.
Availability
-
when needed, database is accessible and
usable.'''

scheme = '''Confidentiality Confidentiality ensures that sensitive data remains protected from
unauthorized access or disclosure.
• Integrity Integrity ensures the accuracy, consistency, and reliability of data stored
in the database.
Availability - Availability ensures that the database and its data are accessible and
usable when needed.'''

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

