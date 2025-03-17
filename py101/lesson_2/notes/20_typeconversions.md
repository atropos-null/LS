## Type Conversion

Type coercion is the process of converting a value of one type to another. 

### Explicit Type Coercion

Explicit type coercion occurs when a programmer intentionally employs various built-in 
functions to convert a value of one type to another.

common types:

`int()`
`float()`
`str()`

Most often, we pass a string value to the `int()` function. However, it can also accept a 
real number(floating-point numbers), bytes-like object (which we won't discuss in this 
assignment), and, surprisingly, it also won't raise an error if we pass a boolean to it.

#### A special aside bout **NaN**

Floats have a special *Not-a-Number* value nan. Not-a-Number is one of the common ways to 
represent the missing value in the data. It typically arises from operations that don't 
have a meaningful result. When explicitly coercing values to floats using the `float()` function,it's important to note how NaN is handled.

**NaN** stands for "Not-a-Number" and it's a special value used in floating-point arithmetic to represent undefined or unrepresentable results. ​NaN is not equal to anything, including itself.

Since you can't use the equality operator (==) with NaN, you need to use the math.isnan() 
function.

When will you encounter NaN?
1.  Division of zero by zero: 0/0
2.  Operations with infinity: `float('inf') - float('inf')`
3.  Taking the square root of negative numbers (when using the math module)
4.  Data analysis with missing values (often represented as NaN)
5.  When explicitly converting the string "NaN" to a float

NaN is particularly important when working with data analysis libraries like NumPy or Pandas, where it's commonly used to represent missing values in datasets.

NaN has some unique properties. For example, NaN is not equal to any value, including itself. This means that if you compare NaN to NaN using `==`, the result will be `False`. To check if a value is NaN, you can use the `math.isnan()` function or `numpy.isnan()` function. Another important thing to know about NaN is that it can propagate through calculations. For example, if you perform an operation with NaN and another number, the result will often be NaN. This can be useful for debugging, as it can help you trace where an error might have occurred in your calculations.

#### Moving on...

When you use the `print()` function to output a value, Python automatically converts the 
value to a string using the `str()` function. This makes it convenient to display variables and other values in a human-readable format without needing to explicitly call `str()`.

`print()` isn't considered to be coercion. While it does coerce its arguments to strings, 
that is done behind the scenes. It doesn't return the resulting strings; it just prints 
them.

String interpolation is a common technique for including values within a string. When you 
use interpolation, Python automatically coerces the values to strings using the `str()` 
function.

```python
name = "Karl"
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print(message)  # Output: Hello, my name is Karl and I am 30 years old.
```

The `bool()` function is used to convert values to booleans. It works with all built-in 
Python values and most non-built-in values. When using the `bool()` function, it returns 
`True` if the value is truthy (evaluates to `True` in a boolean context), and `False` if the value is falsy (evaluates to False in a boolean context).

`repr()` function returns a string representation of an object, which can be used to recreate the object using Python code.

While `str()` function can be used to convert objects to strings, these two functions serve a slightly different purpose:

`str()`: This function is used to create a string representation of an object that is meant to be human-readable. It focuses on providing a concise and user-friendly representation of the object's value. It is often used for display purposes, such as in print() and string interpolation.

`repr()`: This function is used to create an unambiguous string representation of an object that can be used to recreate the object. It is often used for debugging and development purposes. The `repr()` representation should ideally be a valid Python expression that, when evaluated, would recreate the original object.

### Implicit type coercion

Implicit type conversion, often known as automatic data type conversion, is when Python 
automatically transforms one data type into another without the programmer's direct 
instruction. This typically occurs during calculations or when mixing distinct data types.

##### Combining Integer with Float

For instance, in Python, when you conduct a calculation involving both an integer and a 
float, the system will automatically adjust the integer to a float, ensuring the outcome 
is a float as well.

##### Combining String with Non-string

Unlike many other languages, Python is not real big on coercing non-strings to strings. 
Thus, if you try to use the + operator with a string and a number, Python will raise a 
`TypeError`.

One place where non-strings are automatically converted to string is in the `print()` 
function. `print()` will implicitly convert any non-string arguments to a string before 
printing them.



