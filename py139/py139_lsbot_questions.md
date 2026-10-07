# LS Bot Generated Questions for PY130


<a name="top"></a>

## Table of Contents

- [Purity, Side Effects and Nested Mutable Collections](#purity-side-effects-and-nested-mutable-collections)

### Purity, Side Effects and Nested Mutable Collections

#### Exercise 1 — Analyze User Processing

**Problem Statement**
A function is designed to process a list of user dictionaries. It selects users who have been active within the last 30 days and records the time of this check.

Code
```python
def process_recent_users(users):
    user_profiles = []
    for user_profile in users:
        if user_profile['days_since_active'] <= 30:
            user_profile['last_seen'] = 'now'
            user_profiles.append(user_profile)
    return user_profiles

# --- Test Data ---
user_data = [
    {'name': 'Alice', 'days_since_active': 10},
    {'name': 'Bob', 'days_since_active': 45},
    {'name': 'Charlie', 'days_since_active': 5},
]

processed = process_recent_users(user_data)
```

**Task**

1. After the code runs, has the user_data list or any of its contents been mutated?
2. Explain your reasoning by identifying any aliases and tracing the path of any mutation that occurs.
3. Is the process_recent_users function pure or impure? Justify your answer.


<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 2 - Update Project Dependencies

**Problem Statement**
A developer has written a function to update a list of software projects by adding a new dependency to each. They have attempted to avoid side effects by creating copies.

Code
```python
def add_dependency(projects, new_dep):
    updated_projects = []
    for project in projects:
        project_copy = project.copy()
        project_copy['details']['dependencies'].append(new_dep)
        updated_projects.append(project_copy)
    return updated_projects

# --- Test Data ---
project_configs = [
    {
        'name': 'Project Alpha',
        'details': {
            'version': '1.0',
            'dependencies': ['lib_x', 'lib_y'],
        },
    },
    {
        'name': 'Project Beta',
        'details': {
            'version': '2.2',
            'dependencies': ['lib_z'],
        },
    },
]

updated = add_dependency(project_configs, 'lib_common')

```

**Task**

1. Is the `add_dependency` function pure?
2. Explain exactly why or why not by describing which objects are new, which are shared, and where any mutation occurs relative to the original project_configs data structure.

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 3 - Implement a Pure Update

**Problem Statement**
You need to manage a nested inventory structure. Implement a pure function that adds a new item to a specific category within the inventory without modifying the original inventory.

Function Signature
```python
def add_item_to_inventory(inventory, category, item):
    # Your implementation here
    pass
```

**Task**
Implement the `add_item_to_inventory` function. It must return a new inventory dictionary that includes the new item. The original inventory dictionary and its contents must not be mutated. You should only copy the parts of the data structure that are necessary to ensure purity; other parts may be shared between the old and new inventory structures.

The following assertions must pass:
```python
# --- Test Data and Assertions ---
original_inventory = {
    'office': {
        'supplies': ['pens', 'paper'],
        'furniture': ['desk', 'chair'],
    },
    'warehouse': {
        'tools': ['hammer', 'wrench'],
        'materials': ['wood', 'metal'],
    },
}

new_inventory = add_item_to_inventory(original_inventory, 'warehouse', 'screwdriver')

# 1. The new inventory should have the added item.
assert 'screwdriver' in new_inventory['warehouse']['tools']

# 2. The original inventory should be unchanged.
assert 'screwdriver' not in original_inventory['warehouse']['tools']

# 3. The top-level inventory dictionary should be a new object.
assert new_inventory is not original_inventory

# 4. The nested dictionary that was modified should be a new object.
assert new_inventory['warehouse'] is not original_inventory['warehouse']

# 5. Unmodified nested data can be shared to avoid unnecessary copying.
assert new_inventory['office'] is original_inventory['office']
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 4 - Restructure Categorized Data

**Problem Statement**
A function **generate_report** is written to process a dictionary where keys are categories and values are lists of numbers. It sorts the numbers for each category and calculates a summary.

Code
```python
def generate_report(data):
    report = {}
    for category, data_points in data.items():
        data_points.sort()
        report[category] = {
            'count': len(data_points),
            'first': data_points[0],
            'last': data_points[-1],
        }
    return report

# --- Test Data ---
sensor_data = {
    'temperature': [25, 23, 26, 22],
    'humidity': [60, 65, 58],
}

report_result = generate_report(sensor_data)
```

**Task**

1.  After `generate_report(sensor_data)` is called, is the original `sensor_data` dictionary modified in any way?
2.  If it is modified, describe the change. If not, explain why it remains unchanged.
3.  Is this function pure? Provide a brief justification.

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 5 - Refactor User Deactivation

**Problem Statement**
An administrator function, `deactivate_user`, finds a user by their ID in a list of user dictionaries and sets their is_active status to False.

Code
```python
def deactivate_user(users, user_id):
    for user in users:
        if user['id'] == user_id:
            user['is_active'] = False
            break
    return users

# --- Test Data ---
user_database = [
    {'id': 1, 'name': 'Dana', 'is_active': True},
    {'id': 2, 'name': 'Evan', 'is_active': True},
    {'id': 3, 'name': 'Frank', 'is_active': True},
]
```

**Task**

The current implementation of `deactivate_user` has a side effect: it mutates one of the dictionaries in the list it receives as an argument. Refactor the function to be pure. The new function should return a new list. For the user being deactivated, a new dictionary must be created. For all other users, the original dictionary objects should be reused in the new list.

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 6 - Department Grouping Behavior

**Problem Statement**
The function `group_by_department` reorganizes a list of employee records into a dictionary where keys are department names. It creates copies of the employee dictionaries before adding them to the new structure.

Code
```python
def group_by_department(employees):
    grouped = {}
    for employee in employees:
        dept = employee['department']
        if dept not in grouped:
            grouped[dept] = []

        # Create a shallow copy of the employee dictionary
        employee_copy = employee.copy()
        grouped[dept].append(employee_copy)

    # A new requirement is added: standardize a skill name
    if 'Engineering' in grouped:
        for eng_employee in grouped['Engineering']:
            if 'devops' in eng_employee['skills']:
                skill_index = eng_employee['skills'].index('devops')
                eng_employee['skills'][skill_index] = 'DevOps'

    return grouped

original_employees = [
    {'name': 'Alice', 'department': 'Engineering', 'skills': ['python', 'devops']},
    {'name': 'Bob', 'department': 'HR', 'skills': ['communication', 'hiring']},
    {'name': 'Charlie', 'department': 'Engineering', 'skills': ['java', 'spring']},
]

grouped_data = group_by_department(original_employees)
```

**Task**

1.  After this code executes, is the `original_employees` data structure—including all its nested elements—in the same state as it was before the function call?
2.  Explain your answer by describing which objects, if any, are shared between `original_employees` and the returned grouped_data. Is the use of `.copy()` sufficient to prevent side effects in this case?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 7 - User Settings Merge

**Problem Statement**
A function `merge_user_settings` takes a user's settings and a set of default settings. It should return a new dictionary representing the merged settings, with the user's settings taking precedence. The original user settings object should not be changed.

Code
```python
def merge_user_settings(user_settings, default_settings):
    merged = user_settings.copy()
    for key, value in default_settings.items():
        if key not in merged:
            merged[key] = value

    # Ensure notification settings are complete
    if 'notifications' not in merged:
        merged['notifications'] = {}
    
    if 'email' not in merged['notifications']:
         merged['notifications']['email'] = True

    return merged

user = {
    'username': 'testuser',
    'preferences': {'theme': 'dark'},
    'notifications': {'push': True},
}

defaults = {
    'preferences': {'theme': 'light', 'layout': 'compact'},
    'notifications': {'email': True, 'push': True},
}

final_settings = merge_user_settings(user, defaults)
```

**Task**

1. Predict the final value of the user dictionary after the function call.
2. Is `merge_user_settings` a pure function as implemented?
3. Justify your answer by identifying any shared mutable objects between the original user dictionary and the returned `final_setting`s dictionary and explaining how a side effect occurs.

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 8 - Project Assignment Implementation

**Problem Statement**
Implement a pure function `add_project_to_employees` that takes a dictionary of employees and adds a new project to the project lists of specified employee IDs. The function must not mutate the original employees dictionary or any of its contents.

Function Signature
```python
def add_project_to_employees(employees, employee_ids, project_name):
    # Your implementation here
    pass
```

**Task**
Implement the function according to these rules:

1. It must return a new top-level dictionary.
2. For each employee whose project list is modified, their corresponding entry in the new dictionary must be a new dictionary containing a new project list.
3. The original data for any employee who is ​not​ modified must be shared, not copied.
4. The original employees dictionary and all nested objects must not be mutated.

Tests
```python
# Use these assert statements to verify your implementation.

employees_db = {
    101: {'name': 'Alice', 'projects': ['Project A']},
    102: {'name': 'Bob', 'projects': ['Project B', 'Project C']},
    103: {'name': 'Charlie', 'projects': []},
}

updated_db = add_project_to_employees(employees_db, [101, 103], 'Project X')

# 1. The returned dictionary should be a new object.
assert id(updated_db) != id(employees_db)

# 2. The data for the modified employees should be correct.
assert updated_db[101] == {'name': 'Alice', 'projects': ['Project A', 'Project X']}
assert updated_db[103] == {'name': 'Charlie', 'projects': ['Project X']}

# 3. The dictionaries for modified employees should be new objects.
assert id(updated_db[101]) != id(employees_db[101])
assert id(updated_db[103]) != id(employees_db[103])

# 4. The nested 'projects' lists for modified employees should be new objects.
assert id(updated_db[101]['projects']) != id(employees_db[101]['projects'])

# 5. The unmodified employee's dictionary should be the SAME object (shared).
assert id(updated_db[102]) == id(employees_db[102])

# 6. The original database must remain unchanged.
assert employees_db == {
    101: {'name': 'Alice', 'projects': ['Project A']},
    102: {'name': 'Bob', 'projects': ['Project B', 'Project C']},
    103: {'name': 'Charlie', 'projects': []},
}

print("All tests passed!")
```

<details> 
<summary>Possible Solution</summary> 
</details>

[Back to the top](#top)


<details> 
<summary>Possible Solution</summary> 
</details>

[Back to the top](#top)