# In My Words, what I wish I had for PY120

> In the literature of the object-oriented world one of the classic characterizations of the approach is called responsibility-driven design; it uses the word *_roles_* and *_responsibilities_* rather than tasks. The main point is to think about code in terms of **behavior** rather than in terms of data or algorithms."

> - JWPercival (2020)

***

## First Principles

Everything in Python is an object, and all computation happens by sending messages to objects according to fixed rules.

Python is a runtime dispatch system. Top level syntax issues operation requests to objects. Objects participate in these requests via protocoals utilizing dunder methods.  Behavior is selected by MRO. Failure travels via stack unwinding.

There are two messages channels happening within Python: First is a value channel (returns), second is an exception channel (raise/unwind). Every call has two exits.

Meaning lives in the interpreter’s protocol rules and in the object’s ability to satisfy a protocol. 

Objects are allowed to remain ignorant of each other's implementations. Ignorance is a feature, not a flaw. Print must not know what it is printing, only that it can be print. Join must not know what its joining, containers must not know what they are containing. 

Protocols are defined by the Python interpreter, not the class. A class either honors the protocol or violates it. Dispatch is how Python interpreter decides which object behavior runs next. Dispatch means "look for method on this object. If it is not found, follow the MRO. "

Python binds late with strict contracts and ignorance is preserved. 

## Duck Typing

Let's talk about "Duck Typing". Duck typing is not just a cute pythonic way to structure your OOP code. Duck typing is Python's operational philosophy. Every meaningful action in Python is a conversation between objects mediated by the interpreter protocols. There is no central authority within Python saying "You are a list, and you are an integer". Instead, at **runtime** Python asks, "Do you respond correctly I send you this message?"

In many languages types define behavior, inheritance grants permission and interfaces are contracts you must sign in advance. In python, behavior defines type, permission is granted retroactively and contracts are invisible. There is no ontological rock bottom in Python until you hit `type()`. 

## Attributes and State

Attribute is the collective variables, data, and methods of a given object. Concretely, it is everything to the right of the dot in `obj.x()`. 

To the right of the dot we have:
1. Instance variables
2. Instance methods
3. Properties, a mix of both variables and methods.

### The Three Types

1. Instance Methods:
* `self`
* bound to an instance
* used when behavior depends on instance state

2. Static Methods:
* no first parameter, just namespaced inside the class
* used when behavior logically belongs to a class but doesn't depend on class or instance

3. Class Methods:
* `cls`
* bound to class object
* used when behavior depends on class identity

Instance methods preserve polymorphism of behavior; class methods preserve polymorphism of construction.

```python

class Animal:

    def speak(self):
        return "..."
    
class Dog(Animal):
    
    def speak(self):
        return "Woof"

class Cat(Animal):

    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())

```

What didn't change? `speak()` and `a.speak()`. What changed? Behavior changed at runtime as determined by type.


Instance methods preserve **behavior** along the inheritance morphism. Class methods preserve **identity** along the inheritance morphism.

```python

class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())  # Same call, different behavior per instance
```

`speak()` is the same interface, but each instance gives a different response. This is polymorphism after construction — at the moment of behavior.

By the way, `super()` changes the method resolution, not the binding target. Likewise, `cls` is determine by the call site, not the defining class. 

### Properties

Properties look like a variable on the outside but are methods on the inside.  The `@property` decorator, when applied to a method, makes it inaccessible as a method. You must access it like one would as an instance variable. `@property` automatically defines a getter but not a setter.  `@property` is invoked when you read the attribute attachment to it, but the setter is invoked if one tries to write to it.

```python

class Ticket:

    def __init__(self, price):
        self.price = price #Setter is called!
    
    @property
    def price(self):
        return self._price 

    @price.setter
    def price(self, new_price): 
        #Validation stuff normally
        self._price = new_price
```

### Class Methods

Class methods are most useful for the alternate constructor patterns, which happens when the object is created by the class method and not the `__new__`/`__init__` combination. An alternate constructor method is a class method that creates and returns an instance of the class using a different input pattern. It normally looks like:

