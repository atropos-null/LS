# PY129 LSBOT Prep Questions

## Pass 8, Kel's Take on James' Take

Prompt:

Generate 20 intermediate to advanced Python problems focusing on:
* composition
* duck typing
* encapsulation
* mix-ins
* comparison and arithmetic magic methods

Each problem must meet these constraints:
* Solvable in ≤30 minutes by a PY129 student
* Requires object collaboration, not isolated methods
* Does not assume any classes already exist
* Includes example usage or I/O, but no solutions

For each problem, include:
1.	Problem statement
2.	Examples of expected behavior (inputs/outputs or interactions)
3.	Task type (one of: write code, explain behavior, debug existing code)
4.	Hidden trap (name the implicit assumption or protocol being tested)
5.	One reasonable wrong turn a prepared student might take

Additional constraints:
* Do not name the concepts being tested
* Sort problems from easiest to hardest
* Avoid toy domains (e.g., dogs, cars); prefer realistic system components


### Problem 1, ​Task Type:​ write code

Design DataPacket and DataStream classes. A DataPacket holds a piece of data (e.g., a string). A DataStream is composed of a sequence of DataPacket objects. Implement a way to combine two DataStream objects. The combination should result in a new DataStream containing all the packets from both original streams, in order. Also, provide a simple string representation for a DataStream that indicates how many packets it contains.

Examples of Expected Behavior:

```python    
packet1 = DataPacket("content1")
packet2 = DataPacket("content2")
stream1 = DataStream([packet1])

packet3 = DataPacket("content3")
stream2 = DataStream([packet2, packet3])

combined_stream = stream1 + stream2
print(combined_stream)  # Expected: "DataStream containing 3 packets"
# The combined_stream object should be a new instance, separate from stream1 and stream2.
```
  
<details> 
<summary>Hint</summary> 
​Hidden Trap:​ Returning a new instance from the combination operation, not modifying one of the existing instances in-place.

​Reasonable Wrong Turn:​ Modifying the list of packets of the first operand (self) directly instead of creating a new DataStream object with a new list.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 2, ​Task Type:​ write code

Design a ReadOnlyConfig class that is initialized with a dictionary of settings. Once created, the settings should not be modifiable from outside the object. Create a DatabaseConnector class that takes a ReadOnlyConfig object during its initialization. The connector will use the configuration to generate a connection string.


​Examples of Expected Behavior:

```python  
settings = {'host': 'localhost', 'port': 5432}    
config = ReadOnlyConfig(settings)
connector = DatabaseConnector(config)
print(connector.get_connection_string()) # Expected: "postgresql://localhost:5432"

# This attempt to modify the config should not work
try:
    config.get_settings()['port'] = 9999
except Exception as e:
    print(f"Modification failed: {type(e)}")

# The connection string should remain unchanged

print(connector.get_connection_string()) # Expected: "postgresql://localhost:5432"
```

<details> 
<summary>Hidden Trap</summary> 

Hidden Trap:​ A getter method that returns a mutable object (like a dictionary) allows the object's internal state to be changed. The getter must return a copy.

​Reasonable Wrong Turn:​ Storing the dictionary in a "private" variable (e.g., _settings) but then writing a getter that returns the variable directly, which allows the caller to mutate the original dictionary.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 3 ​Task Type:​ write code

​Problem Statement:​ Create a Renderer class with a method render_layout that accepts a list of page elements. For each element in the list, the method should invoke a draw method on it and collect the results. Create two different classes, HeaderElement and ParagraphElement, which are not related by inheritance. Both classes must implement a draw method that returns a formatted string. The Renderer should be able to process a list containing instances of both element types without checking their specific class.

​Examples of Expected Behavior:
```python

    elements = [
    HeaderElement("Report Title"),
    ParagraphElement("This is the first paragraph."),
    ParagraphElement("This is the second paragraph."),
    ]
    
    renderer = Renderer()
    output = renderer.render_layout(elements)
    # output should be a list of strings:
    # ['<h1>Report Title</h1>', '<p>This is the first paragraph.</p>', '<p>This is the second paragraph.</p>']

```

<details> 
<summary>Hidden Trap</summary> 

Hidden Trap:​ The Renderer must not use isinstance() or type() to check what kind of element it is processing. It should just trust that each element has the required method.

​Reasonable Wrong Turn:​ Writing if/elif logic inside the render_layout method to check the type of each element before calling draw, which defeats the flexibility of the design.

