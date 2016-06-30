import json

readme_text = """# ebook-highlights\n
Stats about what I've highlighted on my Kindle\n
"""

def build_titles_list(titles):
   titles_text = '# Titles\n\n' 

   for title in titles:
       t = title['title']
       a = ', '.join(title['authors'])

       titles_text += '- *%s* by %s \n' % (t, a)

   titles_text += '\n'

   return titles_text

with open('./README.md', 'w') as readme, \
        open('./data/highlighted_titles.json') as titles:

    titles = json.load(titles)
    
    readme_text += build_titles_list(titles)

    readme.write(readme_text)
