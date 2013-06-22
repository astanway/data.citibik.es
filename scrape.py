import os
import simplejson as json
import time
import requests
import socket

url = "http://appservices.citibikenyc.com/data2/stations.php"
r = requests.get(url)
try:
    data = json.loads(r.content)
except:
    print r.content
    raise Exception("No JSON dog")

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2013

sock = socket.socket()
sock.connect((CARBON_SERVER, CARBON_PORT))
s = socket.socket()
s.connect((CARBON_SERVER, 2003))

for station in data['results']:
    lines = []
    station['timestamp'] = data['lastUpdate']
    station['label'] = removeNonAscii(station['label'])
    station['label'] = station['label'].replace(' ', '-').replace('.', '').replace('\'', '')
    lines.append('%(label)s.available_bikes %(availableBikes)s %(timestamp)s' % station)
    lines.append('%(label)s.available_docks %(availableDocks)s %(timestamp)s' % station)
    message = '\n'.join(lines) + '\n'
    sock.sendall(message)
    s.sendall(message)
