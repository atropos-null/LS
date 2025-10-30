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

#### States and Behaviors

**State** refers to the data associated with an individual class instance. **Behavior** is what class instance objects can do, i.e., what methods an object can call. Two instances from the same class will have the same behaviors, but the states within them may be different. **Instance variables** keep track of the state, while **instance methods** expose behavior for objects. 


#### Object Scope

**Object scope** refers to the methods and instance variables an object can access. This is akin to discussing global and local scope instead of identifier scope. 

Object scope has two main components:

1) The methods in the class. This includes any methods acquired by the class via inheritance or mix-ins. 
2) The instance variables associated with the object. This includes any instance variables acquired via inheritance.

Instance variables, however, belong to objects. The methods give values to the instance variables, but those values belong to the object. Any object can call any method the class provides; every method can access the object's instance variables. Thus, all instances of the same type can access the same methods. However, an object can only access its own state.

#### Object Instantiation 

```python
class GoodDog:

    def __init__(self):
        print('This object was initialized!')

sparky = GoodDog() # This object was initialized!
```

The `__init__ ` method gets called every time you create a new object. As you may recall, that's the final step when instantiating an object. The first step is to call the constructor, e.g., `GoodDog()`. The constructor first calls the static method `__new__`.  This method allocates memory for the object and returns an uninitialized object to the constructor. The constructor next initializes the object by calling `__init__`.  In our GoodDog example, we call `GoodDog()`, which, in turn, calls `GoodDog.__new__.` The `__new__` method returns the new object, which the constructor subsequently uses to call `__init__`. `__init__` is frequently called the constructor. However, a better name may be the initializer or the instance constructor. 

Putting setup in` __init__ `ensures every instance is fully initialized at creation time—you can’t forget to run setup—so objects are always in a valid, uniform state. It also makes required data explicit via `__init__ `parameters and works cleanly with inheritance.

#### Instance Variables

```python

class GoodDog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

sparky = GoodDog('Sparky', 5)
```

Adding parameters to `__init__ `means you must provide arguments corresponding to those parameters when calling the constructor. `self.name` and `self.age` are instance variables. Every GoodDog object will have appropriate values for these variables. Instance variables keep track of information about the state of an object.

`__init__(self, name, age)` receives:

self → the newly created GoodDog instance (auto-supplied by Python)
name → 'Sparky' (supplied by you)
age → 5 (supplied by you)


#### Instance Methods

```python

class GoodDog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return 'Arf!'

sparky = GoodDog('Sparky', 5)
print(sparky.speak())
```

All instance methods must have a `self `parameter. Again, all instances of a class have the same behaviors, though they may contain different states.

**Question: Why can't we just write return f'{name} says arf!' inside the speak method? Why do we need to use self.name instead?**


Without `self`, Python looks for a variable named name in the current scope (locals, then globals). There isn’t one inside speak, so name would raise a `NameError`. Instance variables live on the object, not in the method’s local scope. So we must access them through the object reference (self).


#### Privacy

Warning: Instance variables can be reassigned, and if mutable, an instance variable can be mutated.

You can view or change any object's instance variables by just referencing the variable name. You can even delete or change methods. This can lead to all kinds of problems, such as:

* Unexpected instance variable values can lead to incorrect or unexpected behavior of the class instances.
* The class developer may change the implementation in the future, which may break your code.
* Incorrect or modified attributes can lead to unanticipated security problems.

The simplest approach  to discouraging users from using one's "private" attributes is to rely on the convention of marking instance variables and methods for internal use by naming them with a single leading underscore:

```python
class GoodDog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f'{self._name} says arf!'

    def _dog_years(self):
        return self._age * 7

    def show_age(self):
        print(f'My age in dog years is {self._dog_years()}')

# Omitted code
```

This doesn't prevent messing around with these internal use attributes, but it's a clear signal to the user that they're playing with fire. The single underscore convention tells the user they're messing with something they shouldn't. If they go ahead and do so anyway, it's at their own risk.


#### Getters and Setters

Since we can't prevent unrestricted access to instance variables, the next best approach is to provide getter and setter methods for the instance variables a user might want to access or modify. **Getters** and **setters** are common in OOP; they are methods that provide controlled access to an object's attributes. Getters retrieve attribute values, while setters assign attributes to new values.

```python
class GoodDog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f'{self._name} says arf!'

    def name(self):
        return self._name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        self._name = new_name

    def age(self):
        return self._age

    def set_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Age must be an integer')
        if new_age < 0:
            raise ValueError("Age can't be negative")
        self._age = new_age

sparky = GoodDog('Sparky', 5)
print(sparky.name())          # Sparky
print(sparky.age())           # 5
sparky.set_name('Fireplug')
print(sparky.name())          # Fireplug
sparky.set_age(6)
print(sparky.age())           # 6

sparky.set_name(42)
# TypeError: Name must be a string

sparky.set_age(-1)
# ValueError: Age can't be negative
```

In this code, we've used the underscore conventions to mark `self._name` and `self._age `for internal use. However, we've created getter methods name and age to retrieve the `self._name` and `self._age` values, respectively. We've also defined setter methods named `set_name` and `set_age` to change a GoodDog's name and age. To avoid unexpected values being submitted, we raise an exception if the name isn't a string or the age isn't a non-negative integer.

Users of your class can still choose to ignore the underscore convention. However, they no longer need it for any legitimate purpose. They can use the getters and setters. Getters conventionally have the same name as the associated instance variable without leading underscores. Setters conventionally prefix the same name with `set_`.

