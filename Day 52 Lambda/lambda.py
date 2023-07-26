# def double(x):
#   return x*2

def appl(fx, value):
    return 6 + fx(value)


def double(x): return x * 2
def cube(x): return x * x * x
def avg(x, y, z): return (x + y + z) / 3


print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x, 2))
