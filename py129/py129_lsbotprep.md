
# PY129 LSBOT Exam Prep Questions

Each subheading starts a question but more questions related to it are in the body. Make sure to answer all of them!

## Pass 1

Based on the topics covered in PY120 and the Object Oriented Programming with Python book, here are 20 questions that cover the core concepts you'll need to understand for the PY129 assessment.   

### 1. **Conceptual**:  What is a class and what is an object in Python?  

Explain their relationship.  

<details>
<summary>Possible Solution</summary>

Classes are the instructions for creating objects. Within the class are the instructions that says kind of data (state) is expected and what kind of behavior each object will be able to hold and do, respectively. Objects are instances of the class. Each object has it's own specific state and will share the behavior with other instances of the class. If the a blueprint for the creation of a house is the Class, the house itself is the object.   Classes are scaffolding, objects are actors, and the behaviors (methods) are the conversations between actors.

</details>

### 2. **Conceptual**: What is the purpose of the `__init__` method in a Python class? 

What does the `self` parameter represent?

<details>
<summary>Possible Solution</summary>

The dunder __init__ method gives the instance the data details needed to give that instance its unique character. The self parameter represents that unique instance being referred to in code. 

</details>

### 3. **Conceptual**:  Explain the difference between a class attribute and an instance attribute. 

Provide a code example to demonstrate this difference.

<details>
<summary>Possible Solution</summary>


An instance attribute is the data in variables that are unique to the instance itself. A class attribute is the data in the variables unique to the class itself and is essentially a metadata that is available to all instances. In this case Pet._COUNT is a class attribute, which each instantiation updates the count. The other variables like self.breed and self.color are unique to each instance.

```python

class Pet:
    _COUNT = 0

    def __init__(self, name):
        self.name = name
        Pet._COUNT += 1

    def speak(self):
        print(f"{self.name} says hi!")

class Dog(Pet):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Pet):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
sparky = Dog("Sparky", "mutt")
pugsly = Dog("Pugsly", "pug")
whiskers = Cat("Whiskers", "tabby")
print(Pet._COUNT)
```

</details>

### 4. **Conceptual**:  Describe the differences between an instance method, a class method, and a static method.  

Provide a code example showing how to define and call each.  

<details>
<summary>Possible Solution</summary>

An instance method is the actions that each instance of a class can do. It may be `def rolls_over()`  in a `Pet` class or `def start_engine` in a `Vehicle` Class. It always receives the instance object itself as its first argument, conventionally named `self`. A class method is something that all members of the class can do regardless of their unique attributes, such as a `def speak()` in a Pet Class or a `def accumulate_mileage` in a Vehicle class. In this case the actions in the super class can be passed down to the instances. It always receives the instance object itself as its first argument, conventionally named self. A static method is a method that performs an action but doesn't maintain a state, such as "def show_rules()". It's important to note that @classmethod and @staticmethod are decorators needed to enact.

```python

class Game:

    def __init__(self, deal_count, players):
        self.deal_count = deal_count
        self.players = players

    @classmethod
    def play(cls):
        print(f"{cls.__name__}: Let's get ready to rumble")
    
    @staticmethod
    def show_rules():
        print(f"The first to run out of cards wins!")
    
class Uno(Game):

    def __init__(self, deal_count, players):
        super().__init__(deal_count, players)
        
    def deal_cards(self):
        print(f"Dealer deals {self.deal_count} cards to {self.players} players")

uno = Uno(7, 4)
uno.play()
uno.show_rules()
uno.deal_cards()
```
</details>

### 5. **Conceptual**: What is inheritance?  

Explain how a subclass inherits from a superclass and demonstrate with a simple code example.

<details>
<summary>Possible Solution</summary>

Inheritance defines an "Is-a" relationship between a Parent and Child class, allowing the child or subclass to acquire attributes from another class. The Parent class creates a common logic and the child class extends the logic, thereby creating a class heirarchy.

```python

class Vehicle:

    def __init__(self, engine, classification, wheels):
        self.engine = engine
        self.classification = classification
        self.wheels = wheels


class Car(Vehicle):

    def __init__(self, engine, classification, make, model):
        super().__init__(engine, classification, wheels=4, )
        self.make = make
        self.model = model

    def __str__(self):
        return f"A {self.make} {self.model} with a {self.engine} engine"
    
class Truck(Vehicle):
    def __init__(self, engine, classification, make, model):
        super().__init__(engine, classification, wheels=8)
        self.make = make
        self.model = model

    def __str__(self):
        return f"An {self.wheels}-wheeled {self.make} {self.model}"

camry = Car("hybrid", "sedan", "Toyota", "Camry")
zetro = Truck("diesel", "commercial", "Mercedes", "Zetro")
print(camry)
print(zetro)
```

</details>

### 6. **Conceptual**: What is method overriding? 

How can a method in a subclass call the overridden method from its superclass?

<details>
<summary>Possible Solution</summary>

In the MRO the lowest subclass is called first and will override the same method in its parent or grandparent class. 
One can either replace the behavior, as seen below, or to usePython's built-in `super()` function. `The super()` function returns a temporary proxy object that allows you to access methods from the superclass. This is useful when you want to ​extend​ the superclass's behavior, not just replace it.

```python
class Pet:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("An animal makes an animal noise!")

class Dog(Pet):

    def __init__(self, name, breed):
        super().__init__(name, breed)

    def speak(self):            
        print(f"{self.name} barks!")

class Cat(Pet):

    def __init__(self, name, breed):
        super().__init__(name, breed)

    def speak(self):            
        print(f"{self.name} meows!")


fido = Dog("Fido", "mutt")
whiskers = Cat("Whiskers", "stray")
turtles = Pet("Turtles", "swamp")
fido.speak() #Fido barks!
whiskers.speak() #Whiskers meows!
turtles.speak() #An animal makes an animal noise!
```

</details>

### 7. **Conceptual**: Explain Python's Method Resolution Order (MRO). 

How would you view the MRO for a specific class?

<details>
<summary>Possible Solution</summary>

The Method Resolution Order utilizes the C3 Linearization algorithm to determine the order in which it checks a class in its hierarchy to find a specific method and to decide on how to check when multiple inheritance is involved. 

```python

class A: 
    pass
class B(A): 
    pass
class C(A): 
    pass
class D(B, C): 
    pass
```

the order goes from D to B to C to A, thereby solving the diamond problem. 


You would use `.mro()` operator on the class. 
</details>

### 8. **Conceptual**: What is a mix-in class in the context of Python OOP? 

What problem does it solve?

<details>
<summary>Possible Solution</summary>

Mixins provide a "Can-Do" relationship as opposed to a "has-a" or a "is-a" relationship. It solves the problem of extends functionality without requiring instantiation or complicated hierarchies. It is also known as "interface inheritance".

</details>

### 9. **Conceptual**: Explain the concept of polymorphism in Python. 

How does it relate to "duck typing"?

<details>
<summary>Possible Solution</summary>

Polymorphism is the technique of different objects having a common interface for different underlying implementations. This means that what an object does is more important than the type of object it is. Duck Typing is a common means to implement polymorphism. Say you have a pizza and you need to cut it.  You could use a knife, or a pizza wheel. You could also use scissors. All three would react to "pizza_cut()" even though they are different objects.

```python
class Meal:    
    def __init__(self, pizza, tool):        
        self.pizza = pizza        
        self.tool = tool        
        print(f"Let's eat! We have a {self.pizza}.")    
        
    def cut_pizza(self):        
        # The Meal object calls the `cut` method on its tool.        
        # It doesn't care what kind of tool it is, only that it can `cut`.        
        self.tool.cut(self.pizza)
        
    class Pizza:    
        def __init__(self, flavor, size):        
            self.flavor = flavor        
            self.size = size    
        
        def __str__(self):        
            return f"{self.size} {self.flavor} pizza"
            
    #These classes are unrelated by inheritance, but both respond to `cut`.# This is duck typing.
        
        class PizzaWheel:    
            def cut(self, pizza):        
                print(f"Slicing the {pizza} with a pizza wheel!")
        
        class Knife:    
            def cut(self, pizza):        
                print(f"Cutting the {pizza} with a kitchen knife!")
                
        class Scissors:    
            def cut(self, pizza):        
                print(f"Snipping the {pizza} with utility scissors!")
                
    margarita = Pizza("margarita", "small")
    knife = Knife()
    scissors = Scissors()
    pizza_wheel = PizzaWheel()
    monday_meal = Meal(margarita, knife)
    monday_meal.cut_pizza() 
    tuesday_meal = Meal(margarita, scissors)
    tuesday_meal.cut_pizza() 
    wednesday_meal = Meal(margarita, pizza_wheel)
    wednesday_meal.cut_pizza() 
```

In this code example we have different implements cutting the pizza. `Knife`, `Scissors` and `PizzaWheel` are three separate objects all being used under the common interface of `cut_pizza`.

</details>

### 10. **Conceptual**: What is encapsulation? 

How does Python support it, and what is the purpose of name mangling (e.g., `__private_attribute`)?

<details>
<summary>Possible Solution</summary>

Encapsulation is two things. First it is the bundling of instance attributes with an object. Second, it is the hiding of an internal state from the public interface through the use of single underscore, and getter and setter methods. Name mangling is the addition of two underscores at the front of an attribute, such as `__private_atribute` which converts the name internally to `ClassName.__private_attribute`. This is to prevent subclass overriding. 

</details>

### 11. **Conceptual**: What is a collaborator object? 

Provide an example of two classes where one class uses an object of the other class as a collaborator. 

<details>
<summary>Possible Solution</summary>

A collaborator is an object that's methods are used by another object. The collaborator has to do more than exist, but to do something. 

```python
class Pizza:
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.size = size

    def __str__(self):
        return f"a {self.size} {self.flavor} pizza"
    
    def cut_pizza(self):
        print(f"Let's cut the {self.size} {self.flavor} pizza")
    
class Meal:
    def __init__(self, menu):
        self.menu = menu

    def eat(self):
        self.menu.cut_pizza() 
        # COLLABORATION: Meal uses the Pizza's data to print a message
        print(f"Now, let's eat {self.menu}!")


small_margarita = Pizza("margarita", "small")
lunch = Meal(small_margarita)
lunch.eat()
```

In this example the Pizza object is a collaborator for the Meal object. You see the collaboration happening in Menu.eat().

</details>

### 12. **Conceptual**: Explain the difference between the `is` and `==` operators when comparing two objects. 

When would you implement the `__eq__` method?

<details>
<summary>Possible Solution</summary>

By default, the `==` checks if two objects are identical objects, having the same identity descriptor. This is idential to the  `is` operator. If you want `==` to behave like it typically does with regards to evaluating if the value is the same, link in strings or floats and ints, then you need to implement the `__eq__` dunder method in your class.

</details>

### 13. **Conceptual**: What is the purpose of the `__str__` and `__repr__` dunder methods? 

What are the key differences between them?

<details>
<summary>Possible Solution</summary>

`__str__` is a string formated return geared for readibilty and `__repr__` enables a developer the details to recreate an object if necessary. If there is no `__str__`, then `__repr__ `is the fall back.
</details>

### 14. **Conceptual**: How can you define a "private" method or attribute in Python? 

What is the convention, and does it enforce true privacy?

<details>
<summary>Possible Solution</summary>

One defines a 'private' method through the use of a single underscore before the instance attribute name, like "self._name". This signals to developers that is logic should be handled internally and stay private, not accesible by the User.  With that said, there is no true private methods. Encapsulation through getters and setter properties can help slow it down, but nothing is bulletproof in Python.

</details>

### 15. **Coding**: Write a `Cat` class that is initialized with a name. 

The class should have one instance attribute, `name`, and one instance method, `speak`, which returns `"Meow!"`.

<details>
<summary>Possible Solution</summary>

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"
    
patches = Cat("Patches")
print(patches.speak())
```

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

`print(alex > bob)` prints out False and `print(bob > alex)` prints out True. This is a tricky question because the value of `bob` is actually Robert. So of course, the length of Robert is longer than the length of Alex. 
</details>

### 17. **Coding**: What is the output of the following code? 

Explain the role of the class attribute count.

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

The output is 3, as the count is incremented when each new instantation of an object occurs.

</details>

### 18. **Coding**: What does the following code print? 

Explain the method lookup path for `buddy.speak()`.

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

The code snippet prints out "Woof!". The method call is answered by the Dog Parent class and the Animal Grandparent class is not triggered. 

</details>

### 19. **Coding**: Create a Vehicle class and two subclasses, `Car` and `Motorcycle`. 

The Vehicle class should have attributes for make and model. The Car class should have an additional attribute for `num_doors`, and the Motorcycle class should have an additional attribute for `has_sidecar`.

<details> 
<summary>Possible Solution</summary> 

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar=False):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar


toyota_camry = Car("Toyota", "Camry", 4)
harley_davidson = Motorcycle("Harley", "Davidson", False)
```
</details>

### 20. **Coding**: Implement a `Wallet` class that holds `Cash` objects. 

The `Wallet` should be able to add `Cash` objects to it and report the total amount of money it contains. A `Cash` object should have currency and amount attributes. This demonstrates collaborator objects.

<details> 
<summary>Possible Solution</summary> 

