# Using Collections

### Indexing

Indexing is the process of using a whole number to access and perhaps alter an element of 
a sequence. All sequences, including strings, support indexing. Python uses index `0` as the first element of all built-in sequences. 

The `len` function can determine a sequence's length. You can use its return value to determine whether an index is out of range:

```python
seq = ('a', 'b', 'c')
if len(seq) > 3:
    print(seq[3])
```

Suppose we want to access the last element in a sequence? To do that, we can compute the index of the last element and then use that value:

```python
seq = ('a', 'b', 'c')
last_index = len(seq) - 1
print(seq[last_index])        # c
```

### Slicing

The indexing syntax also supports a slicing augmentation. Slicing can extract (or modify) 
any number of consecutive elements simultaneously.

```python
seq = 'abcdefghi'
print(seq[3:7])       # defg
print(seq[-6:-2])     # defg
print(seq[2:8:2])     # ceg

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[3:3])       # []
print(seq[:])         # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[::-1])      # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

The syntax `seq[start:stop]` retrieves the elements from seq whose index is between start 
and stop - 1, inclusive. You can also use negative indexes for the slice. 
Finally, you can use the `seq[start:stop:step]` syntax to slice every "step-th" element.

### Key-Based Access

Indexing uses whole numbers and only works with sequences and strings. However, mappings 
use a syntax called key-based access that looks like indexing. This is when you use the key
in a key/value pair as the "index" or the ...key... We get a `KeyError` if we try to use a 
non-existent key. Keys must be immutable, but values can be mutable.

If there's a chance you might get a `KeyError`, consider using the dict.get method. It returnsthe value associated with a given key if the key exists. 

Can assign a new value to a key:
```python
my_dict['xyz'] = 'Hey there!'
print(my_dict['xyz'])    
```

### Common Collection Operations, Non-Mutating Operations for Collections

`in/not in`: Returns True or False

```python
seq = [4, 'abcdef', (True, False, None)]
print(4 in seq)                         # True
print(4 not in seq)                     # False
print('abcdef' in seq)                  # True
print('abcdef' not in seq)              # False
```

`min/max`: `min` and `max` return the minimum and maximum members in an iterable collection. The only requirement is that any pair of the collection's elements are comparable with the `<` and `>` operators. You can also use min and max with multiple arguments instead of an iterable.

The `sum` function is used in conjunction with iterable collections that consist entirely 
of numeric values. It computes and returns the sum of all the collection's numbers.
Despite what Python's official documentation says, **sum cannot be used with strings**. 
It only works with numeric types. Use `str.join` if you want to concatenate strings.

Two helpful sequence methods are the `index` and `count` methods. `seq.index` returns the index of the first element in the sequence that matches a given object. It raises a `ValueError`  exception if the object is not found. `seq.count` returns the number of times a value occurs in the sequence. `index` also works with strings. It searches for the first matching substring of a string.

### Merging Collections

One of the most impressively helpful functions is `zip`, which works with all iterables. It lets you merge the members of multiple iterables into a single list of tuples. `zip` makes it easy to iterate through many collections simultaneously.

`zip` iterates through 0 or more iterables in parallel and returns a list-like object of 
tuples. Each tuple contains a single object from each of the iterables.

```python
iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]
```

``` python
zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables))
# Pretty printed for clarity
# [
#   (1, 'Kim', None),
#   (2, 'Leslie', True),
#   (3, 'Bertie', False)
# ]
```

Note that we referred to zips return value as a list-like object. It's not a true list, 
but a lazy sequence much the same as a range. You must request values explicitly, which 
you can do with a loop or iterable constructor. That's why we call `list(zipped_iterables)` on line 6 above.

`zip`'s collection arguments are usually the same length but don't have to be. If you want 
to enforce identical lengths, add a `strict=True` keyword argument to the invocation.

The `zip` function's canonical application is to simultaneously iterate over multiple collections.

It's worth noting that `zip` returns what is known as an iterator. We'll discuss iterators 
in more detail in the Core curriculum. However, one characteristic of iterators that is 
important to be aware of is that they can only be consumed once. If you iterate over the 
iterator object, subsequent attempts to iterate will fail.

### Operations on Dictionaries

Python provides 3 methods to get lists of the keys, values, and key/value pairs from a dictionary. Those methods are `dict.keys`, `dict.values`, and `dict.items`.

The lists produced by these methods aren't ordinary lists. Python wraps the output for each list with `dict_keys()`, `dict_values()`, `or dict_items()` to show that these aren't regular lists. They are actually dictionary view objects that are tied to the dictionary. If you add a new key/value pair to the dictionary, remove an element, or update a value, the corresponding lists are updated immediately.

####Updating a dictionary in code: 

```python
people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

keys = people_phones.keys()
values = people_phones.values()

print(keys)    # dict_keys(['Chris', 'Pete', 'Clare'])
print(values)  # dict_values(['111-2222', '333-4444', '555-6666'])

people_phones['Max'] = '123-4567'
people_phones['Pete'] = '345-6789'
del people_phones['Chris']

