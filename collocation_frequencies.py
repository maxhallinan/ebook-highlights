import nltk
from nltk import word_tokenize

stopwords = nltk.corpus.stopwords.words('english')

def get_fdist(raw_text, most_common=50):
    tokens = word_tokenize(raw_text)
    tokens = [t for t in tokens if len(t) > 1]
    tokens = [t for t in tokens if not t.isnumeric()]
    tokens = [t for t in tokens if t.lower() not in stopwords]

    bigrams = nltk.bigrams(tokens)

    fdist = nltk.FreqDist(bigrams)
    fdist = fdist.most_common(most_common)

    return fdist;    
