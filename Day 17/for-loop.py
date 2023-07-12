name = 'Abhishek'
for i in name:
    print(i)
    if (i == "b"):
        print("This is something special!")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(colors)
    for i in color:
        print(i, end=" ")

for k in range(5):
    print(k + 1)

# using * symbol prints the list
# elements in a single line
print(*colors)
# for k in range(1, 20001):
#   print(k)

#  range(start, stop[, step])
for k in range(1, 12, 2):
    print(k)

num = input("Enter an number to see the table ")
for i in range(10):
    print(num, ' x ', i+1, ' = ', int(num)*(i+1))
