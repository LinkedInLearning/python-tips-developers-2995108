import os, sys, time
def fuelle():
    i = 0
    while i < 10:
        print("*x" * 50)
        i += 1
def clear():
    # if sys.platform == "win32": # alternativ
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
fuelle()
time.sleep(5)
clear()
