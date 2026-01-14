
# PY129 LSBOT Exam Prep Questions

## Pass 1

Based on the topics covered in PY120 and the Object Oriented Programming with Python book, here are 20 questions that cover the core concepts you'll need to understand for the PY129 assessment.   

### 1. **Conceptual**:  What is a class and what is an object in Python?  Explain their relationship.  

<details>
<summary>Possible Solution</summary>
</details>

### 2. **Conceptual**: What is the purpose of the `__init__` method in a Python class? What does the `self` parameter represent?

<details>
<summary>Possible Solution</summary>
</details>

### 3. **Conceptual**:  Explain the difference between a class attribute and an instance attribute. Provide a code example to demonstrate this difference.

<details>
<summary>Possible Solution</summary>
</details>

### 4. **Conceptual**:  Describe the differences between an instance method, a class method, and a static method.  Provide a code example showing how to define and call each.  

<details>
<summary>Possible Solution</summary>
</details>

### 5. **Conceptual**: What is inheritance?  Explain how a subclass inherits from a superclass and demonstrate with a simple code example.

<details>
<summary>Possible Solution</summary>
</details>

### 6. **Conceptual**: What is method overriding? How can a method in a subclass call the overridden method from its superclass?

<details>
<summary>Possible Solution</summary>
</details>

### 7. **Conceptual**: Explain Python's Method Resolution Order (MRO). How would you view the MRO for a specific class?

<details>
<summary>Possible Solution</summary>
</details>

### 8. **Conceptual**: What is a mix-in module in the context of Python OOP? What problem does it solve?

<details>
<summary>Possible Solution</summary>
</details>

### 9. **Conceptual**: Explain the concept of polymorphism in Python. How does it relate to "duck typing"?

<details>
<summary>Possible Solution</summary>
</details>

### 10. **Conceptual**: What is encapsulation? How does Python support it, and what is the purpose of name mangling (e.g., `__private_attribute`)?

<details>
<summary>Possible Solution</summary>
</details>

### 11. **Conceptual**: What is a collaborator object? Provide an example of two classes where one class uses an object of the other class as a collaborator. 

<details>
<summary>Possible Solution</summary>
</details>

### 12. **Conceptual**: Explain the difference between the `is` and `==` operators when comparing two objects. When would you implement the `__eq__` method?

<details>
<summary>Possible Solution</summary>
</details>

### 13. **Conceptual**: What is the purpose of the `__str__` and `__repr__` dunder methods? What are the key differences between them?

<details>
<summary>Possible Solution</summary>
</details>

### 14. **Conceptual**: How can you define a "private" method or attribute in Python? What is the convention, and does it enforce true privacy?

<details>
<summary>Possible Solution</summary>
</details>

### 15. **Coding**: Write a `Cat` class that is initialized with a name. The class should have one instance attribute, `name`, and one instance method, `speak`, which returns `"Meow!"`.

<details>
<summary>Possible Solution</summary>
</details>

### 16. **Coding**: Given the following code, what is the output and why? 

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __gt__(self, other):
        return len(self.name) > len(other.name)

alex = Person("Alex")
bob = Person("Robert")

print(alex > bob)
print(bob > alex)
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 17. **Coding**: What is the output of the following code? Explain the role of the class attribute count.

```Python
class Pet:
    count = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        Pet.count += 1

pet1 = Pet("Dog", "Fido")
pet2 = Pet("Cat", "Whiskers")
pet3 = Pet("Dog", "Buddy")

print(Pet.count)
```

<details>
<summary>Possible Solution</summary> 
</details>

### 18. **Coding**: What does the following code print? Explain the method lookup path for buddy. speak().
```Python
class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Labrador(Dog):
    pass

buddy = Labrador()
print(buddy.speak())
```
<details> 
<summary>Possible Solution</summary> 
</details>

### 19. **Coding**: Create a Vehicle class and two subclasses, Car and Motorcycle. The Vehicle class should have attributes for make and model. The Car class should have an additional attribute for num_doors, and the Motorcycle class should have an additional attribute for has_sidecar.

<details> 
<summary>Possible Solution</summary> 
</details>

