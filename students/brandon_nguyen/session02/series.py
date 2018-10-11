#!/usr/bin/env python3
def fibonacci(n):
    """
    The function have one parameter n which represents the index.
    The function returns the nth's value of the index n in fibonacci series (starting with zero indiex).
    0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    if (n==0 or n==1): 
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

