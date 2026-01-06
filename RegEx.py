import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
a = re.findall("ai", txt)
b = re.findall("b", txt)
c = re.split("\s", txt, 1)
print(x)
print(a)
print(b)
print(c)