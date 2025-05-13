## PY109 Essential Concepts

### Everything in Python is an Object

Objects in Python consist of three key components:

* **Identity**: Unique identifier of the object, remaining constant throughout the object's lifetime. 
* **Type**: Defines the type of the object (e.g., int, str, list).
* **Value**: The actual data stored in the object.

### Variables are references to objects in memory

When a variable is created in Python, it is initialized. **Variable initialization**​ is the first time a variable name is bound to a value. This creates the variable name in the current scope. **Variable assignment**​ is the operation of binding a name to an object (a value). In Python, this is done using the `=` operator. 

Initialization includes several steps that occur under the hood: 

1. **Object Creation**:

   When a value is assigned to a variable, Python first creates an object in memory to represent the value. 

2. **Memory Allocation**:

   Python allocates memory for the object in an area called the heap. The memory manager ensures that sufficient memory is allocated for storing the object’s type, value, and metadata. Some values (e.g., integers from -5 to 256, certain strings like identifiers or small immutable strings) are permanently stored using a mechanism called **memory interning** to save memory and improve performance. Note that the behavior of string interning may vary between Python implementations.

3. **Name Binding**:

   The variable name is associated with the object in memory through a reference or pointer. The name must follow Python's naming rules (e.g., cannot start with a number, cannot use reserved keywords). This binding is stored in a dictionary-like structure called the namespace (e.g., local, global, or built-in namespace). The namespace exists for each scope. 

4. **Reference Count Creation/Update**:

   An additional **reference count** is created when the object is created. It tracks how many references (variables or other objects) point to this object, which helps decide whether or not an object will persist in memory. 

   The reference count of the object is incremented or decremented according to how many references point to the object.

5. **Garbage Collection**:

   If the variable is reassigned or goes out of scope, the reference count of the original object decreases. When the reference count of an object drops to zero, Python's garbage collector reclaims the memory used by the object. While reference counting is the primary mechanism, the cyclic garbage collector specifically handles reference cycles that reference counting alone can't address. 

### Names are not Objects. They're labels that refer to objects.

**Variable reassignment**​ is when an existing variable name is bound to a new object (value). Reassignment of a variable never mutates the value it contains; it simply points to a new, different object. The previous variable may be taken out of memory with garbage collection once its reference count becomes 0.

**Variable shadowing** occurs when a variable in an inner scope (e.g., within a function) has the same name as a variable in an outer scope (e.g., global or enclosing scope). The inner variable "shadows" the outer one, making the outer variable inaccessible within the inner scope.

```python
x = f"I am in the global scope"

def shadowing():
    x = f"I am in the local scope"  # Local variable shadows the global one
    print("Inside the function:", x)

shadowing()  # This prints the local 'x'
print("Outside the function:", x)  # This prints the global 'x'
```

### Pass by Object Reference

When you pass a variable to a function in Python, the function parameter becomes a new reference to the same object that the argument variable refers to. This means Python doesn't pass the variable itself or make a copy of the object's value - it passes a reference to the object in memory. The key distinction lies in the object's mutability, which determines whether modifications within the function will affect the original object.

* For mutable objects (like lists, dictionaries), operations that modify the object will affect the original object outside the function
* For immutable objects (like integers, strings), operations that appear to modify the object actually create a new object, leaving the original unchanged.

 
### The Rules of the Scope

Each variable has a  **scope** and that scope has a namespace. A variable's scope is the region of code where that variable is valid and can be referenced. Scope can be Local, Enclosing, Global, and Built-in. 

**Global scope**: Variables defined at the top level of a program or module.
**Local scope**​: Variables defined within a function.
**Enclosing scope**​: When working with nested functions, variables from outer functions.

1.  Variables defined in a function are local to that function and cannot be accessed in the outer scope. 
2.  Functions can access variables from outer scopes for reading. When attempting to reassign an outer scope variable within a function, Python creates a new local variable instead. However, if the outer scope variable references a mutable object (like a list or dictionary), the function can modify the contents of that object without creating a local variable, and these changes will persist outside the function.
3.  To modify a global variable within a function, you must declare it with the global keyword.
4.  Peer scopes do not conflict - variables in one function are not accessible in another function at the same level.

### Expressions and Statements

An expression is any code that evaluates to a value. Statements are complete lines of code that perform an action but do not necessarily produce a value.  An expression: `True`. A statement: `x = 5` or `import math`.

### Functions

Functions in Python create a new local scope. There are function definitions that can have parameters and function calls that can have arguments. Parameters are the names assigned to a function's arguments. Arguments are the actual values that get passed to the function.

Default argument values in Python are evaluated only the first time  when the function is defined, not each time the function is called. Default function arguments in Python work differently depending on whether they are mutable or immutable objects. This means that if the default argument is a mutable object (like a list), changes to it will persist across function calls.


### Loops

The choice between loops is about selecting the most appropriate tool for readability and clarity, not about strict requirements. With that said, `for` loops are used to iterate over a sequence (like a list, tuple, string) or other iterable objects. `while` loops continue executing as long as a condition remains `True`.

### Slicing is mutating

start  - that exact index number
stop   - functionally, index number - 1

Note that the length of the replacement list does not need to match the length of the slice being replaced. Python automatically adjusts the list size to accommodate the change.


### Return Values

#### When empty...

##### Return Empty Strings:
- `capitalize()`
- `.upper()`
- `.lower()`
- `.swapcase()`
- `.title()`
- `.strip()`
- `.rstrip()`
- `.lstrip()`
- `replace()`

##### Return `False` for empty strings:
- `.isalpha()`
- `.isdigit()`
- `.isalnum()`
- `.islower()`
- `.isupper()`
- `.isspace()`

##### Returns empty list for empty string:
- `.split()`

#### When not empty...

##### Returns indices:
- `.find()` - Returns the lowest index of the substring (or `-1` if not found)
- `.rfind()` - Returns the highest index of the substring (or `-1` if not found)

##### Returns `None`:
- Functions without an explicit return statement
- List modification methods:
  - `.append()`
  - `.reverse()`
  - `.extend()`
  - `.remove()`
  - `clear()`
  - `.sort()`
  - `reverses()`

##### Returns the removed item:
- `pop()`

##### Return the value:
- `and`
- `or`

