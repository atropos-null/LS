# PY110 Working Document

<a name="top"></a>

## Table of Contents

- [Introduction to Collections in Python](#introduction-collections-python)
- [Sequences](#sequences)
- [Dictionaries, Sets, and Frozen Sets](#dictionaries-sets-frozen-sets)
- [Working with Strings and Ranges](#working-strings-ranges)
- [Working with Lists and Tuples](#working-lists-tuples)
- [Working with Dictionaries, Sets, and Frozen Sets](#working-dictionaries-sets-frozen-sets)
- [Unpacking Iterables in Python](#unpacking-iterables-python)

***

## Introduction to Collections in Python

A **collection** is a generic term that encompasses several container data types in Python. These containers hold multiple objects, which can be of varied types. The primary purpose of a collection is to store, retrieve, and manipulate data. They do not necessarily maintain order.

**Sequences**, on the other hand, are a subset of collections. What sets them apart is their inherent ability to maintain order. In a sequence, each element has a definite position, defined by its index, which starts from zero and increments by one for each subsequent element.

It's crucial to understand that all sequences are collections, but not all collections are sequences. For instance, strings, lists, and tuples are both sequences and collections. However, sets, frozen sets, and dictionaries are collections but not sequences.

| Collection | Ordered? | Mutable? | Allows Duplicates? | Indexable?     | Syntax                 |
| ---------- | -------- | -------- | ------------------ | -------------- | ---------------------- |
| List       | Yes      | Yes      | Yes                | Yes            | [1, 2, 3]            |
| Dictionary | Yes*     | Yes      | No (keys)          | No (uses keys) | {'a': 1, 'b': 2}     |
| Tuple      | Yes      | No       | Yes                | Yes            | (1, 2, 3)            |
| Set        | No       | Yes      | No                 | No             | {1, 2, 3}            |
| Range      | Yes      | No       | No                 | Yes            | range(1, 4)          |
| Frozenset  | No       | No       | No                 | No             | frozenset([1, 2, 3]) |

Strings are a special type of sequence called "text sequences." Strings are unique among sequences because each character doesn't have a separate identity but is simply part of the original string.

Page Reference: [Introduction to Collections in Python](https://launchschool.com/lessons/1b66cd61/assignments/c3630f0c)


[Back to the top](#top)
***

## Sequences

### Lists

**Lists** (mutable) in Python represent an ordered collection of objects, characterized by zero-based indexing and mutability. The objects in a list are ordered by their position, or index, starting from `0`. Each element in the list can be of any data type, offering flexibility in the kind of data a list can hold. To access a specific element, use its index:

```python 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])   # [2, 3, 4]
print(numbers[:4])    # [0, 1, 2, 3]
print(numbers[6:])    # [6, 7, 8, 9]
print(numbers[::2])   # [0, 2, 4, 6, 8] (every second element)
print(numbers[-1:1])  # [9]
print(numbers[-4:-1]) # [6, 7, 8]
print(numbers[11])    # IndexError


numbers = [1, 2, 3, 4]
numbers[0] = numbers[0] + 1
print(numbers) #[2, 2, 3, 4]

#or:

numbers = [1, 2, 3, 4]
for i in range(len(numbers)):
    numbers[i] += 1
print(numbers) #[2, 3, 4, 5]
```

### Tuples

**Tuples** (immutable) are ordered collections of objects, similar to lists. However, unlike lists, tuples are immutable, meaning their content cannot be altered after creation. This makes them suitable for representing fixed collections of objects. To access a specific element, use its index:

```python
coordinates = (1, 2, 3, 4, 5, 6)
print(coordinates[0:2])   # (1, 2)
print(coordinates[3:])    # (4, 5, 6)
print(coordinates[::-1])  # (6, 5, 4, 3, 2, 1)

fruits = ("apple", "banana", "cherry")
fruits[0] = "strawberry" # TypeError: 'tuple' object does not support item assignment
```

### Strings

**Strings** (immutable) represent sequences of characters. A string is an ordered collection of characters, used to store and represent text-based information. Like tuples, strings are immutable. To access a specific element, use its index. As with lists and tuples we can use negative indexes:

```python
text = "Python Programming"
print(text[0:6])      # "Python"
print(text[7:])       # "Programming"
print(text[::-1])     # "gnimmargorP nohtyP" (reversed)
print(text[::2])      # "Pto rgamn" (every second character)
print(text[18])       #IndexError
```

As strings are immutable, you cannot modify a string's value. However, you can replace a string's value with a completely new string by using reassignment:

```python
greeting = "Hello, World"
greeting[7] = "m" #TypeError: 'string' object does not support item assignment

#Or:

greeting = "Hello, World"
print(greeting) #Hello, World
greeting = "What's up, Doc?"
print(greeting)  #What's up, Doc?
```

### Ranges

A **range** is an immutable sequence of numbers commonly used when looping. They are arithmetic progressions of integers. Compared to lists and tuples, they are memory-efficient since they only store the start, stop, step, and current values. The next element in a range is computed based on the current state of the range, but only when it is needed. To access a specific element in a range, use its index. As with other sequences, you can also use negative indexes:

```python
numbers = range(10, 20)
print(numbers[3]) #13
print(numbers[-4]) #16
print(numbers[100]) #IndexError: range object index out of range

```

As ranges are immutable, this means you cannot modify a value within the range but can with reassignment.

```python
numbers = range(5, 10)
numbers[3] = 12 #TypeError: 'range' object does not support item assignment

numbers = range(5, 10)
print(list(numbers)) #[5, 6, 7, 8, 9] The memory efficiency of ranges is why 
                     # we need to use list to expand the above ranges. Since Python doesn't 
                     # automatically expand the ranges, we have to explicitly do so ourselves

numbers = range(5, 0, -1) 
print(list(numbers)) #[5, 4, 3, 2, 1]
```

### Slicing

The basic syntax for slicing is: `sequence[start:stop:step]`

Where:
* start: The index where the slice begins (inclusive)
* stop: The index where the slice ends (exclusive)
* step: The interval between elements in the slice

When any parameter is omitted:
* Missing start defaults to 0 (beginning of sequence)
* Missing stop defaults to the length of the sequence
* Missing step defaults to 1 (every element)

### Determining Length

`len()`

```python
lst = [1, 2, 3]
print(len(lst)) #3

tup = (4, 5, 6, 432)
print(len(tup)) #4

string = "hello"
print(len(string)) #5

r = range(0, 12, 2)
print(len(r)) #6
```

### Iterating over a Sequence

All sequence types are iterables, meaning Python can iterate over the sequence's elements in a loop. Iterating refers to traversing each item in a collection. In Python, there are multiple ways to iterate, with the `for` loop being the most common and idiomatic way.

```python
lst = [1, 2, 3]
for item in lst:
    print(item)

#1
#2
#3

colors = ("red", "blue", "green")
for color in colors:
    print(color)

# red
# blue
# green

message = "bye"
for char in message:
    print(char)

#b
#y
#e
```

Further Reference:

(Gruppetta, S. (2023a, April 20). Iterable: Python’s Stepping Stones. The Python Coding Stack.)[https://www.thepythoncodingstack.com/p/python-iterable-data-structures]

### Concatenating with the `+` Operator

The `+` operator can concatenate sequences of the same type. That is, it appends the sequence to the right to the sequence on the left and returns a new sequence:

```python
new_list = [1, 2, 3] + [4, 5, 6]
print(new_list) #[1, 2, 3, 4, 5, 6]

new_str = "Hello, " + "World!"
print(new_str) #'Hello, World!'

new_tup = (1, 2) + (True, "hello")
print(new_tup) #(1, 2, True, 'hello')
```

This operation creates a new sequence. It doesn't modify the original sequences. Concatenation, however, doesn't apply to ranges. Attempting to concatenate ranges will raise a `TypeError`.

### `count()` and `index()`

The count and index methods are available for all sequences.

* `sequence.count(value)`: Returns the number of occurrences of a value in the sequence.
* `sequence.index(value)`: Returns the index of the first occurrence of a value in the sequence. If the value isn't present, Python raises a `ValueError`.

```python
lst = [1, 2, 2, 3, 4, 4, 4]
print(lst.count(4)) #3
print(lst.index(4)) #4

string = "hello"
print(string.count("l")) #2
print(string.index("l")) #2
print(string.index("M")) #ValueError: substring not found

rng = range(5, 10)
print(rng.count(7)) #1
print(rng.count(12)) #0
print(rng.index(7)) #2

```

### `min()` and `max()

For lists and tuples, the behavior of `min` and `max` depends on the content of the sequence. If it contains numeric values, `min` and `max` return the smallest and largest number, respectively.

```python
numbers = [3, 1, 4, 1, 5]
print(min(numbers)) #1

num_tup = (2, 3, 7, 1)
print(max(num_tup)) #7
```

If the sequence contains strings, `min` and `max` compare strings lexicographically. In other words, strings are compared character by character using the Unicode values of their characters. The function returns the character with the smallest or largest Unicode value:

```python
word = "banana"
print(min(word)) # 'a' 'a' is the smallest and 'n' is the largest Unicode value in this string.
print(max(word)) # 'n'
```

Ranges return the `min` or `max` number in the range:

```python
print(min(range(5))) #0
print(max(range(5))) #4
```

### Conversion to Lists and Tuples

#### Converting to a list

```python
string = "hello"    #Converting a string to a list breaks the string into individual characters
print(list(string)) #['h', 'e', 'l', 'l', 'o']

my_tup = (0, 1, 2, 3) #Converts from a tuple to a list, preserving order
print(list(my_tup)) #[0, 1, 2, 3]

r = range(5)   #Converting a range to a list creates a list of numbers in the given range
print(list(r)) # [0, 1, 2, 3, 4]
```

#### Converting to a Tuple

```python
lst = [1, 2, 3, 4]
print(tuple(lst)) #(1, 2, 3, 4)

string = "hello"
print(tuple(string)) #('h', 'e', 'l', 'l', 'o')

my_range = range(3)
print(tuple(my_range)) #(0, 1, 2)
```

#### Converting to Strings

```python
lst = [1, 2, 3, 4]
print(str(lst)) #'[1, 2, 3, 4]'

tup = (1, 2, 3, 4)
print(str(tup)) #'(1, 2, 3, 4)'

my_range = range(3)
print(str(my_range)) # 'range(3)'
```

Not exactly what you want. `join()` is probably a better method.

```python
my_list = ["1", "2", "3", "4"]
print(''.join(my_list)) #'1234'

tup = ("four", "score", "and", "seven", "years", "ago")
print(' '.join(tup)) #'four score and seven years ago'
```

Note that all elements of the sequence must be strings when using `join`. One way to get around that is to use a list comprehension as an argument to `join`:
```python
my_list = [1, 2, 3, 4]
my_str = ', '.join([str(element) for element in my_list]) #'1, 2, 3, 4'
print(my_str)
```

Page Reference: [Sequences](https://launchschool.com/lessons/1b66cd61/assignments/90b357b4)

Further References:

[Barczykowska, E. (2024, November 26). Python notes: Slicing — Part 1 - Level Up Coding. Medium.](https://medium.com/gitconnected/python-notes-slicing-part-1-73209d5cbb02)

[Barczykowska, E. (2024b, November 27). Python notes: Slicing — Part 2 - Level Up Coding. Medium.](https://medium.com/gitconnected/python-notes-slicing-part-2-41f2e95ebef5)

[Gruppetta, S. (2023a, September 24). A slicing story. The Python Coding Stack.](https://www.thepythoncodingstack.com/p/a-python-slicing-story)

[Gruppetta, S. (2023b, April 28). Sequences in Python (Data Structure Categories #2). The Python Coding Stack.](https://www.thepythoncodingstack.com/p/sequences-in-python-data-structure-2)


[Back to the top](#top)
***

## Dictionaries, Sets, and Frozen Sets

### Dictionaries 

Dictionaries in Python are **unordered collections of key-value pairs**, they map keys to values.  They're defined using curly braces `{}` with key-value pairs separated by colons. Dictionaries are meant to make it easy to look up the value that corresponds to a particular key.


#### Dictionary Characteristics

1. **​Keys must be immutable**​:

* Allowed keys: strings, numbers, tuples (containing only immutable elements), and frozensets
* Not allowed: lists, sets, dictionaries (mutable objects)
* Dictionary keys must be hashable, not just immutable. Hashability means the object has a hash value that doesn't change during its lifetime (which is why immutability is a prerequisite for hashability). Dictionary keys must be hashable because dictionaries use a hash table implementation internally for efficient lookups
* When you use a mutable object as a key you get a `TypeError`.

```python
my_dict = {}
my_dict[[1, 2, 3]] = "value"  # Raises TypeError: unhashable type: 'list'
```


2. **​Values can be any type**​: Strings, numbers, lists, other dictionaries, functions, etc.

3.  **Order**:

* ​Unordered​ before Python 3.7. Now: dictionaries maintain insertion order
* Don't rely on order for the assessment

4. You can add, modify, or delete key-value pairs after creation.

#### Methods of creating a dictionary

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

3.  Dictionary Comprehensions: For creating dictionaries based on existing data.

```python
# Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
letter_dict = {k: v for k, v in zip(keys, values)}
# Result: {'a': 1, 'b': 2, 'c': 3}
```

#### Accessing values in dictionaries


1. **Using Square Bracket Notation**: The most common way to access dictionary values is using square brackets with the key

* If the key doesn't exist, Python will raise a `KeyError`.
* Case sensitivity matters - keys must match exactly.

```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'year': 2003,
}

print(car['color'])  # Outputs: blue
```

2. **Using the `get()` method**: the preferred approach when you're not sure if a key exists in the dictionary.
```python
# Returns the value if key exists
print(car.get('color'))  # blue

# Returns None if key doesn't exist (no error)
print(car.get('model'))  # None

# Returns a default value if the key doesn't exist
print(car.get('model', 'Unknown'))
```

3. **Checking if a Key Exists**: Before accessing a value, you can check if a key exists using the `in` operator.
```python 
student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student)      # False
print('grade' in student)     # True

# Using it in an if statement
if 'grade' in student:
    print(student['grade'])
else:
    print("Unknown")
```

4. Accessing Values in Nested Dictionaries: for nested dictionaries, chain the square brackets.

Additionally, `get()` with nested dictionaries approach is particularly useful as it won't raise an error if any level of the nested structure is missing.

```python
vehicles = {
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003,
    },
    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': 1998,
    },
}

# Access a value in a nested dictionary
print(vehicles['car']['color'])  # blue

# Using get() with nested dictionaries
print(vehicles.get('car', {}).get('color', 'Unknown'))  # blue
```

**A table for easier viewing, with extra defaults**

| Option                                 | Use case                                             |
|----------------------------------------|------------------------------------------------------|
| `key in my_dict`                       | Check whether a key is in the dictionary             |
| `my_dict.get(key, default)`            | Get the value or a default just once                 |
| `my_dict.setdefault(key, default)`     | Set the value if it's not yet set                    |
| `my_dict = dict.fromkeys(keys, default)`| Construct dictionary with known keys, defaulting values|
| `my_dict = {key: [] for key in keys}`  | Construct dictionary with mutable values for defaults|
| `my_dict = Counter(items)`             | Create mapping meant just for counting occurrences   |
| `my_dict = defaultdict(list)`          | Create mapping with a default for all key lookups    |

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

#### Removing from dictionaries

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

5. Dictionary Comprehension for Selective Removal: To remove multiple items based on a condition, you can use dictionary comprehension.  

```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
    'year': 2003,
    'previous_owners': 2,
}

# Remove all keys that have numeric values
car = {k: v for k, v in car.items() if not isinstance(v, int)}
print(car)  # {'type': 'sedan', 'color': 'blue'}
```

Be sure not to remove while iterating through it, instead create a copy or collect keys to remove first.

```python

# Safer approach
car = {'type': 'sedan', 'color': 'blue', 'mileage': 80_000}
keys_to_remove = [k for k in car if k != 'type']
for key in keys_to_remove:
    del car[key]
```

#### Dictionary Methods

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

**`dict.get()`**: retrieves a value associated with a key. It is safer than bracket notation because it does not raise `KeyError` for missing keys. It provides a clean way to handle missing keys with default values. Can be chained for nested dictionaries: `data.get('user', {}).get('address', {})`

These usually work together!

```python

# Check if a specific value exists in the dictionary
if 'blue' in car.values():
    print("The car is blue")
    
# Check if a specific key exists
if 'model' not in car.keys():  # or simply: if 'model' not in car:
    car['model'] = 'standard'
```

#### Here's a quick syntax review:

```python

# Get all keys
keys = car.keys()  # dict_keys(['type', 'color', 'year'])

# Get all values
values = car.values()  # dict_values(['sedan', 'blue', 2003])

# Get all key-value pairs
items = car.items()  # dict_items([('type', 'sedan'), ('color', 'blue'), ('year', 2003)])
```

#### Nested Dictionaries

These happen alot:

Creating a nested dictionary

```python
 
nested_dict = {
    'person1': {
        'name': 'John',
        'age': 30,
        'hobbies': ['reading', 'hiking']
    },
    'person2': {
        'name': 'Lisa',
        'age': 25,
        'hobbies': ['painting', 'running']
    }
}

# Accessing nested elements
john_age = nested_dict['person1']['age']  # Gets 30
lisa_hobby = nested_dict['person2']['hobbies'][1]  # Gets 'running'

# Adding new nested data
nested_dict['person3'] = {'name': 'Mike', 'age': 35, 'hobbies': ['swimming']}

# Modifying nested data
nested_dict['person1']['hobbies'].append('cooking')

# Consider the nested dictionary below. 
# Write code to: Access the value 'apple'
# Change 'banana' to 'orange'
# Add a new fruit 'grape' to person2's favorites
   
people = {
    'person1': {'name': 'John', 'age': 25, 'favorites': ['apple', 'banana']},
    'person2': {'name': 'Sarah', 'age': 30, 'favorites': ['cherry']}
}

print(people['person1']['favorites'][0])

#Change 'banana' to 'orange'
people['person1']['favorites'][1] = 'orange'
print(people)

## Add 'grape' to person2's favorites
people['person2']['favorites'].append('grape')
print(people)
```

Further References:

[Gruppetta, S. (2024b, May 27). `dict()` is More Versatile Than You May Think. The Python Coding Stack.](https://www.thepythoncodingstack.com/p/python-dict-is-more-versatile-than-you-may-think)

[Back to the top](#top)


### Hashability

A **hash value** is essentially a numeric "fingerprint" of data. When Python needs to store or look up objects in dictionaries or sets, it uses this fingerprint instead of comparing entire objects.

```python
print(hash("hello"))  # Might output: 8768730738463847
print(hash("hello"))  # Will always output the same number for "hello"
```

#### How Hash Values Are Derived

1.  Python applies a mathematical algorithm to convert data of any size into a fixed-size number
2.  The algorithm ensures that:
    * The same input always produces the same hash value
    * Different inputs (usually) produce different hash values
    * The calculation is fast

Python's exact hashing algorithm is implementation-specific, but it's designed to distribute values evenly across the numeric range.

#### Practical Use Cases

The main reason hash values matter is for dictionary and set operations:
```python

# When you do this:
student_grades = {}
student_grades["Alice"] = 95
```

Python internally does the following:
1. Calculates hash(`"Alice"`)
2. Uses that number to determine where to store `95`
3. When retrieving, calculates hash(`"Alice"`) again to find the location

#### Why Some Objects Can't Be Dictionary Keys

Since dictionaries rely on hash values staying consistent, only immutable objects can be used as keys.

#### What Makes an Object Hashable

An object is hashable if:

1.  It has a `__hash__()` method that returns the same integer value throughout its lifetime
2.  It can be compared to other objects via an `__eq__()` method
3.  If `a == b` is True, then `hash(a) == hash(b)` must also be True

This means the hash value must remain constant for the object's entire lifetime, which is why hashable objects are typically immutable.

#### The Hash Function

The `hash()` built-in function:

```python
number = 42
print(hash(number))  # Returns an integer hash value
```

This function computes a fixed-size integer from an object of arbitrary size.

```python
# Same value always produces the same hash
print(hash("hello") == hash("hello"))  # True

# Different values produce different hashes (with rare collisions)
print(hash("hello") == hash("world"))  # False
```


### Immutability and Hashability

Immutability is closely tied to hashability because:

```python
This tuple is immutable and hashable
t = (1, 2, 3)
print(hash(t))  # Works fine

# This list is mutable and not hashable
l = [1, 2, 3]
try:
    print(hash(l))
except TypeError as e:
    print(e)  # "unhashable type: 'list'"

```

If objects could change their values while maintaining the same hash, it would break hash table data structures. 

#### Hashable vs. Non-hashable Types

**Hashable Types (Immutable)**:
* Numbers (int, float, complex)
* Strings
* Bytes
* Tuples (if all elements are hashable)
* Frozen sets
* None
* Boolean values

**Non-hashable Types (Mutable)**:
* Lists
* Dictionaries
* Sets
* Byte arrays
* User-defined classes (by default are hashable, but become non-hashable if you implement __eq__ without __hash__)

#### Hash Tables in Python

Internally, dictionaries and sets use hash tables:
1.  When you add a key to a dictionary, Python:
    * Computes the key's hash value
    * Uses that value to determine where to store the key-value pair
    * When retrieving, it calculates the hash again to find the location
2. This allows for `O(1)` average-case complexity for lookups, rather than `O(n)` with lists, This makes lookups extremely fast because Python can jump directly to the right location rather than searching through everything.

#### Hash Collisions

Sometimes different objects can produce the same hash value:
```python
# These might have the same hash (though unlikely)
str1 = "ab"
str2 = "ba"

```

When this happens, Python's hash tables handle it through techniques like chaining (storing multiple items in the same bucket).

>"A hashable type is a type from which consistent hash values can be computed. A hash function takes an object and returns a hash value, which is used internally in a dictionary to store and retrieve values. Given two identical objects, the hash function must return the same value for both objects."

Further References:

[Gruppetta, S. (2024a, May 11). Where’s William? How quickly can you find him? • What’s a Python hashable object? The Python Coding Stack.](https://www.thepythoncodingstack.com/p/wheres-william-python-hash-hashable)

[Zaczyński, B. (2023, December 1). Build a hash table in Python with TDD.](https://realpython.com/python-hash-table/)

[Back to the top](#top)

### Sets

**Sets** are designed to hold distinct objects, disregarding any sense of order. Sets are unordered collection, no duplicates, mutable but contains only immutable objects. Uses `{}`

​Use Cases​:

* When you need to ensure uniqueness of elements
* Set operations (union, intersection, difference)
* Membership testing for large collections (faster than list)

```python
# Creating a set
unique_numbers = {1, 2, 3, 4, 5}
tags = {"python", "programming", "tutorial"}
```

Sets in Python are mutable, meaning you can modify them after creation by:

* Adding elements using `add()` or `update()`
* Removing elements using `remove()`, `discard()`, or `pop()`
* Clearing all elements with `clear()`

```python
fruits = {'apple', 'banana', 'cherry'}
fruits.add('grape')
fruits.add('strawberries')
print(fruits) #{'apple', 'banana', 'cherry', 'grape', 'strawberries'}
```

While sets themselves are mutable, they can only contain hashable objects, which in Python are typically immutable objects. This is because sets use a hash table implementation internally for fast lookups. Python imposes this requirement to prevent duplicate elements and swiftly respond to set membership checks. Without hashing, Python would have to search every element in the set every time you add a new member, delete an existing member, or check for membership. Attempting to add a mutable object, like a list, to a set results in a `TypeError`.

These objects can be included in sets:

* Integers: `{1, 2, 3}`
* Floats: `{1.1, 2.2, 3.3}`
* Strings: `{"apple", "banana"}`
* Tuples (if they contain only immutable objects): `{(1, 2), (3, 4)}`

These objects CANNOT be included in sets:

* Lists: `{[1, 2], [3, 4]}` 
* Dictionaries: `{{1: 'a'}, {2: 'b'}} `
* Sets: `{{1, 2}, {3, 4}}` 

As with dictionaries, sets don't rely on positional indexing. Instead, they're all about membership. However, they also don't rely on keys as dictionaries do. This means you can't pinpoint a specific object in the set, but you can swiftly and efficiently determine whether an object is in the set:

```python
fruits = {'apple', 'banana', 'cherry'}
print('apple' in fruits) #True
print'grape' in fruits) #False
```

Since sets don't have the concept of order or indexing, any attempt to reference a set member by its index or key will be rebuffed by Python, giving way to a `TypeError`. And, if you try to add a value that already exists in the set, it won't be added again. Python won't raise an error, either. It simply ensures that all values in the set are unique

[Back to the top](#top)

### Frozen Sets

**Frozen set** is an immutable version of a regular set. Once created, you cannot modify its contents - no adding, removing, or changing elements. Frozen sets are significant because their immutability makes them hashable, which means:

Key Characteristics​:

* Immutable (cannot be changed after creation)
* Unordered collection of unique elements
* Can only contain immutable (hashable) objects
    * making them useful as dictionary keys
    * make them useful as elements in other sets
* Created using the `frozenset()` constructor function
* Supports all set operations that don't modify the set (intersection, union, etc.)

```python
# Creating a frozen set
frozen_colors = frozenset(["red", "blue", "green"])

# Attempting to modify will cause errors
frozen_colors.add("yellow")  # AttributeError!
```

Keep in mind:

* frozen sets are useful when you need an immutable collection of unique items
* They support methods like `isdisjoint()`, `issubset()`, and `issuperset()`
* They can be created from any iterable (lists, tuples, regular sets, etc.)
* They cannot be modified after creation

The key difference between sets and frozensets is their mutability. While **both are unordered collections of unique** elements, **regular sets can be modified** after creation, whereas **frozensets are immutable**. This immutability makes frozensets hashable, so they can be used as dictionary keys or as elements in other sets.

As with sets, frozen sets don't support positional indexing. Their primary function is to confirm membership. You can easily verify whether an object belongs to a frozen set, but you can't access an element by its position.

```python
immutable_fruits = frozenset(['apple', 'banana', 'cherry'])
print('apple' in immutable_fruits) #True
print('grape' in immutable_fruits) #False
```

Frozen sets and sets share the principle of not maintaining order or indexing. Therefore, you can't reference an element with an index or key, to attempt to do so would result in a `TypeError`.

### Operations on Dictionaries, Sets and Frozen Sets

The `in` keyword helps check whether an element is present in the collection. For dictionaries, it checks among keys.

```python
# For dictionaries:
person = {'name': 'John', 'age': 25}
print('name' in person) #True
print('height' not in person) #True

# For sets and frozen sets:
fruits_set = {'apple', 'banana'}
print('apple' in fruits_set) #True

fruits_frozenset = frozenset(['apple', 'banana', 'cherry'])
print('apple' in fruits_frozenset) #True
```

The `len` function returns the number of elements in the collection.

```python
person = {'name': 'John', 'age': 25}
print(len(person))  # 2

fruits_set = {'apple', 'banana'}
print(len(fruits_set))  # 2

fruits_frozenset = frozenset(['apple', 'banana', 'cherry'])
print(len(fruits_frozenset))  # 3
```

The clear method empties the collection of all its elements. It does not work with frozen sets since frozen sets are immutable.

```python
person = {'name': 'John', 'age': 25}
person.clear()
print(person)  # {}

fruits_set = {'apple', 'banana'}
fruits_set.clear()
print(fruits_set)  # set()
```

While the specific elements (keys for dictionaries and values for sets and frozen sets) differ, the iteration mechanism is consistent

```python
# For dictionaries (iterates over keys):
person = {'name': 'John', 'age': 25}
for key in person:
    print(key)  # prints each key

# For sets:
fruits_set = {'apple', 'banana'}
for fruit in fruits_set:
    print(fruit)  # prints each fruit

# For frozen sets
fruits_frozenset = frozenset(['apple', 'banana', 'cherry'])
for fruit in fruits_frozenset:
    print(fruit)  # prints each fruit
```

### Conversion to Dictionaries, Sets, and Frozen Sets

```python

#Converting to dictionary
list_of_pairs = [('a', 1), ('b', 2), ('c', 3)] 
print(dict(list_of_pairs))  # {'a': 1, 'b': 2, 'c': 3}

#using the zip function with dict function
keys = ['a', 'b', 'c']
values = [1, 2, 3]
zipped_pairs = zip(keys, values)
print(dict(zipped_pairs))  # {'a': 1, 'b': 2, 'c': 3}

#Converting list to set
my_list = [1, 2, 2, 3, 4, 4, 4]
print(set(my_list))  # {1, 2, 3, 4}

#Converting string to set
string = "hello"
print(set(string))  # {'h', 'e', 'l', 'o'}

#Converting range to set
my_range = range(5)
print(set(my_range))  # {0, 1, 2, 3, 4}

#Converting list to frozenset
my_list = [1, 2, 2, 3, 4, 4, 4]
print(frozenset(my_list))  # frozenset({1, 2, 3, 4})

#Converting string to frozen set
string = "hello"
print(frozenset(string))  # frozenset({'h', 'e', 'l', 'o'})

#Converting range to frozen set
my_range = range(5)
print(frozenset(my_range))  # frozenset({0, 1, 2, 3, 4})

#Converting set to frozen set
fruit_set = {'apple', 'banana', 'cherry'}
fruit_frozenset = frozenset(fruit_set)
print(fruit_frozenset)  # frozenset({'banana', 'cherry', 'apple'})

#Conversting frozen set to set
fruit_frozenset = frozenset(['apple', 'banana', 'cherry'])
fruit_set = set(fruit_frozenset)
print(fruit_set)  # {'banana', 'cherry', 'apple'}
```

Page Reference: [Dictionaries, Sets and Frozen Sets](https://launchschool.com/lessons/1b66cd61/assignments/4e57cfc2)

[Back to the top](#top)

***

## Working with Strings and Ranges

### Working with Ranges

**Range Object:**  
Python's `range()` function creates a special range object, which is an iterable sequence of numbers. In Python, the range function offers a convenient way to generate a sequence of numbers. This special sequence is encapsulated in what we call a range object.

Crucially, the range object *doesn't hold all its numbers simultaneously*—it delivers numbers *upon request*.

**range Function Arguments:**  
The `range()` function is flexible depending on the number of arguments:

* `range(end)`: Generates numbers from `0` up to, but not including, `end`.  
    _Example:_ `list(range(3))` results in `[0, 1, 2]`
* `range(start, end)`: Generates numbers from `start` up to, but not including, `end`.  
    _Example:_ `list(range(1, 3))` results in `[1, 2]`
* `range(start, end, step)`: Generates numbers from `start`, incremented by `step`, up to, but not including, `end`.  
    _Example:_ `list(range(1, 6, 2))` results in `[1, 3, 5]`
* A negative `step` value makes the range decrement:  
    _Example:_ `list(range(6, 1, -1))` results in `[6, 5, 4, 3, 2]`

 **Iterating over Ranges:**  The `for` loop is the standard way to iterate over a range object.

**enumerate Function:**  Used during iteration to track both the element and its position (index) in a sequence. It returns an iterable of tuples: `(index, element)`. Tuple unpacking is a common way to handle these tuples. This function accepts an iterable and returns a new iterable. Each element of the new iterable is a tuple that contains an index number and the original element.

```python
colors = ["red", "green", "blue"]
for idx, color in enumerate(colors):
    print(f"Color {color} is at index {idx}.")

#Color red is at index 0.
#Color green is at index 1.
#Color blue is at index 2.
```

**Range Attributes and Methods:**
* `range.count(value)`: Returns how many times a specific value appears in the range (always 0 or 1).
* `range.index(value)`: Returns the index within the range of the given value. Raises `ValueError` if the value is not in the range.
* `range.start`, `range.stop`, `range.step`: Attributes containing the values used during range creation.


### Working with Strings

**Strings as Sequences:**  Python strings are sequences of characters and share properties/methods with other sequence types (indexing, slicing, length, iteration).


**Common String Methods:**
* `str.index(sub[, start[, end]])`: Searches for a substring and returns the lowest index where found. Raises `ValueError` if not found.
* `str.find(sub[, start[, end]])`: Searches for a substring and returns lowest index where found, or `-1` if not found.
* `str.count(sub[, start[, end]])`: Returns the number of non-overlapping occurrences of a substring.
* All three support optional `start` and `end` arguments to confine the search.
* `str.replace(old, new[, count])`: Substitute occurrences of `old` with `new`. Optional `count` limits replacements.
* `str.upper()` and `str.lower()`: Convert all characters to uppercase or lowercase.
* `str.casefold()`: Internationalized version of `lower()`, designed for case-insensitive comparisons and Unicode. It's crafted to dismiss all variations in case, making it ideal for comparisons that are case-insensitive.

* `str.capitalize()`: Makes the first character uppercase and the rest lowercase.
* `str.swapcase()`: Inverts the case of each character (also internationalized).  
    _Note:_ Running `swapcase()` twice may not return the original string for some Unicode characters (e.g., `'Straße'`).
* `str.join(iterable)`: Concatenates strings from an iterable, using the string as a separator. All elements must be strings.
* `str.split(sep=None, maxsplit=-1)`: Splits a string into a list using a separator (defaults to whitespace). `maxsplit` limits splits. Splitting with an empty string raises `ValueError`.

**Whitespace Removal:**
* `str.strip([chars])`: Removes leading/trailing whitespace (or specified characters).
* `str.lstrip([chars])`: Removes leading whitespace (or specified characters).
* `str.rstrip([chars])`: Removes trailing whitespace (or specified characters).

**Checking String Content:**
* `str.startswith(prefix[, start[, end]])` and `str.endswith(suffix[, start[, end]])`: Check if a string starts/ends with a substring.
* `str.isalpha()`: Returns `True` if all characters are alphabetic.
* `str.isalnum()`: Returns `True` if all characters are alphanumeric.
* `str.isdigit()`: Returns `True` if all characters are digits.
* `str.isspace()`: Returns `True` if all characters are whitespace.

    _Note:_ These return `False` for empty strings and are internationalized (recognize Unicode).

**Conversion to String (`str()`):**  
The `str()` function converts various data types into their string representation by invoking the object's `__str__` method. This works for numbers, booleans, `None`, and collections. The `str` function is the go-to approach for converting various data types to their string representation.

**Iterating over Strings:**  Strings can be iterated character by character using `for` or `while` loops. The `for` loop is the more idiomatic approach.

Page Reference: [Working with Strings and Ranges](https://launchschool.com/lessons/1b66cd61/assignments/ec6f2031)

[Back to the top](#top)

***

## Working with Lists and Tuples

**Lists and Tuples are Fundamental Collection Types:** Lists and tuples as essential structures for holding multiple items in Python.

**Mutability is the Key Difference:** The defining characteristic separating lists and tuples is mutability.
* **Lists are mutable:** Their contents can be changed after creation.
* **Tuples are immutable:** Their content cannot be changed after creation.

### Working with Lists

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
  numbers.pop(2)  # 3
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


### Working with Tuples

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

### Conversions

* **Strings to Lists and Tuples:** Use the `list()` and `tuple()` functions.  
  **Example:**  
  ```python
  list("apple")   # ['a', 'p', 'p', 'l', 'e']
  tuple("banana") # ('b', 'a', 'n', 'a', 'n', 'a')
  ```

* **Tuples to Lists and Vice Versa:** Easily switch using `list()` and `tuple()`.  
  **Example:**  
  ```python
  fruits_list = ["apple", "banana", "cherry"]
  fruits_tuple = tuple(fruits_list)
  fruits_tuple  # ('apple', 'banana', 'cherry')
  ```

* **Dictionaries to Lists and Tuples:**  
  - **Extracting Keys:** Use the `.keys()` method, which returns a dynamic view object. Converting the view to a list or tuple creates a static snapshot.
    - _Dynamic view example:_  
      ```python
      book = {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965}
      key_view = book.keys()
      book['publisher'] = 'Chilton Books'
      key_view  # dict_keys(['title', 'author', 'year', 'publisher'])
      ```
    - _Static snapshot example:_  
      ```python
      book = {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965}
      key_list = list(book.keys())
      book['genre'] = 'Science Fiction'
      key_list  # ['title', 'author', 'year']
      list(book.keys())  # ['title', 'author', 'year', 'genre']
      ```
  - **Gathering Values:** Use the `.values()` method (dynamic), converting to list or tuple for a static snapshot.
    - **Example:**  
      ```python
      data = {'apple': 5, 'banana': 3, 'cherry': 8}
      list(data.values())  # [5, 3, 8]
      ```
  - **Gathering Items (Key-Value Pairs):** Use the `.items()` method for a view of key-value pairs as tuples. Converting to a list or tuple creates a static snapshot.
    - **Example:**  
      ```python
      data = {'apple': 5, 'banana': 3, 'cherry': 8}
      list(data.items())  # [('apple', 5), ('banana', 3), ('cherry', 8)]
      ```

For those instances when we wish to retain the connection between keys and values, the items method steps in.

* **Sets and Frozen Sets to Lists and Tuples:**  
  Use the `list()` and `tuple()` functions. Remember that the order of elements in the resulting list or tuple may vary due to the unordered nature of sets. Sorting may be necessary.
  - **Example:**  
    ```python
    fruits_set = {"apple", "banana", "cherry"}
    list(fruits_set)  # ["banana", "cherry", "apple"]
    ```
  - **Frozen sets are immutable versions of sets and can also be converted:**  
    ```python
    fruits_frozenset = frozenset(["apple", "banana", "cherry"])
    list(fruits_frozenset)  # ["banana", "apple", "cherry"]
    ```

### Iteration

Both lists and tuples can be iterated over using `for` loops. The `enumerate()` function is useful when you need both the index and the value during iteration.

**Example (List Iteration):**  
  ```python
  fruits = ["apple", "banana", "cherry"]
  for fruit in fruits:
      print(fruit)
  ```

**Example (Tuple Iteration):**  
  ```python
  colors = ("red", "green", "blue")
  for color in colors:
      print(color)
  ```

**Example (Iteration with enumerate):**  
  ```python
  fruits = ["apple", "banana", "cherry"]
  for index, fruit in enumerate(fruits):
      print(f"Index {index} has fruit: {fruit}")
  ```


### Key Takeaways

* Lists are the go-to for collections that need to be modified frequently.
* Tuples are suitable for collections where the contents should remain constant.
* Python provides a rich set of methods for working with lists, allowing for efficient manipulation.
* Tuple operations are more limited due to their immutability, but they support fundamental actions like counting and indexing.
* Conversions between different collection types are straightforward using built-in functions and methods.
* Dictionary views (`.keys()`, `.values()`, `.items()`) are dynamic, but conversions to lists or tuples create static copies.
* Both lists and tuples are iterable, and `enumerate` is a valuable tool for accessing both index and value during iteration.


Page Reference: [Working with Lists and Tuples](https://launchschool.com/lessons/1b66cd61/assignments/6992af5a)

[Back to the top](#top)

***

## Working with Dictionaries, Sets and Frozen Sets

### Dictionaries

**Key-Value Storage:**  Dictionaries store data as key-value pairs.  

**Value Data Types:**  Values can be any data type.

**Hashable Keys:**  Dictionary keys must be hashable and unique.

**Accessing Values:**   Values are retrieved using their corresponding keys.  
  ```python
  data['name']
  ```

**KeyError:**  Accessing a non-existent key raises a `KeyError`.

**Deleting Pairs:**  The `del` statement removes a key-value pair.  
  ```python
  del data['age']
  ```
Deleting a non-existent key raises a `KeyError`.

**Checking Key Existence:**  Use `key in d` and `key not in d`.  
  ```python
  'name' in data
  ```

**Copying:**    The `copy()` method creates a shallow copy.  
  ```python
  data_copy = data.copy()
  ```
 
Modifications to mutable values in a shallow copy are reflected in the original.

**Default Values:**
* `get()`: Fetches a value, returning a specified default if the key is not found.  
    ```python
    data.get('country', 'Serbia')
    ```
    > "`get` returns a default value which can be specified."
* `setdefault()`: If the key exists, returns the value; if not, adds the key with the default value.  
    ```python
    data.setdefault('country', 'Serbia')
    ```
    > "`setdefault` creates a new key/value pair in a dictionary with the given key and default value."  
    > "`setdefault` does not change its associated value. It returns the existing value..."

**Removing and Returning Values:**
* `pop()`: Removes and returns the value for a given key.  
    ```python
    city = data.pop('city')
    ```
    Raises `KeyError` if the key doesn't exist, unless a default value is provided as the second argument.
* `popitem()`: Removes and returns the last key-value pair as a tuple (insertion order maintained in Python 3.7+).  
    ```python
    last_item = data.popitem()
    ```
    Raises `KeyError` if the dictionary is empty.

**Merging Dictionaries:**
* `update()`: Merges one dictionary into another, overwriting values for overlapping keys.  
    ```python
    data.update(new_data)
    ```
    > "...if keys in the dictionary being updated overlap with keys in the dictionary passed to update, their values get overwritten."
* `|` (Merge Operator, Python 3.9+): Combines two dictionaries and returns a new dictionary.  
    ```python
    merged_data = data | new_data
    ```
* `|=` (Update Operator, Python 3.9+): Mutates the dictionary on the left.  
    ```python
    data |= new_data
    ```

 **Conversion:**   Iterables of key-value pairs can be converted to dictionaries using `dict()`.  
  ```python
  dict([['name', 'Srdjan'], ['city', 'Belgrade']])
  ```

### Sets

**Unordered Collection:**  Sets are unordered collections of unique objects.  

**No Duplicates:**  Sets are ideal for avoiding duplicates.

**Checking Value Existence:**   Use `value in s` and `value not in s`.  
  ```python
  'apple' in fruits
  ```

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

### Frozen Sets

**Immutable Sets:**  Frozen sets are immutable versions of sets.  

**No Modification After Creation:**  Once created, a frozen set cannot be modified (`add`, `remove`, `discard`, `pop`, `clear` are unavailable).

**Use Non-Mutating Methods:** Any non-mutating set method or operator can be used with frozen sets.

**Hashable Objects:** Useful when set-like behavior is needed for hashable objects (e.g., as dictionary keys).

**Conversion:**  
  The `frozenset()` function converts other sequences and collections to frozen sets.  
  ```python
  frozenset('apple')
  frozenset(['apple', 'banana'])
  ```


Page Reference: [Working with Dictionaries, Sets and Frozen Sets](https://launchschool.com/lessons/1b66cd61/assignments/cf779435)

[Back to the top](#top)

***

## Unpacking Iterables in Python

### Concatenating Iterables


**Python’s `+` Operator:**
* Allows concatenation of iterables of the same type (e.g., lists with lists, tuples with tuples).
* **TypeError** is raised when trying to directly concatenate iterables of different types (e.g., a list and a tuple).
* **Workaround:** Convert iterables to the same type before concatenating.

> "However, challenges arise when we try to concatenate heterogeneous data types, such as a list and a tuple: TypeError: can only concatenate list (not 'tuple') to list"

### The Unary `*` Operator for Unpacking

The unary asterisk (`*`) operator provides an elegant and efficient way to "unpack" the contents of an iterable. This operator expands the iterable into its individual elements.

```python
#With Lists
numbers = [1, 2, 3, 4]
tup1 = (5, 6)
tup2 = (7, 8)
joined_list = [*numbers, *tup1, *tup2]
print(joined_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

#With Tuples
numbers = [1, 2, 3, 4]
tup1 = (5, 6)
tup2 = (7, 8)
joined_tuple = (*numbers, *tup1, *tup2)
print(joined_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

#With Sets
joined_set = {*numbers, *tup1, *tup2}
print(joined_set)    # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

Function arguments in Python also benefit greatly from this unpacking technique.
```python
#Without the *

def test(num1, num2, num3):
    # do something

numbers = [1, 2, 3]
test(numbers[0], numbers[1], numbers[2])

#With the *
def test(num1, num2, num3):
    # do something

numbers = [1, 2, 3]
test(*numbers)
```

Nested unpacking is new since Python 3.8.
```python
def test(num1, num2, num3):
    # do something

numbers = [1, 2, 3]
test(*numbers)
```

> "This unpacking technique isn't just limited to lists. It can be used with tuples, sets, and even dictionaries (with a slight modification which we will see later)."

### Applications of the Unary `*` Operator

* **Merging Iterables of Different Types:**  
The `*` operator allows for easily merging lists, tuples, sets, and other iterables into a new iterable of a desired type (e.g., merging lists and tuples into a new list or tuple).
* **Passing Iterable Elements as Function Arguments:**  
  Instead of manually referencing each element of an iterable to pass as individual arguments to a function, the `*` operator can unpack the iterable and pass its elements directly.
* **Nested Unpacking (Python 3.8+):**  
  Python 3.8 introduced the capability for nested unpacking, allowing unpacking inner iterables within an outer iterable during assignment.
* **When Not to Use the `*` Operator:**  
  While powerful, the `*` operator should be used judiciously. For tasks where a more intuitive and recognizable built-in function exists (like converting a list to a set using `set()`), the built-in function is often preferred for readability and clarity.

> "Python, with its emphasis on clean and efficient code, offers a more elegant solution: the unary asterisk ( * ) operator. This operator can be visualized as a tool that 'unpacks' the contents of an iterable."

### The Unary `**` Operator for Dictionaries

The unary double-asterisk (`**`) operator is used for working with dictionaries.

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'd': 4}
```

However, the `**` operator can not only unpack, but it can be used for the opposite purpose to "collect" or "pack" values into a dictionary. You might see this being used in function arguments, especially when that function takes variable keyword arguments. We haven't learned about keyword arguments yet, so while we will show you a simple example of its usage, you don't have to understand the code at this point. In this example, we pass several keyword arguments into the profile function. Using `**kwargs` collects those keyword arguments into a dictionary that we can then reference by kwargs.

> "In Python programming, readability and clarity are of utmost importance. When you encounter multiple methods or techniques to accomplish a task, it's always prudent to choose the one that is more intuitive and straightforward, both for your future self and for others who might read or maintain your code."

### Applications of the Unary `**` Operator

* **Merging Dictionaries:**  
Merge the contents of multiple dictionaries into a new dictionary. If keys are duplicated, the last dictionary in the sequence provides the value for that key.

* **Packing Keyword Arguments:**  
The `**` operator can also be used in function definitions to "collect" variable keyword arguments into a dictionary, commonly seen as `**kwargs`.


### Key Takeaways

* Direct concatenation of different iterable types using the `+` operator is not supported in Python.
* The unary `*` operator unpacks the elements of an iterable, making them available as individual items.
* The `*` operator is useful for merging different iterable types and passing iterable elements as separate function arguments.
* Nested unpacking (Python 3.8+) allows for unpacking within unpacking during assignment.
* Readability and clarity are crucial in Python code; choose the most intuitive method for a task.
* The unary `**` operator is specifically for unpacking (and packing) dictionaries.
* `**` can merge dictionaries and collect keyword arguments in function definitions (`**kwargs`).


Page Reference: [Unpacking Iterables in Python](https://launchschool.com/lessons/1b66cd61/assignments/670b999b)

[Back to the top](#top)

***