```python
class Cash:
    def __init__(self, currency_type: str, amount: float):
        self.currency_type = currency_type
        self.amount = amount

class Wallet:
    def __init__(self):
        self._cash_list = []

    @property
    def balance(self) -> float:
        return sum(item.amount for item in self._cash_list)

    def add_cash(self, cash_item: Cash):
    
        if not isinstance(cash_item, Cash):
            raise ValueError("Can only add Cash objects to the wallet.")
        
        if cash_item.amount <= 0:
            raise ValueError("Cash amount must be a positive number.")
            
        self._cash_list.append(cash_item)

    def __str__(self):
        return f"Wallet contains {len(self._cash_list)} items. Total balance: {self.balance}"


my_wallet = Wallet()
ten_dollars = Cash("USD", 10.0)
twenty_euros = Cash("EUR", 20.0)
my_wallet.add_cash(ten_dollars)
my_wallet.add_cash(twenty_euros)
print(my_wallet) # Output: Wallet contains 2 items. Total balance: 30.0
```

</details>

### 20a. **Coding** `Wallet` part 2. Creating a Class with Properties

Improve on the `Wallet` Class.

1. The `Wallet` should be initialized with a starting balance. This balance should be stored in an instance variable that is intended for internal use only (follow Python's convention).
2. Implement a balance property that allows a user to get the value of the balance.
3. Implement a setter for the balance property. The setter should perform validation:
    * It must ensure the new balance is a non-negative number (integer or float).
    * If the new balance is invalid, it should raise a `ValueError` with an appropriate message.
4. Add an `add_money` method that takes an amount and adds it to the balance. This method should also validate that the amount being added is a positive number, raising a `ValueError` if not.

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

```python
class Wallet:
    def __init__(self, starting_balance: float = 0.0):
        self.balance = starting_balance

    @property
    def balance(self):

        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Balance must be a number (integer or float).")
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

    def add_money(self, amount: float):

        if not isinstance(amount, (int, float)):
            raise ValueError("Amount to add must be a number.")
        if amount <= 0:
            raise ValueError("Amount to add must be a positive number.")
        
        self.balance += amount

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

```python
class Pet:
    total_pets = 0 #Class Variable initiated to 0

    def __init__(self, name):
        self._name = name #Assigns name to Pet attribute
        self.__class__.total_pets += 1  #creates a shadow variable! THIS IS A TRAP
                                        #Fix to Pets.total_pets += 1

    def speak(self):
        return f"{self._name} makes a sound." #calls the Pet object to speak

    @classmethod
    def get_total_pets(cls):
        return f"There are {cls.total_pets} pets in total." #returns the current amount of total_pet objects via the class variable through a class method

class Dog(Pet):
    def speak(self):
        return f"{self._name} barks." #method overriding, prompting a bark

class Cat(Pet):
    def speak(self):
        return f"{self._name} meows." #method overriding, prompting a meow

# Code to analyze
pet1 = Dog("Fido") #Pet1 initialized, name Fido
pet2 = Cat("Whiskers") #Pet2 initialzied, name Whisker
pet3 = Dog("Rex") #Pet3 initialized, name Rex. 

# 3 total pet objects in circulation, but...

print(pet1.speak()) #method overriding, returning  Fido barks.
print(pet2.speak()) #method overriding, returning Whiskers meows.
print(Pet.get_total_pets()) #0 
print(Dog.get_total_pets()) #2
print(pet3.total_pets) #2 #only looks for dog numbers
```

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

## Pass 4, `__repr__`

### 49. Implement the `__repr__`

Given the following class definition, implement the` __repr__` method so that it provides a developer-friendly, unambiguous string representation of a `Book` object. The representation should ideally be a valid Python expression that could be used to recreate the object.

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

```python
class Book:

    def __init__(self, title, author): 
        self.title = title 
        self.author = author
        
    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)})"

# Example usage:    
book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams") 
print(repr(book)) 

#Expected output:    
#Book('The Hitchhiker's Guide to the Galaxy', 'Douglas Adams')
```

</details>

### 50. Consider a class named Gadget. 

Predict the output of `print(str(my_gadget))` and `print(repr(my_gadget))` in the following four independent scenarios:    

* Scenario A: Gadget has a `__str__` method but no `__repr__` method.    
* Scenario B: Gadget has a `__repr__` method but no `__str__` method.    
* Scenario C: Gadget has neither a `__str__` nor a `__repr__` method.    
* Scenario D: Gadget has both a `__str__` and a `__repr__` method.

<details> 
<summary>Possible Solution</summary> 

If class had both a __str__ and a __repr__ as in Scenario D, the following would be expected:
```python
  def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Gadget({repr(self.name)})"
    
    def __str__(self):
        return f"This is a {self.name}"
    
doohickey = Gadget("Doohickey")
print(repr(doohickey)) #Gadget('Doohickey')
print(str(doohickey)) # This is a Doohickey 
```

However, in Scenario A it has only a __str__ so you can expect:

```python
class Gadget:

    def __init__(self, name):
        self.name = name

    #def __repr__(self):
     #   return f"Gadget({repr(self.name)})"
    
    def __str__(self):
        return f"This is a {self.name}"
    
doohickey = Gadget("Doohickey")
print(repr(doohickey)) #<__main__.Gadget object at 0x7920ce5ce900>
print(str(doohickey)) # This is a Doohickey 
``` 

Without a __repr__, the object identity is given where the repr would have been. __str__ behaves normally. 

In Scenario B, the reverse is there, only a repr but not a str.

```python
class Gadget:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Gadget({repr(self.name)})"
    
    #def __str__(self):
     #   return f"This is a {self.name}"
    
doohickey = Gadget("Doohickey")
print(repr(doohickey)) #Gadget('Doohickey')
print(str(doohickey)) #Gadget('Doohickey')
```

In this case the str falls back to the repr who represents str. 

Scenario C, no repr, no str you get just the memory address

```python
class Gadget:

    def __init__(self, name):
        self.name = name

    #def __repr__(self):
    #    return f"Gadget({repr(self.name)})"
    
    #def __str__(self):
     #   return f"This is a {self.name}"
    
doohickey = Gadget("Doohickey")
print(repr(doohickey)) #<__main__.Gadget object at 0x7a84d6b2a900>
print(str(doohickey)) #<__main__.Gadget object at 0x7a84d6b2a900>
```
</details>

### 51. The `__repr__` method in the `Person` class below is incomplete. 

It doesn't correctly handle names that contain quote characters. 

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

<details> 
<summary>Possible Solution</summary> 

```python
class Person:        
    def __init__(self, name):            
        self.name = name        
        
    def __repr__(self):            
        # This implementation is flawed            
        return f"Person('{repr(self.name)}')"    
        
# Test cases:    
p1 = Person("Alice")    
p2 = Person("Bob O'Malley")    
print(repr(p1)) # Works as expected   
print(repr(p2)) # Produces invalid Python code
```
</details>

### 52. Advanced​: Why is `__repr__` important?

When implementing `__repr__`, it is a common best practice to use the `repr()` built-in function on the instance's attributes within the returned string. 

For example: `return f"Cat({repr(self.name)})"`. 

Explain why this practice is important for creating a robust and reliable representation of an object.

<details> 
<summary>Possible Solution</summary> 

```python
class Cat: 
    def __init__(self, name): 
        self.name = name 
        
    def __repr__(self): 
        return f"Cat({repr(self.name)})" 
        
# Test cases:    
whiskers = Cat("Whiskers") 
roger = Cat("Roger") 
print(repr(whiskers)) #Cat('Whiskers') 
print(repr(roger)) #Cat('Roger')
```

The call to `repr()` inside my `__repr__` method is not calling the `Cat.__repr__` method again. Instead, it's calling `repr()` on a different object—in this case, a string object (`self.name`).

When my code calls `print(repr(whiskers))`, Python's built-in `repr()` function is called with the book object as its argument.

The `repr()` function sees that `whiskers` is an instance of the `Cat` class. It then looks for and calls the `__repr__` method defined in the `Cat` class.

Inside `Cat.__repr__`, Python evaluates the f-string: `f"Cat({repr(self.name)})"`

To build this string, it must first execute `repr(self.name)`, `self.name `is a string.

Now, the built-in `repr()` function is called with a ​string object​ as its argument. Python then calls the `__repr__` method that belongs to the built-in str class.

The `str.__repr__` method does its job: it takes the string and returns a version of it surrounded by quotes, with any internal special characters escaped. 

This is a fundamental concept in object-oriented programming: the same operation `(repr)` behaves differently depending on the type of object it's acting upon.

</details>

### 53. Create a `Vector` class that represents a 2D vector. 

It should be initialized with `x` and `y` coordinates. Implement the `__repr__` method so it returns a string that can be used to recreate the vector object.

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

```python
class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
             return f"Vector({repr(self.x)}, {repr(self.y)})"

    # Example usage:
v1 = Vector(2, 3)
v2 = Vector(-1, 5)

print(v1) # Expected output: Vector(2, 3)
print(v2) # Expected output: Vector(-1, 5)
```

</details>

### 54. You are building a system to manage sports teams. 

Create a `Team` class that is initialized with a team name (a string) and a list of players (a list of strings). Implement the `__repr__` method to provide a clear representation of the Team object.

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

```python
class Team:
        def __init__(self, name, players):
            self.name = name
            self.players = players

        def __repr__(self):
              return f"Team({repr(self.name)}, {repr(self.players)})"

# Example usage:
giants = Team("Giants", ["Eli Manning", "Odell Beckham Jr."])
print(repr(giants))
```
</details>

### 55. A `Product` class needs two different string representations: 

It needs a user-friendly one for customers and a developer-friendly one for debugging.    

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

```python
class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __str__(self):
              return f"{self.name}: ${self.price}"

        def __repr__(self):
              return f"Product({repr(self.name)}, {repr(self.price)})"


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

</details>


### 56. Advanced​: In this exercise, one class will contain an object of another custom class. 

You need to implement `__repr__` for both. Create an `Author` class and a `Book` class. A `Book` object should be initialized with a title and an `Author` object.

Ensure the `__repr__` of a `Book` object correctly represents the nested `Author` object.

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

```python
class Author: 
    def __init__(self, name):
        self.name = name 
    
    def __repr__(self):
        return f"Author({repr(self.name)})"
    
class Book: 
    def __init__(self, title, author): 
        self.title = title 
        self.author = author  # author is expected to be an Author object     
        
    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)}"
        
# Example usage:    
author = Author("J.R.R. Tolkien") 
book = Book("The Hobbit", author) 
print(repr(book)) # Expected output:    # Book('The Hobbit', Author('J.R.R. Tolkien'))
```

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

```python
class InventoryItem: 
    def __init__(self, name, quantity, tags): 
        self.name = name 
        self.quantity = quantity
        self.tags = tags 
        
    def __repr__(self):
        return f"InventoryItem({repr(self.name)}, {repr(self.quantity)}, {repr(self.tags)})"


item = InventoryItem("Laptop", 15, {"electronics", "computer", "office"}) 
print(repr(item)) 
# Possible expected output (order of set elements may vary):    
# InventoryItem('Laptop', 15, {'office', 'computer', 'electronics'})
```
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

```python
class DataValidationError(Exception):
    
    def __init__(self, message):
        super().__init__(message)

class MissingDataError(DataValidationError):
    pass

class InvalidTypeError(DataValidationError):
    pass


def validate_user_data(data):
    def validate_user_data(data):
    required_keys = ['username', 'email']
    
    # Check for missing keys
    for key in required_keys:
        if key not in data:
            raise MissingDataError(f"Missing required key: '{key}'")
    
    # Check for invalid types
    for key in required_keys:
        if not isinstance(data[key], str):
            raise InvalidTypeError(f"'{key}' must be a string.")
            
    return True


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
    connector.connect()
    try:
        connector.process_data(fail=should_fail)
    finally:
        # This block ALWAYS runs, even if an exception occurs above
        connector.disconnect()

# Successful run
res1 = ResourceConnector("DB1")
process_resource(res1, should_fail=False)

print("-" * 20)

# Failing run
res2 = ResourceConnector("API2")
process_resource(res2, should_fail=True)
```

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

```python

class ConfigurationError(Exception):
    def __init__(self, message):
        super().__init__(message)


def load_config(config_dict):

    try:
        return config_dict['db_host']
    except KeyError as e:

        raise ConfigurationError(f"Config failed: '{e.args[0]}' is missing") from e


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

```python
class User:
    
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if "@" not in value:
            raise ValueError("Must have an @ symbol")
        if len(value) < 5:
            raise ValueError("Must be 5 characters or more")
        self._email = value
        
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

```python
def process_data_refactored(data_list, index):

    try:
        value = int(data_list[index])
        result = 100 / value
        print(f"Result is {result}")
    except ValueError as e:
        print("Invalid data format: cannot convert to integer.")
    except IndexError as e:
        print("Invalid index: index is out of range")


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

```python
def attempt_connection(should_fail=False):
    print("Attempting to connect...")
    try:
        if should_fail:
            raise TimeoutError("Connection timed out")
        # Simulate successful connection
    except TimeoutError as e:
        print(f"Error: {e}")
    else:
        print("Connection successful.")
        print("Processing data...")
    finally:
        print("Cleanup.")

attempt_connection(should_fail=False)
print("-" * 20)
attempt_connection(should_fail=True)
```

</details>

### 64. Advanced: Custom Exception with Additional Context

Create a custom exception `TransactionError` that, in addition to a message, stores the `transaction_id` and an `error_code`.  Write a function `process_transaction(tx_id, amount)` that raises this exception with relevant context if the amount is negative.

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

```python
class TransactionError(Exception):

    def __init__(self, message, transaction_id, error_code):
        super().__init__(message)
        self.transaction_id = transaction_id
        self.error_code = error_code
    

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