```python

#Typical constructor method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Alternate constructor method

    @classmethod
    def from_string(cls, data):
        name, age = data.split(", ")
        return cls(Name, int(age))

p = Person("Alice", 50) #init method construction
q = Person.from_string("Alice, 50") #alternate constructor

```

In `q` the `cls(name, age)` is executed and the class method delegates back to the class call. 

With `cls(name, age)` can subclass Person and the subclass inherits the constructor and returns the sucblass automatically, preserving polymorphism.  It is best used when instance create depends on the class and needs to preserve subclass correctness. 

**`cls` is whomever the method was called on, not necessarily the base class!** `cls` is about deferring identity. Whenever a method needs to create "another object of my own kind" and that method might be inherited, cls must be used. 

When you define 
```python
@classmethod
def foo(cls):
    ...
```

You are defining a function that will be bound to the class object and not the instance object. Class methods participate in Polymorphism at the class level.  Class methods are most important when the behavior depends on which concrete class is calling the method. Class methods preserve type identity across inheritance. Common roles for class methods are

* alternate constructor
* factory
* class-level bookkeeping
* modifying class attributes


#### How Class methods preserve polymorphism of construction

Instance methods preserve polymorphism of behavior. Class methods preserve polymorphism of construction. Same polymorphism principle, different moment in the lifecycle.

Class methods defer object construction to the dynamic calling class. Subclasses must inherit construction pathways without being collapsed back into the base type. The key insight: because `cls` refers to whichever class was actually called (not hardcoded to the base class), subclasses can inherit and override construction just like they override behavior.


```python
class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_dict(cls, data: dict):
        # cls is whichever class this is called on
        return cls(data["name"])

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

data = {"name": "Buddy"}

dog = Dog.from_dict(data)  # cls = Dog → creates a Dog
cat = Cat.from_dict(data)  # cls = Cat → creates a Cat

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Buddy says Meow!
```

`from_dict()` is the same interface, but each subclass uses it to construct a different type. This is polymorphism during construction — before behavior even begins.

If you had hardcoded `Animal(data["name"])` instead of `cls(data["name"])`, this polymorphism would break — subclasses would always create a base `Animal` instead of their own type.

```
[Class exists]
     │
     ▼
@classmethod → from_dict(cls, ...)    ← Polymorphism of CONSTRUCTION
     │                                   (Which type gets built?)
     ▼
[Instance exists]
     │
     ▼
def speak(self)                        ← Polymorphism of BEHAVIOR
                                         (How does this instance act?)
```

Instance methods let subclasses say: "I behave differently from my parent." Class methods let subclasses say: "I am constructed differently from my parent." Both use the same polymorphism principle — the same method name does something different depending on which class/instance is involved — but one operates at the creation stage and the other at the usage stage of an object's life.

The magic of `cls` is that it's not hardcoded — it refers to whichever class was actually called. This means subclasses get constructors for free, and they return the right type:

Instance methods require an object to already exist. Class methods don't — they're callable on the class directly. This is useful for setup, validation, or configuration that logically happens before construction.

```python
class Config:
    _settings = {}

    @classmethod
    def load(cls, filepath):
        import json
        with open(filepath) as f:
            cls._settings = json.load(f)

    @classmethod
    def get(cls, key):
        return cls._settings.get(key)

# No instance needed — call directly on the class
Config.load("settings.json")
value = Config.get("debug")
```

## Polymorphism

Polymorphism means "The same interface call produces behavior appropriate to the actual concrete type."

so in `obj.method` it is whatever fills out the `.method`. A class method is a method whose receiver is the class object rather than the instance object.

There are two important forms of polymorphism:

1. Instance dispatch (virtual method calls)
2. Constructor dispatch (which concrete type gets created)

Polymorphism exists when a single syntatic form invokes behavior that is selected based on the runtime type of the receiver. Stated another way: Different types implement the same operation name, but each type provides its own implementation of that operation.

You'll see Polymorphism in two main ways:
1. Subtype polymorphism (aka inheritance-based)
2. Duck typing (behavior-based)

### `a + b`

```python
a + b
```

`+` is also polymorphism.

If `a` is an int, it triggers addition, and `__add__`
If `a` is a list, it triggers concatenation
If `a` is a custom class, `+` is whatever `__add__` defines.

