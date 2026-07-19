import string
def tokenizer_counter(text):
    translator = str.maketrans('', '', string.punctuation)
    clean = text.translate(translator).lower()
    
    words = clean.split()
    
    map = {}
    for word in words:
        if word in map:
            map[word] += 1
        else:
            map[word] = 1
    
    return dict(sorted(map.items()))