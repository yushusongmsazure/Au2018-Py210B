# Name error
10 + something*5
# Type Error
20 + '20'
# Syntax error
while True: print('hello')
# Attribute Error
class Foo:
    def __init__(self):
        self.a = 1

f = Foo()
print(f.a)
print(f.b)
