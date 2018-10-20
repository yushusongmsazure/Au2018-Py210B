#!/usr/bin/env python3
# Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    series =  []
    while (b < 20):
        series.append(b)
        a, b = b, a+b
        return(series[n])
fibonacci(2)


# Lucas Series
# def lucas():



# Sum Series
# def sum_series():