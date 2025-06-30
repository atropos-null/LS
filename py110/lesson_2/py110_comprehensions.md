# PY110 List Comprehension Problems

## Practice Problem 1

Given the following list of dictionaries, use a comprehension to create a new list containing only the names of 
people who are 18 or older.

```python
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30},
    {'name': 'Diana', 'age': 16},
    {'name': 'Eve', 'age': 22}
]
```

<details>
<summary>Show Solution</summary>

````python
#For Loop
new_list = []
for entry in people:
    if entry['age'] > 18:
        new_list.append(entry['name'])

#List Comprehension   
new_list = [entry['name'] for entry in people if entry['age'] > 18]
print(new_list)
````

</details>

Expected result: `['Alice', 'Charlie', 'Eve']`


## Practice Problem 2

Transform the following nested list so that each inner list contains only the even numbers, and each even number is squared.

Expected result: `[[4, 16], [36, 64], [100, 144]]`

```python
numbers = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```

<details>
<summary>Show Solution</summary>

````python
#For Loop
new_list = []
for sublist in numbers:
    evens = []
    for item in sublist:
        if item % 2 == 0:
            evens.append(item ** 2)
    new_list.append(evens)

#List Comprehension
new_list = [[item ** 2 for item in sublist if item % 2 == 0] for sublist in numbers]

print(new_list)
````

</details>

## Problem 3

Flatten the data structure into one structure. 

```python
data = [[[0, 1], []], [[2, 3, 4], [5], [6, 7]], [], [[8, 9]]]
```

We can do it without list comprehensions:

<details>
<summary>Show Solution</summary>

````python
lst = []
for sub in data:
    for subsub in sub:  
        for val in subsub:
            lst.append(val)
print(lst)
````

</details>

The order in the comprehension is the order you see here in the for loop. It goes from outermost to innermost. Literally, whatever the for loop would do in order, follow that in order. 

<details>
<summary>Show Solution</summary>

````python
new_lst = [val for sub in data for subsub in sub for val in subsub]
print(new_lst)
````

</details>


## Problem 4

Given the following dictionary, create a new dictionary where each key maps to a list of words from the original value that have more than 4 characters.

Expected result: `{'morning': ['quick', 'brown', 'jumps'], 'afternoon': ['sleeping'], 'evening': ['under', 'bright', 'starry']}`

```python
sentences = {
    'morning': 'the quick brown fox jumps',
    'afternoon': 'over the lazy dog sleeping',
    'evening': 'under the bright starry sky'
}
```

<details>
<summary>Show Solution</summary>

````python
def get_four(text):
    temp = []
    holding = text.split()
    for item in holding:
        if len(item) >= 4:
            temp.append(item)
    return temp

new_dict = {key: get_four(value) for key, value in sentences.items()}
````

</details>

## Problem 5

Given a list of words, create a dictionary where the keys are the words and the values are the lengths of those words, 
but only include words that start with a vowel.

```python
words = ['apple', 'banana', 'orange', 'grape', 'elephant', 'tiger']
```

<details>
<summary>Show Solution</summary>

````python
counts = {word: len(word) for word in words if word[0] in 'aeiou'}

#Expected result: {'apple': 5, 'orange': 6, 'elephant': 8}
````

</details>

## Problem 6

Transform the following dictionary to create a new dictionary where the keys remain the same, but the values are lists containing only the vowels from the original string values.

```python
data = {
    'first': 'hello world',
    'second': 'python programming',
    'third': 'launch school'
}

#Expected Result: {'first': ['e', 'o', 'o'], 'second': ['o', 'o', 'a', 'i'], 'third': ['a', 'u', 'o', 'o']}
```

<details>
<summary>Show Solution</summary>

```python
new_data = {key: [char for char in value if char in 'aeiou'] for key, value in data.items()}
```
</details>



## Problem 7 

Given the following nested structure, create a flat list of all the even numbers across all sublists.