**Disregarding setters, if our name getter simply returns self._name, how is this approach any better than using a name variable directly?**

Even if the getter is just returning self._name today, it still buys you a few things:

Encapsulation and a stable interface: outside code uses name (getter) as the public way to read the value. You’re free to change how the value is stored (rename _name, compute it dynamically, fetch from elsewhere) without breaking callers.
Read-only access: by exposing only a getter (no setter), you communicate “this should not be reassigned,” while still allowing reads.

Room for future logic: you can easily add validation, transformation, caching, or logging later without changing callers.
Clear separation of public vs internal: _name is marked “internal use” by convention; name is part of the class’s public API.
If you later switch to properties (`@property`), callers can still write `obj.name`, but you retain all the above flexibility.

The following discussion around getters and setters revolves around this code, which is a `Person `class with two instance variables to hold a person's first and last names. 

```python
class Person:

    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f'{first_name} {last_name}'

    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic.')

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name
```
#### The Getter (@property)

The method decorated with @property is the getter.

**Purpose**: To control what happens when you read the attribute's value.
**When it's called**: It runs automatically anytime you access the attribute, like in print(sparky.name).
**What it does**: Its job is to retrieve the underlying data, possibly format it, or compute it on the fly before returning it.

```python
@property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f'{first_name} {last_name}'
```

**When the above code runs**: This code is executed when you read the attribute, like `print(bob.name)`.
**What it does**:
* It reads the raw, internal instance variables (`self._first_name`, `self._last_name`).
* It formats them by capitalizing them with `.title()`.
* It combines them into a single, polished string.

**Direction**: Data flows from inside the object to the outside.

#### The Setter (@name.setter)

The method decorated with @name.setter is the setter.

**Purpose**: To control what happens when you assign a new value to the attribute.
**When it's called**: It runs automatically anytime you use the assignment operator (=), like in `sparky.name = 'Fireplug'`.
**What it does**: Its job is to validate the incoming value and then update the internal state (the instance variable).

```python
@name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)
```

**When it runs**: This code is executed when you assign a new value to the attribute, like bob.name = ('Robert', 'Smith').
**What it does**:
* It receives the new value from the outside (e.g., the tuple ('Robert', 'Smith')).
* It unpacks the new value into first_name and last_name.
* It passes this data to the _set_name helper method, which acts as the chief validator before updating the internal state.

**Direction**: Data flows from outside the object to the inside.

#### Why They Look Similar

They look similar because they are two sides of the same coin—they both manage the same conceptual "name" attribute, which is composed of _first_name and _last_name. But their operations are fundamentally different:

Getter: Reads internal state -> Formats -> Returns a value.
Setter: Receives external value -> Validates -> Updates internal state.


#### Why They Aren't Redundant

They provide a single, intuitive interface (.name) while giving you separate control over the logic for reading (getting) and writing (setting) the value.

Consider this different example which makes the distinction clear:

```python
class GoodDog:
    def __init__(self, name, age):
        self.name = name  # Calls the setter
        self.age = age

    @property
    def name(self):
        print("--- Calling the GETTER to read the name ---")
        return self._name

    @name.setter
    def name(self, name):
        print("--- Calling the SETTER to validate and write the name ---")
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        self._name = name

sparky = GoodDog('Sparky', 5)
# Output: --- Calling the SETTER to validate and write the name ---

print(sparky.name)
# Output:
# --- Calling the GETTER to read the name ---
# Sparky

sparky.name = 'Fido'
# Output: --- Calling the SETTER to validate and write the name ---

```

As you can see, reading the name and assigning to it trigger completely different pieces of code.

Furthermore, you can have a getter without a setter to create a read-only attribute. This powerfully demonstrates they are separate functionalities. For example, if you remove the `@name.setter` method, you could still read `sparky.name`, but trying to assign `sparky.name = 'Fido`' would raise an `AttributeError`.

#### Properties

A more Pythonic way to create getters and setters is to use the `@property` decorator: Decorators are a fairly advanced concept in Python. They are, in fact, methods that modify other methods (the name and age methods seen above).

