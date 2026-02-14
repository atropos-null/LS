# PY129 LS Bpot Prep Questions

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

