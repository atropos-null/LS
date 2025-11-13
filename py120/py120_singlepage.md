# Polymorphism

**Polymorphism** refers to the ability of different object types to respond to the same method invocation, often, but not always, in different ways. In other words, data of different types can respond to a common interface. It's a crucial concept in OO programming that can lead to more maintainable code.

When two or more object types have a method with the same name, arguments, and, in some cases, the same return value type, we can invoke that method with any of those objects. When we don't care what type of object is calling the method, we're using polymorphism. Often, polymorphism involves inheritance from a common superclass. However, inheritance isn't necessary as we'll see in this assignment.

There are two chief ways to implement polymorphism. Let's study polymorphism through inheritance first.

### Polymorphism through inheritance

Consider the following class hierachy and associated code:

```python
class Animal:
    def move(self):
        print(f'I am a {self.__class__.__name__}: I am not moving.')

class Fish(Animal):
    def move(self):
        print(f'I am a {self.__class__.__name__}: I am swimming.')

class Cat(Animal):
    def move(self):
        print(f'I am a {self.__class__.__name__}: I am walking.')

# Sponges and Corals don't have a separate move method - they don't
# move
class Sponge(Animal):
    pass

class Coral(Animal):
    pass

animals = [Fish(), Cat(), Sponge(), Coral()]
for animal in animals:
    animal.move()

# I am a Fish: I am swimming.
# I am a Cat: I am walking.
# I am a Sponge: I am not moving.
# I am a Coral: I am not moving.
```

Every object in the `animals` list is a different kind of animal, but the client code -- the code that uses those objects, i.e., the `for` loop -- doesn't care what each object is. The only thing it cares about is that each object in the list has a `move` method that requires no arguments. That is, every animal object can implement some form of locomotion, though some animals don't move. The interface for this class hierarchy lets us work with all of those types in the same way even though the implementations may be dramatically different. That is polymorphism.

If we run the above code, we call the move method for each of 4 different kinds of animal. Let's look at them in pairs.

