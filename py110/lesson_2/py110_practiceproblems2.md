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

```python
reverse_sorted = sorted(lst, reverse=True)
print(reverse_sorted)

regular_sorted = sorted(lst)
print(regular_sorted)
```

## Practice Problem 2

Repeat the previous exercise but, this time, perform the sort by mutating the original list.

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]

#Expected result

[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
```

Answer:

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst.sort()              #[-16, -6, 7, 8, 9, 10, 11, 50]

lst.sort(reverse=True)  #[50, 11, 10, 9, 8, 7, -6, -16]
```

## Practice Problem 3

Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]

[-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
[9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort
```

Answer:

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst.sort(key=str)
print(lst)      #[-16, -6, 10, 11, 50, 7, 8, 9]

lst.sort(key=str, reverse=True)
print(lst)   #[9, 8, 7, 50, 11, 10, -6, -16]
```

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

```python
def get_published_year(book):
    return int(book['published'])

sorted_books = sorted(books, key=get_published_year)
print(sorted_books)
```

# Practice Problems: Nested Data Structures

## Practice Problem 1

For each object shown below, demonstrate how you would access the letter `g`.

```python
lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]] 

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

```

Answer:

List 1: `lst1[2][1][3]`
List 2: `lst2[1]['third'][0]`
List 3: `lst3[2]['third'][0][0]]`
Dict 1: `dict1['b'][0][1]`
Dict 2: `list(dict2['3rd'].keys())[0]`

## Practice Problem 2

For each of these collection objects, demonstrate how you would change the value `3` to `4`.

```python
lst1 = [1, [2, 3], 4]

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

dict1 = {'first': [1, 2, [3]]}

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
```

Answer:

List 1: `lst1[1][1] = 4`

List 2: `lst2[2] = 4`

Dict 1: `dict1['first'][2][0] = 4`

Dict 2: `dict2['a']['a'][2] = 4`

## Practice Problem 3

Given the following code, what will the final values of `a` and `b` be? Try to answer without running the code.

```python
a = 2
b = [5, 8]
lst = [a, b] #lst = [2, [5,8]]

lst[0] += 2  #lst = [4, [5,8]] 
lst[1][0] -= a #lst = [4, [3,8]] 'a' is not the a in the list but the variable integer a above.
```

Answer: `lst = [4, [3,8]]`


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

```python

names = list(munsters.keys())
for name in names:
    age, gender = list(munsters[name].values())
    print(f"{name} is a {age}-old {gender}")

#other option:

for name, info in munsters.items():
    print(f"{name} is a {info['age']}-year-old {info['gender']}.")
```

# Practice Problems: Comprehensions

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

With comprehensions:
```python
all_male_ages = [member['age'] for member in munsters.values()
                               if member['gender'] == 'male']

print(sum(all_male_ages))     # 444
```


