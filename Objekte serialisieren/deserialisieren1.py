import pickle
input = open("data.pkl","rb")
data = pickle.load(input)
input.close()
for i in data:
    print(i)