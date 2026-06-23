#!/usr/bin/env python3
import sys
import string

if len(sys.argv) != 3:
    print("Error")
    sys.exit(1)

S = sys.argv[1]
try:
    N = int(sys.argv[2])
except ValueError:
    print("Error")
    sys.exit(1)

for c in string.punctuation:
    S = S.replace(c, "")
s_list = S.split(" ")
new_list = [word for word in s_list if len(word) > N]

print(new_list)
