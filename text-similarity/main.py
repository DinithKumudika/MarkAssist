import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):

     # Tokenize the text into individual words
    tokens = nltk.word_tokenize(text.lower())

     # Remove stopwords (common words that do not contribute much to the similarity)
    stopwords = nltk.corpus.stopwords.words('english')
    
    filtered_words = [word for word in tokens if word not in stopwords]

    # Return the preprocessed text as a single string
    return ' '.join(filtered_words)

52 
# Read and preprocess the contents of the text files

with open('file1.txt', 'r') as file:
    file1_contents = file.read()
    file1_processed = preprocess(file1_contents)

with open('file2.txt', 'r') as file:
    file2_contents = file.read()
    file2_processed = preprocess(file2_contents)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the vectorizer on the preprocessed texts
vectors = vectorizer.fit_transform([file1_processed, file2_processed])

# Calculate the cosine similarity between the vectors
similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

similarity_percentage = round(similarity * 100, 2)
print(f"The similarity between the two text files is: {similarity_percentage}%")