```python
def process_divisions(operations):
    for num, den in operations:
        try:
            result = num / den
            print(f"{num} / {den} = {result}")
            
        except ZeroDivisionError:
            print(f"Warning: Cannot divide {num} by zero. Skipping.")
            continue  # Moves to the next item in the list
            
        except TypeError as e:
            if isinstance(num, str) or isinstance(den, str):
                print(f"Stopping: Invalid input types (found a string: '{num}' or '{den}').")
                return # Stops the function immediately
            
            # If it's a TypeError but not a string (like 'None'), 
            # we treat it as an "any other exception" case.
            raise RuntimeError("A type-related processing error occurred.") from e
            
        except Exception as e:
            # 3. Any other exception: catch and re-raise as RuntimeError
            raise RuntimeError("An unexpected error occurred during processing.") from e

# --- Test Cases ---

ops1 = [(10, 2), (20, 5), (30, 0), (40, 8)]
print("--- Processing ops1 ---")
process_divisions(ops1)
# Result: Processes everything, skips (30, 0) with a warning.

ops2 = [(10, 2), (20, 'a'), (30, 5)]
print("\n--- Processing ops2 ---")
process_divisions(ops2)
# Result: Processes (10, 2), then stops immediately on 'a'.

ops3 = [(10, 2), (None, 5)]
print("\n--- Processing ops3 ---")
try: 
    process_divisions(ops3)
except RuntimeError as e: 
    print(f"Caught re-raised error: {e}") 
    print(f"Original cause: {repr(e.__cause__)}")
# Result: Processes (10, 2), then re-raises the None error as a RuntimeError.
```
</details>


## Pass 6

### Problem 1: Playlist Class

**Description**: Create a `Playlist` class that represents a music playlist. The class should be able to store and manage a collection of song titles.

Initialization:

* The `__init__` method should accept one required argument: the name of the playlist (a string).
* It should also accept an optional argument, songs, which is a list of initial song titles (strings). If not provided, the playlist should start empty.
* The `Playlist` object should maintain the state of the songs in the order they are in the list.


**Methods**:

* `add_song(song_title)`: Adds a new song title (string) to the end of the playlist.
* `now_playing()`: Returns the title of the current song. When a playlist is first created, the "current song" is the first song in the list. If the playlist is empty, this method should return None.
* `play_next()`: Advances to the next song in the playlist. The "current song" becomes the next one in the list. If the current song is the last one in the list, this method should loop back to the first song. If the playlist is empty, this method does nothing.

Inputs:
```python
# Input
    rock_hits = Playlist("Rock Hits", ["Stairway to Heaven", "Bohemian Rhapsody"])
    print(rock_hits.now_playing())
    rock_hits.play_next()
    print(rock_hits.now_playing())
    rock_hits.add_song("Hotel California")
    rock_hits.play_next()
    print(rock_hits.now_playing())

    # Output
    #Stairway to Heaven
    #Bohemian Rhapsody
    #Hotel California
```

```python
# Input
    favorites = Playlist("Favorites", ["Song A", "Song B"])
    favorites.play_next()
    print(favorites.now_playing())
    favorites.play_next() # Should loop back to the start
    print(favorites.now_playing())

    # Output
    Song B
    Song A
```
```python
# Input
    empty_playlist = Playlist("Empty")
    print(empty_playlist.now_playing())
    empty_playlist.play_next()
    print(empty_playlist.now_playing())
    empty_playlist.add_song("First Song")
    print(empty_playlist.now_playing())

    # Output
    None
    None
    First Song
```

Common Wrong Turns:

1. Using a mutable default argument (like `songs=[]`) in the `__init__` method signature, which can cause unexpected behavior where all playlists share the same initial song list.
2. Incorrectly managing the index for the current song, leading to `IndexError` or improper looping logic.

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 2: InventoryItem Class​*

**Description**: Design an InventoryItem class to represent an item in a store's inventory. Each item has a name, price, and quantity.

**Initialization (`__init__`)**:

1. The initializer must accept three arguments: name (string), price (float or integer), and quantity (integer).
2. During initialization, the method must perform the following validations:
    •   The price cannot be negative.
    •   The quantity cannot be negative.
3. If any of the validation checks fail, the initializer should raise a `ValueError` with an appropriate error message.
4. If validation passes, the initializer should set the corresponding instance variables.

Methods:

* `get_total_value()`: Returns the total value of the inventory item, calculated as price * quantity.
*  `__str__()`: Returns a user-friendly string representation of the item in the format: `"{name} - Price: ${price:.2f}, Quantity: {quantity}"`. The price should always be formatted to two decimal places.

I/O Examples:

1.  ​Successful instantiation and usage:
```   
 # Input
    item = InventoryItem("Laptop", 1200.50, 10)
    print(item)
    print(item.get_total_value())

    # Output
    Laptop - Price: $1200.50, Quantity: 10
    12050.0
```

 2.  ​Instantiation with invalid price:
 
 ```
 # Input
    try:
        item = InventoryItem("Keyboard", -50, 25)
    except ValueError as e:
        print(e)

    # Output
    Price cannot be negative.
```

3.  ​Instantiation with invalid quantity:
```
# Input
    try:
        item = InventoryItem("Mouse", 25, -5)
    except ValueError as e:
        print(e)

    # Output
    Quantity cannot be negative.
```    

**Common Wrong Turns**:

1.  Failing to raise a `ValueError`. Instead, some might print an error message or return `None`, which does not correctly prevent the object from being created in an invalid state.
2.  Implementing validation in separate methods instead of directly within `__init__`, which allows an invalid object to be created before the validation methods are called.

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 3: Initiation and `__init__`: Predict and Explain

Predict the output of the following code. Explain your prediction in detail, referencing the Python object model and instantiation process.

```python
class Document:
    def __init__(self, text):
        self.text = text

class Index:
    def __init__(self, name, document):
        self.name = name
        self.docs = [document]
        print(f"Index '{self.name}' created.")
        return self.docs

try:
    doc = Document("Python is a fun language.")
    idx = Index("Programming", doc)
    print(idx)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
```

<details> 
<summary>Hidden Trap</summary> 
Hidden trap is that `__init__` must return `None`, not a value. The constructor call will raise a `TypeError`.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 4: Debug the Code

The following code is intended to create a Dashboard that pulls a metric from a DataService. When dashboard.display_metric() is called, it should print the metric string provided by the service. However, the code raises an error. Identify the bug, explain why it occurs, and provide the corrected code.

Intended Behavior:

```python
# Expected output:
#
# Dashboard ready.
# Current Users: 541
```

Code with bug:
```python
class DataService:
    def get_metric(self):
        return "Current Users: 541"

class Dashboard:
    def __init__(self):
        self.service = DataService
        print("Dashboard ready.")

    def display_metric(self):
        metric = self.service.get_metric()
        print(metric)

dashboard = Dashboard()
dashboard.display_metric()
```


<details> 
<summary>Hint</summary> 
Internal Note: Hidden trap is the confusion between a class and an instance. `self.servic`e is assigned the DataService class, not an instance of it, causing a `TypeError` when the instance method `get_metric` is called on the class.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 5: Implement a Class

(Difficulty: Advanced)

You are given Engine and Wheel classes. Implement a Car class whose constructor accepts one Engine object and a list of four Wheel objects.

The Car instance should have an attribute description that is set during initialization.[10:36 AM]The description should be a string in the format: "A car with a X-horsepower engine and Y-inch wheels.", where X is the engine's horsepower and Y is the diameter of the first wheel in the list.

Provided Classes:

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheel:
    def __init__(self, diameter):
        self.diameter = diameter
 ```

 Examples:
 ```python
 # Example 1
engine1 = Engine(300)
wheels1 = [Wheel(18), Wheel(18), Wheel(18), Wheel(18)]
car1 = Car(engine1, wheels1)
print(car1.description)
# Expected Output: A car with a 300-horsepower engine and 18-inch wheels.

# Example 2
engine2 = Engine(550)
wheels2 = [Wheel(20), Wheel(20), Wheel(20), Wheel(20)]
car2 = Car(engine2, wheels2)
print(car2.description)
# Expected Output: A car with a 550-horsepower engine and 20-inch wheels.

# Example 3
engine3 = Engine(180)
wheels3 = [Wheel(16), Wheel(16), Wheel(16), Wheel(16)]
car3 = Car(engine3, wheels3)
print(car3.description)
# Expected Output: A car with a 180-horsepower engine and 16-inch wheels.
```


<details> 
<summary>Hint</summary> 

Internal Note: Hidden trap involves correctly accessing attributes of collaborator objects (`engine.horsepower`, `wheels[0].diameter`) within the ``__init__`` method to compose a new piece of state for the Car instance.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 6: Predict and Explain Output

Predict the output of the following code and explain why it produces that output. Your explanation should cover the roles of class and instance variables, and how attribute lookup works in the context of collaborator objects.

**class Template:**
```python
    style = 'Standard'

    def __init__(self, template_text):
        self.template_text = template_text

    def render(self, value):
        return f"{self.template_text}: {value} ({self.style})"

class Report:
    style = 'Brief'

    def __init__(self, text):
        self.text = text
        self.formatter = Template(text)

    def generate(self):
        # Is self.formatter.style the same as self.style?
        return self.formatter.render('Data')

report = Report("Sales Data")
print(report.generate())
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Attribute lookup on a collaborator object. Students might mistakenly think that `self.style` inside the Template.render method refers to the Report class's style attribute since the Template object is an instance variable of Report. The lookup, however, is confined to the Template instance (`self.formatter`) and its class.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 7: Debug the Code

The `DeviceManager` class is intended to track the total number of connected devices across all manager instances. However, the code below is not working as expected. Each manager seems to have its own independent count. Identify the bug, explain the flaw in its logic, and provide the corrected code.

Intended Behavior:
```python
manager1 = DeviceManager("Office")
manager1.add_device()
manager1.add_device()

manager2 = DeviceManager("Home")
manager2.add_device()

print(DeviceManager.device_count) # Expected: 3
print(manager1.device_count)       # Expected: 3
print(manager2.device_count)       # Expected: 3
```
Buggy Code:

```python
class DeviceManager:
    device_count = 0

    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self):
        self.device_count += 1 # This line is the problem
        self.devices.append(f"Device_{self.device_count}")
        print(f"{self.name} added a device. " \
              f"Total devices: {self.device_count}")

manager1 = DeviceManager("Office")
manager1.add_device() # Office added a device. Total devices: 1
manager1.add_device() # Office added a device. Total devices: 2

manager2 = DeviceManager("Home")
manager2.add_device() # Home added a device. Total devices: 1

print(DeviceManager.device_count) # Prints 0
```


<details> 
<summary>Hint</summary> 

Hidden Trap:​ The rebinding behavior of the `+=` operator on immutable types. When `self.device_count += 1 `is executed, it doesn't modify the class variable device_count. Instead, it creates a ​new instance variable​ named device_count on self that shadows the class variable. Subsequent access to `self.device_count` within that instance refers to the instance variable, not the shared class variable.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 8: Implement a Class

Implement a `Project` class that collaborates with `Task` objects. The `Project` class must have a class-level priority set to '`Low'`. An individual project instance can override this with its own priority level during initialization.

Create a `log_task` method that accepts a `Task` object. This method should return a string formatted as "`[PRIORITY] Project 'Project Name': Task 'Task Name'"` where [PRIORITY] is the project's instance-level priority if it exists, otherwise it defaults to the class-level priority.

Requirements:

1.  Project class with a class attribute priority = 'Low'.
2.  `__init__` method that accepts a name and an optional priority.
3.  `log_task` method that takes a `Task` object and returns the formatted log string.
4.  A simple `Task` class is provided for you.

Provided Code:

```python
class Task:
    def __init__(self, name):
        self.name = name


Examples:

# Your Project class implementation here

# --- Examples ---
task1 = Task("Review specifications")
task2 = Task("Deploy to production")

default_project = Project("Internal Tool")
urgent_project = Project("Client Hotfix", priority="High")

print(default_project.log_task(task1))
# Expected Output: [Low] Project 'Internal Tool': Task 'Review specifications'

print(urgent_project.log_task(task2))
# Expected Output: [High] Project 'Client Hotfix': Task 'Deploy to production'

print(default_project.priority)
# Expected Output: Low (accesses class attribute)
```



<details> 
<summary>Hint</summary> 

Hidden Trap:​ Incorrect assumption about attribute lookup fallback. A common mistake is to only access self.priority and assume it will automatically fall back to `Project.priority` if the instance attribute isn't set. While this is true for ​reading​ the attribute, the prompt's logic requires determining ​which​ priority to use explicitly. The most direct implementation requires checking for the instance attribute first and then accessing the class attribute (`self.__class__.priority`) as a fallback if it doesn't exist.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 9: Predict and Explain

Predict the output of the following code. Explain precisely why this output occurs, paying close attention to the roles of `cls` and `self` in the context of inheritance and collaboration.

```python
class Registry:
    _items = []

    @classmethod
    def register(cls, item):
        print(f"Registering to {cls.__name__}'s registry.")
        cls._items.append(item)

class Part(Registry):
    pass

class Product(Registry):
    pass

class Factory:
    def __init__(self, item_class):
        self.item_class = item_class

    def create_item(self, name):
        item = f"{self.item_class.__name__}: {name}"
        self.item_class.register(item)
        return item

part_factory = Factory(Part)
part_factory.create_item("Gear")

product_factory = Factory(Product)
product_factory.create_item("Robot")

print(Part._items)
```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted: Misunderstanding how a shared class-level attribute behaves when manipulated through different subclasses.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>) 

