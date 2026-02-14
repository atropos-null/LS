# PY129 LSBOT Prep Questions

## Pass 7, James' Take

Prompt: Generate 20 intermediate and advanced problems that focus on the topics of: composition, duck typing, encapsulation, mix-ins, comparison / arithmetic magic methods.

Each problem must meet the dual constraints of "sophisticated design thinking" and "under 30 minute completion time" for a PY129 student. Each problem should come with examples of how the class should operate. Do not include problems that assume a "class has already been defined". Do not indicate the concepts being tested or the difficulty of the problem to the student, instead indicate the target amount of time it should take to complete the exercise for a PY129 student. Sort the problems easiest to hardest.

Afterwards, a follow up: Please convert this detailed feedback into a rating from 1 to 100. If I get above a 90 please discard the detailed feedback and instead for a rating between 90 to 95, provide 1 to 5 brief (20 words or less) short comings in my answer. Please include a brief (10 words or less) quote from the answer that references specifically where the short coming is found. If I score above a 95, provide my rating with no further feedback.

### 1. Target time to complete: 15-20 minutes

Create a Book class and a Library class. The Book class should be initialized with a title and an author. The Library class should be initialized with a name. The Library class should have a method to add a book and a method to list all the books it contains.

Example Usage:

```python
book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")

public_library = Library("City Central Library")
public_library.add_book(book1)
public_library.add_book(book2)

public_library.list_books()
# Expected Output:
# Books in City Central Library:
# - 1984 by George Orwell
# - Brave New World by Aldous Huxley
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 2. Target time to complete: 15-20 minutes

Create a BankAccount class that manages a balance. It should have methods to deposit, withdraw, and check the balance. The balance should be encapsulated, meaning it cannot be directly accessed or modified from outside the class. A withdrawal should not be permitted if it would result in a negative balance.

Example Usage:
```python
account = BankAccount(100)
print(account.get_balance())  # 100

account.deposit(50)
print(account.get_balance())  # 150

account.withdraw(75)
print(account.get_balance())  # 75

account.withdraw(100) # Should print an error message
print(account.get_balance())  # 75
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 3. Target time to complete: 15-20 minutes

Create a Person class that is initialized with a name and an age. Implement the necessary magic methods to allow Person objects to be compared based on their age. You should be able to check if two people are the same age, or if one is older than the other.

Example Usage:

```python
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 30)

print(person1 == person3) # True
print(person1 > person2)  # True
print(person2 < person3)  # True

```

<details> 
<summary>Possible Solution</summary> 
</details>

### 4. Target time to complete: 15-20 minutes

Create a Vector class to represent a 2D vector with x and y components. Implement the magic methods required to add and subtract two Vector objects. Adding two vectors should result in a new vector where the x and y components are the sum of the original vectors' components. Subtraction should work similarly.

Example Usage:

v1 = Vector(2, 4)
v2 = Vector(3, 1)

v3 = v1 + v2
print(v3) # Expected: Vector(5, 5)

v4 = v1 - v2
print(v4) # Expected: Vector(-1, 3)

<details> 
<summary>Possible Solution</summary> 
</details>

### 5. Target time to complete: 15-20 minutes

Create an HTMLRenderer class. It should have a render method that takes a list of document parts and prints their HTML representation. Create two simple classes, Header and Paragraph, that both have a to_html method. The render method should work with any object that has a to_html method.

Example Usage:

```python
class Header:
    def __init__(self, text):
        self.text = text
    def to_html(self):
        return f"<h1>{self.text}</h1>"

class Paragraph:
    def __init__(self, text):
        self.text = text
    def to_html(self):
        return f"<p>{self.text}</p>"

renderer = HTMLRenderer()
document_parts = [Header("Hello World"), Paragraph("This is a paragraph.")]
renderer.render(document_parts)
# Expected Output:
# <h1>Hello World</h1>
# <p>This is a paragraph.</p>
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 6. Target time to complete: 15-20 minutes

Create a Flyable mix-in that provides a fly method. Then, create a Bird class and an Airplane class. Both classes should use the Flyable mix-in to gain the ability to fly. The fly method should print a message indicating the object is flying.

Example Usage:

```python
# Flyable mix-in and Bird/Airplane classes to be defined here

sparrow = Bird("Sparrow")
boeing747 = Airplane("Boeing 747")

sparrow.fly()   # Expected: Sparrow is flying
boeing747.fly() # Expected: Boeing 747 is flying
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 7. Target time to complete: 15-20 minutes

Design a Car class that is composed of an Engine object. The Engine class should be initialized with a horsepower value. The Car class should be initialized with a make, model, and an Engine object. The Car class should have a start method that prints a message including the car's make, model, and the engine's horsepower. The Engine object should be an encapsulated detail of the Car.

Example Usage:

