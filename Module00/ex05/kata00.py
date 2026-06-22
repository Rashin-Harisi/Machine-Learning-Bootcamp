#!/usr/bin/env python3

#Difference between tuple and list: the value of tuple elements can not be changed
kata = (19,42,21)
i = 0

print("The 3 numbers are: ", end="")
for c in kata:
    print(c, end="")
    if i != len(kata) - 1:
        print(", ", end="")
    i += 1
print()