```python
nested_nums = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9],
    [10, 11, 12, 13, 14]
]
```

<details>
<summary>Show Solution</summary>

```python
flat_list = [num for sublist in nested_nums for num in sublist if num % 2 == 0]

# Expected result: [2, 4, 6, 8, 10, 12, 14]
```
</details>

## Problem 8

Transform the following list of tuples into a list of dictionaries with keys 'name' and 'score', but only include entries where the score is above 75.

Expected result: `[{'name': 'Alice', 'score': 85}, {'name': 'Charlie', 'score': 91}, {'name': 'Eve', 'score': 88}]`

```python
student_scores = [
    ('Alice', 85),
    ('Bob', 72),
    ('Charlie', 91),
    ('Diana', 68),
    ('Eve', 88)
]
```

<details>
<summary>Show Solution</summary>

```python
#for loop

lst = []
for name, score in student_scores:
    if score > 75:
        my_dict = {"name": name, "score": score}
        lst.append(my_dict)
print(lst)


# Comprehension
higher_scores = [{"name": name, "score": score} for name, score in student_scores if score > 75 ]
print(higher_scores)
```
</details>

## Practice Problem 9

Transform the following list of lists so that each inner list is sorted, but only keep numbers that are greater than 5.

```python
data = [[8, 3, 12, 1], [15, 6, 2, 9], [7, 4, 11, 10]]
```
<details>
<summary>Show Solution</summary>

```python
#For Loop:
for sublist in data:
    new_sublist = []
    for element in sublist:
        if element > 5:
            new_sublist.append(element)
    new_data.append(sorted(new_sublist))


new_data = [sorted([number for number in sublist if number > 5]) for sublist in data]

#Expected result: [[8, 12], [6, 9, 15], [7, 10, 11]]
```
</details>

***

# Additional List Comprehensions Practice

## Basic List Comprehensions

1. **Square Numbers**  
   Create a list comprehension that squares all numbers from 1 to 10.  
   **Expected result:**  
   `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`

<details>
<summary>Show Solution</summary>

```python
nums = [num ** 2 for num in range(1,11)]
```
</details>

2. **Filter Even Numbers**  
   Given `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, create a list comprehension that returns only the even numbers.  
   **Expected result:**  
   `[2, 4, 6, 8, 10]`

<details>
<summary>Show Solution</summary>

```python
 evens = [num for num in numbers if num % 2 == 0]
```

</details>

3. **String Lengths**  
   Given `words = ['hello', 'world', 'python', 'code']`, create a list comprehension that returns the length of each word.  
   **Expected result:**  
   `[5, 5, 6, 4]`

<details>
<summary>Show Solution</summary>

```python
lengths = [len(word) for word in words]
```

</details>

---

## Intermediate List Comprehensions

4. **Conditional Transformation**  
   Create a list comprehension that takes numbers 1-20 and returns "even" for even numbers and "odd" for odd numbers.  
   **Expected result:**  
   `['odd', 'even', 'odd', 'even', ...]`

<details>
<summary>Show Solution</summary>

```python
description = ['even' if num % 2 == 0 else 'odd' for num in range(1,21)]
```

</details>

5. **Nested List Processing**  
   Given `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, create a list comprehension that returns all numbers greater than 5.  
   **Expected result:**  
   `[6, 7, 8, 9]`

<details>
<summary>Show Solution</summary>

```python
greater_than_5 = [item for sublist in matrix for item in sublist if item > 5]
```

</details>

6. **Dictionary Value Extraction**  
   Given this dictionary:  
   ```python
   students = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}
   ```
   Create a list comprehension that returns the names of students with grades above 80.  
   **Expected result:**  
   `['Alice', 'Bob', 'Diana']`

<details>
<summary>Show Solution</summary>

```python
greater_than_80 = [student for student, grade in students.items() if grade > 80]
```

</details>
---

## Advanced List Comprehensions

