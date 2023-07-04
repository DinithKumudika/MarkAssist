from sentence_transformers import SentenceTransformer, util

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

model = SentenceTransformer('all-mpnet-base-v2')

answerEmbedding = model.encode(answer, convert_to_tensor=True)
schemeEmbedding = model.encode(scheme, convert_to_tensor=True)

cosine_similarity = util.cos_sim(answerEmbedding, schemeEmbedding)

print("similarity:", cosine_similarity)