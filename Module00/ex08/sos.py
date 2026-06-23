#!/usr/bin/env python3
import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def encrypt_morse(message):
    code = ''
    for letter in message:
        if letter != ' ':
            code += MORSE_CODE_DICT[letter] + ' '
        else:
            code += '/ '
    return code

if len(sys.argv) == 1:
    sys.exit()
list = sys.argv[1:]
for word in list :
    for c in word:
        if not c.isalnum() and not c.isspace():
            print("ERROR")
            sys.exit(1)

str = " ".join(list)
code = encrypt_morse(str.upper())
print(code)