print(keys)    # dict_keys(['Pete', 'Clare', 'Max'])
print(values)
# dict_values(['345-6789', '555-6666', '123-4567'])
```

#### To add a dictionary to another dictionary:

The `update(`) method in Python is used with dictionaries and sets to update the content 
of the dictionary or set with elements from another dictionary, set, or an iterable of 
key-value pairs or elements.

```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)
print(ages)
```

### Useful for lists:

#### Adding to a list: append(), insert(), extend()

`seq.append` appends a single object to the end of a mutable sequence, such as a list

`seq.insert` inserts an object into a mutable sequence before the element at a given index. If the given index is greater than or equal to the sequence's length, the object is appended to the sequence. If the index is negative, it is counts from the end of the sequence.

```python
numbers = [1, 2]
numbers.insert(0, 8)    # Insert 8 before numbers[0]
numbers.insert(2, 6)    # Insert 6 before numbers[2]
numbers.insert(-3, 33)  # Insert 33 before the 3rd element from the end.
```

`seq.extend` appends the contents of an iterable sequence to the calling iterable sequence.

One can also use the `+` operator to concatenate two lists. This operation merges 
the second list into the first one, producing a new combined list.

```python
print([1, 2, 3] + [4, 5])
[1, 2, 3, 4, 5]
```

### Deleting from list: remove(), pop(), clear()

`seq.remove` searches a sequence for a specific object and removes the first occurrence of 
that object. It raises a `ValueError` if there is no such object.

`seq.pop` removes and returns an indexed element from a mutable sequence. If no index is 
given, it removes the last element in the sequence. It raises an error if the index is 
out of range. pop only works with mutable indexed sequences.Remember, it removes by the index. If you want to use by the value itself, use `remove`.


```python
my_list = [2, 4, 6, 8, 10]
print(my_list.pop(1))         # 4
print(my_list.pop())          # 10
```

`seq.clear` removes all elements from a sequence, leaving it empty.

`del` and `pop()` in Python are not equivalent, but they can be used to achieve similar 
results in some cases. del is a statement used to delete an item from a list or a 
variable entirely. For example, `del my_list[2]` would remove the item at index 2 from 
`my_list`. 

`pop()` is a method that removes an item from a list and returns it. For example, 
`my_list.pop(2)` would remove the item at index 2 from `my_list` and `return` it.

If you need to remove an item and use it later, `pop()` is the way to go. If you just 
want to remove an item and don’t need to use it, `del` is a good choice.

#### Sorting: both mutable and immutable

There's `sort()` which does mutate the list. There's also `sorted(my_list)` but its more 
memory intensive. 

`sort` and `sorted` do an ascending sort using the `<` operator to compare elements from the collection. You can reverse the `sort` by adding a `reverse=True` keyword argument to the argument list.

You can also pass a `key=func` keyword argument to tell sort or sorted how to determine 
what values it should sort. **For instance, if you want to perform a case-insensitive sort 
on a list of strings, you can specify `key=str.casefold`**:

```python
words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))
# ['123', 'DEF', 'abc', 'xyz']
print(sorted(words, key=str.casefold))
```

In most cases, you can also use `str.lower` instead of `str.casefold`. However, **using 
`str.casefold` is considered best-practice since sort will be comparing the strings**.

Sort a list of numeric-valued strings by passing `key=int` to the function or method.

Using `sorted` on a dictionary returns a sorted list of the dictionaries keys.

#### Reverse Card!

You can use the `reversed` function to reverse the order of elements in a sequence or dictionary. The returned value is a lazy sequence that contains the elements in the sequence or the keys from a dictionary. Since the result is lazy, you need to iterate over the result or expand it with a function list list or tuple.

For example, trying to just `reverse` creates a problem. Have to throw it in a tuple which 
is also slow.

```python
names = ('Grace', 'Clare', 'Allison', 'Trevor')
reversed_names = reversed(names)
print(reversed_names)
# <reversed object at 0x102848e50>

print(tuple(reversed(names))) # Requires extra memory
# ('Trevor', 'Allison', 'Clare', 'Grace')
print(names)
```

Don't use `list.reverse` when you really need to reverse the list's contents, and 
don't need to preserve the original order. You should use `reversed` when all you need to do is iterate over the list in reverse. Don't use `reversed` if you eventually want to convert the result to a non-lazy sequence such as a list or tuple.

Think of the `reversed` function as a looping aid. You sometimes want to iterate over a collection in `reverse`. `reversed` makes that easy:

```python
names = ('Grace', 'Clare', 'Allison', 'Trevor')
for name in reversed(names):
    print(name)
