
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