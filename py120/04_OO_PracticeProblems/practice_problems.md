# OO Practice Problems

<a name="top"></a>

<details>
<summary>Possible Solution</summary>
</details>

## Practice Problems: Easy 1

### Question 1
Which of the following are objects in Python? If they are objects, how can you find out what class they belong to?

```python
True
'hello'
[1, 2, 3, 'happy days']
142
{1, 2, 3}
1.2345
```

<details>
<summary>Answer</summary>

Everything is an object!

```python
print(True.__class__)
print('hello'.__class__)
print([1, 2, 3, 'happy days'].__class__)
print(142.__class__)
print({1, 2, 3}.__class__)
print(1.2345.__class__)
```

</details>


### Question 2

Suppose you have an AngryCat class that looks like this:

```python
class AngryCat:
    def hiss(self):
        print('Hisssss!!!')
```

How would you create a new instance of this class?

<details>
<summary>Answer:</summary>

```python
class AngryCat:
    def hiss(self):
        print('Hisssss!!!')
    

manny = AngryCat()
manny.hiss()
```

To create a new AngryCat object, just use `AngryCat()`.

> You can create a new instance of any class by calling that class's constructor. The constructor returns a new object of the class that has the same name.

</details>

### Question 3

If we have a `Car` class and a `Truck` class and we want to be able to `go_fast`, how can we add the ability for them to `go_fast` using the mix-in `SpeedMixin`? How can you check whether your `Car` or `Truck` can now go fast?

```python
class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car:
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck:
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')
```

<details>
<summary>Answer:</summary>

```python
class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')


ford = Truck()
ford.go_fast()

bugatti = Car()
bugatti.go_fast()
```
</details>

### Question 4

In the previous question, we had a mix-in called `SpeedMixin` that contained a `go_fast` method. We add this mix-in to the Car class as shown below:

```python
class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
small_car.go_fast() # I am a super fast Car!
```

<details>
<summary>Answer</summary>

The line `print(f'I am a super fast {self.__class__.__name__}!')` calls the class name into the f-string.

It works like this:

1. `self` refers to the object referenced by `small_car`. In this case, that's a `Car` object.
2. `self.__class__` returns a reference to the `Car` class, which is an object of the type class.
3. Finally, `self.__class__.__name__` returns the name of the Car class as a string: 'Car'.
</details>

### Question 5

Which of the following classes would create objects that have an instance variable. How do you know?

```python
class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name
```

<details>
<summary>Answer:</summary>

class Pizza would create an instance variable as it has a self in the init.

```python
class Fruit:
    def __init__(self, name):
        my_name = name #No 'self'

class Pizza:
    def __init__(self, name):
        self.my_name = name

berry = Fruit('strawberry')
marinara = Pizza('marinara')
print(berry.my_name) #AttributeError: 'Fruit' object has no attribute 'my_name'
print(marinara.my_name) #marinara
```

Official Answer:

Pizza class instances will have instance variables by virtue of assigning a value to `self.my_name` in the `Pizza.__init__` method. Fruit class instances don't have instance variables since none are defined. `my_name` is a local variable only defined inside `Fruit.__init__`.

You can verify this by using the vars function to see what instance variables exist in Pizza and Fruit objects:

```python
print(vars(Fruit('orange')))     # {}
print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}
```

In this example, we can see that the `Fruit` object has no instance variables, while the `Pizza` object has a `my_name `instance variable whose value is 'pepperoni'.

</details>

### Question 6

Without running the following code, can you determine what the following code will do? Explain why you will get those results.

```python
import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

oracle = Oracle()
print(oracle.predict_the_future())
```
<details>
<summary>Answer</summary>

One of the four list elements will be printed, chose randomly. Code works as expected.

</details>


### Question 7

Suppose you have the `Oracle` class from above and a `RoadTrip` class that inherits from the `Oracle` class, as shown below. What will happen when you run the code?

```python
import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]

trip = RoadTrip()
print(trip.predict_the_future())

```

<details>
<summary>Answer:</summary>

RoadTrip subclass will overwrite the Oracle subclass for 'choices'.

Official answer:

Each time you run this code, it will print one of those messages. It will make that choice randomly.

Why does this happen? Doesn't `self.choices` in `predict_the_future` look in the Oracle class for a choices method? The answer is no. Since we're calling `predict_the_future` on an instance of `RoadTrip`, every time Python tries to resolve a method name using `self.`, it first looks in the class of the calling object. Even though we called choices from with a method in the Oracle class, self refers to the `RoadTrip` class. Thus, Python first looks for `RoadTrip.choices` before falling back to Oracle.choices. To see the difference, change the name of the RoadTrip.choices to RoadTrip.chooses and rerun the program.

</details>

### Question 8

