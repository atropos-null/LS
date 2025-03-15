# Basic Operations

## Arithmetic operations:

```
+            Addition
-            Subtraction
*            Multiplication
/            Division
//           Integer division
%            Modulo
**           Exponentiation
```

The `//` operator returns the largest whole number less than or equal to the floating point result. That is, it rounds the result down to the nearest whole number. The `//` operator doesn't work with the built-in complex numbers. A single `/` always returns a floating point number.

The `%` operator is usually used to calculate the remainder of dividing two integers. The result has the same sign as the divisor.

Floating point, early thoughts: Note that you should always use strings with decimal.

```python
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3')
# True
```

### Equality Comparison: == and !=

 `==` compares two operands for equality and returns True or False as appropriate. 
 `!=` returns True if they are not equal, False otherwise.

_The operators `==` and `!=` work with almost all data types._

If a and b have different data types, `a == b` usually returns False while `a != b` returns True. However, numbers are an exception: all built-in and standard number types can be compared for equality without regard to their specific types. Thus, `1 == 1.0` is True.

### Ordered Comparison:

```
 < : less than 
 <= : less than or equal to 
 > : greater than
 >= : greater than or equal to
```

Strings are compared lexicographically, which means they are compared character-by-character from left-to-right. Only the first character of each string gets compared. When Python compares two strings that are equal up to the length of the shorter string, then the shorter string is deemed to be less than the longer string. When comparing strings, Python stops as soon as it makes a decision, so not all of the length may be checked. Every uppercase letter is less than every lowercase letter; numeric characters in a string are less than alphabetic characters. Strings with numbers in them are compared character by character.

Comparison can be used to evaluate sets and subsets as well as lists and tuples.

## String Concatenation:

_Because it's strings and not numbers_

```python
'1' + '2' = '12'
'fu' + 'gees' = 'fugees'
```

Use the `*` operator to perform repetitive concatenation. For instance, if you want the string `'abcabcabc'` you can use `*` to generate it:

```python
print('abc' * 3)              # 'abcabcabc'
print(3 * 'abc')              # 'abcabcabc'
```

## Coercion: Making a variable switch types

### Explicit Coercion:

```python
int('5')             # 5
float('3.141592')    # 3.141592
str(5)
str(3.141592)
```

### Implicit Coercion:

For instance, when you use `print()` to print an object -- any object -- print will _implicitly coerce_ it to a string before printing it.

**Type A    Type B       Result type**
```
int         float        float
int         Decimal      Decimal
int         Fraction     Fraction
float       Decimal      --error--
float       Fraction     float
Decimal     Fraction     --error--
```

### (Unnecessary) Explicit coercion

```python
print(str(3))           # 3
print(str(False))       # False
print(str([1, 2, 3]))   # [1, 2, 3]
print(str({4, 5, 6}))   # {4, 5, 6}
```

### Implicit coercion

```python
print(3)                # 3
print(False)            # False
print([1, 2, 3])        # [1, 2, 3]
print({4, 5, 6})        # {4, 5, 6}
```

Python implicitly coerces `True` to the integer value 1 and `False` to 0. 

### Determining Types:

```python
print(type(1))         # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type('abc'))     # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
print(type(None))      # <class 'NoneType'>

foo = 42               # Variables work, too
print(type(foo))       # <class 'int'>
```

### Class types:

```python
print(type('abc').__name__)   # str
print(type(False).__name__)   # bool
print(type([]).__name__)      # list
```

### Is operator:

```python
print(type('abc') is str)     # True
print(type('abc') is int)     # False
print(type(False) is bool)    # True
print(type([]) is list)       # True
print(type([]) is set)        # False
```

### Is instance:

```python
print(isinstance('abc', str))    # True
print(isinstance([], set))       # False
```

### String Representation:

`str()` is used for creating a human-readable representation of an object.
`repr()` is used for creating a more detailed and unambiguous representation of an object, useful for debugging.

### Collection and String Lengths:

What collection types have lengths? strings, sequences, mappings, and sets
How do you determine lengths? `len()`

### Using [] to Update Elements: 

Since they are mutable, lists and dictionaries let you use the `[]` operator to replace collection elements. As you might expect, lists use indexes to update elements, while dictionaries use keys. You cannot use `[]` to create new list elements, but you can do so with dictionaries. (Append is what you use with lists, which adds a single element to the end of a list.)

### Expressions vs Statements:

Expressions always return a value; statements do not. Expressions are often part of statements. For example, in the statement `y = x + 5`, `x + 5` is an expression.

Statements often represent bigger chunks of functionality like loops or conditionals; expressions deal with determining values.

**What types can be called an expression?** Literals, Variable references (when previously defined), arithmetic operations, comparison operations, string operations, function calls.

**What types can be called a statement?** Assignment, control flow (if, else, elif, while, for etc), return statements, import statements.

```python
my_number = 3
```
`my_number = 3` is a statement that assigns the value 3 to the variable `my_number`.
The value `3` itself is an **expression**. 

_Code appearing to the right of an `=` in an assignment or reassignment is an **expression**._

### Expression Evaluation:

Parenthesized sub-expressions are usually evaluated before any non-parenthesized sub-expressions. Nested parenthesized sub-expressions are evaluated before the parenthesized expressions they are contained in.