</details>


<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 4, Task type: write code

Design a Job class with a priority (integer) and a name (string). Create a JobQueue class that holds a list of Job objects. Implement a method in JobQueue called run_next_job that sorts all jobs by priority (a lower number is higher priority) and returns the name of the highest-priority job. The sorting mechanism must be inherent to the Job objects themselves, allowing Python's standard sorting functions to work on them directly.

​Examples of Expected Behavior:

```python
    job1 = Job("Process video", 3)
    job2 = Job("Send emails", 2)
    job3 = Job("Run analytics", 1)

    queue = JobQueue([job1, job2, job3])
    print(queue.run_next_job()) # Expected: "Run analytics"

    # Also, direct comparison should work
    print(job3 < job2) # Expected: True
```
   
<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ For Python's sort() or sorted() to work on custom objects without a key function, the objects must be comparable. This requires implementing rich comparison methods (like __lt__ and __eq__).

​Reasonable Wrong Turn:​ Providing a lambda function as the key to the sort method inside run_next_job (e.g., list.sort(key=lambda j: j.priority)). While functional, this avoids making the Job objects themselves comparable, which is the core task.

</details>


<details> 
<summary>Possible Solution</summary> 
</details>

### Problem 5, ​Task Type:​ write code

Create a JSONExportable class that provides a to_json method. This method should convert the public instance attributes of an object into a JSON string. Then, design two unrelated classes, ServerConfig and UserPreferences, with different sets of attributes. By inheriting from JSONExportable, both classes should gain the ability to be exported to JSON.

Examples of Expected Behavior:
    
```python
config = ServerConfig(host='127.0.0.1', port=8080)
print(config.to_json()) # Expected: '{"host": "127.0.0.1", "port": 8080}'

prefs = UserPreferences(theme='dark', notifications=False)
print(prefs.to_json()) # Expected: '{"theme": "dark", "notifications": false}'
```

<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ A mix-in class should not have its own __init__ method or state; it is intended only to provide behavior to the classes that use it. Its methods operate on self, which will be an instance of the inheriting class.

​Reasonable Wrong Turn:​ Trying to instantiate the JSONExportable class directly, or giving it an __init__ method that conflicts with the __init__ methods of the classes that use it.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 6, ​Task Type:​ debug existing code

The EventManager class below is designed to only allow listeners (callables) to be added, not removed, and to prevent the list of listeners from being modified directly. However, the protection is flawed. Your task is to demonstrate the flaw and explain how to fix the code.

```python
        class EventManager:
        def __init__(self):
            self._listeners = []

        def add_listener(self, listener):
            if callable(listener):
                self._listeners.append(listener)

        def get_listeners(self):
            return self._listeners

        def trigger_event(self, event_name):
            for listener in self._listeners:
                listener(event_name)

```

​Examples of Expected Behavior:

```python        
def my_listener(name):
    print(f"Event '{name}' triggered!")

manager = EventManager()
manager.add_listener(my_listener)

# Demonstrate the flaw here to modify the internal list
listeners = manager.get_listeners()
listeners.clear()

# After the flaw is exploited, this should do nothing
manager.trigger_event("user_login") # Expected: (no output)
```

<details> 
<summary>Hidden Trap</summary> 

Hidden Trap:​ Returning a reference to a mutable internal object (self._listeners) allows the caller to modify the object's state, breaking encapsulation.

​Reasonable Wrong Turn:​ Suggesting the use of name mangling (__listeners) as the fix. While that makes direct access harder, it doesn't solve the core problem of the get_listeners method returning a mutable reference.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 7, ​Task Type:​ explain behavior

Consider the ResourcePool and Connection classes below. Explain step-by-step why the expression 'conn_2' in pool evaluates to True. Specifically, which method makes this possible, and how does the in operator use it?
       
```python
     class Connection:
        def __init__(self, conn_id):
            self.id = conn_id
        def __repr__(self):
            return f"<Connection id={self.id}>"
        def __eq__(self, other):
            if isinstance(other, str):
                return self.id == other
            if isinstance(other, Connection):
                return self.id == other.id
            return NotImplemented

    class ResourcePool:
        def __init__(self, connections):
            self._connections = connections

        def __iter__(self):
            return iter(self._connections)

    pool = ResourcePool([Connection('conn_1'), Connection('conn_2')])
    print('conn_2' in pool)
```

 ​Examples of Expected Behavior:​ The final line prints `True`.

