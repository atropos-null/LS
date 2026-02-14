# PY129 LSBOT Prep Questions

## Pass 6

Prompt:

For {TOPIC}, generate 3 advanced Launch-School–style assessment prompts starting at PY129:
	1.	Predict & explain a short code snippet’s output
	2.	Debug a short snippet (state intended behavior)
	3.	Implement a small function or class with 3 I/O examples

Avoid canonical examples; prefer composition or object collaboration contexts.

Name the hidden trap each prompt is targeting.

Keep each under ~25 lines. No solutions or hints. At least one prompt must rely on a reasonable but incorrect assumption about a protocol or operator.

### Problem 1: Playlist Class

**Description**: Create a `Playlist` class that represents a music playlist. The class should be able to store and manage a collection of song titles.

Initialization:

* The `__init__` method should accept one required argument: the name of the playlist (a string).
* It should also accept an optional argument, songs, which is a list of initial song titles (strings). If not provided, the playlist should start empty.
* The `Playlist` object should maintain the state of the songs in the order they are in the list.


**Methods**:

* `add_song(song_title)`: Adds a new song title (string) to the end of the playlist.
* `now_playing()`: Returns the title of the current song. When a playlist is first created, the "current song" is the first song in the list. If the playlist is empty, this method should return None.
* `play_next()`: Advances to the next song in the playlist. The "current song" becomes the next one in the list. If the current song is the last one in the list, this method should loop back to the first song. If the playlist is empty, this method does nothing.

Inputs:
```python
# Input
    rock_hits = Playlist("Rock Hits", ["Stairway to Heaven", "Bohemian Rhapsody"])
    print(rock_hits.now_playing())
    rock_hits.play_next()
    print(rock_hits.now_playing())
    rock_hits.add_song("Hotel California")
    rock_hits.play_next()
    print(rock_hits.now_playing())

    # Output
    #Stairway to Heaven
    #Bohemian Rhapsody
    #Hotel California
```

```python
# Input
    favorites = Playlist("Favorites", ["Song A", "Song B"])
    favorites.play_next()
    print(favorites.now_playing())
    favorites.play_next() # Should loop back to the start
    print(favorites.now_playing())

    # Output
    Song B
    Song A
```
```python
# Input
    empty_playlist = Playlist("Empty")
    print(empty_playlist.now_playing())
    empty_playlist.play_next()
    print(empty_playlist.now_playing())
    empty_playlist.add_song("First Song")
    print(empty_playlist.now_playing())

    # Output
    None
    None
    First Song
```

Common Wrong Turns:

1. Using a mutable default argument (like `songs=[]`) in the `__init__` method signature, which can cause unexpected behavior where all playlists share the same initial song list.
2. Incorrectly managing the index for the current song, leading to `IndexError` or improper looping logic.

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 2: InventoryItem Class​*

**Description**: Design an InventoryItem class to represent an item in a store's inventory. Each item has a name, price, and quantity.

**Initialization (`__init__`)**:

1. The initializer must accept three arguments: name (string), price (float or integer), and quantity (integer).
2. During initialization, the method must perform the following validations:
    •   The price cannot be negative.
    •   The quantity cannot be negative.
3. If any of the validation checks fail, the initializer should raise a `ValueError` with an appropriate error message.
4. If validation passes, the initializer should set the corresponding instance variables.

Methods:

* `get_total_value()`: Returns the total value of the inventory item, calculated as price * quantity.
*  `__str__()`: Returns a user-friendly string representation of the item in the format: `"{name} - Price: ${price:.2f}, Quantity: {quantity}"`. The price should always be formatted to two decimal places.

I/O Examples:

1.  ​Successful instantiation and usage:
```   
 # Input
    item = InventoryItem("Laptop", 1200.50, 10)
    print(item)
    print(item.get_total_value())

    # Output
    Laptop - Price: $1200.50, Quantity: 10
    12050.0
```

 2.  ​Instantiation with invalid price:
 
 ```
 # Input
    try:
        item = InventoryItem("Keyboard", -50, 25)
    except ValueError as e:
        print(e)

    # Output
    Price cannot be negative.
```

3.  ​Instantiation with invalid quantity:
```
# Input
    try:
        item = InventoryItem("Mouse", 25, -5)
    except ValueError as e:
        print(e)

    # Output
    Quantity cannot be negative.
```    

**Common Wrong Turns**:

1.  Failing to raise a `ValueError`. Instead, some might print an error message or return `None`, which does not correctly prevent the object from being created in an invalid state.
2.  Implementing validation in separate methods instead of directly within `__init__`, which allows an invalid object to be created before the validation methods are called.

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 3: Initiation and `__init__`: Predict and Explain

Predict the output of the following code. Explain your prediction in detail, referencing the Python object model and instantiation process.

```python
class Document:
    def __init__(self, text):
        self.text = text

class Index:
    def __init__(self, name, document):
        self.name = name
        self.docs = [document]
        print(f"Index '{self.name}' created.")
        return self.docs

try:
    doc = Document("Python is a fun language.")
    idx = Index("Programming", doc)
    print(idx)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
```

<details> 
<summary>Hidden Trap</summary> 
Hidden trap is that `__init__` must return `None`, not a value. The constructor call will raise a `TypeError`.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 4: Debug the Code

The following code is intended to create a Dashboard that pulls a metric from a DataService. When dashboard.display_metric() is called, it should print the metric string provided by the service. However, the code raises an error. Identify the bug, explain why it occurs, and provide the corrected code.

Intended Behavior:

```python
# Expected output:
#
# Dashboard ready.
# Current Users: 541
```

Code with bug:
```python
class DataService:
    def get_metric(self):
        return "Current Users: 541"

class Dashboard:
    def __init__(self):
        self.service = DataService
        print("Dashboard ready.")

    def display_metric(self):
        metric = self.service.get_metric()
        print(metric)

dashboard = Dashboard()
dashboard.display_metric()
```


<details> 
<summary>Hint</summary> 
Internal Note: Hidden trap is the confusion between a class and an instance. `self.servic`e is assigned the DataService class, not an instance of it, causing a `TypeError` when the instance method `get_metric` is called on the class.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 5: Implement a Class

(Difficulty: Advanced)

You are given Engine and Wheel classes. Implement a Car class whose constructor accepts one Engine object and a list of four Wheel objects.

The Car instance should have an attribute description that is set during initialization.[10:36 AM]The description should be a string in the format: "A car with a X-horsepower engine and Y-inch wheels.", where X is the engine's horsepower and Y is the diameter of the first wheel in the list.

Provided Classes:

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheel:
    def __init__(self, diameter):
        self.diameter = diameter
 ```

 Examples:
 ```python
 # Example 1
engine1 = Engine(300)
wheels1 = [Wheel(18), Wheel(18), Wheel(18), Wheel(18)]
car1 = Car(engine1, wheels1)
print(car1.description)
# Expected Output: A car with a 300-horsepower engine and 18-inch wheels.

# Example 2
engine2 = Engine(550)
wheels2 = [Wheel(20), Wheel(20), Wheel(20), Wheel(20)]
car2 = Car(engine2, wheels2)
print(car2.description)
# Expected Output: A car with a 550-horsepower engine and 20-inch wheels.

# Example 3
engine3 = Engine(180)
wheels3 = [Wheel(16), Wheel(16), Wheel(16), Wheel(16)]
car3 = Car(engine3, wheels3)
print(car3.description)
# Expected Output: A car with a 180-horsepower engine and 16-inch wheels.
```


<details> 
<summary>Hint</summary> 

Internal Note: Hidden trap involves correctly accessing attributes of collaborator objects (`engine.horsepower`, `wheels[0].diameter`) within the ``__init__`` method to compose a new piece of state for the Car instance.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 6: Predict and Explain Output

Predict the output of the following code and explain why it produces that output. Your explanation should cover the roles of class and instance variables, and how attribute lookup works in the context of collaborator objects.

**class Template:**
```python
    style = 'Standard'

    def __init__(self, template_text):
        self.template_text = template_text

    def render(self, value):
        return f"{self.template_text}: {value} ({self.style})"

class Report:
    style = 'Brief'

    def __init__(self, text):
        self.text = text
        self.formatter = Template(text)

    def generate(self):
        # Is self.formatter.style the same as self.style?
        return self.formatter.render('Data')

report = Report("Sales Data")
print(report.generate())
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Attribute lookup on a collaborator object. Students might mistakenly think that `self.style` inside the Template.render method refers to the Report class's style attribute since the Template object is an instance variable of Report. The lookup, however, is confined to the Template instance (`self.formatter`) and its class.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 7: Debug the Code

The `DeviceManager` class is intended to track the total number of connected devices across all manager instances. However, the code below is not working as expected. Each manager seems to have its own independent count. Identify the bug, explain the flaw in its logic, and provide the corrected code.

Intended Behavior:
```python
manager1 = DeviceManager("Office")
manager1.add_device()
manager1.add_device()

manager2 = DeviceManager("Home")
manager2.add_device()

print(DeviceManager.device_count) # Expected: 3
print(manager1.device_count)       # Expected: 3
print(manager2.device_count)       # Expected: 3
```
Buggy Code:

```python
class DeviceManager:
    device_count = 0

    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self):
        self.device_count += 1 # This line is the problem
        self.devices.append(f"Device_{self.device_count}")
        print(f"{self.name} added a device. " \
              f"Total devices: {self.device_count}")

manager1 = DeviceManager("Office")
manager1.add_device() # Office added a device. Total devices: 1
manager1.add_device() # Office added a device. Total devices: 2

manager2 = DeviceManager("Home")
manager2.add_device() # Home added a device. Total devices: 1

print(DeviceManager.device_count) # Prints 0
```


<details> 
<summary>Hint</summary> 

Hidden Trap:​ The rebinding behavior of the `+=` operator on immutable types. When `self.device_count += 1 `is executed, it doesn't modify the class variable device_count. Instead, it creates a ​new instance variable​ named device_count on self that shadows the class variable. Subsequent access to `self.device_count` within that instance refers to the instance variable, not the shared class variable.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 8: Implement a Class

