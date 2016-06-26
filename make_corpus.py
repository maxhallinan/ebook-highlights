import json

with \
    open('./data/highlights.json') as highlights_file, \
    open('./data/corpus.txt', 'a') as corpus:

        highlights = json.load(highlights_file)

        for highlight in highlights:
            corpus.write(' ' + highlight['body'])
