#!/usr/bin/env python3
import sys
#sys.argv or sys.envp


## check the length of arguments
tmp = " ".join(sys.argv[1:]);
text = tmp[::-1]
#swapcase() function for string
#help(str) you can see all functions and methods
for c in text:
    if c.isupper():
        print(c.lower(), end="")
    elif c.islower():
        print(c.upper(), end ="")
    else:
        print(c, end="")