Implement a `Project` class that collaborates with `Task` objects. The `Project` class must have a class-level priority set to '`Low'`. An individual project instance can override this with its own priority level during initialization.

Create a `log_task` method that accepts a `Task` object. This method should return a string formatted as "`[PRIORITY] Project 'Project Name': Task 'Task Name'"` where [PRIORITY] is the project's instance-level priority if it exists, otherwise it defaults to the class-level priority.

Requirements:

1.  Project class with a class attribute priority = 'Low'.
2.  `__init__` method that accepts a name and an optional priority.
3.  `log_task` method that takes a `Task` object and returns the formatted log string.
4.  A simple `Task` class is provided for you.

Provided Code:

```python
class Task:
    def __init__(self, name):
        self.name = name


Examples:

# Your Project class implementation here

# --- Examples ---
task1 = Task("Review specifications")
task2 = Task("Deploy to production")

default_project = Project("Internal Tool")
urgent_project = Project("Client Hotfix", priority="High")

print(default_project.log_task(task1))
# Expected Output: [Low] Project 'Internal Tool': Task 'Review specifications'

print(urgent_project.log_task(task2))
# Expected Output: [High] Project 'Client Hotfix': Task 'Deploy to production'

print(default_project.priority)
# Expected Output: Low (accesses class attribute)
```



<details> 
<summary>Hint</summary> 

Hidden Trap:​ Incorrect assumption about attribute lookup fallback. A common mistake is to only access self.priority and assume it will automatically fall back to `Project.priority` if the instance attribute isn't set. While this is true for ​reading​ the attribute, the prompt's logic requires determining ​which​ priority to use explicitly. The most direct implementation requires checking for the instance attribute first and then accessing the class attribute (`self.__class__.priority`) as a fallback if it doesn't exist.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 9: Predict and Explain

Predict the output of the following code. Explain precisely why this output occurs, paying close attention to the roles of `cls` and `self` in the context of inheritance and collaboration.

```python
class Registry:
    _items = []

    @classmethod
    def register(cls, item):
        print(f"Registering to {cls.__name__}'s registry.")
        cls._items.append(item)

class Part(Registry):
    pass

class Product(Registry):
    pass

class Factory:
    def __init__(self, item_class):
        self.item_class = item_class

    def create_item(self, name):
        item = f"{self.item_class.__name__}: {name}"
        self.item_class.register(item)
        return item

part_factory = Factory(Part)
part_factory.create_item("Gear")

product_factory = Factory(Product)
product_factory.create_item("Robot")

print(Part._items)
```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted: Misunderstanding how a shared class-level attribute behaves when manipulated through different subclasses.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>) 

### Problem 10: Debug This Snippet

The `APIConnector` class is intended to connect to a service using settings provided by a Settings object. The `build_url` static method is a utility to construct a full URL from an endpoint. However, running this code raises an error. Identify the bug, explain the flawed assumption the original developer made, and rewrite the `APIConnector` class to fix it. The `build_url` method must remain a static method.

```python
class Settings:
    def __init__(self, base_url):
        self.base_url = base_url

class APIConnector:
    def __init__(self, settings):
        self.settings = settings

    @staticmethod
    def build_url(endpoint):
        # Intended behavior: return a URL like "https://api.example.com/users"
        base = self.settings.base_url
        return f"{base}/{endpoint}"

    def get_users(self):
        url = self.build_url("users")
        # ... logic to fetch data from url
        print(f"Fetching from: {url}")

config = Settings("https://api.example.com")
connector = APIConnector(config)
connector.get_users()
```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted: Incorrectly assuming a static method has access to the instance's context (self) or its attributes.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 11: Implement This Class

Implement a `FileAuditor` class that tracks file access events. The class must meet the following requirements:

* It is initialized with a filename (e.g., 'data.csv').
* An instance method `log_access(user)` adds a log entry for that specific file instance.
* A class method get_total_logs(returns an integer representing the total number of logs created across ​all​ `FileAuditor` instances.
* A `__str__` magic method that returns a formatted string for an instance, like 'Auditor for: data.csv'. This method must use a static helper method named `_format_report_name(name)` to generate the string.


```python
# Example Input/Output:

auditor1 = FileAuditor('document1.txt')
auditor1.log_access('user_a')
auditor1.log_access('user_b')

auditor2 = FileAuditor('document2.txt')
auditor2.log_access('user_c')

print(FileAuditor.get_total_logs())
# Expected Output: 3

print(auditor1)
# Expected Output:
# Auditor for: document1.txt

print(auditor2)
# Expected Output:
# Auditor for: document2.txt

```
<details> 
<summary>Hint</summary> 
Hidden Trap Targeted: Confusion about how to correctly invoke a static method from within an instance method (`__str__`) and managing both class and instance state simultaneously.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 12: Predict and Explain​*

Predict the output of the following code snippet and explain your reasoning, paying close attention to how attributes are handled and how state is shared or separated between objects.

```python
class Inventory:
    items = []

    def __init__(self, location):
        self.location = location

    def add_stock(self, item):
        self.items.append(item)

warehouse = Inventory('Warehouse')
store = Inventory('Store')

warehouse.add_stock('Laptop')
store.add_stock('Mouse')

print(f"Warehouse has: {warehouse.items}")
print(f"Store has: {store.items}")
```

<details> 
<summary>Hint</summary> 
Hidden Trap:​ Mutable Class Attributes vs. Instance Attributes.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 13: Debugging​

The following code is intended to allow a `Portfolio` to track the tasks of a `Project`. When a task is added to the `Project` via the `Portfolio`'s `add_task` method, the `Portfolio`'s view of the tasks (`portfolio.project_tasks`) should be updated. However, the code is buggy. Identify the bug, explain why the final state is incorrect, and describe how to fix it.

Intended Behavior:​ The final line should print `['Login Page']`, showing that the portfolio's reference to the project's tasks reflects the new addition.

```python
class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

class Portfolio:
    def __init__(self, project):
        self.project_tasks = project.tasks

    def add_task(self, project, task):
        # This line is buggy
        project.tasks = project.tasks + [task]

# --- Execution ---
p1 = Project("Website Redesign")
portfolio = Portfolio(p1)
portfolio.add_task(p1, "Login Page")

print(f"Project's tasks: {p1.tasks}")
print(f"Portfolio's tasks: {portfolio.project_tasks}")

```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Incorrect assumption that the `+` operator for lists mutates the left operand. This leads to attribute reassignment (`=`), which breaks the reference held by the collaborator object, rather than mutating the original object's state.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 14: Implementation​

Implement two classes, `ServiceLog` and `Car`. A `Car` instance is composed with a ServiceLog instance upon creation. The `Car` class must have a `drive(km)` method and a `service()` method.

* The drive method adds the kilometers driven to the car's total mileage.
* The service method logs the car's current mileage to its ServiceLog by calling the log's record_service method.
* The ServiceLog should store a list of these mileage logs.

Examples:
```python
#​Input:

log = ServiceLog()
car = Car(log)
car.drive(100)
car.service()
print(log.records)

#​Output: [100]
# Input:
log = ServiceLog()
car = Car(log)
car.drive(50)
car.drive(75)
car.service()
car.drive(25)
print(log.records)
print(car.mileage)
      
 #​Output: 
 # [125]
 # 150
    
 # Input:
log = ServiceLog()
car = Car(log)
car.service()
car.drive(30)
car.service()
car.drive(40)
car.service()
print(log.records)

#​Output: [0, 30, 70]
```    

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Correctly managing state through object collaboration, where one object (`Car`) is responsible for triggering state changes in a separate, contained object (`ServiceLog`).
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 15: Predict and Explain

Predict the output of the following code and explain your reasoning. Your explanation should detail how attribute lookup works, paying special attention to `self.__class__` and its role in accessing the nested `Config` class.

```python
class BaseWorker:
    class Config:
        priority = 'NORMAL'

    def display_priority(self):
        # Accesses the Config class via the instance's class
        print(self.__class__.Config.priority)

class UrgentWorker(BaseWorker):
    class Config:
        priority = 'HIGH'

worker = UrgentWorker()
worker.display_priority()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The `self.__class__` Late Binding Trap. When a method defined in a superclass is called on a subclass instance, `self.__class__` resolves to the subclass, not the superclass where the method is defined. This leads to accessing the subclass's version of the class attribute.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 15: Debugging

The `Scheduler` class uses a `Task` collaborator object. The class method `Scheduler.validate_task_class` is intended to check if a given task instance was created from the scheduler's ​default​ `Task` class (DefaultTask). However, the current implementation is flawed and produces an incorrect result. Identify the bug, explain why the comparison fails, and provide the corrected code.

**Intended Behavior**:

The code should print `False`, because `urgent_task` is an instance of `UrgentTask`, not `DefaultTask`. Instead, it currently prints `True`.

```python
class DefaultTask:
    pass

class UrgentTask:
    pass

class Scheduler:
    # This should store the class, but is storing an instance
    default_task_type = DefaultTask()

    @classmethod
    def validate_task_class(cls, task_instance):
        # Buggy line
        is_default = task_instance.__class__ is not cls.default_task_type
        print(not is_default)

# Setup
urgent_task = UrgentTask()
Scheduler.validate_task_class(urgent_task)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The `is` vs. `__class__` Identity Trap. The programmer incorrectly assumes that comparing `task_instance.__class__` with `cls.default_task_type` using is not will always work as intended. While it might work in simple cases, the real protocol for type checking is using `isinstance()` or direct class comparison (`__class__ == ...`). The bug here is that `cls.default_task_type` is actually an ​instance​ of the `DefaultTask`, not the class itself, so `task_instance.__class__` is being compared to an object, which is logically incorrect.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 16: Implementation

Implement the Document class according to the following requirements. It must track the total number of `Document` instances created using a class attribute. It must also support a "versioning" system via an instance method, `create_new_version()`, which returns a new document of the ​exact same class​ as the instance the method was called on. This behavior must be preserved in any subclasses.

Requirements:

1.  A class attribute count that is incremented each time a new instance of that specific class is created.
2.  An `__init__` method that properly increments the counter.
3.  An instance method `create_new_version(self)` that returns a new instance of the correct class.

Examples:

```python

# Example 1: Base class functionality
doc1 = Document()
doc2 = doc1.create_new_version()
print(f"Document count: {Document.count}")
# Expected: Document count: 2
print(f"doc2 is a Document: {isinstance(doc2, Document)}")
# Expected: doc2 is a Document: True

# Example 2: Subclass functionality
class SignedDocument(Document):
    count = 0 # Subclass gets its own counter

signed_doc1 = SignedDocument()
signed_doc2 = signed_doc1.create_new_version()
print(f"SignedDocument count: {SignedDocument.count}")
# Expected: SignedDocument count: 2
print(f"Base document count is unchanged: {Document.count}")
# Expected: Base document count is unchanged: 2
print(f"signed_doc2 is a SignedDocument: {isinstance(signed_doc2, SignedDocument)}")
# Expected: signed_doc2 is a SignedDocument: True
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The Hardcoded Constructor Trap. A naive implementation of create_new_version might hardcode return `Document()`. This would fail the requirement for subclasses, as calling `create_new_version()` on a `SignedDocumen`t instance would incorrectly return a Document instance, and it would increment the wrong counter. The solution requires using `self.__class__()` to instantiate the new object.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 17: Predict and Explain Output​

Predict the output of the following Python code snippet. Explain step-by-step why the output is what it is, paying close attention to how the `system.component_status` property interacts with the `Component` object and influences the system.readiness property.

```python
class Component:
    def __init__(self, status='offline'):
        self._status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status

class System:
    def __init__(self):
        self._component = Component()

    @property
    def readiness(self):
        return f"System readiness: {self._component.status}"

    @property
    def component_status(self):
        return self._component.status

    @component_status.setter
    def component_status(self, new_status):
        self._component.status = new_status

system = System()
print(system.readiness)

system.component_status = 'online'
print(system.readiness)
```

<details> 
<summary>Hint</summary> 


Hidden Trap Targeted:​ This prompt targets the misunderstanding that properties only manage an object's immediate instance variables. Here, a property setter on the System object acts as an interface to modify the state of a separate, internal collaborator object (`_component`).

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 18: Debugging​

The code below is intended to create a `Report` class that collaborates with a `Log` object. Every time the `report.content` is updated, the change should be automatically recorded in `report.log.entries`. However, running the code raises a `RecursionError`. Identify the bug, explain its cause, and provide the corrected Report class definition.

Intended Behavior:

* A Report object is initialized with some content. This first assignment is logged.
* When report.content is reassigned, the new content is stored, and a new entry is added to the log.
* The final print statement should output ['Content updated to: "Initial report."', 'Content updated to: "Revised report."'].

```python
# BUGGY CODE
class Log:
    def __init__(self):
        self.entries = []

    def add_entry(self, data):
        self.entries.append(data)

class Report:
    def __init__(self, initial_content):
        self.log = Log()
        self.content = initial_content

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, new_content):
        self.log.add_entry(f'Content updated to: "{new_content}"')
        self.content = new_content