<details> 
<summary>Hidden Trap</summary> 

Hidden Trap:​ The in operator has a fallback mechanism. If the object's class does not define a __contains__ method, Python will use the __iter__ method to iterate over the object and check each item for equality.

​Reasonable Wrong Turn:​ Stating that ResourcePool must have a __contains__ method. Another wrong turn is failing to mention that the __eq__ method in Connection is what allows the comparison between a Connection object and the string 'conn_2' to succeed.

</details>


<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 8, ​Task Type:​ write code

Create a File class that represents a file with name and size (in bytes). Create a Directory class that holds a collection of File objects. Implement the necessary logic so that adding two Directory objects results in a new Directory containing the files from both. Furthermore, implement a method so that the built-in len() function, when called on a Directory instance, returns the ​total size​ of all files within it, not the number of files.

​Examples of Expected Behavior:
```python
    
    dir1 = Directory([File("doc1.txt", 100), File("img1.png", 1500)])
    dir2 = Directory([File("doc2.txt", 250)])

    new_dir = dir1 + dir2
    print(len(new_dir.files)) # Expected: 3

    print(len(dir1))  # Expected: 1600
    print(len(new_dir)) # Expected: 1850
```



<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ Implementing __add__ to handle the composition of two Directory objects and __len__ to provide a custom meaning for the length of a Directory.

​Reasonable Wrong Turn:​ For __len__, returning len(self.files) which would give the number of files instead of the total size, failing to meet the requirement. For __add__, modifying self.files instead of creating a new Directory instance.

</details>


<details> 
<summary>Possible Solution</summary> 
</details>


***

### Problem 9, ​Task Type:​ write code

Design a system to manage the state of a network connection. Create a ConnectionManager class. The manager's open() and close() methods should delegate their behavior to a separate "state" object. Create two different state classes, ConnectedState and DisconnectedState. The ConnectionManager should hold an instance of one of these state classes. When a method like open() is called on the manager, it should invoke a corresponding method on its current state object. The state object is then responsible for performing the action and telling the manager to transition to a new state if necessary.


​Examples of Expected behavior:

```python

    manager = ConnectionManager()
    print(f"Initial state: {manager.current_state_name}")
    # Expected: Initial state: DisconnectedState

    manager.open()
    print(f"State after open: {manager.current_state_name}")
    # Expected: State after open: ConnectedState

    # Calling open() again should have no effect
    manager.open()
    print(f"State after second open: {manager.current_state_name}")
    # Expected: State after second open: ConnectedState

    manager.close()
    print(f"State after close: {manager.current_state_name}")
    # Expected: State after close: DisconnectedState
```


<details> 
<summary>Hidden Trap</summary> 

Hidden Trap:​ The state objects (ConnectedState, DisconnectedState) need a way to change the state of the ConnectionManager. This means the manager must pass a reference to itself (self) to the state objects when it calls their methods, allowing the collaborator to modify the original object.

​Reasonable Wrong Turn:​ Placing all the logic inside the ConnectionManager using if/else statements based on a simple string attribute like self.state = "connected". This approach avoids using collaborating state objects, which is the central requirement of the problem.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 10, ​Task Type:​ write code

Create a TimeValue class holding a numeric value and a unit (e.g., "seconds", "minutes"). Create a Multiplier class that holds only a numeric factor. Implement the system so that a TimeValue can be multiplied by a Multiplier in any order (time_value * multiplier or multiplier * time_value). The result should always be a new TimeValue object with its value adjusted. Multiplying two TimeValue objects should be an invalid operation and raise an error.

​Examples of Expected Behavior:

```python

    duration = TimeValue(60, "seconds")
    factor = Multiplier(5)

    result1 = duration * factor
    print(result1) # Expected: <TimeValue: 300 seconds>

    result2 = factor * duration
    print(result2) # Expected: <TimeValue: 300 seconds>

    try:
        duration * duration
    except TypeError as e:
        print(e) # Expected: Meaningful error message
```


<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ This requires implementing __mul__ to handle the TimeValue * Multiplier case and __rmul__ to handle the Multiplier * TimeValue case. Proper type checking inside these methods is crucial.

​Reasonable Wrong Turn:​ Only implementing __mul__. This would cause factor * duration to fail with a TypeError because the Multiplier class doesn't know how to multiply itself by a TimeValue.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 11, ​Task Type:​ write code

