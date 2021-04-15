import pytube
import pprint
import sys
if len(sys.argv)<3:
    print("Das Programm benötigt den URL der Mediadatei als ersten Parameter und eine Angabe, welches Dateiformat geladen werden soll")
    sys.exit()
def weiter(stream, file_handle):
    print("Fertig geladen", stream, file_handle)
print(sys.argv[1], sys.argv[2])
try:    

    video = pytube.YouTube(sys.argv[1])
    video.streams.filter(subtype=sys.argv[2])
    print("Registrieren Callback")
    video.register_on_complete_callback(weiter)
    print("Download starten")
    video.streams.first().download()
except:
    print("Fehler beim Download")