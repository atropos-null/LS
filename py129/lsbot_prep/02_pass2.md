# PY 129 LS Bot Prep Questions

Each subheading starts a question but more questions related to it are in the body. Make sure to answer all of them!


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

The MRO is the precise path Python follows to look for a method. For class D, the MRO is:D -> B -> C -> A -> object.

You can verify this by printing `D.mro()`:

```python
class A: 
    
    def identify(self):
        print(f"I am {__class__.__name__}!")

class B(A): 
    
    def identify(self):
        
        print(f"I am {__class__.__name__}!")
        super().identify()

class C(A): 

    def identify(self):
        
        print(f"I am {__class__.__name__}!")
        super().identify()

class D(B, C): 

    def identify(self):
        
        print(f"I am {__class__.__name__}!")
        super().identify()

d = D()
d.identify()

#Output
#I am D!
#I am B!
#I am C!
#I am A!
```
</details>

### 23. **Difficulty: Advanced (Class vs. Instance Attributes)** 

Create a `Widget` class with a class attribute `widgets_created` that increments every time a new instance is created. 

It should also have an instance attribute for its name. Implement a class method that returns the total number of widgets created. Then, demonstrate how modifying the class attribute through an instance (`my_widget.widgets_created` = 5) can lead to unexpected behavior for future instances. Explain why this happens.

<details> 
<summary>Possible Solution</summary> 

```python
class Widget:    
    widgets_created = 0    
    
    def __init__(self, name):        
        self.name = name           
        self.__class__.widgets_created += 1    
        Widget.widget_created += 1
        
    @classmethod    
    def get_total_widgets(cls):        
        return cls.widgets_created
        
widget1 = Widget("One")
widget2 = Widget("Two")
print(f"Total widgets after creating two: {Widget.get_total_widgets()}") 
widget1.widgets_created = 50
print(f"Value for widget1: {widget1.widgets_created}")         # 50 
print(f"Value for widget2: {widget2.widgets_created}")         # 2  (Reads the class attribute)
print(f"Value from the class: {Widget.get_total_widgets()}") # 2  (Reads the class attribute)#
widget3 = Widget("Three")
print(f"Value for widget2 after new widget: {widget2.widgets_created}") # 3
print(f"Value for the class after new widget: {Widget.get_total_widgets()}") 
print(f"Value for widget1 remains unchanged: {widget1.widgets_created}") # 50
print(f"Value for total Widget: {Widget.widget_created}")
```

When you try to ​access​ an attribute on an instance (e.g., `widget2.widgets_created`), Python first checks for an instance attribute with that name. If it doesn't find one, it then looks for a class attribute.However, when you ​assign​ a value to an instance attribute (e.g., `widget1.widgets_created = 50`), Python creates a new attribute directly on that instance, regardless of whether a class attribute with the same name exists. This new instance attribute then "shadows" or hides the class attribute for that specific instance (`widget1`) only.

</details>

### 24. **Difficulty: Advanced (Encapsulation & Properties)** Design a `BankAccount` class. 

The account balance should be encapsulated using name mangling (__). 

Provide a read-only property to access the balance. Implement deposit and withdraw methods. The withdraw method must not allow the balance to go below zero; if an attempt is made, it should raise a custom `InsufficientFundsError`.

<details> 
<summary>Possible Solution</summary> 

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than {amount}")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance, amount)
        self.__balance -= amount
        return self.__balance
    
    def deposit(self, amount): 
        if not isinstance(amount, (int, float)) or amount <= 0: 
            raise ValueError("Amount must be a positive number.") 
        self.__balance += amount 
        return self.__balance

