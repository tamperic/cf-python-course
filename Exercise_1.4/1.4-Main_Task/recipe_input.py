# Import pickle to work with binary files (for saving/loading Python objects)
import pickle

# Function to take recipes from user input
def take_recipe():
    # Ask for recipe name, cooking time, and ingredients
    name = str(input("Enter a name of recipe: "))
    cooking_time = int(input("Enter a cooking time (in minutes): "))
    ingredients = list(input("Enter ingredients: ").split(",")) # Stored as a list
    
    # Count the number of ingredients
    numberOfIngredients = len(ingredients)
    difficulty = calc_difficulty(cooking_time, numberOfIngredients)

    # Gather all attributes into a dictionary
    recipe = {
        'Name': name, 
        'Cooking Time': cooking_time, 
        'Ingredients': ingredients,
        'Difficulty': difficulty
    }

    return recipe

#Function to calculate the difficulty of the recipe base on cooking time and number of ingredients
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and ingredients < 4:
        difficulty = "Easy"

    elif cooking_time < 10 and ingredients >= 4:
        difficulty = "Medium"

    elif cooking_time >= 10 and ingredients < 4:    
        difficulty = "Intermediate"

    elif cooking_time >= 10 and ingredients >= 4:
        difficulty = "Hard"

    return difficulty

# Ask user for the file name where recipes are stored
filename = input("Enter the filename where you've stored your recipes:")

# Try to open the file and load existing recipes
try:
    with open(filename, 'rb') as my_file:
        data = pickle.load(my_file)
except FileNotFoundError:
    print("This file does not exist! Need to create a new one.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
except:
    print("An unexpected error occured.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
else:
    my_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

# Ask user how many recipes they want to enter
n = int(input("How many recipes do you like to enter? "))

# Loop calling 'take_recipe()' function, append the output of this function into 'recipes_list'
for i in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)

    # Loop going through recipe's ingredients and adding them to 'all_ingredients' if they are not already there
    for ingredient in recipe['Ingredients']:
        ingredient = ingredient.strip()   # Remove spaces
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)


# Gather the updated 'recipes_list' and 'all_ingredients' into the 'data' dictionary
data = {
        'recipes_list': recipes_list,
        'all_ingredients': all_ingredients
    }

# Save updated data abck to the binary file
with open(filename, 'wb') as my_file:
    pickle.dump(data, my_file)
