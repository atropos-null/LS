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

## 

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>
