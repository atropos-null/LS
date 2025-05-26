# PY110 Working Document

<a name="top"></a>

## Table of Contents

- [Introduction to Collections in Python](#introduction-collections-python)
- [Sequences](#sequences)

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

**Lists** in Python represent an ordered collection of objects, characterized by zero-based indexing and mutability. The objects in a list are ordered by their position, or index, starting from `0`. Each element in the list can be of any data type, offering flexibility in the kind of data a list can hold. To access a specific element, use its index:

```python 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])   # [2, 3, 4]
print(numbers[:4])    # [0, 1, 2, 3]
print(numbers[6:])    # [6, 7, 8, 9]
print(numbers[::2])   # [0, 2, 4, 6, 8] (every second element)
print(numbers[-1:1])  # [9]
print(numbers[-4:-1]) # [6, 7, 8]
```

Attempting to access an index outside the list's range will result in an `IndexError`.

Lists are mutable:

```python
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

**Tuples** are ordered collections of objects, similar to lists. However, unlike lists, tuples are immutable, meaning their content cannot be altered after creation. This makes them suitable for representing fixed collections of objects. To access a specific element, use its index:

```python
coordinates = (1, 2, 3, 4, 5, 6)
print(coordinates[0:2])   # (1, 2)
print(coordinates[3:])    # (4, 5, 6)
print(coordinates[::-1])  # (6, 5, 4, 3, 2, 1)
```

Trying to access an index outside the tuple's range results in an `IndexError`.

Tuples are immutable. 

```python
fruits = ("apple", "banana", "cherry")
fruits[0] = "strawberry" # TypeError: 'tuple' object does not support item assignment
```

### Strings

**Strings** represent sequences of characters. A string is an ordered collection of characters, used to store and represent text-based information. Like tuples, strings are immutable. To access a specific element, use its index. As with lists and tuples we can use negative indexes:

```python
text = "Python Programming"
print(text[0:6])      # "Python"
print(text[7:])       # "Programming"
print(text[::-1])     # "gnimmargorP nohtyP" (reversed)
print(text[::2])      # "Pto rgamn" (every second character)
```

Trying to access an index outside the string's range results in an `IndexError`.

Strings, like tuples, are immutable which means you cannot modify a string's value. However, you can replace a string's value with a completely new string by using reassignment:

```python
greeting = "Hello, World"
greeting[7] = "m" #TypeError: 'string' object does not support item assignment

#Or:

greeting = "Hello, World"
print(greeting) #Hello, World
greeting = "What's up, Doc?"
print(greeting) = What's up, Doc?
```

Page Reference: [Sequences](https://launchschool.com/lessons/1b66cd61/assignments/90b357b4)

Further References:

[Barczykowska, E. (2024, November 26). Python notes: Slicing — Part 1 - Level Up Coding. Medium.](https://medium.com/gitconnected/python-notes-slicing-part-1-73209d5cbb02)

[Barczykowska, E. (2024b, November 27). Python notes: Slicing — Part 2 - Level Up Coding. Medium.](https://medium.com/gitconnected/python-notes-slicing-part-2-41f2e95ebef5)


[Back to the top](#top)
***