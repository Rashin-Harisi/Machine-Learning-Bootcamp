#!/usr/bin/env python3

from book import Book
from recipe import Recipe
import time

book = Book("My Cookbook")
time.sleep(1)
cake = Recipe(
    "Cake",
    3,
    60,
    ["flour", "sugar", "eggs"],
    "A simple cake",
    "dessert"
)

salad = Recipe(
    "Salad",
    1,
    15,
    ["avocado", "arugula", "tomatoes", "spinach"],
    "A fresh salad",
    "starter"
)

print("---- Add recipes ----")
book.add_recipe(cake)
book.add_recipe(salad)

print("---- Get recipe by name ----")
found = book.get_recipe_by_name("Cake")
print(found.name)

print("---- Get recipes by type ----")
print(book.get_recipes_by_types("dessert"))
print(book.get_recipes_by_types("starter"))

print("---- Dates ----")
print(book.creation_date)
print(book.last_update)

print("---- Invalid recipe test ----")
try:
    book.add_recipe("not a recipe")
except TypeError as error:
    print(error)