### Problem 10: Debug This Snippet

The `APIConnector` class is intended to connect to a service using settings provided by a Settings object. The `build_url` static method is a utility to construct a full URL from an endpoint. However, running this code raises an error. Identify the bug, explain the flawed assumption the original developer made, and rewrite the `APIConnector` class to fix it. The `build_url` method must remain a static method.

```python
class Settings:
    def __init__(self, base_url):
        self.base_url = base_url

class APIConnector:
    def __init__(self, settings):
        self.settings = settings

    @staticmethod
    def build_url(endpoint):
        # Intended behavior: return a URL like "https://api.example.com/users"
        base = self.settings.base_url
        return f"{base}/{endpoint}"

    def get_users(self):
        url = self.build_url("users")
        # ... logic to fetch data from url
        print(f"Fetching from: {url}")

config = Settings("https://api.example.com")
connector = APIConnector(config)
connector.get_users()
```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted: Incorrectly assuming a static method has access to the instance's context (self) or its attributes.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 11: Implement This Class

Implement a `FileAuditor` class that tracks file access events. The class must meet the following requirements:

* It is initialized with a filename (e.g., 'data.csv').
* An instance method `log_access(user)` adds a log entry for that specific file instance.
* A class method get_total_logs(returns an integer representing the total number of logs created across ​all​ `FileAuditor` instances.
* A `__str__` magic method that returns a formatted string for an instance, like 'Auditor for: data.csv'. This method must use a static helper method named `_format_report_name(name)` to generate the string.


```python
# Example Input/Output:

auditor1 = FileAuditor('document1.txt')
auditor1.log_access('user_a')
auditor1.log_access('user_b')

auditor2 = FileAuditor('document2.txt')
auditor2.log_access('user_c')

print(FileAuditor.get_total_logs())
# Expected Output: 3

print(auditor1)
# Expected Output:
# Auditor for: document1.txt

print(auditor2)
# Expected Output:
# Auditor for: document2.txt

```
<details> 
<summary>Hint</summary> 
Hidden Trap Targeted: Confusion about how to correctly invoke a static method from within an instance method (`__str__`) and managing both class and instance state simultaneously.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 12: Predict and Explain​*

Predict the output of the following code snippet and explain your reasoning, paying close attention to how attributes are handled and how state is shared or separated between objects.

```python
class Inventory:
    items = []

    def __init__(self, location):
        self.location = location

    def add_stock(self, item):
        self.items.append(item)

warehouse = Inventory('Warehouse')
store = Inventory('Store')

warehouse.add_stock('Laptop')
store.add_stock('Mouse')

print(f"Warehouse has: {warehouse.items}")
print(f"Store has: {store.items}")
```

<details> 
<summary>Hint</summary> 
Hidden Trap:​ Mutable Class Attributes vs. Instance Attributes.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 13: Debugging​

The following code is intended to allow a `Portfolio` to track the tasks of a `Project`. When a task is added to the `Project` via the `Portfolio`'s `add_task` method, the `Portfolio`'s view of the tasks (`portfolio.project_tasks`) should be updated. However, the code is buggy. Identify the bug, explain why the final state is incorrect, and describe how to fix it.

Intended Behavior:​ The final line should print `['Login Page']`, showing that the portfolio's reference to the project's tasks reflects the new addition.

```python
class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

class Portfolio:
    def __init__(self, project):
        self.project_tasks = project.tasks

    def add_task(self, project, task):
        # This line is buggy
        project.tasks = project.tasks + [task]

# --- Execution ---
p1 = Project("Website Redesign")
portfolio = Portfolio(p1)
portfolio.add_task(p1, "Login Page")

print(f"Project's tasks: {p1.tasks}")
print(f"Portfolio's tasks: {portfolio.project_tasks}")

```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Incorrect assumption that the `+` operator for lists mutates the left operand. This leads to attribute reassignment (`=`), which breaks the reference held by the collaborator object, rather than mutating the original object's state.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 14: Implementation​

Implement two classes, `ServiceLog` and `Car`. A `Car` instance is composed with a ServiceLog instance upon creation. The `Car` class must have a `drive(km)` method and a `service()` method.

* The drive method adds the kilometers driven to the car's total mileage.
* The service method logs the car's current mileage to its ServiceLog by calling the log's record_service method.
* The ServiceLog should store a list of these mileage logs.

Examples:
```python
#​Input:

log = ServiceLog()
car = Car(log)
car.drive(100)
car.service()
print(log.records)

#​Output: [100]
# Input:
log = ServiceLog()
car = Car(log)
car.drive(50)
car.drive(75)
car.service()
car.drive(25)
print(log.records)
print(car.mileage)
      
 #​Output: 
 # [125]
 # 150
    
 # Input:
log = ServiceLog()
car = Car(log)
car.service()
car.drive(30)
car.service()
car.drive(40)
car.service()
print(log.records)

#​Output: [0, 30, 70]
```    

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Correctly managing state through object collaboration, where one object (`Car`) is responsible for triggering state changes in a separate, contained object (`ServiceLog`).
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 15: Predict and Explain

Predict the output of the following code and explain your reasoning. Your explanation should detail how attribute lookup works, paying special attention to `self.__class__` and its role in accessing the nested `Config` class.

```python
class BaseWorker:
    class Config:
        priority = 'NORMAL'

    def display_priority(self):
        # Accesses the Config class via the instance's class
        print(self.__class__.Config.priority)

class UrgentWorker(BaseWorker):
    class Config:
        priority = 'HIGH'

worker = UrgentWorker()
worker.display_priority()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The `self.__class__` Late Binding Trap. When a method defined in a superclass is called on a subclass instance, `self.__class__` resolves to the subclass, not the superclass where the method is defined. This leads to accessing the subclass's version of the class attribute.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 15: Debugging

The `Scheduler` class uses a `Task` collaborator object. The class method `Scheduler.validate_task_class` is intended to check if a given task instance was created from the scheduler's ​default​ `Task` class (DefaultTask). However, the current implementation is flawed and produces an incorrect result. Identify the bug, explain why the comparison fails, and provide the corrected code.

**Intended Behavior**:

The code should print `False`, because `urgent_task` is an instance of `UrgentTask`, not `DefaultTask`. Instead, it currently prints `True`.

```python
class DefaultTask:
    pass

class UrgentTask:
    pass

class Scheduler:
    # This should store the class, but is storing an instance
    default_task_type = DefaultTask()

    @classmethod
    def validate_task_class(cls, task_instance):
        # Buggy line
        is_default = task_instance.__class__ is not cls.default_task_type
        print(not is_default)

# Setup
urgent_task = UrgentTask()
Scheduler.validate_task_class(urgent_task)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The `is` vs. `__class__` Identity Trap. The programmer incorrectly assumes that comparing `task_instance.__class__` with `cls.default_task_type` using is not will always work as intended. While it might work in simple cases, the real protocol for type checking is using `isinstance()` or direct class comparison (`__class__ == ...`). The bug here is that `cls.default_task_type` is actually an ​instance​ of the `DefaultTask`, not the class itself, so `task_instance.__class__` is being compared to an object, which is logically incorrect.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 16: Implementation

Implement the Document class according to the following requirements. It must track the total number of `Document` instances created using a class attribute. It must also support a "versioning" system via an instance method, `create_new_version()`, which returns a new document of the ​exact same class​ as the instance the method was called on. This behavior must be preserved in any subclasses.

Requirements:

1.  A class attribute count that is incremented each time a new instance of that specific class is created.
2.  An `__init__` method that properly increments the counter.
3.  An instance method `create_new_version(self)` that returns a new instance of the correct class.

Examples:

```python

# Example 1: Base class functionality
doc1 = Document()
doc2 = doc1.create_new_version()
print(f"Document count: {Document.count}")
# Expected: Document count: 2
print(f"doc2 is a Document: {isinstance(doc2, Document)}")
# Expected: doc2 is a Document: True

# Example 2: Subclass functionality
class SignedDocument(Document):
    count = 0 # Subclass gets its own counter

signed_doc1 = SignedDocument()
signed_doc2 = signed_doc1.create_new_version()
print(f"SignedDocument count: {SignedDocument.count}")
# Expected: SignedDocument count: 2
print(f"Base document count is unchanged: {Document.count}")
# Expected: Base document count is unchanged: 2
print(f"signed_doc2 is a SignedDocument: {isinstance(signed_doc2, SignedDocument)}")
# Expected: signed_doc2 is a SignedDocument: True
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The Hardcoded Constructor Trap. A naive implementation of create_new_version might hardcode return `Document()`. This would fail the requirement for subclasses, as calling `create_new_version()` on a `SignedDocumen`t instance would incorrectly return a Document instance, and it would increment the wrong counter. The solution requires using `self.__class__()` to instantiate the new object.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 17: Predict and Explain Output​

Predict the output of the following Python code snippet. Explain step-by-step why the output is what it is, paying close attention to how the `system.component_status` property interacts with the `Component` object and influences the system.readiness property.

```python
class Component:
    def __init__(self, status='offline'):
        self._status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status

class System:
    def __init__(self):
        self._component = Component()

    @property
    def readiness(self):
        return f"System readiness: {self._component.status}"

    @property
    def component_status(self):
        return self._component.status

    @component_status.setter
    def component_status(self, new_status):
        self._component.status = new_status

system = System()
print(system.readiness)

system.component_status = 'online'
print(system.readiness)
```

<details> 
<summary>Hint</summary> 


Hidden Trap Targeted:​ This prompt targets the misunderstanding that properties only manage an object's immediate instance variables. Here, a property setter on the System object acts as an interface to modify the state of a separate, internal collaborator object (`_component`).

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 18: Debugging​

The code below is intended to create a `Report` class that collaborates with a `Log` object. Every time the `report.content` is updated, the change should be automatically recorded in `report.log.entries`. However, running the code raises a `RecursionError`. Identify the bug, explain its cause, and provide the corrected Report class definition.

Intended Behavior:

* A Report object is initialized with some content. This first assignment is logged.
* When report.content is reassigned, the new content is stored, and a new entry is added to the log.
* The final print statement should output ['Content updated to: "Initial report."', 'Content updated to: "Revised report."'].

```python
# BUGGY CODE
class Log:
    def __init__(self):
        self.entries = []

    def add_entry(self, data):
        self.entries.append(data)

class Report:
    def __init__(self, initial_content):
        self.log = Log()
        self.content = initial_content

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, new_content):
        self.log.add_entry(f'Content updated to: "{new_content}"')
        self.content = new_content

report = Report("Initial report.")
report.content = "Revised report."
print(report.log.entries)
```

<details> 
<summary>Hint</summary> 


Hidden Trap Targeted:​ This prompt targets the common mistake of causing infinite recursion within a property. The incorrect assumption is that assigning to `self.content` inside the setter will behave like a normal attribute assignment, when in fact it re-invokes the setter method itself.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 19: Implementation​*

Implement a class named `ManagedResource`. This class must collaborate with a Settings object, which is passed during instantiation. The `Settings` class is provided for you.

Your `ManagedResource` class must have a host property that provides a getter and setter interface for the 'host' key within its Settings collaborator's config dictionary.

* The host getter should retrieve the value of 'host' from the Settings object's config dictionary.
* The host setter must validate that the new value is a string containing at least one dot (`.`). If validation fails, it must raise a `ValueError`. If validation passes, it should update the value of 'host' in the Settings object's config dictionary.

```python
# Provided class - DO NOT MODIFY
class Settings:
    def __init__(self, initial_config):
        self.config = initial_config

    def get(self, key):
        return self.config.get(key)

# Your implementation of ManagedResource goes here

# --- Input/Output Examples ---
# Example 1
settings1 = Settings({'host': 'localhost', 'port': 8080})
resource1 = ManagedResource(settings1)
resource1.host = 'api.example.com'
print(resource1.host)          # Expected: api.example.com
print(settings1.get('host'))   # Expected: api.example.com

# Example 2
settings2 = Settings({'host': 'server1'})
resource2 = ManagedResource(settings2)
try:
    resource2.host = 'invalid-host'
except ValueError:
    print("ValueError caught!") # Expected: ValueError caught!
print(resource2.host)          # Expected: server1

# Example 3
settings3 = Settings({'host': 'db.internal.net'})
resource3 = ManagedResource(settings3)
print(resource3.host)          # Expected: db.internal.net
```


<details> 
<summary>Hint</summary> 

Hidden Trap Targeted:​ This prompt targets the failure to correctly delegate state management to a collaborator. A common mistake is to create a backing instance variable (e.g., `_host`) on the `ManagedResource` instance itself, rather than modifying the dictionary within the shared `Settings` object as required. The I/O examples verify that the collaborator's state is the one being changed.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 20: Predict and Explain Code Output


Predict the output of the following code snippet. Provide a detailed explanation for each line of output, focusing on how inheritance and name mangling affect attribute access.

```python
class Component:
    def __init__(self):
        self.__id = 'C-123'

    def get_id(self):
        return self.__id

class System(Component):
    def __init__(self):
        super().__init__()
        self.__id = 'S-456'

    def get_component_id(self):
        return super().get_id()

    def get_system_id(self):
        return self.__id

