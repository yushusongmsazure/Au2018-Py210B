def grid_fcnt(x,y):

    plus = "+" + "-"*x + "+" + "-"*x + "+"
    pipe = "|" + " "*x + "|" + " "*x + "|"

    for i in range(y*2 + 3):
        if i%(y + 1)==0:
            print(plus)
        else:
            print(pipe)

grid_fcnt(5,3)