import unittest
from item import Book, Magazine
from library_user import LibraryUser, Library

# Define the test case class, inheriting from unittest.TestCase
class TestLibrary(unittest.TestCase):
    def setUp(self): # setUp method is called before each test method to set up any state that's shared across tests
        self.library = Library() # Create a Library instance
        # Create some Book and Magazine instances
        self.book1 = Book("The Dark", "Magnus Berg", 1993, 718)
        self.book2 = Book("The Last Christmas", "George Peril", 2000, 322)
        self.magazine1 = Magazine("Todays World", "Albella", 2022, "April")

        self.user1 = LibraryUser("Jhon")# Create a LibraryUser instance
        # Add items to the library
        self.library.add_item(self.book1)
        self.library.add_item(self.book2)
        self.library.add_item(self.magazine1)
        self.library.register_user(self.user1)# Register the user in the library

    def test_add_item(self): # Test method to check if items are added to the library
        # Assert that the items are in the library's items list
        self.assertIn(self.book1, self.library.items)
        self.assertIn(self.book2, self.library.items)
        self.assertIn(self.magazine1, self.library.items)

    def test_register_user(self): # Test method to check if a user is registered in the library
        self.assertIn(self.user1, self.library.users) # Assert that the user is in the library's users list

    def test_borrow_item(self):  # Test method to check if a user can borrow an item
        self.library.borrow_item(self.user1, self.book1) # Borrow an item
        self.assertIn(self.book1, self.user1.borrowed_items)# Assert that the item is in the user's borrowed items list
        self.assertNotIn(self.book1, self.library.items)# Assert that the item is no longer in the library's items list
      # Test method to check if a user can return an item
    def test_return_item(self):
        # Borrow and then return an item
        self.library.borrow_item(self.user1, self.book1)
        self.library.return_item(self.user1, self.book1)
        # Assert that the item is no longer in the user's borrowed items list
        self.assertNotIn(self.book1, self.user1.borrowed_items)
         # Assert that the item is back in the library's items list
        self.assertIn(self.book1, self.library.items)

if __name__ == '__main__': # Run the tests
    unittest.main()