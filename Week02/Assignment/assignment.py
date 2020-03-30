import re
handle = open('regex_sum_401607.txt')
s = 0
for line in handle:
    line = line.rstrip()
    numList = re.findall('[0-9]+', line)

    for i in numList:
        s = s + int(i)

print(s)