"""
Tim Meese
Au2018-Py210B
Print Grid Exercise
"""
def do_print_grid(self, row, col):
    pass

def main(row, col):
    print("Entering main")
    try:
        do_print_grid(row, col)
    except:
        print("got Name Error exception")

if __name__ == "__main__":
    main()