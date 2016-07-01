import json

with open('./data/highlights.json') as highlights_file, \
        open('./data/highlight_count_by_title.json', 'w') as output_file:

    highlights = json.load(highlights_file)
    highlight_count_by_title = {}

    for highlight in highlights:
        title = highlight['title']

        if title in highlight_count_by_title:
            highlight_count_by_title[title] += 1
        else:
            highlight_count_by_title[title] = 1

    json.dump(highlight_count_by_title, output_file)
