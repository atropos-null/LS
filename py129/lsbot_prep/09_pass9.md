# PY129 LSBOT Prep Questions

## Pass 9, Custody Transfer Drill Prompt

Prompt: Generate 8 timed PY129 assessment-style drills (3–7 minutes each) that specifically target custody-transfer freeze points — the single line where responsibility must move (store, pass, delegate, mutate, aggregate, or return).

Each drill must:

* Be solvable in ≤ 10 lines of implementation
* Require one critical custody-transfer decision
* Involve at least one of:
    * collaborator delegation
	* protocol-triggered behavior (in, iteration, slicing, len, etc.)
	* magic method semantics (__iadd__, __eq__, __str__, __repr__, __contains__, __getitem__)

* Avoid geometry, pure math, or trivial examples
* Prefer coordinator/collaborator scenarios using lists of objects

For each drill, provide:

1. Clear problem description (explicit behavioral requirement — no ambiguity)
2. 2–3 Correct I/O examples
3. 1 Common Wrong Output example that reflects a reasonable but incorrect assumption
4. A short “Hidden Trap” label (≤ 6 words)

Additional constraints (mandatory across the full set):

* At least one drill involving defensive copying in `__init__`
* At least one drill where += must mutate (id unchanged)
* At least one drill where += must rebind (id changes)
* At least one drill involving string aggregation over objects (e.g., “Team: …”)
* At least one drill where a protocol is triggered implicitly (in, slicing, iteration fallback, etc.)

Do not provide solutions.  
Do not provide hints.  
Do not name the concepts being tested.  
Make the traps subtle, not obvious type errors.  
Focus on the single line where responsibility transfers.  


### Drill 1 (3 minutes)

Description​: Create a `WorkLog` class that is initialized with a list of task strings. The `WorkLog` must maintain its own internal list of tasks. This internal list must not be affected by any external changes made to the original list that was passed to the constructor.


```python
# Correct I/O Example 1
tasks = ["Task 1", "Task 2"]
log = WorkLog(tasks)
tasks.append("Task 3")
print(log.tasks) # Expected: ['Task 1', 'Task 2']

# Example 2
tasks = []
log = WorkLog(tasks)
tasks.append("Initial Task")
print(log.tasks) # Expected: []

# Common Wrong Output Example​:

tasks = ["Task 1", "Task 2"]
log = WorkLog(tasks)
tasks.append("Task 3")
print(log.tasks) # Wrong: ['Task 1', 'Task 2', 'Task 3']
```

<details> 
<summary>Hidden Trap</summary> 
Shared reference allows external mutation.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>

### Drill 2 (4 minutes)

Description​: Create an `Inventory` class that stores items in a list. Implement the in-place addition operator (`+=`) to add a list of new items to an `Inventory` object. The operation must modify the original `Inventory` object, not create a new one.

```python
#Correct I/O Examples​:

# Example 1
inv = Inventory(["apple", "banana"])
inv_id_before = id(inv)
inv += ["cherry", "date"]
inv_id_after = id(inv)
print(inv.items) # Expected: ['apple', 'banana', 'cherry', 'date']
print(inv_id_before == inv_id_after) # Expected: True

# Common Wrong Output Example​:

inv = Inventory(["apple", "banana"])
inv_id_before = id(inv)
inv += ["cherry", "date"]
inv_id_after = id(inv)
print(inv.items) # Plausible: ['apple', 'banana', 'cherry', 'date']
print(inv_id_before == inv_id_after) # Wrong: False
```


<details> 
<summary>Hidden Trap</summary> 
Rebinding name instead of mutating object.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 3 (5 minutes)

Description​: Create an immutable `PermissionSet` class that stores permissions as a tuple. Implement the addition operator (`+`) to create a ​new​ `PermissionSet` containing permissions from both operands. Ensure that the in-place addition operator (`+=`) also results in a new object, leveraging the behavior of `+`.

```python
# Correct I/O Example 1
p_set = PermissionSet(("READ", "WRITE"))
id_before = id(p_set)
p_set += ("EXECUTE",)
id_after = id(p_set)
print(p_set.permissions) # Expected: ('READ', 'WRITE', 'EXECUTE')
print(id_before == id_after) # Expected: False

# Common Wrong Output Example​:

p_set = PermissionSet(("READ", "WRITE"))
id_before = id(p_set)
# Assume an incorrect implementation that tries to mutate
# or otherwise fails to create a new object.
p_set += ("EXECUTE",)
id_after = id(p_set)
print(p_set.permissions) # Plausible: ('READ', 'WRITE', 'EXECUTE')
print(id_before == id_after) # Wrong: True
```

