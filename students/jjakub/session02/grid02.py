def grid_fcnt(x):
    plus = "+" + "-"*x + "+" + "-"*x + "+"
    pipe = "|" + " "*x + "|" + " "*x + "|"

    for i in range(x*2 + 3):
        if i%(x + 1)==0:
            print(plus)
        else:
            print(pipe)

grid_fcnt(3)