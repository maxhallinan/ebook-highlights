from datetime import datetime
import json

with open('./data/highlights.json') as highlights, \
        open('./data/by_date_created.json', 'w') as output_file:

    highlights = json.load(highlights)

    highlights_by_date = {}
    
    for highlight in highlights:
        created_at = highlight['created_at']
        dt = datetime.fromtimestamp(created_at)
        date = dt.date()
        date_str = date.strftime('%m-%d-%Y')

        if not date_str in highlights_by_date:
            highlights_by_date[date_str] = []

        highlights_by_date[date_str].append(highlight)

    for date, hls in highlights_by_date.items():
        highlights_by_date[date] = sorted(hls, key=lambda h: h['created_at'])

    json.dump(highlights_by_date, output_file)
