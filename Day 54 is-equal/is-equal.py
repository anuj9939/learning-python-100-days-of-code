a = None
b = None

print(a is b)  # exact location of object in memory
print(a is None)  # exact location of object in memory
print(a == b)  # value

a = "Anuj"
b = "Anuj"
print(a is b)  # exact location of object in memory
print(a == b)  # exact location of object in memory

# list is mutable data type
a = [1, 2, 3]
b = [1, 2, 3]
print("List- ", a is b)  # exact location of object in memory
print("List- ", a == b)  # exact location of object in memory