Create a CommandHistory class that stores a list of command strings. Create an Editor class that uses a CommandHistory object to store its actions. Then, create a Reversible mix-in that provides add_command and undo_last_command methods. This mix-in should not create its own history storage; instead, it must assume that any class using it will provide an attribute named self.history which is a CommandHistory instance. Use this mix-in to give the Editor class its functionality.

​Examples of Expected Behavior:

```python

    editor = Editor()
    editor.add_command("TYPE 'hello'")
    editor.add_command("DELETE 2")
    print(editor.history.get_commands()) # Expected: ["TYPE 'hello'", "DELETE 2"]

    editor.undo_last_command()
    print(editor.history.get_commands()) # Expected: ["TYPE 'hello'"]
```
    



<details> 
<summary>Hidden Trap</summary> 

Hidden Trap:​ The mix-in defines a "protocol"—it requires any consuming class to provide a self.history attribute that behaves in a certain way. This shows how mix-ins can depend on the structure of the class they are mixed into.

​Reasonable Wrong Turn:​ Putting the history list (self.history = CommandHistory()) inside the mix-in's __init__. If multiple classes used this mix-in, they could inadvertently share the same CommandHistory object, causing bugs.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 12, ​Task Type:​ write code

You are given a BaseSettings class and an OverrideSettings class. An OverrideSettings object is initialized with a BaseSettings object. When a setting is requested from an OverrideSettings instance, it should first check if it has the setting itself. If not, it must delegate the request to its BaseSettings object. Implement this behavior using a magic method so that settings can be accessed using dictionary-style square brackets ([]).
​Examples of Expected Behavior:
    
```python

    base = BaseSettings({'font_size': 12, 'theme': 'light'})
    override = OverrideSettings(base, {'theme': 'dark', 'show_toolbar': True})

    print(override['theme'])         # Expected: 'dark'
    print(override['font_size'])     # Expected: 12 (from base)
    print(override['show_toolbar'])  # Expected: True (from override)
```
 
<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ Implementing __getitem__ in the OverrideSettings class to create the specified lookup chain (self then collaborator).

​Reasonable Wrong Turn:​ Manually creating methods like get_setting(key) instead of using the __getitem__ magic method, which would not allow the more idiomatic override['key'] syntax.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>


### Problem 13, ​Task Type:​ explain behavior

A developer is using a Lockable mix-in to provide locking behavior for a LimitedResource class. However, when they try to check if the resource is locked, the program fails with an AttributeError.

Explain why the error occurs and how to fix the LimitedResource class ​without changing the Lockable mix-in​.

```python
class Lockable:
    """A mix-in to provide locking behavior."""
    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False

    def is_locked(self):
        return self._locked

class LimitedResource(Lockable):
    def __init__(self, res_id):
        self.resource_id = res_id
        # Note: The state required by the Lockable mix-in is not initialized here.

# --- Main execution ---
resource = LimitedResource(101)

# The following line raises an AttributeError
print(resource.is_locked())
```

<details> 
<summary>Hidden trap</summary> 

Hidden Trap:​ The problem tests the implicit contract between a mix-in and the class that uses it. The Lockable mix-in provides behaviors that depend on an instance variable (_locked), but following convention, it is stateless and lacks an __init__ method. The hidden requirement is for the student to recognize that the consuming class, LimitedResource, is responsible for initializing any state that the mix-in's methods rely on. The error occurs because the instance variable is read before it has been created.

Reasonable Wrong Turn:​ A student might focus on inheritance and method resolution order. They might correctly identify that is_locked is found in the Lockable mix-in but incorrectly conclude that the mix-in itself is flawed because it doesn't initialize its own state. This could lead them to suggest adding an __init__ method to Lockable, which violates the problem's constraint and misunderstands the design pattern that mix-ins are often stateless helpers, as discussed in the Mix-Ins assignment.


</details>

<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 14, ​Task Type:​ write code

Design a Publisher and Subscriber system. The Publisher class should maintain a list of subscriber objects. It needs a notify method that iterates through its subscribers and calls an update method on each one, passing a message. Create two different Subscriber classes, EmailNotifier and SMSNotifier, that are not related. Both must have an update(message) method. The Publisher should work with any object that has an update method, regardless of its class.

​Examples of Expected Behavior:

```python

    publisher = Publisher()
    email_sub = EmailNotifier('test@example.com')
    sms_sub = SMSNotifier('555-1234')

    publisher.subscribe(email_sub)
    publisher.subscribe(sms_sub)

    publisher.notify("System is going down for maintenance.")
    # Expected output:
    # Sending email to test@example.com: System is going down for maintenance.
    # Sending SMS to 555-1234: System is going down for maintenance.
```

