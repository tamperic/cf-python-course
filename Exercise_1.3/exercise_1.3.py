recipes_list = []
ingredients_list = []

def take_recipe():
    name = str(input("Enter a name of recipe: "))
    cooking_time = int(input("Enter a cooking time (in minutes): "))
    ingredients = list(input("Enter ingredients: ").split(","))
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}

    return recipe

n = int(input("How many recipes do you like to enter?"))

for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)

for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    ingredients = len(recipe['ingredients'])

    if cooking_time < 10 and ingredients < 4:
        recipe['difficulty'] = "Easy"

    elif cooking_time < 10 and ingredients >= 4:
        recipe['difficulty'] = "Medium"

    elif cooking_time >= 10 and ingredients < 4:
        recipe['difficulty'] = "Intermediate"

    elif cooking_time >= 10 and ingredients >= 4:
        recipe['difficulty'] = "Hard"

    print("Recipe: ", recipe['name'])
    print("Cooking Time (min): ", cooking_time)
    print("Ingredients: ")
    for ingredient in recipe['ingredients']:
        if not ingredient in recipe['ingredients']:
            print(ingredient)
        else:
            print("\033[3m(no ingredients entered)\033[0m")
    print("Difficulty level: ", recipe['difficulty'])

ingredients_list = [i for i in ingredients_list if i.strip()]
ingredients_list.sort()

if not ingredients_list:
    print("Ingredients Available Across All Recipes: ")
    print("\033[3m(there are no ingredients available, the list is empty)\033[0m")
else: 
    print("Ingredients Available Across All Recipes: ")
    for ingredient in ingredients_list: 
        print(ingredient)