report = Report("Initial report.")
report.content = "Revised report."
print(report.log.entries)
```

<details> 
<summary>Hint</summary> 


Hidden Trap Targeted:​ This prompt targets the common mistake of causing infinite recursion within a property. The incorrect assumption is that assigning to `self.content` inside the setter will behave like a normal attribute assignment, when in fact it re-invokes the setter method itself.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 19: Implementation​*

Implement a class named `ManagedResource`. This class must collaborate with a Settings object, which is passed during instantiation. The `Settings` class is provided for you.

Your `ManagedResource` class must have a host property that provides a getter and setter interface for the 'host' key within its Settings collaborator's config dictionary.

* The host getter should retrieve the value of 'host' from the Settings object's config dictionary.
* The host setter must validate that the new value is a string containing at least one dot (`.`). If validation fails, it must raise a `ValueError`. If validation passes, it should update the value of 'host' in the Settings object's config dictionary.

```python
# Provided class - DO NOT MODIFY
class Settings:
    def __init__(self, initial_config):
        self.config = initial_config

    def get(self, key):
        return self.config.get(key)

# Your implementation of ManagedResource goes here

# --- Input/Output Examples ---
# Example 1
settings1 = Settings({'host': 'localhost', 'port': 8080})
resource1 = ManagedResource(settings1)
resource1.host = 'api.example.com'
print(resource1.host)          # Expected: api.example.com
print(settings1.get('host'))   # Expected: api.example.com

# Example 2
settings2 = Settings({'host': 'server1'})
resource2 = ManagedResource(settings2)
try:
    resource2.host = 'invalid-host'
except ValueError:
    print("ValueError caught!") # Expected: ValueError caught!
print(resource2.host)          # Expected: server1

# Example 3
settings3 = Settings({'host': 'db.internal.net'})
resource3 = ManagedResource(settings3)
print(resource3.host)          # Expected: db.internal.net
```


<details> 
<summary>Hint</summary> 

Hidden Trap Targeted:​ This prompt targets the failure to correctly delegate state management to a collaborator. A common mistake is to create a backing instance variable (e.g., `_host`) on the `ManagedResource` instance itself, rather than modifying the dictionary within the shared `Settings` object as required. The I/O examples verify that the collaborator's state is the one being changed.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 20: Predict and Explain Code Output


Predict the output of the following code snippet. Provide a detailed explanation for each line of output, focusing on how inheritance and name mangling affect attribute access.

```python
class Component:
    def __init__(self):
        self.__id = 'C-123'

    def get_id(self):
        return self.__id

class System(Component):
    def __init__(self):
        super().__init__()
        self.__id = 'S-456'

    def get_component_id(self):
        return super().get_id()

    def get_system_id(self):
        return self.__id

sys = System()
print(sys.get_component_id())
print(sys.get_system_id())
print(sys._System__id)
print(sys._Component__id)
```
<details> 
<summary>Hint</summary> 

Hidden Trap Targeted​: This prompt targets the misconception that a double-underscore attribute in a subclass overrides the one in its parent class. Due to name mangling, `System.__id` and `Component.__id` become distinct attributes (`_System__id` and `_Component__id`) on the sys instance, coexisting without collision.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 21: Debug Code


The following code is intended to allow the addition of two `Wallet` objects using the `+` operator. The expected behavior is for the final line to print `Wallet` with balance: `350`. However, the line `combined_wallet = wallet1 + wallet2` currently raises a `TypeError`. Identify the bug and provide the corrected code.

```python
# Intended behavior: The code should add the balances of two
# Wallet objects using the `+` operator and print the new
# wallet's representation, which should be "Wallet with balance: 350".

class Wallet:
    def __init__(self, amount):
        self._balance = amount

    # This method is intended to overload the `+` operator.
    def __add__(self, other):
        return Wallet(self._balance + other._balance)

    def __repr__(self):
        return f"Wallet with balance: {self._balance}"

wallet1 = Wallet(100)
wallet2 = Wallet(250)

# This line raises a TypeError. Fix the Wallet class.
combined_wallet = wallet1 + wallet2
print(combined_wallet)

```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted​: This prompt exploits the reasonable but incorrect assumption that all methods starting and ending with double underscores (dunder methods) are subject to name mangling. Python's data model hooks (special methods like `__add__` and `__repr__`) are looked up by the interpreter by their exact names and are exempt from mangling. The bug is naming the method `__add__`, which gets mangled to `_Wallet__add__`, a name the `+` operator does not look for.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 22: Implement a Class

Implement the `AccessLogger` class based on its usage within the `APIClient` class. Your implementation must ensure the provided example code runs without errors and produces the exact output shown. The `APIClient` and `AccessLogger` classes have a composition relationship.

```python
class APIClient:
    def __init__(self, logger):
        self._logger = logger # Has-a relationship

    def make_request(self, url):
        self._logger.log_access(url)
        print(f"Request to {url} successful.")

        # This MUST access the logger's name-mangled attribute.
        count = self._logger._AccessLogger__requests_count
        print(f"Total requests logged: {count}")

# Implement the AccessLogger class below this line.
# It must have:
# 1. An initializer that accepts a filename.
# 2. An attribute for the filename that is accessible externally.
# 3. A private counter for requests that is accessed by APIClient.
# 4. A method to log access attempts.



# Example Usage:
logger = AccessLogger("system.log")
client = APIClient(logger)

client.make_request("api/users")
# Expected Output:
# Attempting to access: api/users
# Request to api/users successful.
# Total requests logged: 1

client.make_request("api/data")
# Expected Output:
# Attempting to access: api/data
# Request to api/data successful.
# Total requests logged: 2

print(logger._log_file)
# Expected Output:
# system.log
```

<details> 
<summary>Hint </summary> 

Hidden Trap Targeted​: This prompt forces the developer to deduce the required attribute names and protection levels from a collaborating object's implementation. The `APIClient`'s direct access to `_AccessLogger__requests_count` dictates that the logger's attribute must be named `__requests_count`. Likewise, the direct access to `logger._log_file `dictates that this attribute must be named `_log_file`, testing the understanding of both conventions in a practical context.
</details>

### Problem 23: Predict Code Output

Predict the output of the following code. Explain precisely what happens when `processor.process_all()` is called and why that output is produced.

```python
class Report:
    def __init__(self, content):
        self._content = content

    def __format(self):
        return f"Report content: {self._content}"

class Logger:
    def process_all(self, reports):
        for report in reports:
            try:
                # Intended to call a private formatting method
                print(report.__format())
            except Exception as e:
                print(f"{type(e).__name__}: {e}")

report1 = Report("Annual data.")
report2 = Report("Quarterly data.")
processor = Logger()
processor.process_all([report1, report2])
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Name Mangling. Python's name mangling (_ClassName__methodName) prevents an external object (Logger) from accessing a "private" method of another object (Report) using the double underscore syntax directly.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 24: Debug Code

