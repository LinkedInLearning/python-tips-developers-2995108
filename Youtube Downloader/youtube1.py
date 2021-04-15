import pprint
import pytube 
video = pytube.YouTube('https://www.youtube.com/watch?v=958o6kXlkuA')
print(type(video.streams))
pprint.pprint(video.streams)
#video.streams.get_by_itag(18).download()
print("Registrieren Callback")
def weiter(stream, file_handler):
    print("Fertig", stream, file_handler)
video.register_on_complete_callback(weiter)
print("Download starten")
video.streams.first().download()
