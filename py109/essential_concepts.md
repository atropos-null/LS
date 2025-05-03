## PY109 Essential Concepts

### Variable Process

When a variable is created in Python, several steps occur under the hood. Python variables are essentially references to objects in memory. Steps that occur when a variable is created in Python:

1. Object Creation:

When a value is assigned to a variable Python first creates an object in memory to represent the value. Objects in Python consist of three key components:
* **Identity**: Unique identifier of the object, remaining constant throughout the object's lifetime. 
* **Type**: Defines the type of the object (e.g., int, str, list).
* **Value**: The actual data stored in the object.


2. Memory Allocation:

Python allocates memory for the object in an area called the heap. The memory manager ensures that sufficient memory is allocated for storing the object’s type, value, and metadata.

3. Name Binding:

The variable name is associated with the object in memory through a reference or pointer.
This binding is stored in a dictionary-like structure called the namespace (e.g., local, global, or built-in namespace).

4. Reference Count Creation/Update:

An additional **Reference Count** is also created once the object is created. It tracks how many references (variables or other objects) point to this object, which will help decide whether or not an object persists in memory. 

The reference count of the object is incremented or decremented according to how many references point to the object. 

5. Garbage Collection (if necessary):

If the variable is reassigned or goes out of scope, the reference count of the original object decreases. When the reference count of an object drops to zero, Python's garbage collector reclaims the memory used by the object.

### Essential Qualities of Every Variable:

**Name**:

A variable has a name that acts as a reference to an object.The name must follow Python's naming rules (e.g., cannot start with a number, cannot use reserved keywords).

**Type**:

Every variable references an object that has a specific type (e.g., `int`, `float`, `str`, `list`). Python is dynamically typed, meaning the type of the variable is determined at runtime when it is assigned.

**Value**:

A variable references an object that contains a specific value (e.g., 10, "hello", [1, 2, 3]).

**Scope**:

A variable has a scope that determines where in the code it can be accessed (e.g., local, global, or nonlocal scope). 

Assignment statements in the local function cannot change variables defined outside the function.

While you can access global variables from inside functions, you cannot reassign them without using the global keyword

**Namespace Association**:

Variables exist within a specific namespace (e.g., a function's local namespace or the global namespace).

**Mutability (of the Object)**:

The mutability of a variable depends on the type of object it references. 

Immutable objects: `int`, `str`, `tuple` (cannot be changed after creation).

Mutable objects: `list`, `dict`, `set` (can be modified in place).

Reassignment of a variable never mutates the value it contains, it just pointing to a new, different object. The previous variable may be taken out of memory with garbage collection once its reference count becomes 0. 

**Variable shadowing** occurs when a variable in an inner scope has the same name as a variable in an outer scope, effectively "hiding" the outer variable.

### Pass by Object Reference

When you pass a variable to a function, the function parameter becomes a new reference to the same object that the argument variable points to, not the variable itself.  An independent copy of that variable is not created, as you see in pass by value languages.  Whether modifications inside the function affect the original object depends on whether the object is mutable or immutable.

