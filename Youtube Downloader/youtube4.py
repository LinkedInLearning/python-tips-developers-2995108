import pytube
import pprint
import sys
if len(sys.argv)< 2:
    print("Das Programm benötigt den URL der Mediadatei als ersten Parameter")
    sys.exit()
def weiter(stream, file_handle):
    print("Fertig geladen", stream, file_handle)
print(sys.argv[1])
try:    

    video = pytube.YouTube(sys.argv[1])
    video.streams.filter(only_audio=True)
    pprint.pprint( video.streams.filter(only_audio=True))
    print("Registrieren Callback")
    video.register_on_complete_callback(weiter)
    print("Download starten")
    video.streams.filter(only_audio=True).first().download()
except:
    print("Fehler beim Download")