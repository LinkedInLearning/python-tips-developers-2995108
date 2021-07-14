import os
import pathlib
dat = pathlib.Path(__file__)
dat2 = "h:\\weeklies"
dat3 = "h:\\weeklies\\test.txt"
print("Absoluter Pfad","\t:\t", dat,"\t:\t",os.path.abspath(dat))
print("Kanonischer Pfad","\t:\t", dat,"\t:\t",os.path.realpath(dat))
print("Realtiver Dateipfad","\t:\t", dat,"\t:\t",os.path.relpath(dat))
print("Basisname","\t:\t", dat,"\t:\t",os.path.basename(dat))
print("Verzeichnisname","\t:\t", dat,"\t:\t",os.path.dirname(dat))
print("Existenz Datei/Verzeichnis","\t:\t", dat,"\t:\t",os.path.exists(dat))
print("Existenz Datei/Verzeichnis","\t:\t", dat2,"\t:\t",os.path.exists(dat2))
print("Existenz Datei/Verzeichnis","\t:\t", dat3,"\t:\t",os.path.exists(dat3))
print("Verzeichnis","\t:\t",dat,"\t:\t",os.path.isdir(dat))
print("Verzeichnis","\t:\t",dat2,"\t:\t",os.path.isdir(dat2))
print("Datei","\t:\t",dat,"\t:\t",os.path.isfile(dat))
print("Datei","\t:\t",dat2,"\t:\t",os.path.isfile(dat2))
print("Dateigroesse","\t:\t",dat,"\t:\t",os.path.getsize(dat))
print("Absolut","\t:\t",dat,"\t:\t",os.path.isabs(dat))