Suppose you have an object named `my_obj` and that you want to call a method named `foo` using `my_obj` as the caller. How can you see where Python will look for the method. You don't need to determine the actual method location; just identifying the search sequence is sufficient.

<details>
<summary>Possible Solution</summary>

`print(my_obj.__class__.mro())`

</details>

### Question 9

There are several variables listed below. What are the different variable types and how do you know which is which?

```python

excited_dog = 'excited dog'
self.excited_dog = 'excited dog'
self.__class__.excited_dog = 'excited dog'
BigDog.excited_dog = 'excited dog'
```

<details>
<summary>Possible Solution</summary>

| Variable                    | Variable Type       |
|-----------------------------|---------------------|
| excited_dog                 | Local variable      |
| self.excited_dog            | Instance variable   |
| self.__class__.excited_dog  | Class variable      |
| BigDog.excited_dog          | Class variable      |

We can tell which is which by how the variables are prefixed. Local variables don't have a prefix, while instance variables are usually prefixed with self..

Class variables are prefixed with self.__class__. when self is an instance of the appropriate class or one of its subclasses. You can also use the name of the class as a prefix, e.g., BigDog.. BigDog is a class variable and the tip off is the PascalCase being used here.

Though not shown here, there are three other ways to access class variables:

You can use a cls. prefix inside class methods.
You can use a type(self). prefix when self is an instance of the class or one of its subclasses.
You can sometimes use a self. prefix when self is an instance of the class or one of its subclasses. However, this is not good practice and should be shunned.

</details>

### Question 10

Suppose you have the following class:

```python
class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
```


Explain what the _cats_count variable is, what it does in this class, and how it works. Write some code to test your theory.

<details>
<summary>Possible Solution</summary>

`_cats.count` is a class variable that tracks the amount of cat objects are instantiated. Everytime a cat object is instantiated, the count goes up by 1. The count is instantiated at the time of its definition.

Every time we create a `Cat` object, Python will call `Cat.__init__`. After saving the cat type in an instance variable, __init__ increments `_cats_count`. Note that we need to reference `self.__class__._cats_count` to access the class variable.

Finally, the class method named `cats_count` returns the current value of the `_cats_count` class variable.

</details>

