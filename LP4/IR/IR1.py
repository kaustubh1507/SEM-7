from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Download necessary NLTK data files
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)

def preprocess(text):
    # Lowercase the text
    text = text.lower()
    # Tokenize and remove punctuation
    tokens = [word for word in text.split() if word not in punctuations]
    # Remove stopwords and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Define the documents
doc1 = "Artificial Intelligence is revolutionizing technology."
doc2 = "Technology is being revolutionized by Artificial Intelligence."

# Apply preprocessing to both documents
processed_doc1 = preprocess(doc1)
processed_doc2 = preprocess(doc2)

print("Processed Document 1:", processed_doc1)
print("Processed Document 2:", processed_doc2)

# Create the TfidfVectorizer
vectorizer = TfidfVectorizer()

# Vectorize the documents
tfidf_matrix = vectorizer.fit_transform([processed_doc1, processed_doc2])

# Compute the cosine similarity
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

# Display the similarity score
print(f"Cosine Similarity between Document 1 and Document 2: {similarity[0][0]:.4f}")