### 20. **Coding**: Implement a Wallet class that holds Cash objects. The Wallet should be able to add Cash objects to it and report the total amount of money it contains. A Cash object should have currency and amount attributes. This demonstrates collaborator objects.


### 20a. **Coding** `Wallet` part 2. Creating a Class with Properties

Improve on the `Wallet` Class.
1. The `Wallet` should be initialized with a starting balance. This balance should be stored in an instance variable that is intended for internal use only (follow Python's convention).
2. Implement a balance property that allows a user to get the value of the balance.
3. Implement a setter for the balance property. The setter should perform validation:
    * It must ensure the new balance is a non-negative number (integer or float).
    * If the new balance is invalid, it should raise a `ValueError` with an appropriate message.
4. Add an add_money method that takes an amount and adds it to the balance. This method should also validate that the amount being added is a positive number, raising a ValueError if not.

Example Usage:

```python
my_wallet = Wallet(100)
print(f"Initial balance: {my_wallet.balance}")  # Expected: Initial balance: 100

my_wallet.add_money(50)
print(f"After adding money: {my_wallet.balance}") # Expected: After adding money: 150

try:
    my_wallet.add_money(-20)
except ValueError as e:
    print(e)  # Expected: Amount must be positive.

try:
    my_wallet.balance = -500
except ValueError as e:
    print(e)  # Expected: Balance cannot be negative.

print(f"Final balance: {my_wallet.balance}") # Expected: Final balance: 150
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 21. **Conceptual** What is the output of the following code? 

Explain why each line produces its output, paying close attention to the difference between class and instance variables and methods.

```python
class Pet:
    total_pets = 0

    def __init__(self, name):
        self._name = name
        self.__class__.total_pets += 1

    def speak(self):
        return f"{self._name} makes a sound."

    @classmethod
    def get_total_pets(cls):
        return f"There are {cls.total_pets} pets in total."

class Dog(Pet):
    def speak(self):
        return f"{self._name} barks."

class Cat(Pet):
    def speak(self):
        return f"{self._name} meows."

# Code to analyze
pet1 = Dog("Fido")
pet2 = Cat("Whiskers")
pet3 = Dog("Rex")

print(pet1.speak())
print(pet2.speak())
print(Pet.get_total_pets())
print(Dog.get_total_pets())
print(pet3.total_pets)
```

<details> 
<summary>Possible Solution</summary> 
</details>


## Pass 2

Based on the topics covered in PY120 and the PY129 Study Guide, here are 20 advanced questions designed to test your readiness for the assessment.

### 22. **Difficulty: Advanced (MRO & `super()`)** Given the following multiple inheritance structure:

```Python
class A: 
    pass
class B(A): 
    pass
class C(A): 
    pass
class D(B, C): 
    pass
```

What is the Method Resolution Order (MRO) for class D? Now, implement these classes. Give each class a method named identify that prints its class name and then calls `super().identify()`. What is the output when you call this method on an instance of D?

<details> 
<summary>Possible Solution</summary> 
</details>

### 23. **Difficulty: Advanced (Class vs. Instance Attributes)** Create a `Widget` class with a class attribute `widgets_created` that increments every time a new instance is created. 

It should also have an instance attribute for its name. Implement a class method that returns the total number of widgets created. Then, demonstrate how modifying the class attribute through an instance (`my_widget.widgets_created` = 5) can lead to unexpected behavior for future instances. Explain why this happens.

<details> 
<summary>Possible Solution</summary> 
</details>

### 24. **Difficulty: Advanced (Encapsulation & Properties)** Design a `BankAccount` class. The account balance should be encapsulated using name mangling (__). 

Provide a read-only property to access the balance. Implement deposit and withdraw methods. The withdraw method must not allow the balance to go below zero; if an attempt is made, it should raise a custom `InsufficientFundsError`.

<details> 
<summary>Possible Solution</summary> 
</details>

### 25. **Difficulty: Advanced (Collaborator Objects)** Design and implement a `Deck` class and a `Card` class. A `Deck` should be initialized with 52 unique `Card` objects. 

The `Deck` class should "have" a list of `Card` objects as its primary instance variable. Implement shuffle and deal methods for the Deck. The deal method should remove and return the top card from the deck.

<details> 
<summary>Possible Solution</summary> 
</details>

### 26. **Difficulty: Advanced (str vs. repr)** Create a `Book class with title and author attributes. Implement both `__str__` and `__repr__` methods. 

The `__str__` method should return a user-friendly string (e.g., "To Kill a Mockingbird by Harper Lee"), while the `__repr__ `should return a developer-friendly string that could be used to recreate the object (e.g., `Book("To Kill a Mockingbird", "Harper Lee")`). Explain the primary use case for each method.

<details> 
<summary>Possible Solution</summary> 
</details>

### 27. **Difficulty: Advanced (Custom Comparison)** Implement a Version class that takes a version string like "2.1.15" as input. Override all rich comparison magic methods (`__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__`) to allow for correct comparison between Version objects. 

For example, Version("2.1.5") should be less than Version("2.2.0").

<details> 
<summary>Possible Solution</summary> 
</details>

### 28. **Difficulty: Advanced ("is-a" vs. "has-a")** Explain the difference between the "is-a" relationship (inheritance) and the "has-a" relationship (composition/collaboration).

Provide a clear Python code example for both. For instance, model a Car, a Truck, a Vehicle, and an Engine. Justify your design choices regarding which relationships are "is-a" and which are "has-a".

<details> 
<summary>Possible Solution</summary> 
</details>

### 29. **Difficulty: Advanced (Polymorphism & Duck Typing)** Write a single function render_elements(elements) that iterates through a list of objects and calls a `.render()` method on each one. 

Create three distinct classes (`Button`, `TextField`, `Checkbox`) that do not share a parent class but each have a `.render()` method with a different implementation (e.g., printing what they are). Demonstrate that your function works polymorphically with a list containing instances of all three classes.

<details> 
<summary>Possible Solution</summary> 
</details>

### 30. **Difficulty: Advanced (Static vs. Class Methods)** Create a class `MyDate`. Implement a class method from_iso_format(date_string) that takes a string like "2023-12-25" and returns a new `MyDate` instance. 

Implement a static method is_valid_format(date_string) that returns True or False depending on whether the date string is in a valid YYYY-MM-DD format. Explain precisely why a class method is appropriate for the first task and a static method is appropriate for the second.

<details> 
<summary>Possible Solution</summary> 
</details>

### 31. **Difficulty: Advanced (Custom Arithmetic)** Implement a `Vector` class that represents a 2D vector with x and y attributes. 

Override the `__add__` and `__sub__` magic methods to allow for vector addition and subtraction. Also, override `__mul__` to perform a scalar multiplication (e.g., my_vector * 3).

<details> 
<summary>Possible Solution</summary> 
</details>

### 32. **Difficulty: Advanced (Mix-ins)** Create a mix-in class called `LoggerMixin` that has a log method which prints a message with the object's class name and memory address. 

Create two unrelated classes, `DatabaseConnection` and `FileSystemObject`, and demonstrate how you can add the logging functionality to both using the mix-in without using multiple inheritance from a common functional base class.

<details> 
<summary>Possible Solution</summary> 
</details>

### 33. **Difficulty: Advanced (Name Mangling)** What is name mangling in Python? 

Provide a code example using a class with an attribute prefixed with a double underscore (e.g., `__value`). Show how to access this attribute from outside the class using its mangled name. Explain why this feature is not for creating true private members and what its main purpose is.

<details> 
<summary>Possible Solution</summary> 
</details>

### 34. **Difficulty: Advanced (`is` vs `==`)** Create a Point class with x and y attributes. Implement the `__eq__` method so that two Point instances are considered equal if their x and y values are the same. 

In your script, create two different Point objects with the same coordinates. Demonstrate that `point1 == point2` evaluates to `True`, while `point1 is point2` evaluates to `False`. Explain the output.

<details> 
<summary>Possible Solution</summary> 
</details>

### 35. **Difficulty: Advanced (Custom Exceptions)** Create a custom exception class `InvalidUsernameError`. Then, create a `User` class. 

In the `__init__` method, validate the username to ensure it is alphanumeric and between 4 and 16 characters long. If the validation fails, raise your `InvalidUsernameError` with an appropriate message.

<details> 
<summary>Possible Solution</summary> 
</details>

### 36. **Difficulty: Advanced (Code Reading: Inheritance and State)** What is the output of the following code and why? Explain the state of each object and which speak method is called in each iteration.

```Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Poodle(Dog):
    def speak(self):
        return f"{self.name} yips."

animals = [Poodle("Fifi"), Dog("Rex"), Animal("Generic")]
for animal in animals:
    print(animal.speak())
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 37. **Difficulty: Advanced (Callable Objects)** Implement a `SequenceGenerator` class where instances of the class are callable. 

The class should be initialized with a start number and a step. Each time the instance is called, it should return the next number in the sequence.

```Python
evens = SequenceGenerator(0, 2)
print(evens()) # Expected: 0
print(evens()) # Expected: 2
print(evens()) # Expected: 4
```

Which magic method must you implement to achieve this?

<details> 
<summary>Possible Solution</summary> 
</details>

### 38. **Difficulty: Advanced (Scope and Inheritance)** Explain how inheritance influences attribute lookup in Python. 

Provide a code example with a base class and a derived class where the derived class accesses:

* An instance variable defined only in the base class's `__init__`.
* A class variable defined only in the base class.
* A method defined only in the base class.

<details> 
<summary>Possible Solution</summary> 
</details>

### 39. **Difficulty: Advanced (`super()` in `init`)** Why is it considered a best practice to call `super().__init__()` within the `__init__` method of a subclass? 

What potential problems can arise if you fail to do so? Provide a simple code example with a multi-level inheritance hierarchy (A -> B -> C) to illustrate a problem where class C fails to initialize state from class A.

<details> 
<summary>Possible Solution</summary> 
</details>

### 40. **Difficulty: Advanced (Properties for Validation)** Create a `Temperature` class that stores temperature in Celsius. 

Use a private `_celsius` attribute. Create a property fahrenheit with a getter and a setter. The getter should convert the Celsius temperature to Fahrenheit. The setter should take a Fahrenheit value, convert it to Celsius, and store it in the private `_celsius` attribute.

<details> 
<summary>Possible Solution</summary> 
</details>

### 41. **Difficulty: Advanced(Inhertance and Collaboration)** You are building a system for a library.

1. Create a `Writer` class that is initialized with a `name`.
2. Create a base class `Publication` that is initialized with a `title` and a `Writer` object (this is a "has-a" relationship/collaboration). It should have a display method that prints the title and the writer's name.
3. Create two subclasses that inherit from `Publication`: `Book` and `Magazine`.
    * Book should be initialized with a title, a writer, and a genre.
    * Magazine should be initialized with a title, a writer, and an issue_date.

4. Both `Book` and `Magazine` should override the display method. They must first call the parent class's display method using `super()` and then print their own specific information (genre for `Book`, issue date for `Magazine`).

5.  Finally, implement a custom `__str__` method for the Publication class that returns the string `"{title}" by {writer's name}`.

### 42. **Difficulty: Advanced (Code Reading: MRO and `super()`)** Predict the output of the following code.

Explain your reasoning by tracing the Method Resolution Order and the super() calls step-by-step.

```Python
class A:
    def process(self):
        print("Processing in A")

class B:
    def process(self):
        print("Processing in B")

class C(A, B):
    def process(self):
        print("Processing in C")
        super().process()

class D(B, A):
    def process(self):
        print("Processing in D")
        super().process()

c_obj = C()
c_obj.process()
print("-" * 10)
d_obj = D()
d_obj.process()
```

<details> 
<summary>Possible Solution</summary> 

Output is as follows:

```
Processing in C
Processing in A
----------
Processing in D
Processing in B
```

</details> 

## Pass 3

### 43. Difficulty: Intermediate    

Create a Book class that has title and author attributes. Implement the magic methods `__str__` and `__eq__` for this class. The `__str__` method should return a string in the format "Title by Author", and the `__eq__` method should return True if two Book objects have the same title and author. Demonstrate that your implementation works.


<details> 
<summary>Possible Solution</summary> 
</details>


### 44. ​Difficulty: Intermediate    

Define a class `Vehicle` with an `__init__` method that accepts make and model as arguments. Create a `Car` class that inherits from `Vehicle` and adds a `wheels` attribute, setting it to `4`. The `Car` class's `__init__` method should properly initialize the attributes from the Vehicle class using `super()`. Provide a code sample that instantiates a Car object and prints its make, model, and wheels.

<details> 
<summary>Possible Solution</summary> 
</details>

### 45. Difficulty: Intermediate    

Write a class `Person` with a "private" attribute `_age`. Implement a getter and a setter for this attribute using the `@property` decorator. The setter should ensure that the age cannot be set to a negative number; if an attempt is made, it should raise a `ValueError`.

<details> 
<summary>Possible Solution</summary> 
</details>


### 46. Difficulty: Advanced    

Create a `ShoppingCart` class that can hold Item objects. The `ShoppingCart` should have a method `add_item` that takes an `Item` object and a `remove_item` method. The `Item` class should have name and price attributes. This demonstrates a "has-a" relationship (composition). Write the code for both classes and show how a ShoppingCart object would collaborate with `Item` objects.

<details> 
<summary>Possible Solution</summary> 
</details>

### ​47. Difficulty: Intermediate    

Explain polymorphism and provide a Python code example. Your example should include a function that can accept different types of objects (e.g., `Dog`, `Cat`, `Bird`), as long as they implement a common method (e.g., `speak`). The function should call this method on the object it receives.

<details> 
<summary>Possible Solution</summary> 
</details>

### 48. ​Difficulty: Advanced    

Create a custom exception class called `OutOfStockError`. Then, create a `VendingMachine` class that has a dictionary of items and their quantities. Implement a `dispense_item` method that takes an item name as an argument. If the item's quantity is 0, this method should raise the `OutOfStockError`. Show how you would call this method and handle the custom exception using a `try...except` block.

<details> 
<summary>Possible Solution</summary> 
</details>

## Pass 4, `__repr__`

### 49. Given the following class definition, implement the` __repr__` method so that it provides a developer-friendly, unambiguous string representation of a `Book` object. The representation should ideally be a valid Python expression that could be used to recreate the object.

```python
class Book:        
    def __init__(self, title, author):            
        self.title = title            
        self.author = author    
        
        # Example usage:    
        book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")    
        print(repr(book))    
        #Expected output:    
        #Book('The Hitchhiker's Guide to the Galaxy', 'Douglas Adams')
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 50. Consider a class named Gadget. Predict the output of `print(str(my_gadget))` and `print(repr(my_gadget))` in the following four independent scenarios:    

* Scenario A: Gadget has a `__str__` method but no `__repr__` method.    
* Scenario B: Gadget has a `__repr__` method but no `__str__` method.    
* Scenario C: Gadget has neither a `__str__` nor a `__repr__` method.    
* Scenario D: Gadget has both a `__str__` and a `__repr__` method.

<details> 
<summary>Possible Solution</summary> 
</details>

### 51. The `__repr__` method in the `Person` class below is incomplete. It doesn't correctly handle names that contain quote characters. 

When `repr()` is called on an instance like `p2`, the resulting string is not valid Python code for recreating the object. Modify the `__repr__` method to fix this, ensuring it produces a valid representation for all string inputs.

```python
class Person:        
    def __init__(self, name):            
        self.name = name        
        
    def __repr__(self):            
        # This implementation is flawed            
        return f"Person('{self.name}')"    
        
# Test cases:    
p1 = Person("Alice")    
p2 = Person("Bob O'Malley")    
print(repr(p1)) # Works as expected   
print(repr(p2)) # Produces invalid Python code
```

### 52. Advanced​: When implementing `__repr__`, it is a common best practice to use the `repr()` built-in function on the instance's attributes within the returned string. 

For example: `return f"Cat({repr(self.name)})"`. 

Explain why this practice is important for creating a robust and reliable representation of an object.

<details> 
<summary>Possible Solution</summary> 
</details>

### 53. Create a `Vector` class that represents a 2D vector. It should be initialized with `x` and `y` coordinates. Implement the `__repr__` method so it returns a string that can be used to recreate the vector object.

```python
class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # Your __repr__ method here

    # Example usage:
    v1 = Vector(2, 3)
    v2 = Vector(-1, 5)

print(v1) # Expected output: Vector(2, 3)
print(v2) # Expected output: Vector(-1, 5)
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 54. You are building a system to manage sports teams. Create a `Team` class that is initialized with a team name (a string) and a list of players (a list of strings). Implement the `__repr__` method to provide a clear representation of the Team object.

```python
class Team:
        def __init__(self, name, players):
            self.name = name
            self.players = players

        # Your __repr__ method here

    # Example usage:
    giants = Team("Giants", ["Eli Manning", "Odell Beckham Jr."])
    print(repr(giants))
    # Expected output:
    # Team('Giants', ['Eli Manning', 'Odell Beckham Jr.'])
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 55. A `Product` class needs two different string representations: a user-friendly one for customers and a developer-friendly one for debugging.    

* Implement `__str__` to return a formatted string like "`Name: $price`".    
* Implement `__repr__` to return a string that could be used to reconstruct the object.
* Observe the difference when you print a single object versus printing a list containing that object.

```python
class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        # Your __str__ method here

        # Your __repr__ method here


    # Example usage:
    book = Product("Python Crash Course", 29.99)
    products_list = [book]

    print(str(book))
    # Expected output for str(book):
    # Python Crash Course: $29.99

    print(repr(book))
    # Expected output for repr(book):
    # Product('Python Crash Course', 29.99)

    print(products_list)
    # Expected output for printing the list:
    # [Product('Python Crash Course', 29.99)]
```


<details> 
<summary>Possible Solution</summary> 
</details>


### 56. Advanced​: In this exercise, one class will contain an object of another custom class. 

You need to implement `__repr__` for both. Create an `Author` class and a `Book` class. A `Book` object should be initialized with a title and an `Author` object.

Ensure the `__repr__` of a `Book` object correctly represents the nested `Author` object.

<details> 
<summary>Possible Solution</summary> 
</details>

```python
class Author:        
    def __init__(self, name):            
        self.name = name        
    
    # Your __repr__ method for Author here  
      
class Book:        
    def __init__(self, title, author):             
        self.title = title           
        self.author = author     # author is expected to be an Author object     
        
        # Your __repr__ method for Book here    
        
        # Example usage:    
author = Author("J.R.R. Tolkien")    
book = Book("The Hobbit", author)    
print(repr(book))    # Expected output:    # Book('The Hobbit', Author('J.R.R. Tolkien'))

```

<details> 
<summary>Possible Solution</summary> 
</details>

### 57. Advanced​: You are creating an `InventoryItem` class for a warehouse management system. 

The class is initialized with a name (string), quantity (integer), and tags (a set of strings). Implement a `__repr__` method that correctly represents this object, paying close attention to how the set of tags is formatted.


```python
class InventoryItem:        
    def __init__(self, name, quantity, tags):            
        self.name = name            
        self.quantity = quantity            
        self.tags = tags        
        
    # Your __repr__ method here    

# Example usage:    
item = InventoryItem("Laptop", 15, {"electronics", "computer", "office"})   
# Note: The order of elements in a set is not guaranteed.    
# The repr() of the set might be in a different order, which is acceptable.    
print(repr(item))    
# Possible expected output (order of set elements may vary):    # InventoryItem('Laptop', 15, {'office', 'computer', 'electronics'})
```

<details> 
<summary>Possible Solution</summary> 
</details>


## Pass 5, Exceptions

### 58. Advanced: Custom Exception Hierarchy for Data Validation

Create a custom exception hierarchy for a data processing application.
1. Define a base exception class called `DataValidationError`.
2. Define two specific exception classes that inherit from `DataValidationError`: `MissingDataError` and `InvalidTypeError`.
3. Write a function `validate_user_data(data)` that takes a dictionary. 
    * It should raise `MissingDataError` if the required keys `'username'` or `'email'` are missing. 
    * It should raise `InvalidTypeError` if `'username'` or `'email'` are not strings.
4. If the data is valid, the function should return `True`.

Test cases:

```python
Valid data
try:
    print(validate_user_data({'username': 'testuser', 'email': 'test@example.com'}))
except DataValidationError as e:
    print(e)
# Expected: True

# Missing 'email'
try:
    validate_user_data({'username': 'testuser'})
except DataValidationError as e:
    print(f"Caught expected error: {type(e).__name__} - {e}")
# Expected: Caught expected error: MissingDataError - Missing required key: 'email'

# Invalid type for 'username'
try:
    validate_user_data({'username': 123, 'email': 'test@example.com'})
except DataValidationError as e:
    print(f"Caught expected error: {type(e).__name__} - {e}")
# Expected: Caught expected error: InvalidTypeError - 'username' must be a string.
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 59. Advanced: Resource Cleanup with `finally`

Simulate a resource connection (like a database or network socket) that must always be closed.vCreate a class `ResourceConnector` with `connect`, `process_data`, and `disconnect` methods. The `process_data` method should simulate a potential error. Write a function `process_resource(connector)` that ensures `disconnect` is always called, whether `process_data` succeeds or fails with an exception.

Test Cases:

```python
class ResourceConnector:
    def __init__(self, name):
        self.name = name
        self.connected = False

    def connect(self):
        print(f"Connecting to {self.name}...")
        self.connected = True

    def disconnect(self):
        print(f"Disconnecting from {self.name}...")
        self.connected = False

    def process_data(self, fail=False):
        if not self.connected:
            raise ConnectionError("Not connected.")
        if fail:
            print("Processing failed!")
            raise ValueError("Simulated processing error")
        print("Processing data successfully.")

def process_resource(connector, should_fail=False):
    # Your implementation here
    pass

# Successful run
res1 = ResourceConnector("DB1")
process_resource(res1, should_fail=False)

print("-" * 20)

# Failing run
res2 = ResourceConnector("API2")
process_resource(res2, should_fail=True)
```
Expected Output:

```
Connecting to DB1...
Processing data successfully.
Disconnecting from DB1...
--------------------
Connecting to API2...
Processing failed!
Disconnecting from API2...
Caught a processing error: Simulated processing error
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 60. Advanced: Exception Chaining

Write a function `load_config(config_dict)` that processes a configuration dictionary. If a required key `'db_host'` is missing, it should catch the `KeyError` and raise a new `ConfigurationError` that includes the original exception as its cause. This is known as exception chaining.

Test Cases:
```python
class ConfigurationError(Exception):
    """Error in application configuration."""
    pass

def load_config(config_dict):
    # Your implementation here
    pass

# Successful case
try:
    host = load_config({'db_host': 'localhost'})
    print(f"DB Host: {host}")
except ConfigurationError as e:
    print(e)

# Failing case
try:
    load_config({'user': 'admin'})
except ConfigurationError as e:
    print(f"Configuration Error: {e}")
    print(f"Original cause: {e.__cause__}")
```

Expected Output:
```
DB Host: localhost
Configuration Error: Missing required configuration key: 'db_host'
Original cause: 'db_host'
```

<details> 
<summary>Possible Solution</summary> 
</details>


### 61 Advanced: Advanced Setters with Multiple Exception Types

Create a `User` class with a `_email` attribute and a public email property. The setter for the email property must perform the following validations and raise the specified exceptions:

1. `Raise TypeError` if the value is not a string.
2. `Raise ValueError` if the string does not contain an @ symbol.
3. `Raise ValueError` if the string is less than 5 characters long.

Test Cases:

```python
class User:
    # Your implementation here
    pass

def create_user(email):
    try:
        user = User(email)
        print(f"User created with email: {user.email}")
    except (TypeError, ValueError) as e:
        print(f"Error: {type(e).__name__} - {e}")

create_user("test@example.com")
create_user(12345)
create_user("test.com")
create_user("a@b")
```

Expected Output:

```
User created with email: test@example.com
Error: TypeError - Email must be a string.
Error: ValueError - Email must contain an '@' symbol.
Error: ValueError - Email must be at least 5 characters long.
```

<details> 
<summary>Possible Solution</summary> 
</details>


### 62. Advanced: Refactoring a Poor Exception Handler

The following function uses a broad except clause that hides bugs and makes debugging difficult. Refactor `process_data` to handle `ValueError` and `IndexError` specifically with different messages, and let any other unexpected exceptions propagate.

Original Code:
```python
def process_data(data_list, index):
    try:
        value = int(data_list[index])
        result = 100 / value
        print(f"Result is {result}")
    except: # This is too broad
        print("An unspecified error occurred.")
```

**Refactored Function Signature**: `def process_data_refactored(data_list, index):`

Test Cases:

```python
# Should print "Invalid data format: cannot convert to integer."
process_data_refactored(['10', '20', 'abc'], 2)

# Should print "Invalid index: index is out of range."
process_data_refactored(['10', '20', '30'], 5)

# Should raise a ZeroDivisionError
try:
    process_data_refactored(['10', '0', '30'], 1)
except ZeroDivisionError as e:
    print(f"Caught an unexpected but specific error: {e}")
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 63. Advanced: Meaningful Use of the else Block

Write a function `attempt_connection()` that simulates trying to connect to a service. The connection attempt might raise a `TimeoutError`. If the connection is successful (no exception), the function should print `"Connection successful."` and then `"Processing data..."`. The `"Processing data..."` message must be in an `else` block to ensure it only runs on a successful connection attempt. A "Cleanup" message should always be printed.

Test Cases:

```python
def attempt_connection(should_fail=False):
    print("Attempting to connect...")
    try:
        if should_fail:
            raise TimeoutError("Connection timed out")
        # Simulate successful connection
    except TimeoutError as e:
        print(f"Error: {e}")
    # Your else/finally blocks here

attempt_connection(should_fail=False)
print("-" * 20)
attempt_connection(should_fail=True)
```

Expected Output:

```
Attempting to connect...
Connection successful.
Processing data...
Cleanup.
--------------------
Attempting to connect...
Error: Connection timed out
Cleanup.
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 64. Advanced: Custom Exception with Additional Context

Create a custom exception `TransactionError` that, in addition to a message, stores the `transaction_id` and an `error_code`.  Write a function p`rocess_transaction(tx_id, amount)` that raises this exception with relevant context if the amount is negative.

Test Cases:

```python
class TransactionError(Exception):
    # Your implementation here
    pass

def process_transaction(tx_id, amount):
    print(f"Processing transaction {tx_id}...")
    if amount < 0:
        raise TransactionError(
            "Transaction amount cannot be negative.",
            transaction_id=tx_id,
            error_code=101
        )
    print("Transaction successful.")

try:
    process_transaction("TX123", 100)
    process_transaction("TX456", -50)
except TransactionError as e:
    print(f"\nTransaction failed!")
    print(f"  Message: {e}")
    print(f"  Transaction ID: {e.transaction_id}")
    print(f"  Error Code: {e.error_code}")
```

Expected Output:

```
Processing transaction TX123...
Transaction successful.
Processing transaction TX456...

Transaction failed!
  Message: Transaction amount cannot be negative.
  Transaction ID: TX456
  Error Code: 101
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 65. Advanced: Selective Exception Handling and Re-raising


Write a function that processes a list of division operations. It should handle `ZeroDivisionError` by logging a warning but continuing. It should handle `TypeError` by stopping immediately but providing a specific error message. Any other exception should be caught and re-raised as a `RuntimeError`.

**Function Signature**: `def process_divisions(operations)`: where operations is a list of tuples (numerator, denominator).

Test Cases:

```python
def process_divisions(operations):    # Your implementation here    
    pass

ops1 = [(10, 2), (20, 5), (30, 0), (40, 8)]
print("--- Processing ops1 ---")
process_divisions(ops1)

ops2 = [(10, 2), (20, 'a'), (30, 5)]
print("\n--- Processing ops2 ---")
process_divisions(ops2)

ops3 = [(10, 2), (None, 5)]
print("\n--- Processing ops3 ---")
try:    
    process_divisions(ops3)
except RuntimeError as e:    
    print(f"Caught re-raised error: {e}")    
    print(f"Original cause: {e.__cause__}")
```

Expected Output:

```
--- Processing ops1 ---
Result: 5.0
Result: 4.0
Warning: Cannot divide by zero. Skipping operation (30, 0).
Result: 5.0
--- Processing ops2 ---
Result: 5.0
Error: Invalid type for division: unsupported operand type(s) for /: 'int' and 'str'
--- Processing ops3 ---
Result: 5.0
Caught re-raised error: An unexpected error occurred during division.
Original cause: unsupported operand type(s) for /: 'NoneType' and 'int'
```

<details> 
<summary>Possible Solution</summary> 
</details>