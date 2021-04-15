import random
try:
    file = open('dat.txt', 'w') 
    file.write(str(random.randint(1,100))) 
except:
    print("Problem beim Schreiben")
finally:
    file.close() 