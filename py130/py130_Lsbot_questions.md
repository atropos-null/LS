# LS Bot Generated Questions for PY130

Total Questions: 

## Lesson 1: Functions, Generators, and Files

### First Class and Higher-Order Functions


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

#### Question 2:

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
</details>


<details> 
<summary>Possible Solution</summary> 
</details>