The `EventBroadcaster` is intended to send notifications from various sources (`EmailSource`, `SMSSource`) by calling a notify interface on them. The current code fails with a TypeError when processing the `SMSSource`. Identify the bug in the `SMSSource` class, explain why it breaks the polymorphic interface, and provide a corrected version of that class only.

Intended Behavior:
* Calling `broadcaster.broadcast()` should print:
    * Emailing: User subscribed 
    * Texting: Your code is 1234

```python
class EmailSource:
    def notify(self, message):
        print(f"Emailing: {message}")

class SMSSource:
    @property
    def notify(self): # BUG IS HERE
        return lambda message: print(f"Texting: {message}")

class EventBroadcaster:
    def __init__(self, sources):
        self.sources = sources
        self.messages = ["User subscribed", "Your code is 1234"]

    def broadcast(self):
        for source, msg in zip(self.sources, self.messages):
            source.notify(msg)

sources = [EmailSource(), SMSSource()]
broadcaster = EventBroadcaster(sources)
broadcaster.broadcast()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Confusing a property with a method. The @property decorator makes notify an attribute that returns a lambda function, but it is not a directly callable method on the instance itself. The broadcaster calls `source.notify(msg)`, which fails because it tries to pass an argument to a property accessor, not a method.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 25: Implement a Class

Implement an Inventory class that manages a collection of items.

* The constructor should accept a dictionary where keys are item names (strings) and values are quantities (integers).
* The class must support the `+` operator to combine two Inventory objects.
* The result should be a ​new​ Inventory object.
* When combining, if an item exists in both inventories, their quantities should be summed.

Examples:
```python
# Example 1
inv1 = Inventory({'screws': 100, 'nails': 50})
inv2 = Inventory({'nails': 150, 'bolts': 25})
combined_inv = inv1 + inv2
# expected: combined_inv.items is {'screws': 100, 'nails': 200, 'bolts': 25}

# Example 2
inv3 = Inventory({'widgets': 5})
inv4 = Inventory({'gadgets': 10})
combined_inv2 = inv3 + inv4
# expected: combined_inv2.items is {'widgets': 5, 'gadgets': 10}

# Example 3
inv5 = Inventory({'staples': 2000})
inv6 = Inventory({'staples': 3000})
combined_inv3 = inv5 + inv6
# expected: combined_inv3.items is {'staples': 5000}
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Incorrect assumption about operator behavior. The `+` operator is not defined for dictionaries. A student cannot simply write `self.items + other.items`. They must correctly implement the `__add__` magic method to manually iterate and merge the two item dictionaries into a new dictionary for the resulting Inventory object.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 26: Predict Code Output

Predict the output of the following code snippet and provide a step-by-step explanation for how you arrived at your answer. Your explanation should focus on how `cls` is resolved during the method call.

```python
class DataSerializer:
    protocol = 'JSON'

    @classmethod
    def serialize(cls, data):
        return f"<{cls.protocol}>{data}</{cls.protocol}>"

class XMLSerializer(DataSerializer):
    protocol = 'XML'

class Message:
    def __init__(self, content, serializer_class):
        self.content = content
        # The collaborator is the class itself, not an instance
        self.serializer = serializer_class

    def send(self):
        return self.serializer.serialize(self.content)

# Note: We are passing the XMLSerializer class, not an instance
message = Message("hello", XMLSerializer)
print(message.send())
```
<details> 
<summary>Hint</summary> 

Hidden Trap​: Late binding of `cls` in class methods. Students may incorrectly assume `cls` refers to the class where the method is defined, not the class that calls it.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 27: Debug Code

The following code is intended to create a `LoggingProxy` for a `DatabaseConnector` object. When a method like connect is called on the proxy, it should first log the action and then delegate the call to the actual database connector instance. However, running the code raises an `AttributeError`. Identify the bug, explain why it occurs, and provide the corrected code.

Intended Behavior​:

```
LOG: Attempting to call connect
Connected to the database.
```

```python
class DatabaseConnector:
    def __init__(self):
        self._is_connected = False

    def connect(self):
        self._is_connected = True
        print("Connected to the database.")

class LoggingProxy(DatabaseConnector):
    def __init__(self, connector_instance):
        # The collaborator is the connector instance
        self.connector = connector_instance

    def connect(self):
        print(f"LOG: Attempting to call connect")
        self.connector.connect()

db = DatabaseConnector()
proxy = LoggingProxy(db)
proxy.connect()
```

<details> 
<summary>Hint</summary> 

Hidden Trap​: Incomplete state initialization due to a missing `super().__init__ `call. Students must recognize that self is the same object throughout the inheritance chain and that the superclass's state must be properly initialized for the subclass to function.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 28: Implement a Class

Implement a `Configuration` class and two subclasses of a Validator: `MinLengthValidator` and `TypeValidator`.

1. Configuration​:
* Its `__init__` method accepts keyword arguments to store settings (e.g., `user='admin'`, `retries=3`).
* It stores these settings in an instance dictionary, perhaps called `_settings`.

2. ​Validator (Base Class)​:
* Provides the interface for validation rules.

3. `MinLengthValidator(Validator)`​:
* Its `__init__` takes a setting key and a minimum length.
* Its validate method takes a `Configuration` instance and returns `True` if the specified setting's value (which is assumed to be a string) meets the minimum length, `False` otherwise.

4.  `​TypeValidator(Validator)`​:
* Its `__init__` takes a setting key and a data type (e.g., str, int).
* Its validate method takes a Configuration instance and returns `True` if the specified setting's value is of the correct type, False otherwise.

Finally, the `Configuration` class must be implemented so that a `Validator` instance can be "subtracted" from it. The expression config - validator should return `True` if the configuration is valid according to the validator, and False otherwise.

I/O Examples​:
```python
# Example 1
config = Configuration(host='localhost', port=8080)
type_val = TypeValidator('port', int)
print(config - type_val) # Expected: True

# Example 2
config = Configuration(user='guest')
len_val = MinLengthValidator('user', 6)
print(config - len_val) # Expected: False

# Example 3
config = Configuration(api_key='ABC-123', retries='5')
type_val = TypeValidator('retries', int)
print(config - type_val) # Expected: False
```

<details> 
<summary>Hint</summary> 

Hidden Trap​: Misplacing the `__sub__` dunder method. The natural reading of config - validator implies that `__sub__` must be implemented on the `Configuration` class, where self is the config instance. A common but incorrect assumption is to place the dunder method on the `Validator` class.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 29: Predict & Explain Output

Predict the output of the following code snippet and be prepared to explain the method resolution order that produces this result.

```python
class DataParser:
    def process(self, data):
        print('Parsing data.')
        return 'parsed'

class Connection:
    def process(self, data):
        print('Opening connection.')
        return 'connected'

class DataTransmitter(Connection, DataParser):
    def process(self, data):
        print('Transmitting data.')
        result = super().process(data)
        print(f'Upstream process returned: {result}')

transmitter = DataTransmitter()
transmitter.process(data={'id': 1})
```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted:​ Misunderstanding `super()` and Method Resolution Order (MRO) in multiple inheritance. `super()` does not necessarily call the parent class, but rather the ​next​ class in the MRO.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 30: Debug a Snippet

The following code is intended to produce a `ConfigurableReport` that uses a formatter object to generate a titled report. However, it currently raises an `AttributeError`. Identify the bug and explain how to fix it.

Intended Behavior:​ The script should run without errors and print the string `=== WEEKLY REPORT ===`.

```python
class Formatter:
    def format_title(self, title):
        return f"=== {title.upper()} ==="

class Report:
    def __init__(self, formatter):
        self.formatter = formatter

class ConfigurableReport(Report):
    def __init__(self, title):
        self.title = title
        # Bug is related to this method's implementation

    def generate(self):
        return self.formatter.format_title(self.title)

report = ConfigurableReport("Weekly Report")
print(report.generate())
```


<details> 
<summary>Hint</summary> 

Hidden Trap Targeted:​ Incomplete state initialization due to a missing `super().__init__()` call. Subclass instances must properly initialize the state defined in their superclass(es).

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 31: Implement a Class

Implement the `TieredPricing` class. It inherits from `BasePricing` and requires an additional `tier_fee` during initialization. Its calculate method should determine a final price by first getting the base price from its parent and then adding its own `tier_fee` to that amount.

Provided Code:

```python
class BasePricing:
    def __init__(self, base_rate):
        self.rate = base_rate

    def calculate(self, units):
        return self.rate * units

# Your implementation here
class TieredPricing(BasePricing):
    pass
```

I/O Examples:
```python 
TieredPricing(base_rate=10, tier_fee=5).calculate(units=3) 
#35

TieredPricing(base_rate=2, tier_fee=100).calculate(units=50) 
# 200 

TieredPricing(base_rate=0, tier_fee=25).calculate(units=1000) 
#25
```

<details> 
<summary>Hint</summary> 

Hidden Trap Targeted:​ Incorrectly applying arithmetic operators to the `super()` proxy object itself instead of to its method's return value. This tests the understanding that `super()` is a proxy used for method dispatch, not a value.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 32: Predict and Explain​

Predict the output of the following Python code. In your explanation, describe the role of `super()` and detail the specific Method Resolution Order (MRO) that determines which log method is invoked.

```python
class Formatter:
    def log(self, message):
        return f"FORMAT: {message}"

class Timestamped:
    def log(self, message):
        return f"TIMESTAMP: {message}"

class MessageClient(Timestamped, Formatter):
    def __init__(self, message):
        self.message = message

    def send(self):
        print(super().log(self.message))

client = MessageClient("Data packet received.")
client.send()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ MRO Nuances with Multiple Mix-ins

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 33: Debugging​

The `ConfigManager` class below uses the Versioned mix-in to track changes to its configuration data. The intended behavior is that calling set_value should update the configuration dictionary and add a version snapshot to the `_history` list. However, running the code raises an exception.

Identify the bug, explain its cause, and provide the corrected code.

```python
class Versioned:
    def record_change(self):
        # Creates a snapshot of the current state for the history
        self._history += (self._data.copy(),)