The `@property `decorator is used to create getter methods for an instance variable. When you apply `@property` to a method named foo, `@property` creates a secondary decorator named `@foo.setter`; this secondary decorator is used to create setter methods. (Thus, you can have a getter without a setter, but you can't have a setter without a getter.)

```python
class GoodDog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f'{self.name} says arf!'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')

        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')

        if age < 0:
            raise ValueError("Age can't be negative")

        self._age = age

sparky = GoodDog('Sparky', 5)
print(sparky.name)          # Sparky
print(sparky.age)           # 5
sparky.name = 'Fireplug'

print(sparky.name)          # Fireplug
sparky.age = 6

print(sparky.age)           # 6

sparky.name = 42  # TypeError: Name must be a string

sparky.age = -1   # ValueError: Age can't be negative
```

With this code, we seem to have two different methods called name and two more named age. The decorators, `@property`, `@name.setter`, and `@age.setter`, make them distinct. The `@property` prior to the first name method creates the @name.setter decorator, while the one prior to the first age method creates the `@age.setter` decorator.

Using these decorators means we no longer need `()` when accessing the getter and setter. We can also use standard assignment syntax to give an instance variable a new value.

Getters created with the `@property` decorator are known as properties. A setter is simply a property whose value can be reassigned.


#### When to Use Properties

Use properties when:

* you want to strongly discourage misuse of the instance variables.
* you want to validate data when your instance variables receive new values.
* you have dynamically computed attributes.
* you need to refactor your code in a manner incompatible with the existing interface.
* you want to improve your code readability, and properties can help.

If you don't need properties to satisfy a specific problem, you shouldn't use them.

When you use properties, use the single or double underscore convention for the associated instance variables.

Remember! There are no guardrails. Without properties (or your own getters/setters), Python doesn’t enforce types or values on instance variables at runtime.

#### Class Methods

Thus far, all the methods we've created are instance methods. They are methods that pertain to a class instance. There are also class-level methods called class methods.

Class methods provide general services for the class as a whole rather than the individual objects. We usually use the class to invoke the method. However, Python also lets you invoke class methods with instance objects. That's a little confusing, though, so you should use the class if possible.

```python

 class GoodCat():

    @classmethod
    def what_am_i(cls):
        print("I'm a GoodCat class!")

GoodCat.what_am_i()    # I'm a GoodCat class!

```

Class methods are where we usually put functionality that doesn't deal with class instances. Since our method has no reason to use the instance variables, we use a class method instead.

There are a variety of ways to call class methods:

* if you need to call a class method from within another class method of the same class, you can use the `cls` argument as the caller for the second method.

```python
class Foo:

    @classmethod
    def bar(cls):
        print('this is bar')

    @classmethod
    def qux(cls):
        print('this is qux')
        cls.bar()

Foo.qux()
# this is qux
# this is bar
```
* When you want to call a specific class method from outside the class that contains the class method, use the class's name to call it, as we did with Foo.qux() above. If you call a class method without using the explicit class name, Python will use the inferred class and the method resolution order (MRO) to determine which class method it should use. 

* If you have an instance object, obj, of a class that has a class method, you can invoke that method by using t`ype(obj), obj.__class__`, or even obj as the caller. You can also use self inside a method, as we show below:

```python
class Foo1:

    @classmethod
    def bar(cls):
        print('this is bar in Foo1')

    def qux(self):
        type(self).bar()
        self.__class__.bar()
        self.bar()
        Foo1.bar()

class Foo2(Foo1):

    @classmethod
    def bar(cls):
        print('this is bar in Foo2')

foo1 = Foo1()
foo1.qux()
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1

foo2 = Foo2()
foo2.qux()
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo1
```

We strongly discourage using the `obj.bar() `syntax for class methods. You lose any indication that you're calling a class method.

**When is a class variable initialized?**

At class definition time, in the class body (e.g., counter = 0 at the top of the class). It exists before any instances are created and is shared by the class and its instances. 

**How is it different from an instance variable?**

Class variables:
* Lives on the class, shared by all instances.
* Typically defined in the class body.
* Same storage for every instance unless shadowed.

Instance variable:
* Lives on each individual object, not shared.
* Usually created/initialized in init via s`elf.attr = value`.
* Each instance can have different values (object state).


#### Class Variables

Instance variables capture information related to specific class instances. Similarly, class variables capture information about the class. We initialize class variables in the main class body, usually at the top of the class. We can access and manipulate them with both instance and class methods.

```python

class GoodCat:

    counter = 0                  # class variable

    def __init__(self):
        GoodCat.counter += 1

    @classmethod
    def number_of_cats(cls):
        return GoodCat.counter

class ReallyGoodCat(GoodCat):
    pass

cat1 = GoodCat()
cat2 = GoodCat()
cat3 = ReallyGoodCat()

print(GoodCat.number_of_cats())        # 3
print(GoodCat.counter)                 # 3
print(ReallyGoodCat.number_of_cats())  # 3
print(ReallyGoodCat.counter)           # 3
```

In GoodCat, we have a class variable name, counter, which we initialize to 0. We want to use this variable to keep track of how many cats we have, so on line 6, we increment it by 1. Since Python calls `__init__ `every time we instantiate a new object, it's a great place to increment counter.

If we want to count all GoodCat objects, including any instances of `ReallyGoodCat` or other subclasses, we need to increment `GoodCat.counter` explicitly instead of `self.__class__.counter`. Otherwise, we'll end up incrementing a counter variable in the subclass. For the same reason, we also refer to `GoodCat.counter` in the number_of_cats method.

**Why is tracking how many instances have been created a good use case for a class variable?**

Because the count is a single piece of information about the class as a whole, not about any one object. A class variable lives on the class and is shared by all instances, so each time an object is created you can increment the same counter and get an aggregate total. 

#### Class Constants

Some classes have variables you never want to change once the class is defined. For this, you can use class constants. Class constants have the same naming conventions as ordinary constants. Like those constants, they are only constant by convention. Python doesn't enforce constancy.

As with class methods, you can use `cls.CONSTANT`, `type(obj).CONSTANT`, `obj.__class__.CONSTANT`, and `obj.CONSTANT` to access class constants. Once again, you should use the explicit class name syntax if you want to make sure you're accessing a class constant in a specific class.

#### More about `self`

`self` is that it always represents an object. What object, though? It's the calling object for a method. 

```python

class Pet:

    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        print(f'{self.name} says {sound}!')

class Cat(Pet):

    def speak(self):
        super().speak('meow')

cheddar = Cat('Cheddar')
cheddar.speak()
```

The actual calling object is a Cat object. It's that object that self refers to on line 7. It happens that a Cat object is also a Pet object, which explains our first sentence.

This also applies to line 4, though we never directly called the `__init__` method from the Cat class. However, Python uses a Cat object to call `__init__`.

By the way, that invocation of `super()` on line 12 returns an object that lets you call methods from the superclass of an object. Thus `super().speak('meow')` calls the speak method from the Pet class.

A reminder:  The first parameter defined for any instance method always represents the calling object, no matter what name you use.

**Can we also use self to call an instance method? Why or why not?**

es. Inside an instance method, self is the calling object, so you can invoke other instance methods on that same object with self.other_method(...).

Why it works:

* Methods belong to the class but are available to all instances. Accessing a method via an instance (like `self.speak`) creates a bound method that will automatically pass self as the first argument when called.
* Since self is “the current object,” `self.some_method()` is just like calling obj.some_method() from the outside, but on the current instance.

#### More About `cls`

The first parameter of a class method, conventionally named `cls`, always represents a class. Usually, that's the class used to invoke the method. For instance, if we call the `GoodCat.number_of_cats` method from earlier, we're using the GoodCat class to call the method. Thus, when we access `cls.counter` in the method, it refers to the number of GoodCat objects created.

`cls` is nearly identical to self in almost all respects. However, it conventionally references a class rather than an ordinary object. In Python, though, classes are instance objects, too! They are instantiated from the type class. Theoretically, there is no difference between `cls` and `self`. Nevertheless, use `cls` when defining a class method and self for instance methods.

```python
class Animal:

    @classmethod
    def make_sound(cls):
        print(f'{cls.__name__}: A generic sound')

class Dog(Animal):

    @classmethod
    def make_sound(cls):
        super().make_sound()
        print(f'{cls.__name__}: Bark')

Dog.make_sound()
# Dog: A generic sound
# Dog: Bark
```

Inside a class method, cls refers to the calling class, so you can access class variables with `cls.variable`. That’s conventional and works fine.

Be mindful of inheritance: cls will be the subclass when invoked via a subclass, so you’ll read/write that subclass’s variable (or create/shadow one). If you need to target a specific class’s variable, use the explicit class name.

#### Static Methods

You'll often encounter methods that belong to a class, but don't need access to any class or instance attributes. As a result, they don't make sense as either class or instance methods. Instead, they usually provide utility services to the instance or class methods, or to the users of the class. These methods are called **static methods**.

To define a static method, you use the @staticmethod decorator followed by a function definition that doesn't use a `self` or `cls` parameter.

Not all methods that can be made into static methods should be. For instance, a static method can't be easily converted to an instance method without requiring code changes elsewhere. If there's a reasonable chance that a static method may one day require access to instance or class state, then the method may not be suitable for use as a static method.

Static methods are often meant for internal use only, i.e., helper methods for your class's instance and class methods. They are also suitable for clarifying intent: use a static method when you want to be clear that the method doesn't use or modify the object or class state.


Page Reference: [Classes and Objects](https://launchschool.com/books/oo_python/read/classes_objects)

[Back to the top](#top)
***

### Magic Methods

When speaking, it's common to pronounce `__something__` as "dunder something". Thus, `__new__ `is "dunder new" and `__init__` is "dunder init".

`dunder methods` are designed to be called implicitly by Python in response to specific language constructs. This could be:

* Object creation (via `__new__` and `__init__`)
* Operators like `+`, `==`, `<` (via `__add__`, `__eq__`, `__lt__`, etc.)
* Built-in functions like `str()` and `repr()` (via `__str__ `and `__repr__`)
* String interpolation in f-strings (which implicitly calls `__str__`)

This suggests that dunder methods are Python's way of letting us customize how our objects behave in these common scenarios without having to call special methods ourselves. We just define the dunder method, and Python knows to call it at the right time. For instance, when we define `__init__`, we never write code like `my_object.__init__()`. Instead, Python automatically calls `__init__ `when we create an instance with Cat('Fuzzy'). That's what "Python knows to call it at the right time" means in practice. This "right time" pattern, where Python looks for and invokes these methods automatically, is what makes dunder methods so powerful. It lets us override Python's default behavior for things like object creation, string representation, comparisons, and operators, all without changing how other code interacts with our objects.

#### The `__str__` and `__repr__ `Methods

The return value of `str` is meant to be a human-readable representation of an object. In contrast, `repr` typically depicts how you would recreate an object.

In most cases, `str` and `repr` return the same value. However, this isn't universally true. One of the coolest aspects of str and repr is that they work with every object in Python, regardless of type. 

```python
class Cat:

    def __init__(self, name):
        self.name = name

cat = Cat('Fuzzy')
print(str(cat))  # <__main__.Cat object at 0x...>  #This output doesn't tell us that this particular cat's name is "Fuzzy."
print(repr(cat)) # <__main__.Cat object at 0x...>
```

What's happening here? When Python tries to call `str(cat)`, it looks for a `__str__` method in the Cat class. Likewise, when it tries to call `repr(cat)`, it looks for `Cat.__repr__`. Since neither method exists, Python looks elsewhere. But where?

Every object in Python ultimately inherits from the object class. In fact, this is the default superclass for a class that doesn't explicitly subclass another class. Thus, our Cat class inherits from object.

As it happens,` object.__str__` and `object.__repr__ `produce the above output.

Suppose you want to define class-specific `str` and `repr` methods for a class. All you have to do is add `__str__` and `__repr__` instance methods to the class:

```python
class Cat:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Cat({repr(self.name)})'

cat = Cat('Fuzzy')
print(str(cat))  # Fuzzy
print(repr(cat)) # Cat('Fuzzy')
print(f"The cat's name is {cat}.") # The cat's name is Fuzzy.
```

##### Why would we want to define class specific `str` and `repr`?

Defining class-specific `__str__` and `__repr__` methods allows us to control how our objects are represented as strings, which is crucial for readability and debugging. The default behavior isn't always helpful!

If you don't define these methods, printing an object gives you a default representation that isn't very informative. It shows the class name and the object's memory address, but nothing about its actual state. The `__str__` method is intended to provide a "human-readable" string representation of an object. This is what gets used when you call `print()` on an object or use it in an f-string. By defining it, you can provide a much cleaner and more useful output for the end-user of your class.

The `__repr__` method is meant to provide an unambiguous, official string representation of an object. The goal is that the string returned by `__repr__` should be valid Python code that can recreate the object. This is incredibly useful for debugging.

```python
# Continuing with the Cat class from above
cat = Cat('Fuzzy')
print(repr(cat)) # Cat('Fuzzy')
```

You could copy the output `Cat('Fuzzy')` and paste it into your code to create a new Cat object with the same state.

In summary, you'll want to define these methods to:

* Improve Readability: Make your objects display their state in a clear, meaningful way.
* Aid in Debugging: `__repr__` gives developers a quick way to see the exact state of an object.
* Integrate with Python: Allows your custom objects to work seamlessly with built-in functions like `print()` and string formatting.

When a program calls str on an object, Python first searches for a `__str__` method in the object. If it finds one, it invokes that method to determine the string representation. If it doesn't find a `__str__` method in the object, it then searches any classes it inherits from (we'll explore inheritance later). If it finds `__str__` in one of the inherited classes, it will use that method. If Python doesn't find a `__str__` method anywhere, it next looks for a `__repr__ `method using the same search mechanism used for the `__str__` method. If it can't find a `__repr__` method anywhere, it calls object.`__str__`, which returns a somewhat meaningless string that usually looks something like this: `<__main__.MyType object at 0x1052828a0>`. When a program calls `repr` on an object, Python takes a similar path to finding an appropriate `__repr__` method. Note that Python never searches for `__str__` when it is responding to a call to `repr`.

```python
# Class definition omitted

cat = Cat('Fuzzy')

# Cat has both __str__ and __repr__
print(str(cat))  # Fuzzy
print(repr(cat)) # Cat('Fuzzy')

# Cat has __str__ but not __repr__
print(str(cat))  # Fuzzy
print(repr(cat)) # <__main__.Cat object at 0x...>

# Cat has __repr__ but not __str__
print(str(cat))  # Cat('Fuzzy')
print(repr(cat)) # Cat('Fuzzy')

# Cat has neither __repr__ nor __str__
print(str(cat))  # <__main__.Cat object at 0x...>
print(repr(cat)) # <__main__.Cat object at 0x...>
```

Python implicitly calls `str` or `repr` in a variety of places:

* It implicitly calls `str` on each positional argument passed to the print function.
* It implicitly calls `str` when performing string interpolation, as in an f-string.
* It implicitly calls `repr` when printing the elements of a container object.

##### Why might implementing __str__ in your class be more useful than defining a custom method like display?

It highlights a core principle of object-oriented programming in Python: leveraging the language's built-in mechanisms makes your code more integrated and intuitive.

Implementing `__str__` is more useful than a custom method like display because `__str__` automatically integrates with Python's built-in functions and syntax. Python knows to call `__str__` in many common situations, whereas a custom method like display must always be called explicitly by you.

**Practical Situation: Displaying a List of Objects**

Imagine you have a Book class and a list of Book instances representing a library catalog.

Scenario 1: Using `__str__`

If your Book class implements `__str__`, displaying the catalog is natural and simple.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'

book1 = Book('The Hobbit', 'J.R.R. Tolkien')
book2 = Book('1984', 'George Orwell')

library = [book1, book2]

# Python automatically uses __str__ here
for book in library:
    print(book)

# Output:
# "The Hobbit" by J.R.R. Tolkien
# "1984" by George Orwell
```

Notice how `print(book)` just works. You don't need to know the specific method name for displaying a book; you just use the standard print function.

Scenario 2: Using a custom display method

If you used a custom display method instead, your code becomes less idiomatic.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f'"{self.title}" by {self.author}')

book1 = Book('The Hobbit', 'J.R.R. Tolkien')
book2 = Book('1984', 'George Orwell')

library = [book1, book2]

# You must remember and call the specific method
for book in library:
    book.display()

# This would not work as intended; it would print the default object representation
# for book in library:
#     print(book)
```

The difference becomes critical when your objects are used by code you didn't write—for example, a logging library or a debugging tool. These tools will automatically call `str()` on your objects to get a representation. They won't know to look for a custom display method.

By implementing `__str__`, you are making your class a good "citizen" of the Python ecosystem, allowing it to work seamlessly and predictably with the rest of the language.

#### The Comparison Methods

You may recall that you can compare most Python types for equality with the `==` or `!=` operators. You can also compare many types as ordered quantities with `<`, `<=`, `>`, and `>=`. Here are the magic methods that correspond to all these operators:

| Operator | Method   | Description                |
|----------|----------|----------------------------|
| ==       | __eq__   | Equal to                   |
| !=       | __ne__   | Not equal to               |
| <        | __lt__   | Less than                  |
| <=       | __le__   | Less than or equal to      |
| >        | __gt__   | Greater than               |
| >=       | __ge__   | Greater than or equal to   |


##### Customizing `== `and `!=`
Let's first see what happens with `==` and `!=` when `__eq__` and `__ne__` aren't defined for an object. We'll use the Cat class from above:

```python
# Class definition omitted

fuzzy = Cat('Fuzzy')
fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')

print(fuzzy == fluffy)        # False
print(fluffy == fluffy)       # True
print(fuzzy != fluffy)        # True
print(fuzzy != fuzzy)         # False

print(fluffy == fluffy2)      # False
print(fluffy != fluffy2)      # True
```

There shouldn't be any surprises here on lines 7-10. `fuzzy` is obviously not the same as `fluffy`, but `fluffy` is clearly `fluffy`. The inequalities also work as expected.

However, things get a little strange on lines 12 and 13. `fluffy` and `fluffy2` represent someone named Fluffy. However, the objects are not equal to each other. This worked when we previously compared the fluffy object with itself, but not now. The problem is that `fluffy` and `fluffy2` are distinct objects. By default, Python assumes that two custom objects are only equal when they are the same object.

If you need more control over equality, you need the `__eq__` and `__ne__` methods. **Without them, Python assumes that equal objects are the same object.** With these methods defined, however, Python uses them to check for equality.

```python
class Cat:

    def __init__(self, name):
        self.name = name

    # __str__ and __repr__ omitted

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

fuzzy = Cat('Fuzzy')
fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')

print(fuzzy == fluffy)        # False
print(fluffy == fluffy)       # True
print(fuzzy != fluffy)        # True
print(fuzzy != fuzzy)         # False

print(fluffy == fluffy2)      # True
print(fluffy != fluffy2)      # False
```
Note that lines 23 and 24 return values reflecting the equality of the fluffy and fluffy2 objects.

##### How could we call the `__eq__` method directly to compare two Cat instances?

While using the == operator is the standard and more readable way, you can absolutely call the __eq__ method directly just like any other instance method.

Here's how you would do it using the Cat class from the lesson:
```python
class Cat:
    def __init__(self, name):
        self.name = name

    # __str__ and __repr__ omitted

    def __eq__(self, other):
        return self.name == other.name

fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')

# Standard comparison using the operator
result1 = (fluffy == fluffy2)
print(f"Using '==': {result1}") # Using '==': True

# Calling the __eq__ method directly
result2 = fluffy.__eq__(fluffy2)
print(f"Using .__eq__(): {result2}") # Using .__eq__(): True
```

As you can see, `fluffy == fluffy2` is essentially syntactic sugar for `fluffy.__eq__(fluffy2)`. It's a fun way to see how Python's operators map directly to these dunder methods under the hood!

Inheritance plays a big role in how `==` works. When Python sees an expression like `fluffy == fluffy2`, it tries to find a `__eq__` method in fluffy's class. That is, it tries to find `Cat.__eq__`. If the method exists, Python calls it as `fluffy.__eq__(fluffy2)`.

However, if `Cat.__eq__` doesn't exist, Python looks elsewhere. In the case of Cat, it looks to the object class -- a class that all objects inherit from. There it finds object.`__eq__`, which it calls to evaluate `fluffy == fluffy2`. object.`__eq__ `checks whether two objects are the same object, so `fluffy.__eq__(fluffy2)` returns `True` only when `fluffy` and `fluffy2` reference the same object.

Since the object class has no state, there's nothing that `object.__eq__` can compare for equality. As a result, it defaults treating object identity as equality. That is, two objects are equal only when they are the same object.

What happens when Python encounters an expression like `a == b` where the types of `a` and `b` are different? 

1) Python calls `a.__eq__(b)`.
2) If the return value is a boolean, `a == b` evaluates to that value.
3) If the return value is `NotImplemented`: Python calls `b.__eq__(a)`.
4) If the return value is a boolean, `a == b` evaluates to that value.
5) If the return value is `NotImplemented`: `a == b` evaluates as `a` is `b`, which will usually be `False`.

