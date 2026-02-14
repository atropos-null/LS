# PY129 LSBOT Exam Prep Questions


## Pass 3

### 43. Difficulty: Intermediate    

Create a Book class that has title and author attributes. Implement the magic methods `__str__` and `__eq__` for this class. The `__str__` method should return a string in the format "Title by Author", and the `__eq__` method should return True if two Book objects have the same title and author. Demonstrate that your implementation works.


<details> 
<summary>Possible Solution</summary> 

```python
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author
    

subtle_art1 = Book("The Subtle Art of Not Giving a F*ck", "Mark Manson")
subtle_art2 = Book("The Subtle Art of Not Giving a F*ck", "Mark Manson")
courage = Book("The Courage to be Disliked", "Ichiro Kishimi")

print(subtle_art1 == subtle_art2) #True
print(subtle_art2 == courage) #False
```

</details>


### 44. ​Difficulty: Intermediate    

Define a class `Vehicle` with an `__init__` method that accepts make and model as arguments. Create a `Car` class that inherits from `Vehicle` and adds a `wheels` attribute, setting it to `4`. The `Car` class's `__init__` method should properly initialize the attributes from the Vehicle class using `super()`. Provide a code sample that instantiates a Car object and prints its make, model, and wheels.

<details> 
<summary>Possible Solution</summary> 

```python
class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):

    def __init__(self, make, model):
        super().__init__(make, model)
        self.wheels = 4

    def __str__(self):
        return f"A {self.make} {self.model} has {self.wheels} wheels."
    

toyota_camry = Car("Toyota", "Camry")
print(str(toyota_camry))
```

</details>

### 45. Difficulty: Intermediate    

Write a class `Person` with a "private" attribute `_age`. Implement a getter and a setter for this attribute using the `@property` decorator. The setter should ensure that the age cannot be set to a negative number; if an attempt is made, it should raise a `ValueError`.

<details> 
<summary>Possible Solution</summary> 

```python


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be greater than 0")
        self._age = value

    def __str__(self):
        return f"{self.name} is {self.age}"

tommy = Person("Tommy", 10) #Tommy is 10
print(str(tommy))
embryo = Person("Unborn baby", -1) #ValueError: Age must be greater than 0

```
</details>


### 46. Difficulty: Advanced    

Create a `ShoppingCart` class that can hold Item objects. The `ShoppingCart` should have a method `add_item` that takes an `Item` object and a `remove_item` method. The `Item` class should have name and price attributes. This demonstrates a "has-a" relationship (composition). Write the code for both classes and show how a ShoppingCart object would collaborate with `Item` objects.

<details> 
<summary>Possible Solution</summary> 

```python
class Item:    
    
    def __init__(self, name, price):        
        self.name = name        
        self.price = price    
    
    def __str__(self):        
        return f"{self.name}"
    
    class ShoppingCart:    
        def __init__(self):        
            self.items = []    
            
        def add_item(self, item):        
            self.items.append(item)        
            print(f"Added {item.name} to cart.")    
        
        def remove_item(self, item):               
            if item in self.items:            
                self.items.remove(item)             
                print(f"Removed {item.name} from cart.")        
            else:            
                print(f"{item.name} is not in the cart.")    
                
        def view_cart(self):        
            if not self.items:            
                print("The cart is empty.")            
                return        
            print("Items in cart:")        
            for item in self.items:                        
                print(f"- {item.name}: ${item.price:.2f}")#
                
 cable = Item("USB-C Cable", 10.99)
 shampoo = Item("Shampoo", 5.50)
 socks = Item("Socks", 7.00)
 new_cart = ShoppingCart()
 new_cart.add_item(cable)
 new_cart.add_item(shampoo)
 new_cart.add_item(socks)
 new_cart.remove_item(socks)
 new_cart.view_cart()
 new_cart.remove_item(socks) #Test for error
 
```
</details>

### ​47. Difficulty: Intermediate    

Explain polymorphism and provide a Python code example. Your example should include a function that can accept different types of objects (e.g., `Dog`, `Cat`, `Bird`), as long as they implement a common method (e.g., `speak`). The function should call this method on the object it receives.

<details> 
<summary>Possible Solution</summary> 

Polymorphism means different objects respond to the same message in their own way.

```python
class Animal:

    def __init__(self, name):
        self.name = name

    def identify(self):
        print(f"I am a ")

    def speak(self):
        print(f"This {self.__class__.__name__} named {self.name} makes noises!")
    
class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"This {self.__class__.__name__} named {self.name}  makes barks!")

class Bird(Animal):

    def __init__(self, name):
        super().__init__(name)

    def make_sounds(self):
        print(f"This {self.__class__.__name__} makes chirps!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"This {self.__class__.__name__} named {self.name} makes chirps!")


animal = Animal("Bobby")
cat = Cat("Whiskers")
dog = Dog("Fido")
bird = Bird("Pete")

def make_animal_speak(animal_object):
    animal_object.speak()

animals = [animal, cat, dog, bird]
for animal in animals:
    make_animal_speak(animal)
```

</details>

### 48. ​Difficulty: Advanced    

Create a custom exception class called `OutOfStockError`. Then, create a `VendingMachine` class that has a dictionary of items and their quantities. Implement a `dispense_item` method that takes an item name as an argument. If the item's quantity is 0, this method should raise the `OutOfStockError`. Show how you would call this method and handle the custom exception using a `try...except` block.

<details> 
<summary>Possible Solution</summary> 

```python
class OutOfStockError(Exception):
    def __init__(self, message):
        super().__init__(message)

class VendingMachine:
    def __init__(self):
        self.items = {"O.B. tampons": 1000, 
                      "Apple 60W USB-C Charge Cable (1 m)": 10000, 
                      "Pampers Premium Diapers": 5000,
                      "Apple M5 MacBook Air": 0}
    
    def dispense_item(self, item_name):
        if item_name not in self.items:
            print(f"Item '{item_name}' not found.")
            return
        if self.items[item_name] == 0:
            raise OutOfStockError(f"The item '{item_name}' is currently unavailable.")
        
        self.items[item_name] -= 1
        print(f"Successfully dispensed {item_name}.")

vm = VendingMachine()

try:
    # Attempt to get the MacBook Air (which has 0 quantity)
    vm.dispense_item("Apple M5 MacBook Air")
except OutOfStockError as e:
    print(f"{e}")

try:
    vm.dispense_item("Pampers Premium Diapers")
except OutOfStockError as e:
    print(e)
```

</details>