<details> 
<summary>Hidden Trap</summary>  

​Hidden Trap:​ This is a classic example of the Observer pattern, which relies on duck typing. The Publisher should not care about the type of its subscribers, only that they respond to the update message.

​Reasonable Wrong Turn:​ Adding type checks in the Publisher's subscribe or notify methods, which would make the system rigid and defeat the purpose of a polymorphic design.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 15, ​Task Type:​ write code

You have Vector and Matrix classes. A vector can be represented as a list of numbers, and a matrix as a list of lists.
Implement the multiplication logic so that matrix * vector performs correct matrix-vector multiplication and returns a new Vector object. Assume valid dimensions.

​Examples of Expected Behavior:
```python
    
# Represents the matrix:
# | 1 2 |
# | 3 4 |
m = Matrix([[1, 2], [3, 4]])
# Represents the vector [10, 20]
v = Vector([10, 20])

# Result should be [(1*10 + 2*20), (3*10 + 4*20)] = [50, 110]
result_vector = m * v
print(result_vector) # Expected: <Vector: [50, 110]>
print(isinstance(result_vector, Vector)) # Expected: True
```

<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ Implementing the __mul__ method in the Matrix class to handle an operand of type Vector. The logic involves iterating through rows of the matrix and computing the dot product with the vector.

​Reasonable Wrong Turn:​ Trying to implement __mul__ on the Vector class. While vector * matrix could be defined, the standard mathematical convention is matrix * vector, making Matrix.__mul__ the more natural place for the implementation.

</details>


<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 16, ​Task Type:​ debug existing code

The code below attempts to use multiple inheritance to create a SecureFileTransmitter. The LoggedTransmitter should log before transmitting, and the EncryptedTransmitter should encrypt before transmitting. Due to the way super() is called, the logging step is skipped. Debug the code and fix the super() calls so that all parent methods in the chain are called correctly.

```python
        class BaseTransmitter:
        def transmit(self, data):
            print(f"Transmitting: {data}")

    class EncryptedTransmitter(BaseTransmitter):
        def transmit(self, data):
            encrypted_data = f"encrypted({data})"
            # Incorrect super() call
            BaseTransmitter.transmit(self, encrypted_data)

    class LoggedTransmitter(BaseTransmitter):
        def transmit(self, data):
            print("LOG: Preparing to transmit.")
            # Incorrect super() call
            BaseTransmitter.transmit(self, data)

    class SecureFileTransmitter(LoggedTransmitter, EncryptedTransmitter):
        pass

    transmitter = SecureFileTransmitter()
    transmitter.transmit("my_file.txt")
    # Current (wrong) output:
    # LOG: Preparing to transmit.
    # Transmitting: my_file.txt
    #
    # Expected (correct) output:
    # LOG: Preparing to transmit.
    # Transmitting: encrypted(my_file.txt)
```

<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ In a multiple inheritance scenario, hardcoding the parent class in super() (e.g., BaseTransmitter.transmit(...)) breaks the Method Resolution Order (MRO). The fix is to use the no-argument super().transmit(...), which correctly follows the MRO chain.

​Reasonable Wrong Turn:​ Rearranging the base classes in SecureFileTransmitter's definition.
While this changes the behavior, it doesn't fix the underlying incorrect super() calls which is the root cause of the bug.
</details>

<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 17, ​Task Type:​ explain behavior

A developer has used name mangling (__api_key) in the ExternalService class, thinking it provides strong security. Explain why this is not a security feature and demonstrate how a user of the class can still access and modify the __api_key attribute directly from outside the class instance.

```python

    class ExternalService:
        def __init__(self, key):
            self.__api_key = key

        def connect(self):
            print(f"Connecting with key: {self.__api_key}")
```

​Examples of Expected Behavior:
```python

service = ExternalService("ABC-123")
service.connect() # Prints "Connecting with key: ABC-123"

# Write code here that accesses and changes the key
# e.g., service._ExternalService__api_key = "DEF-456"

service.connect() # Should now print "Connecting with key: DEF-456"
```      

<details> 
<summary>Possible Solution</summary> 

​Hidden Trap:​ Name mangling is a mechanism to avoid accidental name collisions in subclasses, not a security or privacy feature. The mangled name is predictable (_ClassName__attributeName).