class ConfigManager(Versioned):
    def __init__(self, initial_data):
        self._data = initial_data
        self._history = []

    def set_value(self, key, value):
        self._data[key] = value
        self.record_change()

# --- Intended Usage ---
config = ConfigManager({'theme': 'dark', 'font_size': 12})
config.set_value('font_size', 14)

# Expected `config._history` after execution:
# [{'theme': 'dark', 'font_size': 14}]
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Implicit Contract Violation (and Immutability)

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 34: Implementation​


You are building a data processing pipeline where some components are retryable. Implement the `Retryable` mix-in, which provides a `.execute() `method. This method should attempt to call `_perform_task()`, a method that will be defined on the host class.

The `.execute()` method must adhere to the following logic:

* It takes max_attempts as an argument.
* It calls `self._perform_task()`.
* If `_perform_task()` returns `True`, the execution is successful, and `.execute()` should return `'Success'`.
* If `_perform_task()` returns `False`, it should retry the call until it has been attempted `max_attempts` times.
* If all attempts fail, `.execute()` should return 'Failure'.

The `Retryable` mix-in assumes that any class using it will have an instance attribute task_name (a string) and will implement the `_perform_task` method.

```python
# --- Provided Code (Do not change) ---
class UnstableTask:
    def __init__(self, name, fail_count):
        self.task_name = name
        self.attempts = 0
        self.fail_limit = fail_count

    def _perform_task(self):
        self.attempts += 1
        if self.attempts > self.fail_limit:
            print(f"'{self.task_name}' succeeded on attempt {self.attempts}.")
            return True
        else:
            print(f"'{self.task_name}' failed on attempt {self.attempts}.")
            return False

# --- Your Implementation ---
# Implement the Retryable mix-in here.
class Retryable:
    pass # Your code here

# --- I/O Examples ---
class DataUpload(Retryable, UnstableTask):
    pass

# Example 1: Task succeeds on the second attempt
task1 = DataUpload(name="Image Upload", fail_count=1)
print(f"Final status: {task1.execute(max_attempts=3)}\n")
# Expected Output:
# 'Image Upload' failed on attempt 1.
# 'Image Upload' succeeded on attempt 2.
# Final status: Success

# Example 2: Task fails all attempts
task2 = DataUpload(name="Database Sync", fail_count=3)
print(f"Final status: {task2.execute(max_attempts=2)}\n")
# Expected Output:
# 'Database Sync' failed on attempt 1.
# 'Database Sync' failed on attempt 2.
# Final status: Failure

# Example 3: Task succeeds on the first attempt
task3 = DataUpload(name="Log Archiving", fail_count=0)
print(f"Final status: {task3.execute(max_attempts=5)}")
# Expected Output:
# 'Log Archiving' succeeded on attempt 1.
# Final status: Success
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ State Collision and Composition

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 35: Predict and Explain the Output 

Predict the output of the following Python code. Provide a step-by-step explanation of how you arrived at your answer, paying close attention to the relationship between the `Logger` and `DataProcessor` classes and how the final output is generated.

```python
class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f"Logging to {self.file_name}"

class DataProcessor:
    def __init__(self, data_source, logger):
        self.source = data_source
        self.logger = logger # A DataProcessor has a Logger

    def process(self):
        print(f"Processing data from {self.source}.")
        print(self.logger)

file_logger = Logger("system.log")
processor = DataProcessor("API", file_logger)
processor.process()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Mistaking collaboration for inheritance. A student might incorrectly think `DataProcessor` inherits from Logger and try to explain method resolution, when the key is that `DataProcessor` simply holds a `Logger` instance and delegates the call to print, which in turn invokes the Logger's `__str__` method.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 36:  Debug the Code

The following code is intended to model a `Car` that has an `Engine`. When `car.start()` is called, it should delegate the action to its `Engine` object and print "Engine started with Vroom!". However, running the code produces an error. Identify the bug, explain why it occurs, and provide the corrected code.

Intended Behavior:


Expected Output: `Engine started with Vroom!`

Buggy Code:
```python
class Engine:
    def start(self):
        return "Engine started with Vroom!"

class Car:
    def __init__(self):
        self.engine = Engine() # A Car has an Engine

    def start(self):
        # Incorrectly assumes the Car IS-AN Engine
        message = start()
        print(message)

car = Car()
car.start()
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ `NameError` due to incorrect delegation. The code calls `start()` instead of `self.engine.start()`. This directly targets the common mistake of thinking a "has-a" relationship provides the containing object with the collaborator's methods directly, as an "is-a" relationship would.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 37: Implement a Class 

Implement a `ShoppingList` class that encapsulates a list of items.

1. The constructor `__init__` should accept an initial list of items.
2. The class must support the `+` operator. When two `ShoppingList` instances are added, it should return a ​new​ `ShoppingList` instance containing all items from both lists.
3. The original lists must not be mutated.

Provide the complete class implementation.

Examples:

```python
# Example 1
groceries = ShoppingList(["milk", "eggs"])
household = ShoppingList(["soap", "paper towels"])
full_list = groceries + household
print(full_list.items)
# Expected Output: ['milk', 'eggs', 'soap', 'paper towels']


# Example 2
list1 = ShoppingList(["apples"])
print(list1.items) # Check before operation
# Expected Output: ['apples']

list2 = list1 + ShoppingList(["bananas"])
print(list1.items) # Verify original is unchanged
# Expected Output: ['apples']
print(list2.items)
# Expected Output: ['apples', 'bananas']

# Example 3
empty_list = ShoppingList([])
other_list = ShoppingList(["chair"])
result = empty_list + other_list
print(result.items)
# Expected Output: ['chair']
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Assuming the `+` operator will work "for free". A student might assume that because the class contains a list, Python will know to concatenate the inner lists. This is a reasonable but incorrect assumption. The trap is realizing this will cause a `TypeError` and that the `__add__` magic method must be implemented to define the behavior of the + operator for ShoppingList objects.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 38: Predict and Explain the Output

Predict the output of the following code snippet. Explain how instance and class variable scoping rules within the inheritance hierarchy determine the final output.

```python
class DataParser:
    # Class variable
    _delimiters = [',', ';']

    def get_delimiters(self):
        return self._delimiters

class CsvParser(DataParser):
    def __init__(self):
        # Instance variable with the same name
        self._delimiters = [',']

class LogEntryProcessor:
    def __init__(self, text, parser):
        self.text = text
        self.parser = parser

    def process(self):
        delimiters = self.parser.get_delimiters()
        print(f"Using delimiters: {delimiters}")

processor = LogEntryProcessor("user;admin", CsvParser())
processor.process()
```

<details> 
<summary>Hint</summary> 

Hidden Trap: Shadowing a class variable with an instance variable in a subclass, and then calling a method defined in the superclass.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 39: Debug the Code Snippet

The following code is intended to allow different Project instances to have independent build settings. Modifying the settings for one project should not affect another. However, the code is buggy and a change to `project_a`'s settings incorrectly alters `project_b`'s settings. Identify the bug and explain why it occurs.

```python
class BaseSettings:
    config = {'version': '1.0', 'strict_mode': False}

    def enable_strict_mode(self):
        self.config['strict_mode'] = True

class PythonProjectSettings(BaseSettings):
    pass

class Project:
    def __init__(self, name):
        self.name = name
        self.settings = PythonProjectSettings()

# --- Intended Behavior ---
project_a = Project("Project A")
project_b = Project("Project B")

# Enable strict mode only for Project A
project_a.settings.enable_strict_mode()

# Check settings for both projects
print(f"{project_a.name} strict_mode: "
      f"{project_a.settings.config['strict_mode']}")
print(f"{project_b.name} strict_mode: "
      f"{project_b.settings.config['strict_mode']}")
```

<details> 
<summary>Hint</summary> 

Hidden Trap: Mutating a shared, mutable class variable through an instance reference, causing unintended side effects across all instances of the class and its subclasses.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 40: Implement the `__add__` Method

Complete the `BaseComponent` and `Resistor` classes below. The `__add__` method in `BaseComponent` should allow adding an integer to a component's value, returning a ​new component object of the same class​ with the updated value. The `Resistor` subclass should inherit this behavior without overriding `__add__`.

```python
class BaseComponent:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{type(self).__name__}({self.value})"

    def __add__(self, num):
        # Your implementation here
        pass

class Resistor(BaseComponent):
    # A class attribute specific to Resistors
    TOLERANCE = 0.05

# --- I/O Examples ---
# 1. Adding to a BaseComponent instance
c1 = BaseComponent(100)
c2 = c1 + 20
print(f"Result: {c2}, Type: {type(c2)}")
# Expected: Result: BaseComponent(120), Type: <class '__main__.BaseComponent'>

# 2. Adding to a Resistor instance
r1 = Resistor(500)
r2 = r1 + 50
print(f"Result: {r2}, Type: {type(r2)}")
# Expected: Result: Resistor(550), Type: <class '__main__.Resistor'>

# 3. Verifying subclass attributes are preserved
print(f"New Resistor Tolerance: {r2.TOLERANCE}")
# Expected: New Resistor Tolerance: 0.05
```

<details> 
<summary>Hint</summary> 


Hidden Trap: Using the correct constructor (`self.__class__` or `type(self)`) within a superclass method to ensure polymorphic instantiation, rather than hardcoding the base class name.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 41: Predict and Explain Output


Predict the output of the following code snippet. Provide a step-by-step explanation of how Python's Method Resolution Order (MRO) determines which process method is called and what value is ultimately returned.

```python
class TextProcessor:
    def process(self, data):
        return data.upper()

class JsonProcessor:
    def process(self, data):
        return '{"data": "' + data + '"}'

class DataPipeline(TextProcessor, JsonProcessor):
    def run(self, input_data):
        # some preparatory steps...
        processed = self.process(input_data)
        # some cleanup steps...
        return processed

pipeline = DataPipeline()
print(pipeline.run("launch"))
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt targets the "left-to-right" rule in MRO. Since `TextProcessor` is listed before `JsonProcessor` in the inheritance list, its process method will be found and executed first. The process method in `JsonProcessor` is completely ignored, a behavior that can be counterintuitive if one expects composition or chaining.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 42: Debug a Code Snippet


The `StyledButton` class is intended to create a button whose text is first wrapped in a style tag `(<em>)` by the `StylingMixin`, and then rendered into a full button tag `(<button>)` by the `ButtonWidget` class. The final output for an input of "Click Me" should be `<button><em>Click Me</em></button>`.

However, the current implementation produces incorrect output. Identify the bug and explain why the Method Resolution Order (MRO) causes this unintended behavior.

```python
class ButtonWidget:
    def render(self, text):
        return f"<button>{text}</button>"