Same operator, different behavior based solely on the type at runtime.

Polymorphism is fundamentally about disptach.  If dispatch selects behavior based on runtime type its automatically Polymorphism. If behavior is instead fixed regardless of type, you don't. 


## Encapsulation

Official Definition: The internal state and implementation details of an object are hidden behind a controlled interface. In Python this usually means exposing methods instead of raw data via use of properties, using the single underscore or controlling mutation pathways.  Encapsulation is defining how the outside world is allowed to interact with an object. It allows internal change without break existing code and protects invariants.  It exists so humans can reason about objects safely.

Without encapsulation invariants become socially enforced but with encapsulation invariants become structurally enforned. Encapsulation is the practuce of restricting direct acccess to objects internal state and requiring interaction through a defined interface in order to protect invariants and preserve flexibility of implementation.

Encapsulation is about defining where meaning is allowed to change. It draws a boundary. Inside the boundary implementation may evolve. Outside the boundary, behavior must remain stable.

Encapsulation is about ensuring that the invariant of an object cannot be violated by external mutation. If your object promises "I always represent a Valid Angle between 0-360 degrees", then any path that sets the external state must enforce that.

Properties give you a stable public interface and a validation check on mutation. **Encapsulation guards the Truth Conditions of Your Object**.

Encapsulation covers two closely related ideas: simplifying behavior and hiding data. We encapsulate behavior by identifying a task to a well-defined object or function. We call that object or function an **abstraction**. 

### Name Mangling

```python

class A:

    def __init__(self):
        self.__x = 5
```

Python rewrites it to `_A.__x`.

`self.__x` => `self._A__x`

Name mangling exists to prevent accidental override in subclasses. Without mangling:

```python

class A:

    def __init__(self):
        self.value = 10

class B(A):

    def __init__(self):
        super().__init__()
        self.value = 20.  # B just stomped all over A's attributes.

```   

With mangling:

```python
class A:

    def __init__(self):
        self.__value = 10

class B(A):

    def __init__(self):
        super().__init__()
        self.__value = 20. 
```

Output:

```
self._A__value
self._B__value
```

### `__class__`

Every object carries a pointer to its type.

`obj.__class__` is functionally equivalent to `type(obj)`, except the former is an attribute access and the later is a function call. `__class__` is useful for  `return self.__class__(new_value)` which preserves subclass correctness

### `__name__`

On classes: `User.__name__` => User 
On instances: `user.__class__name__` => `User`

`print(f"I am a {self.__class__.__name__}")` is dynamic across classes.

```python

class Animal:

    def speak(self):
        print(f"I am a {self.__class__.__name__}")

class Dog(Animal):
    pass

a = Animal()
a.speak() # I am an Animal
d = Dog()
d.speak() # I am a Dog
```

`self.__class__` is bound at runtime. `obj.__name__` will raise an AttributeError because instances do not have names, but classes, functions and modules do.

### Duck Typing

Behavior is validated at the moment of use (aka runtime) via protocol participation (dunder methods). But at the language level, the question is always "Does the object satisfy the requested protocol?"

### MRO

MRO is the deterministing Path through the inheritance graph that asks "Where do I find the implementation of this behavior?"

### Inheritance

Use inheritance when a subtype must be useable anwhere its supertype is expected without breaking invariants.


## Exceptions

An exception is an object that represents an abnormal condition that interrupts normal control flow.  An instance of the BaseException class, when raised, it aborts the current execution path.  The interpreter unwinds the call stack until a matching handler is found.  

When an error occurs, Python responds by raising an exception. An exception needs to be handled or else it will crash. One handles it with a try/except block.

How try and except works:

1. Python executes lines of code in the try.
2. If it gets to the end of the try, it skips over the except.
3. However, if there is a problem in the try, try block is abandoned immediately and routed to the except.
4. Python then checks, does the exception type in the Except block match? If yes, it enters the except block.
5. If the exception type does not mat h it it starts going up the MRO looking for someone to handle it. Fialing finding a handler, it crashes.

Exceptions are not just for damage control. They can be used for flow control.

```python
try:
    from speedyjson import load
except:
    from json import load
```

A single try can have multiple except blocks.

