def calculate_gmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def is_greater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def is_lesser(a, b):
  pass
# if we define function later then we used pass
  

a = 9
b = 8
is_greater(a, b)
calculate_gmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
is_greater(c, d)
calculate_gmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