<details> 
<summary>Hidden Trap</summary> 
 `+=` fallback behavior with immutable data.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>



### Drill 4 (4 minutes)

Description​: Given the `Participant` class below, create a `Team` class. `Team` is initialized with a team name string and a list of Participant objects. Implement the `__str__` method for the `Team` class to produce a summary string: `"Team [Name]: [Participant 1], [Participant 2]"`.

```python
# Provided class
class Participant:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
```

```python
# Correct I/O Example 1
p1 = Participant("Alice")
p2 = Participant("Bob")
team = Team("Eagles", [p1, p2])
print(str(team)) # Expected: "Team Eagles: Alice, Bob"

# Example 2
team_solo = Team("Solo", [Participant("Charlie")])
print(str(team_solo)) # Expected: "Team Solo: Charlie"

# Common Wrong Output Example​:

p1 = Participant("Alice")
p2 = Participant("Bob")
team = Team("Eagles", [p1, p2])
# Wrong output if str() is not used on participants
print(str(team)) # Wrong: "Team Eagles: [<__main__.Participant object at ...>, <__main__.Participant object at ...>]"
```

<details> 
<summary>Hidden Trap</summary> 
Forgetting collaborators have their own protocol.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 5 (5 minutes)

Description​: Given the `Book` class below (where equality is based on isbn), create a Bookshelf class that holds a list of `Book` objects. The `Bookshelf` class must correctly support the in operator to check for the presence of a book by its value, not its identity.

```python
# Provided class

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
    def __eq__(self, other):
        return isinstance(other, Book) and self.isbn == other.isbn
```

```python
# Correct I/O Example 1

b1 = Book("The Hobbit", "123")
b2 = Book("The Silmarillion", "456")
shelf = Bookshelf([b1, b2])
book_to_find = Book("The Hobbit", "123") # Different object, same ISBN
print(book_to_find in shelf) # Expected: True

# Example 2
shelf = Bookshelf([Book("The Hobbit", "123")])
book_not_found = Book("Dune", "789")
print(book_not_found in shelf) # Expected: False

# Common Wrong Output Example​:

b1 = Book("The Hobbit", "123")
shelf = Bookshelf([b1])
book_to_find = Book("The Hobbit", "123") # Different object, same ISBN
# Wrong if implementation checks by identity (`is`) instead of equality (`==`)
print(book_to_find in shelf) # Wrong: False
```

<details> 
<summary>Hidden Trap</summary> 
Operator falls back to iteration/equality.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>



### Drill 6 (6 minutes)

Description​: Create a `Report` class that stores a list of data entries (strings). Implement slicing for `Report` objects. When a `Report` is sliced, the operation must return a ​new `Report` object​ containing only the sliced entries, not a raw list.

```python
# Correct I/O Example 1:

report = Report(["Entry 1", "Entry 2", "Entry 3", "Entry 4"])
sliced_report = report[1:3]
print(isinstance(sliced_report, Report)) # Expected: True
print(sliced_report.entries) # Expected: ['Entry 2', 'Entry 3']

# Example 2
report = Report(["A", "B", "C"])
sliced_report = report[:1]
print(isinstance(sliced_report, Report)) # Expected: True
print(sliced_report.entries) # Expected: ['A']

# Common Wrong Output Example​:

report = Report(["Entry 1", "Entry 2", "Entry 3", "Entry 4"])
sliced_report = report[1:3]
print(isinstance(sliced_report, Report)) # Wrong: False
print(sliced_report) # Wrong: ['Entry 2', 'Entry 3']
```

<details> 
<summary>Hidden Trap</summary> 
Protocol returns raw data, not container.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 7 (3 minutes)

Description​: Create a `Message` class with message_id and content attributes. Two `Message` objects must be considered equal if and only if their `message_id` attributes are identical. The content attribute should not be part of the equality comparison.

```python
# Correct I/O Examples​:

# Example 1
msg1 = Message(101, "Hello")
msg2 = Message(101, "Hi there")
print(msg1 == msg2) # Expected: True

# Example 2
msg1 = Message(101, "Hello")
msg3 = Message(102, "Hello")
print(msg1 == msg3) # Expected: False

# Common Wrong Output Example​:

msg1 = Message(101, "Hello")
msg2 = Message(101, "Hi there")
# Wrong if default identity check is used or if content is compared
print(msg1 == msg2) # Wrong: False
```


<details> 
<summary>Hidden Trap</summary> 
Object equality defaults to identity.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 8 (7 minutes)

Description​: Given the `SensorReading` class, create a `Device` class that stores a list of `SensorReading` objects. Implement a method get_critical_readings(max_val) that returns a ​new list​ containing only the `SensorReading` objects from the device whose value exceeds max_val. The device's own list of readings must not be altered.

