# Problems accompanying OOP Book

Page Reference: [Classes and Objects](https://launchschool.com/books/oo_python/read/classes_objects#exercises)

##  Create a Car class that meets these requirements:

1) Each Car object should have a model, model year, and color provided at instantiation time.
2) You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
3) Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
4) Create a method that prints a message about the car's current speed.
5) Write some code to test the methods.

```python
class Car:
    
    def __init__(self, model, year, color):
        self.model = model 
        self.year = year
        self.color = color
        self.speed = 0
    
    def turn_on(self):
        print(f"{self.model} is on.")
    
    def accelerate(self, speed):
        self.speed += speed
        print(f"{self.model} is accelerating.")
    
    def brake(self, speed):
        self.speed -= speed
        if self.speed < 0:
            self.speed = 0  
        print(f"{self.model} is braking.")

    def turn_off(self):
        print(f"{self.model} is off. Goodbye!")

    def display_speed(self):
        print(f"{self.model} is moving at {self.speed} miles per hour.")
        

toyota = Car("Toyota", 2016, "red")
mazda = Car("Mazda", 2020, "white")
toyota.turn_on()
toyota.accelerate(40)
toyota.brake(10)
toyota.display_speed()
toyota.turn_off()

mazda.display_speed()
```

### Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests. 

```python
class Car:
    
    def __init__(self, model, year, color):
        self._model = model 
        self._year = year
        self.color = color
        self.speed = 0
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year
    
    def turn_on(self):
        print(f"{self._model} is on.")
    
    def accelerate(self, speed):
        self.speed  += speed
        print(f"{self._model} is accelerating.")
    
    def brake(self, speed):
        self.speed  -= speed
        if self.speed  < 0:
            self.speed  = 0  
        print(f"{self._model} is braking.")

    def turn_off(self):
        print(f"{self._model} is off. Goodbye!")

    def display_speed(self):
        print(f"{self._model} is moving at {self.speed } miles per hour.")
    
toyota = Car("Toyota", 2016, "red")
mazda = Car("Mazda", 2020, "white")
toyota.turn_on()
print(f"Your {toyota.model} is {toyota.color}.") 
toyota.accelerate(40)
toyota.brake(10)
toyota.display_speed()
toyota.color = "black"
print(f"Your {toyota.model} is {toyota.color}.") 
toyota.turn_off()
mazda.display_speed()
```

### Add a method to the Car class that lets you spray paint the car a specific color. Don't use a setter method for this. Instead, create a method whose name accurately describes what it does. Don't forget to test your code.

```python

class Car:

    def __init__(self, model, year, color):
        self._model = model 
        self._year = year
        self.color = color
        self.speed = 0

    def turn_on(self):
        print(f"{self._model} is on.")

    def accelerate(self, speed):
        self.speed  += speed
        print(f"{self._model} is accelerating.")

    def brake(self, speed):
        self.speed  -= speed
        if self.speed  < 0:
            self.speed  = 0  
        print(f"{self._model} is braking.")

    def turn_off(self):
        print(f"{self._model} is off. Goodbye!")

    def display_speed(self):
        print(f"{self._model} is moving at {self.speed } miles per hour.")

    def get_color(self):
        return self.color

    def spray_paint(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError('Color must be a string')
        self.color = new_color
        print(f"Your {self._model} is now {self.color}")

toyota = Car("Toyota", 2016, "red")
mazda = Car("Mazda", 2020, "white")
toyota.turn_on()
print(f"Your Toyota color is {toyota.get_color()}.")
toyota.accelerate(40)
toyota.brake(10)
toyota.display_speed()
toyota.turn_off()
toyota.spray_paint("black")
```

### Add a class method to your Car class that calculates and prints any car's average gas mileage (miles per gallon). You can compute the mileage by dividing the distance traveled (in miles) by the fuel burned (in gallons)


