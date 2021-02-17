# regular expressions - not unique to python 
# used in validation like password

import re


pattern = re.compile('this')
string = 'search inside of this text please!'
# print('search' in string) 

a = re.search('this', string)
# <re.Match object; span=(17, 21), match='this'>
# print(a.span()) # where the string occurs
# print(a.start())
# print(a.end)
# print(a.group())

# used in multiple searches

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.match(string)
print(c)