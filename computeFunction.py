# computeFunction.py
# Description:
#   This script computes the values of the function f(x) = x^2 + 2
#   for x values from 0 to 9, and prints each x with its corresponding f(x).
# Command line arguments:
#   None
# Example invocation:
#   python computeFunction.py

def compute_f(x):
        return x * x + 2

x = 0
while x < 10:
        fx = compute_f(x)
        print("x = " + str(x) + ", f(x) = " + str(fx))
        x = x + 1
