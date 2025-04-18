## Errors

When Python encounters an error, Instead, it creates an Exception object that describes 
the problem and stops the program.

When an error occurs in a Python program, we say that it raises an Exception.

`NameError` arises when you attempt to use a variable or function that hasn't been defined.

`TypeError` occurs when a value of the wrong type is used in an expression, including:
    * using an argument of the wrong type as a function argument
    * trying to call an object that isn't callable

`SyntaxError` occurs when Python encounters code that does not meet its syntactic rules.
A `SyntaxError` is unique in that it typically arises immediately after loading a Python 
program but before it starts running. Unlike `NameError` and `TypeError`, which hinge on 
specific variables and values encountered during runtime, Python detects `SyntaxErrors `
solely from the program's text.

`ValueError` is raised when a function receives an argument of the correct data type, but 
the value of the argument is inappropriate for the operation.

`IndexError` occurs when trying to access an index of a sequence (like a list or string) 
that is outside the range of valid indexes.

`KeyError` is raised when trying to access a dictionary key that doesn't exist.

`ZeroDivisionError` occurs when attempting to divide by zero or when trying to use 0 on the right side of the modulo (`%`) operator.

#### Exception handling

Python provides a structured way to handle exceptions using the `try`, `except`, `else`, and `finally` statements.

`try` block: The code that might raise an exception is placed within the try block. Python 
will monitor this block for any exceptions that may occur during its execution.

`except` block: If an exception is raised in the `try` block, Python will look for a matching except block that can handle that specific type of exception. If a match is found, the code within the corresponding except block is executed.

`else` block (Optional): The `else` block is executed only if no exceptions occurred in the `try` block. It's used for code that should run when no errors were encountered.

`finally` block (Optional): The `finally` block is always executed, regardless of whether an exception was raised or not. It is used for cleanup operations or tasks that must be 
performed, such as releasing resources.

```python
try:
    num_str = input("Enter a number: ")
    num = int(num_str)

    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Exception handling complete.")
```
