my_file = open('recipes.txt', 'r')

# Read just first 10 characters of my_file
print(my_file.read(10))

# Confirm how many characters were printed
my_file.tell()

# Read next 10 characters from the file
print(my_file.read(10))

# Print the rest of the my_file
string_complete = my_file.read()

# Reset position to the beginning of the my_file
my_file.seek(0)

# Now print the entire my_file
print(my_file.read())

# Print for the first time the first line of the file, the second time the second line, etc
print(my_file.readline())

# Point ot he beginning, store output of 'readlines()' with a variable 'all_recipes' and print entire file
my_file.seek(0)
all_recipes = my_file.readlines()
print(all_recipes)

# Apply 'rstrip' function using 'for' loop to eliminate the newline characters (strip the '\n' character of each item)
all_recipes_clean_1 = []
for recipe in all_recipes:
    all_recipes_clean_1.append(recipe.rstrip('\n'))
print(all_recipes_clean_1)

# Perform 'rstrip' using list comprehension 
all_recipes_clean_2 = [recipe.rstrip('\n') for recipe in all_recipes]
print(all_recipes_clean_2)

# Close the file stream when done performin operations on a file object
my_file.close()