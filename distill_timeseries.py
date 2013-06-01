import os
import simplejson as json
import msgpack
from collections import defaultdict

timeseries = defaultdict(str)

for timestamp in os.listdir('data'):
    with open('data/' + timestamp, 'r') as f:
        data = json.loads(f.read())
        for station in data['results']:
            timeseries[station['id']] += timestamp + ','
            timeseries[station['id']] += str(station['availableDocks']) + ','
            timeseries[station['id']] += str(station['availableBikes']) + '\n'


for k, v in timeseries.items():
    with open('timeseries/' + str(k) + '.csv', 'w') as f:
        header = 'date,availableBikes,availableDocks\n'
        body = header + v
        f.write(body)
