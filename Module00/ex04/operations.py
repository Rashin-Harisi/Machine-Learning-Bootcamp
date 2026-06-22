#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("Usage: python operation.py <number1> <number2>")
    print("Example:")
    print("\tpython operation.py 10 3")
    sys.exit()
if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    sys.exit(1)

try:
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])
except ValueError:
    print("AssertionError: only integers")
    sys.exit(1)

if number2 == 0:
    print("Sum:\t\t", number1 + number2)
    print("Difference:\t", number1 - number2)
    print("Product:\t", number1 * number2)
    print("Quotient:\t ERROR (division by zero)")
    print("Remainder:\t ERROR (module by zero)")
else:
    print("Sum:\t\t", number1 + number2)
    print("Difference:\t", number1 - number2)
    print("Product:\t", number1 * number2)
    print("Quotient:\t", number1 / number2)
    print("Remainder:\t", number1 % number2)

