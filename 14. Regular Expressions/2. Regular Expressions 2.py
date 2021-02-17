import re

pattern = re.compile(r"([a-zA-Z].([a]))")
string = 'search inside of this text please! Chav!'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.match(string)

print(a.groups())