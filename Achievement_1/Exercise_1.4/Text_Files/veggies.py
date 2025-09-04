# vegetables = ['Tomato\n', 'Carrot\n', 'Cucumber\n']
# my_file = open('veggies.txt', 'w')
# my_file.writelines(vegetables)
# my_file.close()


vegetables = ['Tomato\n', 'Carrot\n', 'Cucumber\n']
with open('veggies.txt', 'w') as my_file:
    my_file.writelines(vegetables)