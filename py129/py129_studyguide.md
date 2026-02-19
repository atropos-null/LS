# PY129 Study Guide, Moral Version

<a name="top"></a>

## Table of Contents

- [What You Are Actually Being Tested On](#what-you-are-actually-being-tested-on)
- [Classes and Objects](#classes-and-objects)
- [Inheritance](#inheritance)
- [The `is` Operator and `id()` Function](#the-is-operator-and-id-function)
- [Exceptions](#exceptions)
- [Reading OO Code](#reading-oo-code)
- [Create a Code Spike](#create-a-code-spike)

Page Reference: [Study Guide](https://launchschool.com/lessons/aa7db174/assignments/6478d2d2)

## What You are Actually Being Tested On

The PY129 assessment evaluates you on ​two equally important dimensions​: your technical knowledge and your communication abilities.

### Core Technical Knowledge
You need to demonstrate mastery of the Object-Oriented Programming concepts from PY120, including:
* Classes and objects (instantiation, instance/class/static methods, attributes)
* Inheritance and the Method Resolution Order (MRO)
* Encapsulation and polymorphism
* Magic methods and custom operators
* Exception handling
* Working with collaborator objects

### Communication and Professional Skills

Beyond just knowing the material, the interview specifically assesses your ability to:

*​Speak with Precision and Clarity​*

You must explain concepts using correct vocabulary and clear reasoning. As stated in the interview tips: "You should speak in a clear tone and explain concepts with precision and correct vocabulary."

*​Think and Code Under Pressure​*

The interview simulates a real job interview environment. You'll need to demonstrate how you approach problems, work through code examples, and recover from mistakes in real-time.

*​Drive Technical Conversations​*

You're expected to "speak and drive the conversation" - teaching and presenting OOP topics rather than just answering yes/no questions.

### Why Communication Matters So Much

Launch School emphasizes practicing speaking about technical topics before the interview because "speaking and articulating concepts in front of people is a unique experience" and "talking about it in an interview is different" from just knowing the material. They strongly recommend attending peer-led study groups to practice this skill.

The assessment recognizes that being able to clearly communicate technical concepts is as important for a professional software engineer as understanding the concepts themselves.

### The 5 Default Phrases (Memorize These)

1. **Responsibility Anchor**

Use this to start almost any answer.

>“I’d start by clarifying which object owns this responsibility, because that object should also own the state that changes over time.”

This immediately signals:

* OOP maturity
* encapsulation
* design-first thinking

2. **Delegation Justification**

Use when explaining why something is not in the current class.

>“This object doesn’t own that state, so it delegates the behavior to a collaborator through a public method.”

This covers:

* collaboration
* message passing
* loose coupling

3. **Encapsulation Defense**

Use when explaining why you don’t access attributes directly.

>“I’d avoid reaching into another object’s data and instead ask it for what I need, so its internal representation can change safely.”

4. **Change-Resilience Framing**

Use when asked about refactoring or future changes.

> “This design keeps knowledge localized, so if requirements change, the impact is limited to one object.”

This shows:

* foresight
* maintainability
* real-world thinking

5. Pattern Naming Close

Use when you want to wrap up cleanly.

> “The coordinator directs interactions without taking ownership of the collaborators’ internal behavior.”

This gives your answer a clear ending.

[Back to the top](#top)

## Classes and Objects

> OOP is not about classes.
>
> It is about managing complexity by controlling how responsibility flows through time.
>
>Classes are scaffolding.
>
>Objects are actors.
>
>Methods are conversations.

A **class** is a blueprint or template for creating objects. It defines a set of attributes (data) and methods (behaviors) that the objects created from it will have.

An **object** is an instance of a class. It's a concrete entity created from the class blueprint, with its own specific state.

Think of a `GoodDog` class. The class itself defines what every dog has (like a name) and what every dog can do (like speak). An individual dog, like `sparky`, is an object created from that class, with its own specific name.

```python
class GoodDog:    

    def __init__(self, name):        
        self.name = name    
    
    def speak(self):        
        print(f'{self.name} says Woof!')

sparky = GoodDog('Sparky')
sparky.speak()#  Output: Sparky says Woof!
```

#### Other ways to say the same thing:

##### 1. The "Encapsulation" Focus (Technical)

"An object is a self-contained entity that encapsulates both data (attributes) and behavior (methods). It is a runtime 
instance of a class that occupies a specific block of memory."

Why this is good: It uses the term "encapsulates," which is a core OOP pillar often tested in exams.

##### 2. The "Blueprint" Analogy (Conceptual)

"If a class is the blueprint, an object is the actual house built from it. While all houses from that blueprint share the same structure, each individual object has its own unique state (e.g., its own paint color or address)."

Why this is good: It clearly distinguishes between the definition (class) and the manifestation (object).

##### 3. The "Identity, State, and Behavior" Trio (Academic)

"An object is characterized by three things:

Identity: Its unique location in memory.

State: The data stored in its attributes at any given time.

Behavior: The actions it can perform via methods defined in its class."

Why this is good: Many OOP exams look for these specific three terms (Identity, State, Behavior).

##### 4. The Concise Pythonic Definition

"An object is a realization of a class that bundles variables (state) and functions (behavior) into a single unit."


### Instantiation and `__init__`


**Instantiation** is the process of creating a new object (an instance) from a class. You do this by calling the class as if it were a function, like `GoodDog()`.

The `__init__` method is a special method, often called an **initializer**, that Python calls automatically right after an object has been created. Its job is to set up the initial state of the object by initializing its instance variables.

```python
class GoodDog:
    # The __init__ method initializes the new object's state
    def __init__(self, name, age):
        # self.name and self.age are instance variables
        self.name = name
        self.age = age

# We instantiate a GoodDog object, which calls __init__
sparky = GoodDog('Sparky', 5)
```

In this example, when we create `sparky`, the `__init__` method runs, assigning `'Sparky'` to `self.name` and `5` to `self.age` for that specific object.

#### Another way to say it

> "Instantiation is the process of creating a specific, unique object (an instance) from a class template."

When you instantiate a class, you are allocating memory for a new object and calling the class's constructor to set its initial state. In Python, this is done by "calling" the class like a function, like above. This happens in two steps: 
1. **Creation** (`__new__`): Python creates the raw object in memory.
2. **Initialization** (`__init__`): Python sets the initial values (attributes) of that object.

Analogies to use:

**The Cookie Cutter**: The class is the cookie cutter; instantiation is the act of pressing it into the dough; the object is the resulting cookie.

**The Factory**: The class is the factory schematic; instantiation is the assembly line process; the object is the finished product coming off the line.


##### Exam-Ready Summary:

> "Instantiation is the 'birth' of an object. It transforms a static class (the code) into a dynamic object (an active entity in the computer's memory) with its own distinct identity."

Checklist of terms to use if you get a long-answer question:

* **Constructor**: The method that handles instantiation (in Python, usually referred to as `__init__`). It is called automatically when a new object is created from a class, and it is used to initialize the object's attributes.
* **Memory Allocation**: The system setting aside space for the new object.
* **Initialization**: Setting the starting state of the object.


`__init__` lives at the object level (instance protocol): it is a method bound to a class, invoked by the interpreter after `__new__ `has already allocated the instance. 


### Instance Variables, Class Variables, and Scope


#### Instance Variables (The "Unique" Data)

Instance Variables belong to a specific object instance. They hold the state of that particular object. They are defined inside methods, typically `__init__`, and are prefixed with `self` (e.g., `self.name`). Each object has its own copy of instance variables.

* **Definition**: Variables that are unique to each instance. They represent the individual state of an object.
* **Location**: Usually defined inside the `__init__` method.
* **Access**: Always prefixed with `self` (e.g., `self.name`).
* **Storage**: They live in the object's local namespace (`instance.__dict__`).

#### Class Variables (The "Shared" Data)

Class Variables are shared by all instances of a class. They belong to the class itself, not to any single object. They are defined directly within the class, outside of any instance methods.

* **Definition**: Variables that are shared by all instances of a class. They represent class-level state or constants.
* **Location**: Defined directly within the class body, outside any methods.
* **Access**: Can be accessed via the Class name (`GoodCat.NUMBER_OF_CATS`) or an instance (`cat1.NUMBER_OF_CATS`).
* **Storage**: They live in the class’s namespace (`Class.__dict__`).

Under the hood, `@classmethod` is a Descriptor. When you access it, Python's internal machinery intercepts the call and automatically injects the class object as the first argument. This is the same magic that injects self into regular methods!

```python
class GoodCat:
    # A class variable shared by all instances
    NUMBER_OF_CATS = 0

    def __init__(self, name):
        # An instance variable, unique to each instance
        self.name = name
        GoodCat.NUMBER_OF_CATS += 1

cat1 = GoodCat('Paws')
cat2 = GoodCat('Whiskers')

print(cat1.name)                # Paws
print(cat2.name)                # Whiskers
print(GoodCat.NUMBER_OF_CATS)   # 2
```

**Other Common Options for Class Variables**


1. **Managing "Global" Class State**
Sometimes you want a variable that all instances of a class share (like a configuration setting or a counter), and you want a clean way to update it.

```python
class Connection:
    # Class-level variable (shared by all instances)
    _default_timeout = 30 

    def __init__(self, host):
        self.host = host
        # Each instance uses the current class-level timeout
        self.timeout = Connection._default_timeout

    @classmethod
    def set_default_timeout(cls, seconds):
        """Changes the timeout for all FUTURE connections."""
        if seconds > 0:
            cls._default_timeout = seconds
        else:
            print("Invalid timeout!")

# All new connections will have 30s timeout
c1 = Connection("google.com")

# Change the 'global' setting for the class
Connection.set_default_timeout(60)

# This new connection will have 60s timeout
c2 = Connection("github.com")

print(c1.timeout) # 30
print(c2.timeout) # 60
```

2. **Ensuring Inheritance Works Correctly**
A major reason to use `@classmethod` (with `cls`) instead of a `@staticmethod` or a hardcoded class name is to support Subclassing. When a child class calls a class method, `cls` refers to the Child, not the Parent.

```python
class Robot:
    species = "Basic Bot"

    @classmethod
    def identify(cls):
        # Using cls.species ensures we get the species 
        # of whatever class is actually calling this.
        print(f"I am a {cls.species}")

class BattleBot(Robot):
    species = "Warrior Bot"

# Both call the SAME method defined in the parent
Robot.identify()     # Output: I am a Basic Bot
BattleBot.identify() # Output: I am a Warrior Bot
```

If we had hardcoded `Robot.species` inside the method, `BattleBot.identify()` would have incorrectly printed "Basic Bot".

3. **The "Registry" Pattern**

This is used when you want a class to automatically keep track of all its subclasses. This is very common in plugin systems or frameworks.

```python
class Shape:
    # A list to keep track of every type of shape we create
    registry = []

    @classmethod
    def register_subclass(cls):
        """Adds the current class to the registry."""
        cls.registry.append(cls)

# When we define a new shape, we 'register' it
class Circle(Shape):
    pass
Circle.register_subclass()

class Square(Shape):
    pass
Square.register_subclass()

# Now the parent class 'knows' about its children without imports
print(f"Known shapes: {[s.__name__ for s in Shape.registry]}")
# Output: Known shapes: ['Circle', 'Square']
```

Just like `self`, `cls` is not a reserved keyword in Python; it’s a naming convention. You could name it `rainbow_unicorn`, and the code would run. However, always use `cls`. It is the universal standard in the Python community, and using anything else will confuse other developers (and your future self).


**Fun Fact: Calling `@classmethod` from an Instance**

A common misconception is that you can only call class methods on the class (e.g., `MyClass.my_method()`). In reality, you can call them on an instance as well:

```python
obj = MyClass()
obj.my_class_method() # This works!
```

Why do this? If you have an object and you want to create another object of the exact same type (without knowing exactly what subclass obj is), you can call a factory method on the instance.


#### A Detour: Factory Method 

A **Factory Method** is essentially a "Specialized Maker" for objects.

Instead of you manually building an object by calling the class directly (e.g., `User()`), you call a method that does the building for you and returns the finished product.

Think of it like this:

* Standard Constructor (`__init__`): You go to the store, buy all the parts, and assemble the bike yourself.
* Factory Method: You call a bike shop, tell them what you need, and they hand you a fully assembled bike.

Why call it on an Instance?
This is the "magic" part I mentioned. It allows for Polymorphism in creation.

Imagine you have a piece of code that receives an object, but it doesn't know (or care) if that object is a BasicUser, a ProUser, or an AdminUser. It just knows it has a "User" object.

If you want to create a duplicate or a sibling of that object without knowing its exact class, the @classmethod factory is your best friend.

**The Example: A Game Spawner**

```python

class Enemy:
    def __init__(self, health):
        self.health = health

    @classmethod
    def spawn_reinforcement(cls):
        """The Factory Method"""
        print(f"Spawning a new {cls.__name__}!")
        return cls(health=100) # Creates an instance of 'cls'

class Goblin(Enemy):
    pass

class Dragon(Enemy):
    pass

# --- The Scenario ---

def trigger_event(some_enemy):
    # This function doesn't know if 'some_enemy' is a Goblin or a Dragon.
    # It just knows it's an 'Enemy'.
    
    # By calling the factory method on the INSTANCE, 
    # Python automatically knows which class to use for 'cls'.
    new_enemy = some_enemy.spawn_reinforcement()
    return new_enemy

# 1. We have a Goblin
g = Goblin(50)
# 2. We pass it to the generic function
spawned_1 = trigger_event(g) 
# Output: "Spawning a new Goblin!"

# 3. We have a Dragon
d = Dragon(500)
# 4. We pass it to the SAME generic function
spawned_2 = trigger_event(d) 
# Output: "Spawning a new Dragon!"
```

**What happened here?**

1. When you call `some_enemy.spawn_reinforcement()`, Python looks at the instance `some_enemy`.
2. It sees that the method is a `@classmethod`.
3. It finds the Class that the instance belongs to.
4. It passes that Class into the method as the `cls` argument.

**Summary of Benefits**:

* Encapsulation: The logic for "how to spawn a reinforcement" (e.g., setting the default health to 100) is hidden inside the factory method.

* Type Safety: You don't have to write if isinstance(obj, Goblin): return Goblin(). The @classmethod handles the "type-matching" automatically.

* Flexibility: If you add a new Zombie class later, the trigger_event function will work for Zombies immediately without changing a single line of code.

**When to reach for Class Methods?**

Ask yourself: "Does this logic need to know which class it is part of?"

If Yes (to create an instance or check a class variable) → `@classmethod`.
If No (it's just a helper function) → `@staticmethod`.
If it needs to change an object's data → Regular method (`self`).


#### We also have Scope

**Scope** determines where variables can be accessed. Instance variables belong to the object, while class variables belong to the class. If you try to change a class variable using self, it may create a new instance variable instead of modifying the class variable.

##### The Common Pitfall: "Shadowing" 

The Oops:

```python
class GoodCat:
    species = "Feline"  # Class Variable

cat1 = GoodCat()
cat1.species = "Tabby" # This DOES NOT change the class variable!
```

The Yeah:

```python
class GoodCat:
    NUMBER_OF_CATS = 0  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable
        GoodCat.NUMBER_OF_CATS += 1

cat1 = GoodCat('Paws')
cat2 = GoodCat('Whiskers')

# CORRECT way to modify/access class variables
print(GoodCat.NUMBER_OF_CATS )  # 2

# THE PITFALL: Accidental Shadowing
cat1.NUMBER_OF_CATS  = 999  # This creates an INSTANCE variable on cat1
print(cat1.NUMBER_OF_CATS )    # 999 (looks at instance first)
print(cat2.NUMBER_OF_CATS )    # 2 (looks at class)
print(GoodCat.NUMBER_OF_CATS ) # 2 (class variable remains unchanged)
```

If an exam question asks "how many copies of a class variable exist?", the answer is always **one**. If it asks "how many copies of an instance variable exist?", the answer is **one per instance**.


### Instance Methods vs. Class Methods vs. Static Methods


#### Instance Methods (The Doers)

> "Instance methods are used when the logic requires knowledge of a specific object's data (attributes)."

- Operate on a specific object instance.
- The first parameter is conventionally `self`, which refers to the instance calling the method. 
    - Alternative way to say it: "Implicitly pass the object as the first argument."
- They can access and modify the object's state (instance variables).
- They define the behavior of an object.
- They have access to both the instance (via `self`) and the class (via `self.__class__`).

```python
class GoodDog:

    def __init__(self, name):
        self.name = name

    def speak(self): # Instance method
        return f'{self.name} says arf!'

dog = GoodDog("Pugsly")
print(dog.speak()) # Pugsly says arf!
```

#### Class Methods ("The Factories")

> "Class methods are used when the logic involves the class as a whole, such as modifying class-level variables or providing alternative constructors."

- Operate on the class itself, not an instance.
- The first parameter is conventionally `cls`, which refers to the class.
    - Alternative way to say it: "Implicitly pass the class as the first argument."
- They are marked with the `@classmethod` decorator.
- They can access and modify class state (class variables), but not instance state.
- They are often used to create a new instance of the class from a different type of data (e.g., creating a User object from a JSON string)

```python
class Animal:
    @classmethod
    def make_sound(cls): # Class method
        print(f'{cls.__name__}: A generic sound')

dog = Animal()
dog.make_sound() # Animal: A generic sound
```

#### Static Methods (The "Namespace Utilities")

> "Static methods are used for utility logic that is related to the class conceptually but doesn't need to access any class or instance data."

- Don't operate on the instance or the class. They are essentially regular functions grouped with a class for organizational purposes. 
- They do not take `self` or `cls` as their first parameter.
    - Alternative way to say it: "Pass nothing automatically. You must provide all arguments manually."
- They are marked with the `@staticmethod` decorator.
- They do not know anything about the state of the object or the class, thus they cannot access or modify class or instance state.
- They are often used for utility functions that are related to the class.

```python
class TheGame:
    @staticmethod
    def show_rules(): # Static method
        print("These are the rules of the game.")

uno = TheGame()
uno.show_rules()
```

#### Advanced Example: The "All-in-One" Class

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    # 1. Instance Method: Needs the specific pizza's ingredients
    def __repr__(self):
        return f'Pizza({self.ingredients})'

    # 2. Class Method: A "Factory" to create a specific type of pizza
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    # 3. Static Method: Independent logic (just checks a string)
    @staticmethod
    def validate_ingredient(ingredient):
        allowed = ['mozzarella', 'tomatoes', 'pepperoni']
        return ingredient in allowed

# Usage:
p = Pizza.margherita()  # Using class method as a factory
print(p)               # Pizza(['mozzarella', 'tomatoes'])
print(Pizza.validate_ingredient('pineapple')) # False (Static utility)
```

[Back to the top](#top)

***

## Attributes and State


> "State is the configuration of an object's properties at a specific moment in time. It represents the object's identity and determines how it will react to methods."

**State (The "Snapshot")** refers to the data that an object holds at any given time. This data is stored in its instance variables. For example, a `GoodDog` object's state might include its name and age. State is dynamic; it changes as the program runs (e.g., a `bank_account.balance `changes after a deposit).

**Another way to say it**:  "State is encapsulated within data attributes (instance variables). If you change the value of an instance variable, you have changed the object's state."

**Analogy**: If you pause a movie, the "state" is the specific frame, the characters' positions, and the remaining time.

> "An attribute is any name associated with an object. Python divides attributes into two categories: 
>   1. Data Attributes: (Variables) These represent the State.
>   2. Methods: (Functions) These represent the Behavior."

**Attributes (The "Dot Notation" Rule)** is a broader term that includes all of an object's instance variables and its instance methods. In Python, the term **Attribute** is the umbrella term for anything following the dot (`.`). Therefore, `sparky.name` is an attribute (an instance variable), and `sparky.speak` is also an attribute (an instance method).

**Fun Fact**: You can see all of an object's data attributes by looking at `object.__dict__`.

Attributes: Any member of a class or object that is accessed via dot notation.
- **Data Attributes**: Store data (Variables like `self.name`).
- **Methods**: Store logic/behavior (Functions like `self.speak()`).
- **Python Fact**: In Python, methods are technically "callable attributes."

#### The "Everything is an Attribute" Example

This is a great snippet to include because it shows you understand how Python handles these internally:

```python

class GoodDog:
    def __init__(self, name):
        self.name = name  # Data Attribute

    def bark(self):       # Method (Callable Attribute)
        return "Woof!"

sparky = GoodDog("Sparky")

# Testing for attributes
print(hasattr(sparky, "name"))  # True (Data attribute)
print(hasattr(sparky, "bark"))  # True (Method attribute)

# State is usually stored here:
print(sparky.__dict__)          # {'name': 'Sparky'}
```

**Question**: "What is the relationship between state and attributes?" 

**Answer**: "State is the current value of an object's data attributes. Attributes is the broader category that includes both the data (State) and the methods (Behavior)."

### Calling and Accessing Attributes: `self`, `cls`, `obj.__class__`


> Both `self` and `cls` are conventions. Python automatically passes the instance or class as the first argument, and by convention, we name that parameter `self` or `cls`.

* **`self` ("The Instance Binder")**: Inside an instance method, `self` is a reference to the specific object instance the method was called on. It's used to access that object's attributes, like `self.name`. `self` is the bridge between the method and the object’s memory space.

**Alternative way to say it**: "`self` represents the explicit binding of an instance to a method. Python requires `self` to be explicitly defined in the signature so the method knows whose state it is modifying."

**Exam Phrase**: "`self` allows for encapsulation by ensuring that a method only interacts with the data belonging to the specific object that called it."

* **`cls` ("The Class Binder")**: Inside a class method, `cls` is a reference to the class itself. It's used to access class-level attributes, like a class variable or another class method.

**Alternative way to say it**: "`cls` is a reference to the class itself, ensuring that even if a class is inherited, the class method has access to the correct class context (the child or the parent) that invoked it."


* **`obj.__class__` ("The 'Genetic' Link")**: This is an attribute on any object that points back to the class it was created from. You can use it to access class attributes from an instance. For example, `sparky.__class__.number_of_dogs` would work if `number_of_dogs` were a class variable.

**Alternative way to say it**: "This is a metadata attribute that reveals the 'type' of the object. It allows an instance to 'look up' and see the blueprints it was built from."

**Pro Tip**: Accessing a class variable via self.var_name is common, but using self.__class__.var_name is safer because it avoids the "shadowing" 


| Goal                  | How to do it                | Context                        |
|-----------------------|-----------------------------|-------------------------------|
| Access instance data  | `self.attribute`            | Inside an Instance Method      |
| Access class data     | `cls.attribute`             | Inside a Class Method          |
| Access class data     | `ClassName.attribute`       | Anywhere                       |
| Access class data     | `obj.__class__.attribute`   | From an Instance               |


**Note on `type(obj)` vs `obj.__class__`**

For the exam, it's worth noting:

- `sparky.__class__` is the attribute that stores the class.
- `type(sparky)` is the built-in function that retrieves it.
- They both point to the same thing: <class '__main__.GoodDog'>.

> "In Python, `self` and `cl`s are not reserved keywords, but conventions. They represent the first argument passed to methods. This design choice makes the connection between an object and its methods explicit rather than hidden."

**Explicit vs Implicit**:

Explicit Definition: You must include `self` or `cls` as the first parameter when writing the method code.

Implicit Calling: You do not pass `self` or `cls` when you call the method. Python's "syntactic sugar" handles it for you.

```python
# What you write:
sparky.speak()

# What Python actually does behind the scenes:
GoodDog.speak(sparky)  # It passes the instance into the first argument!
```

### Creating and Using Properties, Getters, and Setters

**Getters and Setters** are methods that provide controlled access to an object's attributes. A getter retrieves an attribute's value, and a setter modifies it. This allows you to add logic, like validation, when an attribute is accessed or changed.

```python
class GoodDog:
    def __init__(self, name):
        self._name = name # Convention for internal use

    # Getter
    def name(self):
        return self._name

    # Setter
    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        self._name = new_name

sparky = GoodDog("Sparky")
print(sparky.name()) #Sparky
```

**Properties** are the more "Pythonic" way to manage getters and setters. They let you use the simple attribute access syntax (e.g., `sparky.name`) while still running your getter and setter methods in the background.

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property # This defines the getter for a 'name' property
    def name(self):
        return self._name

    @name.setter # This defines the setter for the 'name' property
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        self._name = value

kate = Person('Kate')
print(kate.name)         # Calls the getter
kate.name = 'Katherine'  # Calls the setter
```

#### The "Uniform Access Principle" 

**Definition**: The "Uniform Access Principle" (UAP) is the formal name for why we use properties. The UAP suggests that the way an object's services are accessed should be consistent, regardless of whether they are implemented as variables or methods. This is where properties in Python come in handy, as they allow you to use the same syntax for accessing both attributes and methods, providing a uniform interface.

**In plain English**: The person using your class shouldn't have to care if `kate.name` is a simple variable or a complex method. They just use the dot.

### Python Setters Explained

#### How Python Connects `__init__` to a Setter

When you assign a value to an attribute in `__init__`, Python automatically uses the **setter** if that attribute is defined as a **property**. 

##### Example

```python
class Example:
    def __init__(self, value):
        self._value = None  # private attribute used to store the actual value
        self.value = value  # This line calls the setter!
    
    @property
    def value(self):
        """Getter method"""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Setter method"""
        print(f"Setting value to {new_value}")
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value

ten = Example(10) # Setting value to 10
```

#### How It Works

1. The `@property` decorator creates a property object for `value`.
2. When you write `self.value = something`, Python checks if `value` is a property.
3. If it finds a property with a setter defined, it calls the setter method.
4. This works through Python's **descriptor protocol** - properties are descriptors that intercept attribute access.

#### Behind the Scenes

```python
# When you do this:
self.value = 10

# Python essentially does this:
type(self).value.__set__(self, 10)  # Calls the setter method
```

##### Validation in `__init__` (The "Clean Slate" Rule)

By calling the setter inside `__init__`, you ensure that an object cannot be created in an invalid state. The validation logic is centralized in one place (the setter) and enforced from the very first second the object exists.

#### What Happens Without a Setter? 

##### Scenario 1: Property Without Setter (Read-Only)

If a property doesn't have a setter, Python raises an **AttributeError** when you try to assign to it. 

```python
class Example:
    def __init__(self, value):
        self._value = value
        self.value = 10  # AttributeError: property 'value'  of 'Example' has no setter
    
    @property
    def value(self):
        """Only a getter, no setter"""
        return self._value
    
ten = Example(10)
```

**The Workaround:** Set the internal attribute directly

```python
class Example:
    def __init__(self, value):
        self._value = value  # ✅ Set the internal attribute directly
    
    @property
    def value(self):
        """Read-only property"""
        return self._value

obj = Example(42)
print(obj.value)  # ✅ Works: 42
obj.value = 100   # ❌ AttributeError: property 'value' has no setter
```

#### Scenario 2: No Property at All (Regular Attribute)

If there's no property decorator, it's just a regular attribute assignment:

```python
class Example:
    def __init__(self, value):
        self.value = value  # ✅ Just creates a regular attribute

obj = Example(42)
obj.value = 100  # ✅ Works fine - it's a normal attribute
```

#### Why Use Setters?

##### Regular Assignment vs.  Setter

| Feature | Regular Assignment | Setter |
|---------|-------------------|--------|
| **Syntax** | `self.attr = value` | `self.attr = value` (looks the same!) |
| **Storage** | Direct | Goes through setter method |
| **Validation** | None | ✅ Can validate |
| **Side effects** | None | ✅ Can trigger other code |
| **Type conversion** | None | ✅ Can convert/transform |
| **Performance** | Faster | Slightly slower (method call) |

#### Common Use Cases

##### 1. Validation

```python
class User:
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value
```

##### 2. Type Conversion

```python
class Temperature:
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = float(value)  # Always convert to float
```

##### 3. Side Effects / Triggering Actions

```python
class GUI:
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = value
        self.refresh_display()  # Update the UI when text changes!
```

##### 4. Computed/Derived Values

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height
    
    @area.setter
    def area(self, value):
        # Keep aspect ratio, adjust size
        ratio = (value / self. area) ** 0.5
        self._width *= ratio
        self._height *= ratio
```

##### 5. Backwards Compatibility

```python
class OldClass:
    def __init__(self):
        self. old_name = "value"  # Original attribute

# Later, you want to rename but keep old code working:
class NewClass:
    def __init__(self):
        self._new_name = "value"
    
    @property
    def old_name(self):  # Old name still works
        return self._new_name
    
    @old_name.setter
    def old_name(self, value):
        self._new_name = value
```

##### Quick Reference

**Three Scenarios:**
- **With property + setter**: Assignment calls the setter method (validation, side effects, etc.)
- **With property, no setter**: Assignment raises `AttributeError` (read-only)
- **No property at all**:  Assignment works normally (creates/updates regular attribute)

**Key Takeaway:** The beauty of properties is that the syntax looks identical to regular attribute access, but you get all the control of a method! 

### Access Control in Python

Python doesn't have strict private attributes like some other languages. Instead, it relies on naming conventions:

- **Single Underscore (`_name`)**: This is a convention that tells other developers that an attribute is intended for internal use within the class and should not be accessed directly from outside. Python does not enforce this.
    - The **"Social Contract"**: It’s a "gentleman’s agreement" between programmers. It says: "I might change how this works later, so don't touch it directly if you want your code to keep working."

- **Double Underscore (`__name`)**: This triggers a feature called **name mangling**. Python renames the attribute to `_ClassName__name`, making it harder to access accidentally from outside the class or from a subclass. It's used for Inheritance Safety, preventing naming conflicts in inheritance. 
    - **Stated alternatively**: "Name mangling prevents attributes from being accidentally overridden by subclasses."
    - If class `Dog` has `__mood`, Python renames it to `_Dog__mood`. If a subclass `Bulldog` also has `__mood`, it becomes `_Bulldog__mood`.

Btw, there's also a deleter property but its not covered in the materials.


| Decorator        | Action  | Triggered by...         | Typical Use                  |
|------------------|---------|-------------------------|------------------------------|
| `@property`      | Getter  | `x = obj.attr`          | Formatting data for display  |
| `@attr.setter`   | Setter  | `obj.attr = val`        | Validation and type checking |
| `@attr.deleter`  | Deleter | `del obj.attr`          | Cleanup or logging           |



#### Better Ways to Say It (Exam Vocabulary)

* Instead of saying "internal attribute," try using "underlying attribute." (e.g., `_name` is the underlying attribute for the name property).
* Instead of saying "it runs a method in the background," use "intercepts attribute access."
* Instead of "adding logic to variables," try  "managed attributes."


### Encapsulation and Polymorphism

These are two fundamental principles of OOP.

#### Encapsulation

**Encapsulation** refers to two things:
1. It is the practice of bundling data (attributes) and the methods that operate on that data together within a single unit (a class).
2. It is also the hiding of the internal state of an object from the outside world and only exposing a controlled public interface (through methods and properties). 

Getters, setters, and the underscore conventions are tools for encapsulation.

Here is an example from the curriculum that demonstrates encapsulation in action.

```python

class SmartLamp:
    def __init__(self, color):
        # The setter is called during instantiation
        self.color = color

    @property  # This decorator defines the getter
    def color(self):
        return self._color

    @color.setter  # This decorator defines the setter for the 'color' property
    def color(self, new_color):
        # Validation logic is placed inside the setter property
        if not isinstance(new_color, str):
            raise TypeError('Color must be a color name.')

        self._color = new_color

    def glow(self):
        # This method can now use the public property or the internal variable
        return (f'The lamp glows {self.color}.')


lamp = SmartLamp('blue')
print(lamp.glow())          # The lamp glows blue.

# We use simple attribute assignment, which calls the setter method
lamp.color = 'red'
print(lamp.glow())          # The lamp glows red.

# Accessing the attribute calls the getter method
print(f"The lamp's current color is: {lamp.color}") # The lamp's current color is: red

# The setter's validation logic still protects the object's state
try:
    lamp.color = 12345
except TypeError as e:
    print(e)                # Color must be a color name.
```

**How It Works**

1. **​The Getter** (`@property`)​: The `@property` decorator is placed above a method with the same name as the desired property (color). This turns the method into a "getter." Now, when you access `lamp.color`, Python automatically calls this method and returns its result.

2. **​The Setter** (`@color.setter`)​: The setter decorator is named after the getter method (`@color.setter`). This links it to the color property. When you assign a value, like `lamp.color = 'red'`, Python calls this setter method, passing `'red'` as the `new_color` argument. This is where we place our validation logic.

3. **​The `__init__` Method**​: Notice the change in `__init__`. Instead of assigning directly to `self._color`, we now assign to `self.color`. This is a crucial improvement. It means that the validation logic inside the setter is executed ​even when the object is first created​. If you tried to create a SmartLamp with an invalid initial color (`SmartLamp(99)`), it would raise the `TypeError` immediately.

4. **​The Underlying Variable**​:  The property acts as a proxy for the private storage variable (`self._color`). This allows the class to intercept every attempt to read or write data, giving the class 'final say' over its own state."The properties `color` and `color.setter` act as the public interface that controls access to this internal variable.This approach gives you the best of both worlds: the safety of validation from getter/setter methods and the clean, intuitive syntax of direct attribute access.

5. Other ways to say it:
- **Public Interface**: `lamp.color` is the interface the user interacts with.
- **Implementation Details**: `self._color` is the internal implementation that the user shouldn't touch.
- **Data Integrity**: The setter ensures the "integrity" of the object's state (by preventing invalid colors).
- **Decoupling**: If you decide to change `self._color` to `self._hex_code` later, you only change the code inside the property. The person using your `SmartLamp` doesn't have to change their code at all. This is called **Decoupling**.

##### "Black Box Theory" and Bundling vs. Hiding

Encapsulation treats an object as a 'Black Box.' The outside world knows what the box can do (its public methods/properties), but it doesn't need to know how it does it or what's inside. This is called **Information Hiding**.

**"What is the main advantage of encapsulation?"**

* **Maintenance**: You can change the internal code without breaking external code.
* **Validation**: You can prevent garbage data from entering your object.
* **Readability**: It provides a clean, consistent way to interact with objects.


#### Polymorphism

**Polymorphism** means "many forms." In programming, polymorphism is the ability of different types of objects to provide a consistent interface for different underlying implementations. Instead of needing to know the specific type of an object, your code can be **type-agnostic**—it simply calls a method and trusts the object to respond appropriately.

**Another way to say it**: “Polymorphism means different objects respond to the same message in their own way.”

*   **Greek Roots:** "Poly" (many) and "Morph" (form).
*   **The Goal:** To allow one common interface to control many different data types.

**Use Polymorphism When**:
* You have multiple related types with common behavior
* You need to extend functionality frequently
* Building frameworks or plugin systems
* Testing requires mocking/stubbing

**❌ Avoid Polymorphism When**:
* The problem is simple and unlikely to change
* Performance is absolutely critical
* Only one implementation exists (YAGNI principle)
* It makes the code harder to understand

#### What are different ways to implement polymorphism?

In Python, there are four primary ways to implement polymorphism:

* **Primary 1: Inheritance (Formal / "Is-A" Relationship)**: Subclasses **override** a method inherited from a common superclass. This allows client code to treat them as generic versions of that superclass.

    * **Method Overriding**: When a child class provides a specific implementation for a method already defined in its parent.
    * **Dynamic Dispatch**: The "magic" where Python decides which version of a method to run **at runtime** based on the actual object type, not the variable type.

Subclasses override a method inherited from a common superclass, allowing client code to treat them as generic versions of that superclass.

```python

class Animal:    
    def move(self):        
        print(f'I am a {self.__class__.__name__}: I am not moving.') # Default behavior

class Fish(Animal):    
    def move(self):        
        print(f'I am a {self.__class__.__name__}: I am swimming.') # Overridden behavior
        
class Cat(Animal):    
    def move(self):        
        print(f'I am a {self.__class__.__name__}: I am walking.') # Overridden behavior

animals = [Fish(), Cat(), Animal()]
for animal in animals:    
    animal.move() # Dynamic Dispatch happens here

#Output
#I am a Fish: I am swimming.
#I am a Cat: I am walking.
#I am a Animal: I am not moving.
```

All the classes are explicitly related through the Animal superclass. The `Fish` and `Cat` classes override the move method to provide their own specific behaviors.

Even though the objects are of different types, the `for` loop can treat them all as Animals and call the move method on each one, demonstrating polymorphism through inheritance.

Here is another example:

```python
class Wedding:
    def __init__(self, guests, flowers, songs):
        self.guests = guests
        self.flowers = flowers
        self.songs = songs

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_wedding(self) # One simple, polymorphic call

class WeddingPreparer:
    def prepare_wedding(self, wedding):
        pass

class Chef(WeddingPreparer):
    def prepare_wedding(self, wedding):
        self.prepare_food(wedding.guests)

    def prepare_food(self, guests):
        print("Preparing food for the guests.")

class Decorator(WeddingPreparer):
    def prepare_wedding(self, wedding):
        self.decorate_place(wedding.flowers)

    def decorate_place(self, flowers):
        print("Decorating the place with flowers.")

class Musician(WeddingPreparer):
    def prepare_wedding(self, wedding):
        self.prepare_performance(wedding.songs)

    def prepare_performance(self, songs):
        print("Preparing the musical performance.")

wedding = Wedding(100, ['roses'], ['classical music'])
preparers = [Chef(), Decorator(), Musician()]
wedding.prepare(preparers)

# Expected Output:
# Preparing food for the guests.
# Decorating the place with flowers.
# Preparing the musical performance.
```

1. **​Common Superclass**:​ All the preparer classes (`Chef`, `Decorator`, `Musician`) inherit from a common superclass, `WeddingPreparer`. This creates a formal, explicit relationship between them. They are all officially a "type of" `WeddingPreparer`.
2. **​Explicit Interface**:​ The `WeddingPreparer` class establishes a contract. By inheriting from it, the subclasses are expected to conform to its interface, which includes the `prepare_wedding` method.

* **Primary Method 2:  Duck Typing**: Often called **Structural Typing**. Python prioritizes an object's **behavior** (what it can do) over its **inheritance lineage** (what it is). If different objects implement methods with the same name, you can call those methods interchangeably.

> "If it walks like a duck and quacks like a duck, it's a duck."

```python
class Dog:
    def make_sound(self):
        print('Bark')

class Cat:
    def make_sound(self):
        print('Meow')

def animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sound(dog) # Output: Bark
animal_sound(cat) # Output: Meow
```

Here, `animal_sound` works with both `Dog` and `Cat` objects because they both have a `make_sound` method. This is polymorphism in action.

Duck typing occurs when unrelated types implement the same method names with compatible arguments and return values. Python focuses on whether an object has the required behavior rather than its specific class, enabling polymorphic use without a shared superclass. 

Here's Wedding again, except this time as duck typing. 

```python
class Wedding:
    
    def __init__(self, guests, flowers, songs):
        self.guests = guests
        self.flowers = flowers
        self.songs = songs

    def prepare(self, preparers):
        for preparer in preparers:
            # All it knows is that each preparer can `prepare_wedding`
            preparer.prepare_wedding(self)

class Chef:
    def prepare_wedding(self, wedding):
        self.prepare_food(wedding.guests)

    def prepare_food(self, guests):
        print("Preparing food...")

class Decorator:
    def prepare_wedding(self, wedding):
        self.decorate_place(wedding.flowers)

    def decorate_place(self, flowers):
        print("Decorating the place...")

class Musician:
    def prepare_wedding(self, wedding):
        self.prepare_performance(wedding.songs)

    def prepare_performance(self, songs):
        print("Preparing the performance...")

# Example usage:
wedding = Wedding(100, "dahlias", "Pachbel's Canon")
chef = Chef()
decorator = Decorator()
musician = Musician()

preparers = [chef, decorator, musician]
wedding.prepare(preparers)
```

The `Wedding.prepare` method is much simpler and more flexible. It just iterates and calls `prepare_wedding` on each object.

The `Chef`, `Decorator`, and `Musician` objects are all treated as "preparers" because they all "quack" the same way—they all have a `prepare_wedding` method. If you wanted to add a new `Photographer` class, you would just need to make sure it also has a `prepare_wedding` method. You wouldn't have to change the `Wedding` class at all! This is the power of duck typing.

We've now seen `Wedding` in two different guises: **Comparing the Two Approaches**

So, what's the difference?  ​

1. Relationship:    
    * ​Duck Typing:​ The `Chef`, `Decorator`, and `Musician` classes are ​unrelated​. They just happen to share a common behavior (the `prepare_wedding` method). The relationship is informal and based on capability.    

    * ​Inheritance:​ The `Chef`, `Decorator`, and `Musician` classes are ​formally related​. They all share an "is-a" relationship with `WeddingPreparer`. A `Chef` ​is a​ `WeddingPreparer`. This relationship is explicit in the code.

2.  ​Flexibility:    
    * Duck Typing:​ This approach is often considered more flexible and "Pythonic." Any object from any class can be used as a preparer, as long as it has a prepare_wedding method. You don't need to change its inheritance structure.   
     
    * ​Inheritance:​ This is more rigid. An object can only be treated as a `WeddingPreparer` if its class inherits from `WeddingPreparer`. However, this rigidity can also be a benefit, as it creates a clear contract and allows you to share common code in the superclass. Both approaches achieve polymorphism, but they do so in different ways.


| Feature | Inheritance | Duck Typing |
| :--- | :--- | :--- |
| **Relationship** | Formal **"Is-A"** | Informal **"Behaves-Like"** |
| **Enforcement** | Explicit (via shared superclass) | Implicit (via method names) |
| **Flexibility** | Rigid but creates a clear contract | Highly flexible and "Pythonic" |
| **Best For** | Hierarchical systems (e.g., Biology) | Plugin systems or varying data types |

Both approaches achieve polymorphism, but they do so in different ways.

* **Primary Method 3: Mix-ins (Component / "Can-Do" Relationship)** 

Mix-ins use **Multiple Inheritance** to inject a set of methods into classes that are otherwise unrelated. You use these to share a "Can-Do" capability (like `CanColor` or `CanJSONify`) across your codebase.

- **Interface Inheritance:** You aren't inheriting an object type; you are inheriting a focused, standard set of methods.
- **Rule:** Mix-ins should never be instantiated on their own; they only exist to add "flavor" to other classes.

Interface inheritance is the practice of using mix-ins to share specific behaviors across classes, especially when those classes do not share a hierarchical "is-a" relationship. Instead of inheriting an object type from a superclass, the class inherits an interface, which is a focused, standard set of methods. Using this approach allows you to reuse code in multiple unrelated classes as if the methods were copied and pasted directly into them.

```python
class ColorMixin:
    def set_color(self, color):
        self._color = color

class Car(ColorMixin):    
    def __init__(self, color):        
        self.set_color(color)

class House(ColorMixin):    
    def __init__(self, color):        
        self.set_color(color)

my_car = Car('red')
my_house = House('white')
things = [my_car, my_house]
for item in things:       
    item.set_color('blue') 
    
# Output:
# Color set to blue
# Color set to blue
```

* **Primary Method 4: Operator Overloading (Symbolic Polymorphism)** The ability of a single operator (like `+` or `*`) to have different meanings depending on the data types it is working with.

- **How it works:** Python uses "Magic Methods" (Dunder methods). By defining these in your class, you make your objects polymorphic with Python’s built-in operators.
- **Common Dunder Methods:** `__add__` (+), `__len__` (len()), `__str__` (print()).

```python
print(5 + 5)            # 10 (Addition)
print("High" + "Five")  # "HighFive" (Concatenation)
# The '+' operator is polymorphic!
```

##### Summary of Academic Terms for the Exam

| Type         | Relationship                | How it's enforced          | Best For...                                       |
|--------------|----------------------------|----------------------------|---------------------------------------------------|
| Inheritance  | "Is-A" (Formal)            | Shared Superclass          | Large systems with a clear hierarchy.             |
| Duck Typing  | "Behaves-Like" (Informal)  | Method Names               | Maximum flexibility and "Pythonic" code.          |
| Mix-ins      | "Can-Do" (Component)       | Multiple Inheritance       | Adding specific features to unrelated classes.     |
| Operator     | "Symbolic"                 | Magic Methods (`__add__`)  | Making custom objects work like built-in types.    |


*   **Method Overriding:** Replacing a parent's method with a child's version.
*   **Dynamic Dispatch:** Determining which method to call at runtime.
*   **Structural Typing:** Another name for Duck Typing (checking structure, not names).
*   **Type-Agnostic:** Code that functions regardless of the specific class of the objects it handles.
*   **Interface:** The set of public methods an object exposes to the world.

Page Reference: [Classes and Objects, Object Oriented Programming with Python](https://launchschool.com/books/oo_python/read/classes_objects)

[Back to the top](#top)

***

## Inheritance

**Inheritance** is a key principle of OOP that allows a class to acquire (or inherit) attributes from another class. This creates a formal **"is-a" relationship**.

*   **Superclass (Base Class):** The parent class that provides the common logic.
*   **Subclass (Derived Class):** The child class that inherits and extends that logic.

This creates a class **hierarchy**, which describes the relationships between classes. For example, a `Car` is a specific type of `Vehicle`. Therefore, it makes sense for a `Car` class to inherit from a `Vehicle` class, gaining its general vehicle-related behaviors. 

```python
class Vehicle:    
    def __init__(self, wheels):        
        self._wheels = wheels        
        print(f'I have {self._wheels} wheels.')    
    
    def drive(self):        
        print('I am driving.')

class Car(Vehicle):    
    def __init__(self):        
        print('Creating a car.')        
        super().__init__(4)

class Truck(Vehicle):    
    def __init__(self):        
        print('Creating a truck.')        
        super().__init__(18)

class Motorcycle(Vehicle):    
    def __init__(self):        
        print('Creating a motorcycle.')        
        super().__init__(2)    
    
    def drive(self):        
        super().drive()        
        print('No! I am riding!')

car = Car() 
#Output:
# Creating a car. 
# I have 4 wheels.

truck = Truck()
# Output: 
# Creating a truck.
# I have 18 wheels.

motorcycle = Motorcycle()
motorcycle.drive()

# Output:
# Creating a motorcycle.
# I have 2 wheels.
# I am driving. 
# No! I am riding!

```

### Benefits of Inheritance

*   **Code Reuse (DRY):** Extracts common behaviors into one superclass so you don't repeat yourself.
*   **Centralized Logic:** Update logic in one parent class, and it automatically updates for all children.
*   **Hierarchical Structure:** Models real-world relationships logically.
*   **Polymorphism:** Allows you to treat different subclasses (Car, Truck) as if they were the general superclass (Vehicle).

As the curriculum notes, when you use inheritance, you can "extract common behaviors from classes that share that behavior, and move it to a superclass. This lets us keep logic in one place."


### Risks and Disadvantages of Inheritance

While powerful, inheritance also introduces some risks if not used carefully.

*   **Tight Coupling:** A change in the superclass can accidentally break subclasses (the "Fragile Base Class" problem).
*   **Rigid Hierarchy:** Real-world objects don't always fit into a perfect "is-a" tree.
*   **Complexity:** Deep hierarchies make it hard to trace where a method is actually defined.
*   **Liskov Substitution Principle (LSP):** An academic rule stating that a subclass should be able to replace its superclass without breaking the program. If a subclass changes a method's behavior too much, it violates this principle.

### Tools for Verifying Inheritance

Exams often test these two built-in functions:
1.  **`isinstance(obj, Class)`**: Returns `True` if the object is an instance of that class **or** any of its subclasses.
2.  **`issubclass(Child, Parent)`**: Returns `True` if the first class inherits from the second.

In summary, inheritance is a fundamental tool in OOP for creating logical hierarchies and reusing code. The key is to use it when there is a clear "is-a" relationship between your classes. For other situations where you just want to share a common behavior without implying a hierarchical relationship, other patterns like using mix-ins or composition might be more appropriate.


### Understanding `self` and `cls` with Inheritance


The behavior of `self` and `cls` remains consistent with inheritance, which is a powerful feature.

*   **`self`**: Always refers to the **actual instance** that called the method, even if the method is defined way up in the parent class.
*   **`cls`**: Always refers to the **actual class** that called the method. If `Child.who_are_we()` is called, `cls` is `Child`, even if the method was inherited from `Parent`.

Here's an example to illustrate:

```python
class Parent:
    def identify(self):
        # self refers to the instance that called this method
        print(f"Instance method called on: {self.__class__.__name__}")

    @classmethod
    def who_are_we(cls):
        # cls refers to the class that called this method
        print(f"Class method called on: {cls.__name__}")

class Child(Parent):
    pass

child_instance = Child()
child_instance.identify()   # Prints "Instance method called on: Child"

Child.who_are_we()          # Prints "Class method called on: Child"
```

### The `super()` Function


`super()` is a built-in function used to access methods from a parent class.

*   **Why use it?** It prevents hardcoding the parent's name and ensures that the parent’s state (its `__init__`) is properly set up before the child adds its own data.
*   **No `self`:** You do not pass `self` into `super()` methods (e.g., `super().__init__(arg)`); Python handles the binding automatically.

### Mix-ins (Interface Inheritance)


Mix-ins provide a **"has-a capability"** (e.g., `CanSwim`) rather than a formal "is-a" identity. 

```python
class Vehicle:
    def __init__(self, year):
        self.year = year

class Car(Vehicle):
    def __init__(self, year, make):
        # Call the __init__ method of the superclass (Vehicle)
        super().__init__(year)
        self.make = make

my_car = Car(2023, 'Toyota')
print(my_car.year)  # Initialized by Vehicle's __init__
print(my_car.make)  # Initialized by Car's __init__
```

**Mix-ins** are classes that provide specific behaviors to other classes but are not meant to be instantiated on their own. They are a way to "mix in" functionality. This is often described as **interface inheritance**, because the subclass is inheriting a set of methods (an interface), not a more general object type.

```python

# --- Mix-ins defining specific behaviors (interfaces) ---
class WalkableMixin:    
    def walk(self):        
        return f"{self.name} is walking."

class SwimmableMixin:    
    def swim(self):        
        return f"{self.name} is swimming."
        
# --- Base class ---
class Animal:    
    def __init__(self, name):        
        self.name = name

# --- Concrete classes using the Pythonic mix-in order ---
class Dog(WalkableMixin, SwimmableMixin, Animal):    
    def bark(self):        
        return "Woof!"

class Cat(WalkableMixin, Animal):    
    def meow(self):        
        return "Meow!" 

class Fish(SwimmableMixin, Animal):    
    pass
    
# --- Demonstration (output remains the same) ---

fido = Dog("Fido")
print(fido.walk())  # => Fido is walking. 
print(fido.swim())  # => Fido is swimming.

whiskers = Cat("Whiskers")
print(whiskers.walk()) # => Whiskers is walking.

nemo = Fish("Nemo")
print(nemo.swim())   # => Nemo is swimming.
```

#### Benefits and Risks

#### Benefits

1. **​Unrelated Behaviors**​: Walking and swimming are distinct abilities. A `Dog` has both, a `Cat` has one, and a `Fish` has the other. There's no clean "is-a" hierarchy that could provide these methods to the correct classes without also giving them to classes that shouldn't have them.

2. **​Code Reusability (DRY)**​: The logic for walk and swim is defined only once in their respective mix-ins. We don't have to copy and paste the same method into the `Dog`, `Cat`, or `Fish` classes.

3. **​Clear Intent** ​: When you look at the class definition class `Dog(Animal, WalkableMixin, SwimmableMixin)`:, it's immediately clear what a `Dog` is and what it can do. It's an `Animal` that "has the ability to" walk and swim.

4. **​Flexibility**​: If we wanted to create a `Duck` class later, we could easily give it both walking and swimming capabilities. We just pick and choose the behaviors we need. This pattern of using mix-ins to provide optional or shared capabilities is a cornerstone of flexible object-oriented design in Python.


#### Risks   

* **​Multiple Inheritance Complexity**​: Because mix-ins use multiple inheritance, they can introduce complexity. If multiple parent classes define methods with the same name, it can be hard to predict which one will be called without inspecting the MRO.

* **​Naming Collisions**​: If a class and its mix-in, or two different mix-ins, define attributes or methods with the same name, they can overwrite each other, leading to unexpected bugs.

#### What's the Most Pythonic Approach?

Using mix-ins for interface inheritance is a very Pythonic pattern. It aligns with the principle of ​**Composition Over Inheritance** (COI)​, which many developers prefer.

* Inheritance​ establishes an ​"is-a"​ relationship (e.g., a `Motorcycle` is a `Vehicle`).
* ​Composition and Mix-ins​ establish a ​"has-a"​ relationship (e.g., a `Car` ​has the ability​ to be colored).

#### Final Note: Mixins go on the left of the arguments

Placing the mix-in to the left of the main parent class is the most common and "Pythonic" way to do it.The reason for this convention comes down to Python's **​Method Resolution Order**​. When you call a method on an object, Python looks for that method in a specific sequence determined by the order of parent classes in your class definition. Placing mix-ins to the left of the superclass is the standard convention because it ensures their methods take precedence, which is almost always why you're using a mix-in in the first place.


### "Is-a" vs. "Has-a"



These terms describe the two primary relationships between objects in OOP and help you decide when to use inheritance versus other techniques.

- **"Is-a"**: This relationship implies inheritance. A `Car` **is a** `Vehicle`. This means `Car` should be a subclass of `Vehicle`. This relationship is rigid and defines the object's core identity.
- **"Has-a"**: This relationship implies composition or collaboration. An object "has" another object or capability.
    - A `Person` **has a** name (an instance variable).
    - A `Car` **has a** `ColorMixin` (it uses a mix-in for behavior).
    - A `Car` **has an** `Engine` (it is composed of an Engine object that it collaborates with).

Many developers prefer "has-a" relationships over "is-a" relationships, a principle known as **Composition Over Inheritance**. This approach is often more flexible and leads to more modular code.

### More on Composition

In OOP, ​composition​ is a design principle where a class uses one or more objects of other classes to provide some of its functionality. This is a powerful way to build complex objects by combining simpler ones. 

The key idea behind composition is the ​"has-a" relationship​. For example, you could say a `Car` object "has an" `Engine` object. The Car class doesn't inherit from the `Engine` class (a car is not an engine), but it contains an instance of `Engine` and delegates tasks to it, like starting the car.

This use of other objects is a form of ​collaboration​. The objects that a class interacts with to perform its responsibilities are often called collaborators.

This use of other objects is a form of ​collaboration​. The objects that a class interacts with to perform its responsibilities are often called collaborators. Here's a simple conceptual example:

```python
class Engine:    
    def start(self):        
        return "Engine started!"

class Car:    
    def __init__(self, engine):        # The Car object is "composed" of an Engine object.   
        self.engine = engine         
           
    def start_car(self):        
        # The Car class delegates the work to its collaborator object.        
        return self.engine.start()

v6 = Engine() 
my_car = Car(v6)
print(my_car.start_car())  # Outputs: Engine started!
```

#### What Makes a Strong Composition?

A strong composition is built on a clear and logical ​"has-a" relationship​. The primary characteristics are:

1. **​Clear Delegation**:​ The main (or "composing") class delegates specific responsibilities to the objects it contains. For example, a `Car` class doesn't manage the details of combustion; it tells its Engine object to `start()`, and the `Engine` handles the rest.

2. **Collaboration**:​ The objects work together to achieve a goal. The curriculum notes that **"merely having an object inside your class isn't collaboration. At least one of the class's instance methods must use that object to aid the containing class's behavior."**

3. **Logical Containment**:​ The relationship makes sense in the real world or the problem domain. A `Person` "has a" `Name`, and a `Car` "has an" `Engine`. The composed object is an integral part of the container. In many strong composition scenarios, the contained object's lifecycle is tied to the container—when the `Car` is destroyed, its specific `Engine` instance is also destroyed.


#### Risks and Benefits 


#### Benefits

* **Flexibility**:​ This is the primary advantage. You can easily swap out components. For example, you could give your `Car` a `V8Engine `or an `ElectricMotor` object. As long as they both have a start method, the `Car` class doesn't need to change. This is much harder to do with inheritance.

* **​Single Responsibility**:​ Each class can focus on doing one thing well. The `Car` class worries about car-related things, while the `Engine` class worries about engine-related things. This makes your code easier to understand, test, and maintain.

* **​Lower Coupling**:​ Composition reduces dependencies between classes. Unlike inheritance, where a change in a superclass can break all its subclasses, changes to a composed object's internal implementation won't break the container class, as long as its public interface remains the same.

#### Risks (or Tradeoffs):

* **​Increased Indirection**:​ To understand how a `Car` starts, you have to look at the `Car` class and then navigate to the `Engine` class. This can sometimes make the code flow harder to trace compared to a single, larger class.

* **​More Boilerplate Code**:​ The container class often needs to write methods that simply call the corresponding method on the composed object. This is known as "forwarding" or "delegating," and it can sometimes feel like you're writing extra code just to pass a message along.


#### Some more Examples of Composition

#### Example 1: A `Person` and their `Job`

A `Person` object isn't a type of `Job`, but it certainly "has a" `Job`. This is a classic "has-a" relationship.

```python
class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

    def get_description(self):
        return f"work as a {self.title} for ${self.salary:,} per year."

class Person:
    def __init__(self, name, job_title, job_salary):
        self.name = name
        # The Person object is composed of a Job object
        self.job = Job(job_title, job_salary)

    def introduce(self):
        # The Person class delegates the job description to the Job object
        print(f"Hi, I'm {self.name}. I {self.job.get_description()}")

# Create an instance
engineer_job = Person("Maria", "Software Engineer", 120000)
engineer_job.introduce()
# Output: Hi, I'm Maria. I work as a Software Engineer for $120,000 per year.
```

##### Example 2: A Library and its Books

A `Library` is not a `Book`, but it "has" many `Book` objects. This shows composition with a collection of objects.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'

class Library:
    def __init__(self, name):
        self.name = name
        # The Library is composed of a list of Book objects
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"Books at {self.name}:")
        for book in self.books:
            # The Library interacts with its collaborator objects
            print(f"- {book}")

# Create instances
my_library = Library("City Center Library")
my_library.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
my_library.add_book(Book("1984", "George Orwell"))

my_library.list_books()
# Output:
# Books at City Center Library:
# - "The Hobbit" by J.R.R. Tolkien
# - "1984" by George Orwell
```

#### Isn't Composition more "Pythonic" than Inheritance?

While there's no official rule, the general consensus in the Python community—and modern object-oriented design— leans heavily in favor of composition. You could say that ​favoring composition is often more "Pythonic"​ because it aligns with core Python philosophies like simplicity and explicitness. 

Here's why:

1. **​Flexibility and Simplicity**​: Composition leads to more flexible and loosely-coupled designs. A class that is composed of other objects is less dependent on their internal implementation than a subclass is on its superclass. This makes your system easier to change and maintain, which aligns with the Zen of Python's "Simple is better than complex."

2. **​Avoiding Complex Hierarchies**​: Inheritance can lead to deep and complicated class hierarchies that are difficult to understand and reason about. Composition keeps relationships flatter and more explicit. You can see exactly what components an object has by looking at its` __init__` method.

3.  **​The "Composition Over Inheritance" Principle**​: As the curriculum mentions, this is a widely-accepted design principle. The reasoning is that "using mix-ins and composition in preference to inheritance is more flexible and safer." By following this principle, you often end up with code that is easier to test and reuse. 

However, this doesn't mean inheritance is "un-Pythonic" or should be avoided entirely. ​Inheritance is the right tool when you have a clear "is-a" relationship​. For example, a `GoldenRetriever` truly ​is a​ `Dog`. Using inheritance here is natural and correctly models the relationship. The problem arises when developers force an "is-a" relationship where it doesn't really fit, just to reuse some code.

In summary, the Pythonic approach is to choose the design that most clearly and simply models your problem. More often than not, that turns out to be composition.


### The Influence of Inheritance on Scope


Inheritance doesn't change Python's lexical scope rules (Local, Enclosing, Global, Built-in). Instead, it influences the **attribute lookup path** for an object. When you try to access a method or attribute on an object (e.g., `my_car.start_engine()`), Python doesn't just look in the `Car` class. If it can't find it there, it searches up the inheritance hierarchy (`Vehicle`, and eventually the base `object` class) until it finds the attribute or runs out of classes to search.

This lookup path is formally known as the **Method Resolution Order (MRO)**.

It's important to remember that instance variables belong to the object instance, not the class. While a subclass instance acquires the same instance variables defined in its superclass's `__init__`, they are not "looked up" via the MRO in the same way methods are.


### Method Resolution Order (MRO)


The **Method Resolution Order (MRO)** is the exact path Python follows to search for a method in a class hierarchy. Python has a well-defined algorithm for this to handle complex scenarios, including multiple inheritance and mix-ins. The algorithm is the **C3 Linearization Algorithm** and is used to create a linear order of classes that respects the inheritance hierarchy and ensures that subclasses are considered before their superclasses. This order is then used to determine which method to call when there are multiple possibilities due to inheritance.

You can see the MRO for any class by calling the `.mro()` method on the class itself.

Consider this complex hierarchy:

```python
class LandDwellingMixin: 
    pass
class LanguageMixin: 
    pass
class BipedalismMixin: 
    pass
class Creature: 
    pass
class Mammal(Creature): 
    pass
class Primate(LandDwellingMixin, Mammal): 
    pass
class Human(BipedalismMixin, LanguageMixin, Primate): 
    pass

# The .mro() method returns a list of classes in lookup order
print(Human.mro())
```

Output:
```
[
    <class '__main__.Human'>,
    <class '__main__.BipedalismMixin'>,
    <class '__main__.LanguageMixin'>,
    <class '__main__.Primate'>,
    <class '__main__.LandDwellingMixin'>,
    <class '__main__.Mammal'>,
    <class '__main__.Creature'>,
    <class 'object'>
]
```

When you call a method on a `Human` instance, Python will search for that method in this exact order, stopping as soon as it finds it. The search starts with the class itself (`Human`), moves through its mix-ins from left to right, and then proceeds to its superclass (`Primate`) and does the same for it, all the way up to the base `object` class.

The MRO helps to prevent the "Diamond Problem", a common issue in multiple inheritance, where a class inherits from two classes that both inherit from a common superclass. This creates a "diamond" shape in the inheritance hierarchy.

For example, consider the following classes:

```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass
```

In this example, class `D` inherits from both `B` and `C`, which both inherit from `A`. If you create an instance of `D` and call method, it’s unclear whether `B`’s or `C`’s method should be called. The C3 Linearization Algorithm helps resolve this ambiguity by determining a consistent order for method resolution.

**`D` would call `B` first**. In the above example, the MRO for class `D` would be `D`, `B`, `C`, `A`. So, when you call method on an instance of D, it would first look in B, then C, and finally A. The C3 Linearization Algorithm ensures that this order is consistent and respects the inheritance hierarchy.

#### `.mro` and `super()`

```python
class Machine:
    def identify(self):
        return "I am a Machine.\n"

class Appliance(Machine):
    def identify(self):
        message = super().identify()
        return f"{message} I am an Appliance.\n"

class Toaster(Machine):
    def identify(self):
        message = super().identify()
        return f"{message} I am a Toaster.\n"

class SmartToaster(Appliance, Toaster):
    pass

my_toaster = SmartToaster()
print(my_toaster.identify())
```

Step 1: What method gets called?

`my_toaster.identify()` is called. `SmartToaster` has no identify, so Python looks up the next class in the MRO `SmartToaster`’s bases are (`Appliance`, `Toaster`), so Python checks `Appliance` first.
So the method that runs is: Appliance.identify.

Step 2: What is the MRO?

Let’s compute it conceptually. For:

```python
class SmartToaster(Appliance, Toaster):
    pass
```

The MRO is: SmartToaster → Appliance → Toaster → Machine → object

Why does `Toaster` appear after `Appliance?` Because you listed (Appliance, Toaster) in that order, and Python merges the parent chains consistently (C3 linearization).

Step 3: What does `super()` mean here?

`super()` does not mean “call my parent class.” It means “call the next class in the MRO after the class I’m currently in. So inside `Appliance.identify`, `super().identify()` means:

“Find the next class after Appliance in SmartToaster’s MRO, and call its identify.”

The next class after `Appliance` is `Toaster`. So `super()` inside `Appliance.identify` calls: `Toaster.identify`

Step 4: What happens inside `Toaster.identify`?

Now we’re inside `Toaster.identify`. It also does: `message = super().identify()`. Again: `super()` means “next in the MRO after Toaster”. Next after `Toaster` is `Machine`.

So this calls: `Machine.identify` and `Machine.identify` returns: "I am a Machine.\n"

Step 5: Bubble back up (build the final string)

Now we go back to `Toaster.identify`:

```python
return f"{message} I am a Toaster.\n"
```

So `Toaster.identify` returns:

```python
"I am a Machine.\n I am a Toaster.\n"
```

Now we go back to `Appliance.identify`:

```python
return f"{message} I am an Appliance.\n"
```

Where message is what came back from `Toaster`, so `Appliance `returns:

`"I am a Machine.\n I am a Toaster.\n I am an Appliance.\n"`

So this prints:
```
I am a Machine. I am a Toaster. I am an Appliance.
```

**Why people get this wrong**

Most people assume:

* `Appliance` calls `Machine`
* `Toaster` calls `Machine`
* `SmartToaster` calls both somehow

But in multiple inheritance, `super()` is cooperative: it follows the MRO chain so each class gets a turn exactly once. 

> In multiple inheritance, super() calls the next method in the MRO, not “the parent.” Python resolves methods using a single, linear order (the MRO), and super() always moves forward along that line.

**Another way to say it**: “In multiple inheritance, super() follows the method resolution order, so each class’s method is called once in a consistent linear sequence.”

One more for the road:

```python
class A:
    def speak(self):
        return "A"

class B(A):
    def speak(self):
        return super().speak() + " B"

class C(A):
    def speak(self):
        return super().speak() + " C"

class D(B, C):
    pass

print(D().speak())
```

Execution flow:

1. `d.speak()` → looks in `D`, not found
2. Checks `B` → found! Calls `B.speak()`
3. `B.speak()` calls `super().speak()` → follows MRO to `C `(not `A`!)
4. `C.speak()` returns `super().speak()` + "C" → calls `A.speak()`
5. `A.speak()` returns "A"
6. Back to `C`: returns "A" + "C" = "AC"
7. Back to `B`: returns "AC" + "B" = "ACB"

[Back to the top](#top)

Further References:
[Christinelinster. (n.d.). ls-py120/practice_snippets at main · christinelinster/ls-py120. GitHub.](https://github.com/christinelinster/ls-py120/tree/main/practice_snippets)


***

## The `is` Operator and `id()` Function

Let's remember the most fundamental tenant of Python,

 **The "Three Pillars" of an Object**:

Every object in Python has three distinct properties:

1. **Identity**: Its address in memory (checked with `is` or `id()`).
2. **Type**: Its class (checked with `type()` or `isinstance()`).
3. **Value**: The data it contains (checked with `==`).

The built-in `id()` function and the `is` operator are closely related. They both deal with an object's **identity**.

- **`id()` function**: The `id()` function returns a unique integer for an object that is constant for its entire lifetime. In many Python implementations, this is the object's memory address. You can think of it as a unique "serial number" for that specific object in memory.

- **`is` operator**: The `is` operator compares the identity of two objects. It evaluates to `True` only if two variables point to the exact same object in memory. In other words, `a is b` is equivalent to `id(a) == id(b)`.

This is different from the `==` operator, which compares the **values** of two objects. You can have two different objects in memory that have the same value, so `==` would be `True` but `is` would be `False`.

Here's an example:

```python
class Person:
    pass

person1 = Person()
person2 = Person()
person3 = person2

# id() shows the unique identity of each object
print(hex(id(person1)))   # e.g., 0x104ccf9d0
print(hex(id(person2)))   # e.g., 0x104ccfa10
print(hex(id(person3)))   # e.g., 0x104ccfa10 (same as person2)

# `is` checks if the identities are the same
print(person1 is person2) # False - different objects
print(person2 is person3) # True - same object
```


## Magic Methods (Dunder Methods)


Magic methods, also known as "dunder" methods (for **double underscore**), are special methods that let you customize the behavior of your classes. They help make your classes more intuitive and integrate better with Python's built-in functions and operators.

Their names always start and end with double underscores (e.g., `__init__`, `__str__`). You typically don't call these methods directly. Instead, Python calls them for you when you use certain syntax, like operators (`+`, `==`) or built-in functions (`str()`, `repr()`).

### Custom Comparison Methods: `__eq__`, `__ne__`, `__lt__`, etc.

**The Story**

In the early days of object-oriented programming, you could create a Person class with a name and age, but Python didn't know how to compare people. `person1 == person2` would check if they're the same object in memory, not if they represent the same person. Want to sort a list of people by age? Impossible without writing custom sorting functions.

The pain: every built-in operator (`==`, `<`, `>`, etc.) worked great for numbers and strings, but your custom objects were second-class citizens. You couldn't use them naturally with `sorted()`, comparison operators, or any code that relied on ordering.

Python's solution: magic methods (also called "dunder methods" for double underscore). Define `__eq__` and Python calls it when someone writes `obj1 == obj2`. Define `__lt__` ("less than") and your objects work with `<`, `sorted()`, `min()`, `max()`, and more. Your custom classes become first-class citizens that work seamlessly with Python's built-in functions.

The pain this solves: inability to use custom objects with comparison operators, sorting functions, set membership, dictionary keys, and any algorithm that needs to compare objects.

**The Moral**
Magic methods let you define what operators mean for your objects—`__eq__` controls `==`, `__lt__` controls making custom classes work naturally with Python's built-in functions.

**Simple Example**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        """Called when using =="""
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other):
        """Called when using <"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

alice = Person("Alice", 30)
bob = Person("Bob", 25)
alice2 = Person("Alice", 30)

# __eq__ in action:
print(alice == alice2)  # True - same name and age
print(alice == bob)     # False - different

# __lt__ in action:
print(bob < alice)      # True - 25 < 30
print(alice < bob)      # False

# Works with built-in functions!
people = [alice, bob, Person("Charlie", 35), Person("Diana", 20)]
sorted_people = sorted(people)  # Uses __lt__ for sorting
print(sorted_people)  # [Diana(20), Bob(25), Alice(30), Charlie(35)]

youngest = min(people)  # Uses __lt__ to find minimum
print(youngest)  # Diana(20)

# Works with comparison chains:
diana = Person("Diana", 20)
print(diana < bob < alice)  # True - Diana(20) < Bob(25) < Alice(30)
```

These methods allow you to define how instances of your custom class behave with comparison operators. Specifically, the dunder comparison methods allow you to define how operators like `==`, `!=`, `<`, and `>` work with instances of your classes.

- `__eq__`: For equality (`==`)
- `__ne__`: For inequality (`!=`)
- `__lt__`: For less than (`<`)
- `__le__`: For less than or equal to (`<=`)
- `__gt__`: For greater than (`>`)
- `__ge__`: For greater than or equal to (`>=`)


The dunder comparison methods allow you to define how operators like `==`, `!=`, `<`, and `>` work with instances of your classes.


#### Equality Methods: `__eq__` and `__ne__`

By default, Python's `==` operator checks if two variables refer to the ​same object​ (identity), which is the same as using the `is` operator. This is often not what you want. You usually want to consider two objects equal if their ​state​ is the same.

You can define your own logic for equality by implementing the `__eq__` method. 

When Python encounters `a == b`, it effectively calls `a.__eq__(b)`. Here's an example. Without a custom `__eq__` method, two different `Cat` objects with the same name are not considered equal:

```python
class Cat:
    def __init__(self, name):
        self.name = name

fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')

print(fluffy == fluffy2)      # False, because they are different objects
```

Now, let's implement `__eq__` to define equality based on the cat's name:

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name == other.name

fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')

print(fluffy == fluffy2)      # True, because their names are the same
```

While defining `__eq__` often gives you a working `__ne__` for free, it's best practice to define `__ne__` yourself to handle all cases correctly, especially when dealing with different types.

Another example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        """
        This method is called when you use ==
        It must return True or False
        """
        if not isinstance(other, Person):
            return NotImplemented 
        return self.name == other.name and self.age == other.age #NOTICE YOU CAN OPERATOR CHAIN THEM

# Why is this important?
alice1 = Person("Alice", 30)
alice2 = Person("Alice", 30)
bob = Person("Bob", 25)

# Without __eq__, Python compares object identity (memory address)
# With __eq__, we define semantic equality

print(alice1 == alice2)  # True - same name and age
print(alice1 == bob)     # False - different person
print(alice1 is alice2)  # False - different objects in memory
```

#### Ordered Comparison Methods: `__lt__`, `__gt__`, etc.

If you try to compare custom objects using operators like < or > without defining the corresponding methods, Python will raise a `TypeError`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ted = Person('Ted', 33)
carol = Person('Carol', 49)

if ted < carol:
    print('Ted is younger than Carol') #TypeError: '<' not supported between instances of 'Person' and 'Person'
```

To fix this, you need to implement the ordered comparison methods. Let's add `__lt__ `(less than) and `__gt__` (greater than) to compare Person objects based on their age.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    def __gt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age > other.age

ted = Person('Ted', 33)
carol = Person('Carol', 49)

if ted < carol:
    print('Ted is younger than Carol')  # This now works and will print
```

**Handling Edge Case Example**

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        # 1. Compare with another Temperature object
        if isinstance(other, Temperature):
            return self.celsius == other.celsius
        
        # 2. Compare with a simple number (integer/float)
        if isinstance(other, (int, float)):
            return self.celsius == other
            
        return NotImplemented

t = Temperature(25)
print(t == 25)      # True (Handled by Case 2)
print(t == "cold")  # False (Returns NotImplemented, Python defaults to False)
```

#### A Note on `NotImplemented`

In the examples above, you can see `NotImplemented` returned. This is a special singleton value that you should return from a comparison method if it doesn't know how to handle the other object's type.

When a method returns `NotImplemented`, Python knows to try the "reflected" operation on the other object. For example, if `a < b` calls `a.__lt__(b)` and it returns `NotImplemented`, Python will then try `b.__gt__(a)`. If all attempts fail, a `TypeError` is raised. This makes your custom classes more robust and able to interact with other types gracefully.

Said alternatively, "When you return `NotImplemented`, you're telling Python: "I don't know how to compare myself with this other object. Try asking the other object to compare with me, or raise a `TypeError` if that doesn't work either."

```python
class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented  # This allows Python to try other.__eq__(self)
        return self.pages == other.pages

book = Book(100)
print(book == 100)  # False (Python tries 100.__eq__(book), which returns False)

# If we returned False instead of NotImplemented:
class BadBook:
    def __init__(self, pages):
        self.pages = pages
    
    def __eq__(self, other):
        if not isinstance(other, BadBook):
            return False  # Always False for non-Books
        return self.pages == other.pages

bad_book = BadBook(100)
print(bad_book == 100)  # False - this seems OK
print(100 == bad_book)  # False - but this prevents Python from handling it properly
```

#### All of them together

Here is the complete class definition followed by examples of each comparison method in use.

```python
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    # Equality: based on both title and rating
    def __eq__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.title == other.title and self.rating == other.rating #Notice the chaining! 

    # Inequality
    def __ne__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return not self.__eq__(other)

    # Less than: based on rating
    def __lt__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.rating < other.rating

    # Less than or equal to
    def __le__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.rating <= other.rating

    # Greater than
    def __gt__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.rating > other.rating

    # Greater than or equal to
    def __ge__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self.rating >= other.rating

# --- Create some instances to compare ---
movie_a = Movie("The Grand Budapest Hotel", 8.1)
movie_b = Movie("Isle of Dogs", 7.8)
movie_c = Movie("The Grand Budapest Hotel", 8.1)

# --- Example Usage ---

# 1. __eq__ (==)
# Compares movie_a and movie_c
print(f"movie_a == movie_c: {movie_a == movie_c}")  # True, title and rating match

# 2. __ne__ (!=)
# Compares movie_a and movie_b
print(f"movie_a != movie_b: {movie_a != movie_b}")  # True, they are different movies

# 3. __lt__ (<)
# Compares movie_b's rating to movie_a's rating
print(f"movie_b < movie_a: {movie_b < movie_a}")    # True, because 7.8 is less than 8.1

# 4. __le__ (<=)
# Compares movie_a's rating to movie_c's rating
print(f"movie_a <= movie_c: {movie_a <= movie_c}")  # True, because 8.1 is less than or equal to 8.1

# 5. __gt__ (>)
# Compares movie_a's rating to movie_b's rating
print(f"movie_a > movie_b: {movie_a > movie_b}")    # True, because 8.1 is greater than 7.8

# 6. __ge__ (>=)
# Compares movie_a's rating to movie_c's rating
print(f"movie_a >= movie_c: {movie_a >= movie_c}")  # True, because 8.1 is greater than or equal to 8.1
```

##### Breakdown of the Methods

1. `__eq__` and `__ne__` check for value equality. In this case, two `Movie` objects are only considered equal if both their title and rating are identical.   
2. The ordered comparison methods (`__lt__`, `__le__`, `__gt__`, `__ge__`) are all based on a single attribute: the rating. This allows you to sort a list of `Movie` objects or find the one with the highest rating. 
3. Notice that each method includes `if not isinstance(other, Movie): return NotImplemented`. This is a robust way to handle comparisons with objects of different types, as covered in the curriculum.


### Custom Arithmetic Methods: `__add__`, `__sub__`, `__mul__`, etc.

These methods let you define how arithmetic operators work with your objects. For example, you can define how to "add" two `Vector` objects together.

- `__add__`: Defines behavior for the `+` operator.
- `__iadd__`: Defines behavior for the augmented assignment `+=` operator.
- `__sub__`: Defines behavior for the `-` operator.
- `__isub__`: Defines behavior for the augmented assignment `-=` operator.
- `__mul__`: Defines behavior for the `*` operator.
- `__imul__`: Defines behavor for the augmented assignment `*=` operator.
- `__truediv__`: Defines behavior for the `/` operator.
- `__itruediv__`: Defines behavior for the augmented assignment `/=` operator.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Provides a developer-friendly string representation."""
        return f'Vector({repr(self.x)}, {repr(self.y)})'

    # --- Addition ---
    def __add__(self, other):
        """Defines the behavior for the `+` operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __iadd__(self, other):
        """Defines the behavior for the `+=` operator (in-place)."""
        if not isinstance(other, Vector):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self

    # --- Subtraction ---
    def __sub__(self, other):
        """Defines the behavior for the `-` operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __isub__(self, other):
        """Defines the behavior for the `-=` operator (in-place)."""
        if not isinstance(other, Vector):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y
        return self

    # --- Scalar Multiplication ---
    def __mul__(self, scalar):
        """Defines the behavior for the `*` operator with a number."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        new_x = self.x * scalar
        new_y = self.y * scalar
        return Vector(new_x, new_y)

    def __imul__(self, scalar):
        """Defines the behavior for the `*=` operator (in-place)."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        self.x *= scalar
        self.y *= scalar
        return self

    def __truediv__(self, scalar):
        """Defines the behavior for the `/` operator with a number."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        new_x = self.x / scalar
        new_y = self.y / scalar
        return Vector(new_x, new_y)

    def __itruediv__(self, scalar):
        """Defines the behavior for the `/=` operator (in-place)."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        self.x /= scalar
        self.y /= scalar
        return self

```

**How to Use It**
Here's how you can use instances of this Vector class with the operators we defined:

```python
# -- Setup --
v1 = Vector(10, 20)
v2 = Vector(3, 4)
print(f"Initial v1: {v1}")
print(f"Initial v2: {v2}\n")

# -- Addition (+) --
# Calls v1.__add__(v2) and returns a new Vector
sum_vector = v1 + v2
print(f"v1 + v2       = {sum_vector}")
print(f"v1 is unchanged: {v1}\n")

# -- Subtraction (-) --
# Calls v1.__sub__(v2) and returns a new Vector
diff_vector = v1 - v2
print(f"v1 - v2       = {diff_vector}")
print(f"v1 is unchanged: {v1}\n")

# -- Scalar Multiplication (*) --
# Calls v1.__mul__(5) and returns a new Vector
scaled_vector = v1 * 5
print(f"v1 * 5        = {scaled_vector}")
print(f"v1 is unchanged: {v1}\n")


# -- In-place Addition (+=) --
# Calls v1.__iadd__(v2) which modifies v1 and returns it
print(f"v1 before +=: {v1}")
v1 += v2
print(f"v1 after  +=: {v1}\n")

# -- In-place Multiplication (*=) --
# Calls v1.__imul__(2) which modifies v1 and returns it
print(f"v1 before *=: {v1}")
v1 *= 2
print(f"v1 after  *=: {v1}\n")

# --- Scalar Division (/) ---
# Calls v1.__truediv__(2) and returns a new Vector
quotient_vector = v1 / 2
print(f"v1 / 2        = {quotient_vector}")
print(f"v1 is unchanged: {v1}\n")

# --- In-place Scalar Division (/=) ---
# Calls v1.__itruediv__(2) and modifies v1 in-place
v1 /= 2
print(f"v1 /= 2       = {v1}")
print(f"v1 is modified:  {v1}")

```

##### Key Patterns to Notice

1.  **​Standard vs. In-Place Operators**​:

* The standard methods (`__add__`, `__sub__`, `__mul__`, `__truediv__`) do not change the original object (`self`). They perform the calculation and return a NEW OBJECT of the class with the result. This is "immutable-like" behavior.
* The in-place, or augmented assignment, methods (`__iadd__`, `__isub__`, `__imul__`) ​mutate the EXISTING object​ (`self`). The curriculum emphasizes that you must return `self` from these methods for them to work correctly. This is "mutable" behavior.

If you define `__add__` but forget to define `__iadd__`, Python will actually fall back to using `__add__` (thereby creating a new object) for the `+=` operation. However, defining `__iadd__` explicitly is better for performance because it avoids creating a new object.

2. **The "Reflected" Arithmetic (`__radd__`)**

The Scenario: What happens when your object is on the RIGHT side of the operator?

* `v1 + 5` calls `v1.__add__(5)`. This works!
* `5 + v1` calls `5.__add__(v1)`. Since the integer class doesn't know about your Vector, it returns `NotImplemented`.

The Solution: Python then looks for `v1.__radd__(5)`.

```python
    def __radd__(self, other):
        """Allows 5 + Vector(1, 2)"""
        return self.__add__(other)
```

3.  **​Type Checking and `NotImplemented`**​:

* It is a best practice to check if the other operand is of a compatible type. In our example, `__add__` expects another Vector, while `__mul__`  and `__truediv__` expects a number (int or float).
* If the operation is not supported with the given type, don't forget to return `NotImplemented`. This allows Python to try other ways to complete the operation (for instance, if the right-hand operand's class also defines the operation).

4.  **​Consistency**​:

* As the curriculum notes, you should normally define the in-place version (e.g., `__iadd__`) whenever you define the primary version (`__add__`). This provides a consistent and expected interface for users of your class.

**Summary of Arithmetic Dunder Groups**

| Operator | Binary Method   | In-Place Method  | Reflected Method |
|----------|----------------|------------------|------------------|
| +        | `__add__`      | `__iadd__`       | `__radd__`       |
| -        | `__sub__`      | `__isub__`       | `__rsub__`       |
| *        | `__mul__`      | `__imul__`       | `__rmul__`       |
| /        | `__truediv__`  | `__itruediv__`   | `__rtruediv__`   |


### Custom Formatting Methods: `__str__` and `__repr__`
 
These two methods control how your objects are converted to strings.

- `__str__`: Called by the `str()` built-in function and by operations like `print()`. It should return a user-friendly, readable string representation of the object.
- `__repr__`: Called by the `repr()` built-in function. It should return an unambiguous, developer-focused string representation. Ideally, this string could be used to recreate the object.

If a class has a `__repr__` but no `__str__`, Python will use `__repr__` as a fallback when `str()` is called.

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Cat({repr(self.name)})'

cat = Cat('Fuzzy')

print(str(cat))  # Fuzzy (calls __str__)
print(repr(cat)) # Cat('Fuzzy') (calls __repr__)

```
To format the `__repr__` method, you typically return a string that includes the class name and the values of the important attributes of the object. This helps to clearly identify the object and its state.

```python

# for numbers
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

```

In this example, the `__repr__` method returns a string that includes the class name (`Point`) and the values of the `x` and `y` attributes. This way, when you print a `Point` object or look at it in a debugger, you can easily see its state.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
```

In this example, the `name` attribute is a string, so it’s enclosed in quotes in the `__repr__` method. This helps to distinguish string values from other types of values, like numbers.

**What if there are more than two values??**

If your object has more than two attributes, you can include all of them in the `__repr__` string. Just separate them with commas, like in the examples we’ve seen. The goal is to provide a clear and complete representation of the object’s state.

```python

class Car:
    def __init__(self, make, model, year, features):
        self.make = make
        self.model = model
        self.year = year
        self.features = features

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, features={self.features})"

``` 

If your object has a mix of data types, you can format the `__repr__` method to include all of them, just like in the previous examples. You can include strings in quotes, numbers as they are, and other data types in a way that makes sense for that type.

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
```

In this example, name is a string, so it’s enclosed in quotes, while price and quantity are numbers, so they’re included as is.

**The "Why": Different Audiences, Different Goals**

`__str__` and `__repr__` were created to solve a fundamental problem: an object can have more than one useful string representation, depending on the audience.

The core reason for having two separate methods is to serve two distinct audiences:

1. `​__str__` is for the End-User:​ Its primary goal is ​readability​. It should produce a clean, user-friendly output. When you're writing a script and use `print()` to display information to someone running the program, `__str__` is what gets used. Think of it as the "informal" or "display" representation.

2.  `​__repr__` is for the Developer:​ Its primary goal is ​unambiguity and completeness​. It should provide an "official" or "developer-friendly" representation of the object. This is crucial for debugging, logging, and working in an interactive console. A good `__repr__` should, ideally, be valid Python code that could be used to recreate the object.

Let's look at the datetime example from the curriculum, which illustrates this perfectly:

```python
from datetime import datetime

dt = datetime.now()

# For the user: A clean, readable date and time.
print(str(dt))
# Output: 2023-10-27 10:30:54.123456

# For the developer: Unambiguous code to recreate the object.
print(repr(dt))
# Output: datetime.datetime(2023, 10, 27, 10, 30, 54, 123456)
```

You can see the difference in purpose immediately. The `str()` output is for display, while the `repr()` output is a precise, executable piece of code.

**What I Didn't Mention: Fallback Behavior and Implicit Usage**

Here are some crucial details that highlight the practical differences:

1. **The Fallback Mechanism is One-Way**

This is perhaps the most important rule to remember about their relationship:

* When you call `str(obj)`, Python first looks for a `__str__` method. If it doesn't find one, ​it falls back to using the `__repr__` method​. If neither is found, it uses the default `object.__str__.`

* When you call `repr(obj)`, Python only looks for a `__repr__` method. ​It will never fall back to `__str__`​. If it doesn't find one, it uses the default `object.__repr__`.

This behavior is why it's a common best practice to ​always implement `__repr__`​ for your custom classes. If you provide a good `__repr__`, you get a reasonable default behavior for `str()` for free. You can then add a` __str__` later if you need a more user-friendly version.

2. **Containers Use `__repr__` for their elements**

This is a subtle but powerful point. When you print a container object like a list or a dictionary, the container's own `__str__` method is called. However, to represent the ​items inside it​, it calls `__repr__` on each element. This is done to ensure the output is unambiguous. Consider a list of `Cat` objects:

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"A cat named {self.name}"

    def __repr__(self):
        return f"Cat('{self.name}')"

cat1 = Cat("Fuzzy")
cat2 = Cat("Whiskers")

cats = [cat1, cat2]

# print() on a single cat uses __str__
print(cat1)
# Output: A cat named Fuzzy

# But print() on the list of cats uses __repr__ for the items inside!
print(cats)
# Output: [Cat('Fuzzy'), Cat('Whiskers')]
```

If the list used `__str__` for its elements, the output would be `[A cat named Fuzzy, A cat named Whiskers]`, which is much less clear and not useful for debugging. The `__repr__ `output tells you exactly what objects are in the list.

3. **String Interpolation (f-strings) Uses `__str__`**

When you embed an object in an f-string, Python implicitly calls `str()` on it.
```python
cat1 = Cat("Fuzzy")
message = f"Here is my pet: {cat1}"
print(message) #Output: Here is my pet: A cat named Fuzzy
```

This makes f-strings excellent for producing user-facing output, as they naturally use the user-friendly representation of your objects.

Another complete example:

```python
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

# Demonstrating the difference
card = Card("Ace", "Spades")

print(str(card))   # "Ace of Spades" - readable for users
print(repr(card))  # "Card('Ace', 'Spades')" - clear for developers

# In the Python REPL:
# >>> card
# Card('Ace', 'Spades')  ← This uses __repr__

# When debugging a list:
cards = [Card("2", "Hearts"), Card("King", "Diamonds")]
print(cards)  # Uses __repr__ for each card
# [Card('2', 'Hearts'), Card('King', 'Diamonds')]
``` 

In summary,` __str__` and `__repr__` were created to provide context-appropriate string representations that serve the different needs of end-users and developers, making your custom objects behave like "good citizens" within the Python ecosystem.

| Feature       | `__str__`                       | `__repr__`                                   |
|---------------|---------------------------------|----------------------------------------------|
| Audience      | End-User (The Public)           | Developer (The Maintainer)                   |
| Goal          | Readability (Pretty)            | Unambiguity (Technical)                      |
| Mnemonic      | Statement (Display)             | Reproduce (Code)                             |
| Triggered by  | `print()`, `str()`, f-strings   | `repr()`, interactive console, items in list |
| Fallback      | Falls back to `__repr__`        | Never falls back                             |
| Ideal Output  | `"Fuzzy"`                       | `"Cat('Fuzzy')"`                             |


Page Reference: [Object Oriented Programming with Python, Magic Methods](https://launchschool.com/books/oo_python/read/magic_methods)


### Magic Methods + Collaboration 

These notes summarize **Python’s data model** (magic/dunder methods) with a focus on how
they relate to **object collaboration** and **container-like objects**.

Magic methods are protocol hooks Python calls when you use common syntax.

- `print(obj)` → calls `obj.__str__()`
- `obj += x` → calls `obj.__iadd__(x)` if defined
- `for x in obj` → calls `obj.__iter__()`

> **Rule of thumb:**  
> Magic methods let objects “participate” in built-in operations without special casing.


#### Collaboration Principle (applies everywhere)

> **Containers assemble; collaborators describe themselves.**

Meaning:
- A container object can *format the whole*
- Each element/collaborator should format *itself* (`__str__`, `__repr__`, etc.)

#### Illustrative Example: In-place “add” (`__iadd__`) for a Collection-like Object

- `__add__` ( `+` ) typically returns a **new** object
- `__iadd__` ( `+=` ) often **mutates in place** and returns `self`

```python
class Bucket:
    def __init__(self):
        self._items = []

    def add_many(self, items):
        # "real logic" goes here (explicit method)
        self._items.extend(items)

    def __iadd__(self, items):
        # operator sugar delegates to the real method
        self.add_many(items)
        return self
```

Key Info:

* Returning `self` is important for chaining and expected semantics.
* In-place mutation means aliases see changes (same object identity).

#### Illustrative Example: Container `__str__` Delegating to Elements

`join()` requires strings, so containers often convert elements via `str(element)`:

```python
class Container:
    def __init__(self, elements):
        self._elements = list(elements)

    def __str__(self):
        parts = [str(e) for e in self._elements]
        return "Items: " + ", ".join(parts)

```

**Why `str(e)` matters**

* `str(e)` calls `e.__str__()` if defined
* each element controls its own representation (encapsulation)
* container just assembles the overall string

### Magic Attributes: `__class__` and `__name__`


 `__class__` and `__name__` provide metadata about your code, which is particularly useful for introspection, debugging, and controlling how modules are executed.

#### The `__name__` Attribute

This attribute is used to get the name of a class as a string. It’s often used for debugging or logging purposes, to identify the class of an object. The `__name__` attribute has two common contexts: modules and classes.

1. **`__name__` in a Module**

In the context of a module (a .py file), `__name__` is a special variable that Python automatically sets. Its value depends on how the file is being used:

* If the file is being run directly by the Python interpreter, Python sets `__name__` to the string '`__main__`'.
* If the file is being imported into another module, Python sets `__name__` to the module's name (the filename without the .py extension).

This behavior is fundamental to a very common Python idiom: the `if __name__ == '__main__'`: block, known as **Module Entry Point Control**. This block of code will only execute when the file is run directly, not when it's imported. This allows you to create modules that are both reusable (importable) and runnable for testing or as a main program.

The `if __name__ == "__main__"`  allows a file to be used as both a reusable library (when imported) and an executable script (when run directly)."

**Scenario Question**: "What happens if you don't use this block?"
**Answer**: Any code in the module (like `print()` or function calls) will execute the moment the file is imported into another file, which is usually undesirable.

Anyway, that's not on the exam, you'll just see it a lot in the future. Here is the example from the curriculum:

```python
# file: mod1.py
print(f"In mod1.py, __name__ is: {__name__}") #In mod1.py, __name__ is: mod1
```

```python
# file: test.py
import mod1

print(f"In test.py, __name__ is: {__name__}") #In test.py, __name__ is: __main__
```

As you can see, when mod1 was imported, its `__name__` was '`mod1`'. But for the file we ran directly, `test.py`, its `__name__` was `'__main__'`.

2. **`__name__` on a Class**

When accessed on a class, `__name__` simply returns the name of the class as a string.

```python
class MyClass:
    pass

print(MyClass.__name__)  # Output: 'MyClass'
```

##### This is how they get ya: `__name__` in Inheritance

This is a high-level exam "Gotcha":

```python
class Parent:
    @classmethod
    def get_my_name(cls):
        return cls.__name__

class Child(Parent):
    pass

print(Child.get_my_name()) # Output: 'Child'
```

**The Lesson**: `__name__` always reflects the name of the specific class it is called on, even if the method was inherited from a parent.

#### The `__class__` Attribute

This attribute is used to get the class of an object. It returns the class object itself, not just the name. This means you can use it to create new instances of the class or access class variables. 

The `__class__` attribute is accessed on an ​​instance​​ of a class. It returns a reference to the class object that the instance was created from. This is incredibly useful for finding out what type of object you are working with at runtime.

```python
class Dog:
    def __init__(self, name):
        self.name = name

fido = Dog("Fido")

# __class__ returns the class object itself
print(fido.__class__)
# Output: <class '__main__.Dog'>

# You can use it to check the type
if fido.__class__ is Dog:
    print("Fido is an instance of the Dog class.")
# Output: Fido is an instance of the Dog class.
```

##### `__class__` vs. `type()`

**The Fact**: For almost every object, `obj.__class__` and `type(obj)` return the exact same class object.

**The Difference**: `__class__` is an attribute of the instance, while `type()` is a built-in function. In an exam, `type(obj)` is often considered the more standard way to retrieve the class, but `obj.__class__` is what’s happening "under the hood."


#### Tying Them Together

You can use both attributes together to get the string name of an object's class. This is a common pattern:

```python
class Cat:
    pass

whiskers = Cat()

# 1. Get the class object from the instance
the_class = whiskers.__class__  # <class '__main__.Cat'>

# 2. Get the string name from the class object
class_name = the_class.__name__ # 'Cat'

print(class_name) # Output: 'Cat'
```

You can also chain them directly:
```python
print(whiskers.__class__.__name__) # Output: 'Cat'
```

##### The String vs. Object Distinction

* `__name__` returns a string (e.g., "Cat").
* `__class__` returns the Class Object itself (e.g., `<class 'Cat'>`).

Why it matters: You can't call a method on a string, but you can use the class object to create new instances or access class variables. This is because the class object contains all the methods and variables defined in the class, while the name is just a string.


Summary of Differences:

```python
# The Metadata Chain:
# Instance -> Class -> Name String

fido = Dog("Fido")

print(fido.__class__ is Dog)        # True (The instance knows its class)
print(fido.__class__.__name__)      # "Dog" (The class knows its name)
```

| Attribute   | Accessed On       | What it Returns  | Example                                   |
| :---------- | :---------------- | :--------------- | :---------------------------------------- |
| __name__  | A module or class | A string         | MyClass.__name__ returns 'MyClass'    |
| __class__ | An instance       | The class object | my_instance.__class__ returns MyClass |

[Back to the top](#top)
*** 

## Exceptions

### What are Exceptions?
 
An exception is an object that represents an abnormal or exceptional condition that interrupts normal control flow. An exception is not just an error message. It is a control-flow mechanism.

#### Examples of common exceptions

* `ZeroDivisionError`: Division by zero
* `TypeError`: Wrong type for an operation 
* `ValueError`: Incorrect value
* `IndexError`: Index out of range
* `KeyError`: Dictionary key doesn't exist
* `FileNotFoundError`: File doesn't exist
* `AttributeError`: Attribute doesn't exist on an object

### Exceptions are objects, too

In Python, exceptions are objects that represent an error. Yes, _the error itself becomes an object_. 

Since the error is an object, that means it has (yet again, sorry you need to memorize this) a: 

1. Type (what kind of object it is)
2. Value (what data it holds)
3. Methods (things you can do with it)


```python
result = 10 / 0 # This line causes a ZeroDivisionError
```

Behind the scenes, Python does this with `result = 10 / 0`:

```python
# Python creates an exception object
exception_object = ZeroDivisionError("division by zero")

# Then it "raises" (throws) that object:
raise exception_object
```

You can see this in action:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(type(e))                   # <class 'ZeroDivisionError'>
    print(isinstance(e, Exception))  # True
    print(e)                         # division by zero
```

**_The variable `e` holds the actual exception object._**

#### What Does It Mean That Errors are Objects?

1. **Errors have properties (attributes)**

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # The exception object has properties:
    print(e.args)   # ('division by zero',)
    print(type(e))  # <class 'ZeroDivisionError'>

```

2. **Errors have methods**
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # You can call methods on the exception object:
    print(e.__str__())  # Get the string representation: division by zero
    print(e.__class__)  # Get the class: <class 'ZeroDivisionError'>
```

3. **Custom exceptions can have custom properties**

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance  # Attribute 1
        self.amount = amount    # Attribute 2
        super().__init__(f"Balance {balance} is less than {amount}")

try:
    raise InsufficientFundsError(100, 500)
except InsufficientFundsError as e:
    # e is an object!   It has attributes!
    print(e.balance)   # Access attribute:  100
    print(e. amount)   # Access attribute: 500
    print(e)           # "Balance 100 is less than 500"
```

#### Concrete Example: Seeing the Object

Let's watch the exception object directly:

```python
# Create an exception object WITHOUT raising it: 
error_obj = ValueError("This is invalid!")

# It's just an object sitting there:
print(error_obj)       #This is invalid! 
print(type(error_obj)) # <class 'ValueError'>
print(error_obj.args)  # ('This is invalid!',)

# You can pass it around like any object:
def log_error(error):
    print(f"Error type: {type(error)}") # Error type: <class 'ValueError'>
    print(f"Error message: {error}") # Error message: This is invalid!

log_error(error_obj)

# You can raise it later:
raise error_obj
```

#### The Object Lifecycle

Here's what happens step by step:

```python
# Step 1: An error occurs
result = 10 / 0

# Step 2: Python creates an exception object. This happens automatically, behind the scenes

# Step 3: Python "raises" (throws) that object. Program stops and the exception propagates up the call stack.

# Step 4: You catch the object
try:
    result = 10 / 0
except ZeroDivisionError as e:

# Step 5: Now you have the object in your hands! 
# e is the exception object
    print(e)
    print(type(e))
    print(e.args)
```

#### Why Does This Matter?

**Reason 1**: You can store and examine the error.

```Python
try:
    risky_function()
except Exception as e:
    # You have the error object! 
    error_type = type(e).__name__   # Get the error type
    error_message = str(e)          # Get the message
    
    # Log it, send it somewhere, etc.
    log_to_file(error_type, error_message)
```

**Reason 2**: You can extract custom data from it
```Python
try:
    account.withdraw(500)
except InsufficientFundsError as e:  # e is an object with custom properties! 
    print(f"You need ${e.shortfall} more")
```

**Reason 3**: You can create your own exception objects.

```python
# Create your own error object:
my_error = CustomError("Something went wrong", error_code=42)

# Store it:
errors = [my_error]

# Raise it later:
raise errors[0]
```

Think of it like this:

```python
# Regular objects:
person = {
    "name": "Alice",
    "age": 30
}

# Exception objects:
error = InsufficientFundsError(balance=100, amount=500)

# Both are objects with properties! 
print(person["name"])  # Alice
print(error.balance)   # 100
```

The exception is just a special kind of object designed to represent an error.

"**Exceptions are objects**" means:

✅ When an error occurs, Python creates an object to represent that error

✅ That object has properties (like balance, amount)

✅ That object has methods (like `__str__()`)

✅ You can catch that object with except and examine it

✅ You can store it in variables

✅ You can create custom exception objects with your own properties

The error doesn't just disappear—it becomes a concrete object that you can work with!

### Catching Exceptions with `try/except`

To manage potential errors gracefully without crashing your program, you can use a `try...except` block.

1. **​try block**​: You place the code that might cause an exception inside the `try` block.
2. **​except block**​: If an exception occurs in the `try` block, Python stops execution of that block and looks for a matching `except` block. If it finds one that handles the specific type of exception raised, the code inside that `except` block is executed. Here is an example that handles two different potential exceptions:

```python
try:
    num_str = input("Enter a number: ")
    num = int(num_str)
    result = 10 / num
except ValueError:
    print("Invalid input, you didn't enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Exception handling complete.")
```

In this code:

* If the user enters non-numeric text, a `ValueError` is raised by `int()`, and the first except block runs.   
* If the user enters `0`, a `ZeroDivisionError` is raised, and the second except block runs.
* The optional `else` block runs only if no exceptions occurred.
* The optional finally block runs every time, whether an exception happened or not.

#### What goes in a try/except block?

The essential and optional elements are:

* **`​try` Block** (Required)​:  This is the starting point. You place the code that you anticipate might raise an exception inside this block.

* **`​except` Block** (At least one except or finally is required)​: This block catches and handles exceptions.    
    * It must follow the `try` block.    
    * You can have multiple except blocks to handle different types of exceptions. Python will execute the ​first​ one that matches the type of exception raised.    
    * You can optionally capture the exception object using `as e` to get more details about the error.

*  **​else Block** (Optional)​: This block contains code that will run **_​only if no exceptions were raised​_** in the `try` block. It must be placed after all the `except` blocks. This is useful for separating the code that should run on success from the main logic being monitored for errors.

*  **​finally Block** (Optional)​: This block contains code that will ​always​ run, no matter what happens—whether an exception was raised, caught, or not. It is typically used for cleanup actions, like closing a file or releasing network resources. If included, it must be the very last block.


| Block     | When does it run?                | Common Purpose                                        |
|-----------|----------------------------------|-------------------------------------------------------|
| try       | Always                           | The "risky" code.                                     |
| except    | Only if an error occurred        | Error handling and recovery.                          |
| else      | Only if NO error occurred        | Actions that depend on success (e.g., commit to DB).  |
| finally   | Always (No matter what)          | Cleanup (closing files, network ports).               |


### Raising Exceptions

Besides catching exceptions that Python raises automatically, you can also trigger them yourself using the `raise` statement. This is useful when you detect a condition in your code that makes it impossible to proceed as intended. You can raise built-in exceptions or custom ones you've created.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age is set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print(e)  # Prints: Age cannot be negative.
```

**Raising with a Message**
```python 
 TypeError("Expected a string, got int instead")
```

**Re-raising an exception (catch, then re-raise)**:
```python
try:
    risky_operation()
except ValueError as e:
    print("Logging the error...")
    raise  # Re-raise the same exception
```

The `raise` statement is the core command for signaling that an error or an exceptional condition has occurred that prevents the program from continuing its normal flow. The most common and useful way to use it is by providing an instance of an exception class, usually with an informative message. Syntax:​ `raise ExceptionClassName("A descriptive error message")`

Here is a practical example:

```python
def process_payment(amount):
    if amount <= 0:
        # Create an instance of ValueError and raise it
        raise ValueError("Payment amount must be a positive number.")
    print(f"Processing payment of ${amount}...")

try:
    process_payment(-50)
except ValueError as e:
    print(f"Error: {e}")

# Output:
# Error: Payment amount must be a positive number.
```

In this code, the `raise` statement actively stops the function and creates a `ValueError` object. The `try...except` block then catches this object, and its message is printed. The `raise` statement works specifically with objects that are instances of a class that inherits from Python's built-in `Exception` class.

When you write `raise ValueError("...")`, you are doing two things at once:   
1. Creating a new object: `ValueError("...")` instantiates the `ValueError` class.    
2. "Throwing" that object up the call stack for an `except` block to catch.

All standard built-in exceptions like `ValueError`, `TypeError`, and `FileNotFoundError` are classes that inherit from the base `Exception` class. This shared ancestry is what makes the whole system work. An `except` block can catch a specific exception or any of its parent classes.

Custom Exceptions follow the same rule:​ When you create your own custom exception, you must make it a subclass of `Exception` (or one of its children).

#### What is the difference between 'raising' an exception and 'catching' an exception?

In Python, raising and catching exceptions are two sides of the same coin: one triggers an error state, and the other handles it.

1. Raising Exceptions

Raising is the act of manually triggering an exception. You do this when your code encounters a situation it cannot or should not handle internally, or when a specific condition (like invalid input) is met.

Keyword: `raise`

Purpose: To signal that something has gone wrong.

Direction: Sends the error up the call stack.

When to Use: When a function detects it cannot fulfill its task.


Example:
```python
def set_age(age):
    if age < 0:
        # We manually trigger an error because age cannot be negative
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

set_age(-5) # This will crash the program unless "caught"
```

2. Catching Exceptions

Catching is the act of intercepting an exception that has been raised (either by your code, a library, or Python itself) so that you can handle it gracefully instead of letting the program crash.

Keywords: `try`, `except`

Purpose: To recover from errors and keep the program running.

Direction: Stops the error from moving up the stack.

When to Use: When you want to provide a fallback or log an error without crashing.


Example:
```python
try:
    set_age(-5)
except ValueError as e:
    # We "catch" the error here
    print(f"Caught an error: {e}")
    # The program continues running from here
```

**The Flow**
1. A function raises an exception.
2. Python looks for a catch (`except` block) in the current function.
3. If not found, it moves up to the caller, then the caller's caller (the "call stack").
4. If it reaches the top level without being caught, the program terminates with a Traceback.

**Philosophies: "Fail Fast" vs. "Graceful Degradation"**

Raising is about "Failing Fast": It is often better to raise an error immediately when a problem is detected (e.g., a function receives a string instead of an integer) rather than allowing the program to continue with corrupted data.

Catching is about "Graceful Degradation": You catch exceptions at "boundaries" (like a UI or a web API endpoint) to show a user-friendly message or provide a default value instead of showing a raw code crash.

**Best Practice Tip: Be Specific**

When Raising: Raise the most specific exception possible (e.g., ValueError instead of just Exception).


#### What are the best practices for writing an exception block?

* ​Be Specific:​ Raise the most specific exception possible (e.g., `ValueError` instead of just `Exception`). Avoid catching a generic `Exception` or using a bare `except:` clause unless you have a very good reason (like logging all unexpected errors before terminating). A bare `except:` can hide bugs by catching things you didn't anticipate, like a `SystemExit` or `KeyboardInterrupt`.

Why not bare excepts?

**The Reason 1**: It catches `BaseException` subclasses like `KeyboardInterrupt` (Ctrl+C) and `SystemExit`.

**The Reason 2** It's considered a 'code smell'.

**The Result**: If you use a bare `except:`, the user might not be able to stop your program using the keyboard!

**The Rule**: Always catch Exception (which ignores those system-level signals) or a specific subclass.

* Keep `try` Blocks Minimal:​ Only wrap the single line or small section of code that you actually expect to fail. This makes it crystal clear where an error might originate and prevents you from accidentally catching an exception from an unrelated part of the code.

* ​Provide Meaningful Recovery or Feedback:​ Don't let an except block do nothing (e.g., `except ValueError: pass`).

This silently swallows errors and can lead to very confusing behavior. Instead, you should:    
1. Log the error for later debugging. 
2. Show a user-friendly message.    
3. Return a default value or `None`.    
4. Re-raise the exception if the current function can't handle it.
5. ​Use `finally` for Cleanup:​ If you have actions that ​must​ happen regardless of whether an exception occurred (like closing a file or releasing a resource), place them in a `finally` block.

#### `raise...from`

Sometimes you catch an exception and want to raise a different one, but you don't want to lose the original "cause."

**The Syntax**: raise `MyCustomError("Message") from e`

**Why it matters**: It keeps the "traceback" intact, showing both the original error and your new one.

#### How does this fit in with properties and setters?

Setters are the perfect place to raise exceptions to enforce data validation and business rules. A setter's job is to act as a gatekeeper for an attribute. It ensures that the attribute is never set to an invalid state. If the calling code tries to assign an invalid value, the setter should signal this error clearly, and raising an exception is the most Pythonic way to do it. Here is a practical example:

```python
class Product: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price # This calls the setter    
        
    @property 
    def price(self): 
        return self._price 
        
    @price.setter 
    def price(self, value): 
        if not isinstance(value, (int, float)): 
            # Rule 1: Price must be a number            
            raise TypeError("Price must be a number.") 
        if value < 0: 
            # Rule 2: Price cannot be negative            
            raise ValueError("Price cannot be negative.") 
        self._price = value
            
# --- Usage --- # This works fine
try: 
    product = Product("Laptop", 1200) 
    print(f"{product.name} costs ${product.price}") #THIS PRINTS
except (ValueError, TypeError) as e: 
    print(f"Error creating product: {e}") # This will be caught by the exception handler
        
try:
    p = Product("Laptop", -10)
except (TypeError, ValueError) as e:
    print(f"Validation failed: {e}")

```

In this example, the price setter validates the incoming value. If the value violates the rules, the setter raises an appropriate exception. The code that attempts to create the Product can then use a `try...except` block to gracefully handle the invalid data, preventing the program from crashing and allowing it to respond to the bad input.

#### Deep Dive: How the "Handshake" Works between the constructor and the setter

1. Instantiation: You call product = `Product("Laptop", 1200)`.
2. Constructor Execution: The `__init__` method starts.
3. The Trigger: Python reaches `self.price = price`.
4. The Interception: Python sees that price is a managed property. Instead of creating a simple variable, it "intercepts" the assignment and redirects it to the `@price.setter method`.
5. Validation: The setter runs. It checks if `1200` is a number and if it's positive.
6. Storage: Since `1200` is valid, the setter saves it into `self._color` (the internal, "hidden" variable).
7. Error Handling: If you had passed `-10`, the setter would have raised an exception, immediately stopping the `__init__` process and sending the error up to your `try/except block`.


### The Exception Hierarchy

Python's exceptions are organized into a class hierarchy. All exception classes inherit from the `BaseException` class. The most important subclass for day-to-day programming is `Exception`. Nearly all common, built-in exceptions inherit from `Exception`. This hierarchy is significant because you can catch exceptions using their specific type or any of their parent types. For example, since `ZeroDivisionError` is a subclass of `ArithmeticError`, an `except ArithmeticError:` block would catch a `ZeroDivisionError`. Understanding this hierarchy helps you write more flexible exception handlers, though you don't need to memorize the exact structure.

But because you are curious, here's the structure:

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── FileNotFoundError
    └── ... many others ...
```

### What's going on under the hood with the `Exception` class?

The `Exception` class is not just a marker; it's a fully functional Python class that provides the core behavior for all exceptions. Here’s what’s happening "under the hood":

1. ​**​Initialization​** (`__init__`): When you raise `ValueError("some message")`, you are creating an instance of the `ValueError` class. The string "some message" is passed to its `__init__` method. The base Exception class's `__init__` method takes all the arguments you provide and stores them in an attribute called `.args`. 

2. **​​String Representation** (`__str__`)​: When you `print(e)`, Python implicitly calls the `__str__` magic method on the exception object. The `Exception` class's `__str__` method is designed to format the contents of `.args` into a user-friendly string—which is the error message you see. You can see this in action by creating a custom exception and overriding these methods:

```python
class MyCustomError(Exception):
    """An example of what's going on inside an exception class."""
    def __init__(self, message, error_code):
        # Call the parent's __init__ to store the message
        super().__init__(message)
        # Add our own custom attributes
        self.error_code = error_code

    def __str__(self):
        # Override __str__ to create a custom, detailed error message
        # Get the original message from the parent class
        original_message = super().__str__()
        return f"[ERROR CODE: {self.error_code}] {original_message}"

# --- Usage ---
try:
    raise MyCustomError("Network connection failed", 503)
except MyCustomError as e:
    print(e)
    # Access the custom attribute we added
    print(f"The internal error code was: {e.error_code}")
    # You can also inspect the args from the base class
    print(f"The .args attribute is: {e.args}")

# Output:
# [ERROR CODE: 503] Network connection failed
# The internal error code was: 503
# The .args attribute is: ('Network connection failed',)
```

Under the hood an exception is just a regular Python object with a special purpose. The `raise` statement "throws" this object, and the except statement "catches" it, all using the standard OOP principles of instantiation, inheritance, and magic methods you've learned.

### Be more specific, what is `e`?

**`e`** doesn't stand for anything specific. It's just a variable name that programmers chose by convention. The primary reason for doing this is to get the descriptive error message associated with the exception. When you `print(e)` or use `e` in an f-string, you are seeing the human-readable message that the exception object carries.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)
```

The `as e` part means: "Capture the exception object and store it in an instance named e." When Python raises an exception,it's actually creating an instance of an exception class (like `ValueError`).  The `as e` part allows you to refer to this instance using the variable name `e`. So, `e` is a variable that holds the exception instance.

You could use any variable name you want:

```python
# Using 'e' (common convention):
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)

# Using 'error' (also clear):
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(error)

# Using 'exc' (abbreviation for exception):
try:
    result = 10 / 0
except ZeroDivisionError as exc:
    print(exc)

# Using 'my_exception' (very explicit):
try:
    result = 10 / 0
except ZeroDivisionError as my_exception:
    print(my_exception)

# Even 'x' or 'foo' would work (but it's confusing):
try:
    result = 10 / 0
except ZeroDivisionError as x:
    print(x)
```

All of these do the exact same thing. `e` is just tradition — most Python programmers use e because it's short and everyone understands it means "exception."

### Be more specific about `e.args`?

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than {amount}")

try:
    raise InsufficientFundsError(100, 500)
except InsufficientFundsError as e:
    print(f"e.args: {e.args}")
    print(f"e.balance: {e.balance}")
    print(f"e.amount: {e.amount}")

# Output:
# e.args: ('Balance 100 is less than 500',)
# e.balance: 100
# e.amount: 500
```

Notice that `.args` contains the message passed to `super().__init__()`, while `e.balance` and `e.amount` are the custom attributes we created.


### `as` vs. `from`

**`except ... as ...` (The "Capture")**

Here is the breakdown of the two different keywords and how they work together:

This is used only in the `except` block. Its purpose is to capture the exception object and give it a variable name (usually `e`) so you can look at its data.

Think of it as: "Catch the error and put it in a glove labeled `e`."

```python
try:
    1 / 0
except ZeroDivisionError as e:  # <--- This is the "Capture"
    print(e.args)               # Now we can use the variable 'e'
```

**`raise ... from ...` (The "Chain")**

This is used in the `raise` statement. Its purpose is to link a new error to an old error that you already captured.

Think of it as: "Throw a new error, but point back to the original error as the cause."

```python
try:
    1 / 0
except ZeroDivisionError as e:
    # We take the captured 'e' and link it to our new error
    raise ValueError("Calculation failed") from e  # <--- This is the "Chain"
```

| Syntax            | Where it lives   | What it does                                 | Exam Phrasing                    |
|-------------------|------------------|----------------------------------------------|----------------------------------|
| except ... as e   | except block     | Assigns a name to the caught exception object.| "Capturing the exception instance." |
| raise ... from e  | raise statement  | Links a new exception to the one stored in e. | "Explicit exception chaining."      |

Why you use them together: You usually need to use `as` before you can use `from`.

1. You use as `e` to get a handle on the error.
2. You then use from `e` to tell Python, "This new error I'm raising was caused by that `e` I just caught."


### Custom Exception Classes

You can define your own exception types by creating a new class that inherits from the built-in `Exception` class or one of its subclasses. This is very useful for creating more specific and descriptive errors related to your application's domain.

When creating custom exceptions, it's good practice to:

* End the class name with `Error`.
* Provide a clear, helpful default error message.

Most exceptions inherit from `Exception`. This means:

* `except Exception`: catches most runtime errors (but not `SystemExit` or `KeyboardInterrupt`)
* Specific exceptions are more precise: `except ValueError:`  is better than `except Exception:`

Here's an example:

```python
class ValidationError(Exception):    
    def __init__(self, message="Invalid data provided"):        
        super().__init__(message)
    
def validate_username(username):    
    if len(username) < 3:        
        raise ValidationError("Username must be at least 3 characters long.")
        try:    
            validate_username("Al")
        except ValidationError as e:    
            print(f"Validation failed: {e}")
```

```python
class InvalidAgeError(Exception):
    """Custom exception for age validation"""
    pass

def register_person(name, age):
    if age < 18:
        raise InvalidAgeError(f"{name} must be 18 or older to register")
    return f"{name} registered successfully"

try:
    register_person("Alice", 16)
except InvalidAgeError as e:
    print(f"Registration failed: {e}")
```

**Custom Exceptions with additional functionality**

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than {amount}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

try:
    account = BankAccount(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Cannot withdraw: {e}")
    print(f"Current balance: {e.balance}")
```

#### Breaking Down Custom Exception Classes

```python
# VERSION 1: Bare minimum
class SimpleError(Exception):
    pass

# VERSION 2: With custom message
class CustomMessageError(Exception):
    def __init__(self, message):
        super().__init__(message)

# VERSION 3: With custom data (like the BankAccount example)
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self. amount = amount
        super().__init__(f"Balance {balance} is less than {amount}")

# Using all three:
try:
    raise SimpleError()
except SimpleError as e:
    print(f"1. {e}")  # Output: (empty, no message)

try:
    raise CustomMessageError("Something went wrong!")
except CustomMessageError as e: 
    print(f"2. {e}")  # Output: Something went wrong!

try:
    raise InsufficientFundsError(100, 150)
except InsufficientFundsError as e:
    print(f"3. {e}")  # Output: Balance 100 is less than 150
    print(f"   Balance: {e.balance}, Needed: {e.amount}")
```

| Component                 | Required?         | Purpose                                      |
|---------------------------|-------------------|----------------------------------------------|
| Inherit from Exception    | ✅ Yes            | Makes it an exception class                  |
| `__init__` method         | ❌ No*            | Only if you need custom parameters           |
| `super().__init__(message)` | ✅ Yes (if using `__init__`) | Sets the error message         |
| Store custom attributes   | ❌ No*            | Only if you need to access data later        |

Creating custom exceptions like `ValidationError` makes your code more readable and allows you to handle your application's specific error conditions distinctly from Python's built-in errors.

#### Deep Dive: The `__init__` Method in Custom Exception Classes

For exceptions, the `__init__` works in much the same way in your routine classes.

```python
class MyError(Exception):
    def __init__(self, message):
        super().__init__(message)

# When you raise it:
raise MyError("Something went wrong")  # __init__ is called automatically
```

##### Why Do You Need `__init__` in Exception Classes?

**Reason 1**: To Accept Custom Parameters

Without `__init__`, you can only raise an exception with a default message:

```python
class SimpleError(Exception):
    pass

raise SimpleError()  # You can only do this
raise SimpleError("custom message")  # This works but gets messy
```

With `__init__`, you have control:

```python
class SimpleError(Exception):
    def __init__(self, message):
        super().__init__(message)

raise SimpleError("Now I control the message!")  # Clean and clear
```

**Reason 2**: To Store Data for Later Access

Without `__init__`, you can't easily store data to access in the except block:

```python
class BadError(Exception):
    pass

try:
    raise BadError("Amount was 500 but balance was 100")
except BadError as e:
    print(e)  # "Amount was 500 but balance was 100"
    # But you can't easily extract the numbers!
    # You'd have to parse the string
```

With `__init__`, you store the data directly:

```python
class GoodError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than {amount}")

try:
    raise GoodError(100, 500)
except GoodError as e:
    print(e)  # "Balance 100 is less than 500"
    print(e.balance)  # 100  (easy access!)
    print(e.amount)   # 500  (easy access!)
```

**What is `super().__init__()` doing?**

The Exception class (the parent) has its own `__init__` that expects a message:

```python
# This is roughly what Exception's __init__ looks like:
class Exception:
    def __init__(self, *args):
        self.args = args  # Store the message(s)
```

When you call `super().__init__("my message")`, you're telling the parent class to store that message.

**What happens if you DON'T call `super().__init__()`?**

```python
class BadError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        # OOPS!  Forgot to call super().__init__()

try:
    raise BadError(100, 500)
except BadError as e:
    print(e)  # Output: (empty!)  No message! 
    print(e.balance)  # Works:  100
```

The exception exists and you can access the data, but the error message is missing!

**Correct Way**

```python
class GoodError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than {amount}")

try:
    raise GoodError(100, 500)
except GoodError as e:
    print(e)  # Output: "Balance 100 is less than 500"  Perfect!
    print(e.balance)  # 100
```

##### The pattern you will always see

```python
class MyException(Exception):
    def __init__(self, param1, param2):
        # Store the data you'll need later
        self.param1 = param1
        self. param2 = param2
        
        # Call the parent's __init__ with a formatted message
        super().__init__(f"Error: {param1} and {param2}")
```

##### Complete Practical Example

```python
class InsufficientFundsError(Exception):
    def __init__(self, account_holder, balance, amount):
        self.account_holder = account_holder
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(
            f"{account_holder}:  Tried to withdraw ${amount} "
            f"but only have ${balance}.  Need ${self.shortfall} more."
        )

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self. balance:
            raise InsufficientFundsError(self. holder, self.balance, amount)
        self.balance -= amount
        return self.balance

# Using it:
try:
    account = BankAccount("Alice", 100)
    account.withdraw(150)
except InsufficientFundsError as e:
    # You can use the message: 
    print(f"Error: {e}")  # Error: Alice: Tried to withdraw $150 but only have $100. Need $50 more.
    # Or access the specific data:
    print(f"Account: {e.account_holder}") #Account: Alice
    print(f"Balance: ${e.balance}") #Balance: $100
    print(f"Attempted:  ${e.amount}") #Attempted: $150
    print(f"Shortfall:  ${e.shortfall}") #Shortfall:  $50
```

#### Wait, why do we want to store data in exception objects?

Without storing data, you're trapped with just the error message. With stored data, you can make intelligent decisions based on the actual values!

```python
class PaymentError(Exception):
    def __init__(self, transaction_id, amount, reason, retry_possible=False):
        self.transaction_id = transaction_id
        self. amount = amount
        self.reason = reason
        self.retry_possible = retry_possible
        super().__init__(
            f"Payment failed for transaction {transaction_id}: {reason}"
        )

def process_payment(card, amount):
    transaction_id = generate_id()
    
    try:
        charge_card(card, amount)
    except PaymentError as e: 
        # Use the stored data to handle the error intelligently:
        
        # 1. Decide whether to retry:
        if e.retry_possible:
            print(f"Retrying transaction {e.transaction_id}...")
            # retry_payment(e.transaction_id)
        else:
            print(f"Cannot retry.  Reason: {e.reason}")
        
        # 2. Refund if already charged:
        if charge_already_processed(e.transaction_id):
            issue_refund(e.transaction_id, e.amount)
            print(f"Refunded ${e.amount}")
        
        # 3. Notify the user with specific information:
        notify_user(
            f"Payment of ${e.amount} failed: {e.reason}.  "
            f"Reference: {e.transaction_id}"
        )
        
        # 4. Log for fraud detection:
        if "suspicious" in e.reason:
            flag_for_fraud_review(e.transaction_id, e.amount)

process_payment(my_card, 99.99)
```

### Exceptions in Practice

1. **Graceful File Handling**

A common task is reading from a file. But what if the file doesn't exist? Instead of crashing, your program can handle this situation gracefully using `a try...except` block. This approach follows the "Ask Forgiveness, Not Permission" (AFNP) philosophy, where you try an operation and handle the error if it fails.

```python
def read_user_settings(file_path="settings.txt"):
    """
    Tries to read user settings from a file.
    If the file doesn't exist, it returns default settings.
    """
    try:
        with open(file_path, 'r') as f:
            print("Settings file found. Loading user settings.")
            # In a real app, you would parse the file content here
            return f.read()
    except FileNotFoundError:
        print(f"Warning: '{file_path}' not found. Using default settings.")
        return {'theme': 'dark', 'notifications': 'enabled'} # Return a default value

# --- Usage ---
settings = read_user_settings()
print(f"Current settings: {settings}")

# If 'settings.txt' does not exist, the output will be:
# Warning: 'settings.txt' not found. Using default settings.
# Current settings: {'theme': 'dark', 'notifications': 'enabled'}
```

Here, the except `FileNotFoundError`: block prevents the program from terminating and provides a sensible fallback, making the application more robust.

2. **Enforcing Business Rules with Custom Exceptions**

Custom exceptions are perfect for signaling when a specific business rule or application constraint has been violated. They make your code's intent much clearer than using a generic exception like `ValueError`. 

Imagine a `BankAccount` class. You want to prevent a withdrawal that would overdraw the account.

```python
class InsufficientFundsError(Exception):
    """Custom exception raised for withdrawals exceeding the available balance."""
    def __init__(self, balance, amount_to_withdraw):
        message = (f"Attempted to withdraw ${amount_to_withdraw} "
                   f"but only ${balance} is available.")
        self.balance = balance
        self.amount_to_withdraw = amount_to_withdraw
        super().__init__(message)

class BankAccount:
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def withdraw(self, amount):
        if amount > self.balance:
            # Raise our custom exception to signal the specific error
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")

# --- Usage ---
account = BankAccount(100)
try:    
    account.withdraw(50)  # This will succeed    
    account.withdraw(75)  # This will fail and raise the exception 
except:
    InsufficientFundsError as e:    
        print(f"Transaction failed: {e}")

# Output:
# Successfully withdrew $50. New balance: $50
# Transaction failed: Attempted to withdraw $75 but only $50 is available.
```

Using `InsufficientFundsError` makes it obvious exactly what went wrong and allows the calling code to handle that specific scenario.

3. **Retrying Network Operations**

When interacting with external services over a network (like an API), connections can sometimes fail temporarily. Instead of giving up immediately, you can use exception handling to implement a retry mechanism.This example simulates fetching data from an API that might fail.

```python
import time
import random

def fetch_data_from_api():    
    
    """Simulates a network request that might fail."""    
    if random.random() < 0.7: # 70% chance of failure        
    raise ConnectionError("Failed to connect to the server")    
    return {"user_id": 123, "data": "API response"}

def get_data_with_retries(max_retries=3):    
    for attempt in range(max_retries):        
        try:            
            print(f"Attempt {attempt + 1}...")            r
            return fetch_data_from_api()        
        except ConnectionError as e:            
            print(f"Failed: {e}.")            
            if attempt < max_retries - 1:                
                print("Retrying in 1 second...")                
                time.sleep(1)            
            else:                
                print("All attempts failed.")                
                raise # Re-raise the final exception    

# --- Usage ---
try:    
    data = get_data_with_retries()   
     print(f"Success! Data received: {data}")
except ConnectionError:    
    print("Could not retrieve data from the API after multiple attempts.")
```

In this pattern, the `except` block does more than just log an error—it controls the program's flow to retry the failed operation. If all retries fail, it re-raises the exception with raise to let the caller know that the operation was ultimately unsuccessful.


### Exception Semantics in Python: A Practical Doctrine

An exception is an object that represents an abnormal or exceptional condition that interrupts normal control flow.

Mechanically:

* It is an instance of a subclass of BaseException.
* When raised, it aborts the current execution path.
* The interpreter unwinds the call stack until a matching handler is found.

An exception is not just an error message. It is a control-flow mechanism.

#### `raise`

`raise` signals that normal execution cannot continue in the current function.

When executed:
* The current frame stops immediately.
* An exception object is propagated upward.
* The interpreter searches for an except block.
* If none is found, the program terminates.

`raise` is vertical control transfer.

#### return

`retur`n completes a function normally and hands a value back to the immediate caller.

When executed:
* The current frame ends.
* A value is passed back.
* Control resumes at the call site.

`return` is horizontal control transfer.


#### The Three Error Paradigms

All error handling strategies answer one question: Is failure control flow, or is failure data?


1. Bubbling Up (Exception Propagation)

Shape:  Lower layers raise. Upper boundary layer handles.

Example layers: Persistence → Service → Controller. Only the controller catches.

Benefits:
* Minimal boilerplate.
* Centralized error policy.
* Clean domain code.
* Framework-friendly.

Risks
* Shadow control flow.
* Hard to see what can be raised.
* Layer boundaries may leak unexpected exceptions.

Discipline Rule

Catch exceptions only when you can:
1.	Add meaningful context (raise ... from e)
2.	Translate to a domain-level exception
3.	Recover (retry/fallback)
4.	Guarantee cleanup

Otherwise, let them bubble.


2. Water-Tight Handling (Catch & Re-Raise Everywhere)

Shape: Every layer catches and normalizes exceptions.

Benefits
* Local clarity.
* Explicit contract per layer.

Risks
* Boilerplate.
* Risk of swallowing stack traces.
* High maintenance cost.
* Type checkers don’t track exception contracts.

Proper Use: Translate exceptions at layer boundaries, not at every function.

Persistence errors → DomainError
DomainError → HTTP response

Do not catch for decoration alone.

3. Result Pattern (Never Raise, Always Return)

Shape:  Failure is returned as data.

`Result[Ok, Err]`

Benefits
* Explicit success/error paths.
* No shadow jumps.
* Predictable control flow.
* Strong mental clarity.

Risks
* Verbosity.
* Plumbing overhead.
* Interop friction with Python ecosystem.
* Union types can become noisy.

Use for expected, routine failures:
* Validation errors
* User input parsing
* Business rule rejections
* “Not found”

Not for invariant violations or system failures.



4. Returning Exceptions or `None`

A lightweight `Resul`t pattern.

Benefits
* Explicit
* Type checker friendly
* No stack unwinding surprises

Risks
* Easy to ignore
* Blurs semantics
* Inconsistent conventions

If you go this route, define a strict convention.

The Layering Rule (Clean Synthesis)

Use both exceptions and return values — but assign them territories.

Use `raise` for:
* Invariant violations
* Unexpected states
* Dependency failures
* Programmer errors

These represent broken assumptions.

Use `return` for:
* Expected alternative outcomes
* Validation failures
* Domain decisions

These represent legitimate states.


#### The Boundary Principle

Catch exceptions at:
* Request handlers
* CLI entry points
* Background job boundaries
* Layer translation points

Do not catch mid-layer unless you are:
* Adding information
* Recovering
* Translating semantics

#### Shadow Control Flow 

Exceptions create a second invisible execution path.

If overused without discipline:
* They resemble spaghetti control flow.
* Debugging becomes archaeology.

Deterioration Pattern to Watch

Systems decay when:
* Exceptions are caught “just in case.”
* Broad except Exception blocks hide origin.
* Logging replaces reasoning.
* Failure contracts are undocumented.

This is not inherent to exceptions. It is a governance failure.

Clean Doctrine Summary
1.	Exceptions are control-flow interruption.
2.	`raise` aborts upward.
3.	`return` completes normally.
4.	Use exceptions for unexpected failures.
5.	Use return values for expected alternatives.
6.	Catch at boundaries, not everywhere.
7.	Translate at layer seams.
8.	Never swallow without intent.


Exceptions are not “bad” and `Results` are not “better.” They solve different problems.

Exceptions express that “The world is not in a valid state.” While Return values express: “The world is valid, but this branch is different.”


[Back to the top](#top)

*** 

## What are Collaborator Objects?

In object-oriented programming, a **collaborator** is an object that another object holds a reference to and interacts with to carry out its responsibilities. This creates a "has-a" relationship, which is a key design principle known as **composition**.

Instead of a class trying to do everything itself, it can delegate specific tasks to other objects. These other objects are its collaborators.

For example, a `Person` object might **have a** `Pet` object. The `Pet` object is a collaborator of the `Person` object.

### The "Has-A" Relationship

As you've seen in the curriculum, we can describe relationships between classes in two main ways:

- **Is-A Relationship (Inheritance):** A `Bulldog` **is a** `Dog`. We use inheritance for this.
- **Has-A Relationship (Composition):** A `Person` **has a** `Pet`. We use collaborator objects for this.

Many developers prefer "has-a" relationships over "is-a" relationships, a principle called **Composition Over Inheritance**. This approach often leads to more flexible and maintainable code because it allows you to build complex objects by combining simpler, independent objects.

#### Code Example

The following is an example from the curriculum where a `Person` can have multiple pets. The `list` object that holds the pets, and the `Pet` objects themselves, are collaborators.

```python
class Pet:
    def jump(self):
        return 'Jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'
        
class Cat(Pet):
    def speak(self):
        return 'meow!'

class Person:
    def __init__(self, name):
        self.name = name
        self.pets = [] # This list is a collaborator

    def add_pet(self, pet):
        self.pets.append(pet)

# Instantiate objects
bob = Person('Bob')
buddy = Dog()
kitty = Cat()

# Bob's Person object uses its collaborator list to add pets
bob.add_pet(buddy)
bob.add_pet(kitty)

# The Person object can now delegate tasks to its collaborators
for pet in bob.pets:
    print(pet.speak())

# Expected Output:
# bark!
# meow!
```

In this example, the `Person` object doesn't need to know how to speak. Instead, it holds onto `Pet` objects and can ask them to perform actions. The list object stored in `self.pets` is also a collaborator because the `Person` class uses it (via `append`) to manage its collection of pets.

### An Important Distinction

It's important to remember that simply storing an object as an instance variable doesn't automatically make it a collaborator. For an object to be considered a collaborator, the containing class must actively use it in its methods to help fulfill its own functionality.

For instance, if `Person` just stored a list of pets but never used that list, the list wouldn't truly be collaborating.

In our example,`Person` uses the list's `append` method, making it a collaborator.

### When is `self.collaborator.method()` used...

An object uses a collaborator by holding a reference to it and calling its public methods.

One uses `self.collaborator.method()` when :
* the collaborator owns the data
* the collaborator owns the rule
* you just need the result

The object that owns the state should own the behavior that manipulates that state. If asked why you call a collaborator method, say:

> “This object doesn’t own that responsibility, so it delegates the behavior to its collaborator.”


### High-Level Reasoning: Why Use Collaborators?

Collaborator objects are central to object-oriented design because they allow you to model real-world relationships and build complex systems from smaller, more focused components.

1.  **Modeling the Problem Domain**: They represent the connections between different actors in your program. A car **has an** engine, a customer **has an** order, a person **has pets**. This makes your code more intuitive and easier to understand.
2.  **Delegating Responsibility:** Classes can delegate tasks to their collaborators. A `Car` object doesn't need to know the intricate details of combustion; it just tells its `Engine` collaborator to `start()`. This keeps each class focused on a single responsibility.
3.  **Flexibility and Maintainability:** Composition makes your code more flexible. You can easily swap out a collaborator for a different one without changing the containing class, as long as the new collaborator responds to the same methods. This makes your system easier to update and maintain over time.

In essence, collaborator objects allow you to build powerful and well-structured programs where objects work together, each handling its specific responsibilities.

#### The Law of Demeter (The "Principle of Least Knowledge")

While Collaborator Objects allow us to link classes together, we must be careful not to create a "chain of dependencies." The **Law of Demeter** is a design guideline that says: "An object should only talk to its immediate friends, not to strangers."

In OOP terms, a method should only call methods on:

* The object itself (`self`).
* Objects passed in as arguments.
* Objects held in its own instance variables (its direct collaborators).

Example: Avoiding the "Train Wreck"

If you see a line of code with multiple dots, it’s often a violation of this law (sometimes called a "Train Wreck").

```python
# ❌ VIOLATION: The Driver is talking to a "stranger" (the Engine).
# The Driver shouldn't need to know that Cars have Engines or how Engines ignite.
driver.car.engine.ignite()

# ✅ REFINED: The Driver talks only to their "friend" (the Car).
# The Car then delegates the task to its own friend (the Engine).
driver.start_car()
```

* **The Rule**: An object should only "talk" to its immediate friends (its direct collaborators). It should not "talk to strangers" (collaborators of its collaborators).
* **The Violation**: `driver.car.engine.start()`
* **Why?** The driver has to know about the car and the engine. If you change how engines work, you might break the driver.
* **The Solution (Delegation)**: `driver.car.start()` The driver tells the car to start. The car then tells the engine to start. The driver stays "ignorant" of the engine, which is good for Loose Coupling and enscapsulation.


## Collaborator Objects (A More Explicit Look)

As we discussed, a collaborator is an object that another object uses to perform its functions. The key word here is **​uses​**. It's not enough for an object to simply hold another object; it must interact with it by calling its methods or accessing its properties.

Consider this example from the curriculum:
```python
class Engine:
    def start(self):
        return "Engine started!"

class Car:
    def __init__(self, engine):
        self.engine = engine  # An engine object will be passed to Car

    def start(self):
        # Car delegates the action of starting to its collaborator
        return self.engine.start()

class Driver:
    def __init__(self, car):
        self.car = car # Driver now has a Car object

    def drive(self):
        # Driver delegates the action of starting the car to its collaborator
        return self.car.start()

# Create the collaborators first
engine = Engine()
car = Car(engine) #Engine object passed to Car
driver = Driver(car)

print(driver.drive()) # Output: Engine started!
```

In this code:

* The `Engine` object is a collaborator of the `Car` object. The `Car` class doesn't start itself; it tells its engine collaborator to `start()`.
* The `Car` object is a collaborator of the driver object. The `Driver` doesn't know the details of starting a car; it tells its car collaborator to `start()`.

This chain of collaboration allows each class to have a single, focused responsibility. The Driver's job is to drive, the Car's job is to be a car, and the Engine's job is to be an engine.

### Tight Coupling vs. Loose Coupling

While the terms "tight coupling" and "loose coupling" are not explicitly defined in the PY120 curriculum, they are vital software design principles that you will encounter frequently as you progress. They describe the degree of dependence between different parts of a system.

* **​Tight Coupling​**: This is when two or more classes are highly dependent on each other. A class that is tightly coupled to another knows too much about the inner workings of that class. A change in one class will often force you to make changes in the other. This makes the code brittle and hard to maintain. 

​Example of Tight Coupling:

```python
class Car:
        def __init__(self):
            # The Car class directly creates a specific Engine.
            # It's now permanently tied to the V6Engine class.
            self.engine = V6Engine()

        def start(self):
            return self.engine.start()

    class V6Engine:
        def start(self):
            return "V6 engine started!"
```

The problem here is that the `Car` class is "hard-coded" to use a `V6Engine`.

What if you want to create a `Car` with an `ElectricEngine`? You would have to modify the `Car` class itself.

* **​Loose Coupling**​: This is the goal of good object-oriented design. Classes are independent and interact through well-defined public interfaces (i.e., methods) without needing to know about each other's internal implementation. A change in one class has little to no impact on the others. This makes the system modular, flexible, and easier to test and maintain.

### Dependency Injection

Dependency Injection is a specific design pattern used to achieve **​loose coupling**​. It's a more advanced topic, but the core idea is simple:

>Instead of an object creating its own dependencies (collaborators), the dependencies are provided, or "injected," from an outside source.

Let's refactor our tightly coupled `Car` example to use dependency injection.

Example of Loose Coupling via Dependency Injection:

```python
# --- Define different types of engines ---
class V6Engine:
    def start(self):
        return "V6 engine started!"
                                        # Notice that they both have start methods.
class ElectricEngine:
    def start(self):
        return "Electric motor started quietly!"

# --- The Car class receives its dependency ---
class Car:
    # The engine is "injected" via the constructor
    def __init__(self, engine_object):
        self.engine = engine_object

    def start(self):
        return self.engine.start()

# --- The outside code creates and injects the dependencies ---
v6 = V6Engine()
electric = ElectricEngine()

my_ford = Car(v6)         # Injecting a V6Engine
my_tesla = Car(electric)    # Injecting an ElectricEngine

print(my_ford.start())    # Output: V6 engine started!
print(my_tesla.start())   # Output: Electric motor started quietly!
```

Notice the difference? The `Car` class is no longer responsible for creating its engine. It simply accepts an `engine_object` that is expected to have a start method. We can now create `Car` instances with any kind of engine, as long as that engine object conforms to the expected interface (it has a start method).

The `Car` class is now loosely coupled from the specific engine classes. This makes our code far more flexible and reusable. Passing a dependency through the `__init__` method is one of the most common forms of dependency injection.

### What are the trade-offs between Tight Coupling and Loose Coupling?

The choice between tight and loose coupling is not about finding the one "right" way, but about understanding the advantages and disadvantages of each approach for a given situation. As the curriculum states, this is the "art" of programming. Here is a breakdown of the trade-offs:

#### Tightly Coupled Designs

In a tightly coupled design, classes are closely connected and have detailed knowledge of each other.

* **​Advantage**: Easier to Understand (at first)

When you look at a method in a tightly coupled system, the logic is usually all in one place. You don't have to jump between multiple files or classes to follow the flow of execution. For smaller, simpler programs, this can make the code seem more straightforward and easier to write initially.

* **​Disadvantage**: Less Flexible and Harder to Maintain

The main drawback is that the code becomes brittle. Since classes are so dependent on each other's implementation, a change in one class can create a ripple effect, forcing you to make changes in several other classes. This makes the system harder to modify, reuse, and test.

For example, if a `TTTGame` class directly managed every detail of a `Player`'s move, including the logic for getting input from a human, it would be tightly coupled. If you later wanted to add a `Computer` player, you would have to significantly change the `TTTGame` class.

#### Loosely Coupled Designs

In a loosely coupled design, classes are independent and interact through well-defined, stable interfaces (i.e., public methods). This is often achieved through techniques like dependency injection.

* ​**Advantage**: More Flexible and Maintainable

This is the primary benefit, and particularly lends itself to agile environments. You can change the internal workings of one class without affecting the classes that use it, as long as you don't change the public methods they rely on. You can easily swap out components for different ones (like replacing a `Human` player with a `Computer` player). This makes the code much easier to extend, test in isolation, and maintain over the long term.

* **​Disadvantage**: Harder to Understand (at first)

The flexibility of loose coupling comes at the cost of increased indirection. To understand what a piece of code does, you often have to trace the interactions across several different objects and files. The overall behavior of the system emerges from the collaboration of these objects, which can be more challenging to grasp than a single, monolithic piece of code.

#### The Core Trade-off

The Launch School curriculum summarizes this trade-off in the discussion about the Tic Tac Toe game: In OOP, there are poor designs, but there is rarely one ​right​ design.

It all comes down to tradeoffs between tightly coupled dependencies or loosely coupled dependencies. Tightly coupled dependencies are easier to understand but offer less flexibility. Loosely coupled dependencies are more challenging to understand but offer more long-term flexibility. Which path is right depends on your application.

A key piece of advice is to avoid over-complicating things, especially when you're starting out.

Most of the time, beginners tend to over-apply design patterns. Don't prematurely optimize or build for large-scale architecture when you don't need it.

The goal is to recognize when you are creating dependencies and to find a balance that makes sense for the problem you are solving right now, while keeping an eye on future flexibility. Mastering this balance is a skill that grows with experience.


| Method                | Description                                                  | Coupling Level                                               |
|-----------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Internal Creation     | `self.engine = Engine()` inside `__init__`.                  | Tight (The car is stuck with that specific Engine class).    |
| Constructor Injection | `def __init__(self, engine): self.engine = engine.`          | Loose (You can pass in any engine object).                   |
| Method Injection      | `def service(self, mechanic): mechanic.fix(self).`           | Loose (The mechanic is a collaborator only for that specific task). |

### Are there other techniques for loose coupling other than dependency injection?

Yes, absolutely. While dependency injection is one of the most common and powerful techniques for achieving loose coupling, it's really a specific implementation of a broader principle. Other techniques and patterns also help accomplish the same goal.

Here are a couple of key approaches:

1. **​Relying on Polymorphism (via Duck Typing in Python)**

This is the foundational concept that makes techniques like dependency injection so effective in Python. Loose coupling is achieved when a class interacts with its collaborators through a generic interface, rather than depending on a specific concrete class.

In Python, we don't have formal interfaces like in some other languages. Instead, we have "duck typing": if an object has the methods and properties we need, we can use it, regardless of its actual class.

* ​How it works:​ Your class doesn't care about ​what​ its collaborator is, only ​what it can do​.
* ​Example:​ Let's revisit the Car and Engine example.

```python
class Car:
            def __init__(self, engine_object):
                self.engine = engine_object

            def start(self):
                # This car doesn't know or care if the engine is gas or electric.
                # It only cares that it can call a `start()` method on it.
                return self.engine.start()

        class ElectricEngine:
            def start(self):
                return "Electric motor started quietly!"

        class LoudV8Engine:
            def start(self):
                return "V8 ROARS TO LIFE!"

        # We can use any object that has a `start` method.
        my_tesla = Car(ElectricEngine())
        my_hotrod = Car(LoudV8Engine())
```

The `Car` class is loosely coupled because it's not tied to `ElectricEngine` or `LoudV8Engine`. It is coupled only to the ​idea​ that it will be given a collaborator that knows how to start. This is the essence of **polymorphism**.

2. ​**Event-Driven Architecture (The Observer Pattern)**

This is a more advanced pattern, but the concept is very powerful for decoupling. Instead of objects calling methods on each other directly, they communicate through events.
* ​How it works:
    * One object (the "publisher" or "subject") fires an event when its state changes (e.g., "a new user has signed up").
    * Other objects (the "subscribers" or "observers") can listen for this event. When they "hear" it, they perform their own actions (e.g., send a welcome email, update a dashboard).
    * ​The Decoupling Benefit:​ The publisher has no idea who is listening. It just shouts out that something happened. You can add or remove any number of subscribers without ever having to change the publisher's code. They are completely decoupled.
    * ​A Simple Analogy:​ Think of a radio station.

It broadcasts a signal (the event). It doesn't know or care who is listening. Any number of people can tune their radios (the subscribers) to that station to receive the signal. New listeners can tune in and others can tune out at any time without the radio station knowing or changing.

While you've focused more on the first approach in PY120 (polymorphism and collaborators), understanding the concept of event-driven design is valuable as you move into more complex applications, such as web development or graphical user interfaces, where this pattern is very common.

[Back to the top](#top)

***

## Reading OO Code

Reading Object-Oriented code is a crucial skill that goes beyond just understanding syntax. It's about comprehending the design, structure, and interactions within a program. It's a different way of thinking compared to reading procedural code.

### High-Level Reasoning

At a high level, reading OO code is about understanding a system of interacting components rather than a top-down sequence of instructions. As the Launch School curriculum notes, "Object-Oriented Programming (OOP) represents a significant departure from procedural programming." Most large programs, libraries, and frameworks you'll encounter in your career are built using an OO style. Therefore, the ability to read, understand, and navigate these codebases is fundamental to being an effective software engineer.

Reading OO code well means you can:
- Quickly understand the purpose and capabilities of an existing system.
- Modify or extend the code with confidence, without introducing bugs.
- Learn design patterns and idioms from experienced developers.

### Key Aspects of Reading OO Code

When you're reading an OO program, you are essentially trying to build a mental model of how the different parts of the system work together. Here's what you should focus on:

#### 1. Identifying the Core Components (The "Nouns")

First, identify the primary classes in the program. Classes are the blueprints for objects. Ask yourself:
- What are the main entities or concepts in this program? (e.g., Player, Card, Deck, Game).
- What is the responsibility of each class? What part of the problem does it solve?
- What **state** (data) does each object of a class manage? (Look at the instance variables, often initialized in the `__init__` method).
- What **behaviors** (methods) does each class define? What can objects of this class **do**?

#### 2. Understanding the Relationships Between Objects

Objects rarely exist in isolation. The real complexity and power of OOP come from how objects interact. You need to understand these relationships:

- **Inheritance ("is-a")**: Look for class definitions that inherit from another class (e.g., `class Cat(Animal):`). This tells you that a Cat is a specialized type of Animal and acquires its behaviors and properties. Understanding inheritance is key to seeing how code is reused and extended.
- **Collaboration ("has-a")**: Look for objects that hold references to other objects. For example, a Game object might have an instance variable that holds a Deck object. This is called composition or aggregation, and it's a primary way objects collaborate to achieve a larger goal.
- **Polymorphism**: This is the ability for different types of objects to respond to the same method call.

As noted in the curriculum, polymorphism "is the ability for different data types to respond to the same interface." When you see a method call like `animal.move()`, you need to recognize that the actual behavior could be different depending on whether `animal` is a Fish object or a Bird object.

#### 3. Recognizing the Public Interface

Encapsulation is the bundling of data and the methods that operate on that data. A key part of reading OO code is distinguishing between a class's **public interface** and its **private implementation details**.

- The public interface consists of the methods you are meant to call from outside the class. This is how you interact with an object.
- Implementation details are the internal mechanics of how the class works. In Python, these are often marked by a leading underscore (e.g., `_some_internal_data`) as a convention to indicate they shouldn't be relied upon externally.

Understanding this boundary allows you to use a class effectively without needing to know every detail of how it works internally.

Putting all this together can be challenging, and as the curriculum says, "putting them together to construct an object-oriented (OO) program isn't easy." The same is true for reading one. It takes practice to develop the skill of seeing not just lines of code, but a network of collaborating objects.

### Cheat Sheet: To Do List

1. Name the responsibility.
2. Name the object that owns it.
3. Explain why another object should not own it.
4. Mention what would change if requirements changed


### Example OOP Code

Let's use an example that incorporates several concepts from the PY129 Study Guide, and then walk through how you would "read" and explain it during an assessment. Here is a small system that models pets and their owners.

```python
class Owner:
    def __init__(self, name):
        self.name = name

class Pet:
    _total_pets = 0  # Class variable with leading underscore

    def __init__(self, name, owner):
        self.name = name      # Instance variable for state
        self.owner = owner    # Collaborator object
        Pet._total_pets += 1

    def __str__(self):
        return f"A {type(self).__name__} named {self.name}, owned by {self.owner.name}"

    @classmethod
    def get_total_pets(cls):
        return f"Total number of pets is {cls._total_pets}"

class Dog(Pet):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner) # Call superclass constructor
        self.breed = breed            # Add specific state

    def speak(self):
        return "Woof!"

class Cat(Pet):
    def speak(self):
        return "Meow!"

# --- Script Execution ---

lucy = Owner("Lucy")
sparky = Dog("Sparky", lucy, "Golden Retriever")
whiskers = Cat("Whiskers", lucy)

print(sparky)
# Output: A Dog named Sparky, owned by Lucy

print(Pet.get_total_pets())
# Output: Total number of pets is 2

for pet in [sparky, whiskers]:
    print(f"{pet.name} says: {pet.speak()}")

# Output:
# Sparky says: Woof!
# Whiskers says: Meow!
```

#### How to Read This Code for PY129

Here is a systematic approach to analyzing this code, demonstrating the kind of thinking required for the assessment.

##### Step 1: Identify Classes and High-Level Relationships

First, identify the main components.

- "I see four classes here: `Owner`, `Pet`, `Dog`, and `Cat`."
- "There is an *inheritance* relationship, which is an **'is-a'** relationship. `Dog` is a `Pet`, and `Cat` is a `Pet`. `Pet` is the superclass, and `Dog` and `Cat` are subclasses."
- "There is also a *collaboration* relationship, which is a **'has-a'** relationship. The `Pet` class's `__init__` method takes an owner object as an argument. This means every `Pet` object **has an** `Owner` object as a collaborator."

##### Step 2: Analyze the `Pet` Superclass (The Base)

Next, break down the superclass to understand the shared state and behavior.

- "The `Pet` class has a *class variable*, `_total_pets`. The leading underscore signifies that this is intended for internal use, a convention for *access control* in Python."
- "It also has a *class method*, `get_total_pets`, decorated with `@classmethod`. It operates on the class itself (via the `cls` parameter), not an instance, to access the `_total_pets` class variable."
- "The `__init__` method sets up the *state* for each `Pet` instance by creating *instance variables* `self.name` and `self.owner`."
- "The class defines a *magic method*, `__str__`. This provides a user-friendly string representation for `Pet` objects, which is used when I call `print(sparky)`."

##### Step 3: Analyze the `Dog` and `Cat` Subclasses

Now, examine how the subclasses specialize the superclass.

- "The `Dog` and `Cat` classes inherit from `Pet`. In the `Dog` class's `__init__` method, it calls `super().__init__(name, owner)`. This is crucial because it ensures that the `Pet` class's initialization logic (like setting the name and owner and incrementing the pet counter) is executed for `Dog` objects."
- "The `Dog` class also *extends the state* of a `Pet` by adding its own instance variable, `self.breed`. This is a common pattern in inheritance where a subclass is a more specific version of its superclass."

##### Step 4: Identify Polymorphism in Action

Look for methods with the same name in different classes within the same hierarchy.

- "Both `Dog` and `Cat` have a `speak` method. This is an example of *polymorphism*. They share the same interface (`speak()`) but provide their own unique implementation."
- "The `for` loop at the end demonstrates this powerful concept. The code `pet.speak()` is called on each object in the list. Python determines at runtime which version of `speak` to execute based on whether `pet` is a `Dog` or a `Cat` object. This makes the code flexible and extensible; we could add a `Parrot` class with its own `speak` method without changing the loop."

#####    Summary for the Interviewer

To conclude your analysis, you would summarize the key OOP principles you've identified:

> "This code demonstrates several core OOP concepts. We have *inheritance* with `Pet` as a base class for `Dog` and `Cat`. We see *collaboration* where `Pet` objects contain a reference to an `Owner` object. The `speak` method is a clear example of *polymorphism*. Finally, principles of *encapsulation* are shown through the bundling of data (like `name`) and methods (`speak`) within each class, and the use of a conventional private class variable `_total_pets`."

This systematic process—identifying classes, relationships, state, behavior, and key principles like polymorphism—is exactly what the PY129 assessment is looking for. It shows you can move beyond just executing code in your head and can analyze its design and structure.

[Back to the top](#top)

***


## Create a Code Spike

A code spike is a small, experimental program written to explore a specific concept or behavior. The goal isn't to build a feature, but to gain understanding. You create a minimal amount of code to answer a question, observe the result, and then discard the code. The value is in the learning process, not the artifact.

For the PY129 assessment, code spikes are crucial for moving from theoretical knowledge to a practical, demonstrable understanding of OOP concepts. The assessment requires you to explain topics with precision and clarity, often using code you write live. Spikes are the perfect way to practice this.

### How to Create a Code Spike for PY129

Here is a high-level process using an example from the PY129 Study Guide, such as understanding how `super()` works with multiple inheritance.

#### 1. Isolate a Single Concept

Choose one topic to explore. For example: **"How does super() determine which method to call in a multiple inheritance hierarchy?"**

#### 2. Formulate a Hypothesis

State what you expect to happen.
- *"I believe super() will follow the Method Resolution Order (MRO) to call the next method in the chain. If a class D inherits from B and C, and I call super() in a method within D, it should call the method in B first."*

#### 3. Write Minimal Code to Test

Create the simplest possible class structure to test your hypothesis.

```python
# spike.py
class A:
    def greet(self):
        print("I'm in A!")

class B(A):
    def greet(self):
        print("I'm in B!")
        super().greet()

class C(A):
    def greet(self):
        print("I'm in C!")
        super().greet()

class D(B, C):
    def greet(self):
        print("I'm in D!")
        super().greet()

d = D()
d.greet()

# Optional: inspect the MRO directly
print(D.mro())
```

#### 4. Run and Observe the Outcome

Execute the file.

```
# Output
I'm in D!
I'm in B!
I'm in C!
I'm in A!
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

#### 5. Analyze and Synthesize

Compare the output to your hypothesis.

- The output confirms that `super()` follows the MRO. The call chain was D -> B -> C -> A. My hypothesis was correct.
- This spike demonstrates that `super()` doesn't necessarily call the parent class's method, but rather the **next** class's method in the MRO.

We can "prove" our hypothesis using Introspection. This is much more convincing than just printing values.

```python
# Add this to the end of your spike
print(f"Dracula's local data: {dracula.__dict__}")
print(f"Frankenstein's local data: {frankenstein.__dict__}")
```

**The Analysis**: "By looking at `__dict__`, we can see that dracula has 'population': 999 stored directly on the instance, while frankenstein does not have a population key at all. This proves that Frankenstein is still 'borrowing' the value from the Class namespace, while Dracula is using his own 'shadowed' version."

#### 6. Iterate or Discard

- Now you could ask a follow-up question: *"What happens if I change the inheritance order to class D(C, B)?"* Modify the code, predict the new outcome, and run it again to confirm.
- Once you are confident in your understanding, delete the `spike.py` file.

The knowledge is now in your head, which was the entire point.

### But why do this?

The most important, and subtle, thing to understand about code spikes is the ​mindset​ you adopt when creating one.
Here are a few crucial, subtle aspects:

1.  **​The Code is Disposable, The Knowledge is Not**

The explicit goal of a spike is to produce knowledge, not code. As the curriculum states, "the idea of a spike is to throw away the code." This is liberating. It gives you permission to write messy, simple, or "bad" code because its only purpose is to answer a question for you. This removes the pressure of building something robust and lets you focus entirely on the concept you're exploring.

2.  **​Spikes Inform Design, They Aren't The Design**

A common mistake is to turn a spike directly into a feature. A spike is a pre-design activity. As noted in the "Coding and Design Tips" lesson, a spike is like the "initial braindump of ideas" you might do before writing an essay. You use the insights gained from the spike to make better, more informed decisions when you begin to formally structure your classes and methods.

3. **​Spikes Are Especially Useful in OOP**

The curriculum points out that "spikes are more common in OO code than procedural code." The subtle reason for this is that Object-Oriented Programming is less about a linear, top-to-bottom flow and more about the interactions and relationships between objects. It can be hard to visualize how these objects will collaborate. A spike allows you to quickly model these interactions in a low-stakes environment before you commit to a class structure.

In essence, a spike is a tool for targeted learning and risk reduction. By embracing its temporary and exploratory nature, you can learn concepts more quickly and build better-designed programs later.

### Code Spike: Investigating Attribute Shadowing

1. **Isolate a Single Concept**

The question we want to answer is: "When I assign a value to an attribute on an instance (e.g., `self.my_var = value`), what happens if a class variable with the same name already exists? Does it modify the class variable, or does it create a new instance variable that 'shadows' the class variable?"

2. **Formulate a Hypothesis**

* ​Reading Hypothesis:​ When accessing `some_instance.my_var`, Python first looks for an instance variable named `my_var` on some_instance. If it doesn't find one, it then looks for a class variable `my_var` on the instance's class.
* ​Writing Hypothesis:​ When assigning `some_instance.my_var = value`, Python will ​always​ create or update the ​instance variable​ `my_var` on some_instance. It will not modify the class variable. This new instance variable will then "shadow" the class variable for that specific instance.

3. **Write Minimal Code to Test**

We'll create a Monster class with a class variable population. Each monster can also have a personal threat_level. We'll create a situation where we accidentally name an instance variable population to see what happens.

```python
# spike.py

class Monster:
    # Class variable: tracks total number of monsters
    population = 0

    def __init__(self, name):
        # Instance variable: unique to each monster
        self.name = name
        print(f"{self.name} has appeared! (Instance created)")

        # Let's see the value of 'population' from within the instance
        # before we increment the class variable
        print(f"  - Reading 'self.population' before increment: {self.population}")

        # Modify the class variable the correct way
        Monster.population += 1
        print(f"  - Total monster population is now: {Monster.population}")

    def set_personal_population(self, value):
        """A badly named method to test attribute assignment."""
        print(f"\n--- {self.name} is attempting to set self.population to {value} ---")
        self.population = value # This is the key line for our hypothesis
        print(f"  - Reading 'self.population' from instance: {self.population}")
        print(f"  - Reading 'Monster.population' from class: {Monster.population}")

# --- Spike Execution ---

print("--- Creating Monsters ---")
dracula = Monster("Dracula")
frankenstein = Monster("Frankenstein")

print(f"\n--- Checking Initial State ---")
# Test Reading Hypothesis: instances should see the class variable
print(f"Dracula's 'population' attribute: {dracula.population}")
print(f"Frankenstein's 'population' attribute: {frankenstein.population}")
print(f"The Monster class 'population' attribute: {Monster.population}")

# Test Writing Hypothesis: create a shadowing instance variable on Dracula
dracula.set_personal_population(999)

print("\n--- Checking State After Shadowing ---")
print(f"Dracula's 'population' attribute is now: {dracula.population}")
print(f"Frankenstein's 'population' attribute is still: {frankenstein.population}")
print(f"The Monster class 'population' attribute is still: {Monster.population}")
```

4. **Run and Observe the Outcome**

```
--- Creating Monsters ---
Dracula has appeared! (Instance created)
  - Reading 'self.population' before increment: 0
  - Total monster population is now: 1
Frankenstein has appeared! (Instance created)
  - Reading 'self.population' before increment: 1
  - Total monster population is now: 2

--- Checking Initial State ---
Dracula's 'population' attribute: 2
Frankenstein's 'population' attribute: 2
The Monster class 'population' attribute: 2

--- Dracula is attempting to set self.population to 999 ---
  - Reading 'self.population' from instance: 999
  - Reading 'Monster.population' from class: 2

--- Checking State After Shadowing ---
Dracula's 'population' attribute is now: 999
Frankenstein's 'population' attribute is still: 2
The Monster class 'population' attribute is still: 2
```

5. **Analyze and Synthesize**

The results perfectly confirm our hypotheses:

* ​Reading:​ Initially, when `dracula.population` was accessed, Python didn't find an instance variable named `population` on the `dracula` object, so it correctly retrieved the value from the `Monster.population` class variable (2).
* ​Writing:​ The line `self.population = value` inside the method created a ​new instance variable​ named population that is unique to the dracula object. It did ​not​ change the `Monster.population` class variable.
* ​Shadowing:​ After the assignment, whenever we access dracula.population, Python now finds the instance variable first and returns its value (`999`). This instance variable is "shadowing" the class variable. The frankenstein instance, which was not modified, continues to access the unchanged class variable.

6. **Iterate or Discard**

This spike has given us a deep, practical understanding of Python's attribute lookup path. We've proven that assignment via `self.x` or `instance.x` creates an instance variable, which is a critical piece of knowledge for designing robust classes.
Now that we have this knowledge, the code has served its purpose and we can discard the `spike.py` file.


### "The 3-Step Assessment Strategy"

A cheat sheet for when the interviewer says: "Can you show me how X works?"

#### When asked to spike a concept during the interview

Do the following:

1. **State the Goal**: "I'm going to create a minimal class structure to demonstrate how [Concept] works."
2. **Write the "Simple Case"**: Create the parent/child classes with just one or two methods. Keep it to nouns like Parent/Child or A/B/C so you don't get bogged down in real-world logic.
3. **Explain the "Why"**: As you run the code, point to the output and use the technical vocabulary 

[Back to the top](#top)