##### Why might we get unexpected results when comparing instances of A and B if both A and B define a `__eq__` method that doesn't return NotImplemented?

If both class A and class B define an `__eq__` method that returns a boolean (`True` or `False`) instead of `NotImplemented` when faced with an unknown type, you can get non-symmetrical comparison results. This means that `a == b` could evaluate to a different value than `b == a`, which violates the fundamental expectation of how equality should work. In the above, if `a.__eq__(b)` returns `False` instead of `NotImplemented,` Python assumes `a` has authoritatively determined the result and never gives `b` a chance to perform the comparison from its perspective.

Let's imagine a `Fruit` class that knows how to compare itself to a `Vegetable` (based on name), but the `Vegetable` class is stricter and only knows how to compare itself to other `Vegetables`.

**Incorrect Implementation (without NotImplemented)**

```python
class Vegetable:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        # This method only knows about Vegetables
        if not isinstance(other, Vegetable):
            return False # Problem: This gives a final answer!
        return self.name == other.name

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        # This method is more flexible and can check other types
        # It assumes the other object has a `name` attribute
        try:
            return self.name == other.name
        except AttributeError:
            return False

tomato_fruit = Fruit('tomato')
tomato_veg = Vegetable('tomato')

# Let's compare them
print(f"tomato_fruit == tomato_veg: {tomato_fruit == tomato_veg}") #tomato_fruit == tomato_veg: True
print(f"tomato_veg == tomato_fruit: {tomato_veg == tomato_fruit}") #tomato_veg == tomato_fruit: False
```

