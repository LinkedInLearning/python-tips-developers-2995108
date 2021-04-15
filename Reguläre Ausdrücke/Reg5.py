import re
t1 = "Die Antwort ist 42."
print(re.split('\\d', t1))
print(re.split('\W+', "Die Antwort   ist     42."))
print(re.split('\\d', "Die Antwort ist 42."))
print(re.split(r"\d", "Die Antwort ist 42."))
print(re.split("\\d", "Die Antwort ist 42."))
print(re.split(r"\\d", "Die Antwort ist 42."))
