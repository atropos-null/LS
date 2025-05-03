## PY109 Essential Concepts

### Variables are references to objects in memory

When a variable is created in Python, it is initialized. **Variable initialization**​ is the first time a variable name is bound to a value. This creates the variable name in the current scope. **Variable assignment**​ is the operation of binding a name to an object (a value). In Python, this is done using the `=` operator. 

Initialization includes several steps that occur under the hood: 

1. Object Creation:

When a value is assigned to a variable Python first creates an object in memory to represent the value. Objects in Python consist of three key components:

*  **Identity**: Unique identifier of the object, remaining constant throughout the object's lifetime. 
* **Type**: Defines the type of the object (e.g., int, str, list).
* **Value**: The actual data stored in the object.

Further Details:

* Mutability: The mutability of a variable depends on the type of object it references. Immutable objects: `int`, `str`, `tuple` (cannot be changed after creation). Mutable objects: `list`, `dict`, `set` (can be modified in place).

* Scope: A variable's scope is the region of code where that variable is valid and can be referenced. Scope can be Local, Enclosing, Global, and Built-in. 

2. Memory Allocation:

Python allocates memory for the object in an area called the heap. The memory manager ensures that sufficient memory is allocated for storing the object’s type, value, and metadata. Some values are permanently stored, known as Memory Interning. 

3. Name Binding:

The variable name is associated with the object in memory through a reference or pointer. The name must follow Python's naming rules (e.g., cannot start with a number, cannot use reserved keywords). This binding is stored in a dictionary-like structure called the namespace (e.g., local, global, or built-in namespace).

**Variable reassignment**​ is when an existing variable name is bound to a new object (value). Reassignment of a variable never mutates the value it contains, it just pointing to a new, different object. The previous variable may be taken out of memory with garbage collection once its reference count becomes 0. 

4. Reference Count Creation/Update:

An additional **Reference Count** is also created when the object is created. It tracks how many references (variables or other objects) point to this object, which will help to decide whether or not an object will persist in memory. 

The reference count of the object is incremented or decremented according to how many references point to the object. 

5. Garbage Collection (if necessary):

If the variable is reassigned or goes out of scope, the reference count of the original object decreases. When the reference count of an object drops to zero, Python's garbage collector reclaims the memory used by the object. While not relevant to PY109, it's worth noting that Python also has a cyclic garbage collector that handles reference cycles

### Names are not Objects. It's a label that refers to the object.

**Variable shadowing** occurs when a variable in an inner scope has the same name as a variable in an outer scope, effectively "hiding" the outer variable.

### Pass by Object Reference

When you pass a variable to a function, the function parameter becomes a new reference to the same object that the argument variable points to, not the variable itself.  An independent copy of that variable is not created, as you see in pass by value languages.  Whether modifications inside the function affect the original object depends on whether the object is mutable or immutable.