sys = System()
print(sys.get_component_id())
print(sys.get_system_id())
print(sys._System__id)
print(sys._Component__id)
```
<details> 
<summary>Hint</summary> 

Hidden Trap Targeted​: This prompt targets the misconception that a double-underscore attribute in a subclass overrides the one in its parent class. Due to name mangling, `System.__id` and `Component.__id` become distinct attributes (`_System__id` and `_Component__id`) on the sys instance, coexisting without collision.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 21: Debug Code


The following code is intended to allow the addition of two `Wallet` objects using the `+` operator. The expected behavior is for the final line to print `Wallet` with balance: `350`. However, the line `combined_wallet = wallet1 + wallet2` currently raises a `TypeError`. Identify the bug and provide the corrected code.

```python
# Intended behavior: The code should add the balances of two
# Wallet objects using the `+` operator and print the new
# wallet's representation, which should be "Wallet with balance: 350".

class Wallet:
    def __init__(self, amount):
        self._balance = amount

    # This method is intended to overload the `+` operator.
    def __add__(self, other):
        return Wallet(self._balance + other._balance)

    def __repr__(self):
        return f"Wallet with balance: {self._balance}"

wallet1 = Wallet(100)
wallet2 = Wallet(250)

# This line raises a TypeError. Fix the Wallet class.
combined_wallet = wallet1 + wallet2
print(combined_wallet)

```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted​: This prompt exploits the reasonable but incorrect assumption that all methods starting and ending with double underscores (dunder methods) are subject to name mangling. Python's data model hooks (special methods like `__add__` and `__repr__`) are looked up by the interpreter by their exact names and are exempt from mangling. The bug is naming the method `__add__`, which gets mangled to `_Wallet__add__`, a name the `+` operator does not look for.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 22: Implement a Class

Implement the `AccessLogger` class based on its usage within the `APIClient` class. Your implementation must ensure the provided example code runs without errors and produces the exact output shown. The `APIClient` and `AccessLogger` classes have a composition relationship.

```python
class APIClient:
    def __init__(self, logger):
        self._logger = logger # Has-a relationship

    def make_request(self, url):
        self._logger.log_access(url)
        print(f"Request to {url} successful.")

        # This MUST access the logger's name-mangled attribute.
        count = self._logger._AccessLogger__requests_count
        print(f"Total requests logged: {count}")

# Implement the AccessLogger class below this line.
# It must have:
# 1. An initializer that accepts a filename.
# 2. An attribute for the filename that is accessible externally.
# 3. A private counter for requests that is accessed by APIClient.
# 4. A method to log access attempts.



# Example Usage:
logger = AccessLogger("system.log")
client = APIClient(logger)

client.make_request("api/users")
# Expected Output:
# Attempting to access: api/users
# Request to api/users successful.
# Total requests logged: 1

client.make_request("api/data")
# Expected Output:
# Attempting to access: api/data
# Request to api/data successful.
# Total requests logged: 2

print(logger._log_file)
# Expected Output:
# system.log
```

<details> 
<summary>Hint </summary> 

Hidden Trap Targeted​: This prompt forces the developer to deduce the required attribute names and protection levels from a collaborating object's implementation. The `APIClient`'s direct access to `_AccessLogger__requests_count` dictates that the logger's attribute must be named `__requests_count`. Likewise, the direct access to `logger._log_file `dictates that this attribute must be named `_log_file`, testing the understanding of both conventions in a practical context.
</details>

### Problem 23: Predict Code Output

Predict the output of the following code. Explain precisely what happens when `processor.process_all()` is called and why that output is produced.

```python
class Report:
    def __init__(self, content):
        self._content = content

    def __format(self):
        return f"Report content: {self._content}"

class Logger:
    def process_all(self, reports):
        for report in reports:
            try:
                # Intended to call a private formatting method
                print(report.__format())
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

report1 = Report("Annual data.")
report2 = Report("Quarterly data.")
processor = Logger()
processor.process_all([report1, report2])
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Name Mangling. Python's name mangling (_ClassName__methodName) prevents an external object (Logger) from accessing a "private" method of another object (Report) using the double underscore syntax directly.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 24: Debug Code

The `EventBroadcaster` is intended to send notifications from various sources (`EmailSource`, `SMSSource`) by calling a notify interface on them. The current code fails with a TypeError when processing the `SMSSource`. Identify the bug in the `SMSSource` class, explain why it breaks the polymorphic interface, and provide a corrected version of that class only.

Intended Behavior:
* Calling `broadcaster.broadcast()` should print:
    * Emailing: User subscribed 
    * Texting: Your code is 1234

```python
class EmailSource:
    def notify(self, message):
        print(f"Emailing: {message}")

class SMSSource:
    @property
    def notify(self): # BUG IS HERE
        return lambda message: print(f"Texting: {message}")

class EventBroadcaster:
    def __init__(self, sources):
        self.sources = sources
        self.messages = ["User subscribed", "Your code is 1234"]

    def broadcast(self):
        for source, msg in zip(self.sources, self.messages):
            source.notify(msg)

sources = [EmailSource(), SMSSource()]
broadcaster = EventBroadcaster(sources)
broadcaster.broadcast()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Confusing a property with a method. The @property decorator makes notify an attribute that returns a lambda function, but it is not a directly callable method on the instance itself. The broadcaster calls `source.notify(msg)`, which fails because it tries to pass an argument to a property accessor, not a method.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 25: Implement a Class

Implement an Inventory class that manages a collection of items.

* The constructor should accept a dictionary where keys are item names (strings) and values are quantities (integers).
* The class must support the `+` operator to combine two Inventory objects.
* The result should be a ​new​ Inventory object.
* When combining, if an item exists in both inventories, their quantities should be summed.

Examples:
```python
# Example 1
inv1 = Inventory({'screws': 100, 'nails': 50})
inv2 = Inventory({'nails': 150, 'bolts': 25})
combined_inv = inv1 + inv2
# expected: combined_inv.items is {'screws': 100, 'nails': 200, 'bolts': 25}

# Example 2
inv3 = Inventory({'widgets': 5})
inv4 = Inventory({'gadgets': 10})
combined_inv2 = inv3 + inv4
# expected: combined_inv2.items is {'widgets': 5, 'gadgets': 10}

# Example 3
inv5 = Inventory({'staples': 2000})
inv6 = Inventory({'staples': 3000})
combined_inv3 = inv5 + inv6
# expected: combined_inv3.items is {'staples': 5000}
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Incorrect assumption about operator behavior. The `+` operator is not defined for dictionaries. A student cannot simply write `self.items + other.items`. They must correctly implement the `__add__` magic method to manually iterate and merge the two item dictionaries into a new dictionary for the resulting Inventory object.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 26: Predict Code Output

Predict the output of the following code snippet and provide a step-by-step explanation for how you arrived at your answer. Your explanation should focus on how `cls` is resolved during the method call.

```python
class DataSerializer:
    protocol = 'JSON'

    @classmethod
    def serialize(cls, data):
        return f"<{cls.protocol}>{data}</{cls.protocol}>"

class XMLSerializer(DataSerializer):
    protocol = 'XML'

class Message:
    def __init__(self, content, serializer_class):
        self.content = content
        # The collaborator is the class itself, not an instance
        self.serializer = serializer_class

    def send(self):
        return self.serializer.serialize(self.content)

# Note: We are passing the XMLSerializer class, not an instance
message = Message("hello", XMLSerializer)
print(message.send())
```
<details> 
<summary>Hint</summary> 

Hidden Trap​: Late binding of `cls` in class methods. Students may incorrectly assume `cls` refers to the class where the method is defined, not the class that calls it.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 27: Debug Code

The following code is intended to create a `LoggingProxy` for a `DatabaseConnector` object. When a method like connect is called on the proxy, it should first log the action and then delegate the call to the actual database connector instance. However, running the code raises an `AttributeError`. Identify the bug, explain why it occurs, and provide the corrected code.

Intended Behavior​:

```
LOG: Attempting to call connect
Connected to the database.
```

```python
class DatabaseConnector:
    def __init__(self):
        self._is_connected = False

    def connect(self):
        self._is_connected = True
        print("Connected to the database.")

class LoggingProxy(DatabaseConnector):
    def __init__(self, connector_instance):
        # The collaborator is the connector instance
        self.connector = connector_instance

    def connect(self):
        print(f"LOG: Attempting to call connect")
        self.connector.connect()

db = DatabaseConnector()
proxy = LoggingProxy(db)
proxy.connect()
```

<details> 
<summary>Hint</summary> 

Hidden Trap​: Incomplete state initialization due to a missing `super().__init__ `call. Students must recognize that self is the same object throughout the inheritance chain and that the superclass's state must be properly initialized for the subclass to function.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 28: Implement a Class

Implement a `Configuration` class and two subclasses of a Validator: `MinLengthValidator` and `TypeValidator`.

1. Configuration​:
* Its `__init__` method accepts keyword arguments to store settings (e.g., `user='admin'`, `retries=3`).
* It stores these settings in an instance dictionary, perhaps called `_settings`.

2. ​Validator (Base Class)​:
* Provides the interface for validation rules.

3. `MinLengthValidator(Validator)`​:
* Its `__init__` takes a setting key and a minimum length.
* Its validate method takes a `Configuration` instance and returns `True` if the specified setting's value (which is assumed to be a string) meets the minimum length, `False` otherwise.

4.  `​TypeValidator(Validator)`​:
* Its `__init__` takes a setting key and a data type (e.g., str, int).
* Its validate method takes a Configuration instance and returns `True` if the specified setting's value is of the correct type, False otherwise.

Finally, the `Configuration` class must be implemented so that a `Validator` instance can be "subtracted" from it. The expression config - validator should return `True` if the configuration is valid according to the validator, and False otherwise.

I/O Examples​:
```python
# Example 1
config = Configuration(host='localhost', port=8080)
type_val = TypeValidator('port', int)
print(config - type_val) # Expected: True

# Example 2
config = Configuration(user='guest')
len_val = MinLengthValidator('user', 6)
print(config - len_val) # Expected: False

# Example 3
config = Configuration(api_key='ABC-123', retries='5')
type_val = TypeValidator('retries', int)
print(config - type_val) # Expected: False
```

<details> 
<summary>Hint</summary> 

Hidden Trap​: Misplacing the `__sub__` dunder method. The natural reading of config - validator implies that `__sub__` must be implemented on the `Configuration` class, where self is the config instance. A common but incorrect assumption is to place the dunder method on the `Validator` class.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 29: Predict & Explain Output

Predict the output of the following code snippet and be prepared to explain the method resolution order that produces this result.

```python
class DataParser:
    def process(self, data):
        print('Parsing data.')
        return 'parsed'

class Connection:
    def process(self, data):
        print('Opening connection.')
        return 'connected'

class DataTransmitter(Connection, DataParser):
    def process(self, data):
        print('Transmitting data.')
        result = super().process(data)
        print(f'Upstream process returned: {result}')

transmitter = DataTransmitter()
transmitter.process(data={'id': 1})
```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted:​ Misunderstanding `super()` and Method Resolution Order (MRO) in multiple inheritance. `super()` does not necessarily call the parent class, but rather the ​next​ class in the MRO.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 30: Debug a Snippet

The following code is intended to produce a `ConfigurableReport` that uses a formatter object to generate a titled report. However, it currently raises an `AttributeError`. Identify the bug and explain how to fix it.

Intended Behavior:​ The script should run without errors and print the string `=== WEEKLY REPORT ===`.

```python
class Formatter:
    def format_title(self, title):
        return f"=== {title.upper()} ==="

class Report:
    def __init__(self, formatter):
        self.formatter = formatter

class ConfigurableReport(Report):
    def __init__(self, title):
        self.title = title
        # Bug is related to this method's implementation

    def generate(self):
        return self.formatter.format_title(self.title)

report = ConfigurableReport("Weekly Report")
print(report.generate())
```


<details> 
<summary>Hint</summary> 

Hidden Trap Targeted:​ Incomplete state initialization due to a missing `super().__init__()` call. Subclass instances must properly initialize the state defined in their superclass(es).

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 31: Implement a Class

Implement the `TieredPricing` class. It inherits from `BasePricing` and requires an additional `tier_fee` during initialization. Its calculate method should determine a final price by first getting the base price from its parent and then adding its own `tier_fee` to that amount.

Provided Code:

```python
class BasePricing:
    def __init__(self, base_rate):
        self.rate = base_rate

    def calculate(self, units):
        return self.rate * units

# Your implementation here
class TieredPricing(BasePricing):
    pass
```

I/O Examples:
```python 
TieredPricing(base_rate=10, tier_fee=5).calculate(units=3) 
#35

TieredPricing(base_rate=2, tier_fee=100).calculate(units=50) 
# 200 

TieredPricing(base_rate=0, tier_fee=25).calculate(units=1000) 
#25
```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted:​ Incorrectly applying arithmetic operators to the `super()` proxy object itself instead of to its method's return value. This tests the understanding that `super()` is a proxy used for method dispatch, not a value.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 32: Predict and Explain​

Predict the output of the following Python code. In your explanation, describe the role of `super()` and detail the specific Method Resolution Order (MRO) that determines which log method is invoked.

