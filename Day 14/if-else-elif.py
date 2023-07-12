# a = int(input("Enter your age: "))
# print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# if(a>=18):
#   print("You can drive")
#   print("Yes")
# else:
#   print("You cannot drive")
#   print("No")
#   print("Yay!")

# ElIF
# num = int(input("Enter the value of num: "))
# if (num < 0):
#   print("Number is negative.")
# elif (num == 0):
#   print("Number is Zero.")
# elif (num == 999):
#   print("Number is Special.")
# else:
#   print("Number is positive.")

# print("I am happy now")

# end ELIF

# Nested if-else-elif
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")