This is the unexpected result! The two comparisons give different answers. Here's why:

`tomato_fruit == tomato_veg`:

1) Python calls `tomato_fruit.__eq__(tomato_veg)`.
2) The Fruit class's `__eq__` method successfully compares `self.name` and `other.name` (`'tomato' == 'tomato'`) and returns `True`. The process stops.

`tomato_veg == tomato_fruit`:

1) Python calls `tomato_veg.__eq__(tomato_fruit)`.
2) The Vegetable class's `__eq__` method checks `isinstance(tomato_fruit, Vegetable)`, which is `False`. Because this is a boolean, Python considers the comparison finished and never tries `tomato_fruit.__eq__(tomato_veg)`.

**The Solution with NotImplemented**

If `Vegetable.__eq__` returns `NotImplemented`, it signals to Python, "I don't know how to do this comparison, you should try something else."

```python
class Vegetable:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Vegetable):
            return NotImplemented # Correct: Defer the decision
        return self.name == other.name

# ... Fruit class is the same ...

tomato_fruit = Fruit('tomato')
tomato_veg = Vegetable('tomato')

print(f"tomato_fruit == tomato_veg: {tomato_fruit == tomato_veg}") # tomato_fruit == tomato_veg: True
print(f"tomato_veg == tomato_fruit: {tomato_veg == tomato_fruit}") # tomato_veg == tomato_fruit: True
```