```python
class Formatter:
    def log(self, message):
        return f"FORMAT: {message}"

class Timestamped:
    def log(self, message):
        return f"TIMESTAMP: {message}"

class MessageClient(Timestamped, Formatter):
    def __init__(self, message):
        self.message = message

    def send(self):
        print(super().log(self.message))

client = MessageClient("Data packet received.")
client.send()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ MRO Nuances with Multiple Mix-ins

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 33: Debugging​

The `ConfigManager` class below uses the Versioned mix-in to track changes to its configuration data. The intended behavior is that calling set_value should update the configuration dictionary and add a version snapshot to the `_history` list. However, running the code raises an exception.

Identify the bug, explain its cause, and provide the corrected code.

```python
class Versioned:
    def record_change(self):
        # Creates a snapshot of the current state for the history
        self._history += (self._data.copy(),)

class ConfigManager(Versioned):
    def __init__(self, initial_data):
        self._data = initial_data
        self._history = []

    def set_value(self, key, value):
        self._data[key] = value
        self.record_change()

# --- Intended Usage ---
config = ConfigManager({'theme': 'dark', 'font_size': 12})
config.set_value('font_size', 14)

# Expected `config._history` after execution:
# [{'theme': 'dark', 'font_size': 14}]
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Implicit Contract Violation (and Immutability)

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 34: Implementation​


You are building a data processing pipeline where some components are retryable. Implement the `Retryable` mix-in, which provides a `.execute() `method. This method should attempt to call `_perform_task()`, a method that will be defined on the host class.

The `.execute()` method must adhere to the following logic:

* It takes max_attempts as an argument.
* It calls `self._perform_task()`.
* If `_perform_task()` returns `True`, the execution is successful, and `.execute()` should return `'Success'`.
* If `_perform_task()` returns `False`, it should retry the call until it has been attempted `max_attempts` times.
* If all attempts fail, `.execute()` should return 'Failure'.

The `Retryable` mix-in assumes that any class using it will have an instance attribute task_name (a string) and will implement the `_perform_task` method.

```python
# --- Provided Code (Do not change) ---
class UnstableTask:
    def __init__(self, name, fail_count):
        self.task_name = name
        self.attempts = 0
        self.fail_limit = fail_count

    def _perform_task(self):
        self.attempts += 1
        if self.attempts > self.fail_limit:
            print(f"'{self.task_name}' succeeded on attempt {self.attempts}.")
            return True
        else:
            print(f"'{self.task_name}' failed on attempt {self.attempts}.")
            return False

# --- Your Implementation ---
# Implement the Retryable mix-in here.
class Retryable:
    pass # Your code here

# --- I/O Examples ---
class DataUpload(Retryable, UnstableTask):
    pass

# Example 1: Task succeeds on the second attempt
task1 = DataUpload(name="Image Upload", fail_count=1)
print(f"Final status: {task1.execute(max_attempts=3)}\n")
# Expected Output:
# 'Image Upload' failed on attempt 1.
# 'Image Upload' succeeded on attempt 2.
# Final status: Success

# Example 2: Task fails all attempts
task2 = DataUpload(name="Database Sync", fail_count=3)
print(f"Final status: {task2.execute(max_attempts=2)}\n")
# Expected Output:
# 'Database Sync' failed on attempt 1.
# 'Database Sync' failed on attempt 2.
# Final status: Failure

# Example 3: Task succeeds on the first attempt
task3 = DataUpload(name="Log Archiving", fail_count=0)
print(f"Final status: {task3.execute(max_attempts=5)}")
# Expected Output:
# 'Log Archiving' succeeded on attempt 1.
# Final status: Success
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ State Collision and Composition

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 35: Predict and Explain the Output 

Predict the output of the following Python code. Provide a step-by-step explanation of how you arrived at your answer, paying close attention to the relationship between the `Logger` and `DataProcessor` classes and how the final output is generated.

```python
class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f"Logging to {self.file_name}"

class DataProcessor:
    def __init__(self, data_source, logger):
        self.source = data_source
        self.logger = logger # A DataProcessor has a Logger

    def process(self):
        print(f"Processing data from {self.source}.")
        print(self.logger)

file_logger = Logger("system.log")
processor = DataProcessor("API", file_logger)
processor.process()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Mistaking collaboration for inheritance. A student might incorrectly think `DataProcessor` inherits from Logger and try to explain method resolution, when the key is that `DataProcessor` simply holds a `Logger` instance and delegates the call to print, which in turn invokes the Logger's `__str__` method.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 36:  Debug the Code

The following code is intended to model a `Car` that has an `Engine`. When `car.start()` is called, it should delegate the action to its `Engine` object and print "Engine started with Vroom!". However, running the code produces an error. Identify the bug, explain why it occurs, and provide the corrected code.

Intended Behavior:


Expected Output: `Engine started with Vroom!`

Buggy Code:
```python
class Engine:
    def start(self):
        return "Engine started with Vroom!"

class Car:
    def __init__(self):
        self.engine = Engine() # A Car has an Engine

    def start(self):
        # Incorrectly assumes the Car IS-AN Engine
        message = start()
        print(message)

car = Car()
car.start()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ `NameError` due to incorrect delegation. The code calls `start()` instead of `self.engine.start()`. This directly targets the common mistake of thinking a "has-a" relationship provides the containing object with the collaborator's methods directly, as an "is-a" relationship would.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 37: Implement a Class 

Implement a `ShoppingList` class that encapsulates a list of items.

1. The constructor `__init__` should accept an initial list of items.
2. The class must support the `+` operator. When two `ShoppingList` instances are added, it should return a ​new​ `ShoppingList` instance containing all items from both lists.
3. The original lists must not be mutated.

Provide the complete class implementation.

Examples:

```python
# Example 1
groceries = ShoppingList(["milk", "eggs"])
household = ShoppingList(["soap", "paper towels"])
full_list = groceries + household
print(full_list.items)
# Expected Output: ['milk', 'eggs', 'soap', 'paper towels']


# Example 2
list1 = ShoppingList(["apples"])
print(list1.items) # Check before operation
# Expected Output: ['apples']

list2 = list1 + ShoppingList(["bananas"])
print(list1.items) # Verify original is unchanged
# Expected Output: ['apples']
print(list2.items)
# Expected Output: ['apples', 'bananas']

# Example 3
empty_list = ShoppingList([])
other_list = ShoppingList(["chair"])
result = empty_list + other_list
print(result.items)
# Expected Output: ['chair']
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Assuming the `+` operator will work "for free". A student might assume that because the class contains a list, Python will know to concatenate the inner lists. This is a reasonable but incorrect assumption. The trap is realizing this will cause a `TypeError` and that the `__add__` magic method must be implemented to define the behavior of the + operator for ShoppingList objects.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 38: Predict and Explain the Output

Predict the output of the following code snippet. Explain how instance and class variable scoping rules within the inheritance hierarchy determine the final output.

```python
class DataParser:
    # Class variable
    _delimiters = [',', ';']

    def get_delimiters(self):
        return self._delimiters

class CsvParser(DataParser):
    def __init__(self):
        # Instance variable with the same name
        self._delimiters = [',']

class LogEntryProcessor:
    def __init__(self, text, parser):
        self.text = text
        self.parser = parser

    def process(self):
        delimiters = self.parser.get_delimiters()
        print(f"Using delimiters: {delimiters}")

processor = LogEntryProcessor("user;admin", CsvParser())
processor.process()
```

<details> 
<summary>Hint</summary> 

Hidden Trap: Shadowing a class variable with an instance variable in a subclass, and then calling a method defined in the superclass.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 39: Debug the Code Snippet

The following code is intended to allow different Project instances to have independent build settings. Modifying the settings for one project should not affect another. However, the code is buggy and a change to `project_a`'s settings incorrectly alters `project_b`'s settings. Identify the bug and explain why it occurs.

```python
class BaseSettings:
    config = {'version': '1.0', 'strict_mode': False}

    def enable_strict_mode(self):
        self.config['strict_mode'] = True

class PythonProjectSettings(BaseSettings):
    pass

class Project:
    def __init__(self, name):
        self.name = name
        self.settings = PythonProjectSettings()

# --- Intended Behavior ---
project_a = Project("Project A")
project_b = Project("Project B")

# Enable strict mode only for Project A
project_a.settings.enable_strict_mode()

# Check settings for both projects
print(f"{project_a.name} strict_mode: "
      f"{project_a.settings.config['strict_mode']}")
print(f"{project_b.name} strict_mode: "
      f"{project_b.settings.config['strict_mode']}")
```

<details> 
<summary>Hint</summary> 

Hidden Trap: Mutating a shared, mutable class variable through an instance reference, causing unintended side effects across all instances of the class and its subclasses.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 40: Implement the `__add__` Method

Complete the `BaseComponent` and `Resistor` classes below. The `__add__` method in `BaseComponent` should allow adding an integer to a component's value, returning a ​new component object of the same class​ with the updated value. The `Resistor` subclass should inherit this behavior without overriding `__add__`.

```python
class BaseComponent:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{type(self).__name__}({self.value})"

    def __add__(self, num):
        # Your implementation here
        pass

class Resistor(BaseComponent):
    # A class attribute specific to Resistors
    TOLERANCE = 0.05

# --- I/O Examples ---
# 1. Adding to a BaseComponent instance
c1 = BaseComponent(100)
c2 = c1 + 20
print(f"Result: {c2}, Type: {type(c2)}")
# Expected: Result: BaseComponent(120), Type: <class '__main__.BaseComponent'>

# 2. Adding to a Resistor instance
r1 = Resistor(500)
r2 = r1 + 50
print(f"Result: {r2}, Type: {type(r2)}")
# Expected: Result: Resistor(550), Type: <class '__main__.Resistor'>

# 3. Verifying subclass attributes are preserved
print(f"New Resistor Tolerance: {r2.TOLERANCE}")
# Expected: New Resistor Tolerance: 0.05
```

<details> 
<summary>Hint</summary> 


Hidden Trap: Using the correct constructor (`self.__class__` or `type(self)`) within a superclass method to ensure polymorphic instantiation, rather than hardcoding the base class name.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 41: Predict and Explain Output


Predict the output of the following code snippet. Provide a step-by-step explanation of how Python's Method Resolution Order (MRO) determines which process method is called and what value is ultimately returned.

```python
class TextProcessor:
    def process(self, data):
        return data.upper()

class JsonProcessor:
    def process(self, data):
        return '{"data": "' + data + '"}'

class DataPipeline(TextProcessor, JsonProcessor):
    def run(self, input_data):
        # some preparatory steps...
        processed = self.process(input_data)
        # some cleanup steps...
        return processed

pipeline = DataPipeline()
print(pipeline.run("launch"))
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt targets the "left-to-right" rule in MRO. Since `TextProcessor` is listed before `JsonProcessor` in the inheritance list, its process method will be found and executed first. The process method in `JsonProcessor` is completely ignored, a behavior that can be counterintuitive if one expects composition or chaining.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 42: Debug a Code Snippet


The `StyledButton` class is intended to create a button whose text is first wrapped in a style tag `(<em>)` by the `StylingMixin`, and then rendered into a full button tag `(<button>)` by the `ButtonWidget` class. The final output for an input of "Click Me" should be `<button><em>Click Me</em></button>`.

However, the current implementation produces incorrect output. Identify the bug and explain why the Method Resolution Order (MRO) causes this unintended behavior.

```python
class ButtonWidget:
    def render(self, text):
        return f"<button>{text}</button>"

class StylingMixin:
    def render(self, text):
        styled_text = f"<em>{text}</em>"
        return super().render(styled_text)

class StyledButton(ButtonWidget, StylingMixin):
    pass

# Intended behavior:
# button = StyledButton()
# print(button.render("Click Me"))
# Expected output: <button><em>Click Me</em></button>

# Current behavior:
button = StyledButton()
print(button.render("Click Me"))
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This tests the interaction between inheritance order and `super()`. The current MRO finds `ButtonWidget.render first`, which does not call `super()`, so the `StylingMixin` is never invoked. The bug requires reversing the inheritance order. This highlights that the functionality of `super()` is entirely dependent on the MRO, which is defined by the class declaration.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 43: Implement a Class


Implement the `ConfigurableService` class. This class must inherit from `BaseService` and `LoggingMixin`. Its execute method should first log the provided data, and then pass that same data to the execute method from its service parent. The class must correctly initialize with a `service_name`.

```python
class BaseService:
    def __init__(self, service_name):
        self.service_name = service_name

    def execute(self, data):
        return f"{self.service_name} processed: {data}"

class LoggingMixin:
    def execute(self, data):
        print(f"Logging data: {data}")
        return super().execute(data)

# Your implementation of ConfigurableService here
```

```python
# --- Examples ---
service1 = ConfigurableService("DataProcessor")
# Expected output:
# Logging data: payload123
# DataProcessor processed: payload123
print(service1.execute("payload123"))

print("-" * 20)

service2 = ConfigurableService("FileHandler")
# Expected output:
# Logging data: document.txt
# FileHandler processed: document.txt
print(service2.execute("document.txt"))

print("-" * 20)

service3 = ConfigurableService("Auth")
# Expected output:
# Logging data: user:token
# Auth processed: user:token
print(service3.execute("user:token"))
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt combines two concepts: MRO for method calls and MRO for initialization. The primary trap is recognizing the need to correctly order the parent classes (`LoggingMixin` must come first) to achieve the desired execute behavior. A second, related trap is handling the `__init__` method. The student must implement an `__init__` in `ConfigurableService` that calls `super().__init__` to properly initialize the service_name from `BaseService`.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 44: Predict and Explain


Predict the output of the following code snippet. Explain your reasoning for each printed line, focusing on object identity and the behavior of the is operator.

```python
class Component:
    def __init__(self, name):
        self.name = name
        self.settings = {'active': True}

    def get_settings(self):
        # Returns a copy of the settings dictionary
        return self.settings.copy()

