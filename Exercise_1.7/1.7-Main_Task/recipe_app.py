# Import packages
from sqlalchemy import create_engine, Column # Import Column type and 
from sqlalchemy.types import Integer, String # Import the Integer and String types
from sqlalchemy.ext.declarative import declarative_base # Import declarative base 
from sqlalchemy.orm import sessionmaker # Import sessionmaker() method to create session on database
import re

# Database setup
engine = create_engine("mysql://cf-python:password@localhost/task_database")
Base = declarative_base() # Generate the 'Base' class from the declarative base function
Session = sessionmaker(bind=engine) # 'Session' class connection it with 'engine' 
session = Session() # Initialize the "session" object for use in the rest of the code

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # '__repr__' method to this class to help identify your objects easily from the terminal 
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + "-" + self.difficulty + ">"
    
    # String representation that prints entire recipe
    def __str__(self):
        return(
            "\nRecipe ID: " + str(self.id) + 
            "\nRecipe Name: " + self.name + 
            "\nCooking Time: " + str(self.cooking_time) + " minutes" +
            "\nIngredients: " + ", ".join(self.return_ingredients_as_list()) + 
            "\nDifficulty: " + self.difficulty
        )

    # Function to calculate the difficulty of the recipe base on cooking time and number of ingredients
    def calculate_difficulty(self):
        numberOfIngredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and numberOfIngredients < 4:
            self.difficulty = "Easy"

        elif self.cooking_time < 10 and numberOfIngredients >= 4:
            self.difficulty = "Medium"

        elif self.cooking_time >= 10 and numberOfIngredients < 4:    
            self.difficulty = "Intermediate"

        elif self.cooking_time >= 10 and numberOfIngredients >= 4:
            self.difficulty = "Hard"

    # Method to retrieve/convert 'ingredients' string inside 'Recipe' objest as a list
    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        else:
            ingredients_list = [i.strip() for i in self.ingredients.split(",")]
            return ingredients_list

# 'create_all()' method in the base class to create tables (in db) of all the models that are defined
Base.metadata.create_all(engine)


#--------------------MAIN OPERATIONS------------------

# Definition for CREATING recipe
def create_recipe():
    print("\n-----CREATE RECIPE-----")

    try:
        # Ask for recipe name
        while True:
            name = input("Enter a name of recipe with max 50 characters (or type 'quit' to cancel): ").strip()

            if name.lower() == "quit":
                print("\nRecipe creation cancelled. Returning to main menu...")
                return  # Exit function immediately

            if len(name) > 50:
                print("Name is too long. It can contain max 50 characters.")
            elif len(name) == 0:
                print("This input field cannot be empty!")
            elif not all(char.isalpha() or char.isspace() for char in name):
                print("Please enter only letters and spaces!")
            else:
                break

        # Ask for recipe cooking time
        while True:
            cooking_time = input("Enter a cooking time in minutes (or 'quit' to cancel): ")

            if cooking_time.lower() == "quit":
                print("\nRecipe creation cancelled. Returning to main menu...")
                return  # Exit function immediately

            if not cooking_time.isnumeric():
                print("Please enter numbers only.")
            else:
                cooking_time = int(cooking_time)
                break

        # Ask for recipe ingredients
        while True:
            number_of_ingredients = input("How many ingredients would you like to enter? (or 'quit' to cancel): ").strip()
            
            if number_of_ingredients.lower() == "quit":
                print("\nRecipe creation cancelled. Returning to main menu...")
                return  # Exit function immediately
    
            if not number_of_ingredients.isnumeric() or int(number_of_ingredients) <= 0:
                print("Please enter a positive number.")
            else: 
                number_of_ingredients = int(number_of_ingredients)
                break
        
        temporary_ing_list = [] # Empty termporary ingredients list
        for i in range(number_of_ingredients):
            while True:
                ingredient = input(f"Enter ingredient {i + 1} (or 'quit' to cancel): ").strip()

                if ingredient.lower() == "quit":
                    print("\nRecipe creation cancelled. Returning to main menu...")
                    return  # Exit function immediately
                
                if len(ingredient) == 0:
                    print("Ingredients list cannot be empty. Please enter some ingredients!")
                else:
                    temporary_ing_list.append(ingredient)
                    break

            ingredients_str = ", ".join(temporary_ing_list) # Convert list into single string for MySQL

        # Create new recipe object
        recipe_entry = Recipe(
            name=name,
            cooking_time=cooking_time,
            ingredients=ingredients_str,
            difficulty=""    # Will be recalculated
        )

        # Calculate difficulty
        recipe_entry.calculate_difficulty()

        # Add recipe entries to database through the 'session' object and commit changes
        session.add(recipe_entry)
        session.commit()
        print("\nRecipe", name, "has been created successfully!")

    except KeyboardInterrupt:
        print("\nRecipe creation cancelled. Returning to main menu...")
        return None

