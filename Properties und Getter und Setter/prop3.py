class A:
    name=property(lambda self:"Meier")


o1 = A()
print("Speicheradresse Instanz %s" % o1)
print("Zugriff über Instanz %s" % o1.name)
print("Zugriff über Klasse %s - nur Propertieobjekt" % o1.name)

o2 = o1
print("Speicheradresse Instanz %s" % o2)


