import json

readme_text = """# ebook-highlights\n
Stats about what I've highlighted on my Kindle\n
"""

def list_titles(titles):
   titles_text = '\n## Titles\n\n' 

   for title in titles:
       t = title['title']
       a = ', '.join(title['authors'])

       titles_text += '- *%s* by %s \n' % (t, a)

   return titles_text

def list_collocations(collocations):
    collocations_text = '\n## Top 25 collocations (word pairs)\n\n'

    for index in range(len(collocations)):
        collocation = collocations[index]
        c = collocation['collocation']
        f = collocation['frequency']

        collocations_text += '%d. %s (%d)\n' % (index + 1, c, f)

    return collocations_text

with open('./README.md', 'w') as readme, \
        open('./data/highlighted_titles.json') as titles, \
        open('./data/collocation_frequencies.json') as collocations:

    titles = json.load(titles)
    collocations = json.load(collocations)
    
    readme_text += list_titles(titles)
    readme_text += list_collocations(collocations) 

    readme.write(readme_text)
