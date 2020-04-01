import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#like a file
dic = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        dic[word] = dic.get(word,0) + 1

#print(line.decode().strip())
print(dic)

#in this fashion we can retrive a html file too.