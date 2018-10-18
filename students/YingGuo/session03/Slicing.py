"""Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order."""

def sequence_1(sequence):
    """first and last items exchanged"""
    first = sequence[0]
    sequence[0] = sequence[-1]
    sequence[-1] = first

    return sequence

def sequence_2(sequence):
    """every other item removed"""
    sequence = sequence[::2]

    return sequence

def sequence_3(sequence):
    """with the first 4 and the last 4 items removed, and then every other item in the remaining sequence"""
    sequence = sequence[4:-5:2]

    return sequence

def sequence_4(sequence):
    """the elements reversed???"""


    
def sequence_5(sequence):
    """the last third, then first third, then the middle third in the new order???"""