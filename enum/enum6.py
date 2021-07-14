wochentag = ["Mo","Di","Mi","Do","Fr","Sa","So"]
enum1 = enumerate(wochentag, start=3)
for i in enum1:
    print(i[0], i[1])