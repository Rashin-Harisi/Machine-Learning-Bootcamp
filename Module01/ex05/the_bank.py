#!/usr/bin/env python3

# **kwargs=> **(collect all extra named arguments into a dictionary) 
#            kwargs(keyword arguments) 
#            you don't know in advance which extra information the user will pass.
#            Every Python object stores its attributes inside a dictionary called: self.__dict__
# class attributes vs. instance attributes => there is only one copy of class attributes, shared by all Account.
# The dir() function is a built-in Python tool used to list the attributes (like methods, variables, etc.) of an object.

import random

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
        attrs = data.__dict__

        if len(attrs) % 2 == 0:
            return True
        if any(attr.startswith("b") for attr in attrs):
            return True
        if ('name' not in attrs
            or "id" not in attrs
            or "value" not in attrs):
            return True
        if not any(attr.startswith(("zip", "addr")) for attr in attrs):
            return True
        if not isinstance(data.name, str):
            return True
        if not isinstance(data.id, int):
            return True
        if not isinstance(data.value, (int, float)):
            return True
        return False 
    

    def get_account(self, name: str):
        for account in self.accounts:
            if account.name == name:
                return account
        return None
    
    def add(self, data: Account):
        if not isinstance(data, Account):
            return False
        if self.get_account(data.name) is not None:
            return False
        self.accounts.append(data)
        return True
    
    def transfer(self, origin:str, dest:str, amount:float):
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, float):
            return False
        
        if amount < 0 :
            return False
        
        origin_account = self.get_account(origin)
        dest_account = self.get_account(dest)
        if origin_account is None or dest_account is None:
            return False
        if self.iscorrupted(origin_account) or self.iscorrupted(dest_account):
            return False
        
        if  amount > origin_account.value:
            return False
        
        if origin == dest :
            return True
        
        origin_account.value -= amount
        dest_account.value += amount
        return True
     
    def fix_account(self, name: str):
        if not isinstance(name, str):
            return False
        account = self.get_account(name)
        if account is None: 
            return False

        attrs = account.__dict__
        for attr in list(attrs):
            if attr.startswith("b"):
                delattr(account, attr)
        if not any(attr.startswith(("zip", "addr")) for attr in attrs):
            account.zip = ""
        if "name" not in attrs or not isinstance(account.name , str):
            account.name = name
        if "id" not in attrs or not isinstance(account.id, int):
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if "value" not in attrs or not isinstance(account.value, (int,float)):
            account.value = 0
        if len(attrs) % 2 == 0:
             account.fix = True
        return not self.iscorrupted(account)


        