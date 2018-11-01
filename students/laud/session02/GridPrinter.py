#!/usr/bin/env python3

# Part 1 & Part 2 (one parameter)
def print_grid(n):
    line = ''
    bars = ''
    cell_size = n+1
    cell_height = (n-1)//2

    # Create an array of breakpoints
    breakpoints = []
    for i in range(0, cell_size*2):
        breakpoints.append(cell_size*i)

    # Create horizontal border
    for place in range(0, (n+2)*2):
        if place in breakpoints:
            line += '+'
        elif (place % 2 == 0):    
            line += '-'
        else:
            line += ' '

    # Create vertical border
    for place in range(0, (n+2)*2):
        if place in breakpoints:
                bars += '|'
        else:
            bars += ' '

    # Combine the above to create grid
    for i in range(2):
        print(line)
        for i in range(cell_height):
            print(bars)
    print(line)
print_grid(15)





# Part 3 (2 parameters)
def print_grid_complex(n,s):
    line = ''
    bars = ''
    cell_size = (s*2) + 2
    line_length = (n*cell_size) + 1

    # Create an array of breakpoints
    breakpoints = []
    for i in range(0, cell_size*n):
        breakpoints.append(cell_size*i)

    # Create horizontal border
    for place in range(0, line_length):
        if place in breakpoints:
            line += '+'
        elif (place not in breakpoints) and (place % 2 == 0):    
            line += '-'
        else:
            line += ' '

    # Create vertical border
    for place in range(0, line_length):
        if place in breakpoints:
                bars += '|'
        else:
            bars += ' '

    # Combine the above to create grid
    for i in range(n):
        print(line)
        for i in range(s):
            print(bars)
    print(line)
print_grid_complex(5,3)