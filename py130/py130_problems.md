# PY130 Practice Problems

A collection of all the practice problems from the PY130 course in one place.

## [Higher-Order Functions](https://launchschool.com/lessons/807cf3b3/assignments/9d6720a1)


### Question 1

Write a select function that mimics the built-in filter function. Your select function should take two arguments: a callback function and an iterable object. It should return a list of all the elements of the iterable for which the callback function returns a truthy value. It should not include any elements for which the callback returns a falsy value.

Start by writing a function that doesn't use any comprehensions. Once your code works, refactor it to use a comprehension.

You can use the following examples to test your code:

```python

numbers = [1, 2, 3, 4, 5]
colors = {'red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet'}

odd_numbers = select(lambda number: number % 2 != 0, numbers)
print(odd_numbers)            # [1, 3, 5]

large_numbers = select(lambda number: number >= 10, numbers)
print(large_numbers)          # []

small_numbers = select(lambda number: number < 10, numbers)
print(small_numbers)          # [1, 2, 3, 4, 5]

short_color_names = select(lambda color: len(color) <= 5, colors)
print(short_color_names)      # ['blue', 'red', 'green']
# The order of the colors may vary, but should include the
# indicated colors.
```

<details> 
<summary>Possible Solution</summary> 

Without Comprehension:

```python
def select(callable, iterable):
    
    result = []
    for item in iterable:
        if callable(item):
            result.append(item)
    return result
```

With Comprehension:

```python

def select(callable, iterable):
    
    return [item for item in iterable if callable(item)]
```

</details>

### Question 2

Write a reject function that mimics the select function you just wrote, but that rejects rather than selects elements from the iterable object. That is, it should return a list of all the elements of the iterable for which the callback function doesn't return a truthy value. It should only include any elements for which the callback returns a falsy value.

You may use comprehensions if you wish.

You can use the following examples to test your code:

```python
numbers = [1, 2, 3, 4, 5]
colors = {'red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet'}

even_numbers = reject(lambda number: number % 2 != 0, numbers)
print(even_numbers)            # [2, 4]

small_numbers = reject(lambda number: number >= 10, numbers)
print(small_numbers)          # [1, 2, 3, 4, 5]

large_numbers = reject(lambda number: number < 10, numbers)
print(large_numbers)          # []

long_color_names = reject(lambda color: len(color) <= 5, colors)
print(long_color_names)
# ['yellow', 'violet', 'orange', 'indigo']
# The order of the colors may vary, but should include the
# indicated colors.
```


<details> 
<summary>Possible Solution</summary> 

Without Comprehension:

```python
def reject(callable, iterable):
    
    result = []
    for item in iterable:
        if not callable(item):
            result.append(item)
    return result
```

With comprehension:

```python

def reject(callable, iterable):

    return [item for item in iterable if not callable(item)]
```

</details>

### Question 3 (Challenging)

A function that often appears in languages that have map and filter functions is called the `reduce` function, or, sometimes, `inject`. Python has one tucked away in the functools module, but we won't be using it in this challenge.

The reduce function reduces the elements in an iterable object to a single value. For instance, reduce can return the sum of all numbers in a list or concatenate the strings in a tuple to form a single long string. It's a bit like map, but instead of returning a new collection, it just returns a single value.

`reduce` functions typically take 3 arguments:

* a callback that takes two arguments. The first argument is the current element of the iterable argument and the second is the current reduction value, commonly called the "accumulator" and named accum.
* an iterable.
* a starting value. The starting value is the initial value for the current argument in the callback.

For instance, consider the following reduce invocation:

```python
numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))     # 300

numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV

```

<details> 
<summary>Possible Solution</summary> 

```python

def reduce(callable, iterable, starting_value):

    accum = starting_value
    for item in iterable:
        accum = callable(item, accum)
    return accum
```

</details>

### Question 4

Use the reduce function shown in the answer to the previous question to compute the sum of the squares in a list of numbers.

<details> 
<summary>Possible Solution</summary> 

```python

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda number, accum: number**2 + accum, numbers, 0)
print(total) #55

```

</details>

## [Generators](https://launchschool.com/lessons/807cf3b3/assignments/6fe63cab)


### Question 1

Create a generator expression that generates the reciprocals of the numbers from 1 to 10. A reciprocal of a number n is 1 / n. Use a for loop to print each value.


<details> 
<summary>Possible Solution</summary> 

```python
reciprocals = (1 / x for x in range(1, 11))

for value in reciprocals:
    print(value)
```
</details>

### Question 2

Create a generator function that generates the reciprocals of the numbers from 1 to n, where n is an argument to the function. Use a for loop to print each value.

<details> 
<summary>Possible Solution</summary> 

```python
def reciprocals(n):
    for i in range(1, n+1):
        yield 1 / i
    
for recip in reciprocals(10):
    print(recip)
```

