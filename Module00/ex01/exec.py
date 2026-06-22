#!/usr/bin/env python3
import sys
#sys.argv or sys.envp

tmp = " ".join(sys.argv[1:]);
text = tmp[::-1]

for c in text:
    if c.isupper():
        print(c.lower(), end="")
    elif c.islower():
        print(c.upper(), end ="")
    else:
        print(c, end="")
