# PY119 Study Guide

<a name="top"></a>

## Table of Contents

- [String Methods](#string-methods)
- [List Methods](#list-methods)
- [Dictionary Methods](#dictionary-methods)
- [Set Methods](#set-methods)
- [Frozenset Methods](#frozenset-methods)
- [Tuple Methods](#tuple-methods)
- [Range and Enumerate](#range-and-enumerate)
- [Sum and All](#sum-and-all)
- [Conditional Statements and Control Flow](#conditional-statements-and-control-flow)
- [Sorting](#sorting)
- [Comprehensions](#comprehensions)
- [Nested Data Structures and Iteration](#nested-data-structurse-and-iteration)
- [Shallow and Deep Copy](#shallow-and-deep-copy)
- [User-level Synergy](#user-level-synergy)
- [Further practice](#further-practice)

Page Reference: [Study Guide](https://launchschool.com/lessons/5638850f/assignments/e420c96a)

***

## String Methods

> str methods: index, find, split, strip, join, replace, upper, lower, capitalize

Python offers several methods for changing string case:

* `str.upper()`: Converts all characters in the string to uppercase.
* `str.lower()`: Converts all characters in the string to lowercase.
* `str.casefold()`: Provides an internationalized version of `lower()`, designed for case-insensitive comparisons, especially with Unicode characters that have complex case variations.
* `str.capitalize()`: Capitalizes the first character of the string and converts the rest to lowercase.
* `str.swapcase()`: Inverts the case of each character in the string. It's also internationalized. Note that applying `swapcase()` twice may not always return the original string due to certain Unicode characteristics.

### Explain the difference between the `str.join()` and `str.split()` methods.

`str.join()` and `str.split()` are inverse operations for manipulating sequences of strings:

* `str.join(iterable)`:  
  Concatenates (joins) strings from an iterable (like a list or tuple) into a single string. The string the method is called on acts as the separator between the elements. All elements in the iterable must be strings; otherwise, a `TypeError` is raised.

* `str.split(sep=None, maxsplit=-1)`:  
  Breaks a string into a list of substrings based on a specified separator `sep`. If `sep` is not provided, it splits at any sequence of whitespace. An optional `maxsplit` argument limits the number of splits performed. Splitting with an empty string as the separator raises a `ValueError`.

### Explain the difference between `str.index()` and `str.find()`.

Both methods search for a substring within a string and return the index where it first appears, but they handle missing substrings differently:

* ​`str.index()`​: Returns the index of the first occurrence. Raises a `ValueError` if the substring isn't found.
* `​str.find()`​: Returns the index of the first occurrence. Returns `-1` if the substring isn't found.

```python
sentence = "Hello, world!"
position = sentence.index("world")  # 7
position = sentence.find("world")   # 7

sentence.index("school")  # ValueError: substring not found
sentence.find("school")   # -1
```

Both methods accept optional start and end parameters to limit the search range:

```python
sentence = "Hello World"
position = sentence.index("l", 6)     # 9 (starts search at index 6)
position = sentence.find("l", 3, 7)  # 3 (searches from index 3 to 7)
```

### How can you remove leading and trailing whitespace (or specific characters) from a string?

Python provides convenient methods for removing whitespace or specific characters from the ends of a string:

* `str.strip([chars])`: Removes leading and trailing whitespace characters by default. If an optional string `chars` is provided, it removes any combination of characters specified in `chars` from both the beginning and end of the string.

* `str.lstrip([chars])`: Removes leading whitespace characters by default. If `chars` is provided, it removes characters from the left (beginning) of the string.

* `str.rstrip([chars])`: Removes trailing whitespace characters by default. If `chars` is provided, it removes characters from the right (end) of the string.

### What about `str.replace()`?

`str.replace()` doesn't modify the original string (strings are immutable in Python)
* ​Case-sensitive​: The method performs exact matches
* ​If substring not found​: Returns the original string unchanged
* ​Empty string replacement​: You can replace substrings with empty strings to effectively remove them.

Syntax: `str.replace(old, new, count)`
* `​old`​: The substring you want to replace
* `​new`​: The substring you want to replace it with
* `​count`​: Optional parameter that determines how many instances to replace


[Back to the top](#top)
***

## List Methods

> list methods : append, extend, insert, remove, pop, clear, index, count, sort, reverse.

Lists are flexibile due to their mutability and introduces several built-in methods for manipulating list content:

* `list.count(object)`: Counts the number of occurrences of a specific object within the list. Returns `0` if the object is not present.  
  **Example:**  
  ```python
  nums = [1, 2, 2, 3, 3, 3]
  nums.count(3)  # 3
  ```

* `list.index(object, start=0, end=len(list))`: Returns the index of the first occurrence of a specified object. Can search within a specified range using `start` and `end` arguments. Raises a `ValueError` if the object is not found.  
  **Example:**  
  ```python
  fruits = ['apple', 'orange', 'banana', 'apple', 'grape']
  fruits.index('apple')  # 0
  ```

* `list.append(object)`: Adds an object to the end of the list.  
  **Example:**  
  ```python
  numbers = [1, 2, 3]
  numbers.append(4)
  numbers  # [1, 2, 3, 4]
  ```

* `list.insert(index, object)`: Inserts an object prior to a specific index position.  
  **Example:**  
  ```python
  numbers = [1, 2, 3, 4]
  numbers.insert(2, 'two-point-five')
  numbers  # [1, 2, 'two-point-five', 3, 4]
  ```

In the above example, the insert call inserts the string `'two-point-five'` between index positions 1 and 2 in the list.

* `list.extend(iterable)`: Appends all elements from an iterable (like another list, tuple, or set) to the end of the current list.  
  **Example:**  
  ```python
  numbers = [1, 2, 3]
  numbers.extend([4, 5, 6, 7])
  numbers  # [1, 2, 3, 4, 5, 6, 7]
  ```

Keep in mind that sets are unordered, so objects added from a set may not be in the expected order.

* `list.remove(value)`: Removes the first occurrence of a specified value from the list. Raises a `ValueError` if the element is not found.  
  **Example:**  
  ```python
  numbers = [1, 2, 'two-point-five', 3, 4]
  numbers.remove('two-point-five')
  numbers  # [1, 2, 3, 4]
  ```

If the element we are trying to remove doesn't exist in the list, `list.remove` raises a `ValueError`.

* `list.pop(index=-1)`: Removes and returns the object at a specific index. If no index is specified, it removes and returns the last item. Raises an `IndexError` if the list is empty or the index is out of range.  
  **Example:**  
  ```python
  numbers = [1, 2, 'two-point-five', 3, 4]
  numbers.pop(2)  #'two-point-five'
  ```

Similarly, if the list is empty, `list.pop` will raise an `IndexError`.

* `list.reverse()`: Reverses the order of the list's elements in-place.  
  **Example:**  
  ```python
  numbers = [1, 2, 3, 4, 5, 6]
  numbers.reverse()
  numbers  # [6, 5, 4, 3, 2, 1]
  ```

* `list.sort(key=None, reverse=False)`: Sorts the list's elements in-place. Can sort various data types as long as elements can be compared. Raises a `TypeError` if elements cannot be compared. The `key` argument can be used for customized sorting (e.g., case-insensitive using `str.casefold` or sorting numeric strings using `int`). The `reverse=True` argument sorts in descending order.  
  **Example:**  
  ```python
  numbers = [61, 103, 525, 10100, 25, 3]
  numbers.sort()
  numbers  # [3, 25, 61, 103, 525, 10100]
  ```

  **Example with key:**  
  ```python
  animals = ['Cat', 'aarDVARK', 'HORSE', 'Python', 'orangutan']
  animals.sort(key=str.casefold)
  animals  # ['aarDVARK', 'Cat', 'HORSE', 'orangutan', 'Python']
  ```

### Adding Elements to a Python List

1. `.append(item)`: Adds a single item to the end of the list.
2. `.insert(index, item)`: Inserts an item at a specified index.
3. `.extend(iterable)`: Adds all items from another iterable (list, tuple, set, etc.) to the end of the list.
   * Note: Adding from an unordered iterable like a set may result in unpredictable order.

---

### Removing Elements from a Python List

* `.remove(value)`: Removes the first occurrence of the specified value. Raises a `ValueError` if not found.
* `.pop(index)`: Removes and returns the item at the given index. If no index is provided, removes and returns the last item. Raises an `IndexError` if the list is empty.

### Sorting a Python List

* Use the `.sort()` method to sort a list in-place (ascending order by default).
  * **Comparable Elements**: List must contain elements that can be compared (e.g., all numbers or all strings).
  * **TypeError**: Raised if the list contains incompatible types.
  * **Reverse Order**: Use `reverse=True`.
  * **Custom Criteria**: Use the `key` argument (e.g., `key=str.casefold` for case-insensitive sort, `key=int` for numeric string sort).


[Back to the top](#top)
***

## Dictionary Methods

> dict methods : keys, values, items, get, setdefault, update, pop, popitem, clear.

**Primary Characteristics:**
* Dictionaries are a collection data type that stores data as **key-value pairs**.
* **Values** can be of any data type, while **keys** must be **hashable** and **unique**.
* Values are accessed using their corresponding keys (not numerical indices).
* **Mutable**: Dictionaries can be changed after creation (items can be added, removed, or updated).

### Methods of creating a dictionary

1. Using Curly Braces (Dictionary Literal). Standard!
```python
# Dictionary with initial key-value pairs
empty_dict = {}  # Empty dictionary

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
}
```

2.  Using the `dict()` Constructor
```python
# Empty dictionary
empty_dict = dict()

# From keyword arguments
person = dict(name='Alice', age=25, city='Portland')

# From a sequence of key-value pairs (tuples)
items = [('type', 'sedan'), ('color', 'blue'), ('mileage', 80_000)]
car = dict(items)
```

`dict()` requires the following to work:

* An iterable of key-value pairs like `[('key1', 'value1'), ('key2', 'value2')]`
* Keyword arguments like `dict(key1='value1', key2='value2')`


### Checking for Key Existence and Accessing Keys

* **Check if a key exists:**  
  Use `key in dict` or `key not in dict`.
* **Accessing a non-existent key:**  
  Raises a `KeyError`.

* `dict.keys()`: returns a `dict_keys` object containing all the keys in the dictionary, not a list. It is dynamic however, and will update if the dictionary changes. Can be converted to a list using `list(car.keys())`. Useful for iterating through all keys in a dictionary.

```python

car = {
    'type': 'sedan',
    'color': 'blue',
    'year': 2003,
}

keys = car.keys()  # dict_keys(['type', 'color', 'year'])
```

**`dict.values()`**: returns a dict_values object containing all the values in the dictionary, and is likewise dynamic like `dict.keys()`. 
`values = car.values()  # dict_values(['sedan', 'blue', 2003])`

Can include duplicate values (unlike keys, which must be unique) and useful when you need to work with all values without their associated keys. 

```python
grades = {'Math': 95, 'Science': 88, 'History': 92}

# Calculate average without needing the subject names
average = sum(grades.values()) / len(grades)
print(f"Average grade: {average}")  # Average grade: 91.67

# Check if a specific value exists
if 88 in grades.values():
    print("Someone got an 88!")
```

**`dict.items()`**: returns a dict_items object containing all key-value pairs as tuples, and is especially useful for iteration, especially over both keys and values.

```python

items = car.items()  # dict_items([('type', 'sedan'), ('color', 'blue'), ('year', 2003)])

# Printing each key-value pair
for key, value in car.items():
    print(f"The car's {key} is {value}.")

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(f"A {key} number is {value}.")

```

```python
def new_dictionary(old_dictionary):   #creating a new dictionary from an old dictionary
    
    new_dict = {} 
    for key, values in old_dictionary.items() :
        new_dict[key] = values
    return new_dict

```

### `get()` vs `setdefault()` Methods

* **`get()`**:  
  * Retrieves the value for a given key.
  * Returns `None` (or a specified default value) if the key is not found.
  * Does **not** modify the dictionary.

* **`setdefault()`**:  
  * Also retrieves the value for a given key.
  * If the key exists, returns its value (no change).
  * If the key does **not** exist, adds the key with a specified default value and returns it.
  * **Modifies** the dictionary if the key is missing.

#### Modifying Dictionaries

1. **Adding or Updating Key-Value Pairs**: The simplest way to modify a dictionary is by assigning a value to a key. If the key doesn't exist, Python adds a new key-value pair; if it does exist, Python updates the value.
```python

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
}

# Adding a new key-value pair
car['year'] = 2003

# Updating an existing value
car['color'] = 'red'

print(car)  # {'type': 'sedan', 'color': 'red', 'mileage': 80_000, 'year': 2003}

#Adding a list as a dictionary value:

dictionary_name[key].append(value to be appended)

```

2. **Using the `update()` method:** lets you add or update multiple key-value pairs at once
```python

car = {
    'type': 'sedan',
    'color': 'blue',
}

# Adding/updating multiple key-value pairs
car.update({'year': 2003, 'mileage': 80_000, 'color': 'green'})

print(car)  # {'type': 'sedan', 'color': 'green', 'year': 2003, 'mileage': 80_000}
```

### Removing from dictionaries

1.  The `del` Statement directly removes a key-value pair from a dictionary, mutating the dictionary object. It raises a `KeyError` if a key doesn't exist. No value is returned.

```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
    'year': 2003,
}

del car['mileage']
print(car)  # {'type': 'sedan', 'color': 'blue', 'year': 2003}
```

2. **The `pop()` method** removes a key-value pair and returns the value associated with the removed key. It will accept a default value as a second argument to return if the key doesn't exist, however if a key nor a default does not exist, it will raise a `KeyError`. This is a useful method when you know what you are removing.
```python

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
    'year': 2003,
}

mileage = car.pop('mileage')  # mileage = 80_000
print(car)  # {'type': 'sedan', 'color': 'blue', 'year': 2003}

#Example with a default value.
model = car.pop('model', 'not specified')  # model = 'not specified'
```

3. **The `popitem()` method**: removes and returns a key-value pair from the dictionary. This creates a way to process items one by one while simultaneously removing them from the dictionary. It's "destructive" because it permanently modifies the dictionary by removing items as you iterate.

This approach is useful when:

* You need to process each item exactly once
* You want to ensure items are removed as you go (to free memory or prevent duplicate processing)
* You don't need to preserve the original dictionary

```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'year': 2003,
}

last_pair = car.popitem()  # last_pair = ('year', 2003)
print(car)  # {'type': 'sedan', 'color': 'blue'}
```

4. **The `clear()` method**: removes all items from a dictionary, resulting in an empty dictionary. Mutates the original dictionary object and does not return any values.
```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'year': 2003,
}

car.clear()
print(car)  # {}
```

### Merging Dictionaries

* **`update()` method**:  
  Merges key-value pairs from one dictionary into another; overwrites values for matching keys.

* **Merge Operators (Python 3.9+)**:
  * `|` creates a new merged dictionary: `merged = dict1 | dict2`
  * `|=` merges in place (like `update()`): `dict1 |= dict2`

[Back to the top](#top)
***

## Set Methods

> set methods: add, update, remove, clear, union, intersection, difference, issubset, issuperset, isdisjoint

**Key Features:**
* **Unordered** collection of **unique** objects.
* **No Duplicates**: Designed for efficient membership tests and set operations (union, intersection, difference).
* **Mutable**: Can add or remove elements.
* **Unordered**: No guarantee of item order.
* **Contain Hashable Elements only**: No Lists, Dictionaries or Subsets!!

**Subset/Superset Operations:**
* `<=` or `issubset()`: Check if one set is a subset of another.
* `>=` or `issuperset()`: Check if one set is a superset of another.
* `<` and `>`: Check for proper subset/superset (not equal).

**Set Operations:**
* `union()` or `|`: Combine elements from two sets (all unique elements, original sets unchanged).  
```python
fruits1.union(fruits2)
# or
fruits1 | fruits2
```

* `intersection()` or `&`: Common elements between two sets (original sets unchanged).  
```python
fruits1.intersection(fruits2)
# or
fruits1 & fruits2
```

* `difference()` or `-`: Elements in the first set but not the second (original sets unchanged).  
```python
fruits1.difference(fruits2)
# or
fruits1 - fruits2
```

* **Disjoint Sets:**  `isdisjoint()` checks if sets have no common elements.  
```python
fruits1.isdisjoint(fruits2)
```

* **Copying:**   The `copy()` method creates a new distinct set.  
```python
fruits_copy = fruits1.copy()
```

**Adding and Removing Members (sets are mutable):**
* `add()`: Adds a single new member (no effect if already present).  
```python
fruits.add('cherry')
```

* `remove()`: Removes a specified element (raises `KeyError` if not found).  
```python
fruits.remove('cherry')
```

* `discard()`: Removes a specified element (no error if not found).  
```python
fruits.discard('orange')
```
> "If you don't care whether the element is in the set, you can use discard instead."

* `clear()`: Removes all elements, leaving an empty set.  
```python
fruits.clear()
```

* `pop()`: Removes and returns an arbitrary element (raises `KeyError` if empty).  
```python
fruits.pop()
```

**Conversion:**   

Sequences and collections can be converted to sets using `set()`. Order is not maintained. Converting a dictionary to a set results in a set of its keys.  
```python
set('apple')
set(['apple', 'banana'])
set({'name': 'Srdjan', 'city': 'Belgrade'})
```

Checking for duplicates: If you want to check for unique characters in an item, in this case an integer, put it through set and compare it to the length of the original. If it is the same length then they are all unique.

```python
 if len(set(str(num))) == len(str(num)):
    return num
```

[Back to the top](#top)
***

## Frozenset Methods

>frozenset methods: union, intersection, difference, issubset, issuperset, isdisjoint

* **Immutable Sets:**  Frozen sets are immutable versions of sets.  
* **No Modification After Creation:**  Once created, a frozen set cannot be modified (`add`, `remove`, `discard`, `pop`, `clear` are unavailable).
* **Use Non-Mutating Methods:** Any non-mutating set method or operator can be used with frozen sets.
* **Hashable Objects:** Useful when set-like behavior is needed for hashable objects (e.g., as dictionary keys).

Allowed Operations: Because they are immutable, frozen sets can utilize any non-mutating method or operator available for regular sets. This includes operations like:

* Checking for element existence (`value in s`, `value not in s`).
* Subset and superset checks (`issubset(`), `<=`, `<`, `issuperset()`, `>=`, `>`).
* Set operations such as union (`union()` or `|`), intersection (`intersection()` or `&`), and difference (`difference()` or `-`). It's important to note that these operations, when applied to frozen sets, also do not mutate the original frozen sets involved.
* Disjoint checks (`isdisjoint()`).
* Copying (`copy()`), although a copy of an immutable object might seem redundant in some contexts, it's a valid operation.

Disallowed Operations: Conversely, frozen sets cannot use mutating methods that alter their content. These include:
* `add()`
* `remove()`
* `discard()`
* `pop()`
* `clear()`

[Back to the top](#top)
***

## Tuple Methods

> tuple methods: count, index, unpacking

Tuples are immutable, which means their content cannot be changed after creation:

* **Tuple Unpacking:**  A concise way to assign values from a tuple to multiple variables simultaneously. The number of variables must match the number of elements in the tuple.

**Example:**  
```python
shades = ('crimson', 'emerald', 'azure')
r, g, b = shades
```

The beauty of tuple unpacking lies in its simplicity and readability. While other iterables can be unpacked, tuples are ideal because they often have a predictable number of elements.

* `tuple.count(object)`: Identical to `list.count`, counts occurrences of an object in a tuple.  

**Example:**  
```python
nums = (1, 2, 2, 3, 3, 3)
nums.count(3)  # 3
```

* `tuple.index(object, start=0, end=len(tuple))`: Identical to `list.index`, returns the index of the first occurrence of an object in a tuple. Raises a `ValueError` if the object is not found.  

**Example:**  
```python
fruits = ('apple', 'orange', 'banana', 'apple', 'grape')
fruits.index('apple')  # 0
```

[Back to the top](#top)
***

## Range and Enumerate

> range and enumerate - Understanding of how to create and use range objects and enumerate for indexing during iteration.

### What is a Python range object and how does it work?

A **Python range object** is a special type of iterable sequence of numbers generated by the `range()` function. Unlike traditional collections that store all their elements in memory at once, a range object generates numbers "upon request" during iteration. 

### How can you generate sequences of numbers using the `range()` function?

The `range()` function is versatile and accepts one, two, or three arguments:

* `range(end)`: Generates numbers from `0` up to, but not including, `end`.  
_Example:_ `list(range(3))` results in `[0, 1, 2]`

* `range(start, end)`: Generates numbers from `start` up to, but not including, `end`.  
_Example:_ `list(range(1, 3))` results in `[1, 2]`

* `range(start, end, step)`: Generates numbers from `start`, incremented by `step`, up to, but not including, `end`.  
_Example:_ `list(range(1, 6, 2))` results in `[1, 3, 5]`

* A negative `step` value makes the range decrement:  
_Example:_ `list(range(6, 1, -1))` results in `[6, 5, 4, 3, 2]`

### How can you iterate over a range object and also track the index of each element?

The standard way to iterate over a range object is using a `for` loop. To simultaneously track both the element and its position (index) in the sequence, you can use the `enumerate()` function.  `enumerate()` takes an iterable (like a range) and returns a new iterable of tuples, where each tuple contains an index number and the original element. Tuple unpacking is commonly used with `enumerate()` to assign the index and element to separate variables within the loop.

**Range Attributes and Methods:**
* `range.count(value)`: Returns how many times a specific value appears in the range (always 0 or 1).
* `range.index(value)`: Returns the index within the range of the given value. Raises `ValueError` if the value is not in the range.
* `range.start`, `range.stop`, `range.step`: Attributes containing the values used during range creation.


[Back to the top](#top)
***

## Sum and All

>The built-in functions sum and all.

### `sum()` Function

The sum function computes and returns the sum of all numeric values in an iterable collection (like lists, tuples, sets, etc.).

```python
#Basic Usage:
numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
print(sum(numbers))  # 88

my_list = [10, 20, 30]
print(sum(my_list))  # 60

```

Optional Second Parameter:

`sum()` accepts an optional second parameter that serves as a starting value:

```python
numbers = [1, 2, 3]
print(sum(numbers))      # 6
print(sum(numbers, 10))  # 16 (starts with 10, then adds 1+2+3)
```

### `all()` Function

The `all()` function returns `True` if ​all​ elements in an iterable are truthy, and `False` otherwise.

```python
#Basic Usage:
collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(all(collection1))  # False
print(all(collection2))  # False
print(all(collection3))  # True
print(all([]))  # True
```

Key Behaviors:
* Returns `True` if every element is truthy
* Returns `False` if any element is falsy
* Returns `True` for an empty collection (since no elements are falsy)


#### Practical Applications

Both functions are commonly used with list comprehensions to test conditions:
```python
# Check if all numbers in a list are even
numbers = [2, 4, 6, 8]
print(all([number % 2 == 0 for number in numbers]))  # True
```

Sum only the even numbers
```python
numbers = [1, 2, 3, 4, 5, 6]
print(sum([num for num in numbers if num % 2 == 0]))  # 12
```

Check if all strings are longer than 3 characters
```python
words = ['hello', 'world', 'python']
print(all([len(word) > 3 for word in words]))  # True
```

[Back to the top](#top)
***

## Conditional Statements and Control Flow

> Conditional statements (if, elif, else) / Iteration using for loops, break, continue

### Conditional Statements

Python uses `if`, `elif`, and `else` to control program flow based on conditions. 

Key Points:
* Every conditional block must start with `if`
* Use `elif` (not "else if") for additional conditions
* `else` is optional and runs when all previous conditions are False
* Python evaluates conditions in order and stops at the first `True` condition
* You can have as many `elif` blocks as needed

Python evaluates every object as either ​truthy​ or ​falsy​ in conditional contexts. You don't need explicit Boolean values.

Falsy values:
* `False`, `None`
* All numeric `0` values (integers, floats, complex)
* Empty strings: `''`
* Empty collections: `[]`, `()`, `{}`, `set()`, `frozenset()`, `range(0)`

Everything else is truthy.

### Iteration Control

`for` Loops with Different Iterables

Python's for loops work with any iterable object:
```python
# Lists
names = ['Chris', 'Max', 'Karis', 'Victor']
for name in names:
    print(name)

# Strings
for char in 'hello':
    print(char)

# Dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterate over keys
for key in my_dict:
    print(key)

# Iterate over values
for value in my_dict.values():
    print(value)

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(f'{key} = {value}')
```

### break - Early Loop Termination

Use `break` to exit a loop completely when a condition is met:

```python
numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break  # Exit loop immediately

    index += 1

print(found_item)  # 2
```

Key points:
* `break` terminates the nearest enclosing loop
* Code after `break` in the same iteration is not executed
* Execution continues after the loop

### `continue` - Skip Current Iteration

Use continue to skip the rest of the current iteration and move to the next:

```python
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue  # Skip this iteration

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)  # ['CHRIS', 'KARIS', 'VICTOR']

#Alternative without continue:
for name in names:
    if name != 'Max':
        upper_name = name.upper()
        upper_names.append(upper_name)
```

[Back to the top](#top)
***

## Sorting

> Sorting lists using the sorted function and list.sort method. Custom sorting using the key parameter and reverse sorting using the reverse parameter.

### What is sorting in Python and why is it important for collections?

Sorting in Python refers to arranging the items within a collection, such as a list, into a predictable sequence or order based on specific criteria. It's crucial for collections, especially lists, because elements are accessed by their index, making their order significant. While lists are commonly sorted, strings can be sorted by converting them to a list of characters, sorting, and then rejoining. Dictionaries, while not directly sortable in the traditional sense, can have their contents extracted (e.g., keys or values) and then processed or displayed in a sorted manner. Python 3.7 and later versions maintain dictionary key insertion order, which is a form of inherent ordering.

Python provides two main built-in tools for sorting: the `sorted()` function and the `list.sort()` method.

* **`sorted()` function**: This function takes an iterable (like a list, string, or tuple) as an argument and returns a new sorted list, leaving the original collection unchanged.
* **`list.sort()` method**: This method is specifically for lists. It sorts the list in-place, meaning it modifies the original list directly and returns `None`. One can call `list.sort()` multiple times to massage the list. 

**Key difference:**  
`sorted()` creates a new sorted list, while `list.sort()` modifies the existing list.


### How does Python determine the order when sorting strings and characters, especially with mixed cases or special symbols?

Python determines the order of characters and strings based on their Unicode code points. The `ord()` function can be used to reveal the numeric Unicode value of a character. When sorting:

* **Case Sensitivity:** Uppercase letters have lower Unicode code points than lowercase letters. This means `'A'` comes before `'a'`, and `'Z'` comes before `'a'`. This is sometimes imprecisely called "ASCIIbetical order."
* **Digits and Punctuation:** Digits and most punctuation marks generally have lower Unicode code points than letters, meaning they will come before letters in a default sort.
* **Multi-character Strings:** When comparing strings with multiple characters, Python compares them character by character from left to right. If characters at the same position are equal, it moves to the next pair. If one string is a prefix of another (e.g., `'cap'` vs. `'cape'`), the shorter string comes first.

### Can sorting be done in reverse order in Python? If so, how?

Yes, both the `sorted()` function and the `list.sort()` method support reverse (descending) sorting. This is achieved by using the `reverse` keyword argument. By default, `reverse` is set to `False` (ascending order). To sort in descending order, you set `reverse=True`.

**Example:**
```python
sorted(numbers, reverse=True)  # sorts numbers from largest to smallest
```

### Custom Sorting with `key` and First-Class Functions

For more complex sorting criteria, both `sorted()` and `list.sort()` accept a `key` keyword argument. You can set your own rules for sorting the list as long as you can express the rule as a function.

#### What are "first-class functions" and "higher-order functions" in Python, and how do they relate to custom sorting?

* **First-Class Functions:** In Python, functions are considered "first-class objects." This means they can be:
* Assigned to variables.
* Passed as arguments to other functions.
* Returned as the result of other functions.

* **Higher-Order Functions:** These are functions that either take one or more functions as arguments or return a function as their result.

**Relation to sorting:**  
The `sorted()` function and `list.sort()` method are higher-order functions because they accept a function object as their `key` argument. This key function is a first-class function that transforms each element in the collection into a value that Python then uses for comparison during the sorting process, enabling tailored sorting criteria beyond the default.


### How is the key argument used in sorted() and list.sort() for custom sorting? Provide an example.

The `key` keyword argument in `sorted()` and `list.sort()` allows for custom sorting criteria. It takes a function as its value. This function is called once for each item in the collection, and its return value is used by the sorting algorithm for comparison. 

**Example: Sorting words by length**
```python
words = ["apple", "pie", "shortcake"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['pie', 'apple', 'shortcake']
```

Here, `len` (the built-in length function) is passed as the key. The `sorted()` function calls `len()` for each word, and the words are then ordered based on their lengths.


### How can you achieve multi-criteria sorting (sorting by one attribute, then another) using the key argument?

To achieve multi-criteria sorting, the function passed to the `key` argument should return a tuple of values. Python's sorting mechanism compares tuples element by element. It will first compare the first elements of the tuples, and if they are equal, it moves on to compare the second elements, and so on.

**Example: Sorting people by age, then by name**
```python
people = [("Jack", 30), ("John", 25), ("Betty", 25), ("Anna", 30)]

def person_key(person):
    name, age = person
    return (age, name) # Return a tuple: age first, then name

sorted_people = sorted(people, key=person_key)
print(sorted_people)
# Output: [('Betty', 25), ('John', 25), ('Anna', 30), ('Jack', 30)]
```

Here, `person_key` returns `(age, name)`. The list is first sorted by age. If two people have the same age (e.g., Betty and John, or Anna and Jack), their names are then used as the secondary sorting criterion.


### What are some practical considerations or useful rules to remember when working with character and string sorting in Python?

* **Uppercase before Lowercase:** Uppercase letters always come before their lowercase counterparts due to their lower Unicode values (e.g., `'A' < 'a'`). This often leads to "ASCIIbetical" results if not accounted for.

* **Digits and Punctuation:** Digits and most punctuation characters typically have lower Unicode values than letters, meaning they will appear earlier in a default sort.

* **Extended ASCII and Other Unicode:** Characters from "Extended ASCII" (code points 128-255) and other global scripts/symbols (code points 256 and above) will appear after standard ASCII characters, ordered by their respective Unicode values.

* **Case-Insensitive Sorting:** For case-insensitive string sorting, use `str.lower` as the key function (e.g., `sorted(animals, key=str.lower)`).

* **In-place vs. New List:** Remember the distinction between `list.sort()` (modifies in-place, returns `None`) and `sorted()` (returns a new sorted list, original unchanged) to avoid unexpected side effects.

### A heads up about lambda sorting

Take this code:

```python
some_names = [
    "Robert",
    "Ishaan",
    "Max",
    "Trevor",
    "Alexandra",
    "Albert",
    "Christine",
]

def get_number_of_a_s(item):
    return item.lower().count("a")

reordered_names = sorted(some_names, key=get_number_of_a_s)
print(*reordered_names, sep="\n")
```

It takes a list of names, and then sorts them according to the quantity of letter a's in the name. This code uses a function and each item in the list is put through the secondary function that's called in the `key=get_number_of_a_s`.

Now take this code:

```python
some_names = [
    "Robert",
    "Ishaan",
    "Max",
    "Trevor",
    "Alexandra",
    "Albert",
    "Christine",
]

reordered_names = sorted(
    some_names,
    key=lambda item: item.lower().count("a"),
)
print(*reordered_names, sep="\n")
```

It is the exact same output. But this case, lambda takes the place of of the function. Notice that its almost identical to the return statement of the first code snippet, with an extra `item:`.

Side by side Comparison:

```python
#Standard Function

def do_boring_stuff(x):
    return 42 * x

#Lambda Function
lambda x: 42 * x
```

Notice that `def do_boring_stuff(x):` and then `return` are covered by `lambda x:`.

The limitation of Lambda is that you can only have a single expression that evaluates to a value. This is the value returned by the lambda function. Therefore, you can't have complex algorithms in a lambda function, just whatever you can fit in a single expression!


### Sorting case insensitive: Because you will see this again.

To sort case insensitive:

```python

def sortme(lst1):
   
   return sorted(lst1, key=str.lower)
              
print(sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"])
print(sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"])

```

### So you have to write your own sorting criteria to be used in keyword=

When using your own code as a key function in sorted, there are a few key elements to keep in mind:

Key Function: The key function should take a single element from the list and return a value that will be used for sorting. This value can be a single value or a tuple, depending on your sorting criteria.

Return Value: The return value of the key function determines the sorting order. For example, if you want to sort elements in ascending order, the return value should be smaller for elements that should come first.

Sorting Criteria: The key function should implement the specific sorting criteria you want. For example, if you want to sort uppercase letters before lowercase letters, the key function should return a value that reflects this order.

[Back to the top](#top)
***

## Comprehensions
 
Comprehensions in Python are a concise and readable shorthand for creating collections such as lists, dictionaries, and sets. They allow you to generate these collections in a single line of code, often replacing multiple lines of traditional loops.

### What is the basic structure of a list comprehension and its components?  

* Structure: The basic structure is `[output_expression for item in existing_list if condition]`.
* Components:  
    * `output_expression`: Determines values in the returned list.  
    * `for item in existing_list`: Describes the looping action.  
    * `if condition`: Optional part for selection criteria (filtering).  
    * Brackets `[ ]`: Identify it as a list comprehension.  
    
**Functionality**: Primarily used for "transformations on lists," taking an existing list and creating a new one where each element is programmatically transformed. They also excel at "filtering" elements based on a condition, or combining both transformation and filtering.

* Transformations: They take an existing list and create a new list where each element has been programmatically transformed. For example, `[num**2 for num in nums]` squares every number in the nums list.  

Examples (Transformation):

```python
nums = [1, 2, 3, 4, 5]
squared = [num**2 for num in nums]
print(squared) # [1, 4, 9, 16, 25]
```

* Filtering: By including the optional if condition part, list comprehensions can select only certain objects from a list that satisfy the condition. For instance, `[num for num in nums if num % 2 == 0]` will create a new list containing only the even numbers from nums. You can also combine both, like `[num**2 for num in nums if num % 2 == 0]` to get the squares of only the even numbers.

Example (Filtering):  
```python
nums = [1, 2, 3, 4, 5]
evens = [num for num in nums if num % 2 == 0]
print(evens) # [2, 4]
```


### How do set comprehensions differ from list comprehensions?  

"Nearly identical to list comprehensions," but the output is a "set, an unordered collection with no duplicate values."

* Uses "curly braces" {} instead of square brackets.
* Important Note: Even without explicit filtering, a set comprehension can result in "fewer items than the original list" due to the elimination of duplicates.

Example:  
```python
nums = [1, 1, 2, 3, 4, 4, 5]
distinct_squares = {num**2 for num in nums}
print(distinct_squares) # {1, 4, 9, 16, 25}
```

### Are there dictionary comprehensions in Python, and how do they work?  

* Also "nearly identical to list comprehensions," outputting a dictionary.
* Uses "curly braces" `{}`.
* The output_expression is a key_expression: value_expression pair.

Example:  
```python
fruits = ['apple', 'banana', 'cherry']
fruit_length = {fruit: len(fruit) for fruit in fruits}
print(fruit_length) # {'apple': 5, 'banana': 6, 'cherry': 6}
```


### Can comprehensions be used with other iterable types beyond lists, sets, and dictionaries?  
Yes, comprehensions (list, set, and dictionary) can be used in conjunction with any iterable data type in Python. This includes tuples, ranges, strings, frozen sets, files, and more. The examples provided demonstrate their use with tuples, ranges, sets, and strings to create new collections.

### While useful, comprehensions can be overused. 

While comprehensions are powerful, there are specific situations where they should be avoided:  

* When you don't use the return value: If your primary goal is to perform an action like printing values (e.g., `[print(num) for num in nums]`), comprehensions are not appropriate because the print function returns None, resulting in a list of `None` values that you don't need. A regular for loop is much better for such side effects.  

* For identity transformations with constructors: If a comprehension simply copies elements without transformation (e.g., `[x for x in some_iterable]`), it's more idiomatic and efficient to use the collection's constructor directly, such as `list(string)` to convert a string to a list of characters. In general, if a comprehension becomes too complex or difficult to read, it's often better to revert to a traditional loop for improved clarity and maintainability.

* **Side Effects (e.g., printing)**:

Do not use comprehensions if you are "not using the return value." For example, using `[print(num) for num in nums]` will create a list of `None` values because the print function returns None. A regular for loop is more appropriate for actions with side effects.

* Incorrect Use Example:  
```python
nums = [1, 2, 3, 4, 5]
values = [print(num) for num in nums if num % 2 != 0]
print(values) # [None, None, None]
```
      
* Correct Alternative:  
```python
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 2 != 0:
        print(num)
```

* Identity Transformations:  If the comprehension is a simple identity transformation (e.g., `[x for x in some_iterable]`), it's better to use the collection's constructor directly, such as `list(string)` instead of `[c for c in string]`.


**In short, don't use comprehensions if you aren't using the return value**

[Back to the top](#top)
***

## Nested Data Structures and Iteration

> Nested data structures and nested iteration

### What are nested data structures in Python, and how do you access their elements? 

Nested data structures in Python refer to collections that contain other collections. For example, a list can contain other lists, dictionaries, tuples, sets, or frozensets. To access elements within a nested structure, you chain element references using bracket notation. Each level of nesting requires another set of brackets with the corresponding index or key.  

Example:  
```python
lst = [[1, 3], [2]]
lst[0][1]  # Accesses the second element of the first inner list (value: 3)
```
  
If you have a list containing a dictionary:  
```python
lst = [{"a": "ant"}]
lst[0]["a"]  # Accesses the value "ant"
```

### How do you update elements within nested data structures?

Updating elements in nested structures also involves chained actions, where the first part references the element, and the second part performs the reassignment or modification.
 
Example:  
```python
lst = [[1, 3], [2]]
lst[0][1] = 5  # Changes the second element of the first inner list to 5
```

**To insert a new key-value pair into a dictionary nested within a list:**  
```python
lst = [{"a": "ant"}]
lst[0]["c"] = "cat"  # Adds a new key-value pair to the first dictionary
```

**Replacing an entire inner collection:**  You can replace an inner collection with a new value (e.g., a string) by directly assigning to its index in the outer list. This is a "destructive action."  

Example:  
```python
lst = [[1, 3], [2]]
lst[1] = 'hi there' # lst is now [[1, 3], 'hi there']
```

**Modifying a value within a nested list:**  This is a "chained action" where `lst[0]` returns the inner list, and then `[1] = 5` reassigns the element within that inner list.  

Example:
```python
lst = [[1, 3], [2]]
lst[0][1] = 5 # lst is now [[1, 5], [2]]
```

**Inserting elements into an inner list:**  The `append()` method can be chained with an element reference to add new elements to an inner list.  

Examples:  
```python
lst = [[1], [2]]
lst[0].append(7)   # lst is now [[1, 7], [2]]

lst[0].append([9])  # lst is now [[1, 7, [9]], [2]]
```

**Inserting key/value pairs into nested dictionaries:**  Similar to lists, you reference the inner dictionary first, then use standard dictionary key/value creation syntax.  

Example:  
```python
lst = [{"a": "ant"}, {"b": "bear"}]
lst[0]["c"] = "cat" # lst is now [{'a': 'ant', 'c': 'cat'}, {'b': 'bear'}]
```

### Nested Comprehensions:

* Used for "nested lists or more advanced needs," such as flattening a matrix.
* Involve multiple `for` clauses, akin to nested loops.
* Structure: `[output_expression for sublist in outer_list if condition1 for item in sublist if condition2]`
* Caution: "Be careful with nested comprehensions. They can be incredibly difficult to read and debug. Sometimes, you just want to use regular loops."

Pattern:
```python
[output_expression for sublist in outer_list
                   if condition1
                   for item in sublist
                   if condition2]
```

Example:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_matrix = []

for row in matrix:
    for cell in row:
        flattened_matrix.append(cell)

print(flattened_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Even cubier:

cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Goal: Flatten to 1D
flat = [num for layer in cube for row in layer for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8]

# Equivalent:
flat = []
for layer in cube:
    for row in layer:
        for num in row:
            flat.append(num)
```

### Other Nested Structures and Hashability

Python lists can contain various data types, including dictionaries, tuples, sets, and frozen sets.

**Dictionaries:**  While the keys in a dictionary must be hashable, the values can be any type.

**Sets and Frozen Sets:**   Sets and frozen sets can also contain nested collections. **However, collections must be hashable**. Sets and frozen sets *cannot* contain lists, dictionaries, or other (non-frozen) sets. Tuples and frozen sets *are* hashable and can be contained within sets.

### Variable References and Pointers in Nested Collections

A crucial concept when working with nested collections is understanding that **variables store references to objects, not the objects themselves**. When an outer collection contains other collections, it holds references to those inner collection objects.

**Modifying a referenced object affects all references:**  

*Example:*  
```python
a = [1, 3]
lst = [a]
a[1] = 5 # lst[0] is now [1, 5]
```

**Modifying through different references:**  

*Example:*  
```python
a = [1, 3]
lst = [a]
lst[0][1] = 8    # a is now [1, 8]
```

In both cases, we're modifying the object that `a` and `lst[0]` point to; we now have two ways to reference the same object.

**Importance of understanding pointers:** This *fundamental concept* is critical for avoiding unexpected behavior.

* **Can all Python collection types be nested within each other without restrictions?**  

Not all Python collection types can be nested without restrictions, especially sets and frozensets. Sets and frozensets can only contain hashable objects, so they cannot directly contain mutable collections like lists, dictionaries, or other (non-frozen) sets. Tuples and frozensets themselves are hashable and can be elements of a set or frozenset.

* **Explain the concept of "variable references for nested collections" and why it's important to understand.**  

When you create nested collections by adding existing variables (which are themselves collections) to a new outer collection, you are adding references (pointers) to those objects, not copies. If you modify the original variable, the corresponding element within the nested structure will also change, and vice versa. This is because both point to the same object in memory. Understanding this helps avoid unintended side-effects when working with nested data structures.


### Nested Loops and Control Flow

You can nest loops within other loops:
```python
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(len(deck))  # 52
```

Control flow in nested loops:
* `break` only exits the innermost loop
* `continue` only affects the innermost loop
* To exit outer loops, use flags or functions

```python
# Using a flag to exit nested loops
found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
    if found:
        break
```

### Now for what they didn't explicitly say about nested comprehensions

```python
data = [[[0, 1], []], [[2, 3, 4], [5], [6, 7]], [], [[8, 9]]]

#This data needs to be flattened into one structure but there's a three levels going on.

#We can do it without list comprehensions:
lst = []
for sublist in data:
    for subsublist in sublist:  
        for value in subsublist:
            lst.append(value)
print(lst)
```

The order in the comprehension is the order you see here in the for loop. It goes from outermost to innermost. Literally, whatever the `for` loop would do in order, follow that in order. 

```python
new_lst = [value for sublist in data for subsublist in sub for val in subsub]
print(new_lst)
```

The pattern for list comprehensions for dictionaries are:
```python
[expression 
for outer_key, outer_value in outer_dict.items() 
for inner_key, inner_value in outer_value.items()]
```

#### Triangular Iteration

In another very common variation, you don't need to iterate over a nested structure, but you need a nested for loop to do the appropriate iteration. Take for example the following problem:

`Given a list of numbers: [1,2,2,3,4,4,5], return the HIGHEST sum of any consecutive numbers where a number doesn't 
repeat.`

The core idea is to use a nested loop structure to generate every possible consecutive sublist and then, for each one, check if it meets the criteria. Here’s how you can break down the problem using that pattern:

1.  **​Generate All Consecutive Sublists**​: This is where triangular iteration shines. Just like generating all substrings, you can generate all sublists. The outer loop will set the starting `index (i)`, and the inner loop will set the ending `index (j)`.
2.  **​Check for Uniqueness**​: For each sublist you generate, you need to see if all its elements are unique. A clever and Pythonic way to do this is to convert the sublist to a set and compare its length to the sublist's length. Since sets only store unique elements, the lengths will be equal only if the sublist had no duplicates.
3.  **​Calculate the Sum**​: If the sublist contains unique numbers, calculate its sum using the built-in `sum()` function.
4.  **​Keep Track of the Maximum**​: You'll need a variable to store the highest sum you've found so far. Compare the sum of each valid sublist to this variable and update it if the new sum is higher.

```python
def highest_sum(numbers):
    max_sum = 0

    # Triangular iteration to generate all consecutive sublists. `i` is the starting index of the sublist
    for i in range(len(numbers)):
        # `j` is the ending index of the sublist
        for j in range(i, len(numbers)):
            # Create the sublist using a slice
            sublist = numbers[i : j+1]

            # 1. Check for uniqueness
            if len(sublist) == len(set(sublist)):
                # 2. If unique, calculate the sum
                current_sum = sum(sublist)

                # 3. Update the maximum sum found so far
                if current_sum > max_sum:
                    max_sum = current_sum

    return max_sum


my_numbers = [1, 2, 2, 3, 4, 4, 5]
print(highest_sum([1,2,2,3,4,4,5]) == 9) #True
print(highest_sum([]) == 0) #True
print(highest_sum([1,1,1]) == 1) #True
print(highest_sum([1,1,2,3,4,5,5,6]) == 15) #True
```

Let's trace the first few steps with your list `[1, 2, 2, ...]`:

•   `​i = 0​`:
    •   `​j = 0​`: sublist is `[1]`. It's unique. `sum`is `1`. `max_sum` becomes `1`.
    •   `​j = 1`​: sublist is `[1, 2]`. It's unique. `sum` is `3`. `max_sum` becomes `3`.
    •   `​j = 2​`: sublist is `[1, 2, 2]`. It's ​not​ unique `(len([1,2,2])` is `3`, but `len(set([1,2,2])) is 2)`. We do nothing.
•   `​i = 1`​:
    •   `​j = 1​`: sublist is `[2]`. It's unique. `sum` is `2`. `max_sum` is still `3`.
    •   `​j = 2`​: sublist is `[2, 2`]. It's ​not​ unique. We do nothing.
    •   `​j = 3`​: sublist is `[2, 2, 3`]. It's ​not​ unique. We do nothing.
•   `​i = 2`​:
    •   `​j = 2`​: sublist is `[2]`. It's unique. `sum` is `2`. `max_sum` is still `3`.
    •   `​j = 3​`: sublist is `[2, 3]`. It's unique. `sum`is `5`.

`max_sum` becomes `5`.

[Back to the top](#top)
***


## Shallow and Deep Copy

When copying collections, it's essential to understand the difference between shallow and deep copies, especially with nested structures.

### Shallow Copying

A shallow copy **creates a new copy of the object, but doesn't create new versions of any nested mutable objects.** Instead, it copies references to those nested mutable objects.

**Behavior:**
* Changes to elements at the top level of the new list will **not** affect the original.
* Changes to elements within nested mutable objects **will** be reflected in both the original and the new copy because they still share the same nested objects.
* This is often desired for performance reasons, as it's less resource-intensive.

**Techniques for Shallow Copying:**

* `list()` function:  
```python
copy_of_lst = list(lst)
```

* Slicing (very Pythonic):  
```python
copy_of_lst = lst[:]
```

* `.copy()` method (explicit, concise, readable; available for lists, sets, frozen sets, dictionaries):  
```python
copy_of_lst = lst.copy()
```

* `copy.copy()` from `copy` module (works with all iterable collections and returns the same type):  
```python
import copy
copy_of_lst = copy.copy(lst)
```

**Key takeaway:**  The critical thing to be aware of is what level you're working at, especially when working with nested collections. If you mutate a shared nested object, the change affects all references to that object.

### Deep Copying

A deep copy **creates a new copy of the object, and recursively creates new copies of all the nested mutable objects in the original object.**

**Behavior:**
* Changes to elements at the top level of the new list will **not** affect the original.
* Changes to elements within nested mutable objects in the new list will **not** affect the original, as completely new copies of these nested objects have been created.
* It can take a great deal more processing to make a deep copy than a shallow copy. Thus, think before you deep copy. Only do it when you need it.

**Technique for Deep Copying:**

* `copy.deepcopy()` from the `copy` module (works for lists, dictionaries, tuples, ranges, etc.):  
```python
import copy
new_lst = copy.deepcopy(lst)
```

Understanding nested data structures, variable references, and the nuances of shallow vs. deep copying is crucial for effective and predictable manipulation of complex data in Python. Mastering these concepts **clarifies our understanding of collections and how to work with them**, enabling developers to implement robust solutions.

[Back to the top](#top)
***

## User-level Synergy

Discuss a function's use and purpose (a "user-level" description) instead of its implementation. This line means you should be able to explain what a function does and why you would use it—focusing on its role or effect—without needing to describe the code inside the function or how it works step-by-step. It's about understanding and communicating the function’s purpose clearly from a user's perspective.

[Back to the top](#top)
***

## Further Practice

[Atropos-Null. (n.d.). LS/py110/lesson_2/py110_comprehensions.md at main · atropos-null/LS. GitHub.](https://github.com/atropos-null/LS/blob/main/py110/lesson_2/py110_comprehensions.md)

[Atropos-Null. (n.d.-b). LS/py110/lesson_2/py110_practiceproblems2.md at main · atropos-null/LS. GitHub.](https://github.com/atropos-null/LS/blob/main/py110/lesson_2/py110_practiceproblems2.md)

[The-Spot-Hub. (n.d.). SPOT-Wiki/Lesson Materials & Code/PY110/Python110_ProblemSets.md at main · The-SPOT-Hub/SPOT-Wiki. GitHub.](https://github.com/The-SPOT-Hub/SPOT-Wiki/blob/main/Lesson%20Materials%20%26%20Code/PY110/Python110_ProblemSets.md)

[Back to the top](#top)
***
