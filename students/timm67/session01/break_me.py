"""
Tim Meese
Au2018-Py210B
Python Pushup: Exploring errors
"""
def throwNameError():
    giraffe

def throwTypeError():
    2 + [1,2]

def throwSyntaxError():
    import foo

def throwAttributeError():
    a = [1,2]
    a.zzz
    
def main():
    print("Entering main")
    try:
        throwNameError()
    except:
        print("got Name Error exception")

    try:
        throwTypeError()
    except:
        print("got Type Error exception")

    try:
        throwSyntaxError()
    except:
        print("got Syntax Error exception")

    try:
        throwAttributeError()
    except:
        print("got Attribute Error exception")

    print("All done")

if __name__ == "__main__":
    main()