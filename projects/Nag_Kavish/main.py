import string

#STOPWORDS
# Most commonly used words in sentences that don't add much meaning
STOPWORDS = {
    "the", "and", "is", "in", "to", "of", "by", "an", "be", "at", "this", "that",
    "are", "it", "from", "a", "for", "on", "with", "as",
}

"""Read text from a .txt file"""
def load(file_path):
    with open(file_path, "r") as f:
        return f.read()

"""Removing punctuation like !"#$%."""
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

"""Return a dictionary of word frequencies (ignoring stopwords)"""
def frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        if word not in STOPWORDS:
            freq[word] = freq.get(word, 0) + 1
    return freq

"""Assign a score to each sentence based on word frequencies"""
def score_sentences(original_text, freq):
    sentences = original_text.split(".")
    scores = {}
    for i in sentences:
        words = i.lower().split()
        score = 0   #initialize score for each sentence
        for j in words:
            if j in freq:
                score += freq[j]
        if len(words) > 0:
            scores[i] = score / len(words)  # normalize
    return scores

"""Generate a summary"""
def summary(text):
    # Preprocess and get frequencies
    clean_text = preprocess(text)
    freq = frequency(clean_text)
    scores = score_sentences(text, freq)

    # Sort all sentences by score (highest first)
    best = sorted(scores, key=scores.get, reverse=True)

    # Take top 30% of sentences
    total = len(best)
    num_sentences = max(1, total // 3)
    best = best[:num_sentences]

    #Cleaned sentences
    result = []
    for s in best:
        if s.strip():
            result.append(s.strip())
    return ". ".join(result)


file_path = input("Enter path to your .txt file: ").strip()

# Auto-add ".txt" if missing
if not file_path.endswith(".txt"):
    file_path += ".txt"

# Try to load safely
try:
    text = load(file_path)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()
except Exception as e:
    print(f"Unexpected error: {e}")
    exit()

print("\nOriginal Text:\n")
print(text)
summarized = summary(text)
print("\nSummary:\n")
print(summarized)
