import json

import highlighted_titles

with open('./data/highlights.json') as highlights, \
        open('./data/highlighted_titles.json', 'w') as output_file:

    highlights = json.load(highlights)

    titles = highlighted_titles.get_titles(highlights)

    json.dump(titles, output_file)
