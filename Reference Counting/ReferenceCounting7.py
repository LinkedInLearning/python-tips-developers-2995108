import sys
for x in ["python", "version", "if", "for", "while","error","def"]:
    print (x, sys.getrefcount(x))
