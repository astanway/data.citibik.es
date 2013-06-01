import os
import requests
import simplejson as json

url = "http://appservices.citibikenyc.com/data2/stations.php"
r = requests.get(url)
data = json.loads(r.content)

stations = {}
for station in data['results']:
    stations[station['id']] = station['label']

with open('id_mapper.json', 'w') as f:
    f.write(json.dumps(stations))
    