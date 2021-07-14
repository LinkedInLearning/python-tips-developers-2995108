import json
import pathlib
jsonObj = {"titel": "RJS EDV-KnowHow","url": "http://rjs.de",	"bemerkung": "Homepage"	}
print(type(jsonObj), jsonObj)

# Erstelle JSON-String
jsonstring = json.dumps(jsonObj)



print(type(jsonstring), jsonstring)
with open(str(pathlib.Path(__file__).parent.absolute()) + "\dat2.json", "w") as fh:
    fh.write(jsonstring)
