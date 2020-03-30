import re
text = 'Q903HP1EPT AOZGTLGW3P XMB8O5E7QS H3IBPQX1E4 SYEC7KV5NK AIHZE22ZY7 HU4K8Z4B3R ETGMJXF910 3A51ZW3NSC ACMRWN1QHI'

num = re.findall('[0-9]+',text)

vowels = re.findall('[AEIOU]+',text)

print(num)
print(vowels)

'''
---greedy matching
gets the largest valid match.
usuailly the one or more charachter pattern gets greedy i.e. ^F.+: here the dot gets  greedy.

but ^F.+?: in here "?" says don't be greedy.
'''

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

emailAdd = re.findall('\S+@\S+',data)
'''here @ is also greedy'''
print(emailAdd)

#matching and extracting differently
email = re.findall('^From (\S+@\S+)',data)
print(email)

y = re.findall('@([^ ]*)',data)
print(y)
'''
^	Matches the beginning of a line
$	Matches the end of the line
.	Matches any character
\s	Matches whitespace
\S	Matches any non-whitespace character
*	Repeats a character zero or more times
*?	Repeats a character zero or more times (non-greedy)
+	Repeats a character one or more times
+?	Repeats a character one or more times (non-greedy)
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	Indicates where string extraction is to start
)	Indicates where string extraction is to end
'''