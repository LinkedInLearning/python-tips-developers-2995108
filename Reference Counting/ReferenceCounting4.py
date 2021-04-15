import sys
x = 42
print("Referenz-Counter einer Variablen x mit dem Wert 42: %s" % sys.getrefcount(x))
print("\n", "*" * 40, "x wird y zugewiesen", "*" * 40,"\n") 
y = x
print("Referenz-Counter einer Variablen x mit dem Wert 42: %s" % sys.getrefcount(x))
print("Referenz-Counter einer Variablen y Verweis auf x: %s" % sys.getrefcount(y))
print("\n", "*" * 40, "Wert von y wird erhöht", "*" * 40,"\n") 
y += 1
print("Referenz-Counter einer Variablen x mit dem Wert 42: %s" % sys.getrefcount(x))
print("Referenz-Counter einer Variablen y Verweis auf x: %s" % sys.getrefcount(y))
