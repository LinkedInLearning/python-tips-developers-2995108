import random
file = open('dat.txt', 'w') 
file.write(str(random.randint(1,100))) 
file.close() 