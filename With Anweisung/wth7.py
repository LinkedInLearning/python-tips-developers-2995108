mgr = open('dat.txt', 'r')
print(type(mgr))
print(type(mgr).__init__)
print(type(mgr).__enter__)

print(type(mgr).__exit__)


with mgr as file:
    print(file.read())