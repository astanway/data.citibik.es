import sys
import os
import socket
import simplejson as json
import msgpack
from collections import defaultdict

timeseries = defaultdict(str)

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003

sock = socket.socket()
sock.connect((CARBON_SERVER, CARBON_PORT))

for timestamp in os.listdir('data'):
    with open('data/' + timestamp, 'r') as f:
        data = json.loads(f.read())
        for station in data['results']:
            lines = []
            station['timestamp'] = data['lastUpdate']
            station['label'] = removeNonAscii(station['label'])
            station['label'] = station['label'].replace(' ', '-').replace('.', '').replace('\'', '')
            lines.append('%(label)s.available_bikes %(availableBikes)s %(timestamp)s' % station)
            lines.append('%(label)s.available_docks %(availableDocks)s %(timestamp)s' % station)
            message = '\n'.join(lines) + '\n'
            sock.sendall(message)


#for k, v in timeseries.items():
#    with open('timeseries/' + str(k) + '.csv', 'w') as f:
#        header = 'date,availableBikes,availableDocks\n'
#        body = header + v
#        f.write(body)