</details>

### Question 3
Use a generator expression to capitalize every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.

<details> 
<summary>Possible Solution</summary> 

```python
strings = ["hello", "world"]

all_caps = (string.capitalize() for string in strings)
print(tuple(all_caps))
```
</details>

### Question 4

Create a generator function that generates the capitalized version of every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.

<details> 
<summary>Possible Solution</summary> 

```python
strings = ['hello', 'world']

def all_caps(listie):
    for element in listie:
        yield element.capitalize()

print(tuple(all_caps(strings)))
```

</details>

### Question 5

Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. Use a single print invocation to print all the capitalized strings as a set.

<details> 
<summary>Possible Solution</summary> 

```python
strings = ['hello', 'world', '!']

all_caps = (string.capitalize() for string in strings if len(string) >= 5)
print(set(all_caps))
```

</details>

### Question 6

Create a generator function that generates the capitalized version of every string in a list of strings whose length is less than 5. Use a single print invocation to print all the capitalized strings as a set.

<details> 
<summary>Possible Solution</summary> 

```python
strings = ['hello', 'world', '!']

def all_caps(listie):
    for element in listie:
        if len(element) < 5:
            yield element.capitalize()

print(set(all_caps(strings)))
```

</details>

## [Arguments and Parameters](https://launchschool.com/lessons/ab8b995d/assignments/6e94e908)


### Problem 1

Write a function named combine that takes three positional arguments and returns a tuple containing all three. Call this function with three different values.


<details> 
<summary>Possible Solution</summary> 

```python
def combine(first, second, third):

    first = "uno"
    second = "dos"
    third = "tres"

    return (first, second, third)

print(combine("one", "two", "three"))
```

</details>

### Problem 2

Define a function named `multiply` that accepts two positional-only arguments and returns their product. The function should not allow these parameters to be passed as keyword arguments.


<details> 
<summary>Possible Solution</summary> 

```python
def multiply(int_1, int_2, /):
    return int_1 * int_2

print(multiply(3, 5)) #15
multiply(int_1=3, int_2=5) #TypeError
```

</details>

### Problem 3

Create a function named `describe_pet` that takes one positional argument animal_type and one keyword argument name with a default value of an empty string. The function should print a description of the pet. The function should not accept more than 1 positional argument.

<details> 
<summary>Possible Solution</summary> 

```python
def describe_pet(animal_type, *, description="Cutie Patootie"):
    return f"This {animal_type} is a {description}."

print(describe_pet("dog", description="blood-hound"))
print(describe_pet("cat", description="purebred"))
print(describe_pet("bunny"))
```

</details>

### Problem 4

Write a function named `calculate_average` that accepts any number of numeric arguments and returns their average. Make sure it returns None if no arguments are provided.

<details> 
<summary>Possible Solution</summary> 

```python
def calculate_average(*args):

    return sum(args)/len(args) if args else None
```
</details>

### Problem 5

Create a function named `find_person` that accepts any number of keyword arguments in which each key is someone's name and the value is their associated profession. The function should check whether any of the key/value pairs has a key of "Antonina" and then, if the key is found, print a message that shows Antonina's profession. Otherwise, it should say "Antonina not found". The function should not accept any positional arguments.

<details> 
<summary>Possible Solution</summary> 

```python

    if "Antonina" in kwargs:
        print(f"Antonina's Profession is {kwargs['Antonina']}")
    else:
        print("Antonina not found")

find_person(Wonnie="Engineer", Antonina="Software Engineer")
# Antonina's profession is Software Engineer

find_person(Sebastian="Engineer", James="Software Engineer")
# Antonina not found
```

</details>

### Problem 6

Define a function named `concat_strings` that takes any number of strings and returns the concatenation of all the strings. Add a keyword-only argument sep with a default value of ' ' that specifies the separator to use between the strings.

<details> 
<summary>Possible Solution</summary> 

```python
def concat_strings(*args, sep=" "):

    return sep.join(args)
    
print(concat_strings("Hello, World", "Hello, world?", "World, Hello"))
```

</details>

### Problem 7

Create a function named `register` that takes exactly three arguments: `username` as positional-only, `password` as keyword-only, and `age` as either a positional or keyword argument. It should return a dictionary that includes username, password, and age keys with the values passed to the the function.

<details> 
<summary>Possible Solution</summary> 

```python
def register(username, /, age, *, password):
    return {'username': username, "age": age, "password": password}

print(register('user1', 30, password='pass123'))
print(register('user2', age=45, password='pass132'))
```

</details>

### Problem 8

Create a function named `print_message` that requires a keyword-only argument (message) and an optional keyword-only argument (level) with a default value of "INFO". The function should print out the message prefixed with the level. The function shouldn't accept any positional arguments.

<details> 
<summary>Possible Solution</summary> 


</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>