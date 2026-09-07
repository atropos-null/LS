# LS Bot Generated Questions for PY130

<a name="top"></a>

## Table of Contents


- [First Class and Higher-Order Functions](#first-class-and-higher-order-functions)
- [Lambdas](#lambdas)
- [Generators, on your own practice](#generators-on-your-own-practice)
- [Generators, on your own practice 2](#generators-on-your-own-practice-2)
- [Generators, team practice](#generators-team-practice)
- [Generators and Files](#generators-and-files)
- [Arguments and Parameters](#arguments-and-parameters)
- [Iterable Unpacking](#iterable-unpacking)
- [Closure Practice](#closure-practice)
- [Closure Practice 2](#closure-practice-2)
- [Decorator Practice 1](#decorator-practice-1)
- [Decorator Practice 2](#decorator-practice-2)
- [Decorator Practice 3](#decorator-practice-3)
- [Decorator Practice 4](#decorator-practice-4)

## Lesson 1: Functions, Generators, and Files

### First Class and Higher Order Functions


#### Question 1

Difficulty:​ Basic
Objective:​ Understand and trace a simple iteration within a class method before introducing higher-order functions. This will establish a baseline for comparison.

Problem Statement:

Consider the following Book and Library classes. The Library class has a print_authors method that iterates through its collection of books and prints the author of each book.

Your task is to carefully trace the execution of the provided code and predict the exact output. Please provide your predicted output.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class Library:
    def __init__(self, title):
        self.title = title
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_authors(self):
        print(f"Authors at {self.title}:")
        for book in self.books:
            print(f"- {book.author}")

# Setup
my_library = Library("City Central Library")
my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
my_library.add_book(Book("1984", "George Orwell"))

# Execution
my_library.print_authors()
```


<details> 
<summary>Possible Solution</summary> 

A library object is created called my_library, with the title of "City Central Library". Then we have 3 separate book objects created and 
appended to the self.books list attribute. The `my_library `object then calls the print_authors method on the Library object. It prints 

```"Authors at City Central Library"
- F.Scott Fitzgerald
- Harper Lee
- George Orwell
```

</details>

#### Question 2

Difficulty:​ Easy
Objective:​ Refactor an explicit loop into `each()`-style iteration and think about what the object vs. the callback is responsible for.

Problem Statement:  You are given a `TodoList` class that stores `Todo` objects. It has a method that prints the description of every todo.

Here is the explicit-loop version:

```python

class Todo:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)

    def print_descriptions(self):
        for todo in self.todos:
            print(todo.description)
 ```

Refactor print_descriptions so that it uses an each-style higher-order method instead of an explicit for loop.

Since Python does not have a built-in `each()` method on lists, you may either:

•   write a helper method named each on TodoList, or
•   describe how you would structure it if such a method existed.

What I want from you

1.  Show your refactored version.
2.  Explain whether the refactor makes the code clearer or less clear.
3.  Describe:
    •   what objects exist,
    •   what object owns the iteration,
    •   what object owns the callback,
    •   what object performs the computation.


<details> 
<summary>Possible Solution</summary> 

```python
class Todo:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def __str__(self):
        return self.description

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)

    def each(self, callback):
        for todo in self.todos:
            callback(todo)

    def print_descriptions(self):
         self.each(lambda todo: print(todo))



my_list = TodoList()
todo_1 = Todo("eat")
todo_2= Todo("sleep")
my_list.add(todo_1)
my_list.add(todo_2)
my_list.print_descriptions()
```

​Objects Involved​:
- One `TodoList` instance (`my_list`).
- Two `Todo` instances (`todo_1`, `todo_2`).
- One lambda function object, created ephemerally when print_descriptions is called.
- ​Who Owns the Iteration?​: The `TodoList` object. The for loop logic is encapsulated within its each method.
- ​Who Owns the Callback?​: The calling context, in this case, the print_descriptions method, creates and provides the callback.
- ​Who Performs the Computation?​: The callback function `(lambda todo: print(todo.description)`). It takes a todo object and performs the `print()` action.

The key takeaway is the ​separation of concerns​. The TodoList is responsible for the iteration logic, while the caller (print_descriptions) is responsible for the action performed during the iteration.

</details>

#### Question 3

Difficulty:​ Easy-to-Medium
Objective:​ Recognize when `select()` is a better fit than an explicit loop, and trace how a callback controls filtering.

Problem Statement: You have a `TaskList` class that stores `Task` objects. Each task has a done status.

Here is an explicit-loop version of a method that returns only the unfinished tasks:

```python
class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done


class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def unfinished_tasks(self):
        result = []
        for task in self.tasks:
            if not task.done:
                result.append(task)
        return result
 ```

 Your Tasks

1.  Refactor unfinished_tasks to use a higher-order function style.
2.  Decide whether select()-style iteration is clearer here than keeping the explicit loop.
3.  Explain:
    - what objects exist,
    - what object owns the iteration,
    - what object owns the callback,
    - what object performs the filtering decision.

Important

- Don’t use `filter()` yet unless you want to compare it to `select()` conceptually.
- Don’t introduce any later-lesson concepts.

<details> 
<summary>Possible Solution</summary> 


```python

class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done


class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def unfinished_tasks(self):
        return self.select(lambda task: not task.done)
    
    def select(self, callback):
        selected = []

        for item in self.tasks:
            if callback(item):
                selected.append(item)

        return selected
    

my_list = TaskList()
todo_1 = Task("eat")
todo_2= Task("sleep")
my_list.add(todo_1)
my_list.add(todo_2)
my_list.unfinished_tasks()
```

Currently with only one reason to iterate, it is not clearer to use select. The explicit loop is just fine. 

- One `TaskList` instance (`my_list`).
- Two `Task` instances (`todo_1`, `todo_2`).
- One lambda function object, created ephemerally when unfinished_tasks is called.
- Who Owns the Iteration?​: The `TaskList` object. The for loop logic is encapsulated within its select method.
- ​Who Owns the Callback?​: The calling context, in this case, the unfinshed_task method, creates and provides the callback.
- ​Who Performs the Computation?​: The callback function `lambda task: not task.done`. The select method then ​uses​ the True or False result from the callback to decide whether to append the task to the selected list. So, the callback makes the decision, and select acts on it.

</details>


#### Question 4

Difficulty:​ Medium

Objective:​ Predict the output of code that uses both `each()` and `select()` together, and trace the control flow through multiple callbacks.

Problem Statement: Here is a complete, runnable program. Read it carefully and predict the exact output.

```python
class Todo:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def __str__(self):
        return f"[{'X' if self.done else ' '}] {self.description}"


class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)

    def each(self, callback):
        for todo in self.todos:
            callback(todo)

    def select(self, callback):
        selected = []
        for todo in self.todos:
            if callback(todo):
                selected.append(todo)
        return selected

    def done_todos(self):
        return self.select(lambda todo: todo.done)


my_list = TodoList()
my_list.add(Todo("Write tests", done=True))
my_list.add(Todo("Run tests"))
my_list.add(Todo("Deploy app", done=True))
my_list.add(Todo("Write docs"))

finished = my_list.done_todos()
print(f"Finished todos: {len(finished)}")

my_list.each(lambda todo: print(todo))
```

1.  Predict the exact output, line by line.
2.  Trace the control flow step by step. Specifically, explain what happens each time the callback inside each() and select() is called.
3.  Identify what object is driving the execution at each stage.

<details> 
<summary>Possible Solution</summary> 

```python
class Todo: #A Todo Class, creating todo objects that have a description and a flag if its done or not, set to false initially.
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def __str__(self): #a str that returns if the todo object's done attribute is marked True, otherwise just the description
        return f"[{'X' if self.done else ' '}] {self.description}"


class TodoList: #A TodoList Class that creates an object that holds Todo Objects
    def __init__(self):
        self.todos = [] #List that holds the todos and is iterated upon later.

    def add(self, todo): #appends a Todo object to self.todos
        self.todos.append(todo)

    def each(self, callback): #a higher order function that initiates the iteration of self.todos
        for todo in self.todos:
            callback(todo)

    def select(self, callback): #a higher order function that appends self.todo items to a new list
        selected = []
        for todo in self.todos:
            if callback(todo):
                selected.append(todo)
        return selected

    def done_todos(self): #utilizes the select method and specifically a lambda to retrieve self.todo items marked done = True
        return self.select(lambda todo: todo.done)


my_list = TodoList() #a TodoList object created
my_list.add(Todo("Write tests", done=True)) #A Todo object created, flagged true and added to the TodoList Object
my_list.add(Todo("Run tests")) #A Todo object created and added to the TodoList Object
my_list.add(Todo("Deploy app", done=True)) #A Todo object created, flagged true and added to the TodoList Object
my_list.add(Todo("Write docs")) #A Todo object created and added to the TodoList Object

finished = my_list.done_todos()  #See Below
print(f"Finished todos: {len(finished)}") #Prints a string with the length of the list with the variable label "finished"

my_list.each(lambda todo: print(todo)) #See Below
```

`finished = my_list.done_todos()` assigns variable name 'finished' to the returned list of todo objects with a True flag.  It invokes the select function which uses the lambda todo: todo.done as it's callback function. The select method then ​uses​ the True or False result from the callback to decide whether to append the task to the selected list. So, the callback makes the decision, and select acts  on it.

`my_list.each(lambda todo: print(todo))` invokes the function to print out the elements of the `self.todos` list, which then involves the Todo Object's str to print.  

Output:
```
Finished todos: 2
[X] Write tests
[ ] Run tests
[X] Deploy app
[ ] Write docs
```

</details>

#### Question 5

Difficulty:​ Medium
Objective:​ Decide whether an explicit loop or `select()` is the clearer choice, and refactor only when it improves the design.

Problem Statement​: You have a `TaskBoard` class that stores `Task` objects. Each task has a priority number, where lower numbers mean higher priority.

Here is an explicit-loop method:

```python
class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority


class TaskBoard:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def urgent_tasks(self):
        result = []
        for task in self.tasks:
            if task.priority <= 2:
                result.append(task)
        return result
 ```

 Your tasks

1.  Refactor urgent_tasks using select()-style iteration.
2.  Explain whether that refactor is clearer than the explicit loop in this case.
3.  Describe:
    - what objects exist,
    - what object owns the iteration,
    - what object owns the callback,
    - what object performs the filtering decision.

Important: 
    - Don’t use any later-lesson concepts.
    - Keep the lambda simple.
    - If you think the explicit loop is clearer, say so and explain why.

<details> 
<summary>Possible Solution</summary> 

```python
class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.description} has priority {self.priority}"

class TaskBoard:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def select(self, callback): 
        selected = []
        for task in self.tasks:
            if callback(task):
                selected.append(task)
        return selected

    def urgent_tasks(self):
        return self.select(lambda task: task.priority <= 2)

my_list = TaskBoard()
my_list.add(Task("Write tests", priority=1)) 
my_list.add(Task("Run tests", priority=2)) 
my_list.add(Task("Deploy app", priority=3)) 
my_list.add(Task("Write docs", priority=4))
high_priority = my_list.urgent_tasks()

for item in high_priority:
    print(item)
```

1. Refactor urgent_tasks using select()-style iteration.
    See Above

2. Explain whether that refactor is clearer than the explicit loop in this case.

    The refactor is not clearer if there's only one method calling upon it.

3. Describe:
    - what objects exist: A TaskBoard object holding 4 Task objects.
    - what object owns the iteration: TaskBoard owns the iteration
    - what object owns the callback: TaskBoard owns the callback
    - what object performs the filtering decision: Task performs the filtering decision through the lambda
    
</details>

[Back to the top](#top)

### Lambdas

30 exercises to help you practice writing lambda expressions. Here is the setup code that will be used for these exercises:

```python

# --- Setup Code ---

# A simple list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# A list of strings
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# A list of dictionaries, representing people
people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
    {'name': 'Diana', 'age': 25, 'city': 'New York'},
]

# A list of tuples, representing products (name, price, quantity)
products = [
    ('Laptop', 1200, 5),
    ('Mouse', 25, 10),
    ('Keyboard', 75, 8),
    ('Monitor', 300, 3),
]

# A simple class for Task objects
class Task:
    def __init__(self, description, priority, completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed
    def __repr__(self):
        # A helper method to make printing tasks cleaner
        status = "X" if self.completed else " "
        return f"Task: '{self.description}' (P:{self.priority}) [{status}]"

# A list of Task objects
tasks = [
    Task('Buy groceries', 2, completed=False),
    Task('Clean the house', 1, completed=True),
    Task('Do laundry', 3, completed=False),
    Task('Walk the dog', 1, completed=False),
]

# A custom select function, similar to filter
def select(callback, iterable):
    return [item for item in iterable if callback(item)]

# --- End of Setup ---
```

Exercises:

```python
#To Complete, drop each line into print() and then fill out the ...:

list(map(..., numbers)) # Return each number squared.
list(filter(..., numbers)) # Keep only the even numbers.
sorted(words, key= ...) # Sort the words by length.
list(map(... , words)) # Return the uppercase version of each word.
select(... , tasks) # Keep only the completed tasks.
max(people, key=...) # Find the person with the highest age.
sorted(products, key=...) # Sort the products by price (the second element in the tuple).
list(map(... , people)) # Return a list of just the names of the people.
list(filter(... , numbers)) # Keep numbers that are greater than 5.
list(map(..., products)) # For each product, return its total value (price * quantity).
sorted(tasks, key=...) #Sort tasks by their priority.
list(filter(... , words)) # Keep only the words that start with the letter 'c'.
list(filter(... , people)) # Keep people who are 25 years old.
list(map(..., numbers)) # Return True for even numbers and False for odd numbers.
sorted(people, key=... )# Sort people by city name.
select(...  , tasks) # Keep only the tasks that are not completed.
list(filter(..., words)) # Keep words with a length of 5 or more.
list(map(... , tasks)) # Return just the description of each task.
list(filter(..., numbers)) # Keep numbers that are divisible by 3.
sorted(products, key=... , reverse=True) # Sort products by quantity, from highest to lowest.
list(filter(..., people)) # Keep people whose name is longer than 5 characters.
list(map(..., words)) # Return the length of each word.
list(filter(... , tasks)) # Keep tasks with a priority of 1.
max(words, key=... ) # Find the longest word.
list(filter(... , people)) # Keep people who live in 'New York' and are older than 25.
select(..., tasks) # Keep tasks that are incomplete and have a priority of 2 or higher.
sorted(people, key=...) #Sort people first by age, then by name.
list(filter(..., products)) # Keep products where the price is less than 100 or the quantity is 10 or more.
list(map(..., people)) #Return a string for each person: "Name is Age years old".
```


<details> 
<summary>Answer Key</summary> 

```python
list(map(lambda number: number**2, numbers)) # Return each number squared.
list(filter(lambda number: number % 2 == 0, numbers)) # Keep only the even numbers.
sorted(words, key=len) # Sort the words by length.
list(map(lambda word: word.title(), words)) # Return the uppercase version of each word.
#alternatively 
list(map(str.title, words))
select(lambda task: task.completed, tasks, tasks) # Keep only the completed tasks.
max(people, key=lambda person: person["age"]) # Find the person with the highest age.
sorted(products, key=lambda tup: tup[1]) # Sort the products by price (the second element in the tuple).
list(map(lambda person: person["name"], people)) # Return a list of just the names of the people.
list(filter(lambda number: number > 5 , numbers)) # Keep numbers that are greater than 5.
list(map(lambda product: product[1] * product[2], products)) # For each product, return its total value (price * quantity).
sorted(tasks, key=lambda task: task.priority) #Sort tasks by their priority.
list(filter(lambda word: word.startswith("c"), words)) # Keep only the words that start with the letter 'c'.
list(filter(lambda person: person['age'] == 25, people)) # Keep people who are 25 years old.
list(map(lambda number: number % 2 == 0, numbers)) # Return True for even numbers and False for odd numbers.
sorted(people, key=lambda person: person['city']) # Sort people by city name.
select(lambda task: not task.completed, tasks) # Keep only the tasks that are not completed.
list(filter(lambda word: len(word) > 5, words)) # Keep words with a length of 5 or more.
list(map(lambda task:  task.description, tasks)) # Return just the description of each task.
list(filter(lambda number: number % 3 == 0, numbers)) # Keep numbers that are divisible by 3.
sorted(products, key=lambda product: product[2], reverse=True)# Sort products by quantity, from highest to lowest.
list(filter(lambda person: len(person['name']) > 5, people)) # Keep people whose name is longer than 5 characters.
list(map(lambda word: len(word), words)) # Return the length of each word.
list(filter(lambda task: task.priority == 1 , tasks)) # Keep tasks with a priority of 1.
max(words, key=len ) # Find the longest word.
list(filter(lambda person: person['city'] == 'New York' and person['age'] > 25 , people)) # Keep people who live in 'New York' and are older than 25.
select(lambda task: not task.completed and task.priority >= 2, tasks) # Keep tasks that are incomplete and have a priority of 2 or higher.
sorted(people, key=lambda person: (person['age'], person['name']))#Sort people first by age, then by name.
list(filter(lambda product: product[1] < 100 or product[2] >= 10, products)) # Keep products where the price is less than 100 or the quantity is 10 or more.
list(map(lambda person: f"{person['name']} is {person['age']} years old", people)) #Return a string for each person: "Name is Age years old".
```

</details>

[Back to the top](#top)

### Generators, on your own practice

#### Exercise 1: Generate Squares

Problem Statement:​ Create a generator function that yields the square of each number from a given iterable of numbers.

Function Signature: ``` def generate_squares(iterable):```

Test Cases:

```python
assert list(generate_squares([1, 2, 3, 4, 5])) == [1, 4, 9, 16, 25]
assert list(generate_squares(range(6))) == [0, 1, 4, 9, 16, 25]
assert list(generate_squares([])) == []
assert list(generate_squares([-1, -2, 0])) == [1, 4, 0]
```

<details> 
<summary>Possible Solution</summary> 

```python
def generate_squares(iterable):

    for number in iterable:
        yield number ** 2
```
</details>

#### Exercise 2: Reverse Sequence

Problem Statement:​ Create a generator function that yields numbers in reverse order from a given start number down to 0, inclusive.

Function Signature: ```def reverse_sequence(start):```

Test Cases:

```python
assert list(reverse_sequence(5)) == [5, 4, 3, 2, 1, 0]
assert list(reverse_sequence(1)) == [1, 0]
assert list(reverse_sequence(0)) == [0]
assert list(reverse_sequence(-1)) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def reverse_sequence(start):
    for i in range(start, -1, -1):
        yield i 
```

</details>

#### Exercise 3: Words from Text

Problem Statement:​ Create a generator function that takes a string of text and yields each word individually. Words are separated by whitespace.

Function Signature: ```def words_from_text(text):```

Test Cases:

```python
text = "Launch School is a great place to learn"
assert list(words_from_text(text)) == ['Launch', 'School', 'is', 'a', 'great', 'place', 'to', 'learn']
assert list(words_from_text("  leading and trailing spaces  ")) == ['leading', 'and', 'trailing', 'spaces']
assert list(words_from_text("one")) == ['one']
assert list(words_from_text("")) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def words_from_text(text):

    for word in text.split():
        yield word 
```

</details>


#### Exercise 4: Dictionary Key-Value Pairs

Problem Statement:​ Create a generator function that yields the key-value pairs of a dictionary as tuples.

Function Signature: ```def dict_items(dictionary):```


Test Cases:
```python
d = {'a': 1, 'b': 2, 'c': 3}
assert list(dict_items(d)) == [('a', 1), ('b', 2), ('c', 3)]
assert list(dict_items({})) == []
d2 = {1: 'one', 2: 'two'}
assert list(dict_items(d2)) == [(1, 'one'), (2, 'two')]
```

<details> 
<summary>Possible Solution</summary> 

```python
def dict_items(dictionary):

    for key, value in dictionary.items():
        yield (key, value)
```

</details>

#### Exercise 5: Limited Range

Problem Statement:​ Create a generator function that works like range but yields numbers from start up to, but not including, stop, and stops early if a limit on the number of generated values is reached.

Function Signature: ```def limited_range(start, stop, limit):```

Test Cases:

```python
assert list(limited_range(0, 10, 5)) == [0, 1, 2, 3, 4]
assert list(limited_range(5, 10, 20)) == [5, 6, 7, 8, 9]
assert list(limited_range(0, 100, 0)) == []
assert list(limited_range(0, 3, 3)) == [0, 1, 2]
```

<details> 
<summary>Possible Solution</summary> 

```python

def limited_range(start, stop, limit):

    loop_count = 0
    count = start 
    while loop_count < limit:
        loop_count += 1
        if count < stop:
            yield count 
            count += 1
```

</details>


#### Exercise 6: Filter Long Words

Problem Statement:​ Create a generator function that takes an iterable of words and a minimum length, then yields only the words that are longer than the minimum length.

Function Signature: ```def filter_long_words(words, min_length):```


Test Cases:

```python
words = ['cat', 'dog', 'elephant', 'python', 'is', 'fun']
assert list(filter_long_words(words, 5)) == ['elephant', 'python']
assert list(filter_long_words(words, 3)) == ['elephant', 'python']
assert list(filter_long_words(words, 10)) == []
assert list(filter_long_words([], 5)) == []
```


<details> 
<summary>Possible Solution</summary> 

```python
def filter_long_words(words, min_length):

    for word in words:
        if len(word) > min_length:
            yield word
```

</details>

#### Exercise 7: Transform and Filter

Problem Statement:​ Create a generator function that processes a sequence of numbers. It should filter out numbers that are not greater than a given threshold and then apply a transform function to each of the remaining numbers before yielding them.

Function Signature: ```def transform_and_filter(numbers, threshold, transform):```


Test Cases:

```python
numbers = [1, 6, 2, 8, 3, 9, 4, 10, 5]
square = lambda x: x * x
assert list(transform_and_filter(numbers, 5, square)) == [36, 64, 81, 100]
add_ten = lambda x: x + 10
assert list(transform_and_filter(numbers, 8, add_ten)) == [19, 20]
assert list(transform_and_filter(numbers, 10, square)) == []
assert list(transform_and_filter([], 0, square)) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def transform_and_filter(numbers, threshold, transform):

    for number in numbers:
        if number > threshold:
            yield transform(number)
```

</details>

#### Exercise 8: enumerate Implementation

Problem Statement:​ Implement your own version of the built-in enumerate function as a generator. It should take an iterable and yield tuples of `(index, value)`.

Function Signature: ```def my_enumerate(iterable):``` 


Test Cases:
```python
assert list(my_enumerate(['a', 'b', 'c'])) == [(0, 'a'), (1, 'b'), (2, 'c')]
assert list(my_enumerate('Python')) == [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
assert list(my_enumerate([])) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def my_enumerate(iterable):

    for element in iterable:
        indexed = iterable.index(element)
        yield (indexed, element)
```

</details>

#### Exercise 9: Conditional Capitalization (Generator Expression)

Problem Statement:​ This time, use a generator ​expression​ to create a generator that capitalizes strings from a list but only if their length is greater than 4.

Function Signature: No function, assign a generator expression to the variable `capitalized_long_words`

Test Cases:

```python
words = ['launch', 'school', 'is', 'a', 'great', 'place']
#insert your expression here
assert list(capitalized_long_words) == ['Launch', 'School', 'Great']

words2 = ['short', 'words']
#insert your expression here
assert list(capitalized_long_words2) == ['Short', 'Words']
```

<details> 
<summary>Possible Solution</summary> 

```python
capitalized_long_words = (word.capitalize() for word in words if len(word) > 4)
capitalized_long_words2 = (word.capitalize() for word in words2 if len(word) > 4)
```
</details>

#### Exercise 10: Chained Generators

Problem Statement:​ Create two generators. The first, number_sequence, yields numbers from 0 to 9. The second, filter_multiples, takes an iterable and a divisor, and yields only the numbers from the iterable that are multiples of the divisor. Chain them together to get multiples of 3 from 0 to 9.

Function Signatures: 

```python

def number_sequence():

def filter_multiples(iterable, divisor):
```

Test Cases:

```python
assert list(number_sequence()) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num_gen = number_sequence()
multiples_of_3 = filter_multiples(num_gen, 3)
assert list(multiples_of_3) == [0, 3, 6, 9]

num_gen_2 = number_sequence()
multiples_of_4 = filter_multiples(num_gen_2, 4)
assert list(multiples_of_4) == [0, 4, 8]
```

<details> 
<summary>Possible Solution</summary> 

```python

def number_sequence():

    number = 0
    for i in range(10):
        yield number
        number += 1


def filter_multiples(iterable, divisor):
    for number in iterable:
        if number % divisor == 0:
            yield number
```

</details>

#### Exercise 11: Flatten a List of Lists with yield from

Problem Statement:​ Create a generator that takes a list of lists (a nested list) and yields each item from the sublists in order. Use the `yield from` syntax.

Function Signature: ```def flatten_list(nested_list):```

Test Cases:

```python
assert list(flatten_list([[1, 2], [3, 4], [5]])) == [1, 2, 3, 4, 5]
assert list(flatten_list([['a', 'b'], ['c']])) == ['a', 'b', 'c']
assert list(flatten_list([[], [1, 2], []])) == [1, 2]
assert list(flatten_list([])) == []
```

<details> 
<summary>Possible Solution</summary> 

```python

def flatten_list(nested_list):

    for single_list in nested_list:
        yield from single_list
```

</details>

#### Exercise 12: Running Total

Problem Statement:​ Create a stateful generator that takes an iterable of numbers and yields the cumulative sum at each step.

Function Signature: ```def running_total(iterable):```

Test Cases:

```python
assert list(running_total([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
assert list(running_total([10, -1, -2, 5])) == [10, 9, 7, 12]
assert list(running_total([])) == []
assert list(running_total([5])) == [5]
```


<details> 
<summary>Possible Solution</summary> 

```python
def running_total(iterable):

    summed = 0
    for item in iterable:
        summed += item
        yield summed
```
</details>

#### Exercise 13: Sliding Window

Problem Statement:​ Create a generator that yields a "sliding window" of a specified size over an iterable. Each yield should be a tuple containing the elements in the current window.

Function Signature: ```def sliding_window(iterable, size):```

Test Cases:

```python
numbers = [1, 2, 3, 4, 5, 6]
assert list(sliding_window(numbers, 3)) == [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
assert list(sliding_window('abcde', 2)) == [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
assert list(sliding_window([1, 2, 3], 5)) == []
assert list(sliding_window([1, 2, 3], 1)) == [(1,), (2,), (3,)]
assert list(sliding_window([], 3)) == []
```
<details> 
<summary>Possible Solution</summary> 

```python

def sliding_window(iterable, size):
        
    for i in range(len(iterable) - size + 1):
        yield tuple(iterable[i : i + size])
```

Note: Definitely revist this one, has exam smell on it.

</details>

#### Exercise 14: Sentence Tokenizer

Problem Statement:​ Given a large string of text, create a generator that yields one sentence at a time. For this exercise, a sentence is a sequence of characters that ends with a '.', '!', or '?'. The punctuation should be included in the yielded sentence.

Function Signature: ```def tokenize_sentences(text):```


Test Cases:

```python
text = "Hello world. This is a test! Are you ready? I am."
assert list(tokenize_sentences(text)) == ["Hello world.", "This is a test!", "Are you ready?", "I am."]
text2 = "Single sentence."
assert list(tokenize_sentences(text2)) == ["Single sentence."]
text3 = "No punctuation here"
assert list(tokenize_sentences(text3)) == ["No punctuation here"]
assert list(tokenize_sentences("")) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def tokenize_sentences(text):
    delimiters = {'.', '!', '?'}
    current_sentence = []

    for char in text:
        current_sentence.append(char)
        if char in delimiters:
            yield "".join(current_sentence).strip()
            current_sentence = []

    if current_sentence:
        remaining_text = "".join(current_sentence).strip()
        if remaining_text:
            yield remaining_text

```
Note: Definitely revist this one, has exam smell on it.

</details>


#### Note: Come back to the following after you've done Files

#### Exercise 15: Log File Parser

Problem Statement:​ You are processing a large log file. Create a generator that reads through a file-like object (e.g., a list of strings for this exercise) and yields a dictionary for each line that starts with "ERROR:". The dictionary should contain the keys 'level', 'timestamp', and 'message'.

Function Signature: ```def parse_error_logs(log_lines):```

Test Cases:

```python 

log_data = [
    "INFO: 2023-09-22T10:00:00Z - System startup",
    "ERROR: 2023-09-22T10:05:15Z - Database connection failed",
    "DEBUG: 2023-09-22T10:05:16Z - Retrying connection",
    "ERROR: 2023-09-22T10:06:00Z - Authentication service timeout",
    "INFO: 2023-09-22T10:07:00Z - System operational"
]
expected = [
    {'level': 'ERROR', 'timestamp': '2023-09-22T10:05:15Z', 'message': 'Database connection failed'},
    {'level': 'ERROR', 'timestamp': '2023-09-22T10:06:00Z', 'message': 'Authentication service timeout'}
]
assert list(parse_error_logs(log_data)) == expected
assert list(parse_error_logs(["INFO: A", "DEBUG: B"])) == []
assert list(parse_error_logs([])) == []
```

<details> 
<summary>Possible Solution</summary> 

```python

def parse_error_logs(log_lines):

    for line in log_lines:
        if line.startswith("ERROR:"):
            result_dict = {}
            time_and_message = line.split(": ")[1]
            tm_split = time_and_message.split(" - ")
            time = tm_split[0]
            message = tm_split[1]
            result_dict['level'] = 'ERROR'
            result_dict['timestamp'] = time
            result_dict['message'] = message
            yield result_dict
```
</details>


#### Exercise 16: Simple CSV Reader

Problem Statement:​ Create a generator to read CSV (Comma Separated Values) data. Given an iterable of strings (lines of a file), it should yield each row as a list of strings. This simplified version doesn't need to handle all edge cases but should handle basic quoted fields.

Function Signature: ```def read_csv(lines):```

Test Cases:

```python
csv_data = [
    "name,age,city",
    'Alice,30,"New York"',
    'Bob,25,Chicago',
    'Charlie,"40","San Francisco, CA"',
]
expected = [
    ['name', 'age', 'city'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Chicago'],
    ['Charlie', '40', 'San Francisco, CA']
]
assert list(read_csv(csv_data)) == expected
assert list(read_csv(['a,b', 'c,d'])) == [['a', 'b'], ['c', 'd']]
assert list(read_csv([])) == []
```


<details> 
<summary>Possible Solution</summary> 

```python

import csv 

reader = csv.reader(lines)
    for row in reader:
        yield row
```
</details>


#### Exercise 17: Data Processing Pipeline

Problem Statement:​ Create a data pipeline using a chain of generators to process temperature data.

1.  A generator `file_reader` that yields lines from a multiline string.
2.  A generator `filter_comments` that takes lines and yields only those that don't start with '#'.
3.  A generator `parse_data` that takes lines, splits them by a comma, and yields tuples of (`city`, `temperature_celsius`) where the temperature is cast to a float.
4.  Finally, create a main generator process_temperatures that takes the raw text data, chains the above generators, and converts Celsius to Fahrenheit (F = C * 9/5 + 32) before yielding the final result as a string: `f"{city}: {temp_f:.1f}F"`.

Function Signature: ```def process_temperatures(raw_data):```


Test Cases:

```python
temp_data = """# Temperature readings for 2023-09-22
New York,20.5
# London data is pending
London,15.0
Tokyo,25.3
Sydney,-5.5
"""
expected_output = [
    "New York: 68.9F",
    "London: 59.0F",
    "Tokyo: 77.5F",
    "Sydney: 22.1F"
]
assert list(process_temperatures(temp_data)) == expected_output
assert list(process_temperatures("# All comments\n# No data")) == []
assert list(process_temperatures("")) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def file_reader(raw_data):
    for line in raw_data.splitlines():
        yield line

def filter_comments(partially_processed_data):
    for element in partially_processed_data:
        if not element.startswith("#"):
            yield element

def parse_data(almost_processed_data):
    for element in almost_processed_data:
        city, temperature_celsius = element.split(",", 1)
        yield city, float(temperature_celsius)

def process_temperatures(raw_data):
    lines = file_reader(raw_data)
    clean_lines = filter_comments(lines)
    records = parse_data(clean_lines)

    for city, temp_celsius in records:
        temp_f = temp_celsius* 9 / 5 + 32
        yield f"{city}: {temp_f:.1f}F"
```

</details>

[Back to the top](#top)

### Generators, on your own practice 2

#### Exercise 1. Select by Value

Problem Statement:  Create a generator function that yields items from an iterable that are equal to a specified value.

Function Signature:  ```def select_by_value(iterable, value):```

Requirements:

* The function must be a generator.
* It must accept an iterable and a value to match.
* It must yield each item from the iterable that is equal to value.
* The order of yielded items must be the same as their order in the input iterable.
* It must handle iterables containing different data types.

Test Cases

```python
assert list(select_by_value([1, 2, 3, 2, 4, 2], 2)) == [2, 2, 2]
assert list(select_by_value(('apple', 'banana', 'apple'), 'apple')) == ['apple', 'apple']
assert list(select_by_value([1, 'a', 2.0, 'a'], 'a')) == ['a', 'a']
assert list(select_by_value([1, 2, 3], 4)) == []
assert list(select_by_value([], 1)) == []
assert list(select_by_value((i for i in [5, 6, 5]), 5)) == [5, 5]
```

Test Summary:  The tests verify selection for integers, strings, and mixed types. They cover cases with multiple matches, no matches, empty inputs, and generator expression inputs.

<details> 
<summary>Possible Solution</summary> 

```python
def select_by_value(iterable, value):

    for element in iterable:
        if element == value:
            yield element
```

</details>

#### Exercise 2. Transform to Uppercase

Problem Statement:  Create a generator function that yields the uppercase version of each string in an iterable.

Function Signature: ```def transform_to_uppercase(strings):```

Requirements:

* The function must be a generator.
* It must accept an iterable of strings.
* It must yield the uppercase version of each string.
* The order of yielded strings must correspond to the order of the original strings.
* It must handle empty iterables.

Test Cases

```python
assert list(transform_to_uppercase(['hello', 'world'])) == ['HELLO', 'WORLD']
assert list(transform_to_uppercase(('Launch', 'School'))) == ['LAUNCH', 'SCHOOL']
assert list(transform_to_uppercase(['', 'a', 'B'])) == ['', 'A', 'B']
assert list(transform_to_uppercase([])) == []
assert list(transform_to_uppercase((s for s in ['one', 'two']))) == ['ONE', 'TWO']
```

Test Summary: The tests verify the transformation for lists and tuples of strings, including empty strings and mixed-case strings. They also cover empty inputs and generator expression inputs.

<details> 
<summary>Possible Solution</summary> 

```python
def transform_to_uppercase(strings):
    for string in strings:
        yield string.upper()
```
</details>

#### Exercise 3. Filter Out Short Words

Problem Statement:  Create a generator function that filters out words from an iterable that are shorter than a given length.

Function Signature: ```def filter_out_short_words(words, min_length):```

Requirements:

* The function must be a generator.
* It must accept an iterable of strings and an integer min_length.
* It must yield only the strings whose length is greater than or equal to min_length.
* The order of yielded strings must be the same as their order in the input iterable.
* It must handle empty iterables and cases where no words meet the criteria.

Test Cases:

```python
words = ['cat', 'dog', 'elephant', 'mouse', 'lion']
assert list(filter_out_short_words(words, 5)) == ['elephant', 'mouse']
assert list(filter_out_short_words(words, 3)) == ['cat', 'dog', 'elephant', 'mouse', 'lion']
assert list(filter_out_short_words(words, 10)) == []
assert list(filter_out_short_words([], 4)) == []
assert list(filter_out_short_words(('a', 'b', 'cde'), 3)) == ['cde']
```

Test Summary: The tests cover various minimum lengths, including cases where some, all, or no words are selected. They test list, tuple, and empty inputs.

<details> 
<summary>Possible Solution</summary> 

```python

def filter_out_short_words(words, min_length):
    for word in words:
        if len(word) >= min_length:
            yield word
```

</details>

#### Exercise 4. Yield with Index

Problem Statement: Create a generator function that works like enumerate. It should yield tuples containing the index and the value for each item in an iterable.

Function Signature: ``` def yield_with_index(iterable):```

Requirements:

* The function must be a generator.
* It must accept any iterable.
* It must yield a 2-element tuple for each item: (index, value).
* The index should start at 0 and increment for each item.
* The order of yielded tuples must correspond to the item order in the input iterable.
* It must handle empty iterables.

Test Cases
```python
assert list(yield_with_index(['a', 'b', 'c'])) == [(0, 'a'), (1, 'b'), (2, 'c')]
assert list(yield_with_index(('x', 'y'))) == [(0, 'x'), (1, 'y')]
assert list(yield_with_index([])) == []
assert list(yield_with_index('hi')) == [(0, 'h'), (1, 'i')]
assert list(yield_with_index((i for i in [9, 8]))) == [(0, 9), (1, 8)]
```

Test Summary: The tests verify correct index-value pairing for lists, tuples, strings, and generator expressions. The test for an empty iterable is also included.

<details> 
<summary>Possible Solution</summary> 

```python
def yield_with_index(iterable):

    i = 0
    for item in iterable:
        yield (i, item)
        i += 1
```

</details>


#### Exercise 5. Repeat Each Item

Problem Statement: Create a generator function that yields each item from an iterable a specified number of times before moving to the next item.

Function Signature ```def repeat_each_item(iterable, num_repeats):```

Requirements:

* The function must be a generator.
* It must accept an iterable and a non-negative integer num_repeats.
* For each item in the iterable, it must yield that item num_repeats times consecutively.
* If `num_repeats` is 0, the generator should yield nothing.
* It must handle empty iterables.

Test Cases
```python
assert list(repeat_each_item([1, 2], 3)) == [1, 1, 1, 2, 2, 2]
assert list(repeat_each_item(('a', 'b'), 2)) == ['a', 'a', 'b', 'b']
assert list(repeat_each_item([1, 2, 3], 1)) == [1, 2, 3]
assert list(repeat_each_item([1, 2, 3], 0)) == []
assert list(repeat_each_item([], 5)) == []
assert list(repeat_each_item((i for i in ['x']), 4)) == ['x', 'x', 'x', 'x']
```

Test Summary: The tests cover repeating items multiple times, once, or zero times. They verify correct behavior for lists, tuples, empty iterables, and generator expressions.

<details> 
<summary>Possible Solution</summary> 

```python

def repeat_each_item(iterable, num_repeats):

    target = num_repeats 
    for item in iterable:
        while num_repeats > 0:
            yield item
            num_repeats -= 1
        num_repeats = target
```

</details>

#### Exercise 6. Yield Every Nth Item

Problem Statement: Create a generator function that yields every Nth item from an iterable, starting with the first item.

Function Signature:  ```def yield_every_nth(iterable, n):```

Requirements:

* The function must be a generator.
* It must accept an iterable and a positive integer n.
* It must yield the 1st item, the (1+n)th item, the (1+2n)th item, and so on.
* The first item (at index 0) should always be yielded if the iterable is not empty.
* It must handle empty iterables.
* Assume n will be 1 or greater.

Test Cases

```python
assert list(yield_every_nth([1, 2, 3, 4, 5, 6, 7, 8], 3)) == [1, 4, 7]
assert list(yield_every_nth('abcdefgh', 2)) == ['a', 'c', 'e', 'g']
assert list(yield_every_nth(range(10), 1)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert list(yield_every_nth([10, 20, 30], 5)) == [10]
assert list(yield_every_nth([], 3)) == []
assert list(yield_every_nth((i for i in 'python'), 4)) == ['p', 'o']
```

Test Summary:  The tests verify correct selection with different step values (n), including a step of 1. They cover lists, strings, ranges, empty iterables, and generator inputs.

<details> 
<summary>Possible Solution</summary> 

```python
def yield_every_nth(iterable, n):

    i = 0
    for item in iterable:
        if i % n == 0:
            yield item
        i += 1
```

</details>

#### Exercise 7. Yield Until Value

Problem Statement: Create a generator function that yields items from an iterable until a specific value is encountered. The stop value itself should not be yielded.

Function Signature: ```def yield_until_value(iterable, stop_value):```


Requirements:

* The function must be a generator.
* It must accept an iterable and a stop_value.
* It must yield items from the beginning of the iterable.
* It must stop yielding as soon as it encounters an item equal to stop_value.
* The stop_value item must not be included in the output.
* If the stop_value is not found, it should yield all items from the iterable.

Test Cases
```python
assert list(yield_until_value([1, 2, 3, 'stop', 4, 5], 'stop')) == [1, 2, 3]
assert list(yield_until_value(('a', 'b', 'c'), 'd')) == ['a', 'b', 'c']
assert list(yield_until_value([99, 10, 25, 99, 40], 99)) == []
assert list(yield_until_value([], 'stop')) == []
assert list(yield_until_value((i for i in [1, 2, 3]), 3)) == [1, 2]

```

Test Summary:  The tests verify that generation stops correctly, handles cases where the stop value is first or not present, and works with empty and generator inputs.

<details> 
<summary>Possible Solution</summary> 

```python

def yield_until_value(iterable, stop_value):
    i = 0
    for item in iterable:
        if item != stop_value:
            yield item
            i += 1
        else:
            break
```

</details>

#### Exercise 8. Flatten One Level

Problem Statement: Create a generator function that takes an iterable of iterables (e.g., a list of lists) and yields each item from the inner iterables, one by one.

Function Signature: ```def flatten_one_level(nested_iterable):```

Requirements:

* The function must be a generator.
* It must accept an iterable where each element is itself an iterable.
* It must yield each element from each inner iterable in sequence.
* The order of yielded elements should correspond to iterating through the outer iterable, and then through each inner iterable.
* It should handle empty outer and inner iterables.

Test Cases
```python
assert list(flatten_one_level([[1, 2], [3, 4, 5], [6]])) == [1, 2, 3, 4, 5, 6]
assert list(flatten_one_level([('a', 'b'), ('c',)])) == ['a', 'b', 'c']
assert list(flatten_one_level([[], [1, 2], []])) == [1, 2]
assert list(flatten_one_level([])) == []
assert list(flatten_one_level([[], []])) == []
assert list(flatten_one_level(['hi', 'world'])) == ['h', 'i', 'w', 'o', 'r', 'l', 'd']
assert list(flatten_one_level((i for i in [[1], [2]]))) == [1, 2]
```

Test Summary: The tests cover nested lists, tuples, and strings, including cases with empty inner and outer iterables. A test with a generator expression input is also included.

<details> 
<summary>Possible Solution</summary> 

```python
def flatten_one_level(nested_iterable):

    for iterable in nested_iterable:
        for element in iterable:
            yield element
```

</details>

#### Exercise 9. Filter Dictionary Items

Problem Statement: Create a generator function that yields (key, value) tuples from a dictionary for which a given predicate function returns a truthy value The predicate function will receive the value as its only argument.

Function Signature: `def filter_dict_items(dictionary, predicate):`

Requirements:

* The function must be a generator.
* It must accept a dictionary and a single-argument function predicate.
* It must iterate over the dictionary's items.
* For each (key, value) pair, it must call predicate(value).
* If the predicate returns a truthy value, the generator must yield the (key, value) tuple.
* The order of yielded items is not guaranteed (it depends on the dictionary's iteration order).

Test Cases

```python
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
is_even = lambda x: x % 2 == 0
result = set(filter_dict_items(data, is_even))
assert result == {('b', 2), ('d', 4)}

is_string = lambda x: isinstance(x, str)
data_mixed = {'id': 123, 'name': 'Alice', 'city': 'New York'}
result_mixed = set(filter_dict_items(data_mixed, is_string))
assert result_mixed == {('name', 'Alice'), ('city', 'New York')}

assert list(filter_dict_items(data, lambda x: x > 10)) == []
assert list(filter_dict_items({}, is_even)) == []
```

Test Summary: The tests verify filtering based on numeric and type-based predicates. They cover cases with some matches, no matches, and an empty dictionary input. Results are converted to a set to handle dictionary order ambiguity.

<details> 
<summary>Possible Solution</summary> 

```python

def filter_dict_items(dictionary, predicate):
    for key, value in dictionary.items():
        if predicate(value):
            yield key, value
```

</details>

#### Exercise 10. Yield Unique Items

Problem Statement: Create a generator function that yields only the unique items from an iterable, preserving the order of their first appearance.

Function Signature: `def yield_unique_items(iterable):`

Requirements:

* The function must be a generator.
* It must accept an iterable.
* It must yield each unique item from the iterable exactly once.
* The order of yielded items must be the same as the order of their first appearance in the input iterable.
* It must handle different data types, including unhashable types if possible (though tests will only use hashable types).
* It must handle empty iterables.

Test Cases

```python
assert list(yield_unique_items([1, 2, 2, 3, 1, 4, 3])) == [1, 2, 3, 4]
assert list(yield_unique_items(('a', 'b', 'a', 'c', 'b', 'b'))) == ['a', 'b', 'c']
assert list(yield_unique_items('abracadabra')) == ['a', 'b', 'r', 'c', 'd']
assert list(yield_unique_items([1, 2, 3])) == [1, 2, 3]
assert list(yield_unique_items([])) == []
assert list(yield_unique_items((i for i in [5, 5, 5]))) == [5]
```

Test Summary
The tests verify that duplicates are removed while preserving the order of first appearance for lists, tuples, strings, and generator inputs.

<details> 
<summary>Possible Solution</summary> 

```python

def yield_unique_items(iterable):

   current_set = set()
   for item in iterable:
      if item not in current_set:
        current_set.add(item)
        yield item
```

</details>

#### Exercise 11. Create a Bounded Range Generator

Problem Statement:  Using a generator expression, create a generator that yields numbers in a sequence with a specified start, stop (exclusive), and step, similar to the built-in range.

Function Signature: ```def bounded_range_generator(start, stop, step):```

Requirements:

* The function must return a generator.
* The implementation must use a generator expression.
* It must yield numbers starting from start.
* It must stop yielding before it reaches or exceeds stop.
* Each subsequent number must be the previous number plus step.
* It should handle positive and negative steps.

Test Cases

```python
# Note: The problem asks for the function to return a generator object.
# We then convert it to a list for testing.
gen1 = bounded_range_generator(1, 10, 2)
assert list(gen1) == [1, 3, 5, 7, 9]

gen2 = bounded_range_generator(10, 0, -2)
assert list(gen2) == [10, 8, 6, 4, 2]

gen3 = bounded_range_generator(5, 5, 1)
assert list(gen3) == []

gen4 = bounded_range_generator(0, 5, 1)
assert list(gen4) == [0, 1, 2, 3, 4]
```

Test Summary: The tests verify the generator expression's output for positive steps, negative steps, and empty ranges, ensuring it behaves like range.

<details> 
<summary>Possible Solution</summary> 

```python

def bounded_range_generator(start, stop, step):
    for item in range(start, stop, step):
        yield item
```

</details>

#### Exercise 12. Chain Iterables

Problem Statement: Create a generator function that accepts multiple iterables as arguments and yields all items from the first iterable, then all items from the second, and so on.

Function Signature: ```def chain_iterables(*iterables):```

Requirements:

* The function must be a generator.
* It must accept a variable number of iterable arguments.
* It must yield all elements from the first iterable, followed by all elements from the second, and so on, in order.
* It should handle cases with no arguments or with empty iterables among the arguments.
* Consider using `yield from` for a concise implementation.

Test Cases
```python
assert list(chain_iterables([1, 2], ('a', 'b'))) == [1, 2, 'a', 'b']
assert list(chain_iterables(range(3), "xyz")) == [0, 1, 2, 'x', 'y', 'z']
assert list(chain_iterables([1], [], [2, 3])) == [1, 2, 3]
assert list(chain_iterables()) == []
assert list(chain_iterables(('single',))) == ['single']
assert list(chain_iterables((i for i in [1,2]), (i for i in [3,4]))) == [1, 2, 3, 4]
```

Test Summary: The tests verify chaining of different iterable types (list, tuple, range, string). They cover cases with empty iterables, a single iterable, no iterables, and generator inputs.

<details> 
<summary>Possible Solution</summary> 

```python

def chain_iterables(*iterables):

    for iterable in iterables:
        yield from iterable
```

</details>

#### Exercise 13. Interleave Iterables

Problem Statement: Create a generator that accepts two iterables and yields one item from the first, then one from the second, then the next from the first, and so on. If one iterable is exhausted, it should continue yielding items from the other.

Function Signature: ```def interleave_iterables(iter1, iter2):```

Requirements:

* The function must be a generator.
* It must accept two iterables.
* It must yield items by alternating between `iter1` and `iter2`.
* When one iterable is exhausted, the generator must yield all remaining items from the other iterable.
* It must handle empty iterables.

Test Cases
```python
assert list(interleave_iterables([1, 2, 3], ['a', 'b', 'c'])) == [1, 'a', 2, 'b', 3, 'c']
assert list(interleave_iterables([1, 2], ['a', 'b', 'c', 'd'])) == [1, 'a', 2, 'b', 'c', 'd']
assert list(interleave_iterables(range(4), ('x', 'y'))) == [0, 'x', 1, 'y', 2, 3]
assert list(interleave_iterables([], [1, 2, 3])) == [1, 2, 3]
assert list(interleave_iterables(['a', 'b'], [])) == ['a', 'b']
assert list(interleave_iterables([], [])) == []
```

Test Summary: The tests verify interleaving for iterables of equal length and different lengths. They also cover cases where one or both inputs are empty.

<details> 
<summary>Possible Solution</summary> 

```python
def interleave_iterables(iter1, iter2):

    iterator1 = iter(iter1)
    iterator2 = iter(iter2)

    iter1_exhausted = False
    iter2_exhausted = False

    while not (iter1_exhausted and iter2_exhausted):
        if not iter1_exhausted:
            try:
                yield next(iterator1)
            except StopIteration:
                iter1_exhausted = True

        if not iter2_exhausted:
            try:
                yield next(iterator2)
            except StopIteration:
                iter2_exhausted = True
```

</details>

#### Exercise 14. Transform and Filter with a Generator Expression

Problem Statement: Write a function that returns a generator expression. The generator should process an iterable of numbers, selecting only the even ones and yielding their squares.

Function Signature: ```def square_of_evens(numbers):```


Requirements:

* The function must return a generator object, created from a generator expression.
* The returned generator must iterate over the input numbers.
* It must only consider even numbers.
* It must yield the square of each even number.
* It must handle empty iterables.

Test Cases

```python
# The function returns a generator, which we then listify for assertion.
gen1 = square_of_evens([1, 2, 3, 4, 5, 6])
assert list(gen1) == [4, 16, 36]

gen2 = square_of_evens(range(10))
assert list(gen2) == [0, 4, 16, 36, 64]

gen3 = square_of_evens([1, 3, 5, 7])
assert list(gen3) == []

gen4 = square_of_evens([])
assert list(gen4) == []

```

Test Summary: The tests confirm that the returned generator correctly filters for even numbers and squares them. Cases with no even numbers and empty inputs are included.

<details> 
<summary>Possible Solution</summary> 

```python

def square_of_evens(numbers):
    return (x**2 for x in numbers if x % 2 == 0)
```

</details>

#### Exercise 16. Bounded Repetition

Problem Statement: Create a generator that yields items from an iterable, but stops after a certain total number of items have been yielded, or when the iterable is exhausted, whichever comes first.

Function Signature: ```def bounded_repetition(iterable, max_yields):```


Requirements:

* The function must be a generator.
* It must accept an iterable and a non-negative integer `max_yields`.
* It must yield items from the iterable in their original order.
* It must stop yielding after `max_yields` items have been produced.
* If the iterable has fewer than `max_yields` items, it yields all of them.
* If `max_yields` is 0, it should yield nothing.

Test Cases
```python
assert list(bounded_repetition([1, 2, 3, 4, 5, 6], 4)) == [1, 2, 3, 4]
assert list(bounded_repetition('hello world', 20)) == ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
assert list(bounded_repetition(range(100), 5)) == [0, 1, 2, 3, 4]
assert list(bounded_repetition([1, 2, 3], 3)) == [1, 2, 3]
assert list(bounded_repetition([1, 2, 3], 0)) == []
assert list(bounded_repetition([], 10)) == []
```

Test Summary: The tests cover cases where the yield limit is reached, the iterable is exhausted first, the limit equals the iterable length, the limit is zero, and the input is empty.

<details> 
<summary>Possible Solution</summary> 

```python

def bounded_repetition(iterable, max_yields):

    i = 0
    for item in iterable:
        if i < max_yields:
            yield item
        i += 1

```
</details>

#### Exercise 17. Skip Header and Footer

Problem Statement: Create a generator that yields items from an iterable, but skips a specified number of items at the beginning (header) and at the end (footer).

Function Signature: ```def skip_header_footer(iterable, header_size, footer_size):```

Requirements:

* The function must be a generator.
* It must accept an iterable, a non-negative header_size, and a non-negative footer_size.
* It must not yield the first header_size items.
* It must not yield the last footer_size items.
* It should correctly handle cases where header_size + footer_size is greater than or equal to the total number of items.

Test Cases
```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert list(skip_header_footer(data, 2, 3)) == [3, 4, 5, 6, 7]
assert list(skip_header_footer('abcdefg', 1, 2)) == ['b', 'c', 'd', 'e']
assert list(skip_header_footer(range(5), 0, 0)) == [0, 1, 2, 3, 4]
assert list(skip_header_footer([1, 2, 3, 4], 2, 2)) == []
assert list(skip_header_footer([1, 2, 3], 5, 2)) == []
assert list(skip_header_footer([], 2, 2)) == []
```

Test Summary: The tests verify correct skipping from both ends, no skipping (zero sizes), and cases where the number of items to skip exceeds the iterable's length.

<details> 
<summary>Possible Solution</summary> 

```python

def skip_header_footer(iterable, header_size, footer_size):

    i = 0
    for item in iterable:
        if i >= header_size and i <= (len(iterable) - footer_size - 1):
            yield item   
        i += 1
```

</details>

#### Exercise 18. Yield Runs of Consecutive Duplicates

Problem Statement: Create a generator that processes a sorted iterable and yields lists of consecutive identical items.

Function Signature: ```def yield_runs(sorted_iterable):```

Requirements:

* The function must be a generator.
* It must accept an iterable that is assumed to be sorted.
* It must yield a list for each run of consecutive identical items.
* Each yielded list should contain all identical items in that run.
* It must handle empty iterables.

Test Cases
```python
assert list(yield_runs([1, 1, 2, 3, 3, 3, 4, 4])) == [[1, 1], [2], [3, 3, 3], [4, 4]]
assert list(yield_runs(['a', 'a', 'a', 'b', 'c', 'c'])) == [['a', 'a', 'a'], ['b'], ['c', 'c']]
assert list(yield_runs([1, 2, 3, 4, 5])) == [[1], [2], [3], [4], [5]]
assert list(yield_runs([5, 5, 5, 5])) == [[5, 5, 5, 5]]
assert list(yield_runs([])) == []
assert list(yield_runs((i for i in 'abbccc'))) == [['a'], ['b', 'b'], ['c', 'c', 'c']]
```

Test Summary: The tests cover various runs of different lengths, including single-item runs and a single run consuming the whole iterable. Empty and generator inputs are also tested.

<details> 
<summary>Possible Solution</summary> 

```python

def yield_runs(sorted_iterable):

    current_run = []
    current_value = None

    for item in sorted_iterable:
        if not current_run:
            current_value = item
            current_run.append(item)
        elif item == current_value:
            current_run.append(item)
        else:
            yield current_run
            current_value = item
            current_run = [item]

    if current_run:
       yield current_run
```
</details>

#### Exercise 19. Partition by Predicate

Problem Statement: Create a generator that yields items from an iterable in two groups based on a predicate. First, it should yield all items for which the predicate is truthy, and then it should yield all items for which the predicate is falsy.

Function Signature: ```def partition_by_predicate(iterable, predicate):```

Requirements:

* The function must be a generator.
* It must accept an iterable and a single-argument function predicate.
* It must iterate through the entire iterable once, caching the results.
* It must first yield from all items for which predicate(item) is truthy, in their original relative order.
* After that, it must yield from all items for which predicate(item) is falsy, in their original relative order.
* It must handle empty iterables.

Test Cases
```python
is_even = lambda n: n % 2 == 0
data = [1, 2, 3, 4, 5, 6, 7, 8]
assert list(partition_by_predicate(data, is_even)) == [2, 4, 6, 8, 1, 3, 5, 7]

is_long = lambda s: len(s) > 3
words = ('cat', 'elephant', 'dog', 'mouse')
assert list(partition_by_predicate(words, is_long)) == ['elephant', 'mouse', 'cat', 'dog']

assert list(partition_by_predicate(range(5), lambda x: True)) == [0, 1, 2, 3, 4]
assert list(partition_by_predicate(range(5), lambda x: False)) == [0, 1, 2, 3, 4]
assert list(partition_by_predicate([], is_even)) == []

```


Test Summary: The tests verify correct partitioning for numbers and strings. They also cover edge cases where the predicate is always true or always false, and when the input is empty.


<details> 
<summary>Possible Solution</summary> 

```python
def partition_by_predicate(iterable, predicate):

    truthy = []
    falsy = []

    for item in iterable:
        if predicate(item):
            truthy.append(item)
        else:
            falsy.append(item)

    for element in truthy:
        yield element
    for element in falsy:
        yield element
```
</details>

#### Exercise 20. Group By Key

Problem Statement: Create a generator that groups items from an iterable of dictionaries by a common key.For each unique value of the specified key, the generator should yield a tuple containing that value and another generator that yields all dictionaries having that value.

Function Signature: ```def group_by_key(iterable, key):```

Requirements:

* The function must be a generator.
* It must accept an iterable of dictionaries and a key.
* It must identify unique values for the given key in the order they first appear.
* For each unique key-value, it must yield a 2-element tuple: (`key_value,` `items_generator)`.
    * `key_value` is the value associated with the specified key.
    * `items_generator` is a generator that yields all dictionaries from the original iterable (in their original order) that have `key_value` for the given key.
* It must handle cases where dictionaries are missing the specified key (they should be ignored).
* The outer generator should not consume the input iterable more than once.

Test Cases
```python
data = [
    {'name': 'Alice', 'city': 'New York'},
    {'name': 'Bob', 'city': 'Los Angeles'},
    {'name': 'Charlie', 'city': 'New York'},
    {'name': 'David', 'city': 'Chicago'},
    {'name': 'Eve', 'city': 'Los Angeles'},
    {'name': 'Frank'},
]
grouped = group_by_key(data, 'city')
result = {city: list(items) for city, items in grouped}

assert 'New York' in result
assert result['New York'] == [
    {'name': 'Alice', 'city': 'New York'},
    {'name': 'Charlie', 'city': 'New York'}
]
assert 'Los Angeles' in result
assert result['Los Angeles'] == [
    {'name': 'Bob', 'city': 'Los Angeles'},
    {'name': 'Eve', 'city': 'Los Angeles'}
]
assert len(result) == 3

grouped_order = group_by_key(data, 'city')
assert next(grouped_order)[0] == 'New York'
assert next(grouped_order)[0] == 'Los Angeles'

assert list(group_by_key([], 'city')) == []

data_gen = (d for d in data)
grouped_gen = group_by_key(data_gen, 'city')
result_gen = {city: list(items) for city, items in grouped_gen}
assert result == result_gen
```

Test Summary: The tests verify correct grouping, handling of missing keys, preservation of original item order within groups, and preservation of group order. They also confirm it works with empty and generator inputs.

<details> 
<summary>Possible Solution</summary> 

```python

def group_by_key(iterable, key):

    groups = {}
    group_order = []

    for item in iterable:
        if key not in item:
            continue

        key_value = item[key]

        if key_value not in groups:
            groups[key_value] = []
            group_order.append(key_value)

        groups[key_value].append(item)

    for key_value in group_order:
        items_generator = (item for item in groups[key_value])
        yield key_value, items_generator
```
</details>

[Back to the top](#top)

### Generators, team practice

#### Exercise 1​, Generate Squares

Problem Statement​: Create a generator function that yields the square of each number from an input iterable.

Function Signature​: ```def generate_squares(numbers):```

Complete Requirements​:

* The function must accept an iterable of numbers as an argument.
* The function must yield the square of each number in the order they appear in the input.
* The function must produce no values if the input iterable is empty.

Ready-to-run Test Code​:

```python
# Test case 1: Basic functionality
assert list(generate_squares([1, 2, 3, 4, 5])) == [1, 4, 9, 16, 25]

# Test case 2: Input with zero and negative numbers
assert list(generate_squares([0, -2, 10])) == [0, 4, 100]

# Test case 3: Empty input
assert list(generate_squares([])) == []

# Test case 4: Input is a tuple
assert list(generate_squares((10, 20))) == [100, 400]

print("Exercise 1 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python

def generate_squares(numbers):
    for number in numbers:
        yield number ** 2
```

</details>

#### Exercise 2​, Filter Short Words

Problem Statement​: Create a generator function that yields only the words from an input iterable that are shorter than a given maximum length.

Function Signature​: ```def filter_short_words(words, max_length):```

Complete Requirements​:

* The function must accept an iterable of strings and an integer `max_length`.
* The function must yield only the words whose length is strictly less than `max_length`.
* The function must preserve the original relative order of the yielded words.
* The function must produce no values if no words meet the criteria.

Ready-to-run Test Code​:

```python
words_list = ["apple", "banana", "pie", "kiwi", "fig"]

# Test case 1: Words shorter than 5
assert list(filter_short_words(words_list, 5)) == ["pie", "kiwi", "fig"]

# Test case 2: Words shorter than 4 (boundary)
assert list(filter_short_words(words_list, 4)) == ["pie", "fig"]

# Test case 3: No words meet the criteria
assert list(filter_short_words(words_list, 3)) == []

# Test case 4: Empty input list
assert list(filter_short_words([], 5)) == []

print("Exercise 2 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def filter_short_words(words, max_length):
    for word in words:
        if len(word) < max_length:
            yield word
```

</details>

#### Exercise 3, Generate Indexed Values

Problem Statement​: Create a generator function that behaves like enumerate, yielding a tuple of (index, value) for each item in an input iterable.

Function Signature​: ```def generate_indexed(items):```

Complete Requirements​:

* The function must accept an iterable as an argument.
* The function must yield a tuple (index, value) for each item.
* The index must start at 0 and increment for each item.
* The function must produce no values if the input iterable is empty.

Ready-to-run Test Code​:

```python
# Test case 1: List of strings
assert list(generate_indexed(['a', 'b', 'c'])) == [(0, 'a'), (1, 'b'), (2, 'c')]

# Test case 2: A single-element tuple

assert list(generate_indexed(('hello',))) == [(0, 'hello')]

# Test case 3: An empty list
assert list(generate_indexed([])) == []

# Test case 4: A string iterable
assert list(generate_indexed('hi')) == [(0, 'h'), (1, 'i')]

print("Exercise 3 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def generate_indexed(items):

    i = 0
    for item in items:
        yield (i, item)
        i += 1
```
</details>

#### ​Exercise 4, Flatten a List

Problem Statement​: Create a generator function that takes a list of lists (or other iterables) and yields each item from the nested lists in sequence, effectively "flattening" the structure.

Function Signature​: ```def flatten_list(nested_list):```

Complete Requirements​:

* The function must accept a list where each element is an iterable.
* The function must iterate through each nested iterable and yield its items one by one.
* The function must maintain the order of items as they appear.
* The function must correctly handle empty nested lists and a top-level empty list.

Ready-to-run Test Code​:

```python
# Test case 1: Basic functionality with lists
assert list(flatten_list([[1, 2], [3, 4, 5], [6]])) == [1, 2, 3, 4, 5, 6]

# Test case 2: With empty sublists
assert list(flatten_list([[], [10, 20], [], [30]])) == [10, 20, 30]

# Test case 3: Top-level list is empty
assert list(flatten_list([])) == []

# Test case 4: Mixed iterable types (list of tuples)
assert list(flatten_list([(1, 2), (3, 4)])) == [1, 2, 3, 4]

print("Exercise 4 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def flatten_list(nested_list):

    for sublist in nested_list:
        for element in sublist:
            yield element
```

</details>

#### Exercise 5​, Generate Number Countdown

Problem Statement​: Create a generator function that yields numbers in a countdown sequence, from a given starting number down to and including 0.

Function Signature​: ```def generate_countdown(start):```

Complete Requirements​:

* The function must accept a non-negative integer start.
* The function must first yield the start number, then start - 1, and so on, down to 0.
* If start is 0, the function should yield only 0.

Ready-to-run Test Code​:

```python
# Test case 1: Countdown from 5
assert list(generate_countdown(5)) == [5, 4, 3, 2, 1, 0]

# Test case 2: Countdown from 1
assert list(generate_countdown(1)) == [1, 0]

# Test case 3: Countdown from 0 (boundary)
assert list(generate_countdown(0)) == [0]

print("Exercise 5 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def generate_countdown(start):

    i = 0
    for _ in range(start+1):
        result = start - i
        yield result
        i += 1
```

</details>

#### Exercise 6​, Generate Dictionary Key-Value Pairs

Problem Statement​: Create a generator function that takes a dictionary and yields each key-value pair as a formatted string.

Function Signature​: ```def format_dict_items(data_dict):```

Complete Requirements​:

* The function must accept a dictionary as an argument.
* The function must yield a string for each item in the format `"Key: <key>, Value: <value>"`.
* The order of the yielded strings is not important.
* The function must produce no values if the input dictionary is empty.

Ready-to-run Test Code​:

```python
# Test case 1: Basic dictionary
inventory = {'apples': 5, 'oranges': 10}

expected = {"Key: apples, Value: 5", "Key: oranges, Value: 10"}
assert set(format_dict_items(inventory)) == expected

# Test case 2: Dictionary with different value types
mixed_data = {'name': 'Alice', 'age': 30, 'active': True}
expected = {"Key: name, Value: Alice", "Key: age, Value: 30", "Key: active, Value: True"}
assert set(format_dict_items(mixed_data)) == expected

# Test case 3: Empty dictionary
assert set(format_dict_items({})) == set()

print("Exercise 6 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def format_dict_items(data_dict):

    for key, value in data_dict.items():
        result = f"Key: {key}, Value: {value}"
        yield result
```

</details>

#### Exercise 7, Chain Two Iterables

Problem Statement​: Create a generator function that yields all items from a first iterable, followed by all items from a second iterable.
You must use `yield from`.

Function Signature​: ```def chain_iterables(iter1, iter2):```

Complete Requirements​:

* The function must accept two iterables as arguments.
* The function must first yield all items from `iter1` in their original order.
* After `iter1` is exhausted, the function must yield all items from iter2 in their original order.
* The implementation must use the yield from expression for both iterables.

Ready-to-run Test Code​:

```python
# Test case 1: Two lists
assert list(chain_iterables([1, 2], [3, 4])) == [1, 2, 3, 4]

# Test case 2: First iterable is empty
assert list(chain_iterables([], ('a', 'b'))) == ['a', 'b']

# Test case 3: Second iterable is empty
assert list(chain_iterables((10, 20), [])) == [10, 20]

# Test case 4: Both iterables are empty
assert list(chain_iterables((), [])) == []

# Test case 5: Different iterable types
assert list(chain_iterables('hi', [1, 2])) == ['h', 'i', 1, 2]

print("Exercise 7 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def chain_iterables(iter1, iter2):

    iterable = [iter1, iter2]
    for item in iterable:
        yield from item
```
</details>

#### Exercise 8, Generate Consecutive Pairs

Problem Statement​: Create a generator function that takes a sequence and yields tuples of each element paired with the element that immediately follows it.

Function Signature​: ```def generate_consecutive_pairs(sequence):```

Complete Requirements​:

* The function must accept an iterable as an argument.
* The function must yield a tuple (item, next_item) for each consecutive pair of items.
* The generator should produce no output if the input iterable has fewer than two items.

Ready-to-run Test Code​:

```python
# Test case 1: List of numbers
assert list(generate_consecutive_pairs([1, 2, 3, 4])) == [(1, 2), (2, 3), (3, 4)]

# Test case 2: A string
assert list(generate_consecutive_pairs('abc')) == [('a', 'b'), ('b', 'c')]

# Test case 3: A sequence with two elements
assert list(generate_consecutive_pairs([10, 20])) == [(10, 20)]

# Test case 4: A sequence with one element
assert list(generate_consecutive_pairs([100])) == []

# Test case 5: An empty sequence
assert list(generate_consecutive_pairs([])) == []

print("Exercise 8 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def generate_consecutive_pairs(sequence):

    for i in range(len(sequence)-1):
        yield sequence[i], sequence[i+1]
```

</details>

#### Exercise 9​, Generate Running Total

Problem Statement​: Create a generator function that takes an iterable of numbers and yields a running total.

Function Signature​: ```def generate_running_total(numbers):```

Complete Requirements​:

* The function must accept an iterable of numbers.
* The function must maintain an internal state for the current total, initialized to 0.
* For each number in the input, the function must add it to the total and yield the new total.
* The function must produce no values if the input iterable is empty.

Ready-to-run Test Code​:
```python
# Test case 1: Positive integers
assert list(generate_running_total([1, 2, 3, 4])) == [1, 3, 6, 10]

# Test case 2: Mix of positive and negative numbers
assert list(generate_running_total([10, -2, 5, -8])) == [10, 8, 13, 5]

# Test case 3: A single number
assert list(generate_running_total([100])) == [100]

# Test case 4: Empty input
assert list(generate_running_total([])) == []

print("Exercise 9 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def generate_running_total(numbers):

    running_total = 0
    for number in numbers:
        running_total += number
        yield running_total
```

</details>

#### Exercise 10​, Generate Tagged Items from Nested Data

Problem Statement​: You are given a dictionary where keys are tags (strings) and values are lists of items. Create a generator function that yields a tuple (tag, item) for every single item in all the lists.

Function Signature​: ```def generate_tagged_items(data):```

Complete Requirements​:

* The function must accept a dictionary where values are lists.
* The function must iterate through the dictionary's key-value pairs.
* For each key (tag) and its corresponding list of items, the function must iterate through the items.
* The function must yield a tuple (tag, item) for each item.
* The exact order of yielded tuples is not important, but items with the same tag should appear in their original relative order.

Ready-to-run Test Code​:
```python
data = {
    'fruit': ['apple', 'banana'],
    'vegetable': ['carrot'],
    'dairy': ['milk', 'cheese']
}

# Test case 1: Basic functionality
expected_items = {
    ('fruit', 'apple'), ('fruit', 'banana'),
    ('vegetable', 'carrot'),
    ('dairy', 'milk'), ('dairy', 'cheese')
}
assert set(generate_tagged_items(data)) == expected_items

# Test case 2: Dictionary with an empty list
data_with_empty = {'colors': ['red', 'blue'], 'shapes': []}
expected_items = {('colors', 'red'), ('colors', 'blue')}
assert set(generate_tagged_items(data_with_empty)) == expected_items

# Test case 3: Empty dictionary
assert set(generate_tagged_items({})) == set()

print("Exercise 10 tests passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python
def generate_tagged_items(data):

    for key, values in data.items():
        for value in values:
            yield (key, value)
```
</details>


[Back to the top](#top)

### Generators and Files

#### 1. Title Case Lines

Problem Statement: Create a generator function that takes an iterable of strings (lines) and yields each line converted to title case.

Function Signature: ```def title_case_lines(lines):```

Contract

* The function must return a generator object.
* The function must yield each line from the input iterable, converted to title case using the str.title() method.

Asserts
```python
lines_data = ["hello world", "python is fun", "THE end"]
expected = ["Hello World", "Python Is Fun", "The End"]
gen = title_case_lines(lines_data)
assert list(gen) == expected

lines_data_2 = []
expected_2 = []
gen_2 = title_case_lines(lines_data_2)
assert list(gen_2) == expected_2
```

<details> 
<summary>Possible Solution</summary> 

```python

def title_case_lines(lines):

    for line in lines:
        yield line.title()
```

</details>

#### 2. Filter Lines by Keyword

Problem Statement: Create a generator function that yields only the lines from an iterable that contain a specific keyword.

Function Signature: ```def filter_lines_by_keyword(lines, keyword):```

Contract

* The function must return a generator object.
* The function must yield only the lines from the input iterable that contain the keyword as a substring.
* The matching should be case-sensitive.

Asserts

```python
lines = [
    "An apple a day keeps the doctor away.",
    "Banana is a fruit.",
    "I love pineapple.",
    "This line has nothing to do with apples."
]
gen = filter_lines_by_keyword(lines, "apple")
assert next(gen) == "An apple a day keeps the doctor away."
assert next(gen) == "I love pineapple."

lines_data_2 = ["test", "testing", "tested"]
expected_2 = ["testing", "tested"]
assert list(filter_lines_by_keyword(lines_data_2, "test")) == ["test", "testing", "tested"]
assert list(filter_lines_by_keyword(lines_data_2, "tested")) == ["tested"]
assert list(filter_lines_by_keyword(lines_data_2, "toast")) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def filter_lines_by_keyword(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line
```
</details>

#### 3. Numbered Non-Blank Lines

Problem Statement: Create a generator function that yields non-blank lines from an iterable, prefixed with a 1-indexed line number.

Function Signature: ```def number_non_blank_lines(lines):```

Contract:
* The function must return a generator object.
* The function must skip any line that is empty or contains only whitespace.
* The function must yield the remaining lines, each prefixed with "N: " where N is the 1-indexed count of the non-blank lines yielded so far.

Asserts
```python
lines = [
    "First real line",
    "  ",
    "Second real line",
    "",
    "Third real line"
]
gen = number_non_blank_lines(lines)
assert next(gen) == "1: First real line"
assert next(gen) == "2: Second real line"
assert next(gen) == "3: Third real line"

lines_data_2 = ["   ", "Non-blank", "  \t ", "Another"]
expected_2 = ["1: Non-blank", "2: Another"]
assert list(number_non_blank_lines(lines_data_2)) == expected_2
assert list(number_non_blank_lines(["", "   "])) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def number_non_blank_lines(lines):

    line_count = 1
    for line in lines:
        if line and not line.isspace():
            yield f"{line_count}: {line}"
            line_count += 1

```

</details>

#### 4. Parse Key-Value Pairs

Problem Statement: Create a generator function that parses lines of the format "key=value" and yields a tuple of (key, value).

Function Signature: ```def parse_key_value(lines):```

Contract

* The function must return a generator object.
* The function must parse each line formatted as "key=value", splitting on the first '=' character.
* The function must yield a two-element tuple (key, value).
* The function must strip any leading/trailing whitespace from both the key and the value before yielding.

Asserts
```python
lines = [
    "name=Alice",
    "  age = 30  ",
    "city=New York",
    "role=Software Engineer=Advanced"
]
gen = parse_key_value(lines)
assert next(gen) == ("name", "Alice")
assert next(gen) == ("age", "30")
assert next(gen) == ("city", "New York")
assert next(gen) == ("role", "Software Engineer=Advanced")

lines_data_2 = ["item=book", "price=15.99 "]
expected_2 = [("item", "book"), ("price", "15.99")]
assert list(parse_key_value(lines_data_2)) == expected_2
```

<details> 
<summary>Possible Solution</summary> 

```python
def parse_key_value(lines):
  
    cleaned = []
    even = []
    odd = []

    for line in lines:
        temp_line = line.split("=", 1)
        for string in temp_line: 
            result = string.strip()
            cleaned.append(result)

    for i in range(len(cleaned)):
        if i % 2 == 0:
            even.append(cleaned[i])
        else:
            odd.append(cleaned[i])

    final = list(zip(even, odd))
    for item in final:
        yield item
```

</details>

#### 5. Skip First N Lines

Problem Statement: Create a generator function that yields all lines from an iterable ​after​ skipping the first n lines.

Function Signature:  ```def skip_header(lines, n):```

Contract

* The function must return a generator object.
* The function must not yield any of the first n lines from the input iterable.
* The function must yield all subsequent lines in their original order.
* If the iterable has n or fewer lines, the generator should be empty.

Asserts
```python
lines = ["Header 1", "Header 2", "Data 1", "Data 2", "Data 3"]
gen = skip_header(lines, 2)
assert next(gen) == "Data 1"
assert next(gen) == "Data 2"
assert next(gen) == "Data 3"

lines_data_2 = ["a", "b", "c", "d"]
assert list(skip_header(lines_data_2, 3)) == ["d"]
assert list(skip_header(lines_data_2, 4)) == []
assert list(skip_header(lines_data_2, 5)) == []
assert list(skip_header(lines_data_2, 0)) == ["a", "b", "c", "d"]
```

<details> 
<summary>Possible Solution</summary> 

```python
def skip_header(lines, n):

   for index, value in enumerate(lines):
        if index < n:
            continue
        yield value
```

</details>

#### 6. Extract Log Messages by Level

Problem Statement: Create a generator function that processes log lines with the format "LEVEL: Message". It should filter for a specific log level and yield only the message part.

Function Signature: ```def extract_log_messages(lines, level):```

Contract

* The function must return a generator object.
* The function must only process lines that start with the prefix f"{level}: ".
* The prefix matching must be case-sensitive.
* For each matching line, it must yield the message part (the text after the prefix) with leading/trailing whitespace removed.

Asserts
```python
log_lines = (
    "INFO: System starting up",
    "DEBUG: Variable x=10",
    "ERROR:   File not found   ",
    "INFO: System shutting down",
    "error: lowercase error",
)
gen = extract_log_messages(log_lines, "INFO")
assert next(gen) == "System starting up"
assert next(gen) == "System shutting down"

assert list(extract_log_messages(log_lines, "ERROR")) == ["File not found"]
assert list(extract_log_messages(log_lines, "WARNING")) == []
assert list(extract_log_messages(log_lines, "error")) == ["lowercase error"]
```

<details> 
<summary>Possible Solution</summary> 

```python
def extract_log_messages(lines, level):

    for line in lines:
        if line.startswith(level):
            temp = line.split(": ")
            yield temp[1].strip()
```

</details>

#### 7. Data Processing Pipeline

Problem Statement:  Create two separate generator functions to form a processing pipeline. The first function, clean_lines, should remove comments and extra whitespace. The second function, extract_numbers, should take the output of the first and yield only valid integers.

Function Signatures:
```def clean_lines(lines):``` 
```def extract_numbers(cleaned_lines):``` 

Contract for `clean_lines`:

* The function must return a generator object.
* The function must skip any line that starts with '#'.
* The function must yield the remaining lines with leading/trailing whitespace removed.

Contract for `extract_numbers`

* The function must return a generator object.
* The function must take an iterable of cleaned strings as input.
* The function must attempt to convert each string to an integer.
* The function must yield only the strings that successfully convert to integers, as int types.

Asserts
```python
raw_data = ["100", "# This is a comment", "  250 ", "   -50", "not a number", "42"]
cleaned = clean_lines(raw_data)
numbers_gen = extract_numbers(cleaned)
assert list(numbers_gen) == [100, 250, -50, 42]

data_2 = ["# Header", "1", "2", "  # Another comment", "3", "3.14"]
expected_2 = [1, 2, 3]
assert list(extract_numbers(clean_lines(data_2))) == expected_2
```

<details> 
<summary>Possible Solution</summary> 

```python
def clean_lines(lines):
    for line in lines:
        if line.startswith("# "):
            continue
        result = line.strip()
        yield result

def extract_numbers(cleaned_lines):

    for line in cleaned_lines:
        try: 
            if line.isdigit() or line.startswith("-"):
                integered = int(line)
                yield integered
            
        except TypeError:
            continue
```

</details>

#### 8. Positive Integers with a Generator Expression

Problem Statement: Write a function that accepts an iterable of numbers and returns a generator that yields only the positive numbers. You must implement this using a generator expression within a single return statement.

Function Signature:  ```def get_positives(numbers):```

Contract

* The function must return a generator object.
* The implementation must consist of a single line: return (expression).
* The generator must yield only the numbers from the input iterable that are strictly greater than 0.

Asserts
```python
from types import GeneratorType

numbers = [10, -5, 0, 1, 100, -20, 7]
positive_gen = get_positives(numbers)
assert isinstance(positive_gen, GeneratorType)
assert list(positive_gen) == [10, 1, 100, 7]

numbers_2 = [-1, -2, -3, 0]
assert list(get_positives(numbers_2)) == []
assert list(get_positives([1, 2, 3])) == [1, 2, 3]
```

<details> 
<summary>Possible Solution</summary> 

```python
def get_positives(numbers):
    return (number for number in numbers if number > 0)
```

</details>

#### 9. Chaining Iterables with yield from

Problem Statement: Create a generator function that combines two iterables of lines into a single sequence using yield from.

Function Signature: ```def chain(iter1, iter2):```

Contract

* The function must return a generator object.
* The function must yield all items from `iter1` in order, followed by all items from `iter2` in order.
* The implementation must use yield from for both iterables.

Asserts
```python
source1 = ["a", "b"]
source2 = ("c", "d")
gen = chain(source1, source2)
assert list(gen) == ["a", "b", "c", "d"]

assert list(chain([], [1, 2])) == [1, 2]
assert list(chain([1, 2], [])) == [1, 2]
assert list(chain(range(2), "xy")) == [0, 1, "x", "y"]
```

<details> 
<summary>Possible Solution</summary> 

```python
def chain(iter1, iter2):

    iterables = [iter1, iter2]
    for iterable in iterables:
        for element in iterable:
            yield element
```

</details>

#### 10. Summarize CSV Data

Problem Statement: Create a generator function that processes CSV data representing fruit inventory. Filter for a specific fruit and yield a formatted summary string for each matching entry.

Function Signature: ```def summarize_fruit_inventory(lines, fruit_name):```

Contract

* The function must return a generator object.
* The function must process lines of comma-separated values with the format "fruit,quantity,color".
* The function must filter for lines where the first value matches fruit_name (case-insensitively).
* For each matching line, the function must yield a formatted string: `"Found {quantity} {color} {fruit_name}(s)."`.

Asserts

```python
inventory_data = (
    "apple,100,red",
    "banana,150,yellow",
    "Apple,50,green",
    "grape,200,purple"
)
gen = summarize_fruit_inventory(inventory_data, "apple")
assert next(gen) == "Found 100 red apple(s)."
assert next(gen) == "Found 50 green apple(s)."

data_2 = ["Banana,20,yellow", "Orange,30,orange"]
assert list(summarize_fruit_inventory(data_2, "banana")) == ["Found 20 yellow banana(s)."]
assert list(summarize_fruit_inventory(data_2, "pear")) == []
```

<details> 
<summary>Possible Solution</summary> 

```python
def summarize_fruit_inventory(lines, fruit_name):

    working = []
    for line in lines:
        temp = line.split(",")
        super_temp = []
        for word in temp:
            new_word = word.lower()
            super_temp.append(new_word)
        working.append(super_temp)

    for sublist in working:
        if sublist[0] == fruit_name:
            yield f"Found {sublist[1]} {sublist[2]} {fruit_name}(s)."
```

</details>

[Back to the top](#top)
***

## Lesson 2: Advanced Concepts

### Arguments and Parameters

#### 1. Positional vs. Keyword Arguments: Argument Equivalence

Problem Statement​: Below is a function `describe_shape` and a list of five function calls. For each call, determine if it will execute successfully. Do not run the code; reason about how Python binds the arguments to the parameters.

Function Signature​: 

```python
def describe_shape(sides, name, color="black"):
    pass
```

Contract​:
* `sides`: An integer representing the number of sides.
* `name`: A string, the name of the shape.
* `color`: An optional string for the shape's color, defaulting to "black".
* The function's implementation is not relevant.

Function Calls to Analyze​:

```python
# Call 1
describe_shape(4, "square", "blue")

# Call 2
describe_shape(name="circle", sides=1)

# Call 3
describe_shape("triangle", 3)

# Call 4
describe_shape(5, "pentagon")

# Call 5
describe_shape(sides=6, name="hexagon", "red")
```

<details> 
<summary>Possible Solution</summary> 

```python
def describe_shape(sides, name, color="black"): #Will Run
    pass

# Call 1
describe_shape(4, "square", "blue") #Will Run

# Call 2
describe_shape(name="circle", sides=1) #Will run

# Call 3
describe_shape("triangle", 3) #Will run, because they are two positions and nothing in the body that would force a TypeError

# Call 4
describe_shape(5, "pentagon") #Will run

# Call 5
describe_shape(sides=6, name="hexagon", "red") #Won't run. Positional arguments cannot appear after keyword arguments.
```
</details>

#### 2. Enforcing Positional-Only Arguments: API Command Handler

Problem Statement​: Implement a function that takes exactly two arguments: a command name (which must be positional) and a target.

Function Signature​:

```python
def execute_command(#insert arguments here):
    return f"Executing {command} on {target}."
```

Contract​:

* `command`: A string, the name of the command to execute. Must be passed positionally.
* `target`: A string, the target of the command. Can be passed positionally or by keyword.
* ​Returns​: A formatted string confirming the execution.

Test Cases​:
```python
assert execute_command("start", "server") == "Executing start on server."
assert execute_command("stop", target="database") == "Executing stop on database."

# The following call should raise a TypeError:
execute_command(command="restart", target="worker")
```


<details> 
<summary>Possible Solution</summary> 

```python
def execute_command(command, /, target):
    return f"Executing {command} on {target}."
```

</details>


#### 3. Enforcing Keyword-Only Arguments: Configuration Options

Problem Statement​: Write a function signature for configure_system that meets the following requirements:

1. It must accept one required positional argument, hostname.
2. It must accept two optional keyword-only arguments, `port (default 8080)` and `ssl_enabled (default False)`.

Implement the function to return a dictionary of the final configuration.

Function Signature​: You must design the signature.

Contract​:

* `hostname`: A required string.
* `port`: An optional integer, keyword-only.
* `ssl_enabled`: An optional boolean, keyword-only.
* ​Returns​: A dictionary containing the keys `hostname`, `port`, and `ssl_enabled`.

Test Cases​:

```python
# Replace `configure_system` with your implementation
assert configure_system("api.launchschool.com") == {
    "hostname": "api.launchschool.com",
    "port": 8080,
    "ssl_enabled": False,
}
assert configure_system("app.launchschool.com", port=443, ssl_enabled=True) == {
    "hostname": "app.launchschool.com",
    "port": 443,
    "ssl_enabled": True,
}

# The following call should raise a TypeError:
configure_system("db.launchschool.com", 5432)
```

<details> 
<summary>Possible Solution</summary> 

```python
def configure_system(hostname, /, *, port=8080, ssl_enabled=False ):
    result = {}
    result['hostname'] = hostname
    result['port']= port
    result['ssl_enabled'] = ssl_enabled
    return result

```

</details>

#### 4. Fixing a Broken Signature

Problem Statement​: The following function signature has a SyntaxError. Correct the signature so that the function can be defined and the provided assertions pass. Do not change the function body.

Function Signature (Incorrect)​:

```python
def create_product(name, price=0.0, stock_count):
    return {"name": name, "price": price, "stock_count": stock_count}
```

Contract​:

* `name`: A required string, the product name.
* `stock_count`: A required integer, the number of items in stock.
* `price`: An optional float, the product price.
* ​Returns​: A dictionary representing the product.

Test Cases​:
```python
# Replace `create_product` with your corrected implementation
assert create_product("Laptop", 50) == {"name": "Laptop", "price": 0.0, "stock_count": 50}
assert create_product("Mouse", 200, 25) == {"name": "Mouse", "stock_count": 200, "price": 25}
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### 5. Aggregating Positional Arguments: Sum of All Numbers

Problem Statement​: Implement a function that accepts any number of numeric arguments and returns their sum. If no arguments are provided, it should return 0.

Function Signature​:

```python
def sum_all(*numbers):
    pass # Your implementation here
```

Contract​:

* `*numbers`: A variable number of integers or floats.
* Returns​: The sum of all provided numbers.

Test Cases​:
```python
assert sum_all(1, 2, 3) == 6
assert sum_all(10, 20) == 30
assert sum_all() == 0
assert sum_all(3.5, 1.5, 2.0) == 7.0
```

<details> 
<summary>Possible Solution</summary> 

```python

def sum_all(*numbers):
    if not numbers:
        return 0
    return sum(numbers)
```

</details>

#### 6. Handling Arbitrary Keyword Arguments: HTML Attribute Formatter

Problem Statement​: Implement a function that takes any number of keyword arguments and formats them into an HTML attribute string. For example, `id="main"` and `class_="container"` should become `id="main" class="container"`.

Function Signature​: ``` def format_html_attributes(**attributes):```

Contract​:

* `**attributes`: Keyword arguments representing HTML attributes.
* ​Returns​: A single string with a leading space, containing all attributes formatted as key="value" pairs separated by spaces. The order is not important.

Test Cases​:
```python
result1 = format_html_attributes(id="profile-pic", src="user.jpg", alt="User photo")
assert ' id="profile-pic"' in result1
assert ' src="user.jpg"' in result1
assert ' alt="User photo"' in result1

assert format_html_attributes(href="/home", target="_blank") == ' href="/home" target="_blank"'
assert format_html_attributes() == ""
```

<details> 
<summary>Possible Solution</summary> 

```python
def format_html_attributes(**attributes):

    result = ""
    for key, value in attributes.items():
       result += f' {key}="{value}"'
    return result 
```

</details>

#### 7. Designing a Robust API​: User Profile Creator

Problem Statement​: Design and implement a function create_user_profile that adheres to a strict API contract. The username must be provided positionally and cannot be passed as a keyword. All other profile information (e.g., age, city, bio) must be provided as keyword arguments.

Function Signature​: You must design the signature.

Contract​:

* A required, positional-only username string.
* Any number of optional keyword arguments for other profile data.
* ​Returns​: A dictionary containing the username and all other provided profile data.

Test Cases​:
```python
# Replace `create_user_profile` with your implementation
assert create_user_profile("py-student") == {"username": "py-student"}
assert create_user_profile("js-student", age=25, city="Online") == {
    "username": "js-student",
    "age": 25,
    "city": "Online",
}

# The following call should raise a TypeError:
create_user_profile(username="rb-student")
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### 8. Combining Positional and Variable Arguments: Prefixed Logger

Problem Statement​: Implement a function that takes a required prefix string and any number of additional positional arguments (items). The function should return a list where each item is a string formatted as "[PREFIX] item".

Function Signature​: ```def log_items(prefix, *items):```

Contract​:

*   `prefix`: A string to prepend to each item.
*   `*items`: A variable number of items to be logged.
*   ​Returns​: A list of formatted strings.

Test Cases​:

```python
assert log_items("INFO", "Server starting", "Port 8080") == [
    "[INFO] Server starting",
    "[INFO] Port 8080",
]
assert log_items("DEBUG") == []
assert log_items("ERROR", 404, "Not Found") == ["[ERROR] 404", "[ERROR] Not Found"]
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### 9. Refactoring for Readability: Refactor Plotting Function

Problem Statement​: The function generate_plot is hard to use because callers must remember the correct order for the boolean flags. Refactor its signature to make show_grid and log_scale keyword-only arguments, improving call-site readability. Do not change the function body.

Function Signature (Original)​:

```python
def generate_plot(data, show_grid=True, log_scale=False):
    # Imagine complex plotting logic here
    return {"data_points": len(data), "grid": show_grid, "log": log_scale}
```

Contract (for the refactored function)​:

* `data`: A required list of data points.
* `show_grid`: An optional, keyword-only boolean.
* `log_scale`: An optional, keyword-only boolean.
* Returns​: A dictionary summarizing the plot configuration.

Test Cases (for the refactored function)​:

```python
# Replace `generate_plot` with your refactored implementation
assert generate_plot([1, 2, 3]) == {"data_points": 3, "grid": True, "log": False}
assert generate_plot([1, 2, 3], log_scale=True) == {"data_points": 3, "grid": True, "log": True}
assert generate_plot([1, 2, 3], show_grid=False, log_scale=True) == {
    "data_points": 3,
    "grid": False,
    "log": True,
}

# The following call should raise a TypeError with the refactored signature:
generate_plot([1, 2, 3], False)
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### 10. Call Analysis with Mixed Parameters​: Event Scheduler Validation

Problem Statement​: Analyze the five calls to the schedule_task function below. For each call, determine if it is valid or if it will raise a TypeError. Explain the reason for any failures.

Function Signature​:

```python
def schedule_task(task_id, /, due_date, *, priority="normal", assignee=None):
    pass
```

Contract​:

* `task_id`: Positional-only integer.
* `due_date`: Positional or keyword string.
* `priority`: Keyword-only string.
* `assignee`: Keyword-only string.
* The function's implementation is not relevant.

Function Calls to Analyze​:
```python
# Call 1
schedule_task(101, "2024-12-25", priority="high", assignee="Alice")

# Call 2
schedule_task(102, due_date="2025-01-01")

# Call 3
schedule_task(103, "2024-11-30", "low")

# Call 4
schedule_task(task_id=104, due_date="2025-02-01")

# Call 5
schedule_task(105, "2024-10-31", assignee="Bob")
```
<details> 
<summary>Possible Solution</summary> 
</details>

#### 11. Implementing a kwargs Filter: Allowed Options Filter

Problem Statement​: Implement a utility function filter_options that accepts a set of allowed_keys and an arbitrary number of keyword arguments. It should return a new dictionary containing only the key-value pairs from the keyword arguments where the key is present in allowed_keys.

Function Signature​:

```python
def filter_options(allowed_keys, **options):
    pass # Your implementation here
```

Contract​:

* `allowed_keys`: A set of strings representing valid option keys.
* `**options`: Arbitrary keyword arguments.
* ​Returns​: A new dictionary with filtered key-value pairs.

Test Cases​:
```python
allowed = {"font_size", "color", "background"}
result = filter_options(allowed, font_size=12, color="blue", margin=10, background="white")
assert result == {"font_size": 12, "color": "blue", "background": "white"}

allowed2 = {"user", "action"}
result2 = filter_options(allowed2, user="admin", timestamp="12345")
assert result2 == {"user": "admin"}
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### 12. Choosing the Right Parameter Types: Database Connection String Builder

Problem Statement​: Design a function signature for `build_connection_string`. The function's purpose is to construct a database connection string.

* The db_type (e.g., "postgresql", "mysql") is required and should be positional-only to ensure it's always first.
* The host is required and can be positional or keyword.
* All other connection parameters (e.g., user, password, port, dbname) are optional and must be keyword-only for clarity.

Implement the function to return the connection string.

Function Signature​: You must design the signature.

Contract​:

* `db_type`: A required, positional-only string.
* `host`: A required string.
* Other parameters are optional and keyword-only.
* ​Returns​: A formatted connection string. For example: `"postgresql://user:password@host:port/dbname"`. The exact format can vary, but it should include all provided components.

Test Cases​:
```python
# Replace `build_connection_string` with your implementation
# The exact string format is flexible, but it must contain the right info.
assert build_connection_string("postgresql", "localhost", user="admin", dbname="app_db") == "postgresql://admin@localhost/app_db"
assert build_connection_string("mysql", "127.0.0.1", port=3306, user="root") == "mysql://root@127.0.0.1:3306"

# The following call should raise a TypeError:
build_connection_string(db_type="sqlite", host="file.db")
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### 13. The "Multiple Values for Argument" Error: Uncovering a Tricky TypeError

Problem Statement​: One of the three calls to process_data below will raise a TypeError with the message "got multiple values for argument".Identify which call fails and explain precisely why Python raises this specific error.

Function Signature​:
```python
def process_data(item_id, /, content, *, version=1):
    pass
```

Function Calls to Analyze​:
```python
# Call 1
process_data(1, "some data", version=2)

# Call 2
process_data(2, content="more data")

# Call 3
process_data(3, "extra data", item_id=3)
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### 14.Combining Positional-Only, *args, and **kwargs: Universal Function Wrapper

Problem Statement​: Implement a function invoke that acts as a universal wrapper. It takes a callable function func as its first argument (positional-only), followed by any number of positional and keyword arguments, which it then passes on to func.

Function Signature​:
```python
def invoke(func, /, *args, **kwargs):
    return func(*args, **kwargs)
```

Contract​:

* `func`: A callable object (like a function or method), positional-only.
* `*args`: Any positional arguments to be passed to func.
* `**kwargs`: Any keyword arguments to be passed to func.
* ​Returns​: The return value of func(*args, **kwargs).

Test Cases​:
```python
def add(a, b):
    return a + b

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

assert invoke(add, 2, 3) == 5
assert invoke(add, b=5, a=10) == 15
assert invoke(greet, "World") == "Hello, World!"
assert invoke(greet, "Python", greeting="Welcome") == "Welcome, Python!"
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### 15. The Ultimate Argument Binding Challenge: Deconstruct the Master Signature

Problem Statement​: Below is a complex function signature and a list of function calls. Without running the code, determine which calls are valid and which will raise a TypeError. For each invalid call, state the specific binding rule that is violated.

Function Signature​:
```python
def master_assembler(part_id, /, vendor, *components, location="default", **options):
    pass
```

Contract​:

* `part_id`: Positional-only integer.
* `vendor`: Positional or keyword string.
* `*components`: Variable-length tuple of component strings.
* `location`: Keyword-only string with a default value.
* `**options`: Arbitrary keyword arguments (e.g., priority=True, fast_track=False).

Function Calls to Analyze​:
```python
# Call 1
master_assembler(1001, "Launch Inc.", "cpu", "ram", location="lab", priority=True)

# Call 2
master_assembler(1002, vendor="School Co.", location="warehouse")

# Call 3
master_assembler(1003, "LS Supplies", "case", "psu", "lab")

# Call 4
master_assembler(part_id=1004, vendor="LS Supplies")

# Call 5
master_assembler(1005, "LS Supplies", "gpu", location="lab", components=("ssd",))
```

<details> 
<summary>Possible Solution</summary> 
</details>

[Back to the top](#top)

### Iterable Unpacking


#### 1. Predict the Unpacking

**Problem Statement:** What will `first`, `middle`, and `last` contain after this code executes? No code is required.

```python
first, *middle, last = "Python"
```

<details>
<summary>Possible Solution</summary>

```python
print(first) # "P"
print(middle) # ['y', 't', 'h', 'o']
print(last) # "n"
```

</details>

#### 2. Predict Nested Star Unpacking

**Problem Statement:** What will `name`, `scores`, and `comment` contain after this code executes? No code is required.

```python
record = ('Alice', 95, 88, 92, "Excellent work")
name, *scores, comment = record
```

<details>
<summary>Possible Solution</summary>

```python
print(name)    # "Alice"
print(scores)  # [95, 88, 92]
print(comment) # "Excellent Work"
```

</details>

#### 3. Identify the Error

**Problem Statement:** Without running the code, identify the exception and the loop iteration on which it occurs.

```python
def process_records(records):
    processed = []
    for name, age, city in records:
        processed.append(f"{name} from {city} is {age}")
    return processed

data = [('Alice', 30, 'New York'), ('Bob', 25), ('Charlie', 35, 'Los Angeles')]
```

<details>
<summary>Possible Solution</summary>

Error happens on the second iteration. City is expected and there's no City, so it returns a `"Value Error, not enough values to unpack (expected 3, got 2)"`
</details>

#### 4. Format Person Data

Write `format_person(person_tuple)` using unpacking. Input is `(first_name, last_name, age)`; return `"Last, First (Age: Age)"`.

```python
assert format_person(('John', 'Doe', 35)) == "Doe, John (Age: 35)"
assert format_person(('Grace', 'Hopper', 85)) == "Hopper, Grace (Age: 85)"
```

<details>
<summary>Possible Solution</summary>

```python
def format_person(person_tuple):
    first_name, last_name, age = person_tuple
    return f"{last_name}, {first_name} (Age: {age})"
```

</details>

#### 5. Refactor Record Parsing from Indexing

Refactor the original function using one unpacking assignment.

```python
def parse_record_with_indexing(record):
    return f"ID: {record[0]}, Name: {record[1]}, Score: {record[2]}"

def parse_record_with_unpacking(record):
    pass

assert parse_record_with_unpacking((101, 'Alice', 95)) == "ID: 101, Name: Alice, Score: 95"
```

<details>
<summary>Possible Solution</summary>

```python
def parse_record_with_indexing(record):
    return f"ID: {record[0]}, Name: {record[1]}, Score: {record[2]}"

def parse_record_with_unpacking(record):
    id, name, score = record
    return f"ID: {id}, Name: {name}, Score: {score}"

assert parse_record_with_unpacking((101, 'Alice', 95)) == "ID: 101, Name: Alice, Score: 95"
```

</details>

#### 6. Unpack a Function's Return Value

Implement `get_division_details(dividend, divisor)`. Call `divmod()` once, unpack its result, and return `{'quotient': ..., 'remainder': ...}`.

```python
assert get_division_details(10, 3) == {'quotient': 3, 'remainder': 1}
assert get_division_details(10, 2) == {'quotient': 5, 'remainder': 0}
assert get_division_details(7, 8) == {'quotient': 0, 'remainder': 7}
```

<details>
<summary>Possible Solution</summary>

```python
def get_division_details(dividend, divisor):
    result = {}
    quotient, remainder = divmod(dividend, divisor)
    result['quotient'] = quotient
    result['remainder'] = remainder
    return result
```

</details>

#### 7. Unpack Tuple as Function Arguments

Implement `calculate_distance(point)` by calling the helper with `*` positional unpacking.

```python
import math
def distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

assert calculate_distance((3, 4)) == 5.0
assert calculate_distance((0, 0)) == 0.0
```

<details>
<summary>Possible Solution</summary>

```python
import math
def distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

def calculate_distance(point):
    return distance_from_origin(*point)
```

</details>

#### 8. Unpack into a Single Starred Variable

Implement `collect_into_list(iterable)` using an assignment of the form `*var, = iterable`.

```python
assert collect_into_list((1, 2, 3)) == [1, 2, 3]
assert collect_into_list("abc") == ['a', 'b', 'c']
assert collect_into_list(range(3)) == [0, 1, 2]
```

<details>
<summary>Possible Solution</summary>

```python
def collect_into_list(iterable):
    *var, = iterable 
    return var
```

Python does not allow a starred target to stand alone in an assignment. In *var, = iterable, the comma establishes an unpacking assignment containing one starred target. Since there are no other targets to satisfy, *var collects every element produced by the iterable into a list.

</details>

#### 9. Extract Head and Tail

Implement `get_head_and_tail(sequence)` using starred unpacking. Return `(head, tail_list)`; input has at least one element.

```python
assert get_head_and_tail([1, 2, 3, 4]) == (1, [2, 3, 4])
assert get_head_and_tail(['a', 'b', 'c']) == ('a', ['b', 'c'])
assert get_head_and_tail([100]) == (100, [])
assert get_head_and_tail(('first',)) == ('first', [])
```

<details>
<summary>Possible Solution</summary>

```python
def get_head_and_tail(sequence):

    head, *tail_list = sequence
    return (head, tail_list)
```

</details>

#### 10. Ignore First and Last

Implement `get_inner_elements(sequence)` using starred unpacking and throwaway variables. Input has at least two elements; return the inner elements as a list.

```python
assert get_inner_elements([1, 2, 3, 4, 5]) == [2, 3, 4]
assert get_inner_elements(['a', 'b', 'c', 'd']) == ['b', 'c']
assert get_inner_elements([1, 10]) == []
assert get_inner_elements((1, 2, 3)) == [2]
```

<details>
<summary>Possible Solution</summary>

```python

def get_inner_elements(sequence):
    first, *middle, last = sequence
    return middle
```

</details>

#### 11. Extract Edges and Core

Implement `extract_edges_and_core(seq)` with one starred expression; return `(first, core_list, last)`.

```python
assert extract_edges_and_core((10, 20, 30, 40, 50, 60)) == (10, [20, 30, 40, 50], 60)
assert extract_edges_and_core(['start', 'middle', 'end']) == ('start', ['middle'], 'end')
assert extract_edges_and_core((1, 2)) == (1, [], 2)
```

<details>
<summary>Possible Solution</summary>

```python
def extract_edges_and_core(sequence):
    first, *middle, end = sequence
    return (first, middle, end)
```

</details>

#### 12. Swap First and Last Elements

Implement `swap_first_last(seq)` using unpacking to capture first, middle, and last. Return a new list.

```python
assert swap_first_last([1, 2, 3, 4]) == [4, 2, 3, 1]
assert swap_first_last(('a', 'b', 'c')) == ['c', 'b', 'a']
assert swap_first_last([10, 20]) == [20, 10]
```

<details>
<summary>Possible Solution</summary>

```python
def swap_first_last(sequence):
    first, *middle, last = sequence
    return [last, *middle, first]
```

</details>

#### 13. Refactor with For-Loop Unpacking

Refactor this indexing-based inventory formatter as `format_inventory_unpacked(items)` using loop unpacking and identical output.

```python
def format_inventory_indexed(items):
    formatted_strings = []
    for i in range(len(items)):
        item = items[i]
        name = item[0]
        quantity = item[1]
        formatted_strings.append(f"{name}: {quantity}")
    return formatted_strings

inventory = [('Apples', 10), ('Bananas', 5), ('Oranges', 8)]
assert format_inventory_unpacked(inventory) == ['Apples: 10', 'Bananas: 5', 'Oranges: 8']
assert format_inventory_unpacked([]) == []
assert format_inventory_unpacked([('Milk', 1)]) == ['Milk: 1']
```

<details>
<summary>Possible Solution</summary>

```python

def format_inventory_indexed(items):
    formatted_strings = []
    for i in range(len(items)):
        item = items[i]
        name = item[0]
        quantity = item[1]
        formatted_strings.append(f"{name}: {quantity}")
    return formatted_strings

def format_inventory_unpacked(items):
    result = []
    for item in items:
        name, quantity = item
        result.append(f"{name}: {quantity}")
    return result

inventory = [('Apples', 10), ('Bananas', 5), ('Oranges', 8)]
```

</details>

#### 14. Unpack Dictionary Items

Implement `format_env_vars(env_dict)` using loop unpacking over `.items()`; return `"KEY=VALUE"` strings.

```python
config = {'USER': 'admin', 'HOME': '/home/admin', 'DEBUG': 'False'}
expected = ['USER=admin', 'HOME=/home/admin', 'DEBUG=False']
assert sorted(format_env_vars(config)) == sorted(expected)
assert format_env_vars({}) == []
assert format_env_vars({'API_KEY': '12345'}) == ['API_KEY=12345']
```

<details>
<summary>Possible Solution</summary>

```python
def format_env_vars(env_dict):
    result = []
    for key, value in env_dict.items():
        result.append(f"{key}={value}")
    return result

config = {'USER': 'admin', 'HOME': '/home/admin', 'DEBUG': 'False'}
expected = ['USER=admin', 'HOME=/home/admin', 'DEBUG=False']
```

</details>

#### 15. Summarize Configuration Dictionary

Implement `summarize_config(config_dict)` using unpacking over `.items()`. Return sorted `"key -> value"` strings.

```python
config = {'host': 'localhost', 'port': 8080, 'user': 'admin'}
assert summarize_config(config) == ['host -> localhost', 'port -> 8080', 'user -> admin']
assert summarize_config({}) == []
```

<details>
<summary>Possible Solution</summary>

```python

def summarize_config(config_dict):
    result = []
    for key, value in config_dict.items():
        result.append(f"{key} -> {value}")
    return result

config = {'host': 'localhost', 'port': 8080, 'user': 'admin'}
```

</details>

#### 16. Create Indexed Log Entries

Implement `create_indexed_logs(events)` using `enumerate` and loop unpacking. Format each item as `"[index] Event: event_description"`.

```python
assert create_indexed_logs(['Login', 'Update Profile', 'Logout']) == ['[0] Event: Login', '[1] Event: Update Profile', '[2] Event: Logout']
assert create_indexed_logs([]) == []
```

<details>
<summary>Possible Solution</summary>

```python
def create_indexed_logs(events):

    result = []
    for i, item in enumerate(events):
        result.append(f"[{i}] Event: {item}")
    return result
```

</details>

#### 17. Process Coordinates

Implement `total_manhattan_distance(path)` using loop unpacking. Sum `abs(x) + abs(y)` for all coordinate pairs.

```python
assert total_manhattan_distance([(1, 1), (2, 3), (-1, -1)]) == 9
assert total_manhattan_distance([(10, 0), (0, -10)]) == 20
assert total_manhattan_distance([]) == 0
```

<details>
<summary>Possible Solution</summary>

```python
def total_manhattan_distance(path):

    summed = 0
    for element in path:
        x, y = element
        temp_sum = abs(x) + abs(y)
        summed += temp_sum
    return summed
```

</details>

#### 18. Extract Coordinates with a List Comprehension

Implement `extract_coordinates(points)` as one list comprehension using unpacking to discard each point name.

```python
assert extract_coordinates([('A', 1, 5), ('B', 3, 2), ('C', 9, 8)]) == [(1, 5), (3, 2), (9, 8)]
assert extract_coordinates([]) == []
```

<details>
<summary>Possible Solution</summary>

```python
def extract_coordinates(points):

    return [(number_1, number_2) for letter, number_1, number_2 in points]

```

</details>

#### 19. Combine Parallel Lists with Zip

Implement `create_record(headers, values)` using `zip` plus unpacking in a dictionary comprehension.

```python
assert create_record(['name', 'age', 'city'], ['Alice', 30, 'New York']) == {'name': 'Alice', 'age': 30, 'city': 'New York'}
assert create_record([], []) == {}
```

<details>
<summary>Possible Solution</summary>

```python
def create_record(headers, values):

    total_record = zip(headers, values)
    return {header: value for header, value in list(total_record)}
```

</details>

#### 20. Unpacking in Comprehensions

Implement `process_with_comprehensions(data)` with dictionary and set comprehensions using unpacking. Return `(last_value_per_key, unique_keys)`.

```python
dict_res, set_res = process_with_comprehensions([('a', 1), ('b', 2), ('a', 3), ('c', 4)])
assert dict_res == {'a': 3, 'b': 2, 'c': 4}
assert set_res == {'a', 'b', 'c'}
```

<details>
<summary>Possible Solution</summary>

```python
def process_with_comprehensions(data):

    last_value_per_key = {key: value for key, value in data}
    unique_keys = {*last_value_per_key} # Remember that iterating over a dictionary produces its keys:
    return (last_value_per_key, unique_keys)

dict_res, set_res = process_with_comprehensions([('a', 1), ('b', 2), ('a', 3), ('c', 4)])
assert dict_res == {'a': 3, 'b': 2, 'c': 4}
assert set_res == {'a', 'b', 'c'}
```

</details>

#### 21. Unpack a Generator's Output

Implement `sum_weighted_values(generator)` using loop unpacking to sum `index * value`.

```python
def weighted_gen(data):
    for i, val in enumerate(data):
        yield (i, val)

assert sum_weighted_values(weighted_gen([10, 20, 30])) == 80
assert sum_weighted_values(weighted_gen([1, 1, 1, 1, 1])) == 10
assert sum_weighted_values(weighted_gen([])) == 0
```

<details>
<summary>Possible Solution</summary>

```python
def sum_weighted_values(generator):
    summed = 0
    for tuple_item in generator:
        i, val = tuple_item
        value = i * val
        summed += value
    return summed
```

</details>

#### 22. Unpack Generator of Key-Value Pairs

Implement `generator_to_dict(gen)` using loop unpacking.

```python
def kv_generator():
    yield 'key1', 'value1'
    yield 'key2', 'value2'
    yield 'key3', 'value3'

assert generator_to_dict(kv_generator()) == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```

<details>
<summary>Possible Solution</summary>

```python
def generator_to_dict(gen):
    return {key: value for key, value in gen}

def kv_generator():
    yield 'key1', 'value1'
    yield 'key2', 'value2'
    yield 'key3', 'value3'
```

</details>

#### 23. Refactor Nested Indexing

Refactor using one nested unpacking assignment.

```python
def format_contact_indexed(person_data):
    name = person_data[0]
    email = person_data[1][0]
    phone = person_data[1][1]
    return f"{name}'s contact info is {email} and {phone}."

assert format_contact_unpacked(('Alice', ('alice@example.com', '123-456-7890'))) == "Alice's contact info is alice@example.com and 123-456-7890."
assert format_contact_unpacked(('Bob', ('bob@work.com', '987-654-3210'))) == "Bob's contact info is bob@work.com and 987-654-3210."
```

<details>
<summary>Possible Solution</summary>

```python
def format_contact_unpacked(person_data):
    name, rest = person_data
    email, phone = rest
    return f"{name}'s contact info is {email} and {phone}."
```

</details>

#### 24. Process Nested Student Data

Implement `find_high_achievers(students)` with nested loop unpacking. Return names scoring at least 90 in both subjects.

```python
students = [('Alice', (91, 95)), ('Bob', (88, 92)), ('Charlie', (90, 90)), ('David', (95, 89))]
assert find_high_achievers(students) == ['Alice', 'Charlie']
assert find_high_achievers([('Eve', (100, 100))]) == ['Eve']
assert find_high_achievers([('Frank', (80, 80))]) == []
assert find_high_achievers([]) == []
```

<details>
<summary>Possible Solution</summary>

```python

def find_high_achievers(students):

    result = []
    for student in students:
        name, scores = student
        score_1, score_2 = scores
        if score_1 >= 90 and score_2 >= 90:
            result.append(name)

    return result
```

</details>

#### 25. Process Nested Geographic Coordinates

Implement `get_city_latitudes(data)` using nested unpacking. Records have the form `('CityName', ('Country', (latitude, longitude)))`; return `(city, latitude)` tuples.

```python
data = [('Tokyo', ('Japan', (35.6895, 139.6917))), ('New York', ('USA', (40.7128, -74.0060))), ('London', ('UK', (51.5074, -0.1278)))]
assert get_city_latitudes(data) == [('Tokyo', 35.6895), ('New York', 40.7128), ('London', 51.5074)]
```

<details>
<summary>Possible Solution</summary>

```python
def get_city_latitudes(data):

    result = []
    for data_element in data:
        city, rest = data_element
        country, coordinates = rest
        latitude, longitude = coordinates
        result.append((city, latitude))

    return result
```

</details>

#### 26. Parse Complex Nested Task Data

Implement `get_task_assignments(tasks)` using deeply nested unpacking. Input records are `(id, (project, status), (assignee, email))`; return `(id, project, email)`.

```python
tasks = [(101, ('Core-API', 'In-Progress'), ('J. Doe', 'j.doe@example.com')), (102, ('UI-Kit', 'Complete'), ('A. Smith', 'a.smith@example.com'))]
assert get_task_assignments(tasks) == [(101, 'Core-API', 'j.doe@example.com'), (102, 'UI-Kit', 'a.smith@example.com')]
```

<details>
<summary>Possible Solution</summary>

```python
def get_task_assignments(tasks):
    result = []
    for element in tasks:
        id, second, third = element
        project, status = second
        asignee, email = third
        result.append((id, project, email))
    return result
```

</details>

#### 27. Parse a Structured Record

Implement `parse_user_record(record)` using unpacking for `(id, name, email, *phone_numbers)`; return keys `id`, `name`, `email`, and `phones`.

```python
assert parse_user_record((1, 'Alice', 'alice@email.com', '111-222-3333', '444-555-6666')) == {'id': 1, 'name': 'Alice', 'email': 'alice@email.com', 'phones': ['111-222-3333', '444-555-6666']}
assert parse_user_record((2, 'Bob', 'bob@email.com')) == {'id': 2, 'name': 'Bob', 'email': 'bob@email.com', 'phones': []}
```

<details>
<summary>Possible Solution</summary>

```python
def parse_user_record(record):
    result = {}
    id, name, email, *phone_numbers = record
    result['id'] = id
    result['name'] = name
    result['email'] = email
    result['phones'] = phone_numbers
    return result
```

</details>

#### 28. Debug Unpacking ValueError

Fix the function for 3- or 4-element tuples using starred unpacking to ignore the optional ISBN.

```python
def get_book_details(book_tuple):
    title, author, year = book_tuple
    return f'"{title}" by {author} ({year})'

assert get_book_details_fixed(('The Hobbit', 'J.R.R. Tolkien', 1937)) == '"The Hobbit" by J.R.R. Tolkien (1937)'
assert get_book_details_fixed(('Dune', 'Frank Herbert', 1965, '0441013597')) == '"Dune" by Frank Herbert (1965)'
```

<details>
<summary>Possible Solution</summary>

```python
def get_book_details_fixed(book_tuple):
    title, author, year, *isbn = book_tuple
    return f'"{title}" by {author} ({year})'
```

</details>

#### 29. Debug Mismatched Unpacking

Implement `get_pass_list_fixed(grades)`. Each pair may be `[name, score]` or `[score, name]`; distinguish by type, use unpacking, and return passing names (score at least 60).

```python
grades = [['Alice', 95], ['Bob', 55], [88, 'Charlie'], ['David', 70]]
assert sorted(get_pass_list_fixed(grades)) == sorted(['Alice', 'Charlie', 'David'])
assert get_pass_list_fixed([[40, 'Eve'], ['Frank', 90]]) == ['Frank']
assert get_pass_list_fixed([]) == []
```

<details>
<summary>Possible Solution</summary>

```python
def get_pass_list_fixed(grades):

    result = []
    for element in grades:
        if type(element[0]) is str: 
            name, score = element
        else:
            score, name = element

        if score > 59:
            result.append(name)

    return result
```

</details>

#### 30. Process Configuration Tuples

Implement `process_config(config_list)`. Unpack 2- and 3-element tuples; default missing types to `'string'`. Return `{key: {'value': value, 'type': type}}`.

```python
configs = [('DEBUG', 'True', 'bool'), ('PORT', '8080', 'int'), ('SECRET_KEY', 'my-secret-key')]
expected = {'DEBUG': {'value': 'True', 'type': 'bool'}, 'PORT': {'value': '8080', 'type': 'int'}, 'SECRET_KEY': {'value': 'my-secret-key', 'type': 'string'}}
assert process_config(configs) == expected
assert process_config([]) == {}
```

<details>
<summary>Possible Solution</summary>

```python
def process_config(config_list):
    result = {}
   

    for item in config_list:
        sub_dict = {}
        action, value, *typed  = item
        sub_dict['value'] = value 
        sub_dict['type'] = typed[0] if typed else 'string'
        result[action] = sub_dict
        
    return result
```

</details>

#### 31. Parse Log Entry

Implement `parse_log_entry(entry)` for `TIMESTAMP LEVEL USER - MESSAGE`. Split and use starred unpacking; the message may contain spaces and must be returned as one string.

```python
assert parse_log_entry("2023-10-26T10:00:00 INFO admin - User logged in successfully") == {'timestamp': '2023-10-26T10:00:00', 'level': 'INFO', 'user': 'admin', 'message': 'User logged in successfully'}
assert parse_log_entry("2023-10-26T10:01:30 ERROR root - Disk space is low") == {'timestamp': '2023-10-26T10:01:30', 'level': 'ERROR', 'user': 'root', 'message': 'Disk space is low'}
```

<details>
<summary>Possible Solution</summary>

```python
def parse_log_entry(entry):

    result = {}
    timestamp, *rest = entry.split(" ", 1)
    etc = rest[0].split(" ", 2)
    result['timestamp'] = timestamp
    result['level'] = etc[0]
    result['user'] = etc[1]
    result['message'] = etc[2].lstrip("- ")

    return result
```

</details>

#### 32. Deconstruct File Paths

Implement `deconstruct_path(path)` using `split('/')` and unpacking. Return directory, filename, and extension for a Unix-style path with an extension.

```python
assert deconstruct_path("/usr/local/bin/script.py") == {'dir': '/usr/local/bin', 'filename': 'script', 'ext': 'py'}
assert deconstruct_path("docs/images/archive.zip") == {'dir': 'docs/images', 'filename': 'archive', 'ext': 'zip'}
assert deconstruct_path("main.c") == {'dir': '', 'filename': 'main', 'ext': 'c'}
```

<details>
<summary>Possible Solution</summary>

```python
def deconstruct_path(path):
    
    result = {}
   
    *directories, file = path.split("/")
    filename, extension = file.split(".")
    result['dir'] = "/".join(directories)
    result['filename'] = filename
    result['ext'] = extension

    return result
```

</details>

#### 33. Aggregate Sales Data

Implement `aggregate_sales(sales_records)` for `(product_id, amount, *discounts)`. Net is amount minus discounts; aggregate net totals by product.

```python
sales = [('p1', 100, 10, 5), ('p2', 200), ('p1', 150, 20), ('p3', 50, 5), ('p2', 250, 10, 10, 10)]
assert aggregate_sales(sales) == {'p1': 215, 'p2': 420, 'p3': 45}
assert aggregate_sales([]) == {}
```

<details>
<summary>Possible Solution</summary>

```python

def aggregate_sales(sales_records):

    result = {}
    for record in sales_records:
        product_id, amount, *discounts = record
        total_discount = sum(discounts)
        net = amount - total_discount
        result[product_id] = result.get(product_id, 0) + net
    return result
```

</details>

#### 34. Normalize and Summarize Student Grades

Implement `summarize_grades(student_data)`. Unpack name/scores, sort scores, use starred unpacking to drop the lowest, and return `(name, average_score)` with floating-point averages.

```python
students = [('Alice', [80, 90, 70, 100]), ('Bob', [100, 100, 100, 0]), ('Charlie', [95, 85])]
expected = [('Alice', 90.0), ('Bob', 100.0), ('Charlie', 95.0)]
assert summarize_grades(students) == expected
```

<details>
<summary>Possible Solution</summary>

```python
def summarize_grades(student_data):

    result = []
    for student in student_data:
        name, scores = student
        sorted_scores = sorted(scores)
        minimum, *aggregate_scores = sorted_scores
        average = sum(aggregate_scores)/len(aggregate_scores)
        result.append((name, float(average)))

    return result
```

</details>

[Back to the top](#top)

### Closure Practice

#### 1. Exercise: Basic Adder Factory

Problem Statement: Create a function `make_adder` that takes a single number n. It should return a new function that takes a single number `x` and returns the sum of `n` and `x`.

Function Signature: ```def make_adder(n):```

The function must:

* Accept a single numeric argument `n`.
* Return a new function (a closure).
* The returned function must accept a single numeric argument `x` and `return n + x`.

Asserts:

```python
add_5 = make_adder(5)
add_10 = make_adder(10)

assert add_5(10) == 15
assert add_5(20) == 25
assert add_10(10) == 20
assert add_10(0) == 10
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_adder(n):

    def adder(x):
        return n + x
    return adder
```

</details>

#### 2. Exercise: Configurable Multiplier

Problem Statement: Write a function `make_multiplier` that takes a numeric factor. It should return a new function that accepts a number and returns the product of that number and the original factor.

Function Signature: ```def make_multiplier(factor):```

The function must:

* Accept a single numeric argument factor.
* Return a new function.
* The returned function must accept a single numeric argument num and return factor * num.

Asserts:

```python
double = make_multiplier(2)
triple = make_multiplier(3)

assert double(5) == 10
assert double(100) == 200
assert triple(5) == 15
assert triple(10) == 30
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_multiplier(factor):

    def multiplier(value):
        return factor * value
    return multiplier
```

</details>

#### 3. Exercise: String Formatting Factory

Problem Statement: Write a function `make_string_formatter` that accepts two strings: prefix and suffix. It should return a new function that takes a string text and returns a new string formatted as prefix + text + suffix.

Function Signature: ```def make_string_formatter(prefix, suffix):```

The function must:

* Accept two string arguments, prefix and suffix.
* Return a new function.
* The returned function must accept a single string argument text and return the formatted string.

Asserts:

```python
format_bracket = make_string_formatter("[", "]")
format_wave = make_string_formatter("~~~ ", " ~~~")

assert format_bracket("hello") == "[hello]"
assert format_bracket("world") == "[world]"
assert format_wave("Python") == "~~~ Python ~~~"
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_string_formatter(prefix, suffix):

    def make_text(text):
        return prefix + text + suffix
    return make_text
```

</details>

#### 4. Exercise: Configurable Range Predicate

Problem Statement: Create a function `make_predicate` that accepts a `min_val` and a `max_val`. It should return a predicate function—a function that returns a boolean. The returned predicate should take a single number and return True if the number is between `min_val` and m`ax_val` (inclusive), and False otherwise.

Function Signature: ```def make_predicate(min_val, max_val):```

The function must:

* Accept two numeric arguments, `min_val` and `max_val`.
* Return a new predicate function.
* The returned function must accept a single numeric argument num and return True if min_val <= num <= max_val, otherwise False.

Asserts:

```python
is_child = make_predicate(0, 12)
is_teenager = make_predicate(13, 19)
is_adult = make_predicate(20, 120)

assert is_child(5) is True
assert is_child(13) is False
assert is_teenager(15) is True
assert is_teenager(20) is False
assert is_adult(19) is False
assert is_adult(65) is True
```

<details> 
<summary>Possible Solution</summary> 

```python

def make_predicate(min_val, max_val):

    def predicate(value):
        return max_val > value > min_val
    return predicate
```

</details>

#### 5. Exercise: Simple Counter

Problem Statement: Write a function `make_counter` that takes no arguments. It should return a new function that, when called, returns an integer that is one greater than the last time it was called. The first call should return 1.

Function Signature: ```def make_counter():```

The function must:

* Return a new function.
* The returned function, when called, should increment an internal counter and return the new value.
* The first call to the returned function should yield 1, the second 2, and so on.
* Each function created by make_counter must have its own independent count.

Asserts:

```python
counter_a = make_counter()
assert counter_a() == 1
assert counter_a() == 2
assert counter_a() == 3

counter_b = make_counter()
assert counter_b() == 1
assert counter_b() == 2

assert counter_a() == 4
```
<details> 
<summary>Possible Solution</summary> 

```python
def make_counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

</details>

#### 6. Exercise: Configurable Counter

Problem Statement: Modify the previous exercise. Write a function `make_configurable_counter` that takes a start integer. It should return a counter function that begins counting from start + 1.

Function Signature: ```def make_configurable_counter(start):```

The function must:

* Accept a single integer argument start.
* Return a new counter function.
* The first call to the returned function must return start + 1, the second start + 2, etc.
* Each counter instance must be independent.

Asserts:

```python
counter_10 = make_configurable_counter(10)
assert counter_10() == 11
assert counter_10() == 12

counter_100 = make_configurable_counter(100)
assert counter_100() == 101
assert counter_100() == 102
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_configurable_counter(start):

    count = start

    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

</details>

#### 7. Exercise: Accumulator

Problem Statement: Write a function `make_accumulator` that takes no arguments. It should return a function that accepts a number n. This function should add n to an internal total and return the new total. The initial total is 0.

Function Signature: ```def make_accumulator():```

The function must:

* Return a new accumulator function.
* The returned function must accept a single numeric argument n.
* It must update its internal total by adding n to it and return the new total.
* Each accumulator must have its own independent total.

Asserts:

```python
acc1 = make_accumulator()
assert acc1(10) == 10
assert acc1(5) == 15
assert acc1(-3) == 12

acc2 = make_accumulator()
assert acc2(100) == 100
assert acc2(50) == 150

assert acc1(20) == 32
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_accumulator():

    total = 0

    def accumulate(n):
        nonlocal total
        total += n
        return total
    
    return accumulate
```

</details>

#### 8. Exercise: Limited Use Password Checker

Problem Statement: Write a function `make_password_checker` that takes a password string and an integer max_attempts. It should return a function that takes a string guess. The returned function should return True if the guess matches the password. It should return False otherwise. After `max_attempts` have been used, the function should always return False, effectively locking out the user.

Function Signature: ```def make_password_checker(password, max_attempts):```

The function must:

* Accept a password string and an integer max_attempts.
* Return a new password-checking function.
* The returned function must accept a guess string.
* If the number of attempts is less than max_attempts and the guess is correct, it returns True.
* If the number of attempts is less than max_attempts and the guess is incorrect, it decrements the attempt counter and returns False.
* If the attempt counter reaches zero, all subsequent calls must return False.

Asserts:
```python
checker = make_password_checker("secret", 3)

assert checker("wrong") is False  # Attempt 1
assert checker("another wrong") is False # Attempt 2
assert checker("secret") is True # Correct, doesn't use an attempt
assert checker("wrong again") is False # Attempt 3, now locked
assert checker("secret") is False # Locked
assert checker("anything") is False # Locked
```
<details> 
<summary>Possible Solution</summary> 

```python

def make_password_checker(password, max_attempts):

    maxed_attempts = max_attempts

    def password_checker(guess):

        nonlocal maxed_attempts
        if maxed_attempts <= 0:
            return False
        if password == guess:
            return True

        maxed_attempts -= 1
        return False
    
    return password_checker
```

</details>

#### 9. Exercise: Value Validator

Problem Statement: Create a function `make_validator` that accepts a predicate function `is_valid` and an error_message string. It should return a new function that takes a value. If `is_valid(value)` returns True, the function should do nothing. If it returns False, it should raise a `ValueError` with the provided ` `.

Function Signature: ```def make_validator(is_valid, error_message):```

The function must:

* Accept a function `is_valid` and a string `error_message`.
* Return a new validation function.
* The returned function must accept a single argument value.
* If `is_valid(value)` is falsey, the function must raise a `ValueError` with the text `error_message`.
* If `is_valid(value)` is truthy, the function must return `None`.

Asserts:
```python
validate_positive = make_validator(lambda x: x > 0, "Value must be positive.")
validate_not_empty = make_validator(lambda s: len(s) > 0, "String cannot be empty.")

validate_positive(10) # Should not raise
validate_not_empty("hello") # Should not raise

try:
    validate_positive(-5)
except ValueError as e:
    assert str(e) == "Value must be positive."

try:
    validate_not_empty("")
except ValueError as e:
    assert str(e) == "String cannot be empty."
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_validator(is_valid, error_message):

    def validator(value):

        if is_valid(value):
            return None
        else:
            raise ValueError(error_message)
        
    return validator
```

</details>

#### 10. Exercise: Transformation Pipeline

Problem Statement: Write a function `make_pipeline` that accepts a variable number of functions. It should return a new function that takes an initial value. The new function must apply each function from the pipeline in sequence to the value, with the output of one function becoming the input of the next.

Function Signature: ```def make_pipeline(*funcs):```

The function must:

* Accept any number of functions as arguments.
* Return a new pipeline function.
* The returned function must accept a single argument value.
* It must pass the value to the first function, its result to the second, and so on, returning the final result.

Asserts:
```python
def add_one(x): return x + 1
def double(x): return x * 2
def to_string(x): return str(x)

pipeline = make_pipeline(add_one, double, to_string)
assert pipeline(5) == "12"

pipeline2 = make_pipeline(to_string, len)
assert pipeline2(12345) == 5
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_pipeline(*funcs):

    def pipeline(value):
        
        current_value = value
        for func in funcs:
            current_value = func(current_value)
        return current_value
    
    return pipeline

```

</details>

#### 11. Exercise: Safe Division

Problem Statement: Create a function `make_safe_division` that accepts a `default_value`. It should return a function that takes two numbers, numerator and denominator. The returned function should perform the division `numerator / denominator`. If a `ZeroDivisionError` occurs, it must catch the error and return the `default_value` instead.

Function Signature: ```def make_safe_division(default_value):```

The function must:

* Accept one argument, `default_value`.
* Return a new function for safe division.
* The returned function must accept two numeric arguments, numerator and denominator.
* It must return the result of `numerator / denominator`.
* If denominator is zero, it must return `default_value`.

Asserts:

```python
safe_div_inf = make_safe_division(float('inf'))
assert safe_div_inf(10, 2) == 5.0
assert safe_div_inf(10, 0) == float('inf')

safe_div_none = make_safe_division(None)
assert safe_div_none(20, 4) == 5.0
assert safe_div_none(20, 0) is None
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_safe_division(default_value):

    def safe_division(numerator, denominator):
        try:
            result = numerator / denominator
        except ZeroDivisionError:
            return default_value
        return result     
    
    return safe_division
```

</details>

#### 12. Exercise: Command Dispatcher

Problem Statement: Write a function `make_dispatcher` that accepts a dictionary handlers. The keys of this dictionary are command strings, and the values are functions. It should return a function that accepts a command string and a variable number of arguments. The returned function should find the handler function associated with the command and call it with the provided arguments, returning its result. If the command is not found, it should raise a KeyError.

Function Signature: ```def make_dispatcher(handlers):```

The function must:

* Accept a dictionary handlers mapping command strings to functions.
* Return a new dispatch function.
* The returned function must accept a command string as its first argument, followed by any number of positional arguments.
* It must execute the corresponding function from handlers with the provided arguments.
* If the command is not in handlers, it must raise a `KeyError`.

Asserts:
```python
def add(a, b): return a + b
def subtract(a, b): return a - b
def greet(name): return f"Hello, {name}!"

handlers = {"add": add, "subtract": subtract, "greet": greet}
dispatcher = make_dispatcher(handlers)

assert dispatcher("add", 5, 3) == 8
assert dispatcher("subtract", 10, 4) == 6
assert dispatcher("greet", "World") == "Hello, World!"

try:
    dispatcher("multiply", 2, 3)
except KeyError:
    assert True
else:
    assert False, "KeyError not raised for unknown command"
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_dispatcher(handlers):
    
    def dispatcher(command_string, *args):

        if command_string in handlers:
            return handlers[command_string](*args)

        else:
            raise KeyError
        
    return dispatcher
```

</details>

####  13. Exercise: Predict the Output

Problem Statement: Without running the code, predict what the following program will print.

```python
def make_manager(name):
    tasks = []
    def add_task(task):
        tasks.append(task)
        print(f"{name}'s team is now working on: {tasks}")
    return add_task

manager1 = make_manager("Alice")
manager2 = make_manager("Bob")

manager1("Design the UI")
manager2("Implement the API")
manager1("Test the UI")
```

Write down the expected output line by line.

The answer must:

* Analyze how the tasks list is captured by each closure.
* Determine if the closures for manager1 and manager2 share state.
* Predict the exact output from the three print statements.

<details> 
<summary>Possible Solution</summary> 

Prints out: 
```
Alice's team is now working on: []
Bob's team is now working on: []
Alice's team is now working on: []
```
The code doesn't append anything to the list. If it did it would print out:

```
Alice's team is now working on: ['Design the UI']
Bob's team is now working on: ['Implement the API']
Alice's team is now working on: ['Design the UI', 'Test the UI']
```

</details>

#### 14. Exercise: Debug the Broken Counter

Problem Statement: The following code for a counter factory is broken. When `counter()` is called, it raises an` UnboundLocalError`. Identify the bug and write a corrected version of the `make_broken_counter` function named `make_fixed_counter`.

```python
# Broken version
def make_broken_counter():
    count = 0
    def counter():
        count = count + 1
        return count
    return counter
```

Function Signature: ```def make_fixed_counter():```

The function must:

* Return a counter function that correctly increments a captured variable count on each call.
* The first call to the returned function must return 1.
* The fix must involve a single keyword addition to the counter function.

Asserts:
```python
fixed_counter = make_fixed_counter()
assert fixed_counter() == 1
assert fixed_counter() == 2
assert fixed_counter() == 3
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_fixed_counter():

    count = 0
    
    def counter():
        nonlocal count
        count = count + 1
        return count
    return counter
```

</details>

#### 15. Exercise: Predict Late Binding Behavior

Problem Statement: Without running the code, predict what the following program will print.

```python
def create_functions():
    funcs = []
    for i in [1, 2, 3]:
        funcs.append(lambda: i * 10)
    return funcs

multipliers = create_functions()

for f in multipliers:
    print(f())
```
The answer must:

* Analyze how the loop variable i is captured by the lambda functions.
* Understand the concept of "late binding" in Python closures.
* Predict the output of the final loop.

<details> 
<summary>Possible Solution</summary> 

Prints out:
```
30
30
30
```

To fix it, you would need: ```funcs.append(lambda i = i: i * 10)```

</details>

#### 16. Exercise: Configurable Event Logger

Problem Statement: You are building a logging system. You need a way to create specialized logging functions. Write a function `create_event_logger` that takes a string log_level (e.g., "INFO", "WARNING"). This function should return a new function that accepts a message string and returns a formatted log entry: `"[LOG_LEVEL]: message".`

Function Signature: `def create_event_logger():`

The function must:

* Be named `create_event_logger` and accept a log_level string.
* Return a new function.
* The returned function must accept a message string.
* The returned function must produce a string in the format `f"[{log_level}]: {message}".`

Asserts:
```python
info_logger = create_event_logger("INFO")
warning_logger = create_event_logger("WARNING")
error_logger = create_event_logger("ERROR")

assert info_logger("User logged in.") == "[INFO]: User logged in."
assert warning_logger("Disk space is low.") == "[WARNING]: Disk space is low."
assert error_logger("Failed to connect to database.") == "[ERROR]: Failed to connect to database."
```

<details> 
<summary>Possible Solution</summary> 

```python
def create_event_logger(log_level):
    
    def event_logger(message):
        return (f"[{log_level}]: {message}")
        
    return event_logger
```

</details>

#### 17. Exercise: Sequenced ID Generator*

Problem Statement: You need to generate unique, sequential IDs for different types of documents (e.g., invoices, tickets, reports). Write a function `create_id_generator` that takes a prefix string. It should return a new function that, each time it's called, returns a new ID string. The first ID should be `f"{prefix}-001"`, the second `f"{prefix}-002"`, and so on. The numeric part should always be three digits, zero-padded.

Function Signature: `def create_id_generator(prefix_string):`

The function must:

* Be named `create_id_generator` and accept a prefix string.
* Return a new ID-generating function.
* The returned function takes no arguments.
* Each call to the returned function must produce a new ID with an incrementing number, formatted to three digits with leading zeros.
* Generators for different prefixes must be independent.

Asserts:
```python
invoice_generator = create_id_generator("INV")
ticket_generator = create_id_generator("TKT")

assert invoice_generator() == "INV-001"
assert invoice_generator() == "INV-002"
assert ticket_generator() == "TKT-001"
assert invoice_generator() == "INV-003"
assert ticket_generator() == "TKT-002"
```

<details> 
<summary>Possible Solution</summary> 

```python
def create_id_generator(prefix_string):

    count = 1

    def id_generator():
        
        nonlocal count
        output_str = f"{prefix_string}-{count:03}"
        count += 1
        return output_str
    
    return id_generator
```

</details>

#### 18. Exercise: Data Processing Builder

Problem Statement: In a data processing application, you often apply a series of transformations to an input. Write a function build_data_processor that accepts one or more functions as arguments. It should return a single function that, when given a piece of data, will apply all the transformation functions to it in the order they were provided.

Function Signature: `def build_data_processor(*args):`

The function must:

* Be named `build_data_processor` and accept a variable number of functions.
* Return a new processor function.
* The returned function must accept a single argument data.
* It must apply the series of transformations to data and return the final result.

Asserts:

```python
def clean_whitespace(s): return s.strip()
def to_uppercase(s): return s.upper()
def add_greeting(s): return f"HELLO, {s}!"

name_processor = build_data_processor(clean_whitespace, to_uppercase, add_greeting)
assert name_processor("  alice  ") == "HELLO, ALICE!"

def parse_int(s): return int(s)
def double(n): return n * 2
number_processor = build_data_processor(clean_whitespace, parse_int, double)
assert number_processor("  10  ") == 20
```

<details> 
<summary>Possible Solution</summary> 

```python
def build_data_processor(*args):

    def data_processor(value):
        current_value = value
        for func in args:
            current_value = func(current_value)
        return current_value
    return data_processor
```

</details>

#### 19. Exercise: Access Control Handler

Problem Statement: You are implementing a security system. You need a way to check if a user has the required permissions. Write a function `create_access_handler `that accepts a set of `allowed_roles`. It must return a new function that takes a user dictionary. The user dictionary will have a 'role' key. The returned function should return True if the user's role is in the set of allowed roles, and False otherwise.

Function Signature: `def create_access_handler(allowed_roles):`

The function must:

* Be named `create_access_handler` and accept a set of strings (`allowed_roles`).
* Return a new handler function.
* The returned function must accept a single dictionary user.
* It must return True if `user['role']` is present in the `allowed_roles` set, and False otherwise.

Asserts:

```python
admin_handler = create_access_handler({"admin"})
editor_handler = create_access_handler({"admin", "editor"})
viewer_handler = create_access_handler({"admin", "editor", "viewer"})

user_admin = {"name": "Alice", "role": "admin"}
user_editor = {"name": "Bob", "role": "editor"}
user_viewer = {"name": "Charlie", "role": "viewer"}

assert admin_handler(user_admin) is True
assert admin_handler(user_editor) is False

assert editor_handler(user_admin) is True
assert editor_handler(user_editor) is True
assert editor_handler(user_viewer) is False

assert viewer_handler(user_viewer) is True
```
<details> 
<summary>Possible Solution</summary> 

```python

def create_access_handler(allowed_roles):

    def access_handler(user_dict):
        if user_dict['role'] in allowed_roles:
            return True
        return False
    return access_handler
```
</details>

[Back to the top](#top)


### Closure Practice 2

#### Exercise 1, Configurable Prefixer

Problem Statement​: Create a higher-order function make_prefixer that takes a string prefix and returns a new function. The returned function should take a single string argument and prepend the original prefix to it.

Function Signature​: ```def make_prefixer(prefix):```

Contract​:

* The function must accept one argument, prefix, which is a string.
* The function must return a new function (a closure).
* The returned function must accept one argument, text, which is a string.
* The returned function must return a new string that consists of prefix followed by text.

Tests​:

```python
add_mr = make_prefixer("Mr. ")
add_ms = make_prefixer("Ms. ")

assert add_mr("Smith") == "Mr. Smith"
assert add_mr("Jones") == "Mr. Jones"
assert add_ms("Williams") == "Ms. Williams"
assert make_prefixer("")("Test") == "Test"
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_prefixer(prefix):

    def prefixer(string):
        return f"{prefix}{string}"
    return prefixer
```

</details>

#### Exercise 2, Simple Stateful Counter

Problem Statement​: Write a function `make_counter` that takes no arguments and returns a counter function. Each time the returned function is called, it should return a number that is one greater than the value returned by the previous call. The first call should return 1.

Function Signature​: ```def make_counter():```

Contract​:

* The function must accept no arguments.
* The function must return a new function (a closure).
* The returned function, when called, must return an integer.
* The first call to the returned function must return 1.
* Each subsequent call must return the previous result plus 1.

Tests​:

```python
counter1 = make_counter()
assert counter1() == 1
assert counter1() == 2
assert counter1() == 3

# Verify that a new counter has independent state
counter2 = make_counter()
assert counter2() == 1
assert counter1() == 4
assert counter2() == 2
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter
```

</details>

#### Exercise 3, Tracing Closure State

Problem Statement​: Without running the code, determine what the following script will print.

Code​:

```python
def make_cumulative_adder(base):
    total = base
    def cumulative_adder(x):
        nonlocal total
        total += x
        return total
    return cumulative_adder

adder_plus_5 = make_cumulative_adder(5)
print(f"First call to adder_plus_5: {adder_plus_5(10)}")
print(f"Second call to adder_plus_5: {adder_plus_5(2)}")

adder_plus_10 = make_cumulative_adder(10)
print(f"First call to adder_plus_10: {adder_plus_10(100)}")

print(f"Third call to adder_plus_5: {adder_plus_5(3)}")
print(f"Second call to adder_plus_10: {adder_plus_10(1)}")
```

<details> 
<summary>Possible Solution</summary> 

```
First call to adder_plus_5: 15
Second call to adder_plus_5: 17
First call to adder_plus_10: 110
Third call to adder_plus_5: 20
Second call to adder_plus_10: 111
```

</details>

#### Exercise 4, Event Logger with Mutable State

Problem Statement​: Implement a function `make_event_logger` that returns a logging function. The returned logger should behave in two ways:

1. When called with a string argument, it should record that string as an event and return `None`.
2. When called with the special sentinel value `'GET_EVENTS'`, it should return a ​copy​ of the list of all events logged so far, in the order they were recorded.

Function Signature​: ```def make_event_logger():```

Contract​:

* The function must accept no arguments.
* The function must return a new function (a closure).
* The returned function, when called with a string, must store the string and return None.
* The returned function, when called with the string `'GET_EVENTS'`, must return a new list containing all previously logged event strings.
* Modifying the list returned by a `'GET_EVENTS'` call must not affect subsequent calls.

Tests​:
``` python
logger1 = make_event_logger()
assert logger1("User logged in") is None
assert logger1("User viewed page") is None

events = logger1("GET_EVENTS")
assert events == ["User logged in", "User viewed page"]

# Verify that the returned list is a copy
events.append("Tampering with events")
assert logger1("GET_EVENTS") == ["User logged in", "User viewed page"]

assert logger1("User logged out") is None
assert logger1("GET_EVENTS") == ["User logged in", "User viewed page", "User logged out"]

# Verify independent state for a new logger
logger2 = make_event_logger()
assert logger2("Admin action") is None
assert logger2("GET_EVENTS") == ["Admin action"]
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_event_logger():
    events = []

    def event_logger(string):
        nonlocal events
        if string == "GET_EVENTS":
            results = events.copy()
            return results
        else:
            events.append(string)
    
    return event_logger
```

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 5, Shared State Wallet

Problem Statement​: Create a function `make_wallet` that simulates a simple wallet, starting with an `initial_balance`. It must return a dictionary containing three functions: deposit, withdraw, and balance. These three functions should all share access to the same enclosed balance.

Function Signature​: ```def make_wallet(initial_balance):```

Contract​:

* The function must accept one argument, initial_balance.
* The function must return a dictionary with keys 'deposit', 'withdraw', and 'balance'.
* The deposit function must accept an amount, add it to the balance, and return the new balance.
* The withdraw function must accept an amount. If there are sufficient funds, it should subtract the amount and return the new balance. If not, it should return the string "Insufficient funds".
* The balance function must accept no arguments and return the current balance.

Tests​:

```python
my_wallet = make_wallet(100)
deposit = my_wallet['deposit']
withdraw = my_wallet['withdraw']
get_balance = my_wallet['balance']

assert get_balance() == 100
assert deposit(50) == 150
assert get_balance() == 150
assert withdraw(30) == 120
assert withdraw(150) == "Insufficient funds"
assert get_balance() == 120

# Verify independent wallets
other_wallet = make_wallet(10)
assert other_wallet['balance']() == 10
assert get_balance() == 120
```
<details> 
<summary>Possible Solution</summary> 

```python
def make_wallet(initial_balance):

    current_balance = initial_balance

    def deposit(amount):
        nonlocal current_balance
        current_balance += amount
        return current_balance 
    
    def withdraw(amount):
        nonlocal current_balance
        if amount > current_balance:
            return "Insufficient funds"
        current_balance -= amount
        return current_balance
    
    def balance():
        nonlocal current_balance
        return current_balance

    return {'balance': balance, 'withdraw': withdraw, 'deposit': deposit}
```

</details>

#### Exercise 6, Function Call Limiter

Problem Statement​: Write a higher-order function `make_call_limiter` that takes a function `target_func` and an integer limit. It should return a new function that acts as a wrapper. The wrapper can be called up to limit times, and on each of these calls, it should invoke target_func with the given arguments and return its result. On any subsequent call, the wrapper should raise a ValueError with the message "Call limit reached".

Function Signature​: ```def make_call_limiter(target_func, limit):```

Contract​:

* The function must accept a callable `target_func` and an integer limit.
* The function must return a new function (a closure).
* The returned function must accept any positional and keyword arguments (*args, **kwargs).
* When called limit or fewer times, the returned function must call `target_func` with the provided arguments and return its value.
* When called more than limit times, the returned function must raise a `ValueError`.

Tests​:

```python
def add(a, b):
    return a + b

limited_add = make_call_limiter(add, 2)
assert limited_add(3, 4) == 7
assert limited_add(5, 6) == 11

raised_error = False
try:
    limited_add(7, 8)
except ValueError as e:
    raised_error = True
    assert str(e) == "Call limit reached"
assert raised_error
```

<details> 
<summary>Possible Solution</summary> 

```python

def make_call_limiter(target_func, limit):

    current = limit

    def call_limiter(*args, **kwargs):
        nonlocal current
        if current > 0:
            current -= 1
            return target_func(*args, **kwargs)
        raise ValueError("Call limit reached")
    
    return call_limiter
```

</details>

#### Exercise 7, Stateful Toggle

Problem Statement​: Write a function `make_toggle` that accepts two values, `val1` and `val2`. It should return a function that, when called, alternates between returning `val1` and `val2`. The first call should return `val1`.

Function Signature​: ```def make_toggle(val1, val2):```

Contract​:

* The function must accept two arguments, `val1` and `val2`.
* The function must return a new function (a closure).
* The first call to the returned function must return `val1`.
* The second call must return `val2`.
* The third call must return `val1`, and so on, alternating.

Tests​:

```python
toggler = make_toggle("On", "Off")
assert toggler() == "On"
assert toggler() == "Off"
assert toggler() == "On"
assert toggler() == "Off"

# Verify independent toggler
bool_toggler = make_toggle(True, False)
assert bool_toggler() is True
assert toggler() == "On"
assert bool_toggler() is False
```

<details> 
<summary>Possible Solution</summary> 

```python

def make_toggle(val1, val2):

    current_call = 0

    def toggle():

        nonlocal current_call

        if current_call % 2 == 0:
            current_call += 1
            return val1
        else:
            current_call += 1
            return val2

    return toggle
```

</details>

#### Exercise 8, Password-Protected Function Access

Problem Statement​: Write a function `protect_function` that secures a given function with a password. It should take a `target_func` and a password string and return a new function. This new function requires the correct password as its ​first​ argument. If the password is correct, it will call the `target_func` with any ​remaining​ arguments and return its result. If the password is incorrect, it must return the string "Invalid password".

Function Signature​: ```def protect_function(target_func, password):```

Contract​:

* The function must accept a callable `target_func` and a string password.
* The function must return a new function (a closure).
* The returned function must accept at least one argument (the trial password), plus any arguments intended for `target_func`.
* If the first argument to the returned function matches the original password, it must call `target_func` with the rest of the arguments.
* If the first argument does not match, it must return the specific string "Invalid password".

Tests​:
```python
def get_secret_data(key):
    return f"Secret data for key: {key}"

protected_access = protect_function(get_secret_data, "s3cr3t")

assert protected_access("wrong_pass", 123) == "Invalid password"
assert protected_access("s3cr3t", 123) == "Secret data for key: 123"

def multiply(a, b, c):
    return a * b * c

protected_multiply = protect_function(multiply, "math_wiz")
assert protected_multiply("s3cr3t", 2, 3, 4) == "Invalid password"
assert protected_multiply("math_wiz", 2, 3, 4) == 24
```

<details> 
<summary>Possible Solution</summary> 

```python

def protect_function(target_func, password):

    def inner(attempt, *args):
        if password == attempt:
            return target_func(*args)
        else:
            return "Invalid password"
    return inner
```

</details>

#### Exercise 9, Debugging Late Binding

Problem Statement​: The function `create_multipliers` is intended to create a list of functions. Each function in the list should multiply its argument by its corresponding index in the list (0, 1, 2, 3, 4). However, it has a bug. All the functions in the returned list behave identically. Analyze the code, identify the bug related to closures and variable scope, and describe why it happens. Do not provide the corrected code.


Code​:
```python
def create_multipliers():
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)
    return multipliers

multipliers = create_multipliers()

# The functions are expected to behave as follows:
# multipliers[0](10) should be 0
# multipliers[1](10) should be 10
# ...
# multipliers[4](10) should be 40

# However, the actual output is:
print("Expected: 0, Actual:", multipliers[0](10))
print("Expected: 10, Actual:", multipliers[1](10))
print("Expected: 20, Actual:", multipliers[2](10))
print("Expected: 30, Actual:", multipliers[3](10))
print("Expected: 40, Actual:", multipliers[4](10))
```

<details> 
<summary>Possible Solution</summary>

Late binding problem. The closures retain access to the same i binding, not a separate snapshot of i from each loop iteration.

Because you are curious, the fix is:

```python

def create_multipliers():
    multipliers = []
    for i in range(5):
        def multiplier(x, i=i):
            return i * x
        multipliers.append(multiplier)
    return multipliers
```

</details>

#### Exercise 10, Stateful Pipeline Builder

Problem Statement​: Create a function `make_pipeline_builder` that allows for the step-by-step construction of a data processing pipeline. The function should return a builder function. This builder can be called repeatedly with functions as arguments, adding each to the pipeline. If the builder is called with a non-callable argument (the "final value"), it should pass this value through the entire pipeline of stored functions in the order they were added and return the final result. After processing a final value, the pipeline should reset.

Function Signature​: ```def make_pipeline_builder():```

Contract​:

* The function must accept no arguments.
* The function must return a new function, builder.
* When builder is called with a callable (a function), it must add that function to its internal pipeline and return None.
* When builder is called with a non-callable value, it must process that value through the pipeline.
* The processing must apply the first function in the pipeline to the value, then the second function to that result, and so on.
* After processing and returning the final result, the internal pipeline must be cleared.

Tests​:
```python
def add_one(n): return n + 1
def double(n): return n * 2
def to_string(n): return str(n)

builder = make_pipeline_builder()

assert builder(add_one) is None
assert builder(double) is None
assert builder(to_string) is None

# The pipeline is add_one -> double -> to_string
# For input 5: (5 + 1) -> 6 * 2 -> 12 -> "12"
assert builder(5) == "12"

# The pipeline should now be reset
assert builder(double) is None
assert builder(add_one) is None

# New pipeline is double -> add_one
# For input 10: 10 * 2 -> 20 + 1 -> 21
assert builder(10) == 21
```

<details> 
<summary>Possible Solution</summary> 

```python
def make_pipeline_builder():

    pipeline = []

    def builder(item):
        if callable(item):
            pipeline.append(item)
            return None

        current_value = item

        for func in pipeline:
            current_value = func(current_value)

        pipeline.clear()
        return current_value
    
    return builder
```

</details>


[Back to the top](#top)

### Decorator Practice 1

#### Exercise 1: Manual Decoration​

Difficulty:​ Basic

Problem Statement: You are given a decorator simple_printer and a function add_numbers. Instead of using the @ syntax, write the single line of code required to manually apply the decorator to the function. Your code should rebind the name add_numbers to point to the new decorated function.

Provided Code
```python
def simple_printer(func):
    """A simple decorator that prints a message before calling the function."""
    def wrapper(*args, **kwargs):
        print("Calling the function...")
        return func(*args, **kwargs)
    return wrapper

def add_numbers(a, b):
    """This function adds two numbers."""
    print(f"Executing add_numbers({a}, {b})")
    return a + b

# Your code here: Manually decorate add_numbers with simple_printer
# add_numbers = ...

# --- Tests ---
# The following code should run without modification after you add your line above.
result = add_numbers(5, 10)
print(f"Result: {result}")

# Expected output:
# Calling the function...
# Executing add_numbers(5, 10)
# Result: 15
```

<details> 
<summary>Possible Solution</summary> 

```python

add_numbers = simple_printer(add_numbers)

```
</details>


#### Exercise 2: Creating a Simple Wrapper​

Difficulty:​ Basic

Problem Statement: Write a decorator named `announce_call` that prints "About to run the function..." right before the decorated function is executed and "Done running the function." right after. The decorated function will not take any arguments or return any value.

Function Signature: ```def announce_call(func):```

Contract

* When a function decorated with announce_call is called, it must first print "About to run the function...".
* It must then execute the original function.
* Finally, it must print "Done running the function.".

Tests
```python
# Your decorator implementation here

@announce_call
def say_hello():
    print("Hello, world!")

# This call should produce the three lines of output in the correct order.
say_hello()

# Expected output:
# About to run the function...
# Hello, world!
# Done running the function.
```

<details> 
<summary>Possible Solution</summary> 

```python

def announce_call(func):
    def wrapper(*args, **kwargs):
        print("About to run the function...")
        result = func(*args, **kwargs)
        print("Done running the function.")
        return result
    return wrapper

```
</details>

#### ​Exercise 3: Forwarding Arguments and Return Values​

Difficulty:​ Intermediate

Problem Statement: Create a decorator called passthrough that does nothing but execute the decorated function. It must correctly handle any positional and keyword arguments passed to the decorated function, and it must return the decorated function's exact return value.

Function Signature: ``` def passthrough(func):```

Contract

* The decorator must accept a function as its argument and return a new function.
* The new function must accept any combination of positional and keyword arguments.
* The new function must call the original function, passing along all arguments it received.
* The new function must return the exact value that the original function returned.

Tests
```python
# Your decorator implementation here

@passthrough
def multiply(a, b, verbose=False):
    if verbose:
        print(f"Multiplying {a} and {b}")
    return a * b

# Test 1: Positional arguments
result1 = multiply(3, 5)
print(f"Test 1 Result: {result1}")
assert result1 == 15

# Test 2: Keyword arguments
result2 = multiply(a=4, b=10, verbose=True)
print(f"Test 2 Result: {result2}")
assert result2 == 40

# Test 3: Mixed arguments
result3 = multiply(6, verbose=True, b=7)
print(f"Test 3 Result: {result3}")
assert result3 == 42
```

<details> 
<summary>Possible Solution</summary> 

```python
def passthrough (func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
</details>

#### Exercise 4: Decoration Time vs. Invocation Time​

Difficulty:​ Intermediate

Problem Statement: Consider the following code. Without running it, predict the exact output. Then, provide a brief explanation for why the "Decorator is setting up" message appears only once, while the "Wrapper is executing" message appears each time the function is called.

Code to Analyze
```python
def execution_tracer(func):
    print(f"Decorator is setting up for '{func.__name__}'")
    def wrapper(*args, **kwargs):
        print("Wrapper is executing...")
        result = func(*args, **kwargs)
        print("...wrapper has finished.")
        return result
    return wrapper

@execution_tracer
def calculate_sum(x, y):
    return x + y

print("--- Making the first call ---")
calculate_sum(2, 3)

print("\n--- Making the second call ---")
calculate_sum(10, 20)
```
Question

1.  What will be the exact, line-by-line output of this script?
2.  Explain the difference between code that runs at decoration time and code that runs at invocation time, using the print statements in `execution_tracer` as your example.

<details> 
<summary>Possible Solution</summary> 

--- Making the first call ---
Wrapper is executing...
...wrapper has finished.

--- Making the second call ---
Wrapper is executing...
...wrapper has finished.

</details>

#### Exercise 5: Debugging a Return Value​

Difficulty:​ Intermediate

Problem Statement: The `log_return` decorator is intended to print the return value of the function it decorates before returning it. However, it has a bug. When you run the test code, it fails with an `AssertionError` because the result is `None` instead of the expected integer 12.

Identify the bug in the `log_return` decorator and fix it.

Buggy Code
```python
def log_return(func):
    def wrapper(*args, **kwargs):
        # This wrapper has a bug
        value = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {value}")
    return wrapper

@log_return
def get_product(x, y):
    return x * y

# --- Tests ---
result = get_product(3, 4)

print(f"Final result received: {result}")
assert result == 12, f"Test failed: expected 12, but got {result}"
print("Test passed!")
```

<details> 
<summary>Possible Solution</summary> 

```python

def log_return(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {value}")
        return value
    return wrapper

```
</details>

#### Exercise 6: Argument Validation Decorator​*

Difficulty:​ Advanced

Problem Statement:  Write a decorator named `validate_string_args` that ensures all positional arguments passed to the decorated function are strings. If any positional argument is not a string, the decorator should raise a `TypeError` with the message "All arguments must be strings.". If all arguments are valid, it should execute the function normally.

Function Signature: ```def validate_string_args(func):```

Contract

* The decorator's wrapper must inspect all positional arguments (*args).
* If any positional argument is not of type str, the wrapper must raise a `TypeError`.
* The decorator should not validate keyword arguments.
* If all positional arguments are strings, the wrapper must call the original function with all its arguments (*args, **kwargs) and return its result.

Tests
```python

# Your decorator implementation here

@validate_string_args
def concatenate(*args, separator=" "):
    return separator.join(args)

# Test 1: Should pass
result = concatenate("hello", "world", "from", "python")
assert result == "hello world from python"
print("Test 1 passed.")

# Test 2: Should pass with keyword argument
result_sep = concatenate("a", "b", "c", separator="-")
assert result_sep == "a-b-c"
print("Test 2 passed.")

# Test 3: Should raise TypeError
try:
    concatenate("this", "is", "a", 10, "test")
except TypeError as e:
    assert str(e) == "All arguments must be strings."
    print("Test 3 passed (caught expected error).")

# Test 4: Should raise TypeError
try:
    concatenate(True)
except TypeError as e:
    assert str(e) == "All arguments must be strings."
    print("Test 4 passed (caught expected error).")
```

<details> 
<summary>Possible Solution</summary> 

```python

def validate_string_args(func):

    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("All arguments must be strings.")
        return func(*args, **kwargs)
    return wrapper

```
</details>

#### Exercise 7: Synthesizing an Exception Handler​

Difficulty:​ Advanced

Problem Statement: Create a decorator named `handle_zero_division` that wraps a function. If the wrapped function raises a `ZeroDivisionError`, the decorator should catch the error and return the string "Cannot divide by zero.". For any other exception, the decorator should let it propagate. If no error occurs, it should return the function's normal result.

Function Signature: ```def handle_zero_division(func):```

Contract

* If the decorated function executes successfully, the decorator must return its result.
* If the decorated function raises a ZeroDivisionError, the decorator must return the specific string "Cannot divide by zero.".
* If the decorated function raises any other type of exception (e.g., TypeError), the decorator must not catch it.

Tests
```python
# Your decorator implementation here

@handle_zero_division
def divide(a, b):
    print(f"Dividing {a} by {b}...")
    return a / b

# Test 1: No error
result1 = divide(10, 2)
print(f"Result 1: {result1}")
assert result1 == 5.0

# Test 2: ZeroDivisionError
result2 = divide(8, 0)
print(f"Result 2: {result2}")
assert result2 == "Cannot divide by zero."

# Test 3: Other error (should raise TypeError)
try:
    divide(10, "2")
except TypeError:
    print("Successfully caught expected TypeError.")
except Exception as e:
    print(f"Caught unexpected exception: {type(e).__name__}")
 ```

 <details> 
<summary>Possible Solution</summary> 

```python

def handle_zero_division(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Cannot divide by zero."
    return wrapper

```
</details>

[Back to the top](#top)

### Decorator Practice 2

#### 1.Factory Mechanics: prefix_with​

Problem Statement: Create a decorator factory named `prefix_with`. The factory should accept a string `prefix_str`. The decorator it returns should prepend `"{prefix_str}: "` to the result of the decorated function. The decorated function will always return a string.

Function Signature: ```def prefix_with(prefix_str):```

Tests
```python
# Test Case 1: Simple prefixing
@prefix_with("LOG")
def get_message(message):
    return message

print(get_message("Hello, world!"))
# Expected: LOG: Hello, world!

# Test Case 2: Using a different prefix
@prefix_with("INFO")
def get_status(status):
    return f"Current status is {status}"

print(get_status("active"))
# Expected: INFO: Current status is active

# Test Case 3: Decorating a function with no arguments
@prefix_with("ALERT")
def system_warning():
    return "System integrity compromised"

print(system_warning())
# Expected: ALERT: System integrity compromised
```

<details> 
<summary>Possible Solution</summary> 

```python

def prefix_with(prefix_str):
    def decorator(func):
        def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                final = f"{prefix_str} {result}"
                return final
        return wrapper
    return decorator

```
</details>

#### 2. Scalar State and Rebinding: alternate_calls​

Problem Statement:  Implement a decorator `alternate_calls`. This decorator takes two functions, `func1` and `func2`, as arguments. When the decorated function is called, it should execute `func1` on the first call, `func2` on the second call, `func1` again on the third, and so on, alternating between the two. The decorated function will be called with arguments that are valid for both `func1` and `func2`.

Function Signature:  ```def alternate_calls(func1, func2):```

Tests
```python
def uppercase_string(s):
    return s.upper()

def lowercase_string(s):
    return s.lower()

@alternate_calls(uppercase_string, lowercase_string)
def transform_string(s):
    # This function's body is effectively replaced by the decorator
    pass

# Test the alternating behavior
print(transform_string("First Call"))  # Executes uppercase_string
# Expected: FIRST CALL

print(transform_string("Second Call")) # Executes lowercase_string
# Expected: second call

print(transform_string("Third Call"))  # Executes uppercase_string
# Expected: THIRD CALL

print(transform_string("Fourth Call")) # Executes lowercase_string
# Expected: fourth call
```

<details> 
<summary>Possible Solution</summary> 

```python

def alternate_calls(func1, func2):

    def decorator(func):

        current_call = 0
    
        def wrapper(*args, **kwargs):
            nonlocal current_call
            if current_call % 2 == 0:
                current_call += 1
                return func1(*args, **kwargs)
            else:
                current_call += 1
                return func2(*args, **kwargs)
        return wrapper
    return decorator


```
</details>

#### 3. Mutable State: record_invocations​

Problem Statement: Write a decorator factory `record_invocations`. The factory accepts a dictionary, `record`. The returned decorator should, upon each call to the decorated function, add an entry to `record`. The key should be the decorated function's name (as a string), and the value should be a list of all positional arguments it has been called with so far.

Function Signature:  ```def record_invocations(record):```
    
Tests
```python
call_log = {}

@record_invocations(call_log)
def greet(name):
    print(f"Hello, {name}!")

@record_invocations(call_log)
def farewell(name):
    print(f"Goodbye, {name}.")

greet("Alice")
# Expected print: Hello, Alice!
print(call_log)
# Expected: {'greet': [('Alice',)]}

farewell("Bob")
# Expected print: Goodbye, Bob.
print(call_log)
# Expected: {'greet': [('Alice',)], 'farewell': [('Bob',)]}

greet("Charlie")
# Expected print: Hello, Charlie!
print(call_log)
# Expected: {'greet': [('Alice',), ('Charlie',)], 'farewell': [('Bob',)]}
```

<details> 
<summary>Possible Solution</summary> 

```python
def record_invocations(record):

    def decorator(func):
        def wrapper(*args, **kwargs):
            if func.__name__ not in record:
                record[func.__name__] = []
            record[func.__name__].append(args)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

</details>

#### ​4. Independent State: create_saturating_counter​

Problem Statement: Create a decorator factory `create_saturating_counter` that takes a limit integer. The returned decorator should wrap a function. Each time the decorated function is called, an internal counter is incremented. The decorator should allow the original function to execute only if the counter is less than limit. Once the limit is reached, subsequent calls to the decorated function should do nothing and return None.

Each function decorated by a call to `create_saturating_counter` must have its own independent counter.

Function Signature: ```def create_saturating_counter(limit):```

Tests
```python
@create_saturating_counter(2)
def process_data(data):
    print(f"Processing: {data}")

@create_saturating_counter(3)
def log_event(event):
    print(f"Logging: {event}")

# Test first counter
print("--- Testing process_data (limit 2) ---")
process_data("A") # Processes
# Expected: Processing: A
process_data("B") # Processes
# Expected: Processing: B
process_data("C") # Does not process, returns None
# Expected: (no output)
process_data("D") # Does not process, returns None
# Expected: (no output)

# Test second counter, which should be independent
print("\n--- Testing log_event (limit 3) ---")
log_event("Start")     # Logs
# Expected: Logging: Start
log_event("Progress")  # Logs
# Expected: Logging: Progress
log_event("End")       # Logs
# Expected: Logging: End
log_event("Finished")  # Does not log, returns None
# Expected: (no output)
```

<details> 
<summary>Possible Solution</summary> 

```python
def create_saturating_counter(limit):

    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count 
            if count < limit:
                count += 1
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator
```

</details>

#### 5. Shared State: shared_flag​

Problem Statement: Implement a decorator factory `shared_flag` that accepts a mutable object (like a list or dictionary) to act as a shared state container. The factory returns a decorator. When the first function decorated by this decorator is called, it should set a "flag" within the shared state container and then execute. Any other function that shares this same decorator (i.e., was decorated using the same factory call) should refuse to run if the flag has already been set, returning `None` instead.

Function Signature: ```def shared_flag(state_container):```

Tests
```python
# The shared state container
flag_state = {}

# Both functions are decorated using the decorator from the SAME factory call
# so they will share the state.
flagged_decorator = shared_flag(flag_state)

@flagged_decorator
def critical_task_one():
    print("Executing critical task one.")
    return "Task One Complete"

@flagged_decorator
def critical_task_two():
    print("Executing critical task two.")
    return "Task Two Complete"


# Run the tasks
print(critical_task_one())
# Expected:
# Executing critical task one.
# Task One Complete

print(critical_task_two()) # Should not run as the flag is now set
# Expected:
# None

print(critical_task_one()) # Should also not run again
# Expected:
# None

print(f"Final state: {flag_state}")
# Expected: Final state: {'flag_set': True}
```

<details> 
<summary>Possible Solution</summary> 

```python
def shared_flag(state_container):
    shared_state_container = state_container
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not shared_state_container:
                shared_state_container["flag_set"] = True
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator
```

</details>

#### 6. State Ownership and Lifetime: Tracing​

Problem Statement:  Consider the following code. Trace the creation and sharing of state. Based on your trace, predict what the print statements at the end will output. Do not run the code before answering.

Code
```python
def create_event_logger():
    events = []
    def log_event_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            events.append(f"Function '{func.__name__}' returned '{result}'")
            return result
        return wrapper
    return log_event_decorator, lambda: list(events)

# Scenario 1: Two functions decorated by the same decorator instance
security_logger, get_security_events = create_event_logger()

@security_logger
def login_user(user):
    return f"{user} logged in"

@security_logger
def logout_user(user):
    return f"{user} logged out"

# Scenario 2: Two functions decorated by different decorator instances
database_logger, get_database_events = create_event_logger()

@database_logger
def query_db(query):
    return f"Queried: {query}"

general_logger, get_general_events = create_event_logger()

@general_logger
def read_file(path):
    return f"Read {path}"


# Execute function calls
login_user("admin")
query_db("SELECT *")
logout_user("admin")
read_file("/etc/passwd")
login_user("guest")

# Prediction questions
print("Security Events:", get_security_events())
print("Database Events:", get_database_events())
print("General Events:", get_general_events())
```

<details> 
<summary>Possible Solution</summary> 

```
Security Events: ["Function 'login_user' returned 'admin logged in'", "Function 'logout_user' returned 'admin logged out'", "Function 'login_user' returned 'guest logged in'"]
Database Events: ["Function 'query_db' returned 'Queried: SELECT *'"]
General Events: ["Function 'read_file' returned 'Read /etc/passwd'"]
```
</details>

#### 7. Synthesis: with_feedback​

Problem Statement:  Create a decorator factory `with_feedback` that accepts a list of `forbidden_results`. It returns a decorator that provides feedback on a function's return values. For each decorated function, the decorator must maintain its own independent state, consisting of:

1. A list of all results the function has ever returned.
2. A count of how many times its result was in the `forbidden_results` list.

The decorated function's behavior should be modified as follows:

* After the original function executes, the decorator checks if the return value is in `forbidden_results`.
* If it is, the forbidden count is incremented. The decorator then prints a warning: `"Warning: Forbidden result '{result}' encountered. Total forbidden calls: {count}."`
* Regardless of the result, it is added to the function's result history.
* Finally, the decorator returns the original result.

Function Signature: ```def with_feedback(forbidden_results):```

Tests
```python
forbidden = ["error", "failure", "unknown"]
feedback_decorator = with_feedback(forbidden)

@feedback_decorator
def process_job(job_id):
    if job_id % 3 == 0:
        return "error"
    elif job_id % 2 == 0:
        return "success"
    return "pending"

@feedback_decorator
def check_status(status_code):
    if status_code == 500:
        return "failure"
    return "ok"


print("--- Processing Jobs ---")
process_job(1) # pending
process_job(2) # success
process_job(3) # error
# Expected print: Warning: Forbidden result 'error' encountered. Total forbidden calls: 1.
process_job(4) # success
process_job(6) # error
# Expected print: Warning: Forbidden result 'error' encountered. Total forbidden calls: 2.

print("\n--- Checking Statuses ---")
check_status(200) # ok
check_status(500) # failure
# Expected print: Warning: Forbidden result 'failure' encountered. Total forbidden calls: 1.
check_status(404) # ok
```
<details> 
<summary>Possible Solution</summary> 

```python
def with_feedback(forbidden_results):
    def decorator(func):
        all_results = []
        forbidden_count = 0

        def wrapper(*args, **kwargs):
            nonlocal forbidden_count
            result = func(*args, **kwargs)
            all_results.append(result)
            if result in forbidden_results:
                forbidden_count += 1
                print(f"Warning: Forbidden result '{result}' encountered. Total forbidden calls: {forbidden_count}")
            return result
        return wrapper
    return decorator
```

</details>

[Back to the top](#top)


### Decorator Practice 3

#### Exercise 1

Write a decorator `count_calls` that maintains a single dictionary, `call_counts`. For each decorated function, it should increment a counter in call_counts using the function's name as the key.

```python
# Your implementation of count_calls and call_counts here

@count_calls
def greet(name):
    return f"Hello, {name}!"

@count_calls
def leave(name):
    return f"Goodbye, {name}!"

greet("Alice")
greet("Bob")
greet("Alice")
leave("Charlie")

assert call_counts == {'greet': 3, 'leave': 1}
```

<details> 
<summary>Possible Solution</summary> 

```python
call_counts = {}

def count_calls(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        if name not in call_counts:
            call_counts[name] = 0
        call_counts[name] += 1
        return func(*args, **kwargs)
    return wrapper
```

</details>


#### Exercise 2

Write a decorator factory `log_args_to` that accepts a dictionary object. The returned decorator, when applied to a function, should log the arguments of each call. Specifically, it should append the tuple of positional arguments (args) to a list associated with the function's name in the provided dictionary.

```python
# Your implementation of log_args_to here

call_log = {}

@log_args_to(call_log)
def add(x, y):
    return x + y

@log_args_to(call_log)
def concatenate(*words):
    return "".join(words)

add(3, 4)
add(10, -2)
concatenate("a", "b", "c")
concatenate("hello")

assert call_log['add'] == [(3, 4), (10, -2)]
assert call_log['concatenate'] == [('a', 'b', 'c'), ('hello',)]
```

<details> 
<summary>Possible Solution</summary> 

```python
call_log = {}

def log_args_to(dicty):
    def decorator(func):
        results = []
        def wrapper(*args, **kwargs):
            name = func.__name__
            results.append(args)
            if name not in dicty:
                dicty[name] = results
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

Or:

```python
def log_args_to(dicty):
    def decorator(func):
        results = []
        dicty[func.__name__] = results
        def wrapper(*args, **kwargs):
            results.append(args)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

</details>

#### Exercise 3

The following decorator `sum_values` is intended to maintain a dictionary of running totals. The decorated function `add_to_tally` provides a key and an amount to add. The decorator is not working correctly; it overwrites the previous value instead of adding to it. Fix the `sum_values` decorator.

```python
def sum_values(func):
    totals = {}

    def wrapper(key, amount):
        nonlocal totals
        totals[key] = amount # This line is incorrect
        return func(key, amount)

    # Do not change the lines below
    wrapper.get_totals = lambda: totals
    return wrapper

@sum_values
def add_to_tally(category, value):
    print(f"Added {value} to {category}")

add_to_tally('food', 100)
add_to_tally('transport', 50)
add_to_tally('food', 35)

totals = add_to_tally.get_totals()
assert totals == {'food': 135, 'transport': 50}
```

<details> 
<summary>Possible Solution</summary> 

```python
def sum_values(func):
    totals = {}

    def wrapper(key, amount):
        nonlocal totals
        totals[key] = totals.get(key, 0) + amount
        return func(key, amount)

    # Do not change the lines below
    wrapper.get_totals = lambda: totals
    return wrapper
```

</details>

#### Exercise 4

Implement a decorator `collect_results`. Each function decorated by `collect_results` should get its own, independent list for storing its return values. This list must be accessible via an attribute named `.results` on the decorated function itself.

```python
# Your implementation of collect_results here

@collect_results
def get_evens(n):
    return [i for i in range(n) if i % 2 == 0]

@collect_results
def get_odds(n):
    return [i for i in range(n) if i % 2 != 0]

get_evens(10)
get_evens(4)
get_odds(9)

assert get_evens.results == [[0, 2, 4, 6, 8], [0, 2]]
assert get_odds.results == [[1, 3, 5, 7]]
```

<details> 
<summary>Possible Solution</summary> 

```python
def collect_results(func):
    values = []
    def wrapper(*args, **kwargs):
        return values.append(func(*args, **kwargs))
    wrapper.results = values
    return wrapper    
```

</details>

#### Exercise 5

The group_by decorator below is supposed to take an item and a group name, and append the item to a list for that group. However, it has a bug: all groups end up containing all items. Diagnose and fix the group_by decorator so that each group's list is independent.

```python
def group_by(func):
    grouped_items = {}
    shared_list = [] # This may be part of the problem

    def wrapper(group, item):
        nonlocal grouped_items
        if group not in grouped_items:
            grouped_items[group] = shared_list
        grouped_items[group].append(item)
        return func(group, item)

    # Do not change the lines below
    wrapper.get_groups = lambda: grouped_items
    return wrapper


@group_by
def add_item(group, item):
    print(f"Adding '{item}' to '{group}'")

add_item('fruit', 'apple')
add_item('dairy', 'milk')
add_item('fruit', 'banana')

groups = add_item.get_groups()
assert groups['fruit'] == ['apple', 'banana']
assert groups['dairy'] == ['milk']
```

<details> 
<summary>Possible Solution</summary> 

```python
def group_by(func):
    grouped_items = {}

    def wrapper(group, item):
        shared_list = []
        nonlocal grouped_items
        if group not in grouped_items:
            grouped_items[group] = shared_list
        grouped_items[group].append(item)
        return func(group, item)

    # Do not change the lines below
    wrapper.get_groups = lambda: grouped_items
    return wrapper
```

</details>

#### Exercise 6

Write a decorator record_transaction that maintains a single, shared list of all transactions. A decorated function will be called with keyword arguments describing a transaction (e.g., product='pen', price=1.50, quantity=5). The decorator should create a dictionary from these keyword arguments and append it to the shared transaction log.


```python
# Your implementation of record_transaction and its state here
@record_transaction
def sell(**details):
    # This function's body can be empty
    pass

sell(product='Laptop', price=1200, customer_id=101)
sell(product='Mouse', price=25, quantity=2, customer_id=101)
sell(product='Keyboard', price=75, customer_id=102)

expected_log = [
    {'product': 'Laptop', 'price': 1200, 'customer_id': 101},
    {'product': 'Mouse', 'price': 25, 'quantity': 2, 'customer_id': 101},
    {'product': 'Keyboard', 'price': 75, 'customer_id': 102}
]
assert transaction_log == expected_log
```

<details> 
<summary>Possible Solution</summary> 

```python
transaction_log = []

def record_transaction(func):
    def wrapper(**kwargs):
        transaction_log.append(dict(kwargs))
        return func(**kwargs)
    return wrapper
```

</details>


#### Exercise 7

The `update_user_activity` decorator is meant to track user actions in a nested dictionary. For each user, it should maintain counts of different activities. The current implementation fails to save the activity for a user's first recorded action. Fix the bug in the wrapper function.

```python
def update_user_activity(func):
    activity_log = {}

    def wrapper(user, action):
        user_actions = activity_log.get(user, {})
        user_actions[action] = user_actions.get(action, 0) + 1
        func(user, action)

    # Do not change the lines below
    wrapper.get_log = lambda: activity_log
    return wrapper


@update_user_activity
def record_action(user, action):
    pass

record_action('user1', 'login')
record_action('user2', 'login')
record_action('user1', 'post_comment')
record_action('user1', 'login')
record_action('user2', 'logout')

log = record_action.get_log()
expected = {
    'user1': {'login': 2, 'post_comment': 1},
    'user2': {'login': 1, 'logout': 1}
}
assert log == expected
```

<details> 
<summary>Possible Solution</summary> 

```python
def update_user_activity(func):
    activity_log = {}

    def wrapper(user, action):
        user_actions = activity_log.get(user, {})
        user_actions[action] = user_actions.get(action, 0) + 1
        activity_log[user] = user_actions
        func(user, action)

    # Do not change the lines below
    wrapper.get_log = lambda: activity_log
    return wrapper
```
</details>

#### Exercise 8

Write a decorator `log_calls` that maintains a persistent dictionary. This dictionary, `call_log`, should map decorated function names to a list of tuples, where each tuple contains the positional arguments for a single call.

```python
def log_calls(func):
    # Your implementation here
    pass

@log_calls
def add(a, b):
    return a + b

@log_calls
def subtract(a, b):
    return a - b

add(1, 2)
add(3, 4)
subtract(10, 5)
add(5, 6)
subtract(8, 3)

assert log_calls.call_log['add'] == [(1, 2), (3, 4), (5, 6)]
assert log_calls.call_log['subtract'] == [(10, 5), (8, 3)]
```
<details> 
<summary>Possible Solution</summary> 

```python
def log_calls(func):

    def wrapper(*args):
        name = func.__name__
        if name not in log_calls.call_log:
            log_calls.call_log[name] = []
        log_calls.call_log[name].append(args)

        return func(*args)
    return wrapper

log_calls.call_log = {}
```

</details>

#### Exercise 9

Write a decorator factory `tally_results(tally)`. The factory accepts a dictionary, `tally`, which the decorator will use to store a count of each result returned by the decorated function.

```python
def tally_results(tally):
    # Your implementation here
    pass

current_tally = {}

@tally_results(current_tally)
def get_grade(score):
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

get_grade(95)
get_grade(82)
get_grade(90)
get_grade(75)
get_grade(60)
get_grade(83)
get_grade(45)

assert current_tally['A'] == 2
assert current_tally['B'] == 2
assert current_tally['C'] == 1
assert current_tally['D'] == 1
assert current_tally['F'] == 1
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 10

Write a decorator factory `audit(log`). The factory accepts a dictionary `log`. The decorator it creates should record call details for the decorated function.
The log's structure should be a nested dictionary: `{ function_name: [call_1, call_2, ...] }`, where each call is a dictionary `{'args': tuple_of_args, 'kwargs': dict_of_kwargs}`.

```python
def audit(log):
    # Your implementation here
    pass

audit_log = {}

@audit(audit_log)
def purchase(item, price, quantity=1, **details):
    pass

purchase('book', 12.99, quantity=2, author='Jane Doe')
purchase('pen', 1.50)
purchase('book', 10.00, author='John Smith', condition='used')

expected_log = {
    'purchase': [
        {
            'args': ('book', 12.99),
            'kwargs': {'quantity': 2, 'author': 'Jane Doe'},
        },
        {
            'args': ('pen', 1.50),
            'kwargs': {},
        },
        {
            'args': ('book', 10.00),
            'kwargs': {'author': 'John Smith', 'condition': 'used'},
        },
    ]
}

assert audit_log == expected_log
```

<details> 
<summary>Possible Solution</summary> 
</details>


#### Exercise 11

Write a decorator `with_history`. For each function it decorates, it should attach a history attribute to the function itself. This attribute should be a list containing the return values of all previous calls to that specific function. Each decorated function must have its own independent history.

```python
def with_history(func):
    # Your implementation here
    pass

@with_history
def add(x, y):
    return x + y

@with_history
def multiply(x, y):
    return x * y

add(1, 2)
add(3, 4)
multiply(2, 3)
add(5, 6)
multiply(4, 5)

assert add.history == [3, 7, 11]
assert multiply.history == [6, 20]
assert hasattr(add, 'history')
assert hasattr(multiply, 'history')
assert add.history is not multiply.history
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 12

The collect_kwargs decorator is designed to accumulate all keyword arguments passed to a function across all its calls into a single dictionary. The current implementation incorrectly overwrites the collected arguments with the kwargs from the most recent call.[9:01 AM]Fix the bug.

```python
def collect_kwargs(func):
    collected_kwargs = {}

    def wrapper(*args, **kwargs):
        nonlocal collected_kwargs
        # There is a bug on the next line.
        collected_kwargs = kwargs
        # This attribute is for testing purposes
        wrapper.all_kwargs = collected_kwargs
        return func(*args, **kwargs)

    wrapper.all_kwargs = collected_kwargs
    return wrapper

@collect_kwargs
def get_config(user=None):
    pass

get_config(user='admin', theme='dark')
get_config(user='guest', retries=3)

# This assertion fails with the buggy implementation
assert get_config.all_kwargs == {
    'user': 'guest',
    'theme': 'dark',
    'retries': 3,
}
```
<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 13

Write a decorator factory, `track_events(registry)`, that takes a dictionary as an argument. The returned decorator should be applied to functions that process events. For each call, the decorator must log an "event record" dictionary into the shared registry.

The registry's keys are event types, which correspond to the first argument of the decorated function. The registry's values are lists of event record dictionaries.

Each event record should have the structure: `{'source': function_name, 'args': all_other_args, 'result': return_value}`.

```python
def track_events(registry):
    # Your implementation here
    pass

event_registry = {}

@track_events(event_registry)
def process_login(event_type, username, success):
    return f"User {username} login {'succeeded' if success else 'failed'}."

@track_events(event_registry)
def process_payment(event_type, amount, currency):
    return f"Processed {amount} {currency}."

process_login('auth', 'user1', True)
process_payment('finance', 100, 'USD')
process_login('auth', 'user2', False)
process_payment('finance', 50, 'EUR')
process_login('auth', 'user1', True)

expected_registry = {
    'auth': [
        {'source': 'process_login', 'args': ('user1', True), 'result': 'User user1 login succeeded.'},
        {'source': 'process_login', 'args': ('user2', False), 'result': 'User user2 login failed.'},
        {'source': 'process_login', 'args': ('user1', True), 'result': 'User user1 login succeeded.'}
    ],
    'finance': [
        {'source': 'process_payment', 'args': (100, 'USD'), 'result': 'Processed 100 USD.'},
        {'source': 'process_payment', 'args': (50, 'EUR'), 'result': 'Processed 50 EUR.'}
    ]
}

assert event_registry == expected_registry
```
<details> 
<summary>Possible Solution</summary> 
</details>


[Back to the top](#top)


### Decorator Practice 4

#### Exercise 1 — Decoration vs. Invocation Order

Code:

```python
def first_decorator(func):
    print("Applying 'first_decorator'")
    def wrapper(*args, **kwargs):
        print("'first_decorator' wrapper executing")
        return func(*args, **kwargs)
    return wrapper

def second_decorator(func):
    print("Applying 'second_decorator'")
    def wrapper(*args, **kwargs):
        print("'second_decorator' wrapper executing")
        return func(*args, **kwargs)
    return wrapper

@first_decorator
@second_decorator
def say_hello():
    print("Hello from the original function!")

print("--- Decoration complete ---")

say_hello()

```

Question: What will be printed to the console when this script is executed? List the output line by line in the correct order.

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 2 — Argument Transformation Pipeline

Code

```python
def to_uppercase(func):
    def wrapper(text):
        # Converts the argument to uppercase before passing it on
        return func(text.upper())
    return wrapper

def add_exclamation(func):
    def wrapper(text):
        # Appends an exclamation mark to the argument before passing it on
        return func(text + "!")
    return wrapper

@to_uppercase
@add_exclamation
def process_message(message):
    return f"Processed: {message}"

result = process_message("hello world")
```

Question:  What is the value of the result variable after this code runs?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 3 — Return Value Transformation Pipeline

Code
```python 
def wrap_in_html(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Gets the result from the wrapped function
            result = func(*args, **kwargs)
            # Wraps the result in HTML tags
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

def to_string(func):
    def wrapper(*args, **kwargs):
        # Gets the result from the wrapped function
        result = func(*args, **kwargs)
        # Converts the result to a string
        return str(result)
    return wrapper

@wrap_in_html("p")
@to_string
def get_sum(a, b):
    return a + b

output = get_sum(10, 20)
```

Question: What is the value of the output variable after this code executes?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 4 — The Importance of Order

Code
```python
def multiply_by(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * factor
        return wrapper
    return decorator

def add(amount):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + amount
        return wrapper
    return decorator

@multiply_by(10)
@add(5)
def calculate_v1(n):
    return n

@add(5)
@multiply_by(10)
def calculate_v2(n):
    return n

result1 = calculate_v1(10)
result2 = calculate_v2(10)

```

Question: What are the final values of `result1` and `result2`?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 5 — Observing Transformed Arguments

Code

```python 
log_v1 = []

def record_args_v1(func):
    def wrapper(*args, **kwargs):
        log_v1.append(args)
        return func(*args, **kwargs)
    return wrapper

log_v2 = []

def record_args_v2(func):
    def wrapper(*args, **kwargs):
        log_v2.append(args)
        return func(*args, **kwargs)
    return wrapper

def double_first_arg(func):
    def wrapper(a, *args, **kwargs):
        doubled_a = a * 2
        return func(doubled_a, *args, **kwargs)
    return wrapper


@record_args_v1
@double_first_arg
def process_data_v1(x, y):
    pass

@double_first_arg
@record_args_v2
def process_data_v2(x, y):
    pass


process_data_v1(10, 'A')
process_data_v1(20, 'B')

process_data_v2(10, 'A')
process_data_v2(20, 'B')
```

Question: After the script runs, what are the final values of the lists `log_v1` and `log_v2`?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 6 — Debugging a Conditional Stack

Code

```python
import collections

call_log = collections.defaultdict(int)

def log_call(func):
    def wrapper(*args, **kwargs):
        call_log[func.__name__] += 1
        print(f"'{func.__name__}' was called.")
        return func(*args, **kwargs)
    return wrapper

def requires_non_empty(func):
    def wrapper(items):
        if not items:
            print("Execution skipped: input is empty.")
            return None
        return func(items)
    return wrapper


@log_call
@requires_non_empty
def process_list(data):
    print("Processing list...")
    return len(data)

# --- Function Calls ---
process_list([1, 2, 3])
process_list([])
```

Question: A programmer expected the `log_call` decorator to only log calls that are actually executed. However, the output shows that `'process_list'` is logged even when the list is empty and processing is skipped. Why is the log message printed for the empty list?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 7 — Synthesizing a Formatter Stack

Problem Statement: You are building a command-line tool that formats messages. You need two decorators to apply specific formatting rules to a base message.

1.  A decorator named `add_timestamp` that prepends a fixed timestamp string, "[2023-10-26] ", to the return value of a function.
2.  A decorator named `sanitize_output` that replaces any occurrences of the word "secret" with "[REDACTED]" in the return value of a function.

Implement these two decorators and apply them to the format_message function to satisfy the behavior shown in the tests. The sanitation must happen ​before​ the timestamp is added.

Function Signature
```python
# Implement your 'add_timestamp' and 'sanitize_output' decorators here.

# Apply your decorators in the correct order to this function.
def format_message(text):
    return text


Tests

assert format_message("hello world") == "[2023-10-26] hello world"
assert format_message("this is a secret message") == "[2023-10-26] this is a [REDACTED] message"
assert format_message("a secret is a secret") == "[2023-10-26] a [REDACTED] is a [REDACTED]"
```

<details> 
<summary>Possible Solution</summary> 
</details>


#### Exercise 8 — Decoration Syntax

Problem Statement:  In Python, applying multiple decorators to a function is syntactic sugar for nested function calls. Given the following function definition:

```python
@alpha
@beta
def my_function():
    print("Executing my_function")
```

This is equivalent to manually applying the decorators to the base function my_function in a specific order.

Question:  Which of the following manual applications is equivalent to the stacked decorator syntax shown above?

1.  `my_function = alpha(my_function)`
    `my_function = beta(my_function)`
2.  `my_function = beta(my_function)`
    `my_function = alpha(my_function)`
3.  `my_function = alpha(beta(my_function))`
4.  `my_function = beta(alpha(my_function))`

Choose the single best answer from options 1-4.


<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 9 - Return Value Transformation

Problem Statement:  Two decorators are defined to modify a function's string return value. One converts the string to uppercase, and the other appends an exclamation mark. They are stacked on a function greet.

Code
```python
def to_uppercase(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        return original_result.upper()
    return wrapper

def add_excitement(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        return original_result + '!'
    return wrapper

@to_uppercase
@add_excitement
def greet(name):
    return f"Hello, {name}"

result = greet("World")
```

Question: After the code runs, what is the value of the result variable?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 10 - Argument Observation vs. Modification

Problem Statement

One decorator, `record_call`, appends the arguments it receives to a global list. Another decorator, `double_input`, modifies its argument before passing it to the wrapped function.

Code
```python
CALL_LOG = []

def record_call(func):
    def wrapper(x):
        CALL_LOG.append(x)
        return func(x)
    return wrapper

def double_input(func):
    def wrapper(x):
        return func(x * 2)
    return wrapper

@record_call
@double_input
def process_number(n):
    # This function's return value is not used.
    pass

process_number(5)
process_number(10)
```

Question: After running the code, what is the final value of the CALL_LOG list?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 11 - Conditional Execution

Problem Statement

The cache_result decorator stores a function's return value in a dictionary to avoid re-computation. The `only_if_positive`decorator acts as a gate: it calls the wrapped function only if the input is positive; otherwise, it returns `None` immediately.

Code

```python
CACHE = {}

def cache_result(func):
    def wrapper(n):
        if n not in CACHE:
            CACHE[n] = func(n)
        return CACHE[n]
    return wrapper

def only_if_positive(func):
    def wrapper(n):
        if n > 0:
            return func(n)
        return None
    return wrapper

@only_if_positive
@cache_result
def expensive_calculation(x):
    # Simulate a costly calculation
    print(f"Calculating for {x}...")
    return x * 10

expensive_calculation(5)
expensive_calculation(-3)
expensive_calculation(5)
```

Question
After this code executes, what will be the contents of the CACHE dictionary?

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 12 - Implementing a Logging and Validation Stack

Problem Statement: You are tasked with processing user submissions. Before saving a submission, it must be validated and the attempt must be logged.

Implement two decorators:

1.  `log_submission`: This decorator must record the user's ID and the original, unmodified submission data in a list named SUBMISSION_LOG. Each log entry should be a dictionary {'user_id': id, 'data': data}.
2.  `validate_length`: This decorator checks if the 'content' key in the submission data dictionary has a string value longer than 10 characters. If it is, the decorator should replace the value with the string "[CONTENT TOO LONG]" before passing it to the decorated function.

Stack these decorators on the save_submission function so that the log always contains the original data, even when the validation modifies it.

```python

SUBMISSION_LOG = []
# Implement log_submission decorator here
# Implement validate_length decorator here

@log_submission
@validate_length
def save_submission(user_id, data):
    print(f"Saving for {user_id}: {data}")
    # In a real system, this would save to a database.
 ```

Tests
```python

save_submission('user1', {'content': 'short post'})
save_submission('user2', {'content': 'This is a very long post that exceeds the limit.'})
save_submission('user1', {'content': 'another'})

assert SUBMISSION_LOG == [
    {'user_id': 'user1', 'data': {'content': 'short post'}},
    {'user_id': 'user2', 'data': {'content': 'This is a very long post that exceeds the limit.'}},
    {'user_id': 'user1', 'data': {'content': 'another'}}
]
# The final print output should reflect the validated (and possibly modified) data.

```

#### Exercise 13 - Injecting and Transforming Keyword Arguments

Problem Statement: Consider a system where operations are processed in batches. A `with_batch_id` decorator injects a `batch_id` into the keyword arguments of a function call. A `format_for_export` decorator takes the function's dictionary result and converts it into a formatted string.

Code

```python
def with_batch_id(batch_id):
    def decorator(func):
        def wrapper(*args, **kwargs):
            kwargs['batch_id'] = batch_id
            return func(*args, **kwargs)
        return wrapper
    return decorator

def format_for_export(func):
    def wrapper(*args, **kwargs):
        result_dict = func(*args, **kwargs)
        # Format: "key1=value1;key2=value2;"
        export_string = ""
        for key, value in sorted(result_dict.items()):
            export_string += f"{key}={value};"
        return export_string
    return wrapper

@format_for_export
@with_batch_id("B7-2024")
def process_data(record_id, **details):
    # Combine the record_id and all details into a single dictionary
    final_data = {'record_id': record_id}
    final_data.update(details)
    return final_data

export_result = process_data("REC456", status="completed", user="admin")
```


Question: After the code runs, what is the value of the `export_result` variable?

<details> 
<summary>Possible Solution</summary> 
</details>

[Back to the top](#top)