import urllib.request, urllib.parse, urllib.error, urllib
import json

url = "http://py4e-data.dr-chuck.net/comments_401612.json"

urlHandle = urllib.request.urlopen(url)
data = urlHandle.read()

info = json.loads(data)
count = 0
for item in info["comments"]:
    num = int(item["count"])
    count = count + num

print(count)
