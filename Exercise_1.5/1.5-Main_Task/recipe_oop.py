class Recipe(object):
    # Class variable to store all ingredients from all recipes
    all_ingredients = []

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = None
        self.calculate_difficulty()
        self.update_all_ingredients()

   # Getter methods for 'name' and 'cooking_time'
    def get_name(self):
        return self.name
    def get_cooking_time(self):
        return self.cooking_time 
    
    # Setter methods for 'name' and 'cooking_time'
    def set_name(self, name):
        self.name = name
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        # self.calculate_difficulty()

    def add_ingredients(self, ingredients):
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
        self.update_all_ingredients()

    # Getter method for 'ingredients' that returns the list itself
    def get_ingredients(self):
        return self.ingredients
    
    #Function to calculate the difficulty of the recipe base on cooking time and number of ingredients
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"

        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"

        elif self.cooking_time >= 10 and num_ingredients < 4:    
            self.difficulty = "Intermediate"

        elif self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = "Hard"
        # return self.difficulty
    
    # Getter method for 'difficulty' to call 'calculate_difficulty()' if 'difficulty' hasn't been calculated
    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    # Method to search for an ingredient in the given data
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    # String representation that prints entire recipe
    def __str__(self):
        output = "\nRecipe: " + self.name + "\nCooking Time: " + str(self.cooking_time) + "\nIgredients: " + ", ".join(self.ingredients) + "\nDifficulty: " + self.difficulty + "\n"
        return output
    
    # Method to find recipes that contain a specific ingredient
    def recipe_search(data, search_term):
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)

# Make objects under 'Recipe' class with 'name', 'ingredients', and 'cooking_time' attributes
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
caffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)

# Wrap recipes into list 'recipe_list'
recipe_list = [tea, caffee, cake, banana_smoothie]

# Search recipes containing certain ingredients
print("Search recipes that contain 'Water' as ingredient: ")
Recipe.recipe_search(recipe_list, "Water")

print("Search recipes that contain 'Sugar' as ingredient: ")
Recipe.recipe_search(recipe_list, "Sugar")

print("Search recipes that contain 'Bananas' as ingredient: ")
Recipe.recipe_search(recipe_list, "Bananas")