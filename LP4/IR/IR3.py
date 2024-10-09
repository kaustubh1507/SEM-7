import nltk
from nltk.corpus import stopwords
import string

# Ensure NLTK stopwords are downloaded
nltk.download('stopwords')


# Define a function for text preprocessing
def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()

    # Tokenize the text by splitting into words
    words = text.split()

    # Remove stop words using NLTK's list of English stopwords
    stop_words = set(stopwords.words('english'))

    # Remove punctuation marks
    punctuations = set(string.punctuation)

    # Filter out the stop words and punctuation
    filtered_words = [word for word in words if word not in stop_words and word not in punctuations]

    # Join the filtered words back into a single string
    filtered_text = ' '.join(filtered_words)

    return filtered_text


# Example usage
if __name__ == "__main__":
    # Sample text document
    text_document = """
    Artificial intelligence is revolutionizing the technology world. 
    The future of technology is driven by AI and machine learning innovations.
    """

    # Preprocess the text document (stop word removal)
    cleaned_text = preprocess_text(text_document)

    # Display the result
    print("Original Text:\n", text_document)
    print("\nCleaned Text (after stop word removal):\n", cleaned_text)
