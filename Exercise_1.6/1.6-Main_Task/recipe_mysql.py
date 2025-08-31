# Import 'mysql.connector' module
import mysql.connector

# Initialize a connection object called 'conn', which connects with the following parameteres: host, user, passswd.
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    password='password',
    database='task_database'
)

# Initialize a 'cursor' object from 'conn'
cursor = conn.cursor()

# Crate database called 'task_database'
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# 'USE' statment so that the script can access database
cursor.execute("USE task_database")

# Create a table called 'Recipes' with its 5 columns
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id                INT AUTO_INCREMENT PRIMARY KEY,
    name              VARCHAR(50),
    ingredients       VARCHAR(255),
    cooking_time      INT,
    difficulty        VARCHAR(20)
)''')

# Function to calculate the difficulty of the recipe base on cooking time and number of ingredients
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and ingredients < 4:
        difficulty = "Easy"

    elif cooking_time < 10 and ingredients >= 4:
        difficulty = "Medium"

    elif cooking_time >= 10 and ingredients < 4:    
        difficulty = "Intermediate"

    elif cooking_time >= 10 and ingredients >= 4:
        difficulty = "Hard"

    return difficulty

# Function that allowing user to choose opetion: create, search for, update or delete recipe.
def main_menu(conn, cursor):
    # Definition for creating recipe
    def create_recipe(conn, cursor):
        # Ask for recipe name, cooking time, and ingredients
        name = str(input("Enter a name of recipe: "))
        cooking_time = int(input("Enter a cooking time (in minutes): "))
        ingredients = list(input("Enter ingredients: ").split(",")) # Stored as a list
        ingredients_str = ", ".join(ingredients) # convert list into single string for MySQL

        # Count the number of ingredients
        numberOfIngredients = len(ingredients)
        difficulty = calculate_difficulty(cooking_time, numberOfIngredients)

        query = "INSERT INTO Recipes(name, cooking_time, ingredients, difficulty) VALUES (%s, %s, %s, %s)"
        values = (name, cooking_time, ingredients_str, difficulty)
        # Execute query
        cursor.execute(query, values)
        conn.commit()

        print("\nRecipe has been added successfully!")

    # Definition for searching for recipe
    def search_recipe(conn, cursor):
        # 1. Step: Get all ingredients from 'Recipes' table
        cursor.execute("SELECT ingredients FROM Recipes") 
        results = cursor.fetchall()

        # 2. Step: Add each ingredient into a new 'all_ingredients' list, and make sure that there are no duplicates
        all_ingredients = set() # Create empty 'set' like a list to store all ingredients without duplicates

        # Loop over rows got from database
        for row in results:
            ingredients_str = row[0] # Get string from tuple, each 'row' is a tuple with one element
            ingredients_list = [ingredient.strip() for ingredient in ingredients_str.split(", ")] # Split each string by commas to get individual ingredients and strip extra spaces
            all_ingredients.update(ingredients_list) # Add all ingredients from the list into the 'set (no duplicates)
    
        # 3. Step: Display all ingredients and let user pick one
        all_ingredients = list(all_ingredients) # Convert set to list for indexing

        print("Ingredients Available Across All Recipes:")
        for index, ingredient in enumerate(all_ingredients, 1):
            print(index, ":", ingredient.strip())

        # Ask user to pick one ingredient by number
        try:
            choose_number = int(input("\nEnter a number of the ingredient you want to search for: ")) 
            search_ingredient = all_ingredients[choose_number - 1].strip()
            print("\n->You are searching for recipes with", search_ingredient, ".")
        except:
            print("Invalid input. Please enter a valid number from the list of ingredients.")
        
        # 4. Step: Search Recipes table for rows containing the selected ingredient
        query = "SELECT name, cooking_time, ingredients, difficulty FROM Recipes WHERE ingredients LIKE %s"
        cursor.execute(query, ("%" + search_ingredient + "%",))
        matched_results = cursor.fetchall()

        # Show results
        if matched_results:
            print("\nRecipes containing ", search_ingredient, ":")
            for row in matched_results:
                print("Name: ", row[0])
                print("Cooking time: ", row[1], " minutes")
                print("Ingredients: ", row[2])
                print("Difficulty: ", row[3])
                print()
        else:
            print("\nNo recipes found containing", search_ingredient, ".")

    # Definition for updating recipe
    def update_recipe(conn, cursor):
        # 1. Step: Fetch and list all recipes
        cursor.execute("SELECT * FROM Recipes") 
        fetched_recipes = cursor.fetchall()

        print("\nAll Recipes:")
        for row in fetched_recipes:
            print(
                "\nID: ", row[0],
                "\nName: ", row[1], 
                "\nCooking Time (min):", row[3], 
                "\nIngredients:", row[2], 
                "\nDifficulty:", row[4]
            )
        try:
            choose_recipeID = input("\nEnter the ID of the recipe you want to update (or type 'quit' to cancel): ")
            if choose_recipeID.lower() == 'quit':
                print("Updating canceled. Returning to the main menu.")
                return
            choose_recipeID = int(choose_recipeID) # Convert to int if not quit
        except ValueError:
            print("Incorrect input. Please enter a valid recipe ID.")
            return

        # 2. Step: Choose column to update
        print("\nWhich column would you like to update?")
        print("1. Name")
        print("2. Cooking Time")
        print("3. Ingredients")
        print("4. Cancel")
        choice = int(input("Enter your choice from 1 to 3 you want to edit, or 4 to cancel: "))

        if choice == 1:
            update_name = input("Enter a new recipe name: ")
            update_query = "UPDATE Recipes SET name = %s WHERE id = %s"
            try:
                cursor.execute(update_query, (update_name, choose_recipeID))
                conn.commit()
            except mysql.connector.Error as err:
                print("Error:", err)
                conn.rollback()
        elif choice == 2:
            update_cooking_time = int(input("Enter a new cooking time (min): "))
            update_query = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
            try:
                cursor.execute(update_query, (update_cooking_time, choose_recipeID))
                conn.commit()
            except mysql.connector.Error as err:
                print("Error:", err)
                conn.rollback()

            # Recalculate difficulty
            cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (choose_recipeID,))
            ingredients = cursor.fetchone()[0].split(", ")
            difficulty = calculate_difficulty(update_cooking_time, len(ingredients))
            cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, choose_recipeID)) # Update difficulty in table
        elif choice == 3:
            update_ingredients = input("Enter new ingredients: ")
            update_query = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
            try:
                cursor.execute(update_query, (update_ingredients, choose_recipeID))
                conn.commit()
            except mysql.connector.Error as err:
                print("Error:", err)
                conn.rollback()

            # Recalculate difficulty
            cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (choose_recipeID,))
            cooking_time = cursor.fetchone()[0]
            ingredients_list = [i.strip() for i in update_ingredients.split(",")]
            difficulty = calculate_difficulty(cooking_time, len(ingredients_list))
            cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, choose_recipeID)) # Update difficulty in table
        elif choice == 4:
            print("Editing canceled. Back to the main menu.")
            return
        else:
            print("Input incorrect!")

        conn.commit()
        print("\nRecipe has been updated successfully!")


    # Definition for deleting recipe 
    def delete_recipe(conn, cursor):
        cursor.execute("SELECT * FROM Recipes")
        all_recipes = cursor.fetchall()

        if not all_recipes:
            print("There are no recipes. The list is empty.")
        else:
            print("\nAll Recipes:")
            for row in all_recipes:
                print(
                    "\nID:", row[0],
                    "\nName: ", row[1], 
                    "\nCooking Time (min):", row[3], 
                    "\nIngredients:", row[2], 
                    "\nDifficulty:", row[4]
                )

        try:
            choose_recipeID = input("\nEnter the ID of the recipe you want to delete (or type 'quit' to cancel): ")
            if choose_recipeID.lower() == 'quit':
                print("Deleting canceled. Returning to the main menu.")
                return
            choose_recipeID = int(choose_recipeID) # Convert to int if not quit
        except ValueError:
            print("Incorrect input. Please enter a valid recipe ID.")
            return


        cursor.execute("DELETE FROM Recipes WHERE id = %s", (choose_recipeID,))
        conn.commit()
        print("\nRecipe has been deleted successfully!")

    # This is loop running the main menu.
    # It continues to loop as long as the user doesn't choose to quit.
    choice = ""
    while(choice != 'quit'):
        print("--------------------------------------------------")
        print("\nWhat would you like to do? Pick a choice!")
        print("1. Create recipe")
        print("2. Search for recipe")
        print("3. Update recipe")
        print("4. Delete recipe")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == '1':
            print("--------------------------------------------------")
            print("\nYou have chosen to create a new recipe.")
            create_recipe(conn, cursor)
        elif choice == '2':
            print("--------------------------------------------------")
            print("\nYou have chosen to search for a recipe.")
            search_recipe(conn, cursor)
        elif choice == '3':
            print("--------------------------------------------------")
            print("\nYou have chosen to update specific recipe.")
            update_recipe(conn, cursor)
        elif choice == '4':
            print("--------------------------------------------------")
            print("\nYou have chosen to delete specific recipe.")
            delete_recipe(conn, cursor)
        else:
            break


# Start the main menu
main_menu(conn, cursor)

# close connection after menu loop ends
cursor.close()
conn.close()
print("Connection closed.")