#!/usr/bin/env python3
import string
import sys

def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if text is None:
        print("What is the text to analyze?")
        text = input(">> ")
    if not isinstance(text,str):
        print("AssertionError: argument is not a string")
        return
    printable = sum(1 for c in text if c.isprintable())
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    space = sum(1 for c in text if c.isspace())
    punctuation = sum(1 for c in text if c in string.punctuation)
    print(f"The text contains {printable} printable character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {space} space(s)")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit()
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("AssertionError: more than one argument is provided")
