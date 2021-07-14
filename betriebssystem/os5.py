import os, time
dat = "H:\\xxxxx"
os.mkdir(dat)
print("Verzeichnis {} erstellt".format(dat))
time.sleep(10)
os.rmdir(dat)
print("Verzeichnis {} beseitigt".format(dat))

