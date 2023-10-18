import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the two sentences
sentence1 = "A router is a device that connects computer networks together and directs data traffic between them. It determines the best path for data packets to reach their destinations and can provide additional features like security and network management."
sentence2 = "A router is a piece of hardware that links computer networks and controls data traffic between them. It chooses the most efficient route for data packets to take in order to get to their intended locations. It can also offer extra features like security and network administration."

# Tokenize the sentences
sentences = [sentence1, sentence2]
tokenizer = nltk.RegexpTokenizer(r'\w+')
tokenized_sentences = [tokenizer.tokenize(sentence) for sentence in sentences]

# Convert sentences to lowercase
lowercase_sentences = [[token.lower() for token in sentence] for sentence in tokenized_sentences]

# Convert sentences to TF-IDF vectors
sentence_vectors = TfidfVectorizer().fit_transform([' '.join(sentence) for sentence in lowercase_sentences])

# Calculate cosine similarity
cosine_sim = cosine_similarity(sentence_vectors[0], sentence_vectors[1])[0][0]

# Convert cosine similarity to percentage
similarity_percentage = cosine_sim * 100

# Print the similarity percentage
print(f"The similarity between the sentences is: {similarity_percentage:.2f}%")
