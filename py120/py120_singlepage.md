# Problem Sets: Inheritance
Class based inheritance works great when it's used to model hierarchical domains. Let's take a look at a few practice problems. Suppose we're building a software system for a pet hotel business, so our classes deal with pets.

Given this class:

```python
class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!
```

One problem is that we need to keep track of different breeds of dogs, since they have slightly different behaviors. For example, bulldogs snore when they sleep, but other dogs do not. Okay, I have no idea if that's entirely true; I suspect it isn't. Let's pretend it is.

Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"

```python
class Bulldog(Dog):
   def sleep(self):
       return "snoring!"

karl = Bulldog()
print(karl.speak())       # bark!
print(karl.sleep())        # snoring!
```

Note that since Bulldog objects are instantiated from a subclass of Dog, they can both override and inherit methods from the Dog class. That is why karl can speak.

Let's create a few more methods for our Dog class.

```python
class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

    def fetch(self):
        return 'fetching!'
```

Create a new class called Cat, which can do everything a dog can, except fetch. Assume the methods do the exact same thing. Hint: don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.

Possible Solution:

We could just duplicate the methods in the Cat class. But that would violate the DRY principle: "Don't Repeat Yourself." Okay, that's the last time we'll repeat that. That's why we have OOP; so we can organize behaviors into classes and set up a hierarchical structure that takes advantage of inheritance. Inheritance is a way to re-use common behaviors.

```python
class Pet:
    def speak():
        pass

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

    def sleep(self):
        return 'sleeping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'


class Bulldog(Dog):
   def sleep(self):
       return "snoring!"


class Cat(Pet):
    def speak(self):
        return 'meow!'

```

It's getting slightly more complicated, but we've distributed the methods (behaviors) into appropriate classes. All pets (that we know of) can run, jump and sleep, so those methods are in the Pet class. Many, but not all, pets can also speak (in a fashion). We've placed a do-nothing speak method in the Pet class; that lets us call pet.speak() regardless of what kind of pet we have. If the specific pet class provides a way to speak, we can run that method instead. Otherwise, we do nothing.

On top of the above behaviors, dogs can speak, fetch, and sleep. However, bulldogs snore while they sleep, so we override the sleep method to mention that.

Cats don't have any additional behaviors, but they do have their own speak method.

Let's make sure everything works as expected.

```python
pet = Pet()
dave = Dog()
bud = Bulldog()
kitty = Cat()

print(pet.run())              # running!
print(kitty.run())            # running!
print(kitty.speak())          # meow!
try:
    kitty.fetch()
except Exception as exception:
    print(exception.__class__.__name__, exception, "\n")
    # AttributeError 'Cat' object has no attribute 'fetch'

print(dave.speak())           # bark!

print(bud.run())              # running!
print(bud.sleep())             # "snoring!"
```

We've used try/except blocks to handle the exceptions raised when we call methods that don't exist. Without this try/except block, execution would stop with the first error.


What is the method resolution order and why is it important?

The method resolution order (MRO) is the order in which Python traverses the class hierarchy to look for methods. For example, suppose you have a Bulldog object called bud and you call: bud.drool. Python first looks for a Bulldog.drool method. If it finds the method, it invokes the method and stops searching. If it doesn't find Bulldog.drool, it next looks for Dog.drool, then Pet.drool, and, finally, object.drool. If it finds any of these methods, it invokes that method and stops searching. If it doesn't find the method anywhere, it raises an AttributeError.

In our simple class hierarchy, the MRO is pretty straightforward. Things can quickly get complicated in larger libraries or frameworks. To see the MRO, we can use the mro class method.

```python
print(Bulldog.mro())
# [<class '__main__.Bulldog'>, <class '__main__.Dog'>, <class
#'__main__.Pet'>, <class 'object'>]
```

Using mro like that is often not very pretty. Instead, you can use a list comprehension to make the output more readable:

```python
print([ cls.__name__ for cls in Bulldog.mro() ])
# ['Bulldog', 'Dog', 'Pet', 'object']
```
Note that mro returns a list. Additionally, it's important to remember that all classes in Python are subclasses of the object class by default.

