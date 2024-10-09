from collections import Counter
from functools import reduce
import re


# Define the mapper function
def mapper(text):
    # Convert text to lowercase and filter only alphabetic characters
    clean_text = re.sub(r'[^a-zA-Z]', '', text.lower())

    # Count occurrences of each character using collections.Counter
    return Counter(clean_text)


# Define the reducer function
def reducer(counter1, counter2):
    # Combine the counts from both Counters
    return counter1 + counter2


# Example usage
if __name__ == "__main__":
    # Example dataset
    dataset = [
        "Artificial Intelligence is revolutionizing technology.",
        "The future of technology is driven by AI and machine learning innovations.",
        "We are living in an era of intelligent systems."
    ]

    # Map step: apply the mapper to each document in the dataset
    mapped = map(mapper, dataset)

    # Reduce step: aggregate the character counts from all documents
    reduced_result = reduce(reducer, mapped)

    # Display the final result (character counts)
    for letter, count in sorted(reduced_result.items()):
        print(f"{letter}: {count}")
