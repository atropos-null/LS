# LS Bot Generated Questions for PY130


<a name="top"></a>

## Table of Contents

- [Purity, Side Effects and Nested Mutable Collections](#purity-side-effects-and-nested-mutable-collections)
- [Verbalization and Conceptual Precision](#verbalization-and-conceptual-precision)
- [Partial Function Application and Closures](#partial-function-application-and-closures)
- [Purity, Copying, and Nested Mutability](#purity-copying-and-nested-mutability)
- [Decorators](#decorators)
- [Mixed Assessment Transfer](#mixed-assessment-transfer)
- [Post Written Exam Malaise](#post-written-exam-malaise)
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
<summary>Solution</summary> 

1. After the code runs, has the `user_data` list or any of its contents been mutated? 

No. A new list was created and returned.

2. Explain your reasoning by identifying any aliases and tracing the path of any mutation that occurs. 

In the second line a new, empty list is created, `user_profiles = []` and in line 6 that local list is appended. 
`user_profiles.append(user_profile)` and returned.

3. Is the `process_recent_users` function pure or impure? Justify your answer. 

A new object is created and mutated, while the original argument is not mutated. Creating a new list, appending to it locally, reading the argument, and returning the new list are all compatible with purity.  Local mutation of a list you created inside the function is not a side effect, because nothing outside the function can observe it.

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

1. Is the `add_dependency` function pure? 

Yes. A new object is created with `project_copy = project.copy()`

2. Explain exactly why or why not by describing which objects are new, which are shared, and where any mutation occurs relative to the original
 `project_configs` data structure.

`updated_projects` is new. `project_copy` is new as well. No mutation relative to the original project_configs data structure is mutated.

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

```python
def add_item_to_inventory(inventory, category, item):
    new_inventory = inventory.copy()

    new_category = inventory[category].copy()
    new_tools = inventory[category]['tools'].copy()

    new_tools.append(item)
    new_category['tools'] = new_tools
    new_inventory[category] = new_category

    return new_inventory
```
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

1. After `generate_report(sensor_data)` is called, is the original `sensor_data` dictionary modified in any way? 
Yes.

2. If it is modified, describe the change. If not, explain why it remains unchanged. 
`data_points.sort()`

3. Is this function pure? Provide a brief justification. 

No, because data_points is sorted which leaves a side effect.
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

```python
def deactivate_user(users, user_id):

    result = []

    for user in users:
        if user['id'] == user_id:
            updated_user = user.copy()
            updated_user['is_active'] = False
            result.append(updated_user)
        else:
            result.append(user)
    return result

# --- Test Data ---
user_database = [
    {'id': 1, 'name': 'Dana', 'is_active': True},
    {'id': 2, 'name': 'Evan', 'is_active': True},
    {'id': 3, 'name': 'Frank', 'is_active': True},
]


tested = deactivate_user(user_database, 1)

print(tested is user_database)                    # False
print(tested[0] is user_database[0])              # False
print(tested[1] is user_database[1])              # True
print(tested[2] is user_database[2])              # True
```

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

1. After this code executes, is the `original_employees` data structure—including all its nested elements—in the same state as it was before 
the function call? 

No. 'devops" is now "DevOps".

2. Explain your answer by describing which objects, if any, are shared between `original_employees` and the returned grouped_data. Is the use of `.copy()` sufficient to prevent side effects in this case?

Copy only creates a top level copy, the inner elements still refer back to the original_employee collection, and it is insufficient to preventing side effects.

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

1. Predict the final value of the user dictionary after the function call.

{'username': 'testuser', 'preferences': {'theme': 'dark'}, 'notifications': {'push': True, 'email': True}}

2. Is `merge_user_settings` a pure function as implemented?

No. the user dictionary is modified.

3. Justify your answer by identifying any shared mutable objects between the original user dictionary and the returned `final_setting`s dictionary 
and explaining how a side effect occurs.

The inner elements of the dictionary are still referencing the original with the use of copy and these are modified. Deepcopy would have been useful.

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

```python
def add_project_to_employees(employees, employee_ids, project_name):

    new_employees = employees.copy()

    for employee_id, employee in employees.items():
        if employee_id in employee_ids:
            new_employee = employee.copy()
            new_projects = employee['projects'].copy()
            new_projects.append(project_name)
            new_employee['projects'] = new_projects
            new_employees[employee_id] = new_employee
    
    return new_employees
```

</details>

[Back to the top](#top)


### Verbalization and Conceptual Precision

#### Prompt 1 — Function Memory

Question:​ Casually explain what a closure is in Python. What information does the inner function retain access to after the outer function has finished executing?

Possible Follow-up:​ Is the value at that time copied, or is access to the binding itself retained?

<details> 
<summary>My Answer</summary> 

A closure "remembers" the variables from the scope where it was defined, even after that scope has finished executing. What makes a closure is 3 ingredients:

1. An inner, nested function.

```python

def outer(x):
    def inner(y):
        return x + y
    return inner
```

2. A variable from an enclosing scope that the inner function references (a "free" variable).
3. The enclosing function returns the inner one, so the inner function outlives the outer function.

If `inner` used no outside variables, it would just be a nested function and not an inner.  

Follow up: The access is a retained binding and not a copy.

</details>

####  Prompt 2 — Pre-configured Functions

Question:​ In your own words, what is partial function application? What kind of object does it create, and what is the relationship between the original function's parameters and the new function's parameters?

Possible Follow-up:​ Where does the "pre-filled" argument's state live?

<details> 
<summary>My Answer</summary> 

A partial function application is a function that binds some arguments now, supplies the rest later.

```python
from functools import partial

def add(a, b, c):
    return a + b + c

add_1_2 = partial(add, 1, 2)   # a and b locked in
print(add_1_2(10))             # 13
print(add_1_2(100))            # 103
```

You can do it manually! You don't need functools.

```python
def add(a, b, c):
    return a + b + c

def add_1_2(c):
    return add(1, 2, c)
```

</details>

#### Prompt 3 — Function Roles

Question:​ What is the distinction between a first-class function and a higher-order function? Can a function be both?

Possible Follow-up:​ Can you give an example of a common built-in Python function that is a higher-order function?

<details> 
<summary>My Answer</summary> 

A first class function is an object that can be:
1. **assigned** to a variable
2. **stored** inside another object
3. **passed** as an argument
4. **returned** from a function

It's an object that behaves normally as any other object in the Python ecosystem.

A higher-order function is a function that accepts one or more functions as arguments, and/or returns a function. 

Follow-up: Map and Filter! 

</details>


#### Prompt 4 — Purity and Effects

Question:​ What does it mean for a function to be "pure"? What must be true about both its return value and its interaction with the rest of the program?

Possible Follow-up:​ If a function has no side effects, is it guaranteed to be pure?

<details> 
<summary>My Answer</summary> 

A pure function has the same input --> same output, always. The return value depends only on the arguments. And there are no side effects, it doesn't change anything outside itself.

```python

def pure_add(a, b):
    return a + b

def impure_add(a,b):
    print(f"I'm now returning {a} + {b}")
    return a + b
```

Follow up: No. Both conditions need to be satisfied. A function can have zero side effects and still be impure if it violates not having contact with the outside scope.


</details>

#### Prompt 5 — I/O Side Effects

Question:​ Imagine a function that opens a text file, reads its first line, and returns it. Why is this considered a side effect, even if the function doesn't change the file?

Possible Follow-up:​ What external state is the function's behavior dependent on?

<details> 
<summary>My Answer</summary> 

In strict functional programming (Haskell, etc.), reading mutable external state is considered an effect. From the type system's point of view, the clock, the filesystem, and global variables are all "effectful" sources — you can't get a value out of them without marking the function as effectful.

In everyday Python vocabulary, "side effect" usually means "change," and "non-determinism" is called out separately. Under that looser definition, time.time() has no side effects but is still impure because it's non-deterministic.

</details>

#### Prompt 6 — Global State Side Effects

Question:​ Let's say you have a function that increments a global counter variable every time it's called. Explain why this action is categorized as a side effect.

Possible Follow-up:​ How does this side effect impact the predictability of the function?

<details> 
<summary>My Answer</summary> 

This action is categorized as a side effect because it has to reach outside of the scope of the function to work with this information. This violates the "no outside grabbing of anything" that is needed to satisfy the second rule of Function Purity.

Follow up: If the global variable's value changes the function's output also changes and thus becomes unreliable.

</details>

#### Prompt 7 — Mutation Side Effects

Question:​ Consider a function that takes a list of lists as an argument. It creates and returns a new top-level list, but it also sorts one of the inner lists in place. Why is this function considered impure?

Possible Follow-up:​ What is the term for having multiple variables that refer to the same object?

<details> 
<summary>My Answer</summary> 

Modifying mutable objects passed as an argument, in this case the inner list, is the third category of side effects after I/O operations and Global State modfication.

Follow up: Aliasing.

</details>

#### Prompt 8 — System and Exception Side Effects

Question:​ Besides I/O, global state, and mutation, what are some other categories of side effects? For instance, why might interacting with the system clock or raising an exception be considered side effects?

Possible Follow-up:​ How does raising an exception alter the program's normal control flow?

<details> 
<summary>My Answer</summary> 

The remaining two categories are system interaction and exception handling. System interaction requires reaching outside of the function's scope and gaining something. Exception handling is a border case, but is considered not so pure because it requires a "non local exit" -- a way for a function to communicate and transfer control beyond its return value.

Follow up: Return values flow to the immediate caller. Exceptions flow sideways and upwards, to whoever wrote a matching except. That's a communication mechanism separate from the return path — another form of effect.

</details>


#### Prompt 9 — The nonlocal Keyword

Question:​ What is the fundamental difference between using the nonlocal keyword to reassign a variable in a parent scope, and simply mutating a list object that was defined in that same parent scope?

Possible Follow-up:​ What does nonlocal allow you to change: the object, or what the name is bound to?

<details> 
<summary>My Answer</summary> 

The nonlocal keyword allows a nested function to modify variables in the nearest enclosing scope that is not global. It tells Python that the variable is not local to the current function. 

`nonlocal` reassignment changes which object a name in the parent scope refers to. Mutating a list changes the internal state of the object the name already refers to. One is a change of reference, the other a change of state. That's

</details>

#### Prompt 10 — Decorator Mechanics

Question:​ When you apply a decorator to a function, what happens at decoration time? After the decoration, what object does the original function name actually refer to?

Possible Follow-up:​ Does the original, undecorated function still exist somewhere?

<details> 
<summary>My Answer</summary> 

At decoration time the decorator runs once with the original function and returns a replacement. The original name is then rebound to the replacement.

Follow-up: the original still exists inside the wrapper's closure, but the name no longer points to it.

</details>

#### Prompt 11 — Decorator Application Order

Question:​ If you stack two decorators on top of a function, in what order are they applied? For example, if you have `@decorator_A` on the first line and `@decorator_B` on the second line above `my_func`, which decorator runs first?

Possible Follow-up:​ Which decorator's returned function is called when you finally invoke `my_func`?

<details> 
<summary>My Answer</summary> 

```python

@a
@b
def my_func():
    pass
```

is actually:
```python
def f():
    ...
f = a(b(f))
```

`b`, the decorator closest to the function is applied first, runs first and then `a` wraps whatever `b` returns. The final result is bound to `my_func`. When you *call* `my_func`, you enter `a` wrapper, then `b` wrapper, and then calling `my_func`. It then exits the reverse, going out to `b` and then to `a`.

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

Processing financial data in 'quarterly': Q4-report

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

1. What is the output of this script?
```
0
10
1
2
11
```

2. After all the code has run, what value is retained by the closure referred to by the `counter_b` variable? Explain briefly why this value survives even after the initial call to `make_counter(10`) has completed.

12 is retrained by the `counter_b` variable

`make_counter(10)` creates a local variable count initialized to 10, and returns the inner function counter. That inner function references count, so Python stores count in a closure cell shared between make_counter and the returned counter.

When `make_counter(10)` finishes, its stack frame goes away — but the closure cell does not, because `counter_b` still holds a reference to counter, and counter holds a reference to that cell. So count survives. So the last returned value was 11, but the retained value inside the closure is 12.

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

```python
import datetime
from functools import partial

def log_message(level, source, message, *, timestamp=None):
    ts = timestamp or datetime.datetime.now()
    return f"[{ts}] {level.upper()} ({source}): {message}"

system_error_log = partial(log_message, "ERROR","SYSTEM_CORE")
```
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

Running 'Database backup' with 'high' priority. [Notifying admin]
Running 'Cleanup temp files' with 'low' priority. [Notifying admin]

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

[105, 112]

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

When this new function is called with its own set of positional and keyword arguments, it should invoke the original func, passing the combination of the initially provided arguments and the newly provided arguments. Arguments provided at the final invocation should take precedence (specifically, later keyword arguments override earlier ones).

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

```python
def apply_partially(func, *p_args, **p_kwargs):
    def partial(*new_args, **new_kwargs):
        combined_kwargs = {**p_kwargs, **new_kwargs}
        return func(*p_args, *new_args, **combined_kwargs)
    return partial
```

</details>

[Back to the top](#top)

### Purity, Copying, and Nested Mutability

#### Problem 1 — Data Processing Side Effects

Consider the following function `select_and_tag`, which is intended to select a user record and add a 'processed' tag to it.

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


<details> 
<summary>Solution</summary> 

1. Is the `select_and_tag` function a pure function?

No, its not pure.

2. Explain your reasoning. In your explanation, describe what object or objects, if any, are mutated.

Purity is not about whether the mutation is the function’s intended purpose. It’s about whether the function has an observable effect beyond returning a value. The point of the object is to mutate the user_data object.


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

Yes.

2. Explain ​why​ the shallow copy strategy used here is or is not sufficient to prevent side effects on the original profiles data. Your explanation should focus on the types of values contained within the user dictionaries.

It is sufficient since values are strings and booleans.

<details> 
<summary>Solution</summary> 
</details>


#### Problem 3 — Implementing a Pure Transformation

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

```python
def add_feature_module(all_projects, project_id, module_name):
    new_projects = []

    for project in all_projects:
        if project['id'] == project_id:
            new_project = project.copy()
            new_project['modules'] = project['modules'] + [module_name]
            new_projects.append(new_project)
        else:
            new_projects.append(project)

    return new_projects
```

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

<details> 
<summary>Solution</summary> 


1. Describe the sequence of events that occurs when this script is executed, from top to bottom.

"Script is starting"
"Decorating greet"
"Script has defined greet"
"Hello from greet"
"Script has called greet"

2. What object is passed as an argument to `trace_decorator`?

The function object created by def greet, i.e. the original greet function, is passed as the single argument func.

3. When does the print statement inside `trace_decorator` execute?

At decoration time — i.e., right after the def greet statement runs, at module load, before any call to greet() ever happens.  the print runs once, when the module is being defined. It does not run each time greet() is called. If you called greet() 100 times, Decorating greet... would still only appear once.


4. After the `@trace_decorator` line is processed, what object does the name greet refer to?

greet is rebound to whatever trace_decorator returned. Since this decorator returns func unchanged, greet still refers to the same original function object.

5. What happens when `greet()` is called on line 12?

Because trace_decorator returned the original function unchanged, greet() calls the original function directly

</details>

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

<details> 
<summary>Solution</summary> 

1. In what order are the decorators (`add_one`, `multiply_by_two`) executed at decoration time?

multiply_by_two is applied first — it's closest to the def, so it receives the original get_number and returns its wrapper.

add_one is applied second — it receives the wrapper that multiply_by_two returned, and returns its own wrapper.

2. When `get_number()` is called, in what order do the print statements from the wrapper functions appear?

```
add_one wrapper before call
multiply by two wrapper before call
multiply by two wrapper after call
add one wrapper after call
```

3. Trace the return value from the original `get_number` function as it passes back through the decorator wrappers. 
What is the final value assigned to `final_result`? Explain each step of the calculation.

```
original:            return 10
multiply_by_two:    10 * 2 = 20
add_one:            20 + 1 = 21
final_result = 21
```

</details>

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

<details> 
<summary>Solution</summary> 

1. What happens when the line `@DecoratorClass` is executed during script loading? Describe the process.

The `def display_info` statement creates the original function object and binds the name `display_info` to it. Then Python applies the decorator:
```display_info = DecoratorClass(display_info)``` That calls `DecoratorClass.__init__` with the original function as `original_function`

Then, `print("DecoratorClass __init__ called.")` runs.

`self.original_function = original_function` stores the original function on the new instance.

`__init__` returns None, and Python's class-call machinery returns the newly created instance of `DecoratorClass`.

Finally, the name `display_info` is rebound to that instance. This all happens once, at decoration time — before print("About to call display_info...") runs.

2. After decoration, what kind of object does the name `display_info` refer to?

It refers to an instance of DecoratorClass, not the original function.

3. Where is the original `display_info` function object stored?

Inside the DecoratorClass instance, as the attribute self.original_function.

4. What causes the `__call__` method of `DecoratorClass` to be executed?

The call expression ```display_info("Alice", 30)```

</details>

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

1. After the `@CallCounter` decoration is complete, what object does the name `say_hello` refer to?

An instance of CallCounter — not the original function.

2. Where is the call count (the value of `self.count`) stored?

In the instance attribute self.count, i.e. in the instance's __dict__

3. Why does the count persist across multiple calls to `say_hello`?

Because there is one instance created at decoration time, and that instance lives for as long as the name say_hello is bound — typically the whole lifetime of the module.

4. If you created another decorated function, such as `@CallCounter` `def say_goodbye()`, would it share the same call count as `say_hello?` Why or why not?

No — each decoration creates a separate instance with its own count.

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

1. What will the two print statements output?

Config 1: {'version': 'v1.2', 'setting_a': 25, 'setting_b': 100, 'theme': 'dark', 'is_production': True}
Config 2: {'version': 'v1.2', 'setting_a': 50, 'setting_b': 200, 'theme': 'dark', 'is_production': False}

2. Explain precisely how the arguments for the `config2` call are bound to the parameters of the `build_config` function.

version ← partial's positional 'v1.2' (fits the positional-only slot)

setting_a ← caller's positional 50

setting_b ← caller's keyword 200

theme ← partial's keyword 'dark'

is_production ← default False

The partial's job is simply to prepend its stored positional arguments and merge its stored keywords (caller wins) before handing everything to build_config.

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

1. What is the final line of output printed to the console?

Logged: INIT. History size: 1
Logged: START. History size: 1
Logged: PROCESS. History size: 2
Logged: END. History size: 2


2. What is the value of the `final_history` variable after all the code has run?

['START', 'END']

3. Explain why the history for `logger1` is separate from the history for `logger2`.

logger1 and logger2 are separte function objects and each has their own events list. 

4. If `final_history.append("EXTRA")` is executed afterward, would that affect the state retained by logger2? Explain.

Yes, because it is the function object of logger2. The end would be "['START', 'END', 'EXTRA']"
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

Trace the execution and predict the final line of output printed by this script.

State the governing rule aloud in one or two sentences.

<details> 
<summary>Solution</summary> 

```python
def modify_state(data_list): 
    print("Function start: Modifying data...")
    local_copy = data_list.copy() #only a shallow copy, references are original references. 

    # Modify a nested list through the original reference
    data_list[0].append('X') #[[1, 'X'], [2,3]]

    # Modify the outer list through the local copy
    local_copy.append([4, 5]) #Local copy only modified: [[1, 'X'], [2,3,4,5]]. Original stays: [[1, 'X'], [2,3]]
    print("Function end.")  #Function End. 

state = [[1], [2, 3]]
modify_state(state) #Function start: Modifying data...
print(f"Final state: {state}") #[[1, 'X'], [2,3]]
```

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

1. List everything that will be printed to the console, in the order it is printed.
Processed 1
Processed 6
Processed 3
Processed 8
Final results: [False, True, False, True]
Log: [2, 12, 6, 16]

2. What is the final value of `final_results`?

[False, True, False, True]

3. What is the final value of `side_effects_log`?

[2, 12, 6, 16]

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

Calling 'calculate_sum' with args: (15, 25)
'calculate_sum' returned: 40
Final result received: 40

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

```
Line 1
Line 2
Line 3
```

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

Script: Generator created.
Script: About to take first item.
Generator: Starting to open file.
Generator: Yielding 'Line 1'
Script: Got 'Line 1'.
Script: About to consume the rest.
Generator: Yielding 'Line 2'
Generator: Yielding 'Line 3'
Generator: Execution finished or resource closed.
Script: Got remaining lines: ['Line 2', 'Line 3']

</details>

[Back to the top](#top)

### Post Written Exam Malaise

#### Exercise 1

Contract:

Write a function that accepts a string as a required first argument, an integer as an optional second argument with a default value of 10, and a boolean as a required keyword-only third argument. The first two arguments must be positional-only. The function should return a formatted string indicating the values received.


Assertions:
```python
# Function definition goes here

# Test cases
assert process_data("example", 15, verbose=True) == "Data: example, Level: 15, Verbose: True"
assert process_data("default level", verbose=False) == "Data: default level, Level: 10, Verbose: False"
assert process_data("another", 5, verbose=False) == "Data: another, Level: 5, Verbose: False"

# The following calls should raise a TypeError due to argument rules:
# process_data(data="example", 15, verbose=True)
# process_data("example", width=15, verbose=True)
# process_data("example", 15, True)

```

<details> 
<summary>Solution</summary> 
</details>


#### Exercise 2

Contract:
Write a function that requires at least two positional arguments, and can accept any number of additional positional arguments. The function must also accept an optional keyword-only argument named transform which should be a callable. If transform is provided, it should be applied to each argument before they are combined. The function should return a list containing all the processed arguments.

Assertions:
```python
# Function definition goes here

# Test cases
assert combine_items(1, 2) == [1, 2]
assert combine_items("a", "b", "c", "d") == ["a", "b", "c", "d"]
assert combine_items(10, 20, 30, transform=str) == ["10", "20", "30"]
assert combine_items("apple", "banana", transform=str.upper) == ["APPLE", "BANANA"]

# The following call should raise a TypeError because it provides fewer than two positional arguments:
# combine_items(1)
```

<details> 
<summary>Solution</summary> 
</details>


Exercise 3

Contract:
Write a function that accepts a single positional argument, base, and any number of keyword arguments. The function should return a dictionary that contains all the keyword arguments provided, plus a status key with a value of 'processed' if the base argument is greater than 100, or 'pending' otherwise.

Assertions:
```python
# Function definition goes here

# Test cases
result1 = build_report(200, user="admin", level=5)
assert result1 == {"user": "admin", "level": 5, "status": "processed"}

result2 = build_report(50, user="guest", retries=3)
assert result2 == {"user": "guest", "retries": 3, "status": "pending"}

result3 = build_report(101)
assert result3 == {"status": "processed"}
```


<details> 
<summary>Solution</summary> 
</details>

#### Exercise 4

Contract:
Write a higher-order function that accepts a callable operation and a variable number of positional arguments (*args). It must also accept any number of keyword arguments (**kwargs). The function should invoke the operation callable, passing all *args and **kwargs to it, and return the result.


Assertions:
```python
# Function definition goes here

def add(a, b):
    return a + b

def describe(name, role="user"):
    return f"{name} is a {role}."

# Test cases
assert dispatch(add, 5, 10) == 15
assert dispatch(describe, "Alice", role="admin") == "Alice is a admin."
assert dispatch(describe, "Bob") == "Bob is a user."
assert dispatch(max, [10, 40, 20]) == 40
```

<details> 
<summary>Solution</summary> 
</details>

#### Exercise 5

Contract:
Write a function that takes a base number. It returns a new function. This returned function takes a single argument, a callable, which it applies to the base number, and returns the result.

Assertions:
```python
# Function definition goes here

import math

# Test cases
apply_to_10 = create_applicator(10)
assert apply_to_10(lambda x: x * 2) == 20
assert apply_to_10(lambda x: x + 5) == 15
assert apply_to_10(math.sqrt) == 3.1622776601683795

apply_to_25 = create_applicator(25)
assert apply_to_25(math.sqrt) == 5.0
```

<details> 
<summary>Solution</summary> 
</details>


#### Exercise 6

Contract:
Write a function named create_specialized_multiplier. It must accept keyword arguments that will be stored for later use. It returns a new function. The returned function accepts a single required positional argument number and multiplies it by the value associated with the factor key from the originally provided keyword arguments. If factor was not provided at creation time, the returned function should raise a ValueError.

Assertions:
```python
# Function definition goes here

# Test cases
double = create_specialized_multiplier(factor=2)
assert double(5) == 10
assert double(10) == 20

triple = create_specialized_multiplier(factor=3, other_data="ignored")
assert triple(5) == 15

# Test for ValueError
error_raised = False
try:
    bad_multiplier = create_specialized_multiplier(unrelated_key=5)
    bad_multiplier(10)
except ValueError:
    error_raised = True
assert error_raised
```
<details> 
<summary>Solution</summary> 
</details>



#### Exercise 7

Contract:
Write a function that behaves differently based on the arguments provided. If it is called with two arguments (a string text and a dictionary subs), it should immediately perform substitutions on the string using the dictionary and return the result. If it is called with only the text string, it should return a new function.[12:33 PM]This new function accepts a dictionary subs and performs the substitutions on the original text.

Assertions:
```python
# Function definition goes here

# Test immediate computation
template = "Hello, {name}! Welcome to {place}."
substitutions = {"name": "Alex", "place": "Launch School"}
assert format_template(template, substitutions) == "Hello, Alex! Welcome to Launch School."

# Test deferred computation
formatter = format_template("Your code is {status}.")
assert formatter({"status": "ready"}) == "Your code is ready."
assert formatter({"status": "pending"}) == "Your code is pending."
```

<details> 
<summary>Solution</summary> 
</details>

#### Exercise 8

Contract:
Write a function that creates a configurable counter. The function accepts an initial value and a step value. It returns a new function. Each time the new function is called, it should return the current value of its counter and then increment its internal counter by step. The counters must be independent.

Assertions:
```python
# Function definition goes here

# Test cases
counter1 = make_counter(initial=0, step=2)
assert counter1() == 0
assert counter1() == 2
assert counter1() == 4

counter2 = make_counter(initial=100, step=-10)
assert counter2() == 100
assert counter2() == 90

# Verify independence
assert counter1() == 6
```

#### Exercise 9

Contract:

Write a function, create_pipeline, that accepts a variable number of functions as positional arguments. It returns a new function, the pipeline_runner. The pipeline_runner accepts a single initial value. It then passes this value to the first function in the pipeline, takes the result and passes it to the second function, and so on, finally returning the result from the last function.

Assertions:
```python
# Function definition goes here

def add_five(x):
    return x + 5

def multiply_by_two(x):
    return x * 2

def to_string(x):
    return str(x)

# Test cases
pipeline1 = create_pipeline(add_five, multiply_by_two)
assert pipeline1(10) == 30 # (10 + 5) * 2

pipeline2 = create_pipeline(multiply_by_two, to_string, add_five)
# This will fail with a TypeError because `add_five` will be called with a string.
# The contract is to simply call them in order.
# Let's create a pipeline that works.
def string_add_five(s):
    return s + "5"

pipeline3 = create_pipeline(multiply_by_two, to_string, string_add_five)
assert pipeline3(20) == "405" # (20 * 2) -> "40" -> "40" + "5"
```

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

```python
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