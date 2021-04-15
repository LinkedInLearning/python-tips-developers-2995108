import sys
a = 42
print("Referenz-Counter einer globalen Variablen mit dem Wert 42: %s" % sys.getrefcount(a)) 
 
def meineFkt1(b):
    print("Referenz-Counter einer globalen Variablen mit dem Wert 42 innerhalb der Funktion: %s" 
    % sys.getrefcount(a)) 

def meineFkt2(b):
    a = b
    print("Referenz-Counter einer lokalen Variablen mit dem Wert 42 innerhalb der Funktion: %s" 
    % sys.getrefcount(a)) 
 
print("\n", "*" * 40, "Funktion meineFkt1 wird aufgerufen", "*" * 40,"\n") 
meineFkt1(a)
print("Referenz-Counter einer globalen Variablen mit dem Wert 42 nach Aufruf der Funktion meineFkt1: %s" % sys.getrefcount(a)) 

print("\n", "*" * 40, "Funktion meineFkt2 wird aufgerufen", "*" * 40,"\n") 
meineFkt2(a)
print("Referenz-Counter einer globalen Variablen mit dem Wert 42 nach Aufruf der Funktion meineFkt2: %s" % sys.getrefcount(a)) 
