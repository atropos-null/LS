# Python 120 Working Document

<a name="top"></a>

## Table of Contents

- [Object Oriented Programming with Python Book](#object-oriented-programming-with-Python-Book)

## Object Oriented Programming with Python Book
### The Object Model
#### Terminology

Because large programs become increasingly difficult to maintain, OOP was created to make programming more modular and easier to maintain when it is in discreet chunks. The goal is to create an interaction between smaller parts, and not one big glob of interdependency and potential for breakage.

There are **classes** and **objects**. Classes are a single section with sub functions that all put out the same type of data object. "Every class defines a type, and every type has a class". **Objects** are the product of a class. Objects can also be referred to as **instances** or **instance objects**. "When we create a new object from a class, we say that we created a new class instance." Keep in mind that objects and instances are interachanageable and DWAI. 

Lastly, most everything in Python is an Object. Well, almost.

**Object**: anything that can be said to have a value is an object. That includes:
* numbers 
* strings 
* lists 
* functions 
* modules
* classes in and of themselves. 

**Not objects**: 
* statements 
* keywords
* variables (variables as the name/label that refer to the object held in memory)

A note on syntax, first, use Pascal case when naming classes, and:

>>We typically use nouns when discussing classes and objects. Classes and objects represent concrete (non-abstract) things. Many, but not all, methods are named with verbs; they represent actions and behaviors. The objects we create from classes are specific instances of the class nouns, and we manipulate them using the verbs provided by the method names.

An example of the dynamic between nouns and verbs in classes and methods:

```python
class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.hp = 100
        self.guild = None

    def move(self, dx, dy):
        print(f"{self.name} moves by ({dx}, {dy}).")

    def attack(self, target):
        print(f"{self.name} attacks {target}!")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP.")

    def join_guild(self, guild_name):
        self.guild = guild_name
        print(f"{self.name} joins {guild_name}.")
```

**Instantiation** is the process of creating a new object. Hiding data and functionality from the rest of the code base is known as **encapsulation**. In Python encapsulation is more symbolic than actual. It is the choice of the programmer not to have aspects interact, but isn't 'firewalled' in and of itself. 

* Encapsulation defines boundaries and interfaces, which helps you manage complexity as programs grow.
* Python “hides” by convention, not enforcement. We signal what’s internal vs public and rely on method interfaces to control access.
* It also lets you enforce invariants and refactor safely: callers use the interface; internals can change without ripple effects.
* It supports abstraction: you think in terms of nouns (objects) and verbs (methods), not scattered implementation details.

**Polymorphism** is the ability for different data types to respond to the same interface. 

In **inheritance**, a class can acquire all the behaviors and properties of another class. This lets programmers define small, reusable classes and smaller, more specific classes for fine-grained, detailed behaviors. In inheritance, the inheriting class is called a subclass of the inherited class. The inherited class is, in turn, called a superclass of the subclass.

Here is an example of inheritance and polymorphism:

```python
class Plant:
    def __init__(self, name):
        self.name = name
        self.age_days = 0
        self.water_level = 0

    def water(self, amount=1):
        self.water_level += amount

    def grow(self):
        if self.water_level > 0:
            self.age_days += 1
            self.water_level -= 1

    def harvest(self):
        print(f"{self.name}: generic harvest (maybe nothing yet)")

class Tomato(Plant):
    def harvest(self):
        if self.age_days >= 5:
            print(f"{self.name}: harvested tomatoes!")
        else:
            print(f"{self.name}: not ready yet.")

class Wheat(Plant):
    def harvest(self):
        if self.age_days >= 7:
            print(f"{self.name}: harvested grain!")
        else:
            print(f"{self.name}: not ready yet.")
```

Plant holds general behaviors; subclasses can specialize them (inheritance). Different plants respond to the same harvest interface (polymorphism).

Further example of naming syntax:

```python
class Plant:
    def plant(self): ...
    def water(self, amount=1): ...
    def grow(self): ...
    def harvest(self): ...
```

#### Clases Define Objects

Python classes describe the characteristics of its objects. Classes provide a blueprint of the information its instances store and what those objects can do. The statement that creates the class is called a **class constructor**.

Most objects have data. Collectively, the data inside an object defines its **state**. An object's state is given by its **instance variables**, which store the object's data. These variables can be initialized, accessed, replaced, or mutated through the class's instance methods and from outside the class. A class's **instance methods** are functions that operate on instances of the class. Instance methods are shared by all class instances. The instance methods are often called **behaviors**.

In Python, the terms instance variable, attribute, and property sometimes get used interchangeably. However, they are different and shouldn't be misused:

* Instance variables are variables that are tied to an instance of a class.
* Attributes include all instance variables and instance methods.
* Properties are a special kind of method that enables syntax that makes the property look like an instance variable. You can use the property name like a variable name. Properties are usually associated with instance variables but can also be dynamically computed.

An example of a class method being called outside of the class itself:

```python
class GoodDog:

    def __init__(self, name):
        # self.name is an instance variable (state)
        self.name = name
        print(f'Constructor for {self.name}')

    # speak is an instance method (behavior)
    def speak(self):
        # We're using the self.name instance variable
        print(f'{self.name} says Woof!')

    # roll_over is an instance method (behavior)
    def roll_over(self):
        # We're using the self.name instance variable
        print(f'{self.name} is rolling over.')

sparky = GoodDog('Sparky') # Constructor for Sparky
sparky.speak()             # Sparky says Woof!
sparky.roll_over()         # Sparky is rolling over.

rover = GoodDog('Rover')   # Constructor for Rover
rover.speak()              # Rover says Woof!
rover.roll_over()          # Rover is rolling over
```

Let's break it down:

* __init__ is a magic method (also: dunder method) in Python. It's properly called the initializer method, the instance constructor, or the constructor. It initializes a new instance of an object. Magic methods are any methods whose name begins and ends with a double underscore.  The initialzier doesn’t create the object; it receives an already-created instance and initializes its state (e.g., sets instance variables). It typically returns None.

* The speak and roll_over methods tell a GoodDog instance to speak or roll over. Note the distinction between class constructors and instance constructors. The class constructor, such as `GoodDog()`, orchestrates the instantiation of an instance object. It first calls the static method __new__ to create an instance object of the class. The uninitialized object is then passed to the __init__ instance constructor where it gets initialized.   For clarity going forward, we'll use the following terminology:

    * Constructor refers to the class constructor function, e.g., `GoodDog()`, `list()`, `range()`, etc.
    * __new__ for the __new__ method.
    * **Initializer** refers to the __init__ method.

##### Passing the Calling Object (self) to Instance Methods

Python handles passing the calling object to an instance method automatically.

How it Works:

1) Method Definition: When you define an instance method, you must include a parameter to receive the calling instance. By strong convention, this first parameter is always named self.

