import pickle
data = (2,3,5,7)
output = open("data.pkl","wb")
pickle.dump(data,output)
output.close()