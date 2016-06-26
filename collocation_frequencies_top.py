import json

import collocation_frequencies

with open('./data/highlighted_text.txt') as raw_text, \
        open('./data/collocation_frequencies.json', 'w') as output_file:

    raw_text = raw_text.read()
    fdist = collocation_frequencies.get_fdist(raw_text, 50)
    output = []

    for bigram, frequency in fdist:
        o = {}
        o['frequency'] = frequency
        o['collocation'] = ' '.join(str(i) for i in bigram)

        output.append(o)

    json.dump(output, output_file)    
