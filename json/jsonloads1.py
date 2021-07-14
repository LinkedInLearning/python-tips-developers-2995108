import json

# JSON-String
jsonStr =  '{"titel": "RJS EDV-KnowHow","url": "http://rjs.de",	"bemerkung": "Homepage"	}'

# parsen des JSON-Strings
pythonObj = json.loads(jsonStr)

print(type(pythonObj),pythonObj)


url = pythonObj['url']
print(url)