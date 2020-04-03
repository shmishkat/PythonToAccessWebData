from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_401609.html'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
sum = 0
for num in soup('span'):
    sum = sum + int(num.contents[0])
print(sum)