class StylingMixin:
    def render(self, text):
        styled_text = f"<em>{text}</em>"
        return super().render(styled_text)

class StyledButton(ButtonWidget, StylingMixin):
    pass

# Intended behavior:
# button = StyledButton()
# print(button.render("Click Me"))
# Expected output: <button><em>Click Me</em></button>

# Current behavior:
button = StyledButton()
print(button.render("Click Me"))
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This tests the interaction between inheritance order and `super()`. The current MRO finds `ButtonWidget.render first`, which does not call `super()`, so the `StylingMixin` is never invoked. The bug requires reversing the inheritance order. This highlights that the functionality of `super()` is entirely dependent on the MRO, which is defined by the class declaration.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 43: Implement a Class


Implement the `ConfigurableService` class. This class must inherit from `BaseService` and `LoggingMixin`. Its execute method should first log the provided data, and then pass that same data to the execute method from its service parent. The class must correctly initialize with a `service_name`.

```python
class BaseService:
    def __init__(self, service_name):
        self.service_name = service_name

    def execute(self, data):
        return f"{self.service_name} processed: {data}"

class LoggingMixin:
    def execute(self, data):
        print(f"Logging data: {data}")
        return super().execute(data)

# Your implementation of ConfigurableService here
```

```python
# --- Examples ---
service1 = ConfigurableService("DataProcessor")
# Expected output:
# Logging data: payload123
# DataProcessor processed: payload123
print(service1.execute("payload123"))

print("-" * 20)

service2 = ConfigurableService("FileHandler")
# Expected output:
# Logging data: document.txt
# FileHandler processed: document.txt
print(service2.execute("document.txt"))

print("-" * 20)

service3 = ConfigurableService("Auth")
# Expected output:
# Logging data: user:token
# Auth processed: user:token
print(service3.execute("user:token"))
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt combines two concepts: MRO for method calls and MRO for initialization. The primary trap is recognizing the need to correctly order the parent classes (`LoggingMixin` must come first) to achieve the desired execute behavior. A second, related trap is handling the `__init__` method. The student must implement an `__init__` in `ConfigurableService` that calls `super().__init__` to properly initialize the service_name from `BaseService`.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 44: Predict and Explain


Predict the output of the following code snippet. Explain your reasoning for each printed line, focusing on object identity and the behavior of the is operator.

```python
class Component:
    def __init__(self, name):
        self.name = name
        self.settings = {'active': True}

    def get_settings(self):
        # Returns a copy of the settings dictionary
        return self.settings.copy()

class System:
    def __init__(self):
        self.component = Component("Core")

    def get_component(self):
        return self.component

sys = System()
comp1 = sys.get_component()
comp_settings = comp1.get_settings()

comp_settings['active'] = False

print(f"1: {sys.component.settings['active']}")
print(f"2: {comp1 is sys.get_component()}")
print(f"3: {sys.component.settings is comp_settings}")
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt targets the distinction between returning a direct reference to a mutable object versus returning a ​copy​ of it. The get_settings method's use of `.copy()` is the key. It creates a new dictionary object with the same key-value pairs, breaking the identity link that a student might otherwise assume exists.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 45: Debug the Code


The following code is intended to manage a single, shared configuration object for multiple service instances. The `LogManager` should ensure that all services access the exact same configuration dictionary. However, the final line prints `False`, indicating a bug. Identify the bug, explain why it causes the issue, and describe how to fix it.

```python
# Intended behavior: All Service instances should share the exact same
# logger configuration object. The final check `config1 is config2`
# is expected to print `True`.

class LogManager:
    def __init__(self):
        self.config = {'level': 'INFO', 'file': 'app.log'}

    def update_config(self, new_settings):
        # Creates a new config object based on the old one
        self.config = self.config.copy()
        self.config.update(new_settings)

class Service:
    def __init__(self, name, manager):
        self.name = name
        self.log_manager = manager

    def get_log_config(self):
        return self.log_manager.config

log_mgr = LogManager()
service1 = Service("AuthService", log_mgr)
config1 = service1.get_log_config()

log_mgr.update_config({'level': 'DEBUG'})

service2 = Service("DataService", log_mgr)
config2 = service2.get_log_config()

print(config1 is config2) # Output is False, but should be True

```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The trap here is a reasonable but incorrect assumption about the `update_config` method's behavior. The name implies it will ​mutate​ the existing configuration object. However, its implementation first creates a copy and then ​reassigns​ self.config to that new copy. This severs the identity link to the original object held by `config1`, causing the check to fail.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 46: Implement a Class

Implement the `DeviceCache` class. This class must manage `Device` objects. Its `get_device` method should adhere to the following rule: for any given `device_id`, the method must always return the exact same `Device` object. If `get_device` is called with a `device_id` that has not been seen before, it should create and store a new Device instance. Subsequent calls with that same `device_id` must return that stored instance.

You are given the `Device` class. Your code should produce the expected output for all three examples.

```python
class Device:
    """A simple class representing a hardware device."""
    def __init__(self, device_id):
        self.device_id = device_id
        # The following print statement helps verify when a new object is made.
        print(f"Initializing new device: {self.device_id}")

# Your implementation of DeviceCache goes here.


I/O Examples:

# Example 1: Retrieving the same device twice
cache = DeviceCache()
d1 = cache.get_device("d-101")
d2 = cache.get_device("d-101")
print(f"Example 1 check: {d1 is d2}")
# Expected Output: True

# Example 2: Retrieving two different devices
d3 = cache.get_device("d-205")
print(f"Example 2 check: {d1 is d3}")
# Expected Output: False

# Example 3: Verifying separate caches
cache2 = DeviceCache()
d4 = cache2.get_device("d-101")
print(f"Example 3 check: {d1 is d4}")
# Expected Output: False
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The primary trap is correctly managing the storage and retrieval of object references. The implementation must ensure it's storing the actual object instance and not accidentally creating a new one on each call. A secondary trap, tested by Example 3, is ensuring the cache is an ​instance​ variable, not a class variable, so that different `DeviceCache` objects maintain separate, independent caches.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 47: Predict and Explain

Predict the output of the following code. Explain precisely why it produces that output, detailing the method lookups and comparisons that occur.

```python
class Authorization:
    def __init__(self, level):
        self.level = level

    def __eq__(self, other):
        print("Authorization.__eq__ called")
        if not isinstance(other, Authorization):
            return NotImplemented
        return self.level == other.level

class User:
    def __init__(self, auth_level):
        self.auth = Authorization(auth_level)

    def can_access(self, required_level):
        required_auth = Authorization(required_level)
        return self.auth != required_auth

user = User(auth_level=5)
print(user.can_access(required_level=5))

```

<details> 
<summary>Hint</summary> 


Hidden Trap: The `!=` operator does not automatically call a negated version of `__eq__`. It looks for `__ne__` first and, if not found, falls back to the default identity-based comparison.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 48: Debugging

The following code is intended to determine if a new `EventLog` is a promotion from an old one. The rule is that a log is a promotion if its priority is higher. The code is currently failing with an unhandled `TypeError`. Identify the bug, explain its cause, and provide the corrected code.

Intended Behavior​: The code should execute without error and print `True`.

```python
class EventLog:
    def __init__(self, priority, message):
        self.priority = priority
        self.message = message

    def __lt__(self, other):
        if not isinstance(other, EventLog):
            return NotImplemented
        return self.priority < other.priority

class SystemMonitor:
    @staticmethod
    def is_promotion(old_log, new_log):
        # A new log is a promotion if it is "greater than" the old one.
        return new_log > old_log

old_log = EventLog(priority=1, message="System OK")
new_log = EventLog(priority=5, message="Critical Failure")

print(SystemMonitor.is_promotion(old_log, new_log))
```


<details> 
<summary>Hint</summary> 


Hidden Trap: Assuming that defining `__lt__ `is sufficient for Python to handle `>` comparisons automatically through reflection in all cases. While Python may try `a > b` by evaluating `b < a`, relying on this is fragile. The direct implementation of `__gt__` is missing, causing a `TypeError` when the `>` operator is used.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 49: Implementation

A `GeographicPoint` has latitude and longitude. A `Route` is defined by two `GeographicPoint` objects: a start and an end.

Implement the `Route` class. Two `Route` instances are considered equal if they represent the same journey, regardless of direction (e.g., a route from A to B is equal to a route from B to A). They must also have the same `is_scenic` status.

Your implementation should define the necessary magic method(s) for the `==` operator to work as described.

```python
class GeographicPoint:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return (isinstance(other, GeographicPoint) and
                self.lat == other.lat and self.lon == other.lon)

# Your Route class implementation here...

# I/O Examples:
p1 = GeographicPoint(40.7128, -74.0060) # NYC
p2 = GeographicPoint(34.0522, -118.2437) # LA
p3 = GeographicPoint(49.2827, -123.1207) # Vancouver

route1 = Route(p1, p2, is_scenic=True)
route2 = Route(p2, p1, is_scenic=True) # Reversed points
route3 = Route(p1, p2, is_scenic=False) # Different scenic status
route4 = Route(p1, p3, is_scenic=True) # Different endpoint

print(route1 == route2) # Expected: True
print(route1 == route3) # Expected: False
print(route1 == route4) # Expected: False
```

<details> 
<summary>Hint</summary> 

Hidden Trap: Complex equality logic with collaborator objects. A simple comparison of `self.start == other.start` and `self.end == other.end` is insufficient because the direction doesn't matter. The implementation must account for the commutative nature of the route's endpoints.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 50: Predict and Explain​*

Predict the output of the code below. Explain the sequence of method calls triggered by the `+` operator in the line that initializes the report variable, detailing how each call contributes to the final state of the report object.

```python
class DataPoint:
    def __init__(self, value):
        self.value = value

