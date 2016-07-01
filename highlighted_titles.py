def get_titles(highlights):
    titles = {}

    for highlight in highlights:
        title = highlight['title']
        t = {}
        t['title'] = title
        t['authors'] = highlight['authors']

        if not title in titles:
            titles[title] = t

    return titles
