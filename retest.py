import re

pattern = 'abc'
string = 'abcnjpabcojpdfjpabc'
result = re.findall(pattern, string)
print(result)