```python
# Engine and Car classes to be defined here

v8_engine = Engine(450)
mustang = Car("Ford", "Mustang", v8_engine)
mustang.start()
# Expected Output: The Ford Mustang starts with a 450 horsepower engine.
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 8. Target time to complete: 15-20 minutes

Create a Money class that stores an amount and a currency (e.g., 'USD', 'EUR'). Implement magic methods to allow for the addition of two Money objects and to check if they are equal. Addition should only be possible if the currencies are the same, otherwise it should raise an error. Two Money objects are equal if both their amount and currency are the same.

Example Usage:

```python
wallet1 = Money(20, 'USD')
wallet2 = Money(30, 'USD')
wallet3 = Money(20, 'EUR')

print(wallet1 + wallet2) # Money(50, 'USD')
print(wallet1 == wallet3) # False
# The following line should raise an error
# print(wallet1 + wallet3)
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 9. Target time to complete: 15-20 minutes

Create a Temperature class. Internally, it should store the temperature in Celsius. However, it should provide properties that allow getting and setting the temperature in Fahrenheit as well. The conversion formulas are: F = C * 9/5 + 32 and C = (F - 32) * 5/9. The internal storage in Celsius should be treated as a private detail.

Example Usage:

```python
temp = Temperature()
temp.celsius = 25
print(temp.fahrenheit) # 77.0

temp.fahrenheit = 32
print(temp.celsius)   # 0.0
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 10. Target time to complete: 15-20 minutes

Create a Walkable mix-in with a walk method. Create a Leg class. Create a Robot class that is composed of two Leg objects and also uses the Walkable mix-in. The walk method, when called on a Robot instance, should print a message indicating that the robot is walking on its two legs.

Example Usage:
```python
# Walkable, Leg, and Robot classes to be defined here

robot = Robot()
robot.walk()
# Expected Output: Robot is walking on its 2 legs.
```

<details> 
<summary>Possible Solution</summary> 
</details>


### 11.  Target time to complete: 15-20 minutes

Design a DataExporter class that takes a list of data objects and an exporter strategy object. Create JSONExporter and CSVExporter classes. Each must have an export method. The DataExporter's process method should call the export method on its strategy object, demonstrating duck typing.

Example Usage:

```python
# DataExporter, JSONExporter, CSVExporter classes to be defined here

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

json_exporter_strategy = JSONExporter()
csv_exporter_strategy = CSVExporter()

exporter = DataExporter(data, json_exporter_strategy)
exporter.process()
# Expected Output: Exporting data to JSON: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

exporter.set_strategy(csv_exporter_strategy)
exporter.process()
# Expected Output: Exporting data to CSV: name,age\nAlice,30\nBob,25
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 12. Target time to complete: 15-20 minutes

Model a Computer using composition. Create classes for CPU, RAM, and Storage. The Computer class should be composed of one instance of each of these component classes. The Computer should have a display_specs method that prints out the specifications of all its components.

Example Usage:

```python
# CPU, RAM, Storage, and Computer classes to be defined here

cpu = CPU("Intel i7", "3.4GHz")
ram = RAM(16, "DDR4")
storage = Storage(512, "SSD")

my_computer = Computer(cpu, ram, storage)
my_computer.display_specs()
# Expected Output:
# Computer Specs:
#   CPU: Intel i7 @ 3.4GHz
#   RAM: 16GB DDR4
#   Storage: 512GB SSD

```

<details> 
<summary>Possible Solution</summary> 
</details>


### 13. Target time to complete: 20-25 minutes

Create an ImmutablePoint class representing a 2D point. Its x and y coordinates should be set during instantiation and should not be changeable afterwards. If an attempt is made to modify a coordinate, the class should raise a custom AttributeError.
Also, implement __str__ to provide a user-friendly string representation.

Example Usage:

```python
# ImmutablePoint class to be defined here

p1 = ImmutablePoint(10, 20)
print(p1) # Expected: Point(10, 20)

# The following line should raise an AttributeError
# p1.x = 30
```

<details> 
<summary>Possible Solution</summary> 
</details>


### 14. Target time to complete: 20-25 minutes

Define a Mammal base class. Create two mix-ins: Swimmable and Walkable. Then, create a Whale class that inherits from Mammal and uses the Swimmable mix-in, and a Dog class that inherits from Mammal and uses the Walkable mix-in. Each mix-in should provide a method (swim or walk) that prints an appropriate message.

Example Usage:

```python
# Mammal, Swimmable, Walkable, Whale, and Dog classes to be defined here

moby_dick = Whale("Moby Dick")
moby_dick.swim()   # Expected: Moby Dick is swimming.

fido = Dog("Fido")
fido.walk()    # Expected: Fido is walking.
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 15. Target time to complete: 20-25 minutes

Design an Orchestra class that manages a collection of instruments. Any object with a play_note(note) method can be considered an instrument. Create Violin and Piano classes that adhere to this interface. The Orchestra should have a method play_piece which instructs all its instruments to play the note 'C'.

Example Usage:

```python
# Violin, Piano, and Orchestra classes to be defined here

