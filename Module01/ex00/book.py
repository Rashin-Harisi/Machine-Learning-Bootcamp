#!/usr/bin/env python3
from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self,
                name : str):
            if not isinstance(name , str):
                 raise TypeError("Name must be a string.")
            if not name:
                 raise ValueError("Name should not be empty.")
            self.name = name
            self.last_update: datetime = datetime.now()
            self.creation_date: datetime= datetime.now()
            self.recipes_list:dict ={
                  "starter" : [],
                  "lunch": [],
                  "dessert":[]
            }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for type in self.recipes_list:
             for recipe in self.recipes_list[type]:
                  if recipe.name == name:
                       print(recipe)
                       return (recipe)
        return None
                  
    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        for type in self.recipes_list:
             if type == recipe_type:
                  for recipe in self.recipes_list[recipe_type]:
                       return(recipe.name)
        return None
    
    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if not isinstance(recipe, Recipe):
                raise TypeError("recipe must be a Recipe object")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
