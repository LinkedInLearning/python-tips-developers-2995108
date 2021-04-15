import os
import re
import sys

args = sys.argv

# Declare lists
dateiengesamt = []
dateienspeziell = []

# Iterate through the files.
if len(args) > 1:
    for arg in args[2:]:
        dateiengesamt.append(os.path.abspath(arg))
        if os.path.abspath(arg).endswith(args[1]):
            dateienspeziell.append(os.path.abspath(arg))
    print("Insgesamt %s Datei(en)." % (len(dateiengesamt)))
    print("Dateien mit der Erweiterung %s kommen %sx vor." % (args[1], len(dateienspeziell)))
    print("Der Anteil der gesuchten Dateien betraegt ca %s Prozent" % ((round(float(len(dateienspeziell))/int(len(dateiengesamt))*100))))
else:
    print("Bitte eine Dateiendung und ein Verzeichnis als Parameter angeben")