Page Reference: [Practice Problems: Easy 1](https://launchschool.com/lessons/a6479eb0/assignments/bf55fc72)
[Back to the top](#top)

***

## Practice Problems: Easy 2

### Question 1

Suppose you have these two classes:


```python
class Game:
    def play(self):
        return 'Start the game!'

class Bingo:
    pass
```


Update this code so that Bingo inherits the play method from the Game class.

<details>
<summary>Answer:</summary>

```python
class Game:
    def play(self):
        return 'Start the game!'

class Bingo(Game):
    pass

new = Bingo()
print(new.play())
```

</details>

### Question 2

Update your code from the previous question so the following code works as indicated:

```python
bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'
```

<details>
<summary>Answer:</summary>

```python
class Game:

    count = 0

    def __init__(self, game_name):
        self.game_name = game_name
        Game.count += 1


    def play(self):
        return f'Start the {self.game_name} game!'

class Bingo(Game):
    def __init__(self, game_name, player_name):
        super().__init__(game_name)
        self.player_name = player_name
    

class Scrabble(Game):
    def __init__(self, game_name, player_name1, player_name2):
        super().__init__(game_name)
        self.player_name1 = player_name1
        self.player_name2 = player_name2


bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name) # AttributeError: 'Scrabble' object has no attribute 'player_name'
```
</details>

### Question 3

What are the benefits of using object-oriented programming in Python? 

<details>
<summary>Possible Solution</summary>

1. As software becomes more complex, OOP helps manage this complexity.
2. It lets programmers create containers for data that can be changed and manipulated without affecting the entire program.
3. It lets programmers section off areas of code that perform specific procedures. This allows their programs to become the interaction of many small parts as opposed to a massive blob of dependencies.
4. We can talk about objects as nouns and their behaviors as verbs. These distinctions make it easier to conceptualize the structure of an OO program.
5. Creating classes and objects lets programmers think about code at a more abstract level.
6. It lets programmers write code that can be used with different kinds of data.
7. We can build applications faster as we can reuse pre-written code.
</details>

### Question 4

Suppose we have this code: 

```python
class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')
```

Without running the above code, what would each snippet do were you to run it?

```python
#Snippet 1
hello = Hello()
hello.hi()

#Snippet 2 
hello = Hello()
hello.bye()

#Snippet 3
hello = Hello()
hello.greet()

#Snippet 4 
hello = Hello()
hello.greet('Goodbye')

#Snippet 5
Hello.hi()
```

<details>
<summary>Answer:</summary>

```python

#Snippet 1:
Hello

#Snippet 2:
AttributeError: 'Hello' object has no attribute 'bye'
#since neither Hello nor Greeting define a bye method.

#Snippet 3:
TypeError: Greeting.greet() missing 1 required positional argument: 'message'
# raises a TypeError since hello.greet() is missing greet's argument.

#Snippet 4:
Goodbye

#Snippet 5:
TypeError: Hello.hi() missing 1 required positional argument: 'self'
# This raises a TypeError because hi is missing one positional argument, for the self parameter. This happens because we're invoking hi on the class Hello rather than an instance. When we invoke instance methods as class methods, no instance is passed in as self.

```
</details>

### Question 5

Modify the code from the previous question so that calling `Hello.hi()` on the class (rather than an instance) still uses Greeting's instance method `greet()` to print "Hi".

<details>
<summary>Answer:</summary>

```python
class Hello:
    def hi(self):
        self.greet('Hello')

    # Make sure you define the class method after the instance method. If you try it the other
    # way, the question below will prove a bit challenging.
    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('Hi')
```
</details>

### Question 6

Consider the following code:

```python
class Cat:
    def __init__(self, type):
        self.type = type

print(Cat('hairball')) # <__main__.Cat object at 0x10695eb10>
```

The output here isn't very useful. It only tells us that we've got an instance of the Cat class, and it's memory address. It would be better if the output were more meaningful. For instance, maybe it can print I am a hairball instead. Update the code to produce that result.

<details>
<summary>Answer:</summary>

```python

class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'I am a {self.type}'
```

</details>

### Question 7

What would happen if you ran the following code? Don't run it until you've checked your answer:

```python
class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model())
```

<details>
<summary>Possible Solution</summary>

```python
print(tv.manufacturer())          # Amazon
print(tv.model())                 # Omni Fire

print(Television.manufacturer())  # Amazon
print(Television.model())  # TypeError: Television.model() missing 1 required positional argument: 'self'
```
</details>

Page Reference: [Practice Problems: Easy 2](https://launchschool.com/lessons/a6479eb0/assignments/b5233047)
[Back to the top](#top)

***

## Practice Problems: Medium 1

### Question 1

Alyssa asked Ben to code review the following code:

```python
class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance
```

Ben glanced over the code quickly and said - "It looks fine, except that you're trying to access self.balance instead of self._balance in the balance_is_positive method."

"Not so fast," Alyssa replied. "What I'm doing here is valid; I can definitely use self.balance there!"

Who is correct, Ben or Alyssa? Why?

<details>
<summary>Answer:</summary>

Alyssa is correct. By defining a property named balance that returns the value of self._balance, Alyssa can write return self.balance > 0 with no trouble. Alyssa is correct because the balance method is decorated with @property. This decorator transforms the balance method into a "getter" for a property that is also named balance.

When self.balance is accessed within the balance_is_positive method, Python calls the balance getter method instead of looking for a balance instance variable. This method then returns the value of the self._balance instance variable.

Essentially, @property lets you access a method as if it were an attribute.

</details>

## Question 2
Alan created the following code to keep track of items for a shopping cart application he's writing:

```python
class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10000
```

<details>
<summary>Possible Solution</summary>

```python
class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10000
```
</details>


### Question 3
Let's practice creating an object hierarchy.

Create a class called Animal with a single instance method called speak that takes a string argument and prints that argument to the terminal.

Now create two other classes that inherit from Animal, one called Cat and one called Dog. The Cat class should have a meow instance method that takes no arguments and prints Meow!. The Dog class should have a bark instance method that says Woof! Woof! Woof! (dogs never bark just once). Make use of the Animal class's speak method when implementing the Cat and Dog classes. Don't invoke the print function in either of the subclasses.

<details>
<summary>Possible Solution</summary>

```python

class Animal():
    
    def speak(self, message):
        print(message)
    
class Dog(Animal):
    
    def bark(self):
        self.speak("Woof! Woof! Woof!")

class Cat(Animal):
    
    def meow(self):
        self.speak("Meow!")

cat = Cat()
dog = Dog()

cat.meow()
dog.bark()
```
</details>

### Question 4

You are given the following code:

```python
class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing
```

Write additional code for KrispyKreme such that the print invocations will work as shown above.

<details>
<summary>Answer:</summary>

```python
class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

   
    def __str__(self):
        if (self.filling is None) and (self.glazing is None):
            return 'Plain'
        elif self.filling is None:
            return f'Plain with {self.glazing}'
        elif self.glazing is None:
            return self.filling
        else:
            return f'{self.filling} with {self.glazing}'
        
donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing
```
</details>

### Question 5

How could you change the `light_status` method name below so that the method name is clearer and less repetitive?

```python
class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def light_status(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.light_status())
```

<details>
<summary>Answer:</summary>

No need for light_status, light can be deleted.

```python
class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def status(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.light_status())
```
</details>


Page Reference: [Practice Problems: Medium 1](https://launchschool.com/lessons/a6479eb0/assignments/62d927ad)
[Back to the top](#top)

***

## Practice Problems: Hard 1

### Question 1
Ben and Alyssa are working on a vehicle management system. So far, they have created classes called Auto and Motorcycle to represent automobiles and motorcycles. After having noticed common information and calculations they were performing for each vehicle type, they decided to break the common behaviors into a separate class called `WheeledVehicle`. This is what their code looks like so far:

```python
class WheeledVehicle:
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)
```

Now Syl has asked them to incorporate a new type of vehicle into their system: a Catamaran, defined as follows:

```python
class Catamaran:
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        # ... code omitted ...
```

This new class does not fit well with the object hierarchy defined so far. Catamarans don't have tires. But we still want a common code to track fuel efficiency and range. Modify the class definitions and move code into a mix-in, as necessary, to share code among the Catamaran and the wheeled vehicles.

<details>
<summary>Answer:</summary>

class FuelMixin:

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency
    
    def set_fuel_efficency(self, kilometers_per_liter):
        self.fuel_efficiency = kilometers_per_liter

    def set_fuel_capacity(self, liters):
        self.fuel_capacity = liters

class WheeledVehicle(FuelMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.set_fuel_efficency(kilometers_per_liter)
        self.set_fuel_capacity(liters_of_fuel_capacity)
       

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Catamaran(FuelMixin):
    def __init__(self,
                 number_propellers,
                 number_hulls,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.set_fuel_efficency(kilometers_per_liter)
        self.set_fuel_capacity(liters_of_fuel_capacity)

auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0
</details>

### Question 2

Building on the prior question, we now must also track a basic motorboat. A motorboat has a single propeller and hull, but otherwise behaves similar to a catamaran. Therefore, creators of Motorboat instances don't need to specify number of hulls or propellers. How would you modify the vehicles code to incorporate a new Motorboat class?

<details>
<summary>Answer</summary>

```python
class FuelMixin:

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency
    
    def set_fuel_efficiency(self, kilometers_per_liter):
        self.fuel_efficiency = kilometers_per_liter

    def set_fuel_capacity(self, liters):
        self.fuel_capacity = liters

class WheeledVehicle(FuelMixin):
    def __init__(self, tire_list,kilometers_per_liter,liters_of_fuel_capacity):
        self.tires = tire_list
        self.set_fuel_efficiency(kilometers_per_liter)
        self.set_fuel_capacity(liters_of_fuel_capacity)
       

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Watercraft(FuelMixin):
    def __init__(self,
                 number_propellers,
                 number_hulls,
                 fuel_efficiency,
                 fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.set_fuel_efficiency(fuel_efficiency)
        self.set_fuel_capacity(fuel_capacity)

class Catamaran(Watercraft):
    def __init__(self, number_propellers, number_hulls, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(number_propellers, number_hulls, kilometers_per_liter, liters_of_fuel_capacity)

class Motorboat(Watercraft):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter,liters_of_fuel_capacity)

auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0
```
</details>

### Question 3

The designers of the vehicle management system now want to make an adjustment for how the range of vehicles is calculated. For the seaborne vehicles, due to prevailing ocean currents, they want to add an additional 10km of range even if the vehicle is out of fuel.

Alter the code related to vehicles so that the range for autos and motorcycles is still calculated as before, but for catamarans and motorboats, the range method will return an additional 10km.

<details>
<summary>Answer:</summary>
</details>


Page Reference: [Practice Problems: Hard 1](https://launchschool.com/lessons/a6479eb0/assignments/639c8557)
[Back to the top](#top)

<details>
<summary>Possible Solution</summary>

```python
class FuelMixin:

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency
    
    def set_fuel_efficiency(self, kilometers_per_liter):
        self.fuel_efficiency = kilometers_per_liter

    def set_fuel_capacity(self, liters):
        self.fuel_capacity = liters

class WheeledVehicle(FuelMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.set_fuel_efficiency(kilometers_per_liter)
        self.set_fuel_capacity(liters_of_fuel_capacity)
       

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Watercraft(FuelMixin):
    def __init__(self, number_propellers, number_hulls, fuel_efficiency,fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.set_fuel_efficiency(fuel_efficiency)
        self.set_fuel_capacity(fuel_capacity)

    def range(self):
        return super().range() + 10

class Catamaran(Watercraft):
    def __init__(self, number_propellers, number_hulls, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(number_propellers, number_hulls, kilometers_per_liter, liters_of_fuel_capacity)

class Motorboat(Watercraft):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter,liters_of_fuel_capacity)

auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0
```
</details>