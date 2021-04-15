import re
    
t1 = "Die Antwort ist 42"
pattern = '\d'

match = re.findall(pattern ,t1)
print(match)
for x in match:
    print(x)


pattern = '[a-z]{3}'

match = re.findall(pattern ,t1)
print(match)
