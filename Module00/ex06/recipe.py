#!/usr/bin/env python3
import sys

cookbook={
    "sandwich" : {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10
    },
    "cake" : {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : 60
    },
    "salad" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : 15
    }
}

def print_recipe_names():
    for key in cookbook:
        print(key)

def print_details(name):
    if name not in cookbook:
        print("Recipe not found.")
        return
    recipe = cookbook[name]
    print(f"Recipe for {name}: ")
    print(f'\tIngredients list: {recipe["ingredients"]}')
    print(f'\tTo be eaten for {recipe["meal"]}.')
    print(f'\tTakes {recipe["prep_time"]} minutes of cooking.')
    
            

def del_recipe(name):
    if name not in cookbook:
            print("Recipe not found.")
            return
    del cookbook[name]
    print(f"{name} deleted.")
    
            

def add_new_recipe():
    print("Enter a name:")
    name = input()
    print("Enter ingredients:")
    ingreidents=[]
    while True:
        item = input()
        if item == "":
            break
        ingreidents.append(item)
    print("Enter a meal type:")
    meal = input()
    print("Enter a preparation time:")
    try:
        prep = int(input())
    except ValueError:
        print("It should be intiger only.\n")
        return

    cookbook[name]={
        "ingredients" : ingreidents,
        "meal" : meal,
        "prep_time" : prep
    }

while True:
    print("Welcome to the python Cookbook !")
    print("List of available options:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: print the cookbook")
    print("\t5: Quit")
    print()
    print("Please select an option:")
    try:
        option = int(input(">> "))
    except ValueError:
        print("Sorry, this option does not exist.\n")
        continue

    if option == 1:
        add_new_recipe()
        print()
    elif option == 2:
        print("please enter a recipe name to delete it:")
        name = input(">> ")
        del_recipe(name)
        print()
    elif option == 3:
        print("Please enter a recipe name to get its details:")
        name = input(">> ")
        print_details(name)
        print()
    elif option == 4:
        print_recipe_names()
        print()
    elif option == 5:
        print("Cookbook closed. Goodbye !")
        sys.exit()
    else:
        print("Sorry, this option does not exist.\n")