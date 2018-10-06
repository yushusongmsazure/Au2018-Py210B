def basicprintgrid():
    print("+" + "----" + "+" + "----" + "+")
    for i in range(4):
        print("|" + "    " + "|" + "    " + "|")
    print("+" + "----" + "+" + "----" + "+")
    for i in range(4):
        print("|" + "    " + "|" + "    " + "|")
    print("+" + "----" + "+" + "----" + "+")    

def print_grid(n):
    print("+" + n * "-" + "+" + n * "-" + "+")
    for i in range(n):
        print("|" + n * " " + "|" + n* " " + "|")
    print("+" + n * "-" + "+" + n * "-" + "+")
    for i in range(n):
        print("|" + n * " " + "|" + n * " " + "|")
    print("+" + n * "-" + "+" + n * "-" + "+")

def print_grid2(x , y):

    for i in range(x):
        
        #First line print
        print(end="+")
        for i in range(x):
            print(y * "-", end="+")
        print()

        #body print
        for i in range(y):
            print(end="|")
            for i in range(x):
                print(+ y * " ", end="|")
            print()
    
    #last line print
    print(end="+")
    for i in range(x):
        print(y * "-", end="+")



if __name__ == "__main__":
    basicprintgrid()
    print()
    print_grid(4)
    print()
    print_grid2(6,6)
