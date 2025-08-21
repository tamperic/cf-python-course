class Animal(object):
    # Every animal has an age, but a name may not be necessary
    def __init__(self, age):
        self.age = age
        self.name = None

    # Throw in getter methods for age and name
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    # And setter methods as well
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    # Have a well-formatted strin representation
    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + "\nAge" + str(self.age)
        return output
    
# Create 'a' objects under 'Animal' class
a = Animal(5)
print(Animal)


class Cat(Animal):
    # Introduce a new method where it speaks
    def speak(self):
        print("Meow!")

    # Antoher neat string representation for cats
    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + "\nAge: " + str(self.age)
        return output
    
class Dog(Animal):
    # Implement another speak() method for dogs
    def speak(self):
        print("Woof!")

    # String representation for dogs
    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + "\nAge: " + str(self.age)
        return output
    
# Create objects 'cat' and 'dog' under the 'Cat' and 'Dog' classes
cat = Cat(3)
dog = Dog(6)

cat.set_name("Stripes")
dog.set_name("Bubbles")

print(cat)
print(dog)

cat.speak()
dog.speak()

class Human(Animal):
    # Make its own initialization method
    def __init__(self, name, age):
        #Call the parent class' init method to initialize other attributes like 'name' and 'age'
        Animal.__init__(self, age)

        # Set a name, since humans must have names
        self.set_name(name)

        # New attribute for humans, 'friends'
        self.friends = []

    # Add another method to add friends
    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    # A method to display friends
    def show_friends(self):
        for friend in self.friends:
            print(friend)

    # Humans can speak sentences
    def speak(self):
        print("Hello, my name's " + self.name + "!")

    # Modify the string representation to include friends as well
    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + "\nAge: " + str(self.age) + "\n\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output
    
human = Human("Tobias", 35)
human.add_friend("Robert")
human.add_friend("Elise")
human.add_friend("Asha")
human.add_friend("Saito")
human.add_friend("Lupita")

human.speak()
print(human)