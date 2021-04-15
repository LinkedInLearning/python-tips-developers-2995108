import os
import re
import sys
import platform
import glob

# Define or gather the options and files to use
args = sys.argv

if "Windows" in platform.platform():
    os_system=0
else:
    os_system=1
print(os_system)
# Declare a list to hold the [deck name, slide count]
dateiengesamt = []
dateienspeziell = []
# Set an initial value for the summary option.

# Iterate through the files.
if len(args) > 1:
    if os_system==0:
       for arg in glob.glob(os.path.abspath(args[2])):
           dateiengesamt.append(os.path.abspath(arg))
           if os.path.abspath(arg).endswith(args[1]):
               dateienspeziell.append(os.path.abspath(arg))
    else:
        for arg in args[2:]:
            dateiengesamt.append(os.path.abspath(arg))
            if os.path.abspath(arg).endswith(args[1]):
                dateienspeziell.append(os.path.abspath(arg))
    print("Insgesamt %s Datei(en)." % (len(dateiengesamt)))
    print("Dateien mit der Erweiterung %s kommen %sx vor." % (args[1], len(dateienspeziell)))
    print("Der Anteil der gesuchten Dateien betraegt ca %s Prozent" % ((round(float(len(dateienspeziell))/int(len(dateiengesamt))*100))))

else:
    print("Bitte eine Dateiendung und ein Verzeichnis als Parameter angeben")

