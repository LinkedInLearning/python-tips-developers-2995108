a = input("Geben Sie einen mathematischen Ausdruck ein\n")
try:
    b = eval(a)
except:
    print("Der Ausdruck ist nicht zu evaluieren")
else:
    print(b) 