class System:
    def __init__(self):
        self.component = Component("Core")

    def get_component(self):
        return self.component

sys = System()
comp1 = sys.get_component()
comp_settings = comp1.get_settings()

comp_settings['active'] = False

print(f"1: {sys.component.settings['active']}")
print(f"2: {comp1 is sys.get_component()}")
print(f"3: {sys.component.settings is comp_settings}")
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt targets the distinction between returning a direct reference to a mutable object versus returning a ​copy​ of it. The get_settings method's use of `.copy()` is the key. It creates a new dictionary object with the same key-value pairs, breaking the identity link that a student might otherwise assume exists.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 45: Debug the Code


The following code is intended to manage a single, shared configuration object for multiple service instances. The `LogManager` should ensure that all services access the exact same configuration dictionary. However, the final line prints `False`, indicating a bug. Identify the bug, explain why it causes the issue, and describe how to fix it.

```python
# Intended behavior: All Service instances should share the exact same
# logger configuration object. The final check `config1 is config2`
# is expected to print `True`.

class LogManager:
    def __init__(self):
        self.config = {'level': 'INFO', 'file': 'app.log'}

    def update_config(self, new_settings):
        # Creates a new config object based on the old one
        self.config = self.config.copy()
        self.config.update(new_settings)

class Service:
    def __init__(self, name, manager):
        self.name = name
        self.log_manager = manager

    def get_log_config(self):
        return self.log_manager.config

log_mgr = LogManager()
service1 = Service("AuthService", log_mgr)
config1 = service1.get_log_config()

log_mgr.update_config({'level': 'DEBUG'})

service2 = Service("DataService", log_mgr)
config2 = service2.get_log_config()

print(config1 is config2) # Output is False, but should be True

```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The trap here is a reasonable but incorrect assumption about the `update_config` method's behavior. The name implies it will ​mutate​ the existing configuration object. However, its implementation first creates a copy and then ​reassigns​ self.config to that new copy. This severs the identity link to the original object held by `config1`, causing the check to fail.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 46: Implement a Class

Implement the `DeviceCache` class. This class must manage `Device` objects. Its `get_device` method should adhere to the following rule: for any given `device_id`, the method must always return the exact same `Device` object. If `get_device` is called with a `device_id` that has not been seen before, it should create and store a new Device instance. Subsequent calls with that same `device_id` must return that stored instance.

You are given the `Device` class. Your code should produce the expected output for all three examples.

```python
class Device:
    """A simple class representing a hardware device."""
    def __init__(self, device_id):
        self.device_id = device_id
        # The following print statement helps verify when a new object is made.
        print(f"Initializing new device: {self.device_id}")

# Your implementation of DeviceCache goes here.


I/O Examples:

# Example 1: Retrieving the same device twice
cache = DeviceCache()
d1 = cache.get_device("d-101")
d2 = cache.get_device("d-101")
print(f"Example 1 check: {d1 is d2}")
# Expected Output: True

# Example 2: Retrieving two different devices
d3 = cache.get_device("d-205")
print(f"Example 2 check: {d1 is d3}")
# Expected Output: False

# Example 3: Verifying separate caches
cache2 = DeviceCache()
d4 = cache2.get_device("d-101")
print(f"Example 3 check: {d1 is d4}")
# Expected Output: False
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The primary trap is correctly managing the storage and retrieval of object references. The implementation must ensure it's storing the actual object instance and not accidentally creating a new one on each call. A secondary trap, tested by Example 3, is ensuring the cache is an ​instance​ variable, not a class variable, so that different `DeviceCache` objects maintain separate, independent caches.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 47: Predict and Explain

Predict the output of the following code. Explain precisely why it produces that output, detailing the method lookups and comparisons that occur.

```python
class Authorization:
    def __init__(self, level):
        self.level = level

    def __eq__(self, other):
        print("Authorization.__eq__ called")
        if not isinstance(other, Authorization):
            return NotImplemented
        return self.level == other.level

class User:
    def __init__(self, auth_level):
        self.auth = Authorization(auth_level)

    def can_access(self, required_level):
        required_auth = Authorization(required_level)
        return self.auth != required_auth

user = User(auth_level=5)
print(user.can_access(required_level=5))

```

<details> 
<summary>Hint</summary> 


Hidden Trap: The `!=` operator does not automatically call a negated version of `__eq__`. It looks for `__ne__` first and, if not found, falls back to the default identity-based comparison.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 48: Debugging

The following code is intended to determine if a new `EventLog` is a promotion from an old one. The rule is that a log is a promotion if its priority is higher. The code is currently failing with an unhandled `TypeError`. Identify the bug, explain its cause, and provide the corrected code.

Intended Behavior​: The code should execute without error and print `True`.

```python
class EventLog:
    def __init__(self, priority, message):
        self.priority = priority
        self.message = message

    def __lt__(self, other):
        if not isinstance(other, EventLog):
            return NotImplemented
        return self.priority < other.priority

class SystemMonitor:
    @staticmethod
    def is_promotion(old_log, new_log):
        # A new log is a promotion if it is "greater than" the old one.
        return new_log > old_log

old_log = EventLog(priority=1, message="System OK")
new_log = EventLog(priority=5, message="Critical Failure")

print(SystemMonitor.is_promotion(old_log, new_log))
```


<details> 
<summary>Hint</summary> 


Hidden Trap: Assuming that defining `__lt__ `is sufficient for Python to handle `>` comparisons automatically through reflection in all cases. While Python may try `a > b` by evaluating `b < a`, relying on this is fragile. The direct implementation of `__gt__` is missing, causing a `TypeError` when the `>` operator is used.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 49: Implementation

A `GeographicPoint` has latitude and longitude. A `Route` is defined by two `GeographicPoint` objects: a start and an end.

Implement the `Route` class. Two `Route` instances are considered equal if they represent the same journey, regardless of direction (e.g., a route from A to B is equal to a route from B to A). They must also have the same `is_scenic` status.

Your implementation should define the necessary magic method(s) for the `==` operator to work as described.

```python
class GeographicPoint:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return (isinstance(other, GeographicPoint) and
                self.lat == other.lat and self.lon == other.lon)

# Your Route class implementation here...

# I/O Examples:
p1 = GeographicPoint(40.7128, -74.0060) # NYC
p2 = GeographicPoint(34.0522, -118.2437) # LA
p3 = GeographicPoint(49.2827, -123.1207) # Vancouver

route1 = Route(p1, p2, is_scenic=True)
route2 = Route(p2, p1, is_scenic=True) # Reversed points
route3 = Route(p1, p2, is_scenic=False) # Different scenic status
route4 = Route(p1, p3, is_scenic=True) # Different endpoint

print(route1 == route2) # Expected: True
print(route1 == route3) # Expected: False
print(route1 == route4) # Expected: False
```

<details> 
<summary>Hint</summary> 

Hidden Trap: Complex equality logic with collaborator objects. A simple comparison of `self.start == other.start` and `self.end == other.end` is insufficient because the direction doesn't matter. The implementation must account for the commutative nature of the route's endpoints.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 50: Predict and Explain​*

Predict the output of the code below. Explain the sequence of method calls triggered by the `+` operator in the line that initializes the report variable, detailing how each call contributes to the final state of the report object.

```python
class DataPoint:
    def __init__(self, value):
        self.value = value

class Report:
    def __init__(self, title, data_points=None):
        self.title = title
        self.data = data_points or []

    def __add__(self, other):
        if isinstance(other, DataPoint):
            new_data = self.data + [other.value]
            return Report(self.title, new_data)
        elif isinstance(other, Report):
            new_title = f"{self.title} & {other.title}"
            new_data = self.data + other.data
            return Report(new_title, new_data)
        return NotImplemented

initial = Report("Q1 Sales")
point = DataPoint(100)
adjustment = Report("Adjustments", [-5])

report = initial + point + adjustment
print(len(report.data))
print(report.title)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Chaining methods that return new objects.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 51: Debugging​

The code below is intended to allow a Project's hours to be increased by adding `TimeLog` objects using the `+=` operator. The final print statement should display that the project has 12 total hours. However, running the code raises a `TypeError` on the second `+=` operation. Identify the bug, explain its cause, and provide the corrected `Project` class implementation.

```python
class TimeLog:
    def __init__(self, hours):
        self.hours = hours

class Project:
    def __init__(self, name):
        self.name = name
        self.hours_logged = 0

    def __iadd__(self, other):
        if isinstance(other, TimeLog):
            self.hours_logged += other.hours
        # Missing return statement here

# --- Main execution ---
alpha = Project("Project Alpha")
alpha += TimeLog(8)
alpha += TimeLog(4) # This line causes a TypeError

# Expected output: Project Alpha has 12 hours logged.
print(f"{alpha.name} has {alpha.hours_logged} hours logged.")
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The required return value for in-place augmented assignment methods (`__iadd__`).

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 52: Implementation​

Implement the `Inventory` class to manage item quantities. The class must support the + operator to combine an `Inventory` object with a `Shipment` object, which contains a dictionary of new items. The operation must be commutative, meaning it should work correctly regardless of whether the `Inventory` or `Shipment` is the left operand. Adding a `Shipment` to an `Inventory` should return a ​new​ I`nventory` object with updated quantities.

```python
class Shipment:
    def __init__(self, items):
        self.items = items

class Inventory:
    # Your implementation here
    pass

# --- Examples ---

# Example 1: inventory + shipment
inv = Inventory({'apples': 10, 'bananas': 20})
shipment1 = Shipment({'bananas': 5, 'oranges': 15})
new_inv1 = inv + shipment1
# Expected: new_inv1.stock is {'apples': 10, 'bananas': 25, 'oranges': 15}
print(new_inv1.stock)

# Example 2: shipment + inventory
inv2 = Inventory({'staplers': 50, 'pens': 100})
shipment2 = Shipment({'pens': 25, 'paper': 200})
new_inv2 = shipment2 + inv2
# Expected: new_inv2.stock is {'staplers': 50, 'pens': 125, 'paper': 200}
print(new_inv2.stock)

# Example 3: Original inventory is not mutated
print(inv.stock) # Expected: {'apples': 10, 'bananas': 20}
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Needing `__radd__` to handle operations where the custom class is the right-hand operand.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 53: Predict and Explain Output

Predict the output of the following Python code snippet. Explain in detail the process Python uses to determine the string representation for each print call, paying close attention to how container objects format their contents.

```python
class Component:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f"Component(name='{self.name}')"

class System:
    def __init__(self, system_id, components):
        self.system_id = system_id
        self.components = components

    def __str__(self):
        return f"System ID: {self.system_id}"

main_system = System(
    "SYS-101",
    [Component("sensor"), Component("actuator")]
)

print(main_system)
print(main_system.components)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt targets the rule that container types (like list, dict, tuple) ​always use the `__repr__` method​ of their contents, even when the container itself is being printed (which implicitly uses str). Students may incorrectly assume that `print()`'s call to str propagates down to the elements within the list.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 54: Debug the Code

The following code is intended to display a project's details, including a user-friendly list of its associated tasks. However, the output for the tasks is not as expected. Identify the bug, explain why the current output occurs, and describe the necessary correction to the class definitions.

Intended Behavior:​ The script should print the following line to the console:
`Project: Data Migration, Tasks: [High-priority task, Review task]`

```python
class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.priority}-priority task"

class Project:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def __repr__(self):
        # Developer-facing representation for debugging
        return f"Project: {self.name}, Tasks: {self.tasks}"

task1 = Task("Implement API", "High")
task2 = Task("Code Review", "Review")
project = Project("Data Migration", [task1, task2])

print(project)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt targets the fallback behavior where `print(obj)` (which uses `str(obj)`) will call `obj.__repr__()` if `obj.__str__()` is not defined. The chain of events is: print(project) -> str(project) -> (fallback) repr(project) -> list formatting -> repr(task). Since Task has no `__repr__`, the default object representation is used. The incorrect assumption is that print will somehow find and use the `__str__` method on the nested Task objects.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 55: Implement Classes

Implement the `Book` and `Library` classes based on the requirements demonstrated by the I/O examples below. A `Library` is initialized with a name and a list of Book objects. A `Book` has a title and an author. Your implementation must produce the exact output shown for each print call.

```python
# Your class definitions go here

# Do not change the code below
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")
my_library = Library("City Central", [book1, book2])

# Example 1
print(book1)
# Expected Output 1:
# The Hobbit by J.R.R. Tolkien

# Example 2
print(my_library)
# Expected Output 2:
# City Central Library

# Example 3
print(my_library.books)
# Expected Output 3:
# [Book('The Hobbit', 'J.R.R. Tolkien'), Book('1984', 'George Orwell')]
```



<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt forces the student to recognize that the Book class requires ​both a `__str__` and a `__repr__` method​ to satisfy all examples. Example 1 defines the behavior for `__str__`, while Example 3 (printing a list of books) implicitly defines the required behavior for `__repr__`. A student who only implements `__str__` on `Book` will fail to get the correct output for Example 3.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 56: Predict and Explain​


Predict the output of the following code snippet. Provide a step-by-step explanation for how you arrived at your answer, detailing what `self`, `__class__`, and `__name__` refer to on each line where they are used.

