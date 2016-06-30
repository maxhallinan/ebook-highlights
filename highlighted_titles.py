def get_titles(highlights):
    titles = []

    for highlight in highlights:
        t = {}
        t['title'] = highlight['title']
        t['authors'] = highlight['authors']

        if not t in titles:
            titles.append(t)

    titles = sorted(titles, key=lambda t: t['title'].replace('The ', ''))

    return titles
