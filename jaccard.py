import nltk
from nltk.tokenize import word_tokenize

# Download 'punkt' resource
nltk.download('punkt')

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def tokenize(text):
    return set(word_tokenize(text.lower()))  # Assuming you want case-insensitive comparison

# Example usage
document1 = "The quick brown fox jumps over the lazy dog."
document2 = "A quick brown dog jumps over the lazy fox."

# Tokenize the documents
tokens1 = tokenize(document1)
tokens2 = tokenize(document2)

# Calculate Jaccard similarity
similarity = jaccard_similarity(tokens1, tokens2)

print(f"Jaccard Similarity: {similarity}")

