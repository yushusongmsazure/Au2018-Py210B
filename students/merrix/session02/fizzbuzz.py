for i in range(101):
    if (i % 3) == 0: 
        print( i, "Fizz")
    if (i % 5) == 0:
        print(i, "Buzz")
    if (i % 3 == 0 and i % 5 == 0):
        print(i,"FizzBuzz")