7. **String Processing**  
   Create a list comprehension that takes a sentence and returns a list of words with their vowels removed.  
   ```python
   sentence = "The quick brown fox jumps"
   ```
   **Expected result:**  
   `['Th', 'qck', 'brwn', 'fx', 'jmps']`

<details>
<summary>Show Solution</summary>

```python
#For Loop

no_vowels = []

for word in sentence.split():
    temp = []
    for char in word:
        if char not in 'aeiou':
            temp.append(char)
    string = "".join(temp)
    no_vowels.append(string)     
print(no_vowels)

#List Comprehension

ohne_vowels = ["".join([char for char in word if char not in 'aeiou']) for word in sentence.split()]
print(ohne_vowels)
```

</details>

8. **Nested Dictionary Processing**  
   Using the `munsters` dictionary from your practice problems:  
   ```python
   munsters = {
       'Herman': {'age': 32, 'gender': 'male'},
       'Lily': {'age': 30, 'gender': 'female'},
       'Grandpa': {'age': 402, 'gender': 'male'},
   }
   ```
   Create a list comprehension that returns the names of all female family members.  
   **Expected result:**  
   `['Lily']`

<details>
<summary>Show Solution</summary>

```python
women = []

#For Loop
for name, data in munsters.items(): #note that you have to give a label for the key ("name"), and a label for the values ("data")
    if data['gender'] == 'female': #then you use the label for the values, and then the specific known value. 
        women.append(name)
print(women)

#List comprehension
females = [name for name, data in munsters.items() if data['gender'] == 'female'] #items() shows up on the first line only
print(females)
```

</details>

9. **Multiple Conditions**  
   Create a list comprehension that returns numbers from 1-50 that are divisible by both 3 and 5.  
   **Expected result:**  
   `[15, 30, 45]`

<details>
<summary>Show Solution</summary>

```python
# For Loop
divisible_by3and5 = []
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        divisible_by3and5.append(i)
print(divisible_by3and5)

#List Comprehension
divis_by3and5 = [i for i in range(1,51) if i % 3 == 0 and i %5 == 0]
print(divis_by3and5)
```

</details>

10. **Flattening with Conditions**  
    Given `nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]`, create a list comprehension that flattens the list and keeps only odd numbers.  
    **Expected result:**  
    `[1, 3, 5, 7, 9]`

<details>
<summary>Show Solution</summary>

```python

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

#For Loop

odd_list1 = []
for sublist in nested_list:
    for element in sublist:
        if element % 2 != 0:
            odd_list1.append(element)

print(odd_list1) 

#List Comprehension

odd_list2 = [element for sublist in nested_list for element in sublist if element % 2 != 0]
print(odd_list2)
```

</details>
---

## Additional List Comprehensions

11. **Filter and Transform Strings**  
    Given `words = ['hello', 'world', 'python', 'programming', 'code']`, create a list comprehension that returns words longer than 4 characters, converted to uppercase.  
    **Expected result:**  
    `['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']`

<details>
<summary>Show Solution</summary>

```python
upper_4 = [word.upper() for word in words if len(word) > 4]
```

</details>

12. **Dictionary Keys with Conditions**  
    Using the munsters dictionary from your practice problems:  
    ```python
    munsters = {
        'Herman':  {'age': 32,  'gender': 'male'},
        'Lily':    {'age': 30,  'gender': 'female'},
        'Grandpa': {'age': 402, 'gender': 'male'},
        'Eddie':   {'age': 10,  'gender': 'male'},
        'Marilyn': {'age': 23,  'gender': 'female'},
    }
    ```
    Create a list comprehension that returns the ages of all family members over 25.  
    **Expected result:**  
    `[32, 30, 402]`

<details>
<summary>Show Solution</summary>

```python
#For Loop

ages_forloop = []
for name in munsters.values():
    if name['age'] > 25:
        ages_forloop.append(name['age'])
print(ages_forloop)

# List Comprehension

ages_listcomp = [name['age'] for name in munsters.values() if name['age'] > 25]
print(ages_listcomp)
```
</details>