For `Fish` objects, we call the move method from the `Fish` class, which enables a fish to swim. Likewise, a `Cat` object walks when we tell it to move. This is a simple example of polymorphism in which two different object types can respond to the same method call by **overriding** a method inherited from a superclass. In a sense, overriding methods like this is similar to duck-typing (though we don't call it duck-typing), a concept that we'll meet shortly. However, overriding is considered to be an aspect of inheritance, so this is polymorphism through inheritance.

The `Sponge` and `Coral` classes don't have a `move` method -- at least not one of their own. Instead, they both inherit it from the `Animal` class. Thus, when we call move on a `Sponge` or `Coral` object, the move method in the `Animal` class gets called. That method prints a message, but the message only tells us that the creature in question doesn't move. Often, a method like this might be implemented with a body of pass or return None. Here, we've done a bit more than that, mostly so you can see the polymorphism in action.

In this case, we're still using polymorphism through inheritance. Instead of overriding the `move` method, we're using inheritance to acquire the behavior from a superclass. In this case, that behavior prints an "I am not moving." message, but it could do something else or nothing at all.

Looking at this example, we can see that every object in the list is a different kind of animal, but the client code treats them all as generic animals, i.e., an object that can `move`. Thus, the interface lets us work with all of these types in the same way even though the implementations can be dramatically different. That's polymorphism in action.

**We're personifying for loops a bit here. In practical terms, what do we mean when we say "the for loop doesn't care what each object is?"**

Answer: 

It means the client code (the for loop) relies only on a common interface, not on concrete types. The loop just does “call move with no arguments” for each element, and Python dispatches to the right implementation based on the object. No isinstance checks, no branching, no knowledge of whether it’s a Fish, Cat, Sponge, or Coral—just that each object responds to move().

Example:

```python
animals = [Fish(), Cat(), Sponge(), Coral()]
for animal in animals:   # doesn't inspect types
    animal.move()        # calls the method by name
```

As long as every object in animals has a compatible `move` method, the loop “doesn’t care” what each object actually is. This is the essence of polymorphism described in the assignment: same method name/signature, different implementations.

### Polymorphism through duck typing

**Duck typing** occurs when objects of different unrelated types both respond to the same method name. With duck typing, we aren't concerned with the class or type of an object, but we do care whether an object has a particular behavior. If an object quacks like a duck, then we can treat it as a duck. Specifically, duck typing is a form of polymorphism. As long as the objects involved use the same method name, take compatible arguments, and return compatible values, we can treat the objects as belonging to a common category of objects. However, it does not rely on inheritance since the types are unrelated.

For example, an application may have a variety of elements that can respond to a mouse click by calling a JavaScript method named something like handleClick (JavaScript's naming conventions differ from Python's). Those elements may be completely different -- for instance, a checkbox vs. a text input field -- but they're all clickable objects. Duck typing is an informal way to classify or ascribe a type to objects. Classes provide a more formal way to do that.

In the next example, we define a Wedding class and several preparer classes. The example attempts to implement polymorphic behavior without using duck typing; **it shows you how not to do it!**

```python
class Wedding:
  def prepare(self, preparers):
      for preparer in preparers:
          if isinstance(preparer, Chef):
              preparer.prepare_food(guests)
          elif isinstance(preparer, Decorator):
              preparer.decorate_place(flowers)
          elif isinstance(preparer, Musician):
              preparer.prepare_performance(songs)

class Chef:
    def prepare_food(self, guests):
        # implementation goes here

class Decorator:
    def decorate_place(self, flowers):
        # implementation goes here

class Musician:
    def prepare_performance(self, songs):
        # implementation goes here
```

The problem with this approach is that the `prepare` method has too many dependencies. It relies on specific classes and their names. It also needs to know which method it should call on each of the objects, as well as the argument(s) that those methods require. If you change anything within those classes that impacts Wedding.prepare, you need to refactor the method. For instance, if we need to add another wedding preparer, we must add another elif statement. Before long, the method will become long and messy.

Let's refactor this code to implement polymorphism with duck typing:

```python
class Wedding:
    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_wedding(self)

class Chef:
    def prepare_wedding(self, wedding):
        prepare_food(wedding.guests)

    def prepare_food(self, guests):
        # implementation goes here

class Decorator:
    def prepare_wedding(self, wedding):
        decorate_place(wedding.flowers)

    def decorate_place(self, flowers):
        # implementation goes here

class Musician:
    def prepare_wedding(self, wedding):
        prepare_performance(wedding.songs)

    def prepare_performance(self, songs):
        # implementation goes here

```

Though there is no inheritance in this example, each of the preparer-type classes provides a prepare_wedding method. We still have polymorphism since all of the objects respond to the prepare_wedding method call. If we later need to add another preparer type, we can create another class and implement the prepare_wedding method to perform the appropriate actions.

Note that merely having two different objects that have a method with the same name and compatible arguments doesn't mean that you have polymorphism. In theory, those methods might be used polymorphically, but that doesn't always make sense. Consider the following classes:

```python
class Circle:
    def draw(self):
        pass

class Blinds:
    def draw(self):
        pass

class Beer:
    def draw(self):
        pass
```

These classes each have a method named `draw`, and the methods take no arguments. In the `Circle` class, `draw` presumably draws a `circle` on the screen. In the `Blinds` class, `draw` may cause the window blinds in an office building to be drawn (as in close or open). In the `Beer` class, the `draw` method probably draws a mug of beer from a tap. In theory, you could write some code that uses these methods polymorphically:

```python
for obj in [Circle(), Blinds(), Beer()]:
    obj.draw()

```
However, it's unlikely that this would ever make sense in real code. Unless you're actually calling the method in a polymorphic manner, you don't have polymorphism. In practice, polymorphic methods are intentionally designed to be polymorphic; if there's no intention, you probably shouldn't use them polymorphically.

**Why must polymorphic methods share a common interface in terms of arguments and return values? Why isn't having the same method name sufficient?**

They must be callable and usable in the same way by the client code. Same name alone isn’t enough because:

* Arguments: If methods need different parameters, the caller can’t invoke them uniformly. You’d need conditionals or `isinstance` to decide how to call each one, which breaks polymorphism.

* Return values: If returned types/meanings aren’t compatible, the caller can’t use the results the same way. You’d again need branching to handle differences, defeating the point.

Example where same name isn’t sufficient:

```python
class CsvExporter:
    def export(self, path):  # needs a path
        ...

class DbExporter:
    def export(self):        # no args
        ...
```

Client code can’t just do:

```python
for e in exporters:
    e.export(...)  # what args do we pass?
```

It would need special cases.

Polymorphism works when objects share a common interface: same method name with compatible arguments and return values, so the caller can treat them interchangeably without knowing their concrete types. 


