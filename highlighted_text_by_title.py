import json

with \
    open('./data/highlights.json') as highlights_file, \
    open('./data/highlighted_text_by_book.json', 'w') as output_file:
        highlights = json.load(highlights_file)
        by_book = {}

        for highlight in highlights:
            book_title = highlight['title']

            if book_title in by_book:
                by_book[book_title] += ' ' + highlight['body']
            else:
                by_book[book_title] = highlight['body']
        
        json.dump(by_book, output_file)
