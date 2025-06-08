# Practice Problems

### Practice Problem 1

Given the tuple:

`fruits = ("apple", "banana", "cherry", "date", "banana")`

How would you count the number of occurrences of "banana" in the tuple?

```python
fruits = ("apple", "banana", "cherry", "date", "banana")
number_bananas = fruits.count('banana')
print(number_bananas)
```

### Practice Problem 2

Consider this set:
```python
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers))
```

What is the set's length?
Answer: 5. Duplicates are ignored.


### Problem 3:

Given two sets, how would you obtain a set that contains all the unique values from both sets?

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a | b
print(c) # {1, 2, 3, 4, 5, 6}
```

### Practice Problem 4

Given the following code, what would the output be? 

```python
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)
```

Answer: `{"Fred": 0, "Barney": 1, "Wilma": 2, "Betty": 3, "Pebbles": 4, "Bambam" : 5}`

### Practice Problem 5

Calculate the total age given the following dictionary:

```python
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}
```

Answer: 6174

```python
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total = sum(ages.values())
print(total)
```

### Practice Problem 6

With the above, find out the minimum age:

```python
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

minimum = min(ages.values())
print(minimum)
```

Answer: 10

### Practice Problem 7

What would the following code output? Try to answer without running the code.

```python
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words) 
```

Answer: ['bear']

### Practice Problem 8

Given the following string, create a dictionary that represents the frequency with which each letter occurs. The frequency count should be case-sensitive:

`statement = "The Flintstones Rock"`

Answer: 

```python
statement = "The Flintstones Rock"
working_dict = {}

for char in statement:
    total = statement.count(char)
    if char.isspace():
        continue
    working_dict[char] = total

print(working_dict)
```

### Practice Problem 9

What is the return value of the list comprehension below? Try to answer without running the code.

```python
[num for num in [1, 2, 3] if num > 1]
```
Answer: [2, 3]

### Practice Problem 10

What does the following code print and why?
```python
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())
```

Answer: `{'b': 'bear'}`. When no index is passed to popitem, it removes the last of the sequence and returns it.

### Practice Problem 11

What does the following code return? Try to answer without running the code.

``` python
lst = [1, 2, 3, 4, 5]
lst[:2]
```
Answer: `[1,2]` as it is a slice that only includes the first two elements at index 0 and 1.


### Practice Problem 12

What would be the output of the below code? Try to answer without running the code.

```python
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)
```

Answer = `[1, 2, 3, 4, 5]`. A frozen set is frozen an attempting to add a new element would not be accepted, thus throwing an `AttributeError`. 