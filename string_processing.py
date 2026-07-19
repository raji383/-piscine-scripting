import re

def tokenize(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z0-9\s]', ' ', sentence)
    tokens = []
    for word in sentence.split():
        if word:
            tokens.append(word)
    return tokens