# Trevor
# Allison
# Clare
# Grace
```

**There's no reversing strings, however. Just lists/tuples.**

```python
s = 'hello'
reversed_s = s[::-1]
print(reversed_s)  # Outputs: 'olleh'
```

`get()` method is used to retrieve the value for a given key from a dictionary. If the key 
is not present in the dictionary, the `get()` method returns a default value. By default, 
this value is `None`.

## STRING MFING Operations

`str.lower`: lowers everything
`str.upper`: RAISES EVERYTHING 
`str.capitalize`: Only first letter capitalized
`str.title`: First Letter Of Every Word Is Capitalized
`str.rjust`: right justification

`string.capwords()` is more reliable than titlecase

`str.swapcase`: everything = EVERYTHING, Everything = eVERYTHING 
`str.swapcase().swapcase()` = returns original string

`str.isalpha()` returns `True` if all characters of `str` are alphabetic, `False` otherwise. It returns `False` if the string is empty.

`str.isdigit()` returns `True` if all characters of str are digits, `False` otherwise. 
It returns `False` if the string is empty.

`str.isalnum()` returns `True` if str is composed entirely of letters and/or digits, `False` otherwise. It returns `False` if the string is empty.

`str.islower()` returns `True` if all cased characters in `str` are lowercase letters,`False` otherwise. It returns `False` if the string contains no case characters.

`str.isupper()` returns `True` if all cased characters in str are uppercase, `False` otherwise. It returns `False` if the string contains no case characters.

`str.isspace()` returns `True` if all characters in str are whitespace characters, `False` 
otherwise. It returns `False` if the string is empty. The whitespace characters include 
ordinary spaces (), tabs (`\t`), newlines (`\n`), and carriage returns (`\r`). It also includes two rarely used characters: vertical tabs (`\v`) and form feeds (`\f`), as well as some foreign characters that count as whitespace.

Be careful with these methods: they're all Unicode-aware. If you need to exclude non-ASCII characters, use this pattern: `text.isalpha()` and `text.isascii()`.

`str.strip` method returns a copy of `str` with all leading and trailing whitespace characters. `str.strip` can be fed arguments, but with some caveats. Only leading and trailing characters that match the argument are removed, and only individual characters, not substrings.

The `str.lstrip` method is identical to `str.strip` except it only removes leading characters (the leftmost). Similarly, `str.rstrip` removes trailing characters (the rightmost).

`str.startswith` returns `True` if the string given by str begins with a certain substring, `False` if it does not. The method also accepts "start" and "end" indexes to control where the search begins and ends. `startswith("substring", startindexnumber, endindexnumber)`

`str.endswith` returns `True` if the string given by `str` ends with a certain substring, 
`False` if it does not, and otherwise identical to `startswith`.

The `str.split` method returns a list of the words in the string `str`. By default, 
`split` splits the string at sequences of one or more whitespace characters. If you want 
to split on something other than spaces, you can tell Python what character or character 
string should act as a delimiter. Note that specifying a delimiter changes the splitting 
behavior. Instead of looking for runs of whitespace, it splits the string at every 
occurrence of the delimiter. This also applies when using a literal space character as 
the delimiter. It's worth noting that Python's differs from most others in that you can't 
split a string into individual characters using `split`. Python's `str.split` method doesn't allow a separator of ''. If you need to split a string into characters, use the list or tuple function and print that out or loop over it:

```python
text = 'abcde'
for char in text:
    print(char)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(list(alphabet))
```

`str.splitlines` returns a list of lines from the string `str`. `splitlines` looks for 
line-ending characters like `\n` (line feed), `\r` (carriage return), `\n\r` (new lines), and a variety of other line boundaries.

`str.join` which concatenates all strings in an iterable collection into a single lone 
string. Each string from the collection gets concatenated to the previous string with the 
value of `str` between them.

```python
words = ['You', 'were', 'lucky']
print(''.join(words))         # Youwerelucky
print(' '.join(words))        # You were lucky
print(','.join(words))        # You,were,lucky
print('\n  '.join(words))
# You
# were
# lucky
```

`str.find` searches through `str` looking for the first occurrence of the argument. `str.rfind` does the same, but it searches from right to left (that is, in reverse). Both methods return the index of the first matching substring. Otherwise, they return `-1`.

### Nested Collections:

Collections can be nested inside other collections. For instance, you can have a list 
that contains a dict, a set, a tuple, and another list. Each of those can, in turn, also 
contain nested collections. You can't nest a mutable collection such as a list, dictionary, or another set inside a set. However, you can nest a frozen set inside a set or frozen set.Curiously, you can nest mutable collections inside tuples even though tuples are immutable.

### Comparing Collections:

Equality is the most straightforward comparison. If two iterables meet all of the following requirements, they are equal. Otherwise, they are unequal. Can also do it with `!=`.

They have the same type: (list, tuple, set, etc.) Note that sets and frozen sets are 
considered the same for comparison purposes.

They have the same number of elements:

For sequences, each pair of corresponding elements compares as equal.
For sets, each set has the same members (order doesn't matter).
For mappings, each key/value pair must be present and identical in both mappings (order doesn't matter).

### String comparison, `lower` vs `casefold`:

When comparing strings in a case-insensitive manner, one might initially try to use the 
`str.lower` method, which converts all characters in a string to lowercase. While this 
method works for many use cases, there are some scenarios in which it doesn't account 
for all variations in character case.

The `str.casefold` method offers a more comprehensive approach to normalizing case than 
`str.lower`. It's primarily designed to facilitate case-insensitive string comparisons, 
especially in languages where conventional methods of converting to lowercase may fall 
short.

The `isinstance` function checks whether the first argument references an instance of the 
type given by the second argument.