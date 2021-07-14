x = input("Geben Sie eine Zahl ein\n")
action = ""
# Wenn Zahl kleiner 18 Zugang verboten sonst Zugang gewährt
if int(x) < 18:
    action = "Zugang verboten"
else:
    action = "Zugang gewährt"
print(action)

action = "Zugang verboten" if int(x) < 18 else "Zugang gewährt"
print(action)


