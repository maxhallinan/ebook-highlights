import json

import collocation_frequencies

with open('./data/highlighted_text_by_book.json') as json_file, \
        open('./data/collocation_frequencies_by_title.json', 'w') as output_file:

    hl_text_by_title = json.load(json_file)
    collocations_by_title = {}

    for title, text in hl_text_by_title.items():
        collocations_by_title[title] = collocation_frequencies.get_fdist(text, 5)

    for title, fdist in collocations_by_title.items():
        collocations_by_title[title] = []

        for bigram, frequency in fdist:
            o = {}
            o['collocation'] = ' '.join(str(i) for i in bigram)
            o['frequency'] = frequency

            collocations_by_title[title].append(o)

    json.dump(collocations_by_title, output_file)
