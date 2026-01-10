
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

### 1. **Difficulty: Advanced (MRO & `super()`)** Given the following multiple inheritance structure:

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

### 2. **Difficulty: Advanced (Class vs. Instance Attributes)** Create a `Widget` class with a class attribute `widgets_created` that increments every time a new instance is created. 

It should also have an instance attribute for its name. Implement a class method that returns the total number of widgets created. Then, demonstrate how modifying the class attribute through an instance (`my_widget.widgets_created` = 5) can lead to unexpected behavior for future instances. Explain why this happens.

<details> 
<summary>Possible Solution</summary> 
</details>

### 3. **Difficulty: Advanced (Encapsulation & Properties)** Design a `BankAccount` class. The account balance should be encapsulated using name mangling (__). 

Provide a read-only property to access the balance. Implement deposit and withdraw methods. The withdraw method must not allow the balance to go below zero; if an attempt is made, it should raise a custom `InsufficientFundsError`.

<details> 
<summary>Possible Solution</summary> 
</details>

### 4. **Difficulty: Advanced (Collaborator Objects)** Design and implement a `Deck` class and a `Card` class. A `Deck` should be initialized with 52 unique `Card` objects. 

The `Deck` class should "have" a list of `Card` objects as its primary instance variable. Implement shuffle and deal methods for the Deck. The deal method should remove and return the top card from the deck.

<details> 
<summary>Possible Solution</summary> 
</details>

### 5. **Difficulty: Advanced (str vs. repr)** Create a `Book class with title and author attributes. Implement both `__str__` and `__repr__` methods. 

The `__str__` method should return a user-friendly string (e.g., "To Kill a Mockingbird by Harper Lee"), while the `__repr__ `should return a developer-friendly string that could be used to recreate the object (e.g., `Book("To Kill a Mockingbird", "Harper Lee")`). Explain the primary use case for each method.

<details> 
<summary>Possible Solution</summary> 
</details>

### 6. **Difficulty: Advanced (Custom Comparison)** Implement a Version class that takes a version string like "2.1.15" as input. Override all rich comparison magic methods (`__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__`) to allow for correct comparison between Version objects. 

For example, Version("2.1.5") should be less than Version("2.2.0").

<details> 
<summary>Possible Solution</summary> 
</details>

### 7. **Difficulty: Advanced ("is-a" vs. "has-a")** Explain the difference between the "is-a" relationship (inheritance) and the "has-a" relationship (composition/collaboration).

Provide a clear Python code example for both. For instance, model a Car, a Truck, a Vehicle, and an Engine. Justify your design choices regarding which relationships are "is-a" and which are "has-a".

<details> 
<summary>Possible Solution</summary> 
</details>

### 8. **Difficulty: Advanced (Polymorphism & Duck Typing)** Write a single function render_elements(elements) that iterates through a list of objects and calls a `.render()` method on each one. 

Create three distinct classes (`Button`, `TextField`, `Checkbox`) that do not share a parent class but each have a `.render()` method with a different implementation (e.g., printing what they are). Demonstrate that your function works polymorphically with a list containing instances of all three classes.

<details> 
<summary>Possible Solution</summary> 
</details>

### 9. **Difficulty: Advanced (Static vs. Class Methods)** Create a class `MyDate`. Implement a class method from_iso_format(date_string) that takes a string like "2023-12-25" and returns a new `MyDate` instance. 

Implement a static method is_valid_format(date_string) that returns True or False depending on whether the date string is in a valid YYYY-MM-DD format. Explain precisely why a class method is appropriate for the first task and a static method is appropriate for the second.

<details> 
<summary>Possible Solution</summary> 
</details>

### 10. **Difficulty: Advanced (Custom Arithmetic)** Implement a `Vector` class that represents a 2D vector with x and y attributes. 

Override the `__add__` and `__sub__` magic methods to allow for vector addition and subtraction. Also, override `__mul__` to perform a scalar multiplication (e.g., my_vector * 3).

<details> 
<summary>Possible Solution</summary> 
</details>

### 11. **Difficulty: Advanced (Mix-ins)** Create a mix-in class called `LoggerMixin` that has a log method which prints a message with the object's class name and memory address. 

Create two unrelated classes, `DatabaseConnection` and `FileSystemObject`, and demonstrate how you can add the logging functionality to both using the mix-in without using multiple inheritance from a common functional base class.

<details> 
<summary>Possible Solution</summary> 
</details>

### 12. **Difficulty: Advanced (Name Mangling)** What is name mangling in Python? 

Provide a code example using a class with an attribute prefixed with a double underscore (e.g., `__value`). Show how to access this attribute from outside the class using its mangled name. Explain why this feature is not for creating true private members and what its main purpose is.

<details> 
<summary>Possible Solution</summary> 
</details>

### 13. **Difficulty: Advanced (`is` vs `==`)** Create a Point class with x and y attributes. Implement the `__eq__` method so that two Point instances are considered equal if their x and y values are the same. 

In your script, create two different Point objects with the same coordinates. Demonstrate that `point1 == point2` evaluates to `True`, while `point1 is point2` evaluates to `False`. Explain the output.

