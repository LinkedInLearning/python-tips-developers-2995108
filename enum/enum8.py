from enum import Enum
class Wochentag(Enum):
    Mo = 1
    Di = 2
    Mi = 3
    Do = 4
    Fr = 5
    Sa = 6
    So = 7
print(Wochentag.Di.value)
for i in Wochentag:
    print(i, i.value)