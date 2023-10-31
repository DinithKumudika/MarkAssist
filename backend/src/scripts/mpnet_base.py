from sentence_transformers import SentenceTransformer, util

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

model = SentenceTransformer('all-mpnet-base-v2')

answerEmbedding = model.encode(answer, convert_to_tensor=True)
schemeEmbedding = model.encode(scheme, convert_to_tensor=True)

cosine_similarity = util.cos_sim(answerEmbedding, schemeEmbedding)

print("similarity:", cosine_similarity)