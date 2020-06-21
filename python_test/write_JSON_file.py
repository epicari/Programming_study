#
# write JSON to a file
#
#

import json

data = {}
data['bread'] = []
data['bread'].append({
    'breadType': 'cream',
    'recipe': {
        'flour': 100,
        'water': 100,
        'cream': 200
    }
})

with open('bread_data.json', 'w') as outfile:
    json.dump(list(data.values()), outfile)