Now the results are symmetrical and correct. When `tomato_veg == tomato_fruit` is evaluated, `tomato_veg.__eq__` returns `NotImplemented`, so Python proceeds to call `tomato_fruit.__eq__`, which correctly returns `True`.

By not returning `NotImplemented`, you are short-circuiting Python's comparison logic and preventing it from finding a valid way to compare the two objects.

You can skip the type checks when there's little chance of performing a comparison with a different object type. For instance, a nested class that is marked for internal use can most likely avoid the problem.

##### Customizing `<`, `<=`, `>`, and `>=`

We'll compare Cat objects based on the cat names:

```python
class Cat:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name != other.name

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name < other.name

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name <= other.name

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name > other.name

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name >= other.name

fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')
whiskers = Cat('Whiskers')

print(fluffy < whiskers)      # True
print(fluffy <= whiskers)     # True
print(fluffy <= fluffy2)      # True
print(fluffy > whiskers)      # False
print(fluffy >= whiskers)     # False
print(fluffy >= fluffy2)      # True
```

One last thing: it's worth noting that you don't normally want to use `isinstance` in your code; this is not very object-oriented. However, using `isinstance` in many dunder methods is almost mandatory.

##### How do you decide what makes two instances "equal"?

You decide what makes two instances of your class equal based on the essential attributes that define the object's identity or state within the context of your program. This is a design decision, not a technical one, and it depends entirely on what your class represents.

