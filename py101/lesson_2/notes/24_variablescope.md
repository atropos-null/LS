## Variable Scope

#### Global Scope

In Python, variables initialized outside of any function have a global scope. This means 
they can be accessed from anywhere in your program, including inside functions.

#### Local Scope

**Rule 1**: Variables defined in a function are local to that function and cannot be accessed in the outer scope.

**Rule 2**: Variables that are defined within a function are local unless explicitly marked as global or nonlocal.

```python
def my_func():
    global global_var
    global_var = 20
```

The global keyword is used inside the `my_func` function to indicate that the `global_var` 
being modified is the global variable, not a local one. 

**Rule 3**: Variables used but not reassigned in a function may be in the outer scope.

**Rule 4**: Peer scopes do not conflict.

**Rule 5**: Nested functions have their own scope.

