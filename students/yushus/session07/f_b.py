f,b="Fizz","Buzz"
for i in range(1,101):
    if i%3==0 and i%5==0:print(f+b)
    elif i%3==0:print(f)
    elif i%5==0:print(b)
    else:print(i)
