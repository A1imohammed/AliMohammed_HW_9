# cube.py
# Description:
#   This script prints the cube of odd numbers from 0 to 19,
#   and prints even numbers as they are.
#   A function named cb() is used to cube the odd numbers.
# Command line arguments:
#   None
# Example invocation:
#   python cube.py
 
def cb(x):
    return x * x * x

i = 0
while i < 20:
    if i % 2 == 0:
        print(i)
    else:
        result = cb(i)
        print(result)
    i = i + 1
