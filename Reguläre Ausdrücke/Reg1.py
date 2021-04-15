import re
    
t1 = "Die Antwort ist 42"
pattern = '[a-zA-C]{2,4}'
match = re.search(pattern,t1)

print(match)
print(match.span())
print("Trefferbereich von %s bis %s" % match.span())
if match:
    print("Gefunden")
else:
    print("Nicht Gefunden")

pattern = '[0-9]{2}'
match = re.search(pattern,t1)

print(match)
print(match.span())

print("Trefferbereich von %s bis %s" % match.span())
if match:
    print("Gefunden")
else:
    print("Nicht Gefunden")