The key is to ask: "What properties must be the same for two objects of this class to be considered equivalent in my application?"

Consider these examples:

* For a Vector class: Two vectors are equal if their `x` and `y` components are identical. The state is simple and fully defines the object's value.

* For a Person class: Are two Person objects equal if their names are the same? Probably not, as many people share a name. A better choice would be a unique identifier, like a user ID, employee number, or social security number. Equality would be based on that unique ID.

* For the Cat class in the curriculum: The example defines equality based on the name. This is simple for a demonstration, but in a real-world application, you might decide that two Cat objects are only equal if they represent the same cat in a database, identified by a unique `cat_id`.

Ultimately, you must choose the attribute or combination of attributes that uniquely and meaningfully define an instance for the purpose of comparison.

##### Do you always need to define comparison methods?

No, you don't always need to define them. You only need to define them when the default behavior is not what you want.

**When You DON'T Define `__eq__`**

If you don't define `__eq__` (or any other comparison method), Python uses the default behavior inherited from the object class. This default behavior compares objects based on their **identity**, not their state. It's essentially the same as using the `is` operator. **Two objects are only "equal" if they are the exact same object in memory.**

**When You SHOULD Define `__eq__`**

You should define `__eq__` whenever you want to compare instances based on their values or attributes. If you want the code above to return `True`, you must implement `__eq__` to tell Python that two Cat instances are equal if their name attributes are the same.

**What About Other Comparison Methods (<, >, etc.)?**

You only need to define these if it makes sense to order instances of your class.

You should define them if your objects have a natural order. For example, you might want to sort a list of Cat objects alphabetically by name. To do this, you would need to implement `__lt__` (less than), `__gt__` (greater than), etc.
You should not define them if there's no logical ordering. For example, what would it mean for one Vector to be "less than" another? If there's no clear answer, it's better not to implement these methods. If you try to use an operator like `<` on objects that don't have the corresponding dunder method, Python will correctly raise a T`ypeError`.

#### The Arithmetic Models

The `__add__` method lets you control how the `+` operator works with a custom class, while `__iadd__` handles augmented assignment with `+=`. Other arithmetic operator methods include `__sub__` (subtraction with `-`), `__mul__` (multiplication with `*`), `__truediv__` (floating division with `/`), and `__floordiv__ `(integer division with /`/`). There are several more you can use. As with __add__ and __iadd__, you should normally define the __isub__, __imul__, __itruediv__, and __ifloordiv__ methods when you define the primary method.

For all augmented assignment methods (`__iadd__`, `__isub__`, `__imul__`, etc.), you must always return `self` so that the assignment part of the operator completes correctly. This is a strict requirement of how Python's augmented assignment operators work.

Defining arithmetic operators for custom types can lead to elegant code, but only when their use is intuitive and consistent with the rest of Python. The operators must make sense and generally be limited to numeric and sequence types. Don't define arithmetic operators simply because it's cool; it probably isn't.

In particular, the arithmetic operators should obey the commutative and associative laws of arithmetic, as appropriate. For example, `+` and `*` should be commutative and associative.

Commutative law:
```
a + b == b + a
a * b == b * a
```

