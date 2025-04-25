# square.py
# Description:
#   This script prints the square of all numbers from 0 to 19.
#   It uses a function named sq() to do the squaring.
# Command line arguments:
#   None
# Example invocation:
#   python square.py
 
def sq(x):
        return x * x

i = 0
while i < 20:
    result = sq(i)
    print("The square of " + str(i) + " is " + str(result))
    i = i + 1
