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
If you later switch to properties (@property), callers can still write obj.name, but you retain all the above flexibility.

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