```python
# Provided class
class SensorReading:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"SensorReading({self.value})"


# Correct I/O Example 1

readings = [SensorReading(98), SensorReading(101), SensorReading(105)]
device = Device(readings)
critical = device.get_critical_readings(100)
print(critical) # Expected: [SensorReading(101), SensorReading(105)]
print(device.readings) # Expected: [SensorReading(98), SensorReading(101), SensorReading(105)]

# Example 2

device = Device([SensorReading(10), SensorReading(20)])
critical = device.get_critical_readings(100)
print(critical) # Expected: []

# Common Wrong Output Example​:

readings = [SensorReading(98), SensorReading(101), SensorReading(105)]
device = Device(readings)
critical = device.get_critical_readings(100)
print(critical) # Plausible: [SensorReading(101), SensorReading(105)]
# Wrong if the method mutates the device's internal list
print(device.readings) # Wrong: [SensorReading(101), SensorReading(105)]
```

<details> 
<summary>Hidden Trap</summary> 
Mutating and returning internal state.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 9 (4 minutes)

Description​​: Create a `Project` class that is initialized with a list of `Member` objects. The `Project` must store its own independent list of members. Changes made to the list of members provided during initialization must not affect the project's internal list of members after the project has been created.

```python
# Provided class
class Member:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Member('{self.name}')"
```

```python
# Correct I/O Example 1
initial_members = [Member("Alice"), Member("Bob")]
project = Project(initial_members)
initial_members.pop()
print(project.members) # Expected: [Member('Alice'), Member('Bob')]

# Example 2
core_team = [Member("Charlie")]
project = Project(core_team)
core_team.append(Member("David"))
print(project.members) # Expected: [Member('Charlie')]

# Common Wrong Output Example​​:

initial_members = [Member("Alice"), Member("Bob")]
project = Project(initial_members)
initial_members.pop()
print(project.members) # Wrong: [Member('Alice')]
```


<details> 
<summary>Hidden Trap</summary> 
Constructor stores a mutable reference.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 10 (5 minutes)

Description​​: Create a `Playlist` class that stores a list of song title strings. Implement the in-place addition operator (+=) to append a list of new songs to the playlist. This operation must modify the existing `Playlist` object directly and not create a new one.

```python
# Correct I/O Example 1

playlist = Playlist(["Song A", "Song B"])
id_before = id(playlist.songs)
playlist += ["Song C"]
id_after = id(playlist.songs)
print(playlist.songs) # Expected: ['Song A', 'Song B', 'Song C']
print(id_before == id_after) # Expected: True

# Example 2
p = Playlist([])
id_before = id(p.songs)
p += ["X", "Y"]
id_after = id(p.songs)
print(id_before == id_after) # Expected: True

# Common Wrong Output Example​​:

playlist = Playlist(["Song A", "Song B"])
id_before = id(playlist.songs)
playlist += ["Song C"]
id_after = id(playlist.songs)
print(playlist.songs) # Plausible: ['Song A', 'Song B', 'Song C']
print(id_before == id_after) # Wrong: False
```

<details> 
<summary>Hidden Trap</summary> 
Creating new list vs extending original.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 11 (6 minutes)

Description​​: Create an immutable `Route` class that stores a sequence of waypoints (strings) in a tuple. Implement the addition operator (`+`) to combine two Route objects into a new `Route` object. Ensure the in-place addition operator (`+=`) also results in a new `Route` object by correctly delegating to the `__add__` method.

```python
# Correct I/O Example 1
route1 = Route(("A", "B"))
id_before = id(route1)
route1 += Route(("C",))
id_after = id(route1)
print(route1.waypoints) # Expected: ('A', 'B', 'C')
print(id_before != id_after) # Expected: True

# Common Wrong Output Example​​:

route1 = Route(("A", "B"))
id_before = id(route1)
route1 += Route(("C",))
id_after = id(route1)
print(route1.waypoints) # Plausible: ('A', 'B', 'C')
print(id_before != id_after) # Wrong: False
```

<details> 
<summary>Hidden Trap</summary> 
Implicit += must create new object.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>



### Drill 12 (4 minutes)

Description​​: Create a Meeting class initialized with a topic string and a list of Attendee objects. Implement the `__repr__` method to return a developer-friendly string like `Meeting(topic='...', attendees=[Attendee('name1'), Attendee('name2')])`.

```python
# Provided class
class Attendee:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Attendee('{self.name}')"
```

