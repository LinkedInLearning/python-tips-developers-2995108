import subprocess
import sys

# Represent the command ipconfig -all to use in subprocess.Popen
#befehlsliste=[["ipconfig"]],[["ipconfig"]]
befehlsliste=(["ipconfig"],["ifconfig"])
fehler=0
# Send the stdout and stderr of the process to variables we can use in the script.
for x in befehlsliste:
    try:
        with subprocess.Popen(x, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
            stdout=(proc.stdout.read())
            stderr=(proc.stderr.read())
        fehler=0
        break
    except:
        fehler+=1
        continue

if fehler:
    print("Die Anweisung steht nicht zur Verfügung")
else:
    print("stdout: %s" % (stdout))
    print("stderr: %s" % (stderr))
