#!/usr/bin/env python3

kata = "The right format"

#print(f"{kata:->42}")
print(kata.rjust(42, "-"), end="")