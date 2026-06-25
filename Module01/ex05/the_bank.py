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
    def __init__(self):
        self.accounts = []
    
    @staticmethod
    def iscorrupted(data: Account):
        if len(data.__dict__) % 2 == 0:
            return True
        for att in data.__dict__:
            if att[0] == 'b':
                return True
        if 'name' not in data.__dict__:
            return True
        if 'id' not in data.__dict__:
            return True
        if 'value' not in data.__dict__:
            return True
        for att in data.__dict__:
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
        if not isinstance(data, Account):
            return False
        for account in self.accounts:
            if account.name == data.name:
                return False
            else:
                self.accounts.append(data)
                return True
    def get_account(self, name: str):
        for account in self.accounts:
            if account.name == name:
                return account
        return None
    
    def transfer(self, origin:str, dest:str, amount:float):
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, float):
            return False
        if origin == dest :
            return True
        origin_account = self.get_account(origin)
        dest_account = self.get_account(dest)
        if amount < 0 or amount > origin_account.value:
            return False
        if not self.iscorrupted(origin_account) and not self.iscorrupted(dest_account):
            origin_account.value -= amount
            dest_account.value += amount
            return True
        else:
            return False
    
    def fix_accout(self, name: str):