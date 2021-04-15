try:
    file = open('dat.txt', 'r')     
    print(file.read())
except:
    print("Problem beim Lesen")
finally:
    file.close() 