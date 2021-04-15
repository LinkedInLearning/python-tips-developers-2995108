import re
t1 = "45 EUR"
prog = re.compile(r"\d+")
menge = prog.match(t1)
print(menge.group())
