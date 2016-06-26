import nltk
from nltk import word_tokenize

stopwords = nltk.corpus.stopwords.words('english')

with open('./data/highlighted_text.txt') as raw_text:
    tokens = word_tokenize(raw_text.read())
    tokens = [t for t in tokens if len(t) > 1]
    tokens = [t for t in tokens if not t.isnumeric()]
    tokens = [t for t in tokens if t.lower() not in stopwords]
    bigrams = nltk.bigrams(tokens)

    fdist = nltk.FreqDist(bigrams)

    for bigram, frequency in fdist.most_common(50):
        collocation = ' '.join(str(i) for i in bigram)
        print('%s: %d' % (collocation, frequency))
