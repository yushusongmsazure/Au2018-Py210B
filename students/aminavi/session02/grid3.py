def grid(x,y):
    for i in range(y*2 + 3):
        if i%(y + 1)==0:
            print("+" + "-"*x + "+" + "-"*x + "+")
        else:
            print("|" + " "*x + "|" + " "*x + "|")
grid(1,1)