```python
# Correct I/O Example 1
a1 = Attendee("Alice")
a2 = Attendee("Bob")
meeting = Meeting("Planning", [a1, a2])
print(repr(meeting))
# Expected: "Meeting(topic='Planning', attendees=[Attendee('Alice'), Attendee('Bob')])"

# Common Wrong Output Example​​:

a1 = Attendee("Alice")
a2 = Attendee("Bob")
meeting = Meeting("Planning", [a1, a2])
# Wrong if collaborators are not represented correctly
print(repr(meeting))
# Wrong: "Meeting(topic='Planning', attendees=[<__main__.Attendee object at ...>, <__main__.Attendee object at ...>])"
```

<details> 
<summary>Hidden Trap</summary> 
Container repr needs collaborator repr.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 13 (3 minutes)

Description​​: Create a `Toolbox` class that stores a list of tool name strings. Implement the necessary magic method so that when Python's built-in len() function is called on a `Toolbox` instance, it returns the number of tools in the box.

```python
# Correct I/O Examples​​:

# Example 1
box = Toolbox(["hammer", "screwdriver"])
print(len(box)) # Expected: 2

# Example 2
empty_box = Toolbox([])
print(len(empty_box)) # Expected: 0

# Common Wrong Output Example​​:

box = Toolbox(["hammer", "screwdriver"])
# This would raise a TypeError: object of type 'Toolbox' has no len()
# print(len(box))
# A common incorrect implementation might be a different method name
# print(box.get_length()) # Wrong approach
```

<details> 
<summary>Hidden Trap</summary> 
Protocol delegation via magic method.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>



### Drill 14 (6 minutes)

Description​​: An `Envelope` class contains a single Document object. Two `Envelope` objects are considered equal if their contained Document objects are equal. The Document class determines its equality based on version_id. Implement `__eq__` on `Envelope` to correctly delegate the comparison.

```python
# Provided class
class Document:
    def __init__(self, version_id, content):
        self.version_id = version_id
        self.content = content
    def __eq__(self, other):
        return (isinstance(other, Document) and
                self.version_id == other.version_id)
```

```python
# Correct I/O Example 1

doc1 = Document(1, "Content A")
doc2 = Document(1, "Content B") # Same ID, different content
env1 = Envelope(doc1)
env2 = Envelope(doc2)
print(env1 == env2) # Expected: True

# Example 2
doc3 = Document(2, "Content A")
env3 = Envelope(doc3)
print(env1 == env3) # Expected: False

# Common Wrong Output Example​​:

doc1 = Document(1, "Content A")
doc2 = Document(1, "Content B")
env1 = Envelope(doc1)
env2 = Envelope(doc2)
# Wrong if comparison is by identity (`is`)
print(env1 == env2) # Wrong: False
```

<details> 
<summary>Hidden Trap</summary> 
Re-implementing logic instead of delegating comparison.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 15 (5 minutes)

Description​​: Create a `LogFile` class that stores log entries in a list. The class must be iterable, allowing a for loop to iterate directly over the `LogFile` object to retrieve each log entry string one by one. Do this by implementing `__getitem__`.

```python
# Correct I/O Example 1:

log = LogFile(["INFO: start", "WARN: timeout", "INFO: end"])
output = []
for entry in log:
    output.append(entry)
print(output) # Expected: ['INFO: start', 'WARN: timeout', 'INFO: end']

# Common Wrong Output Example​​:

log = LogFile(["INFO: start"])
# A common error would be for __getitem__ to return the whole list,
# causing an infinite loop or TypeError in the for loop.
# Or, if not implemented, a TypeError: 'LogFile' object is not iterable
```

<details> 
<summary>Hidden Trap</summary> 
Iteration protocol fallback to `__getitem__`.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Drill 16 (7 minutes)

Description​​: A `Ledger` class stores a list of `Transaction` objects. Implement a method `get_total()` on `Ledger` that returns the sum of all transaction amounts. This method must delegate the job of providing an amount to each individual `Transaction` object.

```python
# Provided class
class Transaction:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f"Transaction({self.amount})"
```

```python

# Correct I/O Example 1
ledger = Ledger([Transaction(50), Transaction(-20), Transaction(100)])
print(ledger.get_total()) # Expected: 130

# Example 2
ledger = Ledger([Transaction(-10), Transaction(-15)])
print(ledger.get_total()) # Expected: -25

# Example 3
ledger = Ledger([])
print(ledger.get_total()) # Expected: 0


# Common Wrong Output Example​​:

ledger = Ledger([Transaction(50), Transaction(-20)])
# Attempting to sum the objects directly would cause a TypeError
# print(ledger.get_total()) # Wrong: TypeError: unsupported operand type(s) for +: 'int' and 'Transaction'
```

<details> 
<summary>Hidden Trap</summary> 
Aggregating collaborator states versus objects.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

 