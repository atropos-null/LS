# More Stuff

A common Python technique is composing function calls, also known as composition. 
Composition occurs when a function call is used as an argument to another function call, 
which may, in turn, be passed to another function call. Composition works best when each 
of the inner functions returns an object other than None.

Method chaining is similar to function composition but applies to methods specifically 
rather than ordinary functions. You can chain as many method calls as necessary, though it 
can get messy if you chain more than 2 or 3 methods on a single line. 

```python
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper().split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']
```

Chaining only works when each method in the chain except the last returns an object with 
at least one useful method.

### Useful modules

[Math module](https://docs.python.org/3/library/math.html)  
[Date time module](https://docs.python.org/3/library/datetime.html)  

### Function Definition Order

When Python encounters a `def` statement, it merely reads the function definition into 
memory. It saves it away as an object in the heap. The function's body isn't executed 
until it's called explicitly. In this code, this read-and-save-but-don't-execute process 
occurs when Python encounters both functions.

Nested Functions:

``` python
def foo():
    def bar():
        print('BAR')

    bar() # BAR

foo()
bar() # NameError: name 'bar' is not defined
```

### Global Statements:

By default, any variable that is defined in the outer scope of a function is also available inside that function. Python assumes that all variables that are assigned a value inside a function are local variables. Even if a variable by the same name exists in an outer scope, Python will create a new local variable if the variable's name appears on the left side of an assignment. 

No matter how deeply nested we are, the global statement stipulates that the listed identifiers are to be interpreted as global variables; that is, as identifiers in the global namespace.

Unlike with the global statement, the nonlocal statement requires the named variable to already exist. You can't create the variable in the function that uses nonlocal.
