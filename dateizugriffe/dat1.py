import pathlib
dat1 = pathlib.Path("H:\\Weeklies")
dat2 = pathlib.Path(__file__) 
print(dat1)
print(dat2)

print("Elternverzeichnis","\t:\t", dat1,"\t:\t",dat1.parent)
print("Elternverzeichnis","\t:\t", dat2,"\t:\t",dat2.parent)
print("Absolutpfad","\t:\t", dat1,"\t:\t",dat1.absolute())
print("Absolutpfad","\t:\t", dat2,"\t:\t",dat2.absolute())
print("Dateierweiterung","\t:\t", dat1,"\t:\t",dat1.suffix)
print("Dateierweiterung","\t:\t", dat2,"\t:\t",dat2.suffix)
