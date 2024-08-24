"""
Create a shopping list application that allows users to add items, 
remove items, view all items, and search for specific items (to print its index as well as the details). 

Requirements:
 - Use a list of dictionaries to manage the shopping list.
 - implement a clear interface for user interaction
 - Function to add an item with its quantity.
 - Function to remove an item by its name.
 - Function to mark an item as purchased.
 - Function to display all items, indicating whether they are purchased.
 - Function to search for an item in the list.
 - Main function to handle user input and control the flow of the application.

Sample Input/Output

Shopping List Manager
[1]. Add Item
[2]. Remove Item        
[3]. Display Items      
[4]. Search Item        
[5]. Exit

Select an option (1-5): 1

Enter the item name to add it: PC
Enter the quantity: 22
Added 22 of PC's to the shopping list.

Enter the item name to add it: TV     
Enter the quantity: 54
Added 54 of TV's to the shopping list.

Enter the item name to add it: Car    
Enter the quantity: 4 
Added 4 of Car's to the shopping list.

Enter the item name to add it: stop

Shopping List Manager
[1]. Add Item
[2]. Remove Item
[3]. Display Items
[4]. Search Item
[5]. Exit

Select an option (1-5): 3
Name: PC, Quantity: 22
Name: TV, Quantity: 54
Name: Car, Quantity: 4

Shopping List Manager
[1]. Add Item
[2]. Remove Item
[3]. Display Items
[4]. Search Item
[5]. Exit

Select an option (1-5): 2
Enter the item name to remove it: Pen
The item not exist in the shopping list.

Shopping List Manager
[1]. Add Item
[2]. Remove Item
[3]. Display Items
[4]. Search Item
[5]. Exit

Select an option (1-5): 2
Enter the item name to remove it: Car
Car Removed successfully.

Shopping List Manager
[1]. Add Item
[2]. Remove Item
[3]. Display Items
[4]. Search Item
[5]. Exit

Select an option (1-5): 3
Name: PC, Quantity: 22
Name: TV, Quantity: 54

Shopping List Manager
[1]. Add Item
[2]. Remove Item
[3]. Display Items
[4]. Search Item
[5]. Exit

Select an option (1-5): 4
What item you're looking for? TV
The location of the item in the list is  1
Item Name: TV, Quantity: 54

Shopping List Manager
[1]. Add Item
[2]. Remove Item
[3]. Display Items
[4]. Search Item
[5]. Exit

Select an option (1-5): 5
Exiting th shopping list...
"""


def add_item(shopping_list, item_name, quantity):
    if item_name in shopping_list:
        print(f"{item_name} already exist.")
        return
    else:
        shopping_list.append({"Name": item_name, "Quantity": quantity})
        print(f"Added {quantity} of {item_name}'s to the shopping list.")


def remove_item(shopping_list, item_name):
    for item in shopping_list:
        if item["Name"].lower() == item_name.lower():
            shopping_list.remove(item)
            print(item["Name"], "Removed successfully.")
            break
    else:
         print("The item not exist in the shopping list.")


def display_item(shopping_list):
    if len(shopping_list) == 0:
        print("The shopping list is empty")
        return
    else:
        for item in shopping_list:
            print(f'Name: {item["Name"]}, Quantity: {item["Quantity"]}')


def search_item(shopping_list):
    s_item = input("What item you're looking for? ")
    for item in shopping_list:
        if item["Name"].lower() == s_item.lower():
            print("The location of the item in the list is ", shopping_list.index(item))
            print(f'Item Name: {item["Name"]}, Quantity: {item["Quantity"]}')
            break
    else:
        print("The item you're looking for not found in the list.")


shopping_list = []
while True:
    print("\nShopping List Manager")
    print("[1]. Add Item")
    print("[2]. Remove Item")
    print("[3]. Display Items")
    print("[4]. Search Item")
    print("[5]. Exit")

    option = input("\nSelect an option (1-5): ")
    if option == "1":
        while True:
             item_name = input("\nEnter the item name to add it: ")
             if item_name.lower() == "stop":
                  break
             quantity = input("Enter the quantity: ")
             add_item(shopping_list, item_name, quantity)
    elif option == "2":
        item_name = input("Enter the item name to remove it: ")
        remove_item(shopping_list, item_name)
    elif option == "3":
        display_item(shopping_list)
    elif option == "4":
        search_item(shopping_list)
    elif option == "5":
        print("Exiting th shopping list...")
        break
    else:
        print("Invalid option. Try again...")
