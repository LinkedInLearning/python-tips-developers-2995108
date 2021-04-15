import re
t1 = "Die Antwort ist 42."
menge = re.search('\d', t1)
print(menge.group(0))
print(menge.group())
menge = re.match(r"(\d+)\.(\d+)", "3.14")
print(menge.groups())
print(menge.lastindex )
print(menge.group(menge.lastindex))
for i in menge.groups():
    print(i)
