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