#Fizz Buzz Exercise for Lesson 2

for x in range(100):
    x += 1 #changes range 0-99 to 1-100
    if not(x%3) and not(x%5):
        print('FizzBuzz')
    elif not(x%3):
        print('Fizz')
    elif not(x%5):
        print('Buzz')
    else:
        print(x)
