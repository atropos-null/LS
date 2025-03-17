## Pass by Reference, Pass by Value

#### What does pass by "value" mean?

In C, when you "pass by value", the function only has a copy of the original object. 
Operations performed on the object within the function have no effect on the original 
object outside of the function.

If Python was pure "pass by value", that means there should be no way for operations 
within a function to cause changes to the original object. This implies that Python is 
"pass by reference", since operations within the function affected the original object.
However, not all operations affect the original object. 

Python exhibits a combination of behaviors from both "pass by reference" as well as "pass 
by value". Its behavior is described as pass by object reference as you are actually 
passing a reference to the object (value) rather than a copy of the object itself. 
However, whether the function can modify the object depends on whether the object is 
mutable or immutable.

The important thing to remember is that Python always passes references to objects, not 
the objects themselves. The distinction between mutable and immutable types in Python 
then dictates whether you can modify the original object through that reference.

When an operation within the function mutates the argument, it will affect the original 
object.

##### Restated via LSBOT:

These are two different parameter passing mechanisms that can cause confusion because 
they sound similar but behave differently.

**Pass-by-Reference**

In true pass-by-reference (found in languages like C++), the function parameter becomes 
an alias for the original variable. This means:
*   Any operation on the parameter (including reassignment) affects the original variable
*   You're passing a reference to the variable itself, not just to the value it contains

** Pass-by-Object-Reference (Python's model)**

In Python's pass-by-object-reference:
*   Python passes a reference to the object that a variable points to
*   The parameter becomes a new variable that references the same object
*   Reassigning the parameter will not affect the original variable
*   Mutating the object (if mutable) will affect all variables that reference it

##### Restated via the Duck

In Python, the concept of "pass by reference" and "pass by value" can be a bit different from other languages. Python uses a mechanism called "pass by object reference" or "pass by assignment."

When you pass a variable to a function in Python, you are passing a reference to the object, not the actual object itself. However, whether the object can be modified depends on its type.

Immutable objects (e.g., integers, strings, tuples): If you pass an immutable object to a function and try to modify it, you will create a new object instead. The original object remains unchanged.

Mutable objects (e.g., lists, dictionaries, sets): If you pass a mutable object to a function, you can modify the object within the function, and the changes will be reflected outside the function as well.

Another important aspect to consider is that Python's behavior can sometimes lead to confusion, especially with mutable objects. For example, if you pass a list to a function and modify it, the changes will be visible outside the function. This is because the list is mutable, and you are working with a reference to the same object.