```python

class Car:

    def __init__(self, model, year, color):
        self._model = model 
        self._year = year
        self._color = color
        self.speed = 0

    def turn_on(self):
        print(f"{self._model} is on.")

    def accelerate(self, speed):
        self.speed  += speed
        print(f"{self._model} is accelerating.")

    def brake(self, speed):
        self.speed  -= speed
        if self.speed  < 0:
            self.speed  = 0  
        print(f"{self._model} is braking.")

    def turn_off(self):
        print(f"{self._model} is off. Goodbye!")

    def display_speed(self):
        print(f"{self._model} is moving at {self.speed } miles per hour.")

    def get_color(self):
        return self._color

    def spray_paint(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError('Color must be a string')
        self._color = new_color
        print(f"Your {self._model} is now {self._color}")

    @classmethod
    def gas_mileage(cls, gallons, miles):
        if gallons == 0:
            return 0  # Avoid division by zero
        return miles / gallons

toyota = Car("Toyota", 2016, "red")
mazda = Car("Mazda", 2020, "white")
toyota.turn_on()
print(f"Your Toyota color is {toyota.get_color()}.")
toyota.accelerate(40)
toyota.brake(10)
toyota.display_speed()
mileage = Car.gas_mileage(13, 351)
print(f'Your car averages {mileage:.1f} miles per gallon') # Output: 27.0 
toyota.turn_off()
toyota.spray_paint("black")

mazda.display_speed()
mileage = Car.gas_mileage(12, 240)
print(f'Your car averages {mileage:.1f} miles per gallon') # Output: 27.0 
```

### Create a Person class with two instance variables to hold a person's first and last names. The names should be passed to the constructor as arguments and stored separately. The first and last names are required and must consist entirely of alphabetic characters.

The class should also have a getter method that returns the person's name as a full name (the first and last names are separated by spaces), with both first and last names capitalized correctly.

The class should also have a setter method that takes the name from a two-element tuple. These names must meet the requirements given for the constructor.

```python

class Person:

    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)
    
    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f'{first_name} {last_name}'
    
    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)
    
    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic.')
    
    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name

actor = actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.
character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.
friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.

```

## Going back to your solution to exercise 1, refactor the code to replace any methods that can be converted to static methods. Once you have done that, ask yourself whether the conversion to a static method makes sense.


```python

class Car:
    
    def __init__(self, model, year, color):
        self.model = model 
        self.year = year
        self.color = color
        self.speed = 0
    
    @staticmethod
    def turn_on():
        print(f"Your car is on.")
    
    def accelerate(self, speed):
        self.speed += speed
        print(f"{self.model} is accelerating.")
    
    def brake(self, speed):
        self.speed -= speed
        if self.speed < 0:
            self.speed = 0  
        print(f"{self.model} is braking.")

    @staticmethod
    def turn_off():
        print(f"Your car is off. Goodbye!")


    def display_speed(self):
        print(f"{self.model} is moving at {self.speed} miles per hour.")
        

toyota = Car("Toyota", 2016, "red")
mazda = Car("Mazda", 2020, "white")
toyota.turn_on()
toyota.accelerate(40)
toyota.brake(10)
toyota.display_speed()
toyota.turn_off()

mazda.display_speed()
```

## Create a Car class that makes the following code work as indicated:

```python
vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')
```

```python
class Car:
    
    def __init__(self, model, year, color):
        self._model = model 
        self._year = year
        self.color = color
        self.speed = 0
    
    def __str__(self):
        return f'{self.color.title()} {self.year} {self.model}'

    def __repr__(self):
        color = repr(self.color)
        year = repr(self.year)
        model = repr(self.model)
        return f'Car({model}, {year}, {color})'
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year
    
    def turn_on(self):
        print(f"{self._model} is on.")
    
    def accelerate(self, speed):
        self.speed  += speed
        print(f"{self._model} is accelerating.")
    
    def brake(self, speed):
        self.speed  -= speed
        if self.speed  < 0:
            self.speed  = 0  
        print(f"{self._model} is braking.")

    def turn_off(self):
        print(f"{self._model} is off. Goodbye!")

    def display_speed(self):
        print(f"{self._model} is moving at {self.speed } miles per hour.")
    
vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')
```

## Don't let the mathiness of this problem scare you off. You don't have to know any math; you only need to know how to write code.

Update the following:

```python
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # __iadd__ method omitted; we don't need it for this exercise

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)
```

```python
print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1)) # 13.0
```

```python
import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        dot_product = ((self.x * other.x) +
                        (self.y * other.y))
        return dot_product

    def __abs__(self):
        sum_of_squares = ((self.x ** 2) +
                          (self.y ** 2))
        return math.sqrt(sum_of_squares)

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'
```

## Challenge: Create the classes needed to make the following code work as shown:

```python
mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()
```

To output:

```
Mike Jones: 3 votes
Susan Dore: 4 votes
Kim Waters: 1 votes

Susan Dore won: 50.0% of votes
```

```python
class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self.votes += other
        return self

class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        max_votes = 0
        vote_count = 0
        winner = None

        for candidate in candidates:
            vote_count += candidate.votes
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate.name

        for candidate in candidates:
            name = candidate.name
            votes = candidate.votes
            print(f'{name}: {votes} votes')

        percent = 100 * (max_votes / vote_count)
        print()
        print(f'{winner} won: {percent}% of votes')
```