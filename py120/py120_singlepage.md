# Collaborators

## Objects as State

By now, you should know that classes group common behaviors and objects encapsulate state. An object's state is saved in the object's instance variables. Instance methods can operate on the instance variables. The state is often a string or number. For example, a Person object's my_name attribute is likely to contain a string:

```python
class Person:
    def __init__(self, my_name):
        self.my_name = my_name

    def name(self):
        return self.my_name

joe = Person('Joe')
print(joe.name())             # Joe
print(type(joe.name()))       # <class 'str'>
```

Notice that `self.my_name` holds a string object. That is, '`Joe`' is an object of the `str` class. There's nothing special about the `str` class. Instance variables can hold any object. For instance, it can hold data structures, like lists or dictionaries:

```python
class Person:
    def __init__(self):
        self._heroes = ['Superman', 'Spiderman', 'Batman']
        self.cash = {
            1:   12,  # The key is bill value, value is count
            2:   1,
            5:   2,
            10:  3,
            20:  2,
            50:  1,
            100: 1,
        }

    def cash_on_hand(self):
        return sum([bill_value * count
                    for (bill_value, count) in self.cash.items()])

    def heroes(self):
        return ', '.join(self._heroes)

joe = Person()
print(joe.cash_on_hand())  # 244
print(joe.heroes())        # Superman, Spiderman, Batman
```

In the above example, you can see that we have used a list and a dictionary to represent the object's state. Instance variables can be set to any object, even an object of a custom class you've created. Suppose we have a `Person` that has a `Pet`, like this:

```python
class Person:
    def __init__(self, name):
        self.name = name

class Dog:
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    pass

bob = Person('Robert')
bud = Bulldog()

bob.pet = bud
print(bob.pet)      # <__main__.Bulldog object at 0x105001f50>
```

Those last two lines are something we haven't seen yet, but it's a perfectly valid OO code. We've created a brand new `self.pet` instance variable in bob, and assigned it to the Bulldog object, bud. Thus, when we reference bob.pet on the last line, it returns a Bulldog object.

Since `bob.pet` returns a Bulldog object, we can chain any Bulldog methods to the return value:

```python
print(bob.pet.speak())        # bark!
print(bob.pet.fetch())        # fetching!
```

## Collaboration

In OOP, if object A calls any methods or accesses any instance variables of object B, then object B is a **collaborator** of object A. If object A just holds on to object B for some time, but doesn't do anything with it other than print or return it, then object B is not a collaborator of object A. There are many other ways in which collaboration is defined, but this explanation is perhaps the easiest to understand.

In the above example, bob has a Bulldog collaborator object stored in the `self.pet` instance variable. When we need that Bulldog object to perform some action (i.e., we want to access some behavior of the bulldog), we can go through bob and call the method on the object stored in `self.pet`, such as speak or fetch.

Here's another example:

```python
class Engine:
    def start(self):
        pass

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

class Driver:
    def __init__(self, car):
        self.car = car

    def drive(self):
        return self.car.start()

engine = Engine()
car = Car(engine)
driver = Driver(car)
```

In this code, a `Car` object is a collaborator of a `Driver` object since a driver needs a car to drive. Likewise, an Engine object is a collaborator of a `Car` object; a car needs an engine or it won't run.

Collaboration can also take place inside a class's methods by using method arguments and instance variables as collaborators:

```python
class Foo:
    def __init__(self, obj):
        self.obj = obj

    def bar(self, qux):
        return self.obj.name() + qux.name()
```

In this code, `self.obj` and `qux` are both collaborators of the Foo class's instance objects.

Collaborators are usually custom objects (e.g. defined by the programmer and not inherited from the Python core library). For example, driver is an example of a custom object. However, collaborator objects aren't strictly custom objects. Even the string object stored in `bob.name` might be considered a collaborator object were the Person object to use the string in some way to carry out its functionality. This usually involves something more than just printing or returning the value.

Collaborator objects play an important role in object-oriented design, since they represent the connections between various actors in your program. When working on an object-oriented program be sure to consider what collaborators your classes will have and if those associations make sense, both from a technical standpoint and in terms of modeling the problem your program aims to solve.

In essence, collaborator objects in OOP let objects work together, each handling specific responsibilities and creating a well-structured, maintainable, and efficient application.

Next, let's change our Person/Dog/Bulldog program from the 3rd code block on this page to let a person have many pets. How should we implement this? How about a list of pets?

```python
class Person:
    def __init__(self, name):
        self.name = name

class Pet:
    def jump(self):
        return 'How high?'

class Dog(Pet):

    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    pass

class Cat(Pet):
    pass

bob = Person('Robert')
kitty = Cat()
bud = Bulldog()
bob.pets = [kitty, bud]
print(bob.pets)
# [<__main__.Cat object at 0x102daa410>,
#  <__main__.Bulldog object at 0x102daa450>]
```

Notice that `bob.pets` is a list. The first element is a Cat object, while the second is a Bulldog object. Since it's a list, you can't just call `Pet` methods on pets:

```python
bob.pets.jump()
# AttributeError: 'list' object has no attribute 'jump'
```

There is no `jump` method in the list class, so we get an error. If we want to make each individual pet jump, we'll have to parse out the elements in the list and operate on the individual Pet object. Here, we'll just iterate through the list.

```python
for pet in bob.pets:
    pet.jump()
```

When working with collaborator objects in your class, you may be working with strings, integers, lists, dictionaries, or even custom objects. Collaborator objects allow you to chop up and modularize the problem domain into cohesive pieces; they are at the core of OO programming and play an important role in modeling complicated problem domains.

Question:

**Could a collaborator object be shared between two different objects? What kinds of problems might this solve, and what kinds of problems could it introduce?**

Yes. Two different objects can hold references to the same collaborator object (the same underlying instance) and call its methods. What it can solve:

* Reduce duplication: share a single service-like object (e.g., a logger, config, cache) across many objects.
* Consistency: centralized state/behavior so every user sees the same data and rules.
* Coordination: a shared object can mediate interactions (e.g., a shared queue or controller).

What it can introduce:

* Coupling and side effects: if the collaborator is mutable, changes by one owner affect the other (aliasing). This can create hard-to-track bugs.
* Ownership/lifecycle issues: who is responsible for initializing, resetting, or disposing of the shared object?
* Invariants and ordering: one object might put the collaborator into a state that makes another object fail.
* Concurrency concerns (if applicable): simultaneous access to shared mutable state needs coordination.

Tips:

* Prefer sharing stateless or immutable collaborators when possible.
* If mutation is needed, encapsulate changes behind well-defined methods.
* Consider copying/defensive copying when callers shouldn’t see each other’s changes.
* Make responsibilities explicit: inject the collaborator where needed and document who may modify it.

This aligns with the assignment’s definition that a collaborator is any object whose methods or instance variables are used by another object; sharing just means multiple objects treat the same instance as their collaborator. 