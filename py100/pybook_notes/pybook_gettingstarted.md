# Getting Started

### REPL

Enter just `'python'` at the command line to enter the REPL environment. To paste code cleanly in the REPL, first press the `{F3}` key. This should change the prompt to `(paste)`. You can now paste your code. When you are done pressing, press the `{F3}` key again. 
You may need to press `{Return}` to get back to the `>>> prompt`.

### Style suggestions:

[Official style guide](https://peps.python.org/pep-0008/)

**Set your text editor to use four space characters -- not tabs -- for indentation**.

**Limit code lines and comments to 79 characters**. This guideline isn't universal, but it helps readability. Pylint will throw a fit if you don't.

Use spaces around operators, except for `**`, which should not be surrounded by spaces:

```python
print(3 + 4)    # + is an operator
print(5 * 7)    # * is an operator
print(6 - 2)    # - is an operator
print(7 / 3)    # / is an operator
print(8**3)     # ** operator is not surrounded by spaces
my_num = 3      # = is an operator
```

### `**` 

The `**` operator is used for the following:

* to raise a number to the power of another number. 
* in function definitions to pass a variable number of keyword arguments to a function.  
* to unpack dictionaries into function arguments.

### Continuation Lines:

String literals can be continued over several lines, provided you enclose all the 
string content in a set of parentheses:

```python
return ("This is a long string. "
        "It's actually very long. "
        "It spans multiple lines. "
        "Are you getting tired of this? "
        "So am I.")

return """
    This is a long string.
    It's actually very long.
    It spans multiple lines.
    Are you getting tired of this?
    So am I.
"""
```

It's worth noting that triple-quoted strings preserve leading whitespace 
and any newline characters. You also don't need parentheses.

You can use parentheses to delimit code that will be split over multiple lines:
```python
return (obj.bar1
      + obj.bar2
      + obj.bar3)
```

You can use a backslash to end any line you want to continue:
```python 
result = value1 + \
         value2 + \
         value3
```

A good rule of thumb is that you can use a backslash wherever you can put a space.
That said, you should use backslash continuations sparingly, and only where they improve readability.  You should not use backslashes when they aren't syntactically required for continuation. It's usually better to use one of the other continuation techniques.

#### Removing a full folder:

rm -R {folder}

### Suggested links:

[Python Documentation, main](https://www.python.org/doc/)
[Python Documentation, reference](https://docs.python.org/3/reference/index.html)
[Python Documentation, libraries](https://docs.python.org/3/library/index.html)
