import json

readme_text = """# ebook-highlights\n
Natural language analysis of text I've highlighted on my Kindle.
Updated every once and awhile.
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

with open('./README.md', 'w') as readme, \
        open('./data/highlighted_titles.json') as titles, \
        open('./data/highlight_count_by_title.json') as counts, \
        open('./data/collocation_frequencies.json') as collocations:

    titles = json.load(titles)
    counts = json.load(counts)
    collocations = json.load(collocations)

    readme_text += list_highlight_count_by_title(counts, titles)
    readme_text += list_collocations(collocations)

    readme.write(readme_text)
