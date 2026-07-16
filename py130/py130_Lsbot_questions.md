# LS Bot Generated Questions for PY130


## Lesson 1: Functions, Generators, and Files

### First Class and Higher-Order Functions

#### Question 1


Difficulty:​ Basic

Objective:​ Understand and trace a simple iteration within a class method before introducing higher-order functions. This will establish a baseline for comparison.

Problem Statement:

Consider the following Book and Library classes. The Library class has a print_authors method that iterates through its collection of books and prints the author of each book.

Your task is to carefully trace the execution of the provided code and predict the exact output. Please provide your predicted output.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class Library:
    def __init__(self, title):
        self.title = title
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_authors(self):
        print(f"Authors at {self.title}:")
        for book in self.books:
            print(f"- {book.author}")

# Setup
my_library = Library("City Central Library")
my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
my_library.add_book(Book("1984", "George Orwell"))

# Execution
my_library.print_authors()
```


<details> 
<summary>Possible Solution</summary> 
</details>