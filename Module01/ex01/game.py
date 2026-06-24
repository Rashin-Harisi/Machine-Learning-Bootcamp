#!/usr/bin/env python3

#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:


class GotCharacter:
    def __init__(self,
                 first_name,
                 is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name= None, is_alive = True):
        super().__init__(first_name = first_name, is_alive = is_alive)
        self.family_name = self.__class__.__name__
        self.house_word = "Winter is Coming"

    def print_house_words(self):
        return (print(self.house_word))
    
    def die(self):
        self.is_alive = False

        
"""
You can add attributes and methods after defining the class:
class Sample:
    pass(when you do not have anything in the class put 'pass' keyword)

def hello(self):
    print("hello")

Sample.hello = hello()
Sample.author = "Rashin"

even you can add them to an instace of the class
"""