import subprocess
import sys

# Represent the command ipconfig -all to use in subprocess.Popen
#befehlsliste=[["ipconfig"]],[["ipconfig"]]
befehlsliste=(["ipconfig"],["ifconfig"])
# Send the stdout and stderr of the process to variables we can use in the script.
try:
    with subprocess.Popen(befehlsliste[0], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        stdout=(proc.stdout.read())
        stderr=(proc.stderr.read())
except:
    try:
        with subprocess.Popen(befehlsliste[1], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
            stdout=(proc.stdout.read())
            stderr=(proc.stderr.read())
    except:
        print("Die Anweisung steht nicht zur Verfügung")
        sys.exit()
else:
    print("stdout: %s" % (stdout))
    print("stderr: %s" % (stderr))
