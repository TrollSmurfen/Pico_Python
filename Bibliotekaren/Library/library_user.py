from item import Item, Book, Magazine

class LibraryUser: # Class representing a library user
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

    def remove_item(self, item): # Method to remove an item from the library
        self.items.remove(item)

    def register_user(self, user): # Method to register a new user
        self.users.append(user)

    def borrow_item(self, user, item): # Method to borrow an item from the library
        if item in self.items and item not in [borrowed_item for user in self.users for borrowed_item in user.borrowed_items]:
            user.borrow(item)
            self.items.remove(item)  # Ensure the item is removed from the library's inventory
        else:
            raise Exception("Item is not available for borrowing")

    def return_item(self, user, item): # Method to return an item to the library
        user.return_item(item)
        self.items.append(item)

    def list_items(self): # Method to list all items in the library
        return [item.display_info() for item in self.items]

    def list_available_items(self): # Method to list all available items in the library
        borrowed_items = [borrowed_item for user in self.users for borrowed_item in user.borrowed_items]
        return [item.display_info() for item in self.items if item not in borrowed_items]

    def borrowed_summary(self): # Method to get a summary of borrowed items
        summary = {}
        for user in self.users:
            summary[user.name] = user.list_borrowed_items()
        return summary

   