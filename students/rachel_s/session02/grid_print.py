def grid_print(grid_size, cell_size):
    if grid_size < 1 or cell_size < 1:
        print("Please make grid and cell sizes 1 or greater.")
    else:
        for a in range(grid_size):
            grid_edge(grid_size, cell_size)
            for b in range(cell_size):
                grid_inside(grid_size, cell_size)
        grid_edge(grid_size, cell_size)


def grid_edge(grid_size, cell_size):
    for a in range(grid_size):
        print("+", end=" ")
        for i in range(cell_size):
            print("-", end=" ")
    print("+")

def grid_inside(grid_size, cell_size):
    for a in range(grid_size):
        print("|", end=" ")
        for i in range(cell_size):
            print(" ", end=" ")
    print("|")