"""
Create a python program named as grocery_list_manager that manages a grocery list. 
Users should be able to add items, remove items, update items, and view the list.

Note that:
 - if the items already exist in the list, display an appropriate message
 - if the item not found in the list (when removing it), display an appropriate message
 - if the old item not in the list (when updating it), display an appropriate message
 
Requirements:
 - Use a list to store grocery items.
 - Use functions to add, remove, and display items.
 - Use loops to handle multiple operations until the user decides to exit.

Sample Input/Output:
Welcome to the Grocery List Manager!

Available Options:        
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4:1

What item do you want to add? banana
banana added successfully.

Available Options:        
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4:1

What item do you want to add? apple
apple added successfully. 

Available Options:        
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4:1

What item do you want to add? milk
milk added successfully.

Available Options:      
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4:3

The items are:
banana
apple
milk

Available Options:
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4:2

What item do you want to remove? water
water not found in the list!

Available Options:
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4:2

What item do you want to remove? banana
banana removed successfully

Available Options:
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4:4

What is the old item you want to update it? milk
What is the new item? laptop
milk successfully updated to laptop

Available Options:
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4:3

The items are:
apple
laptop

Available Options:
[1] add items
[2] remove items
[3] display items
[4] update items
[5] exist
Select an option from 1-4: 5 

"""
def add_items(list_items, item):
    if item in list_items:
        print(f"{item} already exist!") 
    else:
        list_items.append(item)
        print(f"{item} added successfully.")


def remove_items (list_items, item):
     if item not in list_items:
          print(f"{item} not found in the list!")
     else:
          list_items.remove(item)
          print(f"{item} removed successfully")

def update_items(list_items, old_item, new_item):
     if old_item in list_items:
          index = list_items.index(old_item)
          list_items[index] = new_item 
          print(f"{old_item} successfully updated to {new_item}")
     else:
          print(f"{old_item} not found in the list!")
     

def display_items(list_items):
     if len(list_items) != 0:
          print("\nThe items are: ")
          for i in list_items:
               print(i)
     else:
          print("\nThe list is empty!")


################# Main ###################
list_items = []
print("Welcome to the Grocery List Manager!")
while True:
     print("\nAvailable Options:")
     print("[1] add items")
     print("[2] remove items")
     print("[3] display items")
     print("[4] update items")
     print("[5] exist")
     
     option = input("Select an option from 1-4:")
     
     if option == "1":
          item = input("\nWhat item do you want to add? ")
          add_items(list_items, item)
     
     elif option == "2":
          item = input("\nWhat item do you want to remove? ")
          remove_items(list_items, item)
     
     elif option == "3":
          display_items(list_items)
     
     elif option == "4":
          old_item = input("\nWhat is the old item you want to update it? ")
          new_item = input("What is the new item? ")
          update_items(list_items, old_item, new_item)
     
     elif option == "5":
          print("Existing...")
          break
     else:
          print("Invalid option. Please Try again.")
     
     
     
