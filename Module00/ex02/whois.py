#!/usr/bin/env python3

import sys

length = len(sys.argv)
if length == 1:
    sys.exit()

if length > 2:
    print("AssertationError: more than one argument is provided")
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("AssertationError: argument is not an integer")
    sys.exit(1)

if number == 0:
    print("I'm Zero.")
elif number % 2 == 0:
    print("I'm  Even.")
else:
    print("I'm Odd.")

    
