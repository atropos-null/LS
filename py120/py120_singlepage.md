# Problem Sets: Classes and Objects

As you know by now, classes are the blueprints for objects. Below are some practice problems that test your knowledge of the connection between classes and objects.

1. Given the following code, create the Person class needed to make the code work as shown:

```python
bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert
```

Possible Solution: 

```python
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
```

2. Modify the class definition from above to facilitate the following methods. Note that there is no name= setter method now.

```python
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith
```

Possible Solution:

```python

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

```
Hint: let first_name and last_name be "states" and create a property that uses those states.

Possible Solution:

This class has three properties, two of which have a setter. The name property constructs the full name from the first_name and last_name properties.

```python
class Person:
    def __init__(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ''
        if len(parts) > 1:
            self.last_name = parts[1]

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
```
There are two items of note here besides the property definitions:

* The __init__ method parses the first and last name from the input name argument. Things get mildly tricky if name doesn't contain both a first and last name.

* The name property applies the strip method to the returned name. Once again, this code is in play if both names aren't available.

3. Add a new setter property for name that takes either a first name or full name, and knows how to set the first_name and last_name properties appropriately. Use the following code to test your code:

```python
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams
```

Possible Solution:

We actually already did this in __init__, so we can just repeat it for the name property's setter.

```python
class Person:
    def __init__(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ''
        if len(parts) > 1:
            self.last_name = parts[1]

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @name.setter
    def name(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ''
        if len(parts) > 1:
            self.last_name = parts[1]

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
```

Note the redundant code in the __init__ method and the name property setter. We can remove that code from __init__ and replace it with an assignment to the name property:

```python
class Person:
    def __init__(self, name):
        self.name = name

    # Remaining code omitted for brevity.
```

This code should provide identical results to Solution 1.

4. Using the class definition from problem 3, let's create some more people (Person objects):

```python
bob = Person('Robert Smith')
rob = Person('Robert Smith')
```

Without adding any code to the Person class, we want to compare bob and rob to see whether they both have the same name. How can we make this comparison?

Possible Solution:

`bob == rob` won't work correctly since `==` only checks whether the two Person objects are the same object. It doesn't check that they have the same name. We have to be more precise and compare the names directly:

```python
print(bob.name == rob.name)         # True
```

The above code compares a string with a string. But aren't strings also just objects of the str class? If we can't compare two Person objects with each other with ==, why can we compare two different str objects with ==

```python
str1 = 'hello world'
str2 = 'hello world'

print(str1 == str2)            # True
```

What about lists, dictionaries, and integers? It seems like Python treats some core library objects differently. For now, memorize this behavior. We'll explain the underlying reason in a future lesson.


5. Continuing with our Person class definition, what do you think the following code prints?

```python
bob = Person('Robert Smith')
print(f"The person's name is: {bob}")
```

See output: ```The person's name is: <__main__.Person object at 0x100385f90>```

We're using string interpolation in this code, as opposed to string concatenation. Python automatically calls the str function on the expression between the {}. Every object in Python responds to the str function which, by default, is inherited from the object class. By default, it prints out some gibberish, which represents the object's place in memory.

Until we learn how to override str's behavior, we must construct the output string in some other way. For instance, we can use:

```python
print("The person's name is: " + bob.name)
# The person's name is: Robert Smith

#or

print(f"The person's name is: {bob.name}")
# The person's name is: Robert Smith
```

Let's override the str function for Person objects by defining a magic method, __str__, in the Person class:

```python
class Person:
   # Code omitted for brevity.

    def __str__(self):
        return self.name
```

Now, what does the below output?

```python
bob = Person('Robert Smith')
print(f"The person's name is: {bob}")
```

This time it works as expected, due to the __str__ method!
```The person's name is: Robert Smith```