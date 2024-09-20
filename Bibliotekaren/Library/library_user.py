from item import Item, Book, Magazine

class LibraryUser: # Class represnting a library user
    def __init__(self, name):
        self.name = name
        self.borrowed_items = [] # List to store borrowed items

    def borrow(self, item): # Method to borrow an item
        self.borrowed_items.append(item)

    def return_item(self, item): # Method to return an item
        self.borrowed_items.remove(item)

    def list_borrowed_items(self): # Method to list all borrowed items
        return [item.display_info() for item in self.borrowed_items]
    
class Library: # Class representing a library
    def __init__(self):
        self.items = [] # List to store all items in the library
        self.users = [] # List to store all registered users

    def add_item(self, item): # Method to add an item to the library
        self.items.append(item)

    def remove_item(self, item): # Method to remove an item to the library
        self.items.remove(item)

    def register_user(self, user): # Method to register a new user
        self.users.append(user)

    def borrow_item(self, user, item):# Method to borrow an item from the library
        if item in self.items and item not in [borrowed_item for  user in self.users for borrowed_item in user.borrowed_items]:
            user.borrow(item)
        else:
            raise Exception ("Item is not available for borrowing")
            
    def return_item(self, user, item): # Method to return an item to the library
        user.return_item(item)
       
    def list_items(self): # Method to list all items in the library
        return [item.display_info() for item in self.items]
    
    def list_available_items(self):
        # Create a list of all borrowed items by iterating through each user and their borrowed items
        borrowed_items = [borrowed_item for user in self.users for borrowed_item in user.borrowed_items]
        # Return a list of items that are not in the borrowed_items list, displaying their information
        return [item.display_info() for item in self.items if item not in borrowed_items]

    def borrowed_summary(self):
        summary = {} # Initialize an empty dictionary to store the summary of borrowed items
        for user in self.users: # Iterate through each user
            # Add an entry to the summary dictionary with the user's name as the key and the list of items they have borrowed as the value
            summary[user.name] = user.list_borrowed_items() 
        return summary# Return the summary dictionary

   