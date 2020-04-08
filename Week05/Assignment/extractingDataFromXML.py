#Extracting data from XML.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et

url = "http://py4e-data.dr-chuck.net/comments_401611.xml"

xml = urllib.request.urlopen(url).read()
tree = et.fromstring(xml)
counts = tree.findall('.//count')
print("Count: " + str(len(counts)))

counter = 0
for count in counts:
    counter += int(count.text)

print("Sum:" + str(counter))