```python
class GoodDog:
    # 'self' is the required first parameter in the definition
    def speak(self):
        # 'self' refers to the instance the method was called on
        print(f'{self.name} says Woof!')
```
2) Method Call: When you call the method on an instance, you don't provide an argument for the self parameter. Python automatically passes the instance object (sparky in this case) as the first argument.

```python
sparky = GoodDog('Sparky')

# You call it with no arguments
sparky.speak()
```

The call `sparky.speak()` is essentially syntactic sugar for `GoodDog.speak(sparky)`. Inside the speak method, the self parameter is automatically bound to the sparky object, giving you access to its state, like `self.name`.

In summary: You must include self in the method's definition, but Python handles passing the instance to it during the call.

Crucial Aspects to note:

* A class defines the behaviors for the instance objects of the class.
* You can instantiate multiple instances of a class.
* The instance objects are distinct from each other.
* The instance objects share the same methods but have different states.

#### Inheritance

Take this example:

```python

class Pet:

    def __init__(self, name): 
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')

class Dog(Pet): #non duplicated code, class dog etc inherits the overall class of Pet

    # __init__ method removed
    def speak(self):
        print(f'{self.name} says Woof!')

    def roll_over(self):
        print(f'{self.name} is rolling over.')

class Cat(Pet):

    # __init__ method removed
    def speak(self):
        print(f'{self.name} says Meow!')

class Parrot(Pet):

    # __init__ method removed
    def speak(self):
        print(f'{self.name} wants a cracker!')

sparky = Dog('Sparky')
fluffy = Cat('Fluffy')
polly = Parrot('Polly')

sparky.roll_over()

for pet in [sparky, fluffy, polly]:
    pet.speak()
```

What's happening in this code? 

After allocating some memory for the instance, Python tries to call` __init__ `on the object's class. However, none of our subclasses has a `__init__` method. Python persists! It looks to the superclass for a method with the same name. In this case, it finds `__init__ `in the Pet class and invokes it. `Pet.__init__ `creates and initializes a `self.name `instance variable in the new object and prints an informative message.

The superclass holds general, shared behaviors, and the subclass holds specific, specialized ones.

This structure allows subclasses to inherit all the common functionality from the superclass without duplicating code. The subclass can then add its own unique behaviors or override inherited ones to suit its specific needs.

Pet (Superclass): Contains the general __init__ and eat methods because all pets have a name and eat.
Dog and Cat (Subclasses): Inherit __init__ and eat from Pet. They then define their own specific speak methods because a dog's "Woof!" is different from a cat's "Meow!". The Dog class also has a roll_over method, which is a behavior specific only to dogs in this example.

##### What's up with `type_name = type(self).__name__.`?

This line is a way to programmatically get the name of the class as a string. It works in three steps:

`self`: `self` refers to the current instance of the class. When the code runs `sparky = Dog('Sparky')`, inside the `__init__` method, `self `is the sparky object.

`type(self)`: The built-in `type()` function returns the class (or type) of an object. So, type(self) gives you the Dog class itself.

`.__name__`: Every class in Python has a special` __name__ `attribute that holds the class's name as a string. When you access this attribute on the Dog class, you get the string 'Dog'.

So, the line effectively says, "Get the current object, find out its class, and then get the name of that class as a string." The chapter also mentions an alternative way to write this line which you might find clearer: self.__class__.__name__. Both type(self) and self.__class__ return the object's class.

My own example:

```python

class SuperHero:

    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')

    def hit(self):
        print(f'{self.name}: Pow-Pow-Pow')

class TeleKenesis(SuperHero):

    def be_annoying(self):
        print(f"{self.name}: Of course I can host the Phoenix Force")

class Wolverine(SuperHero):

    def growl(self):
        print(f"{self.name}: I develop child soldiers but at least I care")


kid_omega = TeleKenesis('Quentin_Quire')
logan = Wolverine('Logan')
```

Page Reference: [The Object Model](https://launchschool.com/books/oo_python/read/object_model)

[Back to the top](#top)

*** 

### Classes and Objects


Page Reference: [Classes and Objects](https://launchschool.com/books/oo_python/read/classes_objects)

[Back to the top](#top)
***