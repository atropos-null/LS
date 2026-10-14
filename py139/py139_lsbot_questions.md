# LS Bot Generated Questions for PY130


<a name="top"></a>

## Table of Contents

- [Purity, Side Effects and Nested Mutable Collections](#purity-side-effects-and-nested-mutable-collections)
- [Verbalization and Conceptual Precision](#verbalization-and-conceptual-precision)
- [Partial Function Application and Closures](#partial-function-application-and-closures)
- [Purity, Copying, and Nested Mutability](#purity-copying-and-nested-mutability)
- [Decorators](#decorators)
- [Mixed Assessment Transfer](#mixed-assessment-transfer)
- [General Pass](#general-pass)


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


### Verbalization and Conceptual Precision

#### Prompt 1 — Function Memory

Question:​ Casually explain what a closure is in Python. What information does the inner function retain access to after the outer function has finished executing?

Possible Follow-up:​ Is the value at that time copied, or is access to the binding itself retained?

<details> 
<summary>My Answer</summary> 
</details>

####  Prompt 2 — Pre-configured Functions

Question:​ In your own words, what is partial function application? What kind of object does it create, and what is the relationship between the original function's parameters and the new function's parameters?

Possible Follow-up:​ Where does the "pre-filled" argument's state live?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 3 — Function Roles

Question:​ What is the distinction between a first-class function and a higher-order function? Can a function be both?

Possible Follow-up:​ Can you give an example of a common built-in Python function that is a higher-order function?

<details> 
<summary>My Answer</summary> 
</details>


#### Prompt 4 — Purity and Effects

Question:​ What does it mean for a function to be "pure"? What must be true about both its return value and its interaction with the rest of the program?

Possible Follow-up:​ If a function has no side effects, is it guaranteed to be pure?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 5 — I/O Side Effects

Question:​ Imagine a function that opens a text file, reads its first line, and returns it. Why is this considered a side effect, even if the function doesn't change the file?

Possible Follow-up:​ What external state is the function's behavior dependent on?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 6 — Global State Side Effects

Question:​ Let's say you have a function that increments a global counter variable every time it's called. Explain why this action is categorized as a side effect.

Possible Follow-up:​ How does this side effect impact the predictability of the function?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 7 — Mutation Side Effects

Question:​ Consider a function that takes a list of lists as an argument. It creates and returns a new top-level list, but it also sorts one of the inner lists in place. Why is this function considered impure?

Possible Follow-up:​ What is the term for having multiple variables that refer to the same object?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 8 — System and Exception Side Effects

Question:​ Besides I/O, global state, and mutation, what are some other categories of side effects? For instance, why might interacting with the system clock or raising an exception be considered side effects?

Possible Follow-up:​ How does raising an exception alter the program's normal control flow?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 9 — Copying and Aliasing

Question:​ Explain the difference between a shallow copy and a deep copy of a nested data structure, like a list of dictionaries. What happens if you modify a value inside a nested dictionary after making a shallow copy?

Possible Follow-up:​ In the shallow copy scenario, is the nested dictionary aliased or copied?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 10 — The nonlocal Keyword

Question:​ What is the fundamental difference between using the nonlocal keyword to reassign a variable in a parent scope, and simply mutating a list object that was defined in that same parent scope?

Possible Follow-up:​ What does nonlocal allow you to change: the object, or what the name is bound to?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 11 — Decorator Mechanics

Question:​ When you apply a decorator to a function, what happens at decoration time? After the decoration, what object does the original function name actually refer to?

Possible Follow-up:​ Does the original, undecorated function still exist somewhere?

<details> 
<summary>My Answer</summary> 
</details>

#### Prompt 12 — Decorator Application Order

Question:​ If you stack two decorators on top of a function, in what order are they applied? For example, if you have `@decorator_A` on the first line and `@decorator_`B on the second line above `my_func`, which decorator runs first?

Possible Follow-up:​ Which decorator's returned function is called when you finally invoke `my_func`?

<details> 
<summary>My Answer</summary> 
</details>


[Back to the top](#top)


### Partial Function Application and Closures

#### Problem 1 — Function Specialization


Given the process_data function and the subsequent creation of the `process_financials` callable, predict the output of the final print statement.

Code
```python
from functools import partial

def process_data(source_type, data, *, category="general"):
    return f"Processing {source_type} data in '{category}': {data}"

process_financials = partial(process_data, "financial")

print(process_financials("Q4-report", category="quarterly"))
```

Task

What will the code print to the console?

<details> 
<summary>Solution</summary> 
</details>


#### Problem 2 — Counter Factory


The `make_counter` function is a factory that produces new, independent counter functions.

Code
```python
def make_counter(start):
    count = start
    def counter():
        nonlocal count
        current = count
        count += 1
        return current
    return counter

counter_a = make_counter(0)
counter_b = make_counter(10)

print(counter_a())
print(counter_b())
print(counter_a())
print(counter_a())
print(counter_b())
```

Task

1. What is the output of this script?
2. After all the code has run, what value is retained by the closure referred to by the counter_b variable? Explain briefly why this value survives even after the initial call to make_counter(10) has completed.

<details> 
<summary>Solution</summary> 
</details>


#### Problem 3 — Configuring a Data Logger


A system requires specialized loggers for different event types. You are given a general-purpose `log_message` function.

Function Signature
```python
import datetime

def log_message(level, source, message, *, timestamp=None):
    ts = timestamp or datetime.datetime.now()
    return f"[{ts}] {level.upper()} ({source}): {message}"
```

Task

Using `functools.partial`, create a specialized logger named `system_error_log` that automatically logs messages with a level of "ERROR" and a source of "SYSTEM_CORE". The resulting callable should only require a message argument to be invoked.

Your implementation should pass the following assertions.

```python
# Your implementation here

# --- Asserts ---
log_entry = system_error_log("Disk space is critically low.")
assert log_entry.endswith("ERROR (SYSTEM_CORE): Disk space is critically low.")
assert "ERROR" in log_entry
assert "SYSTEM_CORE" in log_entry

log_entry_ts = system_error_log("Network failure detected.", timestamp="2023-10-27T10:00:00Z")
assert log_entry_ts.startswith("[2023-10-27T10:00:00Z]")
```

<details> 
<summary>Solution</summary> 
</details>


#### Problem 4 — Reusable Task Runner

A `run_task` function executes system tasks with a specified name and priority. A partial callable, `run_high_priority_task`, is created to simplify running tasks with a fixed priority of "high".

Before answering, check:

- What is requested?
- Which arguments are already bound?
- Which arguments arrive later?
- What state or binding survives?
- When does execution actually occur?
- What object/value is returned?

Code
```python
from functools import partial

def run_task(task_name, *, priority="normal", notify=False):
    notification = " [Notifying admin]" if notify else ""
    return f"Running '{task_name}' with '{priority}' priority.{notification}"

run_high_priority_task = partial(run_task, priority="high", notify=True)

print(run_high_priority_task("Database backup"))
print(run_high_priority_task("Cleanup temp files", priority="low"))
```

Task

What will be printed to the console when this script is executed?

<details> 
<summary>Solution</summary> 
</details>

####  Problem 5 — Data Filtering


The `create_threshold_filter` function returns a filtering function based on a given threshold. This filter is then used in a list comprehension.

Before answering, check:

- What is requested?
- Which arguments are already bound?
- Which arguments arrive later?
- What state or binding survives?
- When does execution actually occur?
- What object/value is returned?

Code
```python
def create_threshold_filter(threshold):
    def has_passed(value):
        return value >= threshold
    return has_passed

data_points = [88, 105, 99, 75, 112, 95]
high_pass_filter = create_threshold_filter(100)

approved_points = [
    point
    for point in data_points
    if high_pass_filter(point)
]

print(approved_points)
```

Task
What is the output of the final print statement?

<details> 
<summary>Solution</summary> 
</details>


#### Problem 6 — Manual Partial Application


The `functools.partial` object is a powerful tool for partial function application. Your task is to implement a function that emulates its core behavior using a closure.

Before answering, check:

- What is requested?
- Which arguments are already bound?
- Which arguments arrive later?
- What state or binding survives?
- When does execution actually occur?
- What object/value is returned?

Function Signature
```python
def apply_partially(func, *p_args, **p_kwargs):
    # Your implementation here
    pass

```

Task

Implement the `apply_partially` function. It should accept a callable `func` and any number of initial positional (`*p_args`) and keyword (`**p_kwargs`) arguments. It must return a new function.

When this new function is called with its own set of positional and keyword arguments, it should invoke the original func, passing the combination of the initially provided arguments and the newly provided arguments.Arguments provided at the final invocation should take precedence (specifically, later keyword arguments override earlier ones).

Your implementation should pass the following assertions.
```python
def format_record(name, value, *, record_id=None, status="active"):
    id_str = f" (ID: {record_id})" if record_id else ""
    return f"Record{id_str}: [{name}={value}] Status: {status}"

# --- Asserts ---
format_user_record = apply_partially(format_record, record_id=100)
user_log = format_user_record("username", "jdoe", status="inactive")
assert user_log == "Record (ID: 100): [username=jdoe] Status: inactive"

format_system_record = apply_partially(format_record, "system_event", status="pending")
system_log = format_system_record(True, record_id=201)
assert system_log == "Record (ID: 201): [system_event=True] Status: pending"

# Test keyword override
final_log = format_system_record(False, record_id=202, status="complete")
assert final_log == "Record (ID: 202): [system_event=False] Status: complete"
```

<details> 
<summary>Solution</summary> 
</details>

[Back to the top](#top)

### Purity, Copying, and Nested Mutability

#### Problem 1 — Data Processing Side Effects


Consider the following function` select_and_tag`, which is intended to select a user record and add a 'processed' tag to it.

Code
```python
def select_and_tag(user_data):
    selected_user = None
    for user in user_data:
        if user['id'] == 2:
            selected_user = user
            break

    if selected_user:
        selected_user['tags'].append('processed')

    return user_data
```

Task

1. Is the `select_and_tag` function a pure function?
2. Explain your reasoning. In your explanation, describe what object or objects, if any, are mutated.
3. If the function is not pure, identify the specific side effect it produces.

<details> 
<summary>Solution</summary> 
</details>

#### Problem 2 — Sufficiency of Shallow Copying


Your teammate has written a function `grant_admin_privileges` to return a new list of user profiles where a specific user is marked as an admin. The user profiles contain only immutable values (strings and booleans). Your teammate asserts that because they used `.copy() `on each user's dictionary, the function is pure and cannot modify the original profiles list.

Code
```python
def grant_admin_privileges(profiles, user_id):
    updated_profiles = []
    for p in profiles:
        profile_copy = p.copy()
        if profile_copy['id'] == user_id:
            profile_copy['is_admin'] = True
        updated_profiles.append(profile_copy)

    return updated_profiles
```

Task

1. Is your teammate's assertion correct? Is the `grant_admin_privileges` function pure?
2. Explain ​why​ the shallow copy strategy used here is or is not sufficient to prevent side effects on the original profiles data. Your explanation should focus on the types of values contained within the user dictionaries.

<details> 
<summary>Solution</summary> 
</details>

#### Problem 3 — Analyzing a Flawed Update Function

The function `log_test_result` is intended to take a session_data dictionary, add a new test result to the history, and return a ​new​ dictionary with the updated data, leaving the original session_data unchanged.

Before answering, check:

- What is requested?
- Which containers are new?
- Which references are shared?
- Which shared objects are mutable?
- Which object actually changes?
- Can that mutation reach the original input?

Code
```python
def log_test_result(session_data, result):
    new_session = session_data.copy()
    new_session['log']['history'].append(result)
    return new_session

```

Task

1. Does the function successfully avoid mutating the original `session_data` object? Demonstrate what happens to an input dictionary after it is passed to this function.
2. Identify the exact reference path from the `new_session` variable back to a mutable object that is still shared with the original session_data.
3. In the context of this specific data structure, explain the key difference between the shallow copy performed by `session_data.copy()` and how `copy.deepcopy()` would have behaved.

#### Problem 4 — Implementing a Pure Transformation


You are given a data structure that represents a list of software projects, where each project is a dictionary containing an 'id' and a list of 'modules'.

Your task is to implement a pure function `add_feature_module` that adds a new module to a specific project without mutating the original data structure.

Function Signature
```python
def add_feature_module(all_projects, project_id, module_name):
    # Your implementation here
    pass
```

Task

Implement the `add_feature_module` function.

- The function must return a new list of projects.
- The original `all_projects` list and its contents must not be mutated.
- You must determine which parts of the data structure (the outer list, the project dictionaries, the module lists) need to be copied to ensure purity.

Use the following test cases to validate your implementation. Your function should pass all assert statements.

Tests
```python
import copy

# Setup original data
original_projects = [
    {
        'id': 'PROJ-101',
        'modules': ['core', 'api', 'db'],
    },
    {
        'id': 'PROJ-202',
        'modules': ['ui', 'auth'],
    },
]

# Create a deep copy for later comparison to ensure the original is unchanged
original_projects_backup = copy.deepcopy(original_projects)

# Call the function
new_projects = add_feature_module(original_projects, 'PROJ-101', 'reporting')

# Test 1: The new data structure should have the added module
assert new_projects[0]['modules'] == ['core', 'api', 'db', 'reporting']
assert len(new_projects[0]['modules']) == 4

# Test 2: The non-targeted project should be unchanged
assert new_projects[1]['modules'] == ['ui', 'auth']

# Test 3: The original data structure must not be mutated
assert original_projects == original_projects_backup

# Test 4: The returned list should be a new object
assert new_projects is not original_projects

# Test 5: The modified project dictionary should be a new object
assert new_projects[0] is not original_projects[0]

# Test 6: The modified project's module list should be a new object
assert new_projects[0]['modules'] is not original_projects[0]['modules']
```

<details> 
<summary>Solution</summary> 
</details>

[Back to the top](#top)

### Decorators

#### Problem 1 — Function Decoration Lifecycle

Analyze the provided code snippet involving a simple function decorator.

Code
```python
def trace_decorator(func):
    print(f"Decorating {func.__name__}...")
    return func

print("Script is starting.")

@trace_decorator
def greet():
    print("Hello from greet!")

print("Script has defined greet.")

greet()

print("Script has called greet.")
```

Task

1. Describe the sequence of events that occurs when this script is executed, from top to bottom.
2. What object is passed as an argument to `trace_decorator`?
3. When does the print statement inside `trace_decorator` execute?
4. After the `@trace_decorator` line is processed, what object does the name greet refer to?
5. What happens when `greet()` is called on line 12?


#### Problem 2 — Wrapper Execution Order


Consider the following code with two decorators applied to a single function.

Before answering, check:

- What happens during decoration?
- What does `get_number` refer to after decoration?
- When `get_number()` is called, which wrapper runs first?
- What value does the innermost function return?
- How does each wrapper modify that value on its way out?

Code
```python
def add_one(func):
    def wrapper():
        print("add_one wrapper: before call")
        result = func()
        print("add_one wrapper: after call")
        return result + 1
    return wrapper

def multiply_by_two(func):
    def wrapper():
        print("multiply_by_two wrapper: before call")
        result = func()
        print("multiply_by_two wrapper: after call")
        return result * 2
    return wrapper

@add_one
@multiply_by_two
def get_number():
    return 10

final_result = get_number()
print(f"Final result: {final_result}")
```

Task

1. In what order are the decorators (`add_one`, `multiply_by_two`) executed at decoration time?
2. When `get_number()` is called, in what order do the print statements from the wrapper functions appear?
3. Trace the return value from the original `get_number` function as it passes back through the decorator wrappers. What is the final value assigned to `final_result`? Explain each step of the calculation.

### Problem 3 — Class-Based Decoration

The following code uses a class as a decorator. Analyze its behavior at both decoration time and call time.

Before answering, check:

- When does `DecoratorClass.__init__` run?
- What is passed to `__init__`?
- After decoration, is `display_info` a function or an instance of a class?
- What makes an object "callable"?
- When `display_info("Alice", 30)` is executed, what method is actually being invoked?

Code
```python
class DecoratorClass:
    def __init__(self, original_function):
        print("DecoratorClass __init__ called.")
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("DecoratorClass __call__ method executed.")
        return self.original_function(*args, **kwargs)

@DecoratorClass
def display_info(name, age):
    print(f"display_info ran with: ({name}, {age})")

print("About to call display_info...")
display_info("Alice", 30)
print("...called display_info.")
```

Task

1.  What happens when the line `@DecoratorClass` is executed during script loading? Describe the process.
2.  After decoration, what kind of object does the name `display_info` refer to?
3.  Where is the original `display_info` function object stored?
4.  What causes the `__call__` method of `DecoratorClass` to be executed?

#### Problem 4 — Decorator with Persistent State

This decorator uses a class to maintain state between function calls.

Before answering, check:

- What object is created at decoration time?
- What attributes does that object have?
- When `say_hello("World")` is called, what code is actually running?
- What object's count attribute is being incremented?
- Does each decoration create a new instance of `CallCounter`?

Code
```python
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CallCounter
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("World")
say_hello("Python")
say_hello("Decorator")
```

Task

1.  After the `@CallCounter` decoration is complete, what object does the name `say_hello` refer to?
2.  Where is the call count (the value of `self.count`) stored?
3.  Why does the count persist across multiple calls to `say_hello`?
4.  If you created another decorated function, such as `@CallCounter` `def say_goodbye()`, would it share the same call count as `say_hello?` Why or why not?

<details> 
<summary>Solution</summary> 
</details>

[Back to the top](#top)

### Mixed Assessment Transfer

#### Problem 1 — Argument Binding Order

Before answering, check:

- What is requested?
- What is returned versus printed?
- Which object or binding changes?
- Which arguments bind where?
- What state survives?
- When does execution stop?

Problem Statement
Consider the following function `build_config` and the subsequent code that uses `functools.partial`.

Code
```python
import functools

def build_config(version, /, setting_a, setting_b=100, *, theme, is_production=False):
    config = {
        'version': version,
        'setting_a': setting_a,
        'setting_b': setting_b,
        'theme': theme,
        'is_production': is_production,
    }
    return config

base_config_builder = functools.partial(build_config, 'v1.2', theme='dark')

config1 = base_config_builder(25, is_production=True)
config2 = base_config_builder(50, setting_b=200)

print(f"Config 1: {config1}")
print(f"Config 2: {config2}")
```

Task

1. What will the two print statements output?
2. Explain precisely how the arguments for the `config2` call are bound to the parameters of the `build_config` function.

State the governing rule aloud in one or two sentences.

<details> 
<summary>Solution</summary> 
</details>

#### Problem 2 — State Encapsulation

Before answering, check:

- What is requested?
- What is returned versus printed?
- Which object or binding changes?
- Which arguments bind where?
- What state survives?
- When does execution stop?

Problem Statement
The `make_event_logger` function is a factory that returns a new logging function. Each logger maintains its own event history.

Code
```python
def make_event_logger():
    events = []
    def log_event(event_name):
        nonlocal events
        events.append(event_name)
        print(f"Logged: {event_name}. History size: {len(events)}")
        return events
    return log_event

logger1 = make_event_logger()
logger2 = make_event_logger()

logger1("INIT")
logger2("START")
logger1("PROCESS")
final_history = logger2("END")
```


Task

1. What is the final line of output printed to the console?
2. What is the value of the `final_history` variable after all the code has run?
3. Explain why the history for `logger1` is separate from the history for `logger2`.
4. If `final_history.append("EXTRA")` is executed afterward, would that affect the state retained by logger2? Explain.

State the governing rule aloud in one or two sentences.

<details> 
<summary>Solution</summary> 
</details>

#### Problem 3 — Shared State Modifier

Before answering, check:

- What is requested?
- What is returned versus printed?
- Which object or binding changes?
- Which arguments bind where?
- What state survives?
- When does execution stop?

Problem Statement

When a function receives a mutable object like a list, it receives a reference to the original object. Operations that mutate the object through that reference will affect the object outside the function's scope.Creating a shallow copy can create a new object, but nested objects may still be shared.

Code
```python
def modify_state(data_list):
    print("Function start: Modifying data...")
    local_copy = data_list.copy()

    # Modify a nested list through the original reference
    data_list[0].append('X')

    # Modify the outer list through the local copy
    local_copy.append([4, 5])
    print("Function end.")

state = [[1], [2, 3]]
modify_state(state)
print(f"Final state: {state}")
```

Task
Trace the execution and predict the final line of output printed by this script.

State the governing rule aloud in one or two sentences.

<details> 
<summary>Solution</summary> 
</details>

#### Problem 4 — Tracing Side Effects

Before answering, check:

- What is requested?
- What is returned versus printed?
- Which object or binding changes?
- Which arguments bind where?
- What state survives?
- When does execution stop?

Problem Statement
Consider the following code, which uses a higher-order function `apply_to_all` to process a list of numbers.

Code
```python
side_effects_log = []

def multiply_and_log(n):
    side_effects_log.append(n * 2)
    print(f"Processed {n}")
    return n > 5

def apply_to_all(items, func):
    results = []
    for item in items:
        results.append(func(item))
    return results

numbers = [1, 6, 3, 8]
final_results = apply_to_all(numbers, multiply_and_log)

print(f"Final results: {final_results}")
print(f"Log: {side_effects_log}")
```

Task

1. List everything that will be printed to the console, in the order it is printed.
2. What is the final value of `final_results`?
3. What is the final value of `side_effects_log`?

State the governing rule aloud in one or two sentences.

<details> 
<summary>Solution</summary> 
</details>

#### Problem 5 — Decorator with Return Value

Before answering, check:

- What is requested?
- What is returned versus printed?
- Which object or binding changes?
- Which arguments bind where?
- What state survives?
- When does execution stop?

Problem Statement

A decorator is a function that takes another function and returns a new function, usually extending or altering its behavior.A common pattern is to perform actions before and after the original function is called. For the decorator to be transparent, it must correctly handle the return value of the function it decorates.

Code
```python
def audit(func):
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' with args: {args}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned: {result}")
        return result
    return wrapper

@audit
def calculate_sum(x, y):
    return x + y

final_result = calculate_sum(15, 25)
print(f"Final result received: {final_result}")

```

Task
Predict the exact, complete output of this script, in the correct order.

State the governing rule aloud in one or two sentences.

<details> 
<summary>Solution</summary> 
</details>

#### Problem 6 — Generator Lifetime

Before answering, check:

- What is requested?
- What is returned versus printed?
- Which object or binding changes?
- Which arguments bind where?
- What state survives?
- When does execution stop?

Problem Statement

The generator function `yield_from_file` reads lines from a file. The main script consumes the generator it produces in multiple steps. Assume a file named sample.txt exists with the following content:

Line 1
Line 2
Line 3


Code
```python
def yield_from_file(path):
    print("Generator: Starting to open file.")
    try:
        with open(path, 'r') as f:
            for line in f:
                print(f"Generator: Yielding '{line.strip()}'")
                yield line.strip()
    finally:
        print("Generator: Execution finished or resource closed.")

lines_generator = yield_from_file('sample.txt')
print("Script: Generator created.")

print("Script: About to take first item.")
first_line = next(lines_generator)
print(f"Script: Got '{first_line}'.")

print("Script: About to consume the rest.")
remaining_lines = list(lines_generator)
print(f"Script: Got remaining lines: {remaining_lines}")
```

Task
Write out the complete, ordered output that will be printed to the console when this script is executed. Explain at what point the `file sample.txt` is opened and at what point it is closed.

State the governing rule aloud in one or two sentences.


<details> 
<summary>Solution</summary> 
</details>

[Back to the top](#top)


<details> 
<summary>Solution</summary> 
</details>

[Back to the top](#top)


### General Pass

#### Exercise 1

Consider the following function definition:

```python
def process_data(a, b, /, c, d=4, *, e, f, **kwargs):
    pass
```

Verbally describe the different kinds of parameters in this function and explain how you would provide arguments to satisfy them in a call. Address positional-only, positional-or-keyword, keyword-only, default, and variable-keyword parameters.

<details> 
<summary>Solution</summary> 
</details>

#### Exercise 2

The following test suite is for a function `create_user_profile` that returns a dictionary for a valid username, or `None` for an invalid one. Complete the test methods by writing the necessary assertions.

```
import unittest

def create_user_profile(username):
    if not username or len(username) < 3:
        return None
    return {
        'username': username,
        'is_active': True,
        'followers': [],
    }

class TestUserProfile(unittest.TestCase):
    def test_creation_and_defaults(self):
        # Your task: Write assertions here to verify that calling
        # create_user_profile('test_user') returns a dictionary with the
        # correct structure and default values. Use at least three
        # different assertion methods.
        pass

    def test_invalid_username(self):
        # Your task: Write an assertion here to verify that calling
        # create_user_profile('') returns None.
        pass
```

<details> 
<summary>Solution</summary> 
</details>


#### Exercise 3

What is the output of the following code? Explain your reasoning.

```python
data = [1, 2, 3, 4]
squares_gen = (n * n for n in data)

print(f"First sum: {sum(squares_gen)}")
print(f"Second sum: {sum(squares_gen)}")

```

<details> 
<summary>Solution</summary> 
</details>


#### Exercise 4

For each of the five scenarios below, identify and briefly explain the primary side effect that occurs. Classify each using one of the five distinct categories of side effects discussed in the PY130 curriculum.


1.  A function call `validate_age(-5)` is made to the following function, causing the program to halt.
```python
        def validate_age(age):
        if not isinstance(age, int) or age <= 0:
            raise TypeError("Age must be a positive integer.")
```

2.  The following code is executed.
```python

    count = 5

    def reset_count():
        global count
        count = 0

    reset_count()
```
3.  The following function is called, and it modifies a list that was defined outside of it.
    
```python
    outer_list = [10, 20]
    def modify_outer_list():
        outer_list.pop()
    modify_outer_list()
```

4.  A list `my_list` is passed as an argument to a function.

```python        
    my_list = [1, 2]
    def append_to_list(a_list):
        a_list.append(3)
    append_to_list(my_list)
```

5. The following function is called.
 
 ```python
 def save_score(name, score):
     with open('scores.txt', 'a') as f:
        f.write(f'{name}:{score}\n')
 
 save_score('Alice', 100)
 ```
 
<details> 
<summary>Solution</summary> 
</details>   

#### Exercise 5

Assume you have two files, `config.py` and `main.py`, in the same directory with the contents shown below.

```python
File: config.py

API_KEY = "default-key"
TIMEOUT = 10

def get_setting(key):
    return f"Setting: {key}"


File: main.py

from config import *

TIMEOUT = 20

print(f"API Key: {API_KEY}")
print(f"Timeout: {TIMEOUT}")
print(get_setting('TIMEOUT'))
```

If you run python `main.py` from your terminal, what will be the output? Explain how the `from ... import *` statement and variable assignments in `main.py` interact to produce this result.

<details> 
<summary>Solution</summary> 
</details>

#### Exercise 6

Imagine a colleague is new to writing tests with Python's unittest framework. In a brief, conversational explanation (2-3 paragraphs), describe the following concepts to them:

- The SEAT approach for structuring a test.
- The purpose of the setUp and tearDown methods in a test class.
- What "code coverage" measures and why a high percentage is desirable but doesn't guarantee bug-free code.

<details> 
<summary>Solution</summary> 
</details>

#### Exercise 7

What does the following code print? Explain the behavior, specifically addressing why the output has the value it does.

```python
multipliers = []
for i in range(4):
    multipliers.append(lambda x: i * x)

print(multipliers[2](10))
```

<details> 
<summary>Solution</summary> 
</details>

#### Exercise 8

What does the following code output? Explain how the `process_items` function demonstrates the concept of a higher-order function.

```python
def process_items(items, operation):
    return [operation(item) for item in items]

def double(n):
    return n * 2

def to_string(n):
    return str(n)

numbers = [1, 2, 3]

result1 = process_items(numbers, double)
result2 = process_items(numbers, to_string)
result3 = process_items(numbers, lambda x: x % 2 == 0)

print(result1)
print(result2)
print(result3)
```

<details> 
<summary>Solution</summary> 
</details>


#### Exercise 9

You have created a small Python utility named `text_analyzer` that you want to share with your team so they can install it in their virtual environments using a command like `pip install ..`

Briefly outline the essential files and directory structure you would create for this project. Describe the purpose of each file or directory you mention. You do not need to write the contents of the files.

<details> 
<summary>Solution</summary> 
</details>

#### Exercise 10

Assume an empty file named `data.txt` exists before this script runs. What will be printed to the console? Explain why, paying close attention to the file's contents and the cursor's position at each step.

```python
with open('data.txt', 'w+') as f:
    f.write('first\n')
    f.write('second')
    content = f.read()
    print(f"Read after write: '{content}'")

    f.seek(0)
    all_content = f.read()
    print(f"Read after seek: '{all_content}'")

```

<details> 
<summary>Solution</summary> 
</details>

[Back to the top](#top)