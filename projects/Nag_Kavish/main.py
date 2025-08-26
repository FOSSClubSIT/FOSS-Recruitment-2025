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

def frequency():
    """WIP"""
    return

def score_sentences(original_text, freq):
    """WIP"""


    return
"""Generate a summary"""
def summary(text):
    text=preprocess(text)
    freq=frequency(text)
    score= score_sentences(text, freq)

    """WIP"""
    return




#main program
file_path = input("Enter path to your .txt file: ")
text = load(file_path)

print("Original Text")
print(text)

