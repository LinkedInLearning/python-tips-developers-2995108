import subprocess

# Represent the command ipconfig -all to use in subprocess.Popen
the_command = ["ipconfig"]
# Send the stdout and stderr of the process to variables we can use in the script.
with subprocess.Popen(the_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
    stdout=(proc.stdout.read())
    stderr=(proc.stderr.read())
# View the output of each variable.
print("stdout: %s" % (stdout))
#stdout2 = stdout.decode('cp1252')
#print(stdout2)
print("stderr: %s" % (stderr))
#stderr2 = stderr.decode('cp1252')
#print(stderr2)