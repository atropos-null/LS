# Data Types

What are the four primitive data types? Floats, Integers, Bools, and Strings. What four types of data sets are mutable? Lists, Dictionaries, Sets, and Functions.

A literal is any syntactic notation that lets you directly represent an object in source code. 

**Integers**: you can write the number without separators (123456789) or break up the number with underscores (123_456_789) _only prints with the use of a f string_. 

**Floats**: you can write the number with only a single decimal point (42348.912346) or break up the number with underscores (42_348.912_346). _only prints with the use of a f string_.

**Scientific Notation**: Note that `10**n`, where `n` is positive, represents a 1 followed by n zeros. Thus, `10**308` is a 1 followed by 308 zeros; a truly enormous number. On the other hand, `10**-n` is equivalent to the reciprocal of `10**n`, e.g., 1.0 / `10**n`. Thus, `10**-308` is a truly minuscule number.Scientific notation can be used in a statement:  

```python 
print(3.14e+20 / 2.72e-15)    # 1.1544117647058823e+35
```

Terms to remember, with regards to variables : **initialization**, **assignment**, **reassignment**.

What is the difference between text sequence and ordinary sequence?  Ordinary sequences contain zero or more objects, but a text sequence does not contain any objects: it simply contains the characters (or bytes) that make up the text sequence. Those characters or bytes are not objects; they are simply part of the value.

### `''`, `""`,  or `""" """` and `\`

Triple quotes are often used for multi-line strings and a special kind of comment 
The backslash, or escape character `\`, tells the computer that the next character isn't syntactic but is part of the string. Escaping a quote prevents Python from seeing it as the string's end.

### Raw string literals

String literals with an r prefix are raw string literals. Raw string literals don't recognize escapes, so you can use literal `\` characters freely.

Both of these print `C:\Users\Xyzzy`:
```python
print("C:\\Users\\Xyzzy")  # Each \\ produces a literal \
print(r"C:\Users\Xyzzy")  # raw string literal
```

**F-strings** enable an operation called string interpolation. String interpolation is a handy way to merge Python expressions with strings.
You may include as many `{expression}` substrings as needed in an f-string. 
If you need literal `{ or }` characters in an f-string, you can escape them by doubling 
the `{ and }` characters you want to use as literal characters:

```python
>>> number = 123456789
>>> print(f"{number:_}")
123_456_789

>>> number = 123456789
>>> print(f"{number:,}")
123,456,789
```

You can also write large integers like this: `1_987_654_321`

`None`: a way to express the absence of a value.  It can also indicate missing, unset, 
or unavailable data and may sometimes be an error indication. None is a literal whose 
value is the lone representative of the NoneType class.

Sequences represent an ordered collection of objects A sequence's objects can be accessed 
using a numeric index. In many other languages, the array is the best-known sequence type, 
but Python uses lists to fill the same role. 

List literals use square brackets `[]` surrounding a comma-delimited list of values, and they are mutable. Tuples use parentheses `()` and are immutable. To define a one-element tuple, you must place a comma after the element value.

### Range arguments

With one argument, the range starts from 0 and ends just before the argument.
With two arguments, the first argument is the starting point, while the second 
argument is one past the last number in the range. 

With three arguments, the 3rd argument is a step value. Thus, `range(1, 10, 2)` 
goes from 1 through 9 with a step of 2 between the numbers. On the other hand, 
`range(0, -5, -1)` goes from 0 through -4 with a step of -1. This results in a range 
that goes from the highest value to the lowest.

### Mappings, Dictionaries

Mappings represent an unordered collection of objects stored as key-value 
pairs. Each key (usually a string) provides a unique identifier for a specific object 
in the mapping. The value is the object associated with that key. Essentially, a Python 
dictionary is a collection of key-value pairs. Dictionaries, in particular, are unordered 
collections in which insertion order is preserved.

### Sets

Sets represent an unordered collection of unique objects; the objects are sometimes called 
the members of the set. Sets are similar to mappings, except instead of using keys and 
values, a set is simply a collection of immutable (and hashable, as mentioned above) 
objects.

There are two main set types: ordinary sets (class set) and frozen sets (class frozenset). 
Frozen sets are merely immutable sets. They also lack a literal syntax: you must use the 
`frozenset` function to create one.