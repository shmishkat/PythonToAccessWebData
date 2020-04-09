import urllib.parse
import urllib.request

import json
target = 'http://py4e-data.dr-chuck.net/json?'
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key' : 42})

#print('Retriving', url)
data = urllib.request.urlopen(url).read()
#print('Retrived', len(data), 'characters')
js = json.loads(data)

print('Place id', js['results'][0]['place_id'])