wochentag = ["Mo","Di","Mi","Do","Fr","Sa","So"]
enum1 = enumerate(wochentag, start=3)
print(enum1.__next__())
print(enum1.__next__())
print(enum1.__next__())

