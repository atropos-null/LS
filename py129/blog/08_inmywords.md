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

Encapsulation is about defin int where meaning is allowed to change. It draws a boundary. Inside the boundary implementation may evolve. Outside the boundary, behavior must remain stable.


## Exceptions

When an error occurs, Python responds by raising an exception. An exception needs to be handled or else it will crash. One hnadles it with a try/except block.

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

***


JWPercival, H. (2020). Architecture Patterns with Python: Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices.(https://openlibrary.telkomuniversity.ac.id/pustaka/160358/architecture-patterns-with-python-enabling-test-driven-development-domain-driven-design-and-event-driven-microservices.html) 