13. **Nested List Selection**  
    Given `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, create a list comprehension that returns all even numbers from the matrix.  
    **Expected result:**  
    `[2, 4, 6, 8]`

<details>
<summary>Show Solution</summary>

```python
#For Loop

even = []
for sublist in matrix:
    for element in sublist:
        if element % 2 == 0:
            even.append(element)
print(even)

#List Comprehension

evens = [element for sublist in matrix for element in sublist if element % 2 == 0]
print(evens)
```
</details>

14. **String Method Chaining**  
    Create a list comprehension that takes the sentence `"The Quick Brown Fox Jumps"` and returns each word in lowercase.  
    **Expected result:**  
    `['the', 'quick', 'brown', 'fox', 'jumps']`

<details>
<summary>Show Solution</summary>

```python

sentence = "The Quick Brown Fox Jumps"

#For Loop

lowered1 = []
for word in sentence.split():
    lowered1.append(word.lower())
print(lowered1)

#List Comprehension

lowered2 = [word.lower() for word in sentence.split()]
print(lowered2)
```

</details>

15. **Range with Multiple Conditions**  
    Create a list comprehension that returns numbers from 1 to 30 that are divisible by 3 but not by 6.  
    **Expected result:**  
    `[3, 9, 15, 21, 27]`

<details>
<summary>Show Solution</summary>

```python
#For loop
wierd_nums1 = []

for i in range(1, 31):
    if i % 3 == 0 and i % 6 != 0:
        wierd_nums1.append(i)
print(wierd_nums1)

#List Comprehension

wierd_nums2 = [i for i in range(1, 31) if i % 3 == 0 and i % 6 != 0]
print(wierd_nums2)
```

</details>

16. **Dictionary Value Processing**  
    Given `grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96, 'Eve': 73}`, create a list comprehension that returns tuples of (name, grade) for students who scored above 80.  
    **Expected result:**  
    `[('Alice', 85), ('Bob', 92), ('Diana', 96)]`

<details>
<summary>Show Solution</summary>

```python
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96, 'Eve': 73}

#For Loop

above_avg = []
for key, value in grades.items():
    if value > 80:
        name = key
        score = value
        above_avg.append((key, score))
print(above_avg)

# List comprehension

above_average = [(key, score)for key, value in grades.items() if value > 80 ]
print(above_average)
```

</details>

17. **Multiple List Processing**  
    Given `numbers = [1, 2, 3, 4, 5]` and `letters = ['a', 'b', 'c', 'd', 'e']`, create a list comprehension that combines them into strings like "1a", "2b", etc.  
    **Expected result:**  
    `['1a', '2b', '3c', '4d', '5e']`

<details>
<summary>Show Solution</summary>

```python
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']

#For Loop
together = []
temp = list(zip(numbers, letters))
for tuple in temp:
    new_element = str(tuple[0]) + tuple[1]
    together.append(new_element)
print(together)

#List Comprehension

zusammen = [str(tuple[0]) + tuple[1] for tuple in list(zip(numbers,letters))]
print(zusammen)
```
</details>

18. **Conditional Expression in Comprehension**  
    Create a list comprehension that takes numbers 1-15 and returns "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, and the number as a string otherwise.  
    **Expected result:**  
    `['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']`

<details>
<summary>Show Solution</summary>

```python

#For Loop

