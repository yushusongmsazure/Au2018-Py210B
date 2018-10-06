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



if __name__ == "__main__":
    basicprintgrid()
    print()
    print_grid(4)
