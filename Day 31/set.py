s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)
print(type(info))

harry = set({"New Set", False, 5.9, 19})
print(type(harry))
print(harry)

for value in info:
    print(value)

info = {"Carla ", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
