# Task One
# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'

"file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67)


# Task Two
# Using your results from Task One, repeat the exercise, but this time using an 
# alternate type of format string (hint: think about alternative ways to use 
# .format() (keywords anyone?), and also consider f-strings if you’ve not used 
# them already).

my_str = "file_{first:0>3d} :   {second:.2f}, {third:.2e}, {fourth:.2e}"
my_str.format(first=2, second=123.4567, third=10000, fourth=12345.67)


# Task Three
# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# to take an arbitrary number of values.

def formatter(*t):
    pass


# Here are some tests.

if __name__ == "__main__":
    assert my_str.format(first=2, second=123.4567, third=10000, fourth=12345.67) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert "file_{:0>3d} :   {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'