class Report:
    def __init__(self, title, data_points=None):
        self.title = title
        self.data = data_points or []

    def __add__(self, other):
        if isinstance(other, DataPoint):
            new_data = self.data + [other.value]
            return Report(self.title, new_data)
        elif isinstance(other, Report):
            new_title = f"{self.title} & {other.title}"
            new_data = self.data + other.data
            return Report(new_title, new_data)
        return NotImplemented

initial = Report("Q1 Sales")
point = DataPoint(100)
adjustment = Report("Adjustments", [-5])

report = initial + point + adjustment
print(len(report.data))
print(report.title)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Chaining methods that return new objects.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 51: Debugging​

The code below is intended to allow a Project's hours to be increased by adding `TimeLog` objects using the `+=` operator. The final print statement should display that the project has 12 total hours. However, running the code raises a `TypeError` on the second `+=` operation. Identify the bug, explain its cause, and provide the corrected `Project` class implementation.

```python
class TimeLog:
    def __init__(self, hours):
        self.hours = hours

class Project:
    def __init__(self, name):
        self.name = name
        self.hours_logged = 0

    def __iadd__(self, other):
        if isinstance(other, TimeLog):
            self.hours_logged += other.hours
        # Missing return statement here

# --- Main execution ---
alpha = Project("Project Alpha")
alpha += TimeLog(8)
alpha += TimeLog(4) # This line causes a TypeError

# Expected output: Project Alpha has 12 hours logged.
print(f"{alpha.name} has {alpha.hours_logged} hours logged.")
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ The required return value for in-place augmented assignment methods (`__iadd__`).

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 52: Implementation​

Implement the `Inventory` class to manage item quantities. The class must support the + operator to combine an `Inventory` object with a `Shipment` object, which contains a dictionary of new items. The operation must be commutative, meaning it should work correctly regardless of whether the `Inventory` or `Shipment` is the left operand. Adding a `Shipment` to an `Inventory` should return a ​new​ I`nventory` object with updated quantities.

```python
class Shipment:
    def __init__(self, items):
        self.items = items

class Inventory:
    # Your implementation here
    pass

# --- Examples ---

# Example 1: inventory + shipment
inv = Inventory({'apples': 10, 'bananas': 20})
shipment1 = Shipment({'bananas': 5, 'oranges': 15})
new_inv1 = inv + shipment1
# Expected: new_inv1.stock is {'apples': 10, 'bananas': 25, 'oranges': 15}
print(new_inv1.stock)

# Example 2: shipment + inventory
inv2 = Inventory({'staplers': 50, 'pens': 100})
shipment2 = Shipment({'pens': 25, 'paper': 200})
new_inv2 = shipment2 + inv2
# Expected: new_inv2.stock is {'staplers': 50, 'pens': 125, 'paper': 200}
print(new_inv2.stock)

# Example 3: Original inventory is not mutated
print(inv.stock) # Expected: {'apples': 10, 'bananas': 20}
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Needing `__radd__` to handle operations where the custom class is the right-hand operand.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 53: Predict and Explain Output

Predict the output of the following Python code snippet. Explain in detail the process Python uses to determine the string representation for each print call, paying close attention to how container objects format their contents.

```python
class Component:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f"Component(name='{self.name}')"

class System:
    def __init__(self, system_id, components):
        self.system_id = system_id
        self.components = components

    def __str__(self):
        return f"System ID: {self.system_id}"

main_system = System(
    "SYS-101",
    [Component("sensor"), Component("actuator")]
)

print(main_system)
print(main_system.components)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt targets the rule that container types (like list, dict, tuple) ​always use the `__repr__` method​ of their contents, even when the container itself is being printed (which implicitly uses str). Students may incorrectly assume that `print()`'s call to str propagates down to the elements within the list.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 54: Debug the Code

The following code is intended to display a project's details, including a user-friendly list of its associated tasks. However, the output for the tasks is not as expected. Identify the bug, explain why the current output occurs, and describe the necessary correction to the class definitions.

Intended Behavior:​ The script should print the following line to the console:
`Project: Data Migration, Tasks: [High-priority task, Review task]`

```python
class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.priority}-priority task"

class Project:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def __repr__(self):
        # Developer-facing representation for debugging
        return f"Project: {self.name}, Tasks: {self.tasks}"

task1 = Task("Implement API", "High")
task2 = Task("Code Review", "Review")
project = Project("Data Migration", [task1, task2])

print(project)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt targets the fallback behavior where `print(obj)` (which uses `str(obj)`) will call `obj.__repr__()` if `obj.__str__()` is not defined. The chain of events is: print(project) -> str(project) -> (fallback) repr(project) -> list formatting -> repr(task). Since Task has no `__repr__`, the default object representation is used. The incorrect assumption is that print will somehow find and use the `__str__` method on the nested Task objects.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 55: Implement Classes

Implement the `Book` and `Library` classes based on the requirements demonstrated by the I/O examples below. A `Library` is initialized with a name and a list of Book objects. A `Book` has a title and an author. Your implementation must produce the exact output shown for each print call.

```python
# Your class definitions go here

# Do not change the code below
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")
my_library = Library("City Central", [book1, book2])

# Example 1
print(book1)
# Expected Output 1:
# The Hobbit by J.R.R. Tolkien

# Example 2
print(my_library)
# Expected Output 2:
# City Central Library

# Example 3
print(my_library.books)
# Expected Output 3:
# [Book('The Hobbit', 'J.R.R. Tolkien'), Book('1984', 'George Orwell')]
```



<details> 
<summary>Hint</summary> 

Hidden Trap:​ This prompt forces the student to recognize that the Book class requires ​both a `__str__` and a `__repr__` method​ to satisfy all examples. Example 1 defines the behavior for `__str__`, while Example 3 (printing a list of books) implicitly defines the required behavior for `__repr__`. A student who only implements `__str__` on `Book` will fail to get the correct output for Example 3.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 56: Predict and Explain​


Predict the output of the following code snippet. Provide a step-by-step explanation for how you arrived at your answer, detailing what `self`, `__class__`, and `__name__` refer to on each line where they are used.

```python
class Notifier:
    def send(self, message):
        print(f"Sending notification: {message}")

class Service:
    def __init__(self):
        self.notifier = Notifier()

    def do_work(self):
        print(f"Starting work in {self.__class__.__name__}...")
        self.notifier.send("Work in progress")
        print(f"Notifier's class is: {self.notifier.__class__.__name__}")

service = Service()
service.do_work()
```



<details> 
<summary>Hint</summary> 

​Hidden Trap:​​ Differentiating between the class of the Service instance (`self`) and the class of its collaborator object (`self.notifier`). Students must correctly identify the object on which `.__class__` is being accessed.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 57: Debug the Code​


The following code is intended to create a Report that uses a DataFormatter collaborator to format its title. The generate method should print a title including the formatter's class name, like "CSVFormatter Report". However, running the code raises an `AttributeError`.

Identify the bug, explain why it occurs, and provide the corrected line of code.

```python
class CSVFormatter:
    pass

class Report:
    def __init__(self, formatter):
        self.formatter = formatter

    def generate(self):
        # Intended to print: "CSVFormatter Report"
        print(f"{self.formatter.__name__} Report")

report = Report(CSVFormatter())
report.generate()
```

<details> 
<summary>Hint</summary> 

​Hidden Trap:​​ The reasonable but incorrect assumption that the `__name__` attribute is available directly on an ​instance​. This tests the distinction between instance attributes and class attributes.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 58: Implement a Function​

Implement a function c`reate_factory_log(component)` that takes an object instance representing a machine part. The function should return a string logging the part's class name. The object passed to the function will be a collaborator in a larger factory system.

Your implementation must work for any object, not just the examples shown.

I/O Examples:
```python
class Gear:
    pass

class Piston:
    pass

class Rotor:
    pass

# Your implementation of create_factory_log here

print(create_factory_log(Gear()))
# Expected: "Component of type 'Gear' received."

print(create_factory_log(Piston()))
# Expected: "Component of type 'Piston' received."

print(create_factory_log(Rotor()))
# Expected: "Component of type 'Rotor' received."

```

<details> 
<summary>Hint</summary> 


​Hidden Trap:​​ The temptation to use isinstance checks or hardcoded strings. The prompt requires a polymorphic solution that dynamically inspects the collaborating object's type using `__class__.__name__`, demonstrating a core principle of object-oriented design.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 59: Predict Output

Predict the output of the following code snippet and explain your reasoning.

```python
class Song:
    def __init__(self, title):
        self.title = title

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_first_song_details(self):
        try:
            song = self.songs[0]
            # This line may raise an exception
            return f"{song.title} by {song.artist}"
        except IndexError:
            return "Playlist is empty."

playlist = Playlist("My Jams")
song1 = Song("Stairway to Heaven")
playlist.add_song(song1)

try:
    print(playlist.get_first_song_details())
except Exception as e:
    print(f"Caught a general exception: {type(e).__name__}")

```


<details> 
<summary>Hint</summary> 

​Hidden Trap: Exception Specificity and Propagation. An except block for a specific exception (`IndexError`) will not catch a different exception type (`AttributeError`). The unhandled exception propagates up the call stack until a suitable handler (except `Exception`) is found.​

</details>
<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 60: Debugging


The following function process_all_data is intended to process a list of raw data. It should create `DataEntry` objects for integer values and return a list of those values. For any non-integer data, it should catch the `TypeError` raised by the `DataEntry` constructor, print an error message, and continue processing the rest of the list. The current implementation is buggy. Identify the bug and describe how to fix it.

