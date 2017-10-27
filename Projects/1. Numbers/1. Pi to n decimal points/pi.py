import math

x = int(input("Please enter the number of decimal points you would like to round pi to. "))

if x > 50:
    x = 50
    print_r("Will not round past 50 digits, limiting.")

print(format(math.pi, ".%dg" % x))