""" 
    Find e to the Nth Digit 
    Enter a number and have the program generate e up to that many decimal places
    Keep a limit as to how far it will go!
"""

import math

def generate_e(n):
    """
        Return Euler's number to n places
    """

    return "%.*f" % (n, math.e)

x = int(input("Please enter the value of n: "))

if x > 50:
    x = 50
    print("Will not calculate beyond 50 points of precision, clamping...")

print(generate_e(x))