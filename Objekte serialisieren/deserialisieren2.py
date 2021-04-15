import pickle

try:
    fp = open("dat2.pkl","rb")
    data = pickle.load(fp)
    fp.close()
except IOError:
    print ("Fehler beim Lesen der Datei")
except:
    print ("Allgemeines Problem")

print(data)
print(data["vname"])
print(type(data))
for x in data:
    print(x)
for x in data.values():
    print(x)