<details> 
<summary>Possible Solution</summary> 
</details>

### 14. **Difficulty: Advanced (Custom Exceptions)** Create a custom exception class `InvalidUsernameError`. Then, create a `User` class. 

In the `__init__` method, validate the username to ensure it is alphanumeric and between 4 and 16 characters long. If the validation fails, raise your `InvalidUsernameError` with an appropriate message.

<details> 
<summary>Possible Solution</summary> 
</details>

### 15. **Difficulty: Advanced (Code Reading: Inheritance and State)** What is the output of the following code and why? Explain the state of each object and which speak method is called in each iteration.

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

### 16. **Difficulty: Advanced (Callable Objects)** Implement a `SequenceGenerator` class where instances of the class are callable. 

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

### 17. **Difficulty: Advanced (Scope and Inheritance)** Explain how inheritance influences attribute lookup in Python. 

Provide a code example with a base class and a derived class where the derived class accesses:

* An instance variable defined only in the base class's `__init__`.
* A class variable defined only in the base class.
* A method defined only in the base class.

<details> 
<summary>Possible Solution</summary> 
</details>

### 18. **Difficulty: Advanced (`super()` in `init`)** Why is it considered a best practice to call `super().__init__()` within the `__init__` method of a subclass? 

What potential problems can arise if you fail to do so? Provide a simple code example with a multi-level inheritance hierarchy (A -> B -> C) to illustrate a problem where class C fails to initialize state from class A.

<details> 
<summary>Possible Solution</summary> 
</details>

### 19. **Difficulty: Advanced (Properties for Validation)** Create a `Temperature` class that stores temperature in Celsius. 

Use a private `_celsius` attribute. Create a property fahrenheit with a getter and a setter. The getter should convert the Celsius temperature to Fahrenheit. The setter should take a Fahrenheit value, convert it to Celsius, and store it in the private `_celsius` attribute.

<details> 
<summary>Possible Solution</summary> 
</details>

### 20. **Difficulty: Advanced(Inhertance and Collaboration)** You are building a system for a library.

1. Create a `Writer` class that is initialized with a `name`.
2. Create a base class `Publication` that is initialized with a `title` and a `Writer` object (this is a "has-a" relationship/collaboration). It should have a display method that prints the title and the writer's name.
3. Create two subclasses that inherit from `Publication`: `Book` and `Magazine`.
    * Book should be initialized with a title, a writer, and a genre.
    * Magazine should be initialized with a title, a writer, and an issue_date.

4. Both `Book` and `Magazine` should override the display method. They must first call the parent class's display method using `super()` and then print their own specific information (genre for `Book`, issue date for `Magazine`).

5.  Finally, implement a custom `__str__` method for the Publication class that returns the string `"{title}" by {writer's name}`.

### 21. **Difficulty: Advanced (Code Reading: MRO and `super()`)** Predict the output of the following code.

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

### Difficulty: Intermediate    

Create a Book class that has title and author attributes. Implement the magic methods `__str__` and `__eq__` for this class. The `__str__` method should return a string in the format "Title by Author", and the `__eq__` method should return True if two Book objects have the same title and author. Demonstrate that your implementation works.


<details> 
<summary>Possible Solution</summary> 
</details>


### ​Difficulty: Intermediate    

Define a class `Vehicle` with an `__init__` method that accepts make and model as arguments. Create a `Car` class that inherits from `Vehicle` and adds a `wheels` attribute, setting it to `4`. The `Car` class's `__init__` method should properly initialize the attributes from the Vehicle class using `super()`. Provide a code sample that instantiates a Car object and prints its make, model, and wheels.

<details> 
<summary>Possible Solution</summary> 
</details>

### Difficulty: Intermediate    

Write a class `Person` with a "private" attribute `_age`. Implement a getter and a setter for this attribute using the `@property` decorator. The setter should ensure that the age cannot be set to a negative number; if an attempt is made, it should raise a `ValueError`.

<details> 
<summary>Possible Solution</summary> 
</details>


### Difficulty: Advanced    

Create a `ShoppingCart` class that can hold Item objects. The `ShoppingCart` should have a method `add_item` that takes an `Item` object and a `remove_item` method. The `Item` class should have name and price attributes. This demonstrates a "has-a" relationship (composition). Write the code for both classes and show how a ShoppingCart object would collaborate with `Item` objects.

<details> 
<summary>Possible Solution</summary> 
</details>

### ​Difficulty: Intermediate    

Explain polymorphism and provide a Python code example. Your example should include a function that can accept different types of objects (e.g., `Dog`, `Cat`, `Bird`), as long as they implement a common method (e.g., `speak`). The function should call this method on the object it receives.

<details> 
<summary>Possible Solution</summary> 
</details>

### ​Difficulty: Advanced    

Create a custom exception class called `OutOfStockError`. Then, create a `VendingMachine` class that has a dictionary of items and their quantities. Implement a `dispense_item` method that takes an item name as an argument. If the item's quantity is 0, this method should raise the `OutOfStockError`. Show how you would call this method and handle the custom exception using a `try...except` block.

<details> 
<summary>Possible Solution</summary> 
</details>