violin = Violin()
piano = Piano()
orchestra = Orchestra()

orchestra.add_instrument(violin)
orchestra.add_instrument(piano)

orchestra.play_piece()
# Expected Output:
# Violin plays note C
# Piano plays note C
```

<details> 
<summary>Possible Solution</summary> 
</details>


### 16. Target time to complete: 20-25 minutes

Create a PlayingCard class that has a rank and a suit. Implement all six rich comparison magic methods (__lt__, __le__, __gt__, __ge__, __eq__, __ne__) to allow a list of PlayingCard objects to be sorted. Define a clear order for ranks (e.g., 2-10, J, Q, K, A) and suits (e.g., Clubs, Diamonds, Hearts, Spades).

Example Usage:

```python
# PlayingCard class to be defined here

card1 = PlayingCard('Queen', 'Hearts')
card2 = PlayingCard('King', 'Hearts')
card3 = PlayingCard('Queen', 'Spades')

print(card1 < card2) # True
print(card3 > card1) # True (assuming Spades > Hearts)

deck = [card2, card1, card3]
deck.sort()
print(deck) # [Queen of Hearts, King of Hearts, Queen of Spades] (or similar, based on defined sort order)
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 17. Target time to complete: 20-25 minutes

Implement a Fraction class that stores a numerator and a denominator. The class should ensure that fractions are always stored in their simplest form (e.g., initializing with 4 and 8 should store 1 and 2). This simplification logic should be an encapsulated part of the class. Implement the __add__ and __mul__ magic methods to perform fraction arithmetic.

Example Usage:

```python
# Fraction class to be defined here

f1 = Fraction(1, 2)
f2 = Fraction(2, 4) # Should be stored as 1/2
f3 = Fraction(1, 4)

print(f1 == f2) # True

f4 = f1 + f3 # 1/2 + 1/4 = 3/4
print(f4) # Fraction(3, 4)

f5 = f1 * f4 # 1/2 * 3/4 = 3/8
print(f5) # Fraction(3, 8)
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 18. Target time to complete: 20-25 minutes

Create a Trackable mix-in that adds created_at and updated_at timestamps to any class. The created_at timestamp should be set upon object creation and never change. The updated_at timestamp should be set upon creation and then updated every time any attribute of the instance is modified.

Example Usage:

```python

# Trackable mix-in to be defined here
import time

class User(Trackable):
    def __init__(self, name):
        super().__init__()
        self.name = name

user = User("Alice")
print(user.name, user.created_at, user.updated_at)
time.sleep(1)
user.name = "Alicia"
print(user.name, user.created_at, user.updated_at) # updated_at should be later than created_at
```

<details> 
<summary>Possible Solution</summary> 
</details>


### 19. Target time to complete: 20-25 minutes

Model a VendingMachine. It should be composed of multiple Slot objects. A Slot should contain an item name, its price, and its quantity. The state of each Slot (especially its quantity) should be encapsulated. The VendingMachine must provide a public purchase_item method that takes a slot number and an amount of money. This method should handle the logic of checking the price, checking the quantity, dispensing the item (printing a message), and reducing the quantity. Direct access to modify a slot's quantity from outside the machine should be prevented.

Example Usage:
```python
# Slot and VendingMachine classes to be defined here

slot1 = Slot("Cola", 1.50, 5)
slot2 = Slot("Chips", 1.00, 3)
machine = VendingMachine([slot1, slot2])

machine.purchase_item(0, 1.50) # Purchase Cola
# Expected: Dispensing Cola.

machine.purchase_item(1, 0.75) # Not enough money for Chips
# Expected: Insufficient funds.

machine.purchase_item(0, 2.00) # Purchase another Cola
# Expected: Dispensing Cola. Change: 0.50
```

<details> 
<summary>Possible Solution</summary> 
</details>

### 20. Target time to complete: 20-25 minutes

Create a Report class that is initialized with a title and a list of Section objects. Create a TextSection class and a TableSection class, both of which are types of Section. Each section must have a render() method that returns a formatted string. The Report class should have a generate() method that iterates through its sections and calls render() on each one, printing the result.[10:55 AM]This demonstrates composition and duck typing.

Example Usage:

```python
# Report, TextSection, TableSection classes to be defined here

intro = TextSection("This is the introduction to the quarterly report.")
financials = TableSection("Financials",
                          [["Revenue", "Expenses", "Profit"],
                           ["$1.2M", "$0.8M", "$0.4M"]])
conclusion = TextSection("This concludes the report.")

report = Report("Q3 Report", [intro, financials, conclusion])
report.generate()

# Expected Output:
# ========== Q3 Report ==========
#
# This is the introduction to the quarterly report.
#
# --- Financials ---
# | Revenue | Expenses | Profit |
# | $1.2M   | $0.8M    | $0.4M  |
#
# This concludes the report.
```

<details> 
<summary>Possible Solution</summary> 
</details>