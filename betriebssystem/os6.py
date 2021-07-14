import os, time
dat = "H:\\xxxxx"
try:
    os.mkdir(dat)
    print("Verzeichnis {} erstellt".format(dat))
except:
    print("Verzeichnis schon vorhanden oder sonst ein Fehler beim Erstellen")
time.sleep(10)
try:
    os.rmdir(dat)
    print("Verzeichnis {} beseitigt".format(dat))
except:
    print("Verzeichnis nicht vorhanden oder sonst ein Fehler beim Löschen")