Associative law:
```
a + (b + c) == (a + b) + c
a * (b * c) == (a * b) * c
```
Most other operators do not have to be commutative or associative.

It's worth noting that concatenation isn't commutative, yet Python uses `+` for strings, lists, and tuples. One could argue that providing `+` for concatenation is non-intuitive. However, it is familiar and comfortable to many developers, not just Python programmers. At this point, concatenation is a perfectly acceptable use for the `+` operator.

The * operator for strings, lists, and tuples is commutative, associative, and relatively intuitive. Performing repetition for other types that support concatenation is acceptable.

Think carefully before defining arithmetic operators for non-arithmetic classes. Operators should be intuitive and consistent with Python's built-in types, or they may lead to confusion and errors.

#### Magic Variables

Python has a handful of **magic variables**, aka **dunder variables**, that are primarily useful for debugging and testing. 

##### The `__name__` Variable

`__name__` returns the current module's name as a string.

If the current module is the program being run, `__name__` returns `__main__.` It's common to see code like this in Python programs to facilitate testing.

```python
if __name__ == '__main__': # call the program's main processing function
```

This code runs the entire program when the module is the main program. It does nothing otherwise. This lets you test your code in a more piecemeal style without running the full program version.

##### The `__file__ `Variable

`__file__` returns the full path name of the current running program. This can help your program find various assets and other resources needed by a program.

```python
import os

print(__file__)
print(os.path.abspath(__file__))
assets = os.path.abspath(f'{__file__}/../assets')
print(assets)

image = f'{assets}/foo.png'
print(image)
```

Then we run this in the terminal:
```python
mkdir ~/Projects/Bar
cd ~/Projects/Bar
python ../Foo/file.py
```

We get:

```python
/Users/me/Projects/Bar/../Foo/file.py
/Users/me/Projects/Foo/file.py
/Users/me/Projects/Foo/assets
/Users/me/Projects/Foo/assets/foo.png
```

On line 3 of `file.py`, we print the value of `__file__`. The output consists of the file name used in the python command (`../Foo/file.py`) appended to the absolute path name of the current working directory (`/Users/me/Projects/Bar`).

If you want to eliminate that relative file reference (`../Foo/file.py`) from the output, you need to request the absolute path name by passing `__file__` as an argument to the path.abspath function from the `os` module. We do this on line 4 of `file.py`. This eliminates the `/Bar/..` portion of the file name.

On line 5 of `file.py`, we want to get the absolute path name of the assets subdirectory in the project directory (`/Users/me/Projects/Foo`). Since we only have `__file__` to work with, we can use a relative path name and pass it to `os.path.abspath`. To get the relative path name, we just append `../assets` to the value of `__file__`.

Finally, on line 8, we print the absolute path name of our `foo.png` image file in the assets folder.

Using `__file__` can be a little tricky until you get comfortable with it. You might think it'll be easier to just hardcode the file and folder names in your program. However, that's not a good idea. Once you start distributing the program, you'll lose control over where people will put the project files. By using `__file__`, relative path names, and `os.path.abspath`, you won't need to care about where people install your software. So long as they don't mess with the folder structure of the project, the program will work.

##### The `__dict__` Variable

`__dict__` returns a dictionary of all the instance variables defined by an object. This can be helpful in the REPL.

```python
class MyClass:

    def __init__(self, x):
        self.x = x
        self.y = []
        self.z = 'xxx'

obj = MyClass(5)
print(obj.__dict__)
# {'x': 5, 'y': [], 'z': 'xxx'}
```

##### Why does Python uses the double underscore naming style for magic variables?

If Python used simple names like `name`, `file`, and `dict` as built-in variables available in every script, you'd run into a serious problem: naming conflicts. These are very common variable names that developers would naturally want to use for their own purposes.

Imagine if name was a reserved global variable, then you couldn't write `name = Alice`. Because `name` would already be bound to Python's special module `name` value. You'd have no way to use that variable `name` for your own data. This would be incredibly frustrating and restrictive.

By using the double underscore naming convention (`__name__`, `__file__`, `__dict__`), Python achieves several things:

1. Avoids Naming Conflicts

The double underscore prefix is so distinctive and unusual that developers naturally avoid it for their own variables. You almost never see someone write `my_var = __something__ `in regular code. So these special variables can coexist peacefully with your own code without collisions.

2. Signals Intent

The double underscores are a visual cue that says: "This is something special and internal to Python. Don't mess with it unless you know what you're doing." It's a convention that communicates meaning to other developers reading your code.

3. Makes the Language More Extensible

By reserving this naming pattern for magic methods and variables, Python can add new special features in future versions without risking conflicts with user code. If Python decided to add a new magic variable in the future, it can safely use the `__name_pattern__` without breaking existing code.

4. Encourages Direct Use in Code

Because the name is so distinctive, when you see `__name__` in code, you immediately know it's something special.

```python
# Less clear what this does
if name == '__main__':
    main()

# Much clearer
if __name__ == '__main__':
    main()
```

This naming convention also reflects Python's philosophy of being explicit and readable. As the Zen of Python says, "Explicit is better than implicit." By using the double underscore convention, Python makes it explicit which names are special and shouldn't be used for regular purposes.

It's worth noting that this convention extends beyond just variables. As you've seen throughout the chapter, dunder methods like `__init__`, `__str__`, `__eq__`, etc., follow the same pattern for the same reasons: they're special methods that Python calls automatically, and the naming convention makes that clear.


Page Reference: [Magic Methods](https://launchschool.com/books/oo_python/read/magic_methods)

[Back to the top](#top)