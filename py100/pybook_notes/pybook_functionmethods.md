# Functions and Methods

When Python encounters a function call, it transfers program flow to the code that 
comprises the function and executes that code. When the code finishes its work, the 
function returns a value to the code that invoked it. The calling code is free to use 
or ignore the return value as the programmer sees fit. Execution resumes from where the 
function was called.

[Python documentation on Functions](https://docs.python.org/3/library/functions.html)

#### `ord and chr`

Given a single character, `ord` returns an integer that represents the Unicode code point 
of that character. For the standard ASCII character sets, the code points refer to the 
values of the characters in the standard ASCII character set. `chr` is the inverse of ord. 
That is, it converts an integer to the corresponding Unicode character.

#### Truthy and Falsy:

The following values are said to be falsy:

* False, None
* all numeric 0 values (integers, floats, complex)
* empty strings: ''
* empty collections: [], (), {}, set(), frozenset(), and range(0)
* Custom data types can also define additional falsy value(s).

**_All other values are said to be truthy_**.

#### `any` and `all`

Two very useful built-in functions are the `any` and `all` functions. They both operate on 
iterable collections, such as lists, tuples, ranges, dictionaries, and sets. The any 
function returns `True` if any element in a collection is truthy, `False` if all of the 
elements are falsy. On the other hand, all returns `True` if all of the elements are truthy, `False` otherwise.

#### REPL only: id, dir function

In most cases, two instances of an object with the same value will always have two distinct identities. This is not always true, though. For instance, _in a process called interning, every unique integer object from -5 through 256 has the same identity_.

When used without arguments, the `dir` function returns a list of all identifiers in the 
current local scope. When used with an argument, `dir()` returns a list of the object's 
attributes (typically, the object's methods and instance variables). Use the sorted function with the output of `dir`, or import the prettyprint module.

Python programmers often add a triple-quoted string at the beginning of a function's block.
This string is a documentation comment -- a docstring -- that Python can access with its 
help() function and the __doc__ property. It has no effect on your code unless your 
program is somehow interested in the comments (which can happen):

```python
def say():
    """
    The say function prints "Hi!"
    """
    print('Hi!')

print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)
```

**Variable shadowing** in Python occurs when a variable declared within a certain scope 
(such as a function or a block) has the same name as a variable declared in an outer 
scope. The inner variable "shadows" the outer variable, meaning that within the inner 
scope, the outer variable is not accessible.

**Lexical scope**, also known as **static scope**, is a convention used by a programming language to determine the scope (visibility) of a variable. In Python, lexical scope means that the scope of a variable is determined by its location within the source code, and it is fixed at the time of writing the code.

Python uses lexical scoping to resolve variable names. This means that when you reference 
a variable in a function, Python will look for the variable's value in the local scope 
(inside the function), then in the enclosing scope (inside any enclosing functions), then 
in the global scope (at the top level of the module), and finally in the built-in scope.

A function that takes a value known as an **argument**. Arguments let you pass data from 
outside the function's scope into the function so it can access that data. You don't need 
arguments when the function doesn't need access to outside data.

The names between parentheses in the function definition are called **parameters**. You can think of parameters as placeholders for potential arguments, while arguments are the values assigned to those placeholders. Since parameters are merely placeholders, we typically talk of them as declarations: they are being used to introduce those names as local variables into a function, but don't obviously provide an immediate value until the function is called. That is, they simply declare variable names.

Arguments are objects passed to a function during invocation. Parameters are placeholders for the objects that will be passed to the function when it is invoked.

#### Return Values

All Python function calls evaluate to a value, provided the function doesn't raise an exception (an error). By default, that value is `None`; this is the implicit return value of most Python functions. However, when you use a return statement, you can return a specific value from a function. This is an explicit return value. There is no distinction between implicit and explicit return values outside the function. Still, it's important to remember that all functions return something unless they raise an exception, even if they don't explicitly execute a return statement.

Python uses the return statement to return a value to the code that invoked the function. If you don't specify a value, it returns `None`. Either way, the return statement terminates the function and returns control to the calling function.

Functions that always return a Boolean value, i.e., True or False, are called predicates.

#### Default parameters

```python

def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!   Argument not empty, default ignored.
say()        # hello!   When the argument is empty, it fills it with a default. 
```

Once you specify a default value for a parameter, all subsequent positional parameters must also have default values. It's also worth noting that you can't accept the default value for a parameter and provide an explicit value for a subsequent parameter.

#### Method invocation

Method invocations occur when you prepend an object followed by a period `(.)` to a function invocation, e.g., `'xyzzy'.upper(`).  We call such function invocations method calls. We also speak of the function as a method. 

_Use 'methods' when discussing functions explicitly designed to require calling objects._

In general, mutating the caller is acceptable practice; many built-in functions and methods do just that. However, you should avoid mutating arguments since such functions can be tough to debug and is considered poor practice. 

_Almost no built-in functions mutate their arguments_.



