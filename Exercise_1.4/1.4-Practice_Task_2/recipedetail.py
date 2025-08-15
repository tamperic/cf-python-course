# Import pickle
import pickle

# Initialize the dictionary
recipe = {
    'Name': 'Tea',
    'Ingredients': ['Tea leaves', 'Water', 'Sugar'],
    'Cooking_Time': 5,
    'Difficulty': 'Easy'
}

# Store the dictionary in a binary file called 'recipe_binary.bin' and open it in write with binary mode ('wb')
my_file = open('recipe_binary.bin', 'wb')

# Call 'pickle.dump()' method, while passing 'recipe' as the dictionary, and 'my_file' as the file object
pickle.dump(recipe, my_file)

# Close the file
my_file.close()


# Load the binary data from ''recipe_binary.bin' and treats it as a pickle, extracting the original data containing the vehicle dictionary
with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print('Recipe details:')
print('Name: ' + recipe['Name'])
print('Ingredients: ' + ', '.join(recipe['Ingredients']))
print('Cooking Time: ' + str(recipe['Cooking_Time']))
print('Difficulty: ' + recipe['Difficulty'])