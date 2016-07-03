import json

readme_text = """# ebook-highlights\n
Natural language analysis of text I've highlighted on my Kindle.
Updated every once and awhile.

`data/clippings.json` generated with 
[my-clippings-to-json](https://github.com/maximumhallinan/my-clippings-to-json).
"""

def list_collocations(collocations):
    collocations_text = '\n## Top collocations\n\n'

    for index in range(len(collocations)):
        collocation = collocations[index]
        c = collocation['collocation']
        f = collocation['frequency']

        collocations_text += '- %s (%d)\n' % (c,f)

    return collocations_text

def list_highlight_count_by_title(counts_by_title, titles):
    count_text = '\n## Titles highlighted\n\n'

    items = counts_by_title.items()
    items = sorted(items, key=lambda item: item[1], reverse=True)

    for index in range(len(items)):
        item = items[index]

        title = item[0]
        count = item[1]
        authors = titles[title]['authors']
        authors = '; '.join(authors)

        count_text += '- *%s* by %s (%d)\n' % (title,authors,count)

    return count_text

def list_words(words):
    word_text = '\n## Top words\n\n'

    for word in words:
        w = word[0]
        f = word[1]

        word_text += '- %s (%d)\n' % (w,f)

    return word_text

with open('./README.md', 'w') as readme, \
        open('./data/highlighted_titles.json') as titles, \
        open('./data/highlight_count_by_title.json') as counts, \
        open('./data/collocation_frequencies.json') as collocations, \
        open('./data/word_frequencies.json') as words:

    titles = json.load(titles)
    collocations = json.load(collocations)
    counts = json.load(counts)
    words = json.load(words)

    readme_text += list_highlight_count_by_title(counts, titles)
    readme_text += list_words(words)
    readme_text += list_collocations(collocations)

    readme.write(readme_text)