If an exception is raised, Python will check whether its type matches the first except block. If not, it checks the next. Once a match is found, all remaining blocks are skipped.

Pro-Tip: Put as little code as possible on the try block, so that the except block is catching a masking user errors. 

Finally: a block that always run before the end. When you include a finally block, and an excepton is raised that does not match any except block, then the finally block runs first before the exception MRO starts kicking in.

```python

except ExceptionType as e:
```

The variable `e` points to an exception object that is created when the exception is raised.

### Catching and Reraising

just write `raise` by itself with no arguments

```python

try: 
    do_something()

except Excception as e:
    handle_exception()
    raise 
```

Imagine you have a function that reads data from a file and processes it. If an error occurs while reading the file, you might want to log a message or perform some cleanup before allowing the exception to propagate. In this case, you could catch the exception, handle it, and then reraise it so that the calling function is also aware of the error. 

### Exception Anti-Pattern: Don't do this

```python

try:
    do_something()
except:
    pass
```

The except catches every exception and sweeps it under the rug. You don't know your code is shit because it hides all helpful information.  And remember! Stack your Exception blocks from most specific to least specific.


### The Two Paths

There are two distinct paths, the value path and the exception path.

The Value Path includes

* dispatch
* method calls
* rebinding
* continuation
* How to exit the Value Path: Return something.

The value channel dominates: returns and continues.

The Exception Path:
* raise
* "unwind the stack": search for someone to handle the exception
* How to exit: An exception raised.

The path reverses direction tearing down frames until an exception is found. The exception channel can be used in two ways:

1. A signal: caught immediately, treated as normal control. (e.g., `StopIteration`)
2. Exception channel that escapes (unwind or crash, e.g. `TypeError`)

By the way, in
```python
for x in y:
    ...
```

Uses `StopIteration` to stop a loop. The `StopIteration` exception is used to signal the end of an iteration in Python. It is typically raised by an iterator’s `__next__()` method to indicate that there are no more items to be returned. When a StopIteration exception is raised, it tells the for loop or other iteration construct to stop iterating. This is how Python knows when to stop a loop: iteration terminates by unwinding through a tiny, controlled rupture.  **Exceptions are a part of the normal flow of the Value Path.**


```python
def c():
    try:
        raise ValueError("boom")
    finally:
        print("cleanup in c")

def b():
    try:
        return c()
    finally:
        print("cleanup in b")

def a():
    try:
        return b()
    except ValueError:
        print("handled in a")
    finally:
        print("cleanup in a")

a()

#cleanup in c
#cleanup in b
#handled in a
#cleanup in a
```

Python is a dual channel execption where return and raise are equally fundamental.

`NotImplemented` = "I'm not the one you want, but go on"
`raise` = "Straight to jail"

Exceptions are not "things that happens sometimes". They are a parallel control system built into the runtime.  The interpreter is always prepared to leave the current path and just up the call graph.

Python programs execute within a dual-channel control mode where every operation may either produce a variable or initiate an unwinding.  The unwind path is the call chain order, not the source code order. The order goes as follows: the current frame -> the caller -> that caller's caller until we hit the top.

Normal execution follows the AST/BYTEcode order within a frame. Unwinding follows the call stack links between the frames.  During unwinding, Python will still honor finally blocks.  A handler is only elgible if the exception occurs while execution is inside the corresponding `try` suite.  If you've already left the `try`, that handler is no longer active. 

Try/except is literally a stage manager standing besides the trap door in the stage floor. "If you fall through this trap door, with this costume (exception type), I will catch you and put you back on the stage at this mark." Every call site really does have two choices: stay on stage (the return) or drop and re-enter somewhere else (raise)

Exceptions are built-in, non-local control transfer mechanisms.

***

## Final Thoughts

`+=` is rebinding unless it mutates

Intstances don't have `__name__`

`is` never calls a method, its identity only.

`super()` follows MRO 

`join()` does not call `__str__`


***


JWPercival, H. (2020). Architecture Patterns with Python: Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices.(https://openlibrary.telkomuniversity.ac.id/pustaka/160358/architecture-patterns-with-python-enabling-test-driven-development-domain-driven-design-and-event-driven-microservices.html) 