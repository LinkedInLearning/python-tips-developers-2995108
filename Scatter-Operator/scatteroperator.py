l1 = [2,3,5,7]
print(l1)
print(*l1)
def test1(*arg):
    print(arg, type(arg))
test1(l1)
test1(*l1)
person = {"vname":"Ralph","nname":"Steyer"}
print(person)
print(*person)
def test2(vname,nname):
    print(vname,nname)
test2(**person)