​Reasonable Wrong Turn:​ Believing that name mangling makes the attribute truly private and inaccessible, and then struggling to find a way to access it without knowing the name-mangling convention.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 18, ​Task Type:​ write code

Design a system for processing a pipeline of operations on a dataset. Create an Operation base class with an abstract execute method. Create two concrete operation classes, FilterOperation and TransformOperation. Then, create a Pipeline class that is initialized with a list of Operation objects. The Pipeline's run method should take initial data and pass it sequentially through each operation's execute method, where the output of one operation becomes the input for the next.

​Examples of Expected Behavior:

```python
    class FilterOperation(Operation):
        # keeps only even numbers
        def execute(self, data): return [n for n in data if n % 2 == 0]

    class TransformOperation(Operation):
        # squares each number
        def execute(self, data): return [n*n for n in data]

    pipeline = Pipeline([FilterOperation(), TransformOperation()])
    initial_data = [1, 2, 3, 4, 5, 6]
    result = pipeline.run(initial_data)
    # After filtering: [2, 4, 6]
    # After transforming: [4, 16, 36]
    print(result) # Expected: [4, 16, 36]
```
<details> 
<summary>Possible Solution</summary> 

Hidden Trap:​ This demonstrates a Chain of Responsibility or Pipeline pattern, where different but related types of objects (operations) are composed into a larger structure (Pipeline) and collaborate to achieve a result. The Pipeline relies on polymorphism to treat all operations uniformly.

​Reasonable Wrong Turn:​ Hardcoding the types of operations inside the Pipeline.run method with if/elif checks, which would make the pipeline inflexible and unable to accept new, custom operation types.
</details>


<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 19, ​Task Type:​ write code

Create an InventoryItem class that stores a name and quantity. Implement the class so that you can use the + and - operators to adjust the quantity. The operations should modify the item's quantity in-place and the item itself should be returned to allow for method chaining. Prohibit the quantity from dropping below zero; if a subtraction would result in a negative quantity, it should be set to zero instead.

​Examples of Expected Behavior:

```python
 item = InventoryItem("screws", 100)

(item + 50 - 25)
print(item.quantity) # Expected: 125

item - 200
print(item.quantity) # Expected: 0
```


<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ Implementing in-place magic methods (__iadd__, __isub__) which are expected to modify self and return it. This is different from standard arithmetic methods (__add__, __sub__) which should return a new instance.

​Reasonable Wrong Turn:​ Implementing __add__ and __sub__ instead of __iadd__ and __isub__. This would mean item = item + 50 works, but item + 50 by itself would appear to do nothing as it would return a new InventoryItem that is immediately discarded.

</details>


<details> 
<summary>Possible Solution</summary> 
</details>

***

### Problem 20, ​Task Type:​ write code

Design a simple file system representation. Create a FileSystemNode base class. Then create File and Directory classes that inherit from it. A File has a name and size. A Directory has a name and contains a collection of other FileSystemNode objects (which can be Files or other Directorys). Implement a get_total_size method for both classes. For a File, this is just its size. For a Directory, this is the sum of the sizes of all nodes it contains, calculated recursively.

​Examples of Expected Behavior:

```python
    # Build a file system structure
    root = Directory("root")
    docs = Directory("docs")
    pics = Directory("pics")
    root.add(docs)
    root.add(pics)

    docs.add(File("report.txt", 100))
    pics.add(File("cat.jpg", 500))
    pics.add(File("dog.png", 700))

    # Add a nested directory
    archive = Directory("archive")
    archive.add(File("old_report.zip", 2000))
    pics.add(archive)

    print(docs.get_total_size())      # Expected: 100
    print(archive.get_total_size())   # Expected: 2000
    print(pics.get_total_size())      # Expected: 500 + 700 + 2000 = 3200
    print(root.get_total_size())      # Expected: 100 (from docs) + 3200 (from pics) = 3300
```

<details> 
<summary>Hidden Trap</summary> 

​Hidden Trap:​ This is the Composite design pattern. The get_total_size method in the Directory class must iterate over its children and call get_total_size on each child, regardless of whether the child is a File or another Directory. This recursive collaboration is the key.

​Reasonable Wrong Turn:​ Writing the get_total_size method in Directory to only sum up File objects, forgetting that it might contain other Directory objects whose sizes must also be included. This would lead to an incomplete/incorrect total size calculation.

</details>

<details> 
<summary>Possible Solution</summary> 
</details>