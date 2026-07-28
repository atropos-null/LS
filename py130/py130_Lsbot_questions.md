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
</details>

#### Exercise 9: Conditional Capitalization (Generator Expression)

Problem Statement:​ This time, use a generator ​expression​ to create a generator that capitalizes strings from a list but only if their length is greater than 4.

Function Signature: No function, assign a generator expression to the variable `capitalized_long_words`

Test Cases:

```python
words = ['launch', 'school', 'is', 'a', 'great', 'place']
capitalized_long_words = (word.capitalize() for word in words if len(word) > 4)
assert list(capitalized_long_words) == ['Launch', 'School', 'Great']

words2 = ['short', 'words']
capitalized_long_words2 = (word.capitalize() for word in words2 if len(word) > 4)
assert list(capitalized_long_words2) == ['Short', 'Words']
```

<details> 
<summary>Possible Solution</summary> 
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
</details>

#### Exercise 11: Flatten a List of Lists with yield from

Problem Statement:​ Create a generator that takes a list of lists (a nested list) and yields each item from the sublists in order. Use the `yield from` syntax.

Function Signature: ``` def flatten_list(nested_list):```

Test Cases:

```python
assert list(flatten_list([[1, 2], [3, 4], [5]])) == [1, 2, 3, 4, 5]
assert list(flatten_list([['a', 'b'], ['c']])) == ['a', 'b', 'c']
assert list(flatten_list([[], [1, 2], []])) == [1, 2]
assert list(flatten_list([])) == []
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 12: Running Total

Problem Statement:​ Create a stateful generator that takes an iterable of numbers and yields the cumulative sum at each step.

Function Signature: ``` def running_total(iterable):```

Test Cases:

```python
assert list(running_total([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
assert list(running_total([10, -1, -2, 5])) == [10, 9, 7, 12]
assert list(running_total([])) == []
assert list(running_total([5])) == [5]
```


<details> 
<summary>Possible Solution</summary> 
</details>


#### Exercise 13: Infinite Fibonacci Sequence

Problem Statement:​ Create a generator that yields numbers in the Fibonacci sequence indefinitely. The sequence starts with 0 and 1.

Function Signature: ``` def fibonacci_sequence():```


Test Cases:

```python
import itertools
fib = fibonacci_sequence()
assert list(itertools.islice(fib, 10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Reset generator for the next test
fib = fibonacci_sequence()
assert list(itertools.islice(fib, 1)) == [0]

# Reset generator for the next test
fib = fibonacci_sequence()
assert next(fib) == 0
assert next(fib) == 1
assert next(fib) == 1
```
<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 14: Cycle an Iterable

Problem Statement:​ Create a generator that takes an iterable and yields its elements repeatedly in a cycle, indefinitely. If the iterable is empty, the generator should yield nothing.

Function Signature: ```def cycle_iterable(iterable):```

Test Cases:
```python

import itertools
c = cycle_iterable(['N', 'E', 'S', 'W'])
assert list(itertools.islice(c, 8)) == ['N', 'E', 'S', 'W', 'N', 'E', 'S', 'W']

c2 = cycle_iterable([1])
assert list(itertools.islice(c2, 5)) == [1, 1, 1, 1, 1]

c3 = cycle_iterable([])
assert list(itertools.islice(c3, 10)) == []
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 15: Interleave Iterables

Problem Statement:​ Create a generator that takes two iterables and yields elements from them one at a time, alternating. If one iterable is longer than the other, it should yield the remaining elements from the longer iterable after the shorter one is exhausted.

Function Signature: ```def interleave(iter1, iter2):```


Test Cases:

```python
assert list(interleave([1, 2, 3], ['a', 'b', 'c'])) == [1, 'a', 2, 'b', 3, 'c']
assert list(interleave([1, 2], ['a', 'b', 'c', 'd'])) == [1, 'a', 2, 'b', 'c', 'd']
assert list(interleave([1, 2, 3, 4], ['a', 'b'])) == [1, 'a', 2, 'b', 3, 4]
assert list(interleave([], [1, 2, 3])) == [1, 2, 3]
assert list(interleave([1, 2, 3], [])) == [1, 2, 3]
assert list(interleave([], [])) == []
```

<details> 
<summary>Possible Solution</summary> 
</details>


#### Exercise 16: Sliding Window

Problem Statement:​ Create a generator that yields a "sliding window" of a specified size over an iterable.
[10:45 AM]Each yield should be a tuple containing the elements in the current window.

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
</details>

#### Exercise 17: Log File Parser

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
</details>


#### Exercise 18: Simple CSV Reader

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
</details>


#### Exercise 19: Sentence Tokenizer

Problem Statement:​ Given a large string of text, create a generator that yields one sentence at a time. For this exercise, a sentence is a sequence of characters that ends with a '.', '!', or '?'. The punctuation should be included in the yielded sentence.

Function Signature: ```def tokenize_sentences(text):```


Test Cases:

```python
text = "Hello world. This is a test! Are you ready? I am."
expected = ["Hello world.", " This is a test!", " Are you ready?", " I am."]
assert list(tokenize_sentences(text)) == expected
text2 = "Single sentence."
assert list(tokenize_sentences(text2)) == ["Single sentence."]
text3 = "No punctuation here"
assert list(tokenize_sentences(text3)) == ["No punctuation here"]
assert list(tokenize_sentences("")) == []
```

<details> 
<summary>Possible Solution</summary> 
</details>

#### Exercise 20: Data Processing Pipeline

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
</details>


### Generators, on your own practice


#### Exercise 1. Select by Value

Problem Statement:  Create a generator function that yields items from an iterable that are equal to a specified value.

Function Signature:  ```def select_by_value(iterable, value):```

Requirements

•   The function must be a generator.
•   It must accept an iterable and a value to match.
•   It must yield each item from the iterable that is equal to value.
•   The order of yielded items must be the same as their order in the input iterable.
•   It must handle iterables containing different data types.

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
</details>

#### Exercise 2. Transform to Uppercase

Problem Statement:  Create a generator function that yields the uppercase version of each string in an iterable.

Function Signature: ```def transform_to_uppercase(strings):```

Requirements

•   The function must be a generator.
•   It must accept an iterable of strings.
•   It must yield the uppercase version of each string.
•   The order of yielded strings must correspond to the order of the original strings.
•   It must handle empty iterables.

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
</details>

#### Exercise 3. Filter Out Short Words

Problem Statement:  Create a generator function that filters out words from an iterable that are shorter than a given length.

Function Signature: ```def filter_out_short_words(words, min_length):```

Requirements

•   The function must be a generator.
•   It must accept an iterable of strings and an integer min_length.
•   It must yield only the strings whose length is greater than or equal to min_length.
•   The order of yielded strings must be the same as their order in the input iterable.
•   It must handle empty iterables and cases where no words meet the criteria.

Test Cases

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
</details>

#### Exercise 4. Yield with Index

Problem Statement: Create a generator function that works like enumerate. It should yield tuples containing the index and the value for each item in an iterable.

Function Signature: ``` def yield_with_index(iterable):```


Requirements

•   The function must be a generator.
•   It must accept any iterable.
•   It must yield a 2-element tuple for each item: (index, value).
•   The index should start at 0 and increment for each item.
•   The order of yielded tuples must correspond to the item order in the input iterable.
•   It must handle empty iterables.

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
</details>


#### Exercise 5. Repeat Each Item*

Problem Statement: Create a generator function that yields each item from an iterable a specified number of times before moving to the next item.

Function Signature ```def repeat_each_item(iterable, num_repeats):```

Requirements

•   The function must be a generator.
•   It must accept an iterable and a non-negative integer num_repeats.
•   For each item in the iterable, it must yield that item num_repeats times consecutively.
•   If num_repeats is 0, the generator should yield nothing.
•   It must handle empty iterables.

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
</details>

#### Exercise 6. Yield Every Nth Item

Problem Statement: Create a generator function that yields every Nth item from an iterable, starting with the first item.

Function Signature:  ```def yield_every_nth(iterable, n):```

Requirements

•   The function must be a generator.
•   It must accept an iterable and a positive integer n.
•   It must yield the 1st item, the (1+n)th item, the (1+2n)th item, and so on.
•   The first item (at index 0) should always be yielded if the iterable is not empty.
•   It must handle empty iterables.
•   Assume n will be 1 or greater.

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
</details>

#### Exercise 7. Yield Until Value

Problem Statement: Create a generator function that yields items from an iterable until a specific value is encountered. The stop value itself should not be yielded.

Function Signature: ```def yield_until_value(iterable, stop_value):```


Requirements

•   The function must be a generator.
•   It must accept an iterable and a stop_value.
•   It must yield items from the beginning of the iterable.
•   It must stop yielding as soon as it encounters an item equal to stop_value.
•   The stop_value item must not be included in the output.
•   If the stop_value is not found, it should yield all items from the iterable.

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
</details>

#### Exercise 8. Flatten One Level

Problem Statement: Create a generator function that takes an iterable of iterables (e.g., a list of lists) and yields each item from the inner iterables, one by one.

Function Signature: ```def flatten_one_level(nested_iterable):```

Requirements

•   The function must be a generator.
•   It must accept an iterable where each element is itself an iterable.
•   It must yield each element from each inner iterable in sequence.
•   The order of yielded elements should correspond to iterating through the outer iterable, and then through each inner iterable.
•   It should handle empty outer and inner iterables.

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
</details>

#### Exercise 9. Filter Dictionary Items

Problem Statement: Create a generator function that yields (key, value) tuples from a dictionary for which a given predicate function returns a truthy value The predicate function will receive the value as its only argument.

Function Signature: `def filter_dict_items(dictionary, predicate):`


Requirements

•   The function must be a generator.
•   It must accept a dictionary and a single-argument function predicate.
•   It must iterate over the dictionary's items.
•   For each (key, value) pair, it must call predicate(value).
•   If the predicate returns a truthy value, the generator must yield the (key, value) tuple.
•   The order of yielded items is not guaranteed (it depends on the dictionary's iteration order).

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
</details>

#### Exercise 10. Yield Unique Items

Problem Statement: Create a generator function that yields only the unique items from an iterable, preserving the order of their first appearance.

Function Signature: `def yield_unique_items(iterable):`

Requirements

•   The function must be a generator.
•   It must accept an iterable.
•   It must yield each unique item from the iterable exactly once.
•   The order of yielded items must be the same as the order of their first appearance in the input iterable.
•   It must handle different data types, including unhashable types if possible (though tests will only use hashable types).
•   It must handle empty iterables.

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
</details>

#### Exercise 11. Create a Bounded Range Generator

Problem Statement:  Using a generator expression, create a generator that yields numbers in a sequence with a specified start, stop (exclusive), and step, similar to the built-in range.

Function Signature: ```def bounded_range_generator(start, stop, step):```

Requirements

•   The function must return a generator.
•   The implementation must use a generator expression.
•   It must yield numbers starting from start.
•   It must stop yielding before it reaches or exceeds stop.
•   Each subsequent number must be the previous number plus step.
•   It should handle positive and negative steps.

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
</details>

#### Exercise 12. Chain Iterables

Problem Statement: Create a generator function that accepts multiple iterables as arguments and yields all items from the first iterable, then all items from the second, and so on.

Function Signature: ```def chain_iterables(*iterables):```

Requirements

•   The function must be a generator.
•   It must accept a variable number of iterable arguments.
•   It must yield all elements from the first iterable, followed by all elements from the second, and so on, in order.
•   It should handle cases with no arguments or with empty iterables among the arguments.
•   Consider using yield from for a concise implementation.

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
</details>

#### Exercise 13. Interleave Iterables

Problem Statement: Create a generator that accepts two iterables and yields one item from the first, then one from the second, then the next from the first, and so on. If one iterable is exhausted, it should continue yielding items from the other.

Function Signature: ```def interleave_iterables(iter1, iter2):```

Requirements

•   The function must be a generator.
•   It must accept two iterables.
•   It must yield items by alternating between iter1 and iter2.
•   When one iterable is exhausted, the generator must yield all remaining items from the other iterable.
•   It must handle empty iterables.

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
</details>

#### Exercise 14. Transform and Filter with a Generator Expression

Problem Statement: Write a function that returns a generator expression. The generator should process an iterable of numbers, selecting only the even ones and yielding their squares.

Function Signature: ```def square_of_evens(numbers):```


Requirements

•   The function must return a generator object, created from a generator expression.
•   The returned generator must iterate over the input numbers.
•   It must only consider even numbers.
•   It must yield the square of each even number.
•   It must handle empty iterables.

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
</details>

#### Exercise 16. Bounded Repetition

Problem Statement: Create a generator that yields items from an iterable, but stops after a certain total number of items have been yielded, or when the iterable is exhausted, whichever comes first.

Function Signature: ```def bounded_repetition(iterable, max_yields):```


Requirements

•   The function must be a generator.
•   It must accept an iterable and a non-negative integer max_yields.
•   It must yield items from the iterable in their original order.
•   It must stop yielding after max_yields items have been produced.
•   If the iterable has fewer than max_yields items, it yields all of them.
•   If max_yields is 0, it should yield nothing.

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
</details>

#### Exercise 17. Skip Header and Footer

Problem Statement: Create a generator that yields items from an iterable, but skips a specified number of items at the beginning (header) and at the end (footer).

Function Signature: ```def skip_header_footer(iterable, header_size, footer_size):```

Requirements

•   The function must be a generator.
•   It must accept an iterable, a non-negative header_size, and a non-negative footer_size.
•   It must not yield the first header_size items.
•   It must not yield the last footer_size items.
•   It should correctly handle cases where header_size + footer_size is greater than or equal to the total number of items.

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
</details>

#### Exercise 18. Yield Runs of Consecutive Duplicates

Problem Statement: Create a generator that processes a sorted iterable and yields lists of consecutive identical items.

Function Signature: ```def yield_runs(sorted_iterable):```


Requirements

•   The function must be a generator.
•   It must accept an iterable that is assumed to be sorted.
•   It must yield a list for each run of consecutive identical items.
•   Each yielded list should contain all identical items in that run.
•   It must handle empty iterables.

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
</details>

#### Exercise 19. Partition by Predicate

Problem Statement: Create a generator that yields items from an iterable in two groups based on a predicate.[11:41 AM]First, it should yield all items for which the predicate is truthy, and then it should yield all items for which the predicate is falsy.

Function Signature: ```def partition_by_predicate(iterable, predicate):```

Requirements

•   The function must be a generator.
•   It must accept an iterable and a single-argument function predicate.
•   It must iterate through the entire iterable once, caching the results.
•   It must first yield from all items for which predicate(item) is truthy, in their original relative order.
•   After that, it must yield from all items for which predicate(item) is falsy, in their original relative order.
•   It must handle empty iterables.

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
</details>

#### Exercise 20. Group By Key

Problem Statement: Create a generator that groups items from an iterable of dictionaries by a common key.[11:41 AM]For each unique value of the specified key, the generator should yield a tuple containing that value and another generator that yields all dictionaries having that value.

Function Signature: ```def group_by_key(iterable, key):```

Requirements

•   The function must be a generator.
•   It must accept an iterable of dictionaries and a key.
•   It must identify unique values for the given key in the order they first appear.
•   For each unique key-value, it must yield a 2-element tuple: (key_value, items_generator).
•   key_value is the value associated with the specified key.
•   items_generator is a generator that yields all dictionaries from the original iterable (in their original order) that have key_value for the given key.
•   It must handle cases where dictionaries are missing the specified key (they should be ignored).
•   The outer generator should not consume the input iterable more than once.

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

Test Summary:The tests verify correct grouping, handling of missing keys, preservation of original item order within groups, and preservation of group order. They also confirm it works with empty and generator inputs.

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

