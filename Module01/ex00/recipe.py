#!/usr/bin/env python3


class Recipe:
    def __init__(self,
                 name : str,
                 cooking_lvl : int,
                 cooking_time : int,
                 ingredients : list,
                 description : str,
                 recipe_type : str):
        valid_types= ("starter", "lunch", "dessert")

        if not isinstance(name , str):
            raise TypeError("Name should be a string.")
        if not name:
            raise ValueError("Name cannot be empty.")
        if not isinstance(cooking_lvl, int):
            raise TypeError("Cooking_lvl should be integer.")
        if not 1 <= cooking_lvl <= 5:
            raise ValueError("Cooking_lvl must be in range of 1 to 5")
        if not isinstance(cooking_time, int):
            raise TypeError("Cooking_time should be an interger.")
        if not cooking_time > 0:
            raise ValueError("Cooking_time must be a positive number")
        if not isinstance(ingredients, list):
            raise TypeError("Ingredients should be a list.")
        for item in ingredients:
            if not isinstance(item, str):
                raise TypeError("All ingredients should be strings.")
        if not isinstance(description, str):
            raise TypeError("Description should be a string.")
        if not isinstance(recipe_type, str):
            raise TypeError("Recipe type should be a string")
        if not recipe_type in valid_types:
            raise ValueError("Type can be one of 'starter', 'lunch', 'dessert'.")
        
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        """Returns the string to print with the recipe's info"""
        return (
            f"Recipe name : {self.name}\n"
            f"Cooking level: {self.cooking_lvl}\n"
            f"Cooking time : {self.cooking_time}\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Description: {self.description}\n"
            f"Type: {self.recipe_type}\n"
        )


"""
tourte = Recipe(
    "Tourte",
    2,
    30,
    ["flour", "eggs", "fruits"],
    "A tourte is a broad term for a traditional French double-crust pie. And its ingredients vary wildly depending on the region.",
    "dessert"
)
to_print = str(tourte)
print(to_print)
"""   