# Practice Problems: Sorting

## Practice Problem 1

Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate the list.

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]

#Expected result

[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
```

Answer:

<details>
<summary>Show answer</summary>

```python
reverse_sorted = sorted(lst, reverse=True)
print(reverse_sorted)

regular_sorted = sorted(lst)
print(regular_sorted)
```
</details>

## Practice Problem 2

Repeat the previous exercise but, this time, perform the sort by mutating the original list.

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]

#Expected result

[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
```

Answer:

<details>
<summary>Show answer</summary>

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst.sort()              #[-16, -6, 7, 8, 9, 10, 11, 50]

lst.sort(reverse=True)  #[50, 11, 10, 9, 8, 7, -6, -16]
```
</details>

## Practice Problem 3

Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]

[-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
[9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort
```

Answer:

<details>
<summary>Show answer</summary>

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst.sort(key=str)
print(lst)      #[-16, -6, 10, 11, 50, 7, 8, 9]

lst.sort(key=str, reverse=True)
print(lst)   #[9, 8, 7, 50, 11, 10, -6, -16]
```
</details>

## Practice Problem 4

How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?

```python
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
```

Answer:

<details>
<summary>Show answer</summary>

```python
def get_published_year(book):
    return int(book['published'])

sorted_books = sorted(books, key=get_published_year)
print(sorted_books)
```
</details>

# Practice Problems: Nested Data Structures

## Practice Problem 1

For each object shown below, demonstrate how you would access the letter `g`.

```python
lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

lst2 = [{
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
```

Answer:

<details>
<summary>Show answer</summary>

List 1: `lst1[2][1][3]`  
List 2: `lst2[1]['third'][0]`  
List 3: `lst3[2]['third'][0][0]]`  
Dict 1: `dict1['b'][0][1]`  
Dict 2: `list(dict2['3rd'].keys())[0]`
</details>

## Practice Problem 2

For each of these collection objects, demonstrate how you would change the value `3` to `4`.

```python
lst1 = [1, [2, 3], 4]

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

dict1 = {'first': [1, 2, [3]]}

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
```

Answer:

<details>
<summary>Show answer</summary>

List 1: `lst1[1][1] = 4`  
List 2: `lst2[2] = 4`  
Dict 1: `dict1['first'][2][0] = 4`  
Dict 2: `dict2['a']['a'][2] = 4`
</details>

## Practice Problem 3

Given the following code, what will the final values of `a` and `b` be? Try to answer without running the code.

```python
a = 2
b = [5, 8]
lst = [a, b] #lst = [2, [5,8]]

lst[0] += 2  #lst = [4, [5,8]] 
lst[1][0] -= a #lst = [4, [3,8]] 'a' is not the a in the list but the variable integer a above.
```

Answer:

<details>
<summary>Show answer</summary>

`lst = [4, [3,8]]`
</details>

## Practice Problem 4

One of the most frequently used real-world string operations is that of "string substitution," where we take a hard-coded string and modify it with various parameters from our program.

Given the object shown below, print the name, age, and gender of each family member:

```python
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

#Expected:

'Herman is a 32-year-old male.'
'Lily is a 30-year-old female.'
'Grandpa is a 402-year-old male.'
'Eddie is a 10-year-old male.'
'Marilyn is a 23-year-old female.'
```

Answer:

<details>
<summary>Show answer</summary>

```python
names = list(munsters.keys())
for name in names:
    age, gender = list(munsters[name].values())
    print(f"{name} is a {age}-old {gender}")

#other option:

for name, info in munsters.items():
    print(f"{name} is a {info['age']}-year-old {info['gender']}.")
```
</details>

# Practice Problems: Comprehensions

## Problem 1 

Consider the following nested dictionary:

```python
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
```

Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

The result should be 444.

With for loop:
<details>
<summary>Show answer</summary>

```python
sum_ages = 0
names = list(munsters.keys())
for name in names:
    age, gender = list(munsters[name].values())
    if gender == 'male':
        sum_ages += age
print(sum_ages)

#Optimized:

total_male_age = 0
for member in munsters.values():
    if member['gender'] == 'male':
        total_male_age += member['age']

print(total_male_age)         # 444
```
</details>

With comprehensions:
<details>
<summary>Show answer</summary>

```python
all_male_ages = [member['age'] for member in munsters.values()
                               if member['gender'] == 'male']

print(sum(all_male_ages))     # 444
```
</details>

## Problem 2

Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order. Use a comprehension if you can. (Try using a for loop first.)

```python
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
```

Expected Result: `[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]`

Answer:

<details>
<summary>Show answer</summary>

```python
new_list = [sorted(element) for element in lst]
print(new_list)
```
</details>

## Problem 3

Given the following data structure, write some code that uses comprehensions to define a dictionary where the key is the first item in each sublist, and the value is the second.

```python
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# Expected Result, Pretty printed for clarity
{
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}
```

Answer:

<details>
<summary>Show answer</summary>

```python
#For Loop:
empty = {}
for element in lst:
    empty[element[0]] = element[1]
print(empty)

#Comprehension:
dictie = {element[0]: element[1] for element in lst}
```
</details>

## Practice Problem 5

Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list. 

Note that the first sublist has the odd numbers 1 and 7; the second sublist has odd numbers 1, 5, and 3; and the third sublist has 1 and 3. Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list is as shown below.

```python
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

#Expected Result:
[[1, 8, 3], [1, 6, 7], [1, 5, 3]]
```

Answer:

<details>
<summary>Show answer</summary>

```python
def sum_of_odd_numbers(sublist):
    odd_numbers = [num for num in sublist if num % 2 != 0]
    return sum(odd_numbers)

sorted_list = sorted(lst, key=sum_of_odd_numbers)
print(sorted_list)
```
</details>

## Practice Problem 6

Given the following data structure, return a new list identical in structure to the original but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension if you can.

```python
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

#Expected Result:
[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
```

Answer:

<details>
<summary>Show answer</summary>

```python
new_list = [{key: value + 1 for key, value in dictionary.items()}
                            for dictionary in lst]
```
</details>

## Practice Problem 7

Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.

```python
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

#Expected Result: [[], [3, 12], [9], [15, 18]]
```

Answer:

<details>
<summary>Show answer</summary>

```python
new_lst = [[value for value in sublst if value % 3 == 0] for sublst in lst]
```
</details>

## Practice Problem 8

Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

```python
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

#Expected Result: [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
```

Answer:

<details>
<summary>Show answer</summary>

```python
def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

result = [transform_item(item) for item in dict1.values()]
print(result)
```
</details>

## Practice Problem 9

Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.

```python
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

#Expected result: [{'e': [8], 'f': [6, 10]}]
```

Answer:

<details>
<summary>Show answer</summary>

```python
def list_is_even(number_list):
    return all(num % 2 == 0 for num in number_list)

def all_even(dictionary):
    return all(list_is_even(lst) for lst in dictionary.values())

result = [d for d in lst if all_even(d)]
```
</details>

## Practice Problem 10

A UUID (Universally Unique Identifier) is a type of identifier often used to uniquely identify items, even when some of those items were created on a different server or by a different application. That is, without any synchronization, two or more computer systems can create new items and label them with a UUID with no significant risk of stepping on each other's toes. It accomplishes this feat through massive randomization. The number of possible UUID values is approximately 3.4 X 10E38, which is a huge number. The chance of a conflict, a "collision", is vanishingly small with such a large number of possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string. The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Write a function that takes no arguments and returns a string that contains a UUID.

Answer:

<details>
<summary>Show answer</summary>

```python
import random

def generate_uuid():
    hex_chars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

# Outputs shown below are samples - you output will vary
print(generate_uuid())  # '02e51c2f-dacd-c319-53b5-e40e6e8c1f78'
print(generate_uuid())  # '39038ab9-3b95-43d8-6959-5d785ccb9b69'
print(generate_uuid())  # 'f7d56480-c5b2-8d4d-465f-01a4ea605729'
```
</details>

## Practice Problem 11


The following dictionary has list values that contains strings. Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.

Answer:

<details>
<summary>Show answer</summary>

```python
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = ['a','e','i','o','u']
empty = []
for key, value in dict1.items():
    for word in value:
        for char in word:
            if char in vowels:
                empty.append(char)
print(empty)

list_of_vowels = [char for key, value in dict1.items() for word in value for char in word if char in vowels]
print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

```
</details>