try:
    account = BankAccount(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Cannot withdraw: {e}")
    print(f"Current balance: {e.balance}")
```
</details>

### 25. **Difficulty: Advanced (Collaborator Objects)** Design and implement a `Deck` class and a `Card` class. 

A `Deck` should be initialized with 52 unique `Card` objects. 

The `Deck` class should "have" a list of `Card` objects as its primary instance variable. Implement shuffle and deal methods for the Deck. The deal method should remove and return the top card from the deck.

<details> 
<summary>Possible Solution</summary> 

```python
import random

class Card:
    SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
    RANKS = (
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

class Deck:
    def __init__(self):
        self.cards = [
            Card(suit, rank)
            for suit in Card.SUITS
            for rank in Card.RANKS
        ]
        self.shuffle_cards()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards: 
            return None
        return self.cards.pop()
```

</details>

### 26. **Difficulty: Advanced (str vs. repr)** Create a `Book class with title and author attributes. 

Implement both `__str__` and `__repr__` methods. 

The `__str__` method should return a user-friendly string (e.g., "To Kill a Mockingbird by Harper Lee"), while the `__repr__ `should return a developer-friendly string that could be used to recreate the object (e.g., `Book("To Kill a Mockingbird", "Harper Lee")`). Explain the primary use case for each method.

<details> 
<summary>Possible Solution</summary> 

```python

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)})"

harper_lee = Book("To Kill a Mockingbird", "Harper Lee")
print(str(harper_lee))
print(repr(harper_lee))
```
`__str__` is for user readability and `__repr__` is for developer friendly output to aid in recreating an object.

</details>

### 27. **Difficulty: Advanced (Custom Comparison)** Implement a Version class that ...

takes a version string like "2.1.15" as input. Override all rich comparison magic methods (`__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__`) to allow for correct comparison between Version objects. 

For example, Version("2.1.5") should be less than Version("2.2.0").

<details> 
<summary>Possible Solution</summary> 

```python
class Version:
    
    def __init__(self, version_string):
        self.version_string = version_string
        self.parts = tuple(int(p) for p in version_string.split("."))

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts == other.parts
    
    def __ne__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts != other.parts
    
    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts < other.parts
    
    def __le__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts <= other.parts
    
    def __gt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts > other.parts
    
    def __ge__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts >= other.parts
        
    def __repr__(self):
        return f"Version('{self.version_string}')"
    

version1 = Version("2.1.5")
version2 = Version("2.2.0")
print(version1 < version2) #True
```

</details>

### 28. **Difficulty: Advanced** Explain the difference between "is-a" and "has-a"

What is the difference between "is-a" relationship (inheritance) and the "has-a" relationship (composition/collaboration).

Provide a clear Python code example for both. For instance, model a Car, a Truck, a Vehicle, and an Engine. Justify your design choices regarding which relationships are "is-a" and which are "has-a".

<details> 
<summary>Possible Solution</summary> 

```python
class Engine: #Has a relationship with a vehicle
    
    def __init__(self, name):
        self.name = name

class Vehicle:
    
    def __init__(self, make, model, engine, wheels=4):
        self.make = make
        self.model = model
        self.engine = engine
        self.wheels = wheels

    def __str__(self):
        return f"This {self.make} {self.model} is a {self.__class__.__name__}."

class Car(Vehicle): #Is-a relationship with Vehicle
    
    def __init__(self, make, model, engine, wheels, classification):
        super().__init__(make, model, engine, wheels)
        self.classification = classification

class Truck(Vehicle): #Is-a relationship with Vehicle
    
    def __init__(self, make, model, engine, wheels, usecase):
        super().__init__(make, model, engine, wheels)
        self.usecase = usecase


electric_engine = Engine("2.0 L 4-cylinder Electric")
big_truck_engine = Engine("Cummins ISX15")

toyota_prius = Car("Toyota", "Prius", electric_engine, 4, "sedan") 
long_haul = Truck("Kenworth", "W900", big_truck_engine, 8, "heavy_duty")
print(str(toyota_prius))
print(str(long_haul))
```

</details>

### 29. **Difficulty: Advanced (Polymorphism & Duck Typing)** Write a render_elements(elements) function

Write a single function, `render_elements(elements)`, that iterates through a list of objects and calls a `.render()` method on each one. 

Create three distinct classes (`Button`, `TextField`, `Checkbox`) that do not share a parent class but each have a `.render()` method with a different implementation (e.g., printing what they are). Demonstrate that your function works polymorphically with a list containing instances of all three classes.

<details> 
<summary>Possible Solution</summary> 

```python


class Button:
    
    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Rendering a <button> for '{self.name}'.")

class TextField:

    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Rendering an <input type='text'> for '{self.name}'.")

class CheckBox:
    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Rendering an <input type='checkbox'> for '{self.name}'.")

button = Button("Submit Form")
field = TextField("Email Address")
text = CheckBox("Accept Terms and Conditions")

group = [button, field, text]

def render_elements(elements):
    for item in elements:
        item.render()
        
render_elements(group)

```

</details>

### 30. **Difficulty: Advanced (Static vs. Class Methods)** Create a class `MyDate`. 

Implement a class method `from_iso_format(date_string)` that takes a string like "2023-12-25" and returns a new `MyDate` instance. 

Implement a static method `is_valid_format(date_string)` that returns True or False depending on whether the date string is in a valid YYYY-MM-DD format. Explain precisely why a class method is appropriate for the first task and a static method is appropriate for the second.

<details> 
<summary>Possible Solution</summary> 

```python
class MyDate:
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_iso_format(cls, date_string):
        parts = date_string.split("-")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        return cls(year, month, day)

    @staticmethod
    def is_valid_format(date_string):
        # Check basic length: "YYYY-MM-DD" is exactly 10 characters
        if len(date_string) != 10:
            return False
        
        # Check if hyphens are in the correct positions
        if date_string[4] != "-" or date_string[7] != "-":
            return False
            
        # Extract components and ensure they are all digits
        year_part = date_string[0:4]
        month_part = date_string[5:7]
        day_part = date_string[8:10]
        
        return year_part.isdigit() and month_part.isdigit() and day_part.isdigit()


date_input = "2023-12-25"

if MyDate.is_valid_format(date_input):
    obj = MyDate.from_iso_format(date_input)
    print(f"Year: {obj.year}, Month: {obj.month}, Day: {obj.day}")
```

A class method is used here because it acts as a Factory. Its job is to create and return a new instance of the class using a different input format than the standard `__init__`. Access to the class: It receives the class itself as the first argument (cls). This allows the method to call cls(year, month, day) to create the object.

A static method is used  for is_valid_format because it is a Utility function that is logically related to the class but does not need to interact with it.

</details>

### 31. **Difficulty: Advanced (Custom Arithmetic)** Implement a `Vector` class 

The `Vector` class represents a 2D vector with x and y attributes. 

Override the `__add__` and `__sub__` magic methods to allow for vector addition and subtraction. Also, override `__mul__` to perform a scalar multiplication (e.g., my_vector * 3).

<details> 
<summary>Possible Solution</summary> 
</details>

### 32. **Difficulty: Advanced (Mix-ins)** Create a mix-in class called `LoggerMixin` 

`LoggerMixin` should be a log method which prints a message with the object's class name and memory address. 

Create two unrelated classes, `DatabaseConnection` and `FileSystemObject`, and demonstrate how you can add the logging functionality to both using the mix-in without using multiple inheritance from a common functional base class.

<details> 
<summary>Possible Solution</summary> 

```python
class LoggerMixin:
   
    def log(self, message):
        class_name = self.__class__.__name__
        memory_address = hex(id(self))
        print(f"[{class_name} at {memory_address}]: {message}")

class DatabaseConnection(LoggerMixin):
    def connect(self):
        self.log("Connecting to the production database...")

class FileSystemObject(LoggerMixin):
    def delete(self):
        self.log("Deleting temporary file from disk...")

# Demonstration
db = DatabaseConnection()
fs = FileSystemObject()

db.connect()
fs.delete()
```

</details>

### 33. **Difficulty: Advanced (Name Mangling)** What is name mangling in Python? 

Provide a code example using a class with an attribute prefixed with a double underscore (e.g., `__value`). Show how to access this attribute from outside the class using its mangled name. Explain why this feature is not for creating true private members and what its main purpose is.

<details> 
<summary>Possible Solution</summary> 

```python

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than {amount}")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance, amount)
        self.__balance -= amount
        return self.__balance
    
    def deposit(self, amount): 
        if not isinstance(amount, (int, float)) or amount <= 0: 
            raise ValueError("Amount must be a positive number.") 
        self.__balance += amount 
        return self.__balance
    

new_wallet = BankAccount(1000)
print(new_wallet.balance) #1000
new_wallet.balance = 500 # Attribute Error: property 'balance' of 'BankAccount' object has no setter
new_wallet._BankAccount__balance = 2000
print(new_wallet.balance) #2000
```

Name mangling is for **inheritance safety** and avoiding **name collisions**. It is not for making an attribute private.

</details>

### 34. **Difficulty: Advanced (`is` vs `==`)** Create a Point class with x and y attributes. 

Implement the `__eq__` method so that two Point instances are considered equal if their x and y values are the same. 

In your script, create two different Point objects with the same coordinates. Demonstrate that `point1 == point2` evaluates to `True`, while `point1 is point2` evaluates to `False`. Explain the output.

<details> 
<summary>Possible Solution</summary> 

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

point1 = Point(1, 2)
print(hex(id(point1))) #0x75cb5ead6900
point2 = Point(1, 2)
print(hex(id(point2))) #0x75cb5e9b4a50 


print(point1 == point2) #True Same values!
print(point1 is point2) #False Different ids!
```

</details>

### 35. **Difficulty: Advanced (Custom Exceptions)** Create a custom exception class `InvalidUsernameError`. 

Then, create a `User` class. 

In the `__init__` method, validate the username to ensure it is alphanumeric and between 4 and 16 characters long. If the validation fails, raise your `InvalidUsernameError` with an appropriate message.

<details> 
<summary>Possible Solution</summary> 

```python


class InvalidUsernameError(Exception):
    def __init__(self, username, message="Invalid username"):
        self.username = username
        super().__init__(f"{message}: '{username}'")

class User:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, name):
        if not (4 <= len(name) <= 16):
            raise InvalidUsernameError(name, "Username must be between 4 and 16 characters")
        if not name.isalnum():
            raise InvalidUsernameError(name, "Username must be alphanumeric (no spaces/symbols)")
        self._username = name
    
    def __str__(self):
        return f"Username: {self.username}"

try:
    gamora = User("Gamora")
    print(gamora) # Output: Username: Gamora

    uwe = User("Uwe") # This will raise the error (too short)
except InvalidUsernameError as e:
    print(f"Error caught: {e}")
```

</details>

### 36. **Difficulty: Advanced (Code Reading: Inheritance and State)** What is the output of the following code and why? 

Explain the state of each object and which speak method is called in each iteration.

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

```python
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

#Output:
#Fifi yips. Method override of the Dog and Animal speak method
#Rex barks. Method override of the Animal speak method
#Generic makes a sound. Animal method called.
```

</details>

### 37. **Difficulty: Advanced (Callable Objects)** Implement a `SequenceGenerator` class 

Instances of the class should be callable. Initialize the class with a start number and a step. Each time the instance is called, it should return the next number in the sequence. IGNORE THIS ONE. LSBOT WAS TRIPPING.

```Python
evens = SequenceGenerator(0, 2)
print(evens()) # Expected: 0
print(evens()) # Expected: 2
print(evens()) # Expected: 4
```

Which magic method must you implement to achieve this?

<details> 
<summary>Possible Solution</summary> 

```python
class SequenceGenerator:
    def __init__(self, start, step):
        self.current = start
        self.step = step

    def __call__(self):
        value_to_return = self.current
        self.current += self.step
        return value_to_return


evens = SequenceGenerator(0, 2)

print(evens()) # Output: 0
print(evens()) # Output: 2
print(evens()) # Output: 4
```

</details>

### 38. **Difficulty: Advanced (Scope and Inheritance)** Explain how inheritance influences attribute lookup in Python. 

Provide a code example with a base class and a derived class where the derived class accesses:

* An instance variable defined only in the base class's `__init__`.
* A class variable defined only in the base class.
* A method defined only in the base class.

<details> 
<summary>Possible Solution</summary>

```python
class Cerebro:

    number_of_episodes = 124

    def __init__(self, quote):
        self.quote = quote

    def best_quote(self):
        print(f"{self.quote}")

class Episode(Cerebro):
    pass

stryfe = Episode("Surprise bitch, I'm you!")
stryfe.best_quote()
print(stryfe.number_of_episodes)
```
</details>

### 39. **Difficulty: Advanced** Why is it considered a best practice to call `super().__init__()` within the `__init__` method of a subclass? 

What potential problems can arise if you fail to do so? Provide a simple code example with a multi-level inheritance hierarchy (A -> B -> C) to illustrate a problem where class C fails to initialize state from class A.

<details> 
<summary>Possible Solution</summary> 

```python
class A:
    def __init__(self):
        self.dna = "Stryfe-Prime"
        self.quote = "Surprise bitch, I'm you!"

    def __str__(self):
        return f"[{self.dna}] says: {self.quote}"

class B(A):
    def __init__(self):
        # B sets 'quote' but FORGETS to call super().__init__()
        # Therefore, 'self.dna' is NEVER created for B or its children.
        self.quote = "or that YOU'RE actually a clone of MEEEEEEEEEEE"

class C(B):
    def __init__(self):
        super().__init__()

# --- The Results ---

stryfe_a = A()
print(f"A works: {stryfe_a}")

try:
    stryfe_c = C()
    print(f"C works: {stryfe_c}") 
except AttributeError as e:
    print(f"C FAILED: Class B broke the chain, so {e}")
```

</details>

### 40. **Difficulty: Advanced (Properties for Validation)** Create a `Temperature` class that stores temperature in Celsius. 

Use a private `_celsius` attribute. Create a property fahrenheit with a getter and a setter. The getter should convert the Celsius temperature to Fahrenheit. The setter should take a Fahrenheit value, convert it to Celsius, and store it in the private `_celsius` attribute.

<details> 
<summary>Possible Solution</summary> 

```python
class Temperature:    
    
    def __init__(self, fahrenheit_value):        
        self.fahrenheit = fahrenheit_value  
        
        @property    
        def fahrenheit(self):        
            return (self._celsius * 9/5) + 32    
            
        @fahrenheit.setter    
        def fahrenheit(self, value):        
            self._celsius = (value - 32) * 5/9
```
</details>

### 41. **Difficulty: Advanced(Inhertance and Collaboration)** You are building a system for a library.

1. Create a `Writer` class that is initialized with a `name`.
2. Create a base class `Publication` that is initialized with a `title` and a `Writer` object (this is a "has-a" relationship/collaboration). It should have a display method that prints the title and the writer's name.
3. Create two subclasses that inherit from `Publication`: `Book` and `Magazine`.
    * Book should be initialized with a title, a writer, and a genre.
    * Magazine should be initialized with a title, a writer, and an issue_date.

4. Both `Book` and `Magazine` should override the display method. They must first call the parent class's display method using `super()` and then print their own specific information (genre for `Book`, issue date for `Magazine`).

5.  Finally, implement a custom `__str__` method for the Publication class that returns the string `"{title}" by {writer's name}`.

<details> 
<summary>Possible Solution</summary>

```python
class Writer:
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

class Publication:

    def __init__(self, title, writer):
        self.title = title
        self.writer = writer #dependency injection

    def display(self):
        # The display method prints the information
        print(f"Title: {self.title}")
        print(f"Writer: {self.writer.name}")

    def __str__(self):
        return f"{self.title} by {self.writer}"

class Book(Publication):

    def __init__(self, title, writer, genre):
        super().__init__(title, writer)
        self.genre = genre

    def display(self):
        # Call the parent's display method first
        super().display()
        print(f"Genre: {self.genre}")


class Magazine(Publication):

    def __init__(self, title, writer, issue_date):
        super().__init__(title, writer)
        self.issue_date = issue_date

    
    def display(self):
        # Call the parent's display method first
        super().display()
        print(f"Issue Date: {self.issue_date}")

    def __str__(self):
        super().__str__
        return f"{self.title} by {self.writer}. Issue Date: {self.issue_date}"
    

rachel_reid = Writer("Rachel Reid")
heated_rivalry = Book("Heated Rivalry", rachel_reid, "Romance")

national_geographic = Writer("The Editors of National Geographic")
secret_life = Magazine("The Secret Life of Cats", national_geographic, "September 2, 2022")

# Using the display method
heated_rivalry.display()
secret_life.display()

# Using the __str__ method (which is inherited by the subclasses)
print(str(heated_rivalry))
print(str(secret_life))
```
</details>

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

