1. Define a `Dog` class that has a breed instance variable. Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. Print the breed of each dog.

```python

class Dog:

    def __init__(self, breed):
        self.breed = breed

sparky = Dog("Golden Retriever")
milo = Dog("Poodle")

print(sparky.breed) #Golden Retriever
print(milo.breed) #Poodle
```

2. Add a `get_breed` method to the `Dog` class from your answer to the previous problem. The method should return the dog's breed. Use the method to print the breeds of the two dog objects you created in the previous problem. You should also mark the breed instance variable for internal use only.

```python
class Dog:

    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed
    

sparky = Dog("Golden Retriever")
milo = Dog("Poodle")

print(sparky.get_breed()) #Golden Retriever
print(milo.get_breed()) #Poodle
```

3. Create a `Cat` class that has a single method named `get_name` that returns the name instance variable. Without initializing name, try to instantiate a `Cat` object and call `get_name`. Print `Name not set!` when the error occurs.

```python
class Cat:

    def get_name(self):
        try:
            return self.name 
        except AttributeError:
            return "Name not set!"

fluffy = Cat()
print(fluffy.get_name())
```

4. Create an instance of the `Dog` class from your answer to Problem 2. Set its breed directly from outside the class, then print the resulting breed.

```python
class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed
    

sparky = Dog("Golden Retriever")
sparky._breed = "Pug"

print(sparky.get_breed()) #Pug
```

5. Define a `Student` class that has a class variable named school_name. You should initialize the school name to 'Oxford'. After defining the class, instantiate an instance of the `Student` class and print the school name using that instance.

```python
class Student:

    school_name = "Oxford"

avg_student = Student()
print(avg_student.__class__.school_name)
print(avg_student.school_name)
```

6. Modify the `Student` class from your answer to the previous problem. The modified class should have an instance variable called name that gets initialized during instantiation. Create two `Student` objects with different names but the same school, then print the name and school for both students.

```python
class Student:

    school_name = "Oxford"

    def __init__(self, name):
        self.name = name

student1 = Student("Wolfgang")
student2 = Student("Joseph")
print(student1.name, student1.__class__.school_name) #Wolfgang Oxford
print(student2.name, student2.__class__.school_name) #Joseph Oxford
```

7. Modify the `Student` class from your answer to the previous problem. The modified class should have a class method that returns the school's name. Without instantiating any `Student` objects, print the school's name in two different ways: once with the class method, and once by accessing the class variable directly.

```python
class Student:

    school_name = "Oxford"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

print(Student.school_name)
print(Student.get_school_name())
```

8. Create a `Car` class that has a class variable named manufacturer and an instance variable named manufacturer. Initialize these variables to different values. Add a `show_manufacturer` method that prints both the class and instance variables.

```python

class Car:

    manufacturer = "BMW"

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(f"{Car.manufacturer=}")
        print(f"{self.manufacturer=}")


car = Car("Mazda")  #Car.manufacturer='BMW'
car.show_manufacturer() #self.manufacturer='Mazda'
```

9. Create a `Bird` class that has an instance attribute, species. Create a `Sparrow` class that inherits from the `Bird` class. Create a `Sparrow `instance object, then print its species. The expected output is sparrow.

```python
class Bird:

    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    pass

manny = Sparrow("sparrow")
print(manny.species)
```

10. Consider the following code:

```python
class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)               # What will this output?
```

Without running the above code, what will it output? If it raises an error, explain why and how to fix it.

Answer: Attribute error. needs a `super()`

```python
class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)
```

11. Create a `Mammal` class that always sets an attribute called legs to a value of `4`. Create a `Human` class that inherits from `Mammal`, but instead sets the value of legs to `2`. Print the number of legs for a human to verify correct operation.

```python
class Mammal:

    def __init__(self):
        self.legs = 4


class Human(Mammal):

    def __init__(self):
        self.legs = 2

mammal = Mammal()
human = Human()
print(mammal.legs) #4
print(human.legs) #2
```

12. Consider the following code:

```python
class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())
```

What will this code output, and why?

Answer: 'roar' Since we called make_sound with Lion as the caller, cls must be the Lion class. Therefore, the return value is the value of Lion.sound.

13. Consider the following code:

```python
class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"
```

When an instance of Pine is created, what value will its type attribute have? Why?

Answer: "Pine Tree". Based on the code in Pine.__init__, we'll first call Tree.__init__ where that shared variable will be set to 'Generic Tree'. However, when execution returns to Pine.__init__, self.type will be reassigned to 'Pine Tree'.

14. Consider the following code:

```python

class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)
```

What will happen if you were to run it? Why?

Answer: "AttributeError: 'B' object has no attribute 'var_a'. Did you mean: 'var_b'?" Since B.__init__ doesn't call super().__init__, b knows nothing about the var_a instance variable.