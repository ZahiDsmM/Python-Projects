"""
Create a simple contact list program where users can add, update, view, and delete contacts. 
Each contact should have a name and phone number.

Requirements:
 - Use a dictionary to store contacts, where the key is the contact's name and the value is their phone number.
 - Use functions for adding, viewing, and deleting contacts.
 - Use loops and flow control for managing multiple contacts.

Sample Input/Output:
Contact List Menu        
[1]. Add Contact
[2]. View Contacts       
[3]. Update Contact      
[4]. Delete Contact      
[5]. Exit

Enter your option (1-5): 2
The contact list is empty

Contact List Menu        
[1]. Add Contact
[2]. View Contacts       
[3]. Update Contact      
[4]. Delete Contact      
[5]. Exit

Enter your option (1-5): 1

Enter a contact name to add it: Zahid
Enter Zahid's phone number: 112233
A new contact added successfully.

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 1

Enter a contact name to add it: Muhammed
Enter Muhammed's phone number: 445566
A new contact added successfully.

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 2
Contact list info: 
Name: Zahid, phone: 112233
Name: Muhammed, phone: 445566

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 3

Enter the old contact name to update it: Smith
Smith not found in the contact list.

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 3

Enter the old contact name to update it: Zahid
Enter the new contact name: John
Enter John's phone number: 778877
The list has been updated successfully.

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 2
Contact list info: 
Name: Muhammed, phone: 445566
Name: John, phone: 778877

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 4

Enter the contact name to delete it: Zahid
Zahid not found in the contact list.

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 4

Enter the contact name to delete it: John
Contact John deleted successfully

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 2
Contact list info: 
Name: Muhammed, phone: 445566

Contact List Menu
[1]. Add Contact
[2]. View Contacts
[3]. Update Contact
[4]. Delete Contact
[5]. Exit

Enter your option (1-5): 5
Existing contact book. Good bye!
"""


store_contacts = {}

def add_contact():
     name = input("\nEnter a contact name to add it: ")
     if name in store_contacts:
          print(f"{name} already exist.")
          return
     
     phone = input(f"Enter {name}'s phone number: ")
     if not phone.isdigit():
          print("Invalid phone number.")
          return
     else:
          store_contacts[name] = phone
          print("A new contact added successfully.")
          

def view_contact():
     if len(store_contacts) == 0:
          print("The contact list is empty")
          return
     else:
          print("Contact list info: ")
          for name, phone in store_contacts.items():
               print(f"Name: {name}, phone: {phone}")


def update_contact():
     old_name = input("\nEnter the old contact name to update it: ")
     if old_name not in store_contacts:
          print(f"{old_name} not found in the contact list.")
          return
     else:
          new_name = input("Enter the new contact name: ")
          new_phone = input(f"Enter {new_name}'s phone number: ")
          store_contacts.pop(old_name)
          store_contacts[new_name] = new_phone
          print("The list has been updated successfully.")
          
          

def delete_contact():
     name = input("\nEnter the contact name to delete it: ")
     if name not in store_contacts:
          print(f"{name} not found in the contact list.")
          return
     else:
          del store_contacts[name]
          print(f"Contact {name} deleted successfully")
     


while True:
     print("\nContact List Menu")
     print("[1]. Add Contact")
     print("[2]. View Contacts")
     print("[3]. Update Contact")
     print("[4]. Delete Contact")
     print("[5]. Exit")
     
     option = input("\nEnter your option (1-5): ")
     if option == "1":
          add_contact()
     
     elif option == "2":
          view_contact()
     elif option == "3":
          update_contact()
     elif option == "4":
          delete_contact()
     elif option == "5":
          print("Existing contact book. Good bye!")
          break
     else:
          print("Invalid option. Please Try again.")