#!/usr/bin/env python3

# **kwargs=> **(collect all extra named arguments into a dictionary) 
#            kwargs(keyword arguments) 
#            you don't know in advance which extra information the user will pass.
#            Every Python object stores its attributes inside a dictionary called: self.__dict__
# class attributes vs. instance attributes => there is only one copy of class attributes, shared by all Account.
# The dir() function is a built-in Python tool used to list the attributes (like methods, variables, etc.) of an object.
class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount



class Bank():
    def __init__(self, data):
        if not isinstance(data, Account):
            raise TypeError("Data must be type of Account class")
        self.accounts = []
    
    @staticmethod
    def iscorrupted(data: Account):
        if len(data.__dict__) % 2 == 0:
            return True
        for att in data.__dict__.dir():
            if att[0] == 'b':
                return True
        if not 'name'and 'id'and'value' in data.__dict__.dir():
            return True
        for att in data.__dict__.dir():
            if att.startswith("zip") or att.startswith("addr"):
                return False
            return True
        if not isinstance(data.name, str):
            return True
        if not isinstance(data.id, int):
            return True
        if not isinstance(data.value, (int, float)):
            return True
        return False 
    

    def add(self, data: Account):
        if self.iscorrupted(data):
            return False
        for account in self.accounts:
            if account.name == data.name:
                return False
            else:
                self.accounts.append(data)
                return True
    
    def transfer(self, origin:str, dest:str, amount:float):
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, float):
            return False
        if origin == dest :
            return True
        if amount < 0 or amount > self.accounts[origin].balance:
            return False
        if not self.iscorrupted(self.accounts[origin]) and not self.iscorrupted(self.accounts[dest]):
            self.accounts[origin].value -= amount
            self.accounts[dest].value += amount
            return True
        else:
            return False
    
    def fix_accout(self, name: str):