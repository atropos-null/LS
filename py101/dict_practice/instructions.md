## Practice Questions on Python Dictionaries for PY109

Here are 12 practice questions involving dictionaries at varying difficulty levels to help you prepare for your PY109 assessment:

1.  ​Basic​: Write a function that takes a dictionary and returns a list of all the keys.
2.  ​Basic​: Create a function that takes a dictionary and returns the sum of all the values (assuming all values are numbers).
3.  ​Intermediate​: Write a function that merges two dictionaries. If there are duplicate keys, the value from the second dictionary should overwrite the value from the first.
4.  ​Basic​: Create a function that counts the frequency of each character in a string and returns the result as a dictionary.
5.  ​Intermediate​: Write a function that inverts a dictionary (swapping keys and values). Assume all values are unique.
6.  ​Intermediate​: Create a function that takes a list of dictionaries and a key name, and returns a new list sorted based on that key's values.
7.  ​Advanced​: Write a function that takes a nested dictionary and flattens it into a single-level dictionary. The keys in the flattened dictionary should be joined with a dot (e.g., {'a': {'b': 1}} becomes {'a.b': 1}).
8.  ​Basic​: Create a function that filters a dictionary to only include key-value pairs where the value meets a certain condition (e.g., is a string, is greater than 10, etc.).
9.  ​Intermediate​: Write a function that groups a list of dictionaries by a specified key and returns a dictionary of lists.
10. Basic: Write a function named filter_by_value that takes a dictionary and a value as arguments. The function should return a new dictionary that only contains the key-value pairs where the value is equal to the given value.
11. ​Intermediate​: Write a function that takes a dictionary and returns a new dictionary with the same keys but with all string values converted to uppercase.



#### Sample Dictionaries

```python

# Sample dictionary with various data types
student_data = {
    'id': 12345,
    'name': 'Jane Smith',
    'grades': {
        'Python': 95,
        'Math': 87,
        'English': 92,
        'History': 78
    },
    'contact': {
        'email': 'jane.smith@example.com',
        'phone': '555-123-4567'
    },
    'enrolled': True,
    'courses': ['Python 101', 'Data Structures', 'Web Development'],
    'attendance': [True, True, False, True, True],
    'graduation_year': 2024,
    'address': None
}

# Another simple dictionary for merging exercises
additional_data = {
    'id': 12345,
    'graduation_year': 2025,  # Note this is different from the original
    'gpa': 3.8,
    'clubs': ['Coding Club', 'Chess Team']
}

# A list of dictionaries for sorting/grouping exercises
students = [
    {'name': 'Alex', 'grade': 'A', 'age': 22},
    {'name': 'Beth', 'grade': 'B', 'age': 19},
    {'name': 'Carlos', 'grade': 'A', 'age': 21},
    {'name': 'Diana', 'grade': 'C', 'age': 20},
    {'name': 'Eric', 'grade': 'B', 'age': 22}
]

Sample dictionary for character frequency counting (Q4)
text = "Launch School is a great place to learn programming"

# Sample dictionaries for merging exercise (Q3)
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}

# Sample for inverting a dictionary (Q5)
grades = {'Python': 95, 'Math': 87, 'English': 92, 'History': 78}

# Sample for list of dictionaries sorting (Q6)
products = [
    {'name': 'Laptop', 'price': 1200, 'stock': 10},
    {'name': 'Phone', 'price': 800, 'stock': 25},
    {'name': 'Tablet', 'price': 500, 'stock': 5},
    {'name': 'Headphones', 'price': 200, 'stock': 50}
]

# Sample for nested dictionary flattening (Q7)
nested_dict = {
    'user': {
        'personal': {
            'name': 'John',
            'age': 30
        },
        'settings': {
            'theme': 'dark',
            'notifications': True
        }
    },
    'app_version': '2.3.1'
}

# Sample for filtering dictionary (Q8)
mixed_data = {
    'name': 'Project X',
    'duration': 45,
    'participants': 12,
    'location': 'Room 302',
    'completed': False,
    'score': 87.5
}

# Sample for grouping dictionaries (Q9)
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 75000},
    {'name': 'Bob', 'department': 'HR', 'salary': 65000},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 80000},
    {'name': 'Diana', 'department': 'Marketing', 'salary': 70000},
    {'name': 'Eve', 'department': 'HR', 'salary': 68000}
]

# Sample for string values to uppercase (Q11)
user_profile = {
    'username': 'pythondev',
    'email': 'dev@example.com',
    'role': 'developer',
    'active': True,
    'login_count': 42
}

# Sample for words grouping by first letter (Q12)
word_list = ['apple', 'banana', 'cherry', 'apricot', 'blueberry', 'cantaloupe', 'avocado', 'blackberry']

```
