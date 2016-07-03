import json

import word_frequencies

with open('texts/highlighted_text.txt') as text_file, \
        open('data/word_frequencies.json', 'w') as output_file:

    text = text_file.read()
    words_fdist = word_frequencies.get_fdist(text, 25)

    json.dump(words_fdist, output_file)
