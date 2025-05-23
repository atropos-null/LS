# Variables

Programs must store information in memory to use and manipulate it, 
and variables are the way to do that.

##### Naming conventions for most identifiers (excluding constant and class names)

* Use snake_case formatting for these names.
* Names may contain lowercase letters (a-z), digits (0-9), and underscores (_).
* Names should begin with a letter.
* If the name has multiple words, separate the words with a single underscore (_).
* Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used.
* Names may only use letters and digits from the standard ASCII character set.

##### Constant names (unchanging named values):

* Use SCREAMING_SNAKE_CASE formatting for these names.
* Names may contain uppercase letters (A-Z), digits (0-9), and underscores (_).
* Names should begin with a letter.
* If the name has multiple words, separate the words with a single underscore (_).
* Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used.
* Names may only use letters and digits from the standard ASCII character set.

##### Class names

* Use PascalCase formatting for these names. PascalCase is sometimes called CamelCase (with both Cs capitalized).
* Names may contain uppercase and lowercase letters (A-Z, a-z) and digits (0-9).
* Names should begin with an uppercase letter.
* If the name has multiple words, capitalize each word.

Constants are usually defined in the global scope. The definitions are usually written at 
the top of the program file, just below any imports. You can use constants anywhere, but 
they should be defined globally. Python does not support true constants. Instead, the 
SCREAMING_SNAKE_CASE naming convention is solely for programmers. 

**Augmented assignment** take the current value of a variable, perform an arithmetic 
operation on the variable's value, and then reassign the variable to the newly computed 
value.

Without augmented assignment:
```python 
foo = 42            # foo is 42
foo = foo - 2       # foo is now 40
foo = foo * 3       # foo is now 120
foo = foo + 5       # foo is now 125
foo = foo // 25     # foo is now 5
foo = foo / 2       # foo is now 2.5
foo = foo**3        # foo is now 15.625
print(foo)          # prints 15.625
```

With augmented assignment:

```python
foo = 42            # foo is 42
foo -= 2            # foo is now 40
foo *= 3            # foo is now 120
foo += 5            # foo is now 125
foo //= 25          # foo is now 5
foo /= 2            # foo is now 2.5
foo **= 3           # foo is now 15.625
print(foo)          # prints 15.625
```

Also works with strings, lists, and sets 

```python
bar = 'xyz'          # bar is 'xyz'
bar += 'abc'         # bar is now 'xyzabc'
bar *= 2             # bar is now 'xyzabcxyzabc'
print(bar)           # prints xyzabcxyzabc
```

Note that augmented assignment is a statement, not an expression. 
Thus, you can't use augmented assignment as a function argument or return value

### Reassignment vs. Mutation

There are two ways to change things in Python and most other programming languages. 
You can change the binding of the variable by making it reference a new object, or you 
can change the value of the object assigned (bound) to the variable. The former is known 
as reassignment while the latter is known as mutation. Reassignment makes that name refer 
to a different object somewhere else in memory. Mutation, on the other hand, does not 
change which object the variable refers to. Instead, it changes the object itself. After 
mutating an object assigned to a specific variable, the variable continues to refer to the 
same object (albeit altered) at the same memory location. Reassigning an element of a mutable collection doesn't reassign the variable; it mutates the collection.


In Python, variables initialized inside an `if`, `match`, `while`, `for`, `with`, or `try` statement are accessible outside of that block of code.  Variables initialized in the same scope where a block begins can be accessed inside the block.

In this code:

```python
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)
```

In this code, the global keyword tells the function to assume that a refers to the 
global variable a. This means that any operation on the variable a inside this function 
will affect the global variable a, not a local one.