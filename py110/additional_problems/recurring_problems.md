# Reoccuring struggles with other PY110/PY119 problems

## Sorting with Extra Steps Part 1

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

<details>
<summary>Possible Solution</summary>

```python
def get_published_year(book):
    return int(book['published'])

sorted_books = sorted(books, key=get_published_year)
print(sorted_books)

```
</details>

## Sorting With Extra Steps, Part 2

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

<details>
<summary>Possible Solution</summary>

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

## Sorting with Extra Steps, Part 3

Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.

```python

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

#Expected result: [{'e': [8], 'f': [6, 10]}]
```

<details>
<summary>Possible Solution</summary>

```python
def list_is_even(number_list):
    return all(num % 2 == 0 for num in number_list)

def all_even(dictionary):
    return all(list_is_even(lst) for lst in dictionary.values())

result = [d for d in lst if all_even(d)]
```
</details>