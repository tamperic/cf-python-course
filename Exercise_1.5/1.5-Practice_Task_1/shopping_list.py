class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    # Method to add item to the shopping list
    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(item + " has been successfully added into your shopping list!" + "\n")
        else:
            print(item + " has been already added into your shopping list." + "\n")

    # Method to remove item from the shopping list
    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(item + " successfully removed from your shopping list." + "\n")
        else: 
            print(item + " doesn't exist in your shopping list." + "\n")

    # Method to display items from the shopping list
    def view_list(self):
        if self.shopping_list:
            print("------------------------" + "\n" + "Your Shopping List:")
            print()
            for item in self.shopping_list:
                print("- " + item)
        else:
            print("Your shopping list is empty!" + "\n")
    
    # # Method to merge lists into one list
    # def merge_lists(self, obj):
    #     merged_lists_name = "Merged List - " + str(self.list_name) + " + " + str(obj.list_name)
        
    #     # Create an empty ShoppingList object
    #     merged_lists_obj = ShoppingList(merged_lists_name)

    #     # Add first shopping lists's items to the new list
    #     merged_lists_obj.shopping_list = self.shopping_list.copy()

    #     # Add second shopping list's item to the new list in order to avoid repeated items in the final list.
    #     for item in obj.shopping_list:
    #         if not item in merged_lists_obj.shopping_list:
    #             merged_lists_obj.shopping_list.append(item)

    #     # Return new merged object
    #     return merged_lists_obj


# Object from ShoppingList class
pet_store_list = ShoppingList("Pet Store Shopping List")
# grocery_store_list = ShoppingList("Grocery Store List")

# for item in ["dog food", "frisbee", "bowl", "collars", "flea collars"]:
#     pet_store_list.add_item(item)
# for item in ["fruits", "vegetables", "bowl", "ice cream"]:
#     grocery_store_list.add_item(item)

# Add items to the list
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove one item from the list
pet_store_list.remove_item("flea collars")

# Try to add the same item again to the list
pet_store_list.add_item("frisbee")

# Display the whole shopping list
pet_store_list.view_list()

# Merge lists into one final list:
# From objects - 1.1 way:
# pet_store_list.merge_lists(grocery_store_list)
# 1.2 way:
# grocery_store_list.merge_lists(pet_store_list)
# From the class itself - 2. way:
# merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

# Check if new object is as expected
# merged_list.view_list()