# Definition for VIEWING all recipes
def view_all_recipes():
    all_recipes = session.query(Recipe).all()
    if all_recipes:
        print("\n-----VIEW ALL RECIPES-----")
        for recipe in all_recipes:
            print(recipe, "\n") # will use __str__
    else:
        print("There are no recipes - the list is empty. Returning to the main menu...")
        return None
    

# Definition for SEARCHING for recipes by ingredients
def search_by_ingredients():
    # 1. Check if any recipes exist on db, continue only if they exist. Otherwise, exit function
    if session.query(Recipe).count() == 0:
        print("There are no recipes - the list is empty.")
        return None
    
    # 2. Retrieve values from 'ingredients' column
    results = session.query(Recipe.ingredients).all() 

    # 3. Create empty 'set' like a list to store all ingredients without duplicates
    all_ingredients = set() 

    # 4. Loop over rows got from database
    for row in results:
        ingredients_str = row[0] # Get string from tuple, each 'row' is a tuple with one element
        ingredients_list = [ingredient.strip() for ingredient in ingredients_str.split(", ")] # Split each string by commas to get individual ingredients and strip extra spaces
        all_ingredients.update(ingredients_list) # Add all ingredients from the list into the 'set (no duplicates)
    
    # Convert set to list for indexing
    all_ingredients = list(all_ingredients) 

    # 5. Display these ingredients (with numbers next to them) to the user
    print("\nINGREDIENTS TO SEARCH FOR:")
    for index, ingredient in enumerate(all_ingredients, 1):
        print(index, ":", ingredient.strip())

    # 6. Let user enter number(s) of ingredient(s) to search for
    user_input  = input("\nEnter the numbers of the ingredients you want to search for: ").strip().split()
    
    # 7. Validate input 
    if not user_input or not all(i.isnumeric() for i in user_input):
        print("Invalid input. Please enter numbers only.")
        return None
    
    user_input = [int(i) for i in user_input]
   
    if any(number < 1 or number > len(all_ingredients) for number in user_input):
        print("Please enter a valid input!")
        return None 
    
    # 8. Initialize list of ingredients to be searched for containing ingredients as strings
    search_ingredients = [all_ingredients[number - 1].strip() for number in user_input]

    # 9. Initialize empty list containing 'like()' conditions for every ingredient to be search for
    conditions = []

    # 10. Loop through 'search_ingredients'
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))

    # 11. Retrieve all recipes from db 
    all_recipes = session.query(Recipe).filter(*conditions).all()
    
    # Display all recipes
    if not all_recipes:
        print("\nNo recipes found with those ingredients.")
        return None
    else:
        print("\nRECIPES FOUND with " + ", ".join(search_ingredients) + ":")
        for recipe in all_recipes:
            print(recipe, "\n")