```python
class `DataEntry`:
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError("DataEntry value must be an integer.")
        self.value = value

    def get_value(self):
        return self.value

def process_all_data(raw_data_list):
    processed_values = []
    try:
        for raw_data in raw_data_list:
            entry = DataEntry(raw_data)
            processed_values.append(entry.get_value())
    except TypeError as e:
        print(f"Error processing entry: {e}")

    return processed_values

# Example Usage:
data = [10, "invalid", 20, 30, "bad_data"]
result = process_all_data(data)
print(f"Processed: {result}")

# Current Incorrect Output:
# Error processing entry: DataEntry value must be an integer.
# Processed: []

# Expected Correct Output:
# Error processing entry: DataEntry value must be an integer.
# Error processing entry: DataEntry value must be an integer.
# Processed: [10, 20, 30]
```


<details> 
<summary>Hint</summary> 

Hidden Trap: Scope of `try/except` block. Placing an entire loop inside a single try block means that an exception raised during any iteration will terminate the whole loop and jump to the except block. To handle errors on a per-item basis, the try/except must be inside the loop.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 61: Implementation


Implement the `MessageBroadcaster` class below. Its `send_all` method accepts a message string and a list of recipient objects. The method should try to deliver the message to each recipient based on the following logic:

1.  First, attempt to call a `send(message)` method on the recipient.
2.  If the recipient does not have a send method, it should fall back to calling a write(message) method.
3.  If a recipient has neither method, it should be skipped without raising an error.
4.  The method must return the total count of messages that were successfully sent.

```python
class MessageBroadcaster:
    # Your implementation here

# --- I/O Examples ---
# Helper classes for testing
class EmailRecipient:
    def send(self, message):
        print(f"Emailing: {message}")

class FileLogger:
    def write(self, message):
        print(f"Logging: {message}")

# Example 1
broadcaster = MessageBroadcaster()
recipients1 = [EmailRecipient(), EmailRecipient()]
count1 = broadcaster.send_all("Hello", recipients1)
print(count1)
# Expected Output:
# Emailing: Hello
# Emailing: Hello
# 2

# Example 2
broadcaster = MessageBroadcaster()
recipients2 = [EmailRecipient(), FileLogger(), EmailRecipient()]
count2 = broadcaster.send_all("Update", recipients2)
print(count2)
# Expected Output:
# Emailing: Update
# Logging: Update
# Emailing: Update
# 3

# Example 3
broadcaster = MessageBroadcaster()
recipients3 = [FileLogger(), 42, EmailRecipient()]
count3 = broadcaster.send_all("Final notice", recipients3)
print(count3)
# Expected Output:
# Logging: Final notice
# Emailing: Final notice
# 2
```


<details> 
<summary>Hint</summary> 

Hidden Trap: Graceful Degradation / Fallback Logic. Correctly implementing the fallback requires careful structuring of `try/except` blocks, likely nested, to first attempt one protocol (`.send()`) and then, only upon its failure, attempt a second protocol (`.write()`). A single try with multiple except clauses is insufficient to model this sequential fallback logic.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 62: Predict and Explain

What will the following code output? Explain your reasoning in detail.

```python
class DataValidationError(Exception):
    pass

class DataValidator:
    def __init__(self, required_keys):
        self.required_keys = set(required_keys)

    def validate(self, data):
        if not self.required_keys.issubset(data.keys()):
            raise DataValidationError("Missing required data keys.")
        return True

class Report:
    def __init__(self, data, validator):
        self.data = data
        self.validator = validator

    def generate(self):
        try:
            self.validator.validate(self.data)
            print("Report generated successfully.")
        except Exception:
            print("A generic error occurred.")
        except DataValidationError:
            print("Data validation failed.")

validator = DataValidator(['id', 'timestamp'])
invalid_data = {'id': 101}
report = Report(invalid_data, validator)
report.generate()
```

<details> 
<summary>Hint</summary> 
Hidden Trap​: Exception hierarchy and except block ordering.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 63: Debug the Code

The following code is intended to catch an `InsufficientFundsError` and print a specific, helpful message. However, when the error is caught, it prints an empty line instead of the expected message. Identify the bug and provide the corrected code.

Intended Behavior:
The script should print the message: `Insufficient funds in account 12345`.

```python
# Buggy Code
class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            msg = f"Insufficient funds in account {self.account_id}."
            raise InsufficientFundsError(msg)
        self.balance -= amount

class PaymentProcessor:
    def process_payment(self, account, amount):
        try:
            account.withdraw(amount)
            print("Payment successful.")
        except InsufficientFundsError as e:
            print(e)

my_account = Account(12345, 100)
processor = PaymentProcessor()
processor.process_payment(my_account, 150)
```

<details> 
<summary>Hint</summary> 

Hidden Trap​: Custom exception classes need an `__init__` method that calls `super().__init__(message)` to store and display the error message.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 64: Implement a Class

Implement the `ConnectionError` custom exception and the Device class to satisfy the requirements outlined in the provided examples.

Requirements:

1. Create a custom exception `ConnectionError` that inherits from `Exception`. Its initializer must accept a message string and an error_code integer and store them as attributes.
2. Create a `Device` class. Its `__init__` method should accept a name.
3. The `Device` class must have an instance method connect_to(self, network). The network object is a collaborator.
4.  If the network object's status attribute is 'offline', the method should raise a `ConnectionError` with the message `f"{self.name}` failed to connect." and an error_code of 101.
5.  If the connection is successful (network.status is 'online'), the method should return True.

```python
# Helper class (do not modify)
class Network:
    def __init__(self, status):
        self.status = status

# Your implementation here:
# class ConnectionError(Exception):
#     ...
#
# class Device:
#     ...

# --- Examples ---

# 1. Successful Connection
online_net = Network('online')
my_device = Device('Router')
print(my_device.connect_to(online_net))
# Expected Output:
# True

# 2. Failed Connection (general catch)
offline_net = Network('offline')
my_pc = Device('My PC')
try:
    my_pc.connect_to(offline_net)
except Exception as e:
    print(e)
# Expected Output:
# My PC failed to connect.

# 3. Failed Connection (specific catch with error code)
try:
    my_pc.connect_to(offline_net)
except ConnectionError as e:
    print(f"Error Code: {e.error_code}, Message: {e}")
# Expected Output:
# Error Code: 101, Message: My PC failed to connect.
```

<details> 
<summary>Hint</summary> 

Hidden Trap​: Designing a custom exception to carry state beyond just a message string.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 65: Predict and Explain the Output

Predict the output of the following code snippet and explain your reasoning. Your explanation should focus on the interaction between the `Inventory` and `Widget` objects.

```python
class Widget:
    def __init__(self, name):
        self.name = name
        self.inspections = 0

    def inspect(self):
        self.inspections += 1

class Inventory:
    def __init__(self, initial_widgets):
        self.widgets = initial_widgets

    def run_quality_check(self):
        for widget in self.widgets:
            widget.inspect()

    def get_total_inspections(self):
        return sum(w.inspections for w in self.widgets)

widget_a = Widget('A')
widget_b = Widget('B')
main_stock = [widget_a, widget_b]

warehouse = Inventory(main_stock)
warehouse.run_quality_check()

print(warehouse.get_total_inspections())
print(widget_a.inspections)
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Tests understanding of object references vs. copies. The `Inventory `object holds references to the original `Widget` objects, not copies. Modifying a widget's state via the warehouse object also mutates the original `widget_a` object because they are the exact same object in memory.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 66: Debug the Code.

The following code is intended to manage a team and its members. A `Team` object should be able to add `Member` objects to its roster. The final output should be `['Dana', 'Fox']`. However, the code currently prints an empty list `[]`. Identify the bug and describe how to fix it.

```python
# Intended behavior: Add two members to a team and list their names.
# Expected output: ['Dana', 'Fox']

class Member:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members + [member]

    def get_roster(self):
        return [m.name for m in self.members]

special_ops = Team("Special Ops")
special_ops.add_member(Member("Dana"))
special_ops.add_member(Member("Fox"))

print(special_ops.get_roster())

```



<details> 
<summary>Hint</summary> 

Hidden Trap:​ Targets a common incorrect assumption about the `+` operator with lists. The expression `self.members + [member]` creates a ​new​ list but does not modify self.members in place. The new list is created and then immediately discarded. The trap is making the student identify that a non-mutating method was used where a mutating one (like .append()) was needed.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 67: Implement Classes with Collaborators*

Implement the `Engine`, `Wheel`, and `Car` classes to satisfy the requirements demonstrated by the I/O examples below.

A `Car` instance is composed of one `Engine` instance and four `Wheel` instances.

* The `Engine` class needs a get_status method that returns the string "`Engine is on.`".
* The `Wheel` class needs a get_status method that returns the string "Tire pressure is normal.".
* The `Car` class must have a run_diagnostics method that returns a dictionary containing status reports from its components.

```python
# --- Implement `Engine`, `Wheel`, and `Car` classes here ---

```

```python
# --- I/O Examples ---

# 1.
engine = Engine()
wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
car = Car(engine, wheels)
print(car.run_diagnostics())
# Expected:
# {
#   'engine': 'Engine is on.',
#   'wheel_1': 'Tire pressure is normal.',
#   'wheel_2': 'Tire pressure is normal.',
#   'wheel_3': 'Tire pressure is normal.',
#   'wheel_4': 'Tire pressure is normal.'
# }

# 2.
class RacingEngine(Engine):
    def get_status(self):
        return "Engine is supercharged."

car2 = Car(RacingEngine(), [Wheel() for _ in range(4)])
print(car2.run_diagnostics()['engine'])
# Expected: Engine is supercharged.

# 3.
car3 = Car(Engine(), [Wheel() for _ in range(4)])
print(isinstance(car3.engine, Engine))
# Expected: True
```

<details> 
<summary>Hint</summary> 

Hidden Trap:​ Tests the ability to correctly model a "has-a" relationship (composition) instead of an incorrect "is-a" relationship (inheritance). The `Car` class should contain an `Engine` and `Wheel` objects as instance variables, not inherit from them. The trap is to see if the student defaults to inheritance when the more appropriate pattern is for the `Car` object to collaborate with its component objects.

</details>
<details> 
<summary>Possible Solution</summary> 
</details>


