from abc import ABC, abstractmethod
# Abstract base class for items
class Item(ABC):
    def __init__(self, title, author, year):
        # Initialize the common attributes for all items
        self.title = title
        self.author = author
        self.year = year

    @abstractmethod # Abstract metod to be implemented by subclasses
    def display_info(self):
        pass

class Book(Item): # Subclass for books
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year) # Initialize the attributes of the parent class
        self.pages = pages # Initialize the specific attribute for books

    def display_info(self): # Implementation of the abstract metod for books 
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}"

class Magazine(Item): # Subclass for magazine
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year) # Initialize the attributes of the parent class
        self.issue = issue # Initialize the specific attribute for magazines

    def display_info(self): # Implementation of the abstract method for magazines
        return f"Magazine: {self.title}, Author: {self.author}, Year: {self.year}, Issue: {self.issue}"