# Definition for EDITING recipes
def edit_recipe():
    # 1. Check if any recipes exist on db, continue only if they exist. Otherwise, exit function
    if session.query(Recipe).count() == 0:
        print("There are no recipes - the list is empty.")
        return None

    # 2. Retrieve 'id' and 'name' for each recipe
    results = session.query(Recipe.id, Recipe.name).all()

    # 3. Display recipes from each item in 'results'
    print("\nAVAILABLE RECIPES:")
    for recipe_id, recipe_name in results:
        print("ID:", recipe_id, " - Name:", recipe_name)

    # 4. User picks a recipe by 'id' 
    choose_recipeID = input("\nEnter the ID of the recipe you want to update (or type 'quit' to cancel): ").strip().lower()

    if choose_recipeID == 'quit':
        print("Updating canceled. Returning to the main menu.")
        return
    
    # Validate as integer
    try:
        choose_recipeID = int(choose_recipeID) # Convert to int if not quit
    except ValueError:
        print("Incorrect input. Please enter a valid recipe ID.")
        return
    
    # 5. Retrieve entire recipe corresponding to the 'id' from db 
    recipe_to_edit = session.query(Recipe).filter_by(id=choose_recipeID).one()
    if not recipe_to_edit:
        print("Recipe with ", choose_recipeID, " doesn't exist.")
        return None
    
    # 6. Display the whole recipe (except difficulty) with number to each attribute
    print("\n-----EDIT " + recipe_to_edit.name + "-----")
    print("\nWhich column would you like to update?")
    print("1. Name: ", recipe_to_edit.name)
    print("2. Cooking Time: ", recipe_to_edit.cooking_time, " minutes")
    print("3. Ingredients: ", recipe_to_edit.ingredients)
    print("4. Cancel")

    # 7. Ask user which attribute want to edit by entering corresponding number
    choice = int(input("Enter your choice from 1 to 3 you want to edit, or 4 to cancel editing: "))

    # 8. Edit based on choice
    # Edit name
    if choice == 1:
        update_name = input("Enter the new name (or 'quit' to cancel): ").strip()
        update_name = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', update_name) # Remove escape sequences

        if update_name == 'quit':
            print("Name editing canceled. Returning to the main menu.")
            return

        if len(update_name) > 50:
            print("Name is too long - max 50 characters allowed.")
            return None
        elif not all(char.isalnum() or char.isspace() for char in update_name):
            print("Please enter only letters, numbers and spaces!")
            return None
        
        recipe_to_edit.name = update_name

    # Edit cooking time
    elif choice == 2:
        while True:
            update_cooking_time = input("Enter a new cooking time (min) - (or 'quit' to cancel): ")

            if update_cooking_time.lower() == 'quit':
                print("Cooking time editing canceled. Returning to the main menu...")
                return 
        
            if not update_cooking_time.isnumeric():
                print("Please enter numbers only.")
                continue

            update_cooking_time = int(update_cooking_time)
            if update_cooking_time <= 0:
                print("Please enter a positive number.")
                continue

            recipe_to_edit.cooking_time = update_cooking_time
            break # Exit loop after siccessful update

    # Edit ingredients
    elif choice == 3:
        while True:
            number_of_ingredients = input("How many ingredients would you like to enter? (or 'quit' to cancel): ").strip()

            if number_of_ingredients.lower() == "quit":
                print("\Ingredients editing cancelled. Returning to main menu...")
                return  # Exit function immediately
            
            if not number_of_ingredients.isnumeric() or int(number_of_ingredients) <= 0:
                print("Please enter a positive number.")
                continue
            else: 
                number_of_ingredients = int(number_of_ingredients)
                break
        
        temporary_ing_list = [] # Empty temporary ingredients list
        for i in range(number_of_ingredients):
                while True:
                    update_ingredient = input(f"Enter ingredient {i + 1} (or 'quit' to cancel): ").strip()

                    if update_ingredient.lower() == "quit":
                        print("\Ingredients editing cancelled. Returning to main menu...")
                        return  # Exit function immediately
                    
                    if len(update_ingredient) == 0:
                        print("Ingredients list cannot be empty. Please enter some ingredients!")
                        continue
                    
                    if update_ingredient in temporary_ing_list:
                        print("This ingredient already entered. Please enter a different one.")
                        continue

                    temporary_ing_list.append(update_ingredient)
                    break # Go to the next ingredient

                ingredients_str = ", ".join(temporary_ing_list) # Convert list into single string for MySQL
                recipe_to_edit.ingredients = ingredients_str # Update recipe
        
    # Cancel editing
    elif choice == 4:
        print("Editing canceled. Back to the main menu.")
        return None
    
    else:
        print("Input incorrect!")
        return None

    # Recalculate difficulty
    recipe_to_edit.calculate_difficulty()

    # 9. Commit changes to db
    session.commit()
    print("\nRecipe has been updated successfully!")
    print(recipe_to_edit)


