import json

import pathlib

# Datei öffnen
with open(str(pathlib.Path(__file__).parent.absolute()) + "\dat.json", "r") as fh:
    jsonStr=fh.read()

# parsen des JSON-Strings
pythonObj = json.loads(jsonStr)

print(type(pythonObj))

print(type(pythonObj),pythonObj)

print("*" * 100)
webseiten = pythonObj["webseiten"]
print(webseiten)