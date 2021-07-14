import json

jsonObj = {"titel": "RJS EDV-KnowHow","url": "http://rjs.de",	"bemerkung": "Homepage"	}
print(type(jsonObj), jsonObj)

# Erstelle JSON-String
jsonstring = json.dumps(jsonObj)



print(type(jsonstring), jsonstring)
