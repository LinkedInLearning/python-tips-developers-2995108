try:
    with open('dat.txt', 'r') as file:
        print(file.read())
except:
    print("Fehler")