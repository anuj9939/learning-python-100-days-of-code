def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed")
    # print("I am always executed")


x = func1()
print(x)

# Day 38 generate own error


def CustomError():
    a = int(input("Enter any value between 5 and 9"))
    try:
        if (a < 5 or a > 9):
            raise ValueError("Value should be between 5 and 9")
    except Exception as e:
        print(e)


CustomError()
