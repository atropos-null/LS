# Classes and Objects

## What is a Class?

A class is a blueprint or template for creating objects. It defines a set of attributes (data) and methods (behaviors) that the objects created from it will have.

## What is an Object?

An object is an instance of a class. It's a concrete entity created from the class blueprint, with its own specific state.

## Understanding the Relationship

Think of a `GoodDog` class. The class itself defines what every dog has (like a name) and what every dog can do (like speak). An individual dog, like `sparky`, is an object created from that class, with its own specific name.

## Example in Python

```python
class GoodDog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Woof!"

# Creating an object (instance) of the GoodDog class
sparky = GoodDog("Sparky")

# Using the object
print(sparky.speak())  # Output: Sparky says Woof!
```

In this example:
- `GoodDog` is the **class** - the blueprint that defines what a dog is
- `sparky` is an **object** - a specific instance of a GoodDog with the name "Sparky"
- The `__init__` method is the constructor that initializes each dog with a name
- The `speak` method defines a behavior that all GoodDog objects can perform
- Each dog object has its own `name` attribute (data)
