import string

# ---------------- STOPWORDS ---------------- #
#Most commonly used words in sentances that doesn't mean much meaning.
STOPWORDS = {
    "the", "and", "is", "in", "to", "of", "by", "an", "be", "at", "this", "that", 
    "are", "it", "from", "a", "for", "on", "with","as", }

"""Read text from a .txt file"""
def load(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
""" Removing punctuation likes !"#$%."""
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
            if word in freq:        
                freq[word] += 1
            else:                 
                freq[word] = 1
    return freq

"""Assign a score to each sentence based on word frequencies"""
def score_sentences(original_text, freq):
    sentences = original_text.split(".")
    scores = {}
    for i in sentences:
        words = i.lower().split()
        count = 0
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
    total_sentences = len(best)
    num_sentences = max(1, total_sentences // 3)  
    best = best[:num_sentences]
    result = []
    for s in best:
        if s.strip():
            result.append(s.strip())
    return ". ".join(result)

#main program
file_path = input("Enter path to your .txt file: ")
text = load(file_path)

print("Original Text")
print(text)