# Definition for DELETING recipes
def delete_recipe():
    # 1. Check if any recipes exist on db, continue only if they exist. Otherwise, exit function
    if session.query(Recipe).count() == 0:
        print("There are no recipes - the list is empty.")
        return None
    
    # 2. Retrieve 'id' and 'name' for each recipe
    results = session.query(Recipe.id, Recipe.name).all()

    # 3. Display recipes from each item in 'results'
    print("\n-----AVAILABLE RECIPES TO DELETE-----")
    for recipe_id, recipe_name in results:
        print(recipe_id, ": ", recipe_name.strip())

    # 4. Ask user to pick a recipe by 'id' to delete
    try:
        choose_recipeID = input("\nEnter the ID of the recipe you want to delete (or type 'quit' to cancel): ")
        if choose_recipeID.lower() == 'quit':
            print("Deleting canceled. Returning to the main menu.")
            return
        choose_recipeID = int(choose_recipeID) # Convert to int if not quit
    except ValueError:
        print("Incorrect input. Please enter a valid recipe ID.")
        return
    
    # 5. Retrieve entire recipe corresponding to the 'id' from db 
    recipe_to_delete = session.query(Recipe).filter_by(id=choose_recipeID).one()
    if not recipe_to_delete:
        print("Recipe with ", choose_recipeID, " doesn't exist.")
        return None
    
    # 5. Ask user to delete specific recipe and confirm deleting
    confirmation = input(f"\nAre you sure you want to delete this {recipe_name} with ID {recipe_id}? \nType 'yes' to confirm or 'no' to cancel deleting: ").strip().lower()

    if confirmation in ["y", "yes"]:
        session.delete(recipe_to_delete)
        session.commit()
        print("\nRecipe has been deleted successfully!")
    else:
        print("Deletion cancelled.")
        return None

# This is loop running the main menu
# It continues to loop as long as the user doesn't choose to quit
while True:
    print("--------------------------------------------------")
    print("\n-----MAIN MENU-----")
    print("\nWhat would you like to do? Pick a choice!")
    print("1. View all recipes")
    print("2. Create recipe")
    print("3. Search for recipe")
    print("4. Update recipe")
    print("5. Delete recipe")
    print("6. Exit the program")
    choice = input("Enter your choice: ").strip().lower()

    if choice == '1':
        print("--------------------------------------------------")
        print("\nYou have chosen to view all recipes.")
        view_all_recipes()
    elif choice == '2':
        print("--------------------------------------------------")
        print("\nYou have chosen to create a new recipe.")
        create_recipe()
    elif choice == '3':
        print("--------------------------------------------------")
        print("\nYou have chosen to search for a recipe by ingredients.")
        search_by_ingredients()
    elif choice == '4':
        print("--------------------------------------------------")
        print("\nYou have chosen to update specific recipe.")
        edit_recipe()
    elif choice == '5':
        print("--------------------------------------------------")
        print("\nYou have chosen to delete specific recipe.")
        delete_recipe()
    elif choice == '6':
        print("--------------------------------------------------")
        print("\nYou have chosen to exit the program.")
        session.close()
        engine.dispose()
        break
    else:
        print("Invalid input. Please enter a valid option.")
