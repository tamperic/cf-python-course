# Import pickle to work with binary files (for saving/loading Python objects)
import pickle

# Function to display recipe with all its attributes
def display_recipe(recipe):
    print("Recipe:", recipe['Name'])
    print("Cooking Time (min):", recipe['Cooking Time'])
    print("Ingredients:", ", ".join(i.strip() for i in recipe['Ingredients']))
    print("Difficulty level:", recipe['Difficulty'])

# Function to search for an ingredient in the given data
def search_ingredient(data):
    all_ingredients = data['all_ingredients']
    print("Ingredients Available Across All Recipes:")
    for index, ingredient in enumerate(all_ingredients, 1):
        print(index, ":", ingredient.strip())

    try:
        choose_number = int(input("Enter a number of the ingredient you want to search for: "))
        ingredient_searched = all_ingredients[choose_number - 1].strip()
    except:
        print("Invalid input. Please enter a valid number from the list of ingredients.")
    else:
        found = False
        recipes_list = data['recipes_list']
        for recipe in recipes_list:
            if ingredient_searched in [i.strip() for i in recipe['Ingredients']]:
                display_recipe(recipe)
                found = True
        if not found:
            print("There are no recipes with that ingredient.")

# Ask user for the file name where recipes are stored
filename = input("Enter the filename where you've stored your recipes: ")

# Try to open the file and load existing recipes
try:
    with open(filename, 'rb') as my_file:
        data = pickle.load(my_file)
except FileNotFoundError:
    print("This file does not exist!")
else:
    search_ingredient(data)
