#!/usr/bin/env python3
import random

def shuffle(words: list):
    new_list = []
    used_indexes= []
    while len(used_indexes) < len(words):
        i = random.randint(0,len(words)-1)
        if i in used_indexes:
            continue
        else:
            used_indexes.append(i)
            new_list.append(words[i])
    return new_list

def unique(words: list):
    new_list = []
    for i in range(len(words)):
        if words[i] in new_list:
            continue
        else:
            new_list.append(words[i])
    return new_list

def ordered(words: list):
    return sorted(words)

def generator(text: str, sep : str = ' ', option : str= None ):
    """
    Splits the text according to sep value and yields the substrings.
    """
    if not isinstance(text, str) or not isinstance(sep, str):
        yield "ERROR"
        return 
    for c in text:
        if not c.isprintable():
            yield "ERROR"
            return 
    words = text.split(sep)
    if option == "shuffle":
        new_list = shuffle(words)
    elif option == "unique":
        new_list= unique(words)
    elif option == "ordered":
        new_list= ordered(words)
    elif option == None:
        new_list = words
    else :
        yield "ERROR"
        return 
    for word in new_list:
        yield word

