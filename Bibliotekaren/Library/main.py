from item import Book, Magazine
from library_user import LibraryUser, Library

if __name__ == "__main__":
    # Create the library
    library = Library()

    # Create some books and magazines
    book1 = Book("The Dark", " Magnus Berg", 1993, 718)
    book2 = Book("The Last Christmas", "George Peril", 2000, 322)
    magazine1 = Magazine("Todays World", "Albella", 2022, "April")

    # Add items to the library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)

    # Register a user
    user1 = LibraryUser("Jhon")
    library.register_user(user1)

    # User borrows a book
    library.borrow_item(user1, book1)

    # Show borrowed items
    print(f"Borrowed items by {user1.name}:")
    print(user1.list_borrowed_items())

    # Show available items in the library
    print("\nAvailable items in the library:")
    print(library.list_available_items())

    # User returns the book
    library.return_item(user1, book1)

    # Show available items again
    print("\nAvailable items in the library after return:")
    print(library.list_available_items())