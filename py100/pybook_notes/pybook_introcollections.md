# Introduction to Collecions

Collections are objects that contain zero or more member objects, often called elements. 
There are 3 main categories of collection: sequences, mappings, and sets.

Lists and tuples differ only in that lists are mutable; tuples are not. 
List literals use `[]`; tuple literals use `()`. The set collections differ similarly: 
sets are mutable; frozen sets are not.

Sequences are types that maintain an ordered collection of objects (also: elements 
or values) that can be indexed by whole numbers, starting at 0.

Lists and tuples are heterogeneous; they may contain different kinds of objects, 
including other sequences.

Ranges are homogenous; they always contain integers.

Strings are a form of sequence called a text sequence. They differ from ordinary sequences 
in several ways:

Strings are homogenous; all characters in a string are, um, characters.
Characters are not a distinct kind of object; they are merely strings of length 1.
A string's individual characters are not separate strings until you reference a character.
Strings are not actual collections since the characters inside the string aren't objects.

Sets are types that maintain an unordered collection of unique objects (also called 
elements or members). Unlike sequences, sets cannot be indexed. Unordered means no 
well-defined order exists for the objects in a set. In fact, the sets `{1, 2, 3}` and
`{3, 1, 2}` are equal since the order doesn't matter. By unique, we mean a set can not 
have duplicate members.

Python has two main built-in set types: sets and frozen sets. Regular sets are mutable; 
frozen sets are immutable. This is the only significant difference between the two.

Frozen sets and tuples are both immutable data structures in Python, meaning their 
contents cannot be changed after creation. However, they have some key differences:

1.  Order:
   •   Tuples maintain a specific order of elements and can be accessed by index.
   •   Frozen sets, like regular sets, are unordered collections. They don't support indexing.
2.  Duplicates:
   •   Tuples can contain duplicate elements.
   •   Frozen sets, like regular sets, only store unique elements. Duplicates are automatically removed.
3.  Usage:
   •   Tuples are typically used when you need an ordered, immutable sequence of elements.
   •   Frozen sets are used when you need an immutable set of unique elements.
4.  Creation:
   •   Tuples have a literal syntax using parentheses: (1, 2, 3)
   •   Frozen sets must be created using the frozenset() function: frozenset([1, 2, 3])
5.  Hashability:
   •   Both tuples and frozen sets are hashable, meaning they can be used as dictionary 
   keys or elements in other sets.

The choice between a frozen set and a tuple depends on your specific use case. If 
you need an ordered, immutable sequence that can contain duplicates, use a tuple. 
If you need an immutable collection of unique elements where order doesn't matter, 
use a frozen set.

Mappings are types that maintain an unordered collection of key/value pairs (also called 
elements or members). Unlike sequences, mappings are accessed by their keys, which usually 
are not numbers. While Python has several mapping types, the only one we'll meet in this 
book is the dictionary or dict type.

Dicts have the following characteristics:

Dicts are mutable.

The keys in a dict must be unique. Trying to add a duplicate key to a dict merely 
replaces the existing key's associated value. Keys must be "hashable" values. We won't 
define "hashable" right now. However, hashable values are usually (not always) immutable.
All built-in immutable types (numbers, strings, booleans, tuples, frozen sets, and None) 
are hashable and can be dict keys. The values in each key/value pair may be any object.

Python dicts maintain the insertion order of the pairs. Python guarantees it. Thus, you 
can iterate over the pairs in the same order they were inserted into the dictionary. 
They are unordered collections, however Python processes them in an ordered fashion. 

Sequence Constructors:

`str()`: Regardless of what you pass to `str`, it returns a string.

`range(start, stop, step)`

This constructor generates a sequence of integers between start and stop - 1 with an 
increment of step between each consecutive integer. You can use a negative step to 
generate a sequence in reverse order.

```python
r = range(5, 12, 2)
print(list(r))            # [5, 7, 9, 11]

r = range(12, 8, -1)
print(list(r))            # [12, 11, 10, 9]

r = range(12, 5, -2)
print(list(r))            # [12, 10, 8, 6]
```

The most important thing to observe here is that ranges never include the "stop" value, so the one before the stop value is the one printed. Furthermore, a negative step value counts downwards from the start to the stop value. Thus, the start value should typically be larger than the stop value when the step value is negative.You can create empty ranges by giving values where start >= stop when step is positive or start <= stop when step is negative. Empty ranges are often bugs.

`range(start, stop)`

When you omit the step argument, Python uses a default value of 1. Hence, 
range(start, stop) is identical to range(start, stop, 1).

`range(stop)`

When you omit the start argument, Python uses a default value of 0 for start. Hence, 
range(stop) is identical to range(0, stop, 1).