fubar = []
for number in range(1, 16):
    if number % 3 == 0:
        fubar.append("Fizz")
    elif number % 5 == 0:
        fubar.append("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        fubar.append("FizzBuzz")
    else:
        fubar.append(str(number))
print(fubar)

# List Comprehension

fubarred = [
    "FizzBuzz" if number % 3 == 0 and number % 5 == 0
    else "Fizz" if number % 3 == 0
    else "Buzz" if number % 5 == 0
    else str(number)
    for number in range(1, 16)
]
print(fubarred)
```
</details>

19. **Nested Dictionary Extraction**  
    Given this data structure similar to your practice problems:  
    ```python
    people = {
        'person1': {'name': 'Alice', 'hobbies': ['reading', 'swimming']},
        'person2': {'name': 'Bob', 'hobbies': ['coding', 'gaming', 'reading']},
        'person3': {'name': 'Charlie', 'hobbies': ['music', 'dancing']}
    }
    ```
    Create a list comprehension that returns all unique hobbies.  
    **Expected result:**  
    `['reading', 'swimming', 'coding', 'gaming', 'music', 'dancing']`

<details>
<summary>Show Solution</summary>

```python
people = {
        'person1': {'name': 'Alice', 'hobbies': ['reading', 'swimming']},
        'person2': {'name': 'Bob', 'hobbies': ['coding', 'gaming', 'reading']},
        'person3': {'name': 'Charlie', 'hobbies': ['music', 'dancing']}
    }

# For Loop

hobbies = []
for hobby in people.values():
    for hobby in hobby['hobbies']:
        if hobby not in hobbies:
            hobbies.append(hobby)
print(hobbies)

#List comprehension

hobby_lobby = list({hobby for hobby in people.values() for hobby in hobby['hobbies']})
print(hobby_lobby)
```

</details>

20. **String Index Processing**  
    Create a list comprehension that takes the string `"programming"` and returns a list of tuples containing each character and its index position.  
    **Expected result:**  
    `[('p', 0), ('r', 1), ('o', 2), ('g', 3), ('r', 4), ('a', 5), ('m', 6), ('m', 7), ('i', 8), ('n', 9), ('g', 10)]`


<details>
<summary>Show Solution</summary>

```python
string = 'programming'

#For Loop

tuppy = []
for char, position in enumerate(string):
    new_tup = position, char
    tuppy.append(new_tup)
print(tuppy)

#List Comprehension
tupps = [(position, char) for char, position in enumerate(string)]
print(tupps)
```

</details>

## Nested Dictionary Structures

### Problem 1: Basic Value Extraction

Data Structure:
```python
students = {
    'Alice': {'grade': 85, 'subject': 'Math'},
    'Bob': {'grade': 92, 'subject': 'Science'},
    'Charlie': {'grade': 78, 'subject': 'Math'},
    'Diana': {'grade': 95, 'subject': 'English'}
}
```
Task:​ Extract all grades into a list.
Expected Result:​ `[85, 92, 78, 95]`

<details>
<summary>Show Solution</summary>

```python
grades = [grade['grade'] for grade in students.values()]
print(grades)

#If subjects was wanted, this would be used. No other label in front of grade or subject worked.

subjects = [subject['subject'] for subject in students.values()]
print(subjects)
</details>

### Problem 2: Conditional Filtering

Data Structure:
```python
employees = {
    'John': {'salary': 50000, 'department': 'IT'},
    'Sarah': {'salary': 75000, 'department': 'Finance'},
    'Mike': {'salary': 60000, 'department': 'IT'},
    'Lisa': {'salary': 80000, 'department': 'HR'}
}
```

Task:​ Extract names of employees in the IT department.
Expected Result:​ `['John', 'Mike']`


<details>
<summary>Show Solution</summary>

```python
it_dept = [name for name, value in employees.items() if value['department'] == 'IT']
print(it_dept)
```
</details>

### Problem 3: Value Transformation

Data Structure:
```python
products = {
    'laptop': {'price': 1200, 'category': 'electronics'},
    'shirt': {'price': 25, 'category': 'clothing'},
    'phone': {'price': 800, 'category': 'electronics'},
    'shoes': {'price': 100, 'category': 'clothing'}
}
```

Task:​ Extract product names for items under $500, converted to uppercase.
Expected Result:​ `['SHIRT', 'SHOES']`

<details>
<summary>Show Solution</summary>

```python
upper_items = [good.upper() for good, data in products.items() if data['price'] < 500]
print(upper_items)
```

</details>

### Problem 4: Complex Nested Structure

Data Structure:
```python
library = {
    'fiction': {
        'books': [
            {'title': '1984', 'author': 'Orwell', 'pages': 328},
            {'title': 'Brave New World', 'author': 'Huxley', 'pages': 268}
        ]
    },
    'science': {
        'books': [
            {'title': 'Cosmos', 'author': 'Sagan', 'pages': 365},
            {'title': 'Brief History', 'author': 'Hawking', 'pages': 256}
        ]
    }
}
```

Task:​ Extract all book titles from all categories.
Expected Result:​ `['1984', 'Brave New World', 'Cosmos', 'Brief History']`

<details>
<summary>Show Solution</summary>

```python

# Let's break it down by level:

categories = [category for category in library.keys()]
print(categories) 
#['fiction', 'science']

books = [book for book in library.values()]
print(books)
#[{'books': [
#           {'title': '1984', 'author': 'Orwell', 'pages': 328}, 
#           {'title': 'Brave New World', 'author': 'Huxley', 'pages': 268}]},
# {'books': 
#           [
#           {'title': 'Cosmos', 'author': 'Sagan', 'pages': 365}, 
#           {'title': 'Brief History', 'author': 'Hawking', 'pages': 256}]}]


data_fiction = [data for data in library['fiction']['books']]
print(data_fiction)
#[{'title': '1984', 'author': 'Orwell', 'pages': 328}, {'title': 'Brave New World', 'author': 'Huxley', 'pages': 268}]

data_science = [data for data in library['science']['books']]
print(data_science)
#[{'title': 'Cosmos', 'author': 'Sagan', 'pages': 365}, {'title': 'Brief History', 'author': 'Hawking', 'pages': 256}]

titles = [book['title'] for category in library.values() for book in category['books']]
print(titles)
#['1984', 'Brave New World', 'Cosmos', 'Brief History']

pages = [book['pages'] for category in library.values() for book in category['books']]
print(pages)
# [328, 268, 365, 256]

```

</details>

### Problem 5: Multiple Conditions
Data Structure:
```python
restaurants = {
    'Pizza Palace': {'rating': 4.2, 'cuisine': 'Italian', 'price_range': 'medium'},
    'Burger Barn': {'rating': 3.8, 'cuisine': 'American', 'price_range': 'low'},
    'Sushi Spot': {'rating': 4.7, 'cuisine': 'Japanese', 'price_range': 'high'},
    'Taco Time': {'rating': 4.0, 'cuisine': 'Mexican', 'price_range': 'low'}
}
```
Task:​ Extract names of restaurants with rating above 4.0 and low price range.
Expected Result:​ `['Taco Time']`

<details>
<summary>Show Solution</summary>

```python
result = [name for name, data in restaurants.items() if data['rating'] >= 4.0 and data['price_range'] == 'low']
print(result)
```

</details>

### Problem 6: Key-Value Combination
Data Structure:

```python
scores = {
    'Alex': [85, 92, 78],
    'Beth': [90, 88, 95],
    'Carl': [76, 82, 85],
    'Dana': [88, 91, 87]
}
```

Task:​ Extract formatted strings showing each student's name and average score.
Expected Result:​ `['Alex: 85.0', 'Beth: 91.0', 'Carl: 81.0', 'Dana: 88.7']`

<details>
<summary>Show Solution</summary>

```python
result = [f'{name}: {sum(scores)/len(scores):.1f}' for name, scores in scores.items()]
print(result)
```

</details>

### Problem 7: Nested List Processing
Data Structure:

```python
inventory = {
    'warehouse_a': {
        'items': ['laptop', 'mouse', 'keyboard'],
        'quantities': [10, 50, 30]
    },
    'warehouse_b': {
        'items': ['monitor', 'speaker', 'webcam'],
        'quantities': [8, 25, 15]
    }
}
```

Task:​ Extract all item names from all warehouses.
Expected Result:​ `['laptop', 'mouse', 'keyboard', 'monitor', 'speaker', 'webcam']`


<details>
<summary>Show Solution</summary>

```python
items = [item for warehouse in inventory.values() for item in warehouse['items']]
print(items)
```

</details>

### Problem 8: Conditional Transformation
Data Structure:
```python

weather_data = {
    'Monday': {'temp': 25, 'condition': 'sunny'},
    'Tuesday': {'temp': 18, 'condition': 'rainy'},
    'Wednesday': {'temp': 30, 'condition': 'sunny'},
    'Thursday': {'temp': 22, 'condition': 'cloudy'},
    'Friday': {'temp': 28, 'condition': 'sunny'}
}
```

Task:​ Extract temperatures in Fahrenheit `(°F = °C × 9/5 + 32)` for sunny days only.
Expected Result:​ `[77.0, 86.0, 82.4]`

<details>
<summary>Show Solution</summary>

```python
temps = [(conditions['temp']* 9/5 + 32) for conditions in weather_data.values() if conditions['condition'] == 'sunny']
print(temps)
```

</details>


### Problem 9: Deep Nesting
Data Structure:
```python
company = {
    'engineering': {
        'teams': {
            'frontend': {'members': ['Alice', 'Bob'], 'lead': 'Alice'},
            'backend': {'members': ['Charlie', 'Diana'], 'lead': 'Charlie'}
        }
    },
    'marketing': {
        'teams': {
            'digital': {'members': ['Eve', 'Frank'], 'lead': 'Eve'},
            'print': {'members': ['Grace'], 'lead': 'Grace'}
        }
    }
}
```

Task:​ Extract all team leads from all departments.
Expected Result:​ `['Alice', 'Charlie', 'Eve', 'Grace']`

<details>
<summary>Show Solution</summary>

```python
leads = [people['lead'] for teams in company.values() for groups in teams.values() for people in groups.values()]
print(leads)
```

</details>

### Problem 10: Complex Filtering and Transformation
Data Structure:

```python
sales_data = {
    'Q1': {
        'jan': {'revenue': 50000, 'expenses': 30000},
        'feb': {'revenue': 60000, 'expenses': 35000},
        'mar': {'revenue': 55000, 'expenses': 32000}
    },
    'Q2': {
        'apr': {'revenue': 65000, 'expenses': 40000},
        'may': {'revenue': 70000, 'expenses': 42000},
        'jun': {'revenue': 45000, 'expenses': 35000}
    }
}
```

Task:​ Extract profit `(revenue - expenses)` for months where profit exceeds $20,000.
Expected Result:​ `[20000, 25000, 23000, 25000, 28000]`

<details>
<summary>Show Solution</summary>

```python
#For Loop

profit = []
for data in sales_data.values():
    for values in data.values():
        amount = values['revenue'] - values['expenses']
        if amount >= 20000:
            profit.append(amount)
print(profit)

#List Comprehension

profits = [ 
        values['revenue'] - values['expenses'] 
        for data in sales_data.values() 
        for values in data.values() 
        if values['revenue'] - values['expenses'] >= 20000
        ]
print(profits)
```
</details>

### Problem 11:  Intermediate

Data Structure:

```python
students = {
    'math_101': {
        'Alice': {'midterm': 85, 'final': 92, 'projects': [88, 90, 87]},
        'Bob': {'midterm': 78, 'final': 84, 'projects': [82, 85, 80]},
        'Charlie': {'midterm': 92, 'final': 89, 'projects': [95, 88, 91]}
    },
    'science_201': {
        'Diana': {'midterm': 88, 'final': 95, 'projects': [90, 93, 89]},
        'Eve': {'midterm': 76, 'final': 82, 'projects': [78, 80, 85]},
    }
}
```

Task:​ Extract the names of all students whose average project score is above 85.
Expected Result:​ `['Alice', 'Charlie', 'Diana']`

<details>
<summary>Show Solution</summary>


</details>

### Problem 12: Advanced
Data Structure:

```python
inventory = {
    'electronics': {
        'smartphones': [
            {'brand': 'Apple', 'model': 'iPhone 14', 'price': 999, 'stock': 15},
            {'brand': 'Samsung', 'model': 'Galaxy S23', 'price': 899, 'stock': 8}
        ],
        'laptops': [
            {'brand': 'Dell', 'model': 'XPS 13', 'price': 1299, 'stock': 5},
            {'brand': 'Apple', 'model': 'MacBook Air', 'price': 1199, 'stock': 12}
        ]
    },
    'clothing': {
        'shirts': [
            {'brand': 'Nike', 'model': 'Dri-Fit', 'price': 35, 'stock': 50},
            {'brand': 'Adidas', 'model': 'Classic', 'price': 28, 'stock': 0}
        ]
    }
}
```

Task:​ Extract the model names of all items that are in stock (stock > 0) and cost less than $1000.
Expected Result:​ `['Galaxy S23', 'Dri-Fit']`

<details>
<summary>Show Solution</summary>


</details>

### Problem 13: Intermediate

Data Structure:
```python
weather_stations = {
    'station_001': {
        'location': 'Downtown',
        'readings': [
            {'date': '2023-01-15', 'temp': 22, 'humidity': 65},
            {'date': '2023-01-16', 'temp': 18, 'humidity': 70},
            {'date': '2023-01-17', 'temp': 25, 'humidity': 60}
        ]
    },
    'station_002': {
        'location': 'Airport',
        'readings': [
            {'date': '2023-01-15', 'temp': 20, 'humidity': 68},
            {'date': '2023-01-16', 'temp': 16, 'humidity': 75},
            {'date': '2023-01-17', 'temp': 23, 'humidity': 62}
        ]
    }
}
```

Task:​ Extract all temperature readings above 20 degrees from all stations.
Expected Result:​ `[22, 25, 23]`

<details>
<summary>Show Solution</summary>


</details>

### Problem 14: Advanced
Data Structure:

```python
company_data = {
    'departments': {
        'engineering': {
            'budget': 500000,
            'employees': [
                {'name': 'Alice', 'salary': 85000, 'skills': ['Python', 'JavaScript']},
                {'name': 'Bob', 'salary': 75000, 'skills': ['Java', 'Python']}
            ]
        },
        'marketing': {
            'budget': 200000,
            'employees': [
                {'name': 'Charlie', 'salary': 60000, 'skills': ['SEO', 'Analytics']},
                {'name': 'Diana', 'salary': 65000, 'skills': ['Design', 'Analytics']}
            ]
        }
    }
}
```

Task:​ Extract the names of employees who know 'Python' and work in departments with a budget over $300,000.
Expected Result:​ `['Alice', 'Bob']`

<details>
<summary>Show Solution</summary>


</details>

### Problem 15: Advanced
Data Structure:
```python
tournament_data = {
    'round_1': {
        'match_a': {'team1': 'Lions', 'team2': 'Tigers', 'score1': 3, 'score2': 1},
        'match_b': {'team1': 'Bears', 'team2': 'Wolves', 'score1': 2, 'score2': 4}
    },
    'round_2': {
        'match_c': {'team1': 'Eagles', 'team2': 'Hawks', 'score1': 1, 'score2': 1},
        'match_d': {'team1': 'Sharks', 'team2': 'Dolphins', 'score1': 5, 'score2': 2}
    }
}
```
Task:​ Extract the names of all winning teams (teams with the higher score). For tied games, include both team names.
Expected Result:​ `['Lions', 'Wolves', 'Eagles', 'Hawks', 'Sharks']`



<details>
<summary>Show Solution</summary>


</details>