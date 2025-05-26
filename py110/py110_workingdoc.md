# PY110 Working Document

<a name="top"></a>

## Table of Contents

- [Introduction to Collections in Python](#introduction-collections-python)
- [Sequences](#sequences)

***

## Introduction to Collections in Python

A **collection** is a generic term that encompasses several container data types in Python. These containers hold multiple objects, which can be of varied types. The primary purpose of a collection is to store, retrieve, and manipulate data.

The key feature to remember about collections is that they can hold multiple elements. However, they don't necessarily maintain those elements in a particular order.

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

Page Reference:

[Introduction to Collections in Python](https://launchschool.com/lessons/1b66cd61/assignments/c3630f0c)


[Back to the top](#top)

### Sequences



Page Reference:

[Sequences](https://launchschool.com/lessons/1b66cd61/assignments/90b357b4)

***


[Back to the top](#top)