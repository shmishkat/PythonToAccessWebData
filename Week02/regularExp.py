import re

handle = open('mbox-short.txt')

for line in handle:
    line = line.rstrip()

    if re.search('From: ',line):
        print(line)

'''
Wild card characters in regex

^ - caret character : start with
. - dot character : any character
* - asterisk character : 0 or many 
\S - match any non-white character

^X.*:
or 
^X-\S+:

'''

