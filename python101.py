for i in range(1, 21):
    if i % 2 != 0:
        print(i, "is a Odd Number")


def FizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "is FizzBuzz")
        elif i % 3 == 0:
            print(i, "is Fizz")
        elif i % 5 == 0:
            print(i, "is Buzz")
        else:
            print(i)
FizzBuzz(15)