# Loops and Iterating

`while` and `for` are the main loops. These loops execute a block repeatedly while a condition remains truthy. You can also think of the loop running until the condition becomes falsy. 

Good for use when you don't know how long it should loop for. 

``` python
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):  REMEMBER LINE 9
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']
```

### `for` Loops

A `for` loop lets you forget about indexing your sequences. You don't have to initialize or increment the index value or even need a condition. Moreover, for loops work on all built-in collections (including strings). Most loops you write in Python will be for loops.

Same as above now in `for`:

```python
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)
    # Deleted: index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']
```

Using a `for` loop with a dict iterates over the dict keys by default. If you want the values or pairs, you can request them with the values or items methods:

##### Looping over a dictionary

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

# Looping over a dictionary's values
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)

# Looping over a dictionary's key/value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in my_dict.items():
    print(item)
```

### Continue/Break

Python uses the keywords continue and break to provide more control over `for` and `while` 
loops. continue starts a new loop iteration; break terminates the loop early. `continue` is essentially a skip. But you can write looping logic without it. You don't have to use 
`continue`, however, it often leads to a more elegant solution to a problem. 
Without `continue`, your loops can get cluttered with nested conditional logic.

The `continue` statement tells Python to start the next iteration of the nearest enclosing 
loop. You can't start a new iteration of an outer loop if you're currently in an inner (nested) loop, which is why you need `break`.

Then there's `while True`:

```python
while True:
    # main loop code is here

    answer = input('Play again? (y/n) ')
    if answer == 'n':
        break
```

Simultaneous interation is occasionally made more helpful with the `zip` function.

```python
forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

zipped_names = zip(forenames, surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')
```

### Comprehensions for List, Set, and Dict

`[print(foo) for foo in collection]`

#### List Comprehesions

The most commonly used comprehensions are list comprehensions. They take an iterable 
collection and create a new list through iteration and optional selection. List 
comprehensions have the following format:

`[ expression for element in iterable if condition ]`

The expression in a comprehension often performs a **transformation**. It determines a new 
value based on an element from the original collection. When the `if` condition portion is present, we say that the comprehension also performs **selection**. With selections, it's not uncommon to return the original values from the collection:

```python
squares = [ number * number for number in range(5) ]
print(squares)      # [0, 1, 4, 9, 16]
```

Alternatively:

```python
squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)      # [0, 1, 4, 9, 16]
```

Comprehensions can also have multiple `for` loop components.

#### Dictionary Comprehensions

Dictionary comprehensions are almost identical to list comprehensions. However, they create new dictionaries instead of lists.

`{ key: value for element in iterable if condition }`

```python
squares = { f'{number}-squared': number * number
            for number in range(1, 6) }
print(squares)

# pretty-printed for clarity.
{
    '1-squared': 1,
    '2-squared': 4,
    '3-squared': 9,
    '4-squared': 16,
    '5-squared': 25
}
```

#### Set Comprehensions

Set comprehensions look almost identical to dict comprehensions. However, they create a 
new set instead of a dict and only have one expression to the left of the word for.

`{ expression for element in iterable if condition }`

```python
squares = { number * number for number in range(1, 6) }
print(squares)      # {1, 4, 9, 16, 25}
```

#### Why no Immutable Comprehensions?

Comprehensions don't build their results all at once. Each kind of comprehension 
works something like this:

```python
result = empty_collection               # [], {}, set()
for item in collection:
    result.append(item)
```

As you can see, our result starts as an empty collection. We then modify the result 
collection during each iteration by appending a new item to result. From this, it's clear 
that the result must be a mutable type. Tuples are immutable, so Python can't have tuple 
comprehensions.

Since ranges and strings are also immutable, comprehensions can't create them. If you must have a tuple or string, use the tuple or str constructors to convert a list comprehension's result into a tuple or string. This doesn't work for range.
