def display(file):
    heroes = []
    for line in file:
        # Removing newline characters
        line = line.rstrip("\n")

        # Split the hero name and the year separately. The separation occurs at ", ". Taking the first element of the split (name).
        hero_name = line.split(", ")[0]

        # Taking the second element of the split (year)
        first_appearance = line.split(", ")[1]

        # Pack these two into a smaller, two-element list, and appent it to the list "heroes".
        heroes.append([hero_name, first_appearance])

    # Sort "heroes" by first appearance
    heroes.sort(key = lambda hero: hero[1])

    for hero in heroes:
        print("----------------------------------")
        print("Superhero: ", hero[0])
        print("Year of First Appearance: ", hero[1])

filename = input("Enter the filename where you've stored your superheroes: ")
try: 
    file = open(filename, 'r')
    display(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
except:
    print("An unexpected error occured.")
else: 
    file.close()
finally:
    print("Goodbye!")