```python
class Notifier:
    def send(self, message):
        print(f"Sending notification: {message}")

class Service:
    def __init__(self):
        self.notifier = Notifier()

    def do_work(self):
        print(f"Starting work in {self.__class__.__name__}...")
        self.notifier.send("Work in progress")
        print(f"Notifier's class is: {self.notifier.__class__.__name__}")

service = Service()
service.do_work()
```



<details> 
<summary>Hint</summary> 

​Hidden Trap:​​ Differentiating between the class of the Service instance (`self`) and the class of its collaborator object (`self.notifier`). Students must correctly identify the object on which `.__class__` is being accessed.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 57: Debug the Code​


The following code is intended to create a Report that uses a DataFormatter collaborator to format its title. The generate method should print a title including the formatter's class name, like "CSVFormatter Report". However, running the code raises an `AttributeError`.

Identify the bug, explain why it occurs, and provide the corrected line of code.

```python
class CSVFormatter:
    pass

class Report:
    def __init__(self, formatter):
        self.formatter = formatter

    def generate(self):
        # Intended to print: "CSVFormatter Report"
        print(f"{self.formatter.__name__} Report")

report = Report(CSVFormatter())
report.generate()
```

<details> 
<summary>Hint</summary> 

​Hidden Trap:​​ The reasonable but incorrect assumption that the `__name__` attribute is available directly on an ​instance​. This tests the distinction between instance attributes and class attributes.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 58: Implement a Function​

Implement a function c`reate_factory_log(component)` that takes an object instance representing a machine part. The function should return a string logging the part's class name. The object passed to the function will be a collaborator in a larger factory system.

Your implementation must work for any object, not just the examples shown.

I/O Examples:
```python
class Gear:
    pass

class Piston:
    pass

class Rotor:
    pass

# Your implementation of create_factory_log here

print(create_factory_log(Gear()))
# Expected: "Component of type 'Gear' received."

print(create_factory_log(Piston()))
# Expected: "Component of type 'Piston' received."

print(create_factory_log(Rotor()))
# Expected: "Component of type 'Rotor' received."

```

<details> 
<summary>Hint</summary> 


​Hidden Trap:​​ The temptation to use isinstance checks or hardcoded strings. The prompt requires a polymorphic solution that dynamically inspects the collaborating object's type using `__class__.__name__`, demonstrating a core principle of object-oriented design.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 59: Predict Output

Predict the output of the following code snippet and explain your reasoning.

```python
class Song:
    def __init__(self, title):
        self.title = title

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_first_song_details(self):
        try:
            song = self.songs[0]
            # This line may raise an exception
            return f"{song.title} by {song.artist}"
        except IndexError:
            return "Playlist is empty."

playlist = Playlist("My Jams")
song1 = Song("Stairway to Heaven")
playlist.add_song(song1)

try:
    print(playlist.get_first_song_details())
except Exception as e:
    print(f"Caught a general exception: {type(e).__name__}")

```


<details> 
<summary>Hint</summary> 

​Hidden Trap: Exception Specificity and Propagation. An except block for a specific exception (`IndexError`) will not catch a different exception type (`AttributeError`). The unhandled exception propagates up the call stack until a suitable handler (except `Exception`) is found.​

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 60: Debugging


The following function process_all_data is intended to process a list of raw data. It should create `DataEntry` objects for integer values and return a list of those values. For any non-integer data, it should catch the `TypeError` raised by the `DataEntry` constructor, print an error message, and continue processing the rest of the list. The current implementation is buggy. Identify the bug and describe how to fix it.

```python
class `DataEntry`:
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError("DataEntry value must be an integer.")
        self.value = value

    def get_value(self):
        return self.value

def process_all_data(raw_data_list):
    processed_values = []
    try:
        for raw_data in raw_data_list:
            entry = DataEntry(raw_data)
            processed_values.append(entry.get_value())
    except TypeError as e:
        print(f"Error processing entry: {e}")

    return processed_values

# Example Usage:
data = [10, "invalid", 20, 30, "bad_data"]
result = process_all_data(data)
print(f"Processed: {result}")

# Current Incorrect Output:
# Error processing entry: DataEntry value must be an integer.
# Processed: []

# Expected Correct Output:
# Error processing entry: DataEntry value must be an integer.
# Error processing entry: DataEntry value must be an integer.
# Processed: [10, 20, 30]
```


<details> 
<summary>Hint</summary> 

Hidden Trap: Scope of `try/except` block. Placing an entire loop inside a single try block means that an exception raised during any iteration will terminate the whole loop and jump to the except block. To handle errors on a per-item basis, the try/except must be inside the loop.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 61: Implementation


Implement the `MessageBroadcaster` class below. Its `send_all` method accepts a message string and a list of recipient objects. The method should try to deliver the message to each recipient based on the following logic:

1.  First, attempt to call a `send(message)` method on the recipient.
2.  If the recipient does not have a send method, it should fall back to calling a write(message) method.
3.  If a recipient has neither method, it should be skipped without raising an error.
4.  The method must return the total count of messages that were successfully sent.

```python
class MessageBroadcaster:
    # Your implementation here

# --- I/O Examples ---
# Helper classes for testing
class EmailRecipient:
    def send(self, message):
        print(f"Emailing: {message}")

class FileLogger:
    def write(self, message):
        print(f"Logging: {message}")

# Example 1
broadcaster = MessageBroadcaster()
recipients1 = [EmailRecipient(), EmailRecipient()]
count1 = broadcaster.send_all("Hello", recipients1)
print(count1)
# Expected Output:
# Emailing: Hello
# Emailing: Hello
# 2

# Example 2
broadcaster = MessageBroadcaster()
recipients2 = [EmailRecipient(), FileLogger(), EmailRecipient()]
count2 = broadcaster.send_all("Update", recipients2)
print(count2)
# Expected Output:
# Emailing: Update
# Logging: Update
# Emailing: Update
# 3

# Example 3
broadcaster = MessageBroadcaster()
recipients3 = [FileLogger(), 42, EmailRecipient()]
count3 = broadcaster.send_all("Final notice", recipients3)
print(count3)
# Expected Output:
# Logging: Final notice
# Emailing: Final notice
# 2
```


<details> 
<summary>Hint</summary> 

Hidden Trap: Graceful Degradation / Fallback Logic. Correctly implementing the fallback requires careful structuring of `try/except` blocks, likely nested, to first attempt one protocol (`.send()`) and then, only upon its failure, attempt a second protocol (`.write()`). A single try with multiple except clauses is insufficient to model this sequential fallback logic.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 62: Predict and Explain

What will the following code output? Explain your reasoning in detail.

```python
class DataValidationError(Exception):
    pass

class DataValidator:
    def __init__(self, required_keys):
        self.required_keys = set(required_keys)

    def validate(self, data):
        if not self.required_keys.issubset(data.keys()):
            raise DataValidationError("Missing required data keys.")
        return True

class Report:
    def __init__(self, data, validator):
        self.data = data
        self.validator = validator

    def generate(self):
        try:
            self.validator.validate(self.data)
            print("Report generated successfully.")
        except Exception:
            print("A generic error occurred.")
        except DataValidationError:
            print("Data validation failed.")

validator = DataValidator(['id', 'timestamp'])
invalid_data = {'id': 101}
report = Report(invalid_data, validator)
report.generate()
```

<details> 
<summary>Hint</summary> 
Hidden Trap​: Exception hierarchy and except block ordering.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 63: Debug the Code

The following code is intended to catch an `InsufficientFundsError` and print a specific, helpful message. However, when the error is caught, it prints an empty line instead of the expected message. Identify the bug and provide the corrected code.

Intended Behavior:
The script should print the message: `Insufficient funds in account 12345`.

```python
# Buggy Code
class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            msg = f"Insufficient funds in account {self.account_id}."
            raise InsufficientFundsError(msg)
        self.balance -= amount

class PaymentProcessor:
    def process_payment(self, account, amount):
        try:
            account.withdraw(amount)
            print("Payment successful.")
        except InsufficientFundsError as e:
            print(e)

my_account = Account(12345, 100)
processor = PaymentProcessor()
processor.process_payment(my_account, 150)
```

<details> 
<summary>Hint</summary> 

Hidden Trap​: Custom exception classes need an `__init__` method that calls `super().__init__(message)` to store and display the error message.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 64: Implement a Class

Implement the `ConnectionError` custom exception and the Device class to satisfy the requirements outlined in the provided examples.

Requirements:

1. Create a custom exception `ConnectionError` that inherits from `Exception`. Its initializer must accept a message string and an error_code integer and store them as attributes.
2. Create a `Device` class. Its `__init__` method should accept a name.
3. The `Device` class must have an instance method connect_to(self, network). The network object is a collaborator.
4.  If the network object's status attribute is 'offline', the method should raise a `ConnectionError` with the message `f"{self.name}` failed to connect." and an error_code of 101.
5.  If the connection is successful (network.status is 'online'), the method should return True.

```python
# Helper class (do not modify)
class Network:
    def __init__(self, status):
        self.status = status

# Your implementation here:
# class ConnectionError(Exception):
#     ...
#
# class Device:
#     ...

# --- Examples ---

# 1. Successful Connection
online_net = Network('online')
my_device = Device('Router')
print(my_device.connect_to(online_net))
# Expected Output:
# True

# 2. Failed Connection (general catch)
offline_net = Network('offline')
my_pc = Device('My PC')
try:
    my_pc.connect_to(offline_net)
except Exception as e:
    print(e)
# Expected Output:
# My PC failed to connect.

# 3. Failed Connection (specific catch with error code)
try:
    my_pc.connect_to(offline_net)
except ConnectionError as e:
    print(f"Error Code: {e.error_code}, Message: {e}")
# Expected Output:
# Error Code: 101, Message: My PC failed to connect.
```

<details> 
<summary>Hint</summary> 

Hidden Trap​: Designing a custom exception to carry state beyond just a message string.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 65: Predict and Explain the Output

Predict the output of the following code snippet and explain your reasoning. Your explanation should focus on the interaction between the `Inventory` and `Widget` objects.

```python
class Widget:
    def __init__(self, name):
        self.name = name
        self.inspections = 0

    def inspect(self):
        self.inspections += 1

class Inventory:
    def __init__(self, initial_widgets):
        self.widgets = initial_widgets

    def run_quality_check(self):
        for widget in self.widgets:
            widget.inspect()

    def get_total_inspections(self):
        return sum(w.inspections for w in self.widgets)

widget_a = Widget('A')
widget_b = Widget('B')
main_stock = [widget_a, widget_b]

warehouse = Inventory(main_stock)
warehouse.run_quality_check()

print(warehouse.get_total_inspections())
print(widget_a.inspections)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Tests understanding of object references vs. copies. The `Inventory `object holds references to the original `Widget` objects, not copies. Modifying a widget's state via the warehouse object also mutates the original `widget_a` object because they are the exact same object in memory.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 66: Debug the Code.

The following code is intended to manage a team and its members. A `Team` object should be able to add `Member` objects to its roster. The final output should be `['Dana', 'Fox']`. However, the code currently prints an empty list `[]`. Identify the bug and describe how to fix it.

```python
# Intended behavior: Add two members to a team and list their names.
# Expected output: ['Dana', 'Fox']

class Member:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members + [member]

    def get_roster(self):
        return [m.name for m in self.members]

special_ops = Team("Special Ops")
special_ops.add_member(Member("Dana"))
special_ops.add_member(Member("Fox"))

print(special_ops.get_roster())

```



<details> 
<summary>Hint</summary> 

Hidden Trap:​ Targets a common incorrect assumption about the `+` operator with lists. The expression `self.members + [member]` creates a ​new​ list but does not modify self.members in place. The new list is created and then immediately discarded. The trap is making the student identify that a non-mutating method was used where a mutating one (like .append()) was needed.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 67: Implement Classes with Collaborators*

Implement the `Engine`, `Wheel`, and `Car` classes to satisfy the requirements demonstrated by the I/O examples below.

A `Car` instance is composed of one `Engine` instance and four `Wheel` instances.

* The `Engine` class needs a get_status method that returns the string "`Engine is on.`".
* The `Wheel` class needs a get_status method that returns the string "Tire pressure is normal.".
* The `Car` class must have a run_diagnostics method that returns a dictionary containing status reports from its components.

```python
# --- Implement `Engine`, `Wheel`, and `Car` classes here ---

```

```python
# --- I/O Examples ---

# 1.
engine = Engine()
wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
car = Car(engine, wheels)
print(car.run_diagnostics())
# Expected:
# {
#   'engine': 'Engine is on.',
#   'wheel_1': 'Tire pressure is normal.',
#   'wheel_2': 'Tire pressure is normal.',
#   'wheel_3': 'Tire pressure is normal.',
#   'wheel_4': 'Tire pressure is normal.'
# }

# 2.
class RacingEngine(Engine):
    def get_status(self):
        return "Engine is supercharged."

car2 = Car(RacingEngine(), [Wheel() for _ in range(4)])
print(car2.run_diagnostics()['engine'])
# Expected: Engine is supercharged.

# 3.
car3 = Car(Engine(), [Wheel() for _ in range(4)])
print(isinstance(car3.engine, Engine))
# Expected: True
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Tests the ability to correctly model a "has-a" relationship (composition) instead of an incorrect "is-a" relationship (inheritance). The `Car` class should contain an `Engine` and `Wheel` objects as instance variables, not inherit from them. The trap is to see if the student defaults to inheritance when the more appropriate pattern is for the `Car` object to collaborate with its component objects.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


