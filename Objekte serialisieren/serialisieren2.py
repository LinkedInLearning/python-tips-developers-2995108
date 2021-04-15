import pickle
person = {}
person["vname"]=input("Vorname\n")
person["nname"]=input("Nachname\n")
for x in person.values():
    print(x)
try:
    fp = open("dat2.pkl","wb")
    pickle.dump(person,fp)
    fp.close()
except IOError:
    print ("Fehler beim Schreiben der Datei")
except:
    print ("Allgemeines Problem")