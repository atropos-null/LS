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

Page Reference: [Practice Problems: Easy 2](https://launchschool.com/lessons/a6479eb0/assignments/b5233047)
[Back to the top](#top)

***

## Practice Problems: Medium 1

Page Reference: [Practice Problems: Medium 1](https://launchschool.com/lessons/a6479eb0/assignments/62d927ad)
[Back to the top](#top)

***

## Practice Problems: Hard 1

Page Reference: [Practice Problems: Hard 1](https://launchschool.com/lessons/a6479eb0/assignments/639c8557)
[Back to the top](#top)

<details>
<summary>Possible Solution</summary>
</details>