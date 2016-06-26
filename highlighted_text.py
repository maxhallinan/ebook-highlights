import json

with \
    open('./data/highlights.json') as highlights_file, \
    open('./data/highlighted_text.txt', 'a') as corpus:

        highlights = json.load(highlights_file)

        for highlight in highlights:
            corpus.write(' ' + highlight['body'])
