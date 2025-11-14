# Encapsulation

**Encapsulation** is one of the fundamental concepts of object-oriented programming. At its core, encapsulation describes the idea of bundling or combining the data and the operations that work on that data into a single entity, e.g., an object.

Encapsulation lets us hide the internal representation of an object from the outside and only expose the attributes that users of the object need. In practice, Python doesn't properly support encapsulation since it doesn't support access control which limits attribute exposure.

In most OOP languages, encapsulation has a broader purpose. It also refers to restricting access to the state and certain behaviors via access control. An object only exposes the data and behaviors that other parts of the application need to work. In other words, objects expose a public interface for interacting with other objects and keep their implementation details hidden. Thus, other objects can't change the data of an object without going through the proper interface.

As it happens, Python doesn't support access control. That said, Python does have a convention that most experienced Python developers know they should follow. If an attribute's name begins with an alphabetic character, the attribute is intended for use by anybody. However, if the attribute's name begins with an underscore, the attribute is intended for internal use. With this convention, we can talk of encapsulation in Python.

Let's take a quick look at these conventions, starting with how they interact with instance variables.

```python
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self._age = age
        self.__breed = breed

    def __str__(self):
        return f'''
My name is {self.name}.
I am {self._age} years old.
I am a {self.__breed}.
'''

rover = Dog('Rover', 4, 'Mutt')
print(rover)                # My name is Rover.
                            # I am 4 years old.
                            # I am a Mutt.

rover.name = 'Fido'
rover._age = 7
rover.__breed = 'Poodle'
print(rover)                # My name is Fido.
                            # I am 7 years old.
                            # I am a Mutt.
print(rover.__breed)        # Poodle
print(rover._Dog__breed)    # Mutt

rover._Dog__breed = 'Boxer'
print(rover)                # My name is Fido.
                            # I am 7 years old.
                            # I am a Boxer.

```

Let's walk through this code.

On lines 14 and 15, we first create a Dog object, then print it. Everything appears as expected at this point; the name, age, and breed are all correct.

On lines 19-26, we attempt to reassign each instance variable to a new value.

The dog's name attribute gets changed, as expected.

The dog's _age attribute also gets changed. This might be unexpected since the leading underscore indicates that it's for internal use. However, this is merely a convention, and developers can ignore it at their own peril.

A more promising result is that the __breed attribute wasn't changed. Curiously, though, line 25 prints a different breed than was printed by line 22. This is an effect of the name mangling that occurs with double underscore attribute names. Internally, the class's method can refer to __breed properly, but outside the class, the name gets mangled. Line 21 actually created an unmangled instance variable named __breed. However, the class's methods don't recognize that instance variable.
Line 26 uses the mangled, _Dog__breed name for the __breed attribute to access the real attribute.
On lines 28 and 29, we show that we can also modify double-underscore attributes by using the mangled name.

Now let's see how things work with methods:

```python

class Dog:
    def walk(self):
        print('Walking the dog.')

    def _chase_car(self):
        print('I am chasing a car!')

    def __goto_vet(self):
        print('The vet! Run and hide!')

    def a_day_in_the_life(self):
        self.walk()
        self._chase_car()
        self.__goto_vet()

rover = Dog()

rover.a_day_in_the_life()   # Walking the dog.
                            # I am chasing a car!
                            # The vet! Run and hide!

rover.walk()                # Walking the dog.
rover._chase_car()          # I am chasing a car!
rover._Dog__goto_vet()      # The vet! Run and hide!
rover.__goto_vet()
# AttributeError: 'Dog' object has no attribute '__goto_vet'.
```

In this case, we can see on lines 12-14 that methods in the class (a_day_in_the_life) can access any method also defined within the class (walk, _chase_car, and __goto_vet). Even the underscore names work as expected. These methods are intended for internal use, and calling them from within another class-defined method like a_day_in_the_life is consistent with that intent.

The remaining code on lines 22-23 demonstrates that we can call methods that begin with alphabetic characters with no problem. We can even call "internal use" methods whose name begins with a single underscore.

Line 24 shows that we can use a mangled name to access a method whose name begins with a double underscore. Line 25 shows that we can't use the double underscore name to access that method.

Together, these two examples show that Python really doesn't control access to a class's attributes. Names that begin with a single or double underscore, by convention, signal the user of your class that they should not use that attribute. However, Python does nothing to prevent the user from bypassing the convention.

In practice, smart programmers never ignore this naming convention. If they do so, they are asking for future trouble, and most programmers don't like trouble, especially when it arrives at 2:27am on a holiday morning.

As for whether you should use single or double underscores for your internal names, we recommend using single underscores. The main reason for using double underscore prefixes is to prevent name clashes with subclasses, a situation we won't encounter at Launch School.

On a final note, always keep in mind that classes should have as few public attributes as possible. If your users don't need a method or instance variable, use the single underscore convention to let future users know it's for internal users. If you want to provide read-only access to an instance variable, create a property with the `O` decorator.

### Questions:

**What does "internal use" mean in this context? What purpose does a method designated for internal use serve?**

“Internal use” means “meant to be used only inside the class (by its own methods), not part of the class’s public interface that other code should call.”

A method designated for internal use (named with a leading underscore) serves as an implementation detail—typically a helper that supports the class’s public methods. It lets you:

* Hide how the class works behind a simpler public API
* Signal to other programmers that the method isn’t stable for external use and may change without notice

Python doesn’t enforce this; it’s a convention. As shown in the assignment’s example, a public method can call internal ones:

```python
class Dog:
    def _chase_car(self):
        print('I am chasing a car!')

    def __goto_vet(self):
        print('The vet! Run and hide!')

    def a_day_in_the_life(self):
        self._chase_car()
        self.__goto_vet()

```

Here, `_chase_car` and `__goto_vet` are used inside the class to implement behavior, while users of the class are expected to call the public methods.

**Is there any way in Python to completely prevent a programmer from changing an object's internal state? If not, what's the point of using a single underscore to indicate internal use?**

No. Python doesn’t have true access control, so you can’t fully prevent someone from changing an object’s internals. Even double-underscore names are only name-mangled; they’re still accessible.

The single leading underscore is a convention to:

* Signal “this is internal, not part of the public API”
* Discourage external code from depending on it (it may change without notice)
* Improve maintainability by clarifying the class’s public interface

If you want read-only access to data, provide a property via @property, but understand that determined code can still bypass it. 

