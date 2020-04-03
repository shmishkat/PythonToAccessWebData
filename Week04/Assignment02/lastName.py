from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Karn.html'

html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html,'html.parser')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href')

print(url)


#print(soup.prettify())