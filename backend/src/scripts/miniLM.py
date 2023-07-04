from sentence_transformers import SentenceTransformer, util

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

model = SentenceTransformer('all-MiniLM-L6-v2')

answerEmbedding = model.encode(answer, convert_to_tensor=True)
schemeEmbedding = model.encode(scheme, convert_to_tensor=True)

cosine_similarity = util.cos_sim(answerEmbedding, schemeEmbedding)

print("similarity:", cosine_similarity)