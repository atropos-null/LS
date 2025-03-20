# Study Guide for PY109 Exam

[Page Link for the study guide](https://launchschool.com/lessons/1318de4f/assignments/ff1c7aa8)

***

### Naming Conventions: legal vs. idiomatic, illegal vs. non-idiomatic

Legal names​ in Python:

* Can contain letters, numbers, and underscores
* Must start with a letter or underscore (not a number)
* Cannot be Python keywords (like if, for, while, etc.)

Illegal names​ violate these rules, such as:

* Names starting with numbers (1variable)
* Names containing spaces
* Names containing any other character that is not underscore (my-variable, variable!)
* Names that are Python keywords (if, class, for)

#### Idiomatic vs. Non-idiomatic Naming Conventions

Idiomatic naming refers to Python's style guide [PEP8](https://peps.python.org/pep-0008/), while non-idiomatic naming doesn't. According to the ["PY101 - Coding Tips" lesson](https://launchschool.com/lessons/a29e9831/assignments/73146c1c), idiomatic names depend on what you're naming:

* Variables and functions​: Use snake_case (lowercase with underscores)
* ​Constants​: Use UPPER_SNAKE_CASE (all uppercase with underscores)
* ​Classes​: Use PascalCase (also called CamelCase or upper CamelCase)

```python

# Idiomatic
user_name = "John"              # Variable (snake_case)
total_score = 42                # descriptive names
temp_value = calculate_total()      #snake case with verb at the front
def convert_to_celsius(fahrenheit): #snake case with verb at the front
    return (fahrenheit - 32) * 5/9 

MAX_USERS = 100                 # Constant (SCREAMING_SNAKE_CASE)
PI = 3.14159                    # Constant (SCREAMING_SNAKE_CASE)
DATABASE_URL = 
"postgresql://localhost:5432"   # Constant (SCREAMING_SNAKE_CASE)

class UserAccount:              # Class (PascalCase)
    pass
class UserAuthentication:       # Class (PascalCase)
    pass
```

**Non-idiomatic naming**​ refers to names that, while legally valid in Python (the code will run), don't follow Python's style conventions. 

```python
# Non-idiomatic (but legal)
userName = "John"        # camelCase for variables is not Python's style
Max_Users = 100          # Mixed case for constants
class user_account:      # snake_case for class names
    pass
```

Remember: 

* Variables and functions use snake_case
* Constants use SCREAMING_SNAKE_CASE
* Classes use PascalCase (also called CamelCase or upper CamelCase)

#### How This Is Tested

Based on the PY109 Study Guide, you might be asked to:

1.  Identify whether names follow legal Python syntax
2.  Determine if names follow Python's style conventions (idiomatic)
3.  Explain why certain names are or aren't idiomatic
4.  Correct non-idiomatic names to make them idiomatic

***

### Type Coercions: explicit (e.g., using int(), str()) and implicit

There are two main types of type coercion in Python:

1.  ​**Explicit type coercion** ​: When you intentionally convert one data type to another using built-in functions
2.  **Implicit type coercion**​: When Python automatically converts one data type to another

#### Explicit Type Coercion

This happens when you deliberately use conversion functions:

```python

# String to integer
age_str = "25"
age_num = int(age_str)  # 25 (integer)

# Integer to string
count = 42
count_str = str(count)  # "42" (string)

# String to float
price_str = "19.99"
price_num = float(price_str)  # 19.99 (float)

# Integer/float to boolean
zero_bool = bool(0)  # False
nonzero_bool = bool(42)  # True
```

Common explicit conversion functions:

* `int()` - Converts to integer
* `float()` - Converts to floating-point
* `str()` - Converts to string
* `bool()` - Converts to boolean
* `list()` - Converts to list
* `tuple()` - Converts to tuple
* `set()` - Converts to set
* `dict()` - Converts to dictionary

#### Implicit Type Coercion

Python performs some automatic conversions:
```python

# Integer + Float = Float
result = 5 + 3.14  # 8.14 (float)

# Boolean in arithmetic operations
total = 10 + True  # 11 (True is treated as 1)
value = 5 * False   # 0 (False is treated as 0)
difference = 10 - False  # 10 (False is treated as 0)

#String Interpolation
name = "Kelley"
age = 30 #LOL
message = f"Name: {name}, Age: {age}"  # Values converted to strings
```

Boolean values are implicitly converted to integers (1 for True, 0 for False) in arithmetic operations. When using f-strings, Python implicitly converts values to strings.

**Important Non-Coercion Cases**

Some operations that look like implicit coercion aren't actually considered coercion:

1.  ​The `print()` function​: While `print()` does display non-string values, this conversion happens behind the scenes and isn't considered true coercion.
`print("Age:", 30)  # Outputs: Age: 30`

2.  ​String Concatenation​: Python does NOT implicitly convert integers to strings for concatenation - this requires explicit conversion.
```python
name = "Clare"
age = 35
print(name + age)  # TypeError: can only concatenate str (not "int") to str

# Correct approach:
print(name + str(age))  # Works with explicit conversion
```

3. Numeric Strings in Calculations: Also requires explicit conversion.
```python
num_str = "10"
result = num_str + 5  # TypeError

# Correct approach:
result = int(num_str) + 5  # Works with explicit conversion
```

4. Container Type Conversion: Requires explicit conversion.
```python

my_list = [1, 2, 3]
my_dict = my_list  # This assigns, doesn't convert

# Correct approach:
my_dict = dict(enumerate(my_list))  # Explicit conversion needed
```

#### Allowed Conversions

**String Conversions**
* String to int: `int("42")` ✓
* String to float: `float("3.14")` ✓
* Any type to string: `str(42)`, `str(3.14)`, `str(True)`, `str([1,2,3])` ✓

**Numeric Conversions**
* Float to int: `int(3.14)` ✓ (truncates decimal part)
* Int to float: `float(42)` ✓
* Boolean to int/float: `int(True) (1)`, `float(False) (0.0)` ✓

**Collection Conversions**
* String to list: `list("hello")` ✓ (creates `['h','e','l','l','o']`)
* List to tuple: `tuple([1,2,3])` ✓
* Tuple to list: `list((1,2,3))` ✓
* List or tuple to set: `set([1,2,2,3])` ✓

**Boolean Conversions**
* Empty strings/collections to boolean: `bool("")`, `bool([])`, `bool({})` all convert to `False` ✓
* Zero to boolean: `bool(0)` converts to `False` ✓
* Any non-zero number to boolean: `bool(42`), `bool(-1)` convert to `True` ✓
* None to boolean: `bool(None)` converts to `False` ✓

#### Special Cases

Special Cases are a doozy and there's a lot of them.

**Special Numeric Conversions**

1.  ​NaN (Not a Number)
   * Created with `float('nan')`
   * NaN doesn't equal anything (including itself): `float('nan') == float('nan'`) returns `False`
   * Test for NaN using `math.isnan()`
   * Any arithmetic with `NaN` results in `NaN`

2.  ​Infinity
   * Created with `float('inf')` or `-float('inf')`
   * Valid in comparisons: `float('inf') > 999999999` is `True`
   * Arithmetic operations work as expected with infinity

3.  ​Underscores in Numeric Literals
   * Python allows `1_000_000` for readability
   * Converting strings with underscores will fail: `int('1_000_000')` raises `ValueError`

**String Conversion Special Cases**

1.  ​Number Base Conversions
    * `int('101', 2)` converts binary '101' to decimal 5
    * `int('FF', 16)` converts hex 'FF' to decimal 255
    *  Base must be between 0 and 36

2.  ​Whitespace in Strings
    * `int(' 42 ')` works (strips whitespace)
    * `int('42 59')` raises `ValueError` (no spaces allowed between digits)

**Boolean Conversion Details**

1.  ​Complex Boolean Conversions
   * Empty collections are falsy: `bool([])`, `bool({})`, `bool(())`, `bool(set())` are all `False`
   * Non-empty collections are truthy, even with falsy elements: `bool([0, ''])` is `True`
   * Custom classes are truthy by default unless `__bool__` or `__len__` is defined

2.  ​Boolean to Number
   * `True == 1` and `False == 0` in arithmetic contexts
   * `3 + True` equals `4`
   * `True * 7` equals `7`

**Container Type Conversions**

1.  ​Dictionary Conversions
   * `dict([('a', 1), ('b', 2)])` creates a dictionary from pairs
   * `dict(a=1, b=2)` uses keyword arguments
   * `dict(zip(['a', 'b'], [1, 2]))` combines two iterables

2.  ​Set Conversions
   * `set('hello')` creates a set with unique letters: `{'h', 'e', 'l', 'o'}`
   * `set()` creates an empty set (not {}, which creates an empty dict)

#### More on Booleans are treated in arithmetic

In Python, boolean values undergo implicit type coercion in arithmetic operations:
* True is treated as the integer 1
* False is treated as the integer 0

Also:
* Boolean arithmetic is different from boolean equality
* True == 1 evaluates to True but True is 1 evaluates to False

```python
# Counting true values in a list
has_passed = [True, False, True, True, False]
total_passed = sum(has_passed)  # 3

# Conditional incrementing
count = 0
value = 25
count += (value > 20)  # Adds 1 if condition is True
```

#### Basic Pattern for Safe Type Conversion

```python
try:
    # Attempt the conversion
    converted_value = target_type(original_value)
    # Code that uses the converted value
except ExceptionType:
    # Handle the specific error
    # Could be ValueError, TypeError, etc.
```

#### Error Cases to Watch For

Python will raise exceptions for invalid conversions, namely in `ValueError` and `TypeError`:

`ValueError`:   When the value is the right type but inappropriate
```python
# ValueError - when the conversion cannot be performed
int("hello")  # ValueError: invalid literal for int() with base 10
float("abc")  #(ValueError: could not convert string to float)

try:
    num = int("abc")  # ValueError: invalid literal for int()
except ValueError:
       print("Please enter a valid number.")
```

`TypeError`: When passing the wrong type to a conversion function.

```python
int(["42"])  # TypeError: int() argument must be a string, a bytes-like object or a real number
float({"value": 42}) #TypeError: float() argument must be a string or number

try:
    num = int(["42"])  # TypeError: int() argument must be a string or number
except TypeError:
    print("Invalid input type for conversion.")
```

#### Try/Except Error Handling 

A robust example:

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

From Rock Paper Scissors:

```python

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False
```

#### Practical Applications of Type Coercion in Python

Here are real programming scenarios you'll encounter:

**User Input Processing** 
One of the most common applications is handling user input.

```python
age_str = input("Enter your age: ")  # Returns a string
age = int(age_str)  # Explicit coercion to integer for calculations

# With error handling
try:
    age = int(age_str)
    years_until_retirement = 65 - age
except ValueError:
    print("Please enter a valid number")
```

**Arithmetic Operations**
Type coercion is essential when performing calculations:

```python
# Implicit coercion: int to float
price = 10
tax_rate = 0.07
total = price * (1 + tax_rate)  # 10.7 (float)

# Explicit coercion for division
num_items = 10
num_people = 3
items_per_person = num_items // num_people  # Integer division
```

**Building Strings for Output**

When creating output for users:

```python
name = "Kelley"
score = 95
message = "Congratulations " + name + "! Your score is " + str(score)

# Better approach with f-strings
message = f"Congratulations {name}! Your score is {score}"
```

**Validation Logic**
Type coercion is key in validation functions:

```python
def is_valid_number(number_str):
    try:
        float(number_str)
        return True
    except ValueError:
        return False
```

**Truthiness in Conditional Statements**
Using type coercion to boolean in if statements:

```python
# Empty collections are falsy
user_input = ""
if not user_input:
    print("You must enter a value")

# Check if a list has elements
items = []
if items:  # Coerced to False when empty
    print("Processing items...")
else:
    print("No items to process")
```

**Data Processing**
When working with data in different formats:

```python
# Converting collection types
data_tuples = [(1, "one"), (2, "two")]
data_dict = dict(data_tuples)  # {1: "one", 2: "two"}

# Converting numerical data for display
temperatures = [22.5, 19.8, 25.1, 23.4]
temperatures_str = [f"{temp:.1f}°C" for temp in temperatures]
```

***

### Numbers

**Integers `(int)`**

Integers in Python are whole numbers without a decimal point. They can be positive or negative and have unlimited precision.

```python

x = 42           # Positive integer
y = -10          # Negative integer
z = 1_000_000    # Large integer with underscores for readability (Doesn't work with strings to int)
```

Key points:

* Python 3 has no size limit for integers (unlike some other languages)
* You can use underscores to make large integers more readable (may cause)
* Integer division (//) produces another integer, rounding down

**Floating-Point Numbers `(float)`**

Floats represent real numbers with decimal points:

```python
pi = 3.14159
e = 2.718282
negative_float = -0.5
```

Important considerations:

* Floats have limited precision and can lead to rounding errors
* When you mix integers and floats in arithmetic operations, the result is always a float:
`result = 3 + 2.0  # result is 5.0 (float)`

Standard arithmetic operations may produce unexpected results due to binary floating-point representation:
` 0.1 + 0.2  # 0.30000000000000004, not exactly 0.3`

**Complex Numbers `(complex)`**
Complex numbers have a real and imaginary part, where the imaginary part is written with a j suffix:

```python

z = 3 + 4j      # Complex number
real_part = z.real  # 3.0
imag_part = z.imag  # 4.0
```
You'll use complex numbers less frequently unless you're doing specialized mathematical or scientific computations.

Checking number types:

```python
type(42)         # <class 'int'>
type(3.14)       # <class 'float'>
type(1+2j)       # <class 'complex'>
```
***

## Strings!

### Basics on Strings

1.  **​Definition and Creation**​: Strings are sequences of Unicode characters, created using single quotes (`'text'`), double quotes (`"text"`), or triple quotes for multi-line strings ('`''text'''` or `"""text"""`).

2.  **​Immutability**​: Strings are immutable - once created, one cannot change individual characters. Any operation that appears to modify a string actually creates a new string.

3.  **​Sequence Type**​: Strings are sequence types, meaning they:
    * Have ordered elements (characters)
    * Can be accessed by index
    * Can be iterated over
    * Support operations like membership testing with in

4.  **​String Representation**​: Strings have literal representation in code and different display formats when printed (e.g., escape sequences like \n are interpreted when displayed).

5.  **​Empty Strings**​: An empty string `''` or `""` is a valid string with length `0`, which evaluates to `False` in boolean contexts.

6.  **​Memory Management**​: Due to immutability, Python can optimize memory by having multiple variables reference the same string object (especially for string literals).

7.  **​Type Conversion**​: Other data types can be converted to strings using the `str() `function.

8.  **​Concatenation and Repetition​:** Strings can be joined with `+` and repeated with `*` operators.

### f-strings and the `.format()` method

F-Strings, short for "Formatted String Literals", were introduced in Python 3.6 and provide a concise, readable way to embed expressions inside string literals.

```python
name = "Victor"
profession = "programmer"
message = f"Hello, {name}. You are a {profession}."
```
Key Features:
    * Start with f or F prefix before the quotation marks
    * Expressions in curly braces {} are evaluated at runtime
    * Can include any valid Python expression inside the braces
    * More readable and typically faster than other formatting methods

**Advanced F-string Techniques**:
```python

# Expression evaluation
price = 19.99
tax_rate = 0.07
print(f"Total price: ${price * (1 + tax_rate):.2f}")

# Using dictionary values
person = {"name": "Alice", "age": 30}
print(f"{person['name']} is {person['age']} years old")

# Formatting options
pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
```

The `.format()` method was introduced before f-strings and provides similar functionality but with a different syntax.

```python
name = "Victor"
profession = "programmer"
message = "Hello, {}. You are a {}.".format(name, profession)
```

Key Features:

* Uses placeholders `{}` in the string
* Values are passed as arguments to the .format() method
* Arguments fill placeholders in order (unless specified otherwise)

**Advanced .format() Techniques**:
```python

# Indexed placeholders
print("{1} was born in {0}".format("New York", "Alice"))  # Alice was born in New York

# Named placeholders
print("Hello, {name}. You are {age} years old.".format(name="Bob", age=25))

# Formatting options
print("Pi rounded to 3 decimal places: {pi:.3f}".format(pi=3.14159))
```

**When to Use Each**:

* F-strings are generally preferred in modern Python code due to their readability and performance
* The `.format()` method is still widely used, especially in older code
* Both methods support the same formatting options (precision, alignment, etc.)
* F-strings can directly use variables from the current scope, while `.format()` requires passing values explicitly.

### String Methods

**Case Modification Methods**

Case Modification Methods are: 
    * ​`.capitalize()`, `.upper()`, `.lower()`, `.swapcase()`, `.title()`
    * Work on empty strings without errors (return empty strings)
    * Handle special characters by leaving them unchanged
    * With non-alphabetic characters, they focus only on the letters 

`​.capitalize()​`: Converts the first character to uppercase and the rest to lowercase
`'hello world'.capitalize()  # 'Hello world'`

`​.swapcase()`​: Converts uppercase to lowercase and vice versa
`'Hello World'.swapcase()  # 'hELLO wORLD'`

`​.upper()`​: Converts all characters to uppercase
`'hello'.upper()  # 'HELLO'`

`​.lower()`​: Converts all characters to lowercase
`'HELLO'.lower()  # 'hello'`

`​.title()`​: Capitalizes the first letter of each word 
`'launch school tech & talk'.title()  # 'Launch School Tech & Talk'`

**Character Testing Methods**

Character Testing Methods are:
    * `​.isalpha()`, `.isdigit()`, `.isalnum()`, `.islower()`, `.isupper()`, `.isspace()`
    * Return `False` for empty strings
    * Particularly useful for input validation
    * Be aware of Unicode characters:
       * '²'.isdigit() returns `True` (superscript is a digit)
       * 'héllò'.isalpha() returns `True` (accented characters are alphabetic)

`​.isalpha()`​: Returns `True` if all characters are alphabetic (letters)
```python
'Hello'.isalpha()  # True
'Hello123'.isalpha()  # False
```

`​.isdigit()`​: Returns `True` if all characters are digits
```python
'12345'.isdigit()  # True
'123abc'.isdigit()  # False
```

`​.isalnum()`​: Returns `True` if all characters are alphanumeric (letters or digits)
```python
'Hello123'.isalnum()  # True
'Hello 123'.isalnum()  # False (space is not alphanumeric)
```

`​.islower()`​: Returns `True` if all characters are lowercase
```python
'hello'.islower()  # True
'Hello'.islower()  # False
```

`​.isupper(`)​: Returns `True` if all characters are uppercase
```python
'HELLO'.isupper()  # True
'Hello'.isupper()  # False
```

`​.isspace()`​: Returns `True` if all characters are whitespace
```python
'   '.isspace()  # True
'hello'.isspace()  # False
```

**String Modification Methods**

String modification methods are:
    * `.strip()`, `.rstrip()`, `.lstrip()`
    * Safe with empty strings (return empty strings)
    * Without arguments, remove whitespace only
    * With arguments, remove any character in the argument string

`​.strip()`​: Removes leading and trailing whitespace (or specified characters)
```python
'  hello  '.strip()  # 'hello'
'xxxhelloxxx'.strip('x')  # 'hello'
```

`​.rstrip()`​: Removes trailing whitespace (or specified characters)
`'  hello  '.rstrip()  # '  hello'`

`.lstrip()​`: Removes leading whitespace (or specified characters)
`'  hello  '.lstrip()  # 'hello  '`

`​.replace()`​: Replaces occurrences of a substring with another
`'Captain Ruby'.replace('Ruby', 'Python')  # 'Captain Python'`
    * Works on empty strings without errors
    * Replaces all occurrences unless limited by the count parameter
    * Returns the original string if the substring to replace isn't found

**Search and Split Methods**

`​.split()`​: Splits string into a list of substrings based on a delimiter
```python
  'hello world'.split()  # ['hello', 'world']
  'hello,world,python'.split(',')  # ['hello', 'world', 'python']
```
* With no arguments, splits on whitespace and returns empty list for empty string
* Consecutive delimiters are treated as one delimiter by default
* Can specify maxsplit to limit number of splits

`​.find()`​: Returns the lowest index of the substring (or -1 if not found)
```python
'hello world'.find('world')  # 6
'hello world'.find('python')  # -1
```
`​.rfind()`​: Like find but searches from the right (returns highest index)
`'hello world hello'.rfind('hello')  # 12`

Both `.find()` and `.rfind()`:
* Return -1 if substring not found (rather than raising an error)
* Empty string is always found at position 0 in non-empty strings
* Always return -1 when searching in empty strings*

**Important to Remember**

1.  Strings in Python are ​immutable​. Methods like .capitalize() and .replace() don't modify the original string - they return a new string.

2.  A common bug is forgetting to capture the return value:
``` python
word = "hello"
word.capitalize()  # This doesn't change 'word'
print(word)  # Still 'hello'
   
   # Correct way:
word = word.capitalize()
print(word)  # Now 'Hello'
```

3.  For searching substrings, you can also use the `in` operator:
``` python
"World" in "Hello, World!"  # True
Python" in "Hello, World!"  # False
```

***

## Booleans, Booleans vs. Truthiness and None

### Boolean vs. Truthiness

Boolean Values:

* Python has two boolean values: True and False (note the capitalization)
* These are specific data types in Python that represent logical truth values
* Boolean values are the direct result of comparison operations (like `==`, `!=`, `>`, `<`)

Truthiness:

**Truthiness** refers to how Python evaluates values in a boolean context (like in an if statement).

Falsy values in Python include:

*   `False`
*   `None`
*   Zero values: 0, 0.0, 0j
*   Empty strings: `''`
*   Empty collections: `[]` (empty list), `{}` (empty dict), `()` (empty tuple)
*   `set()` (empty set)
*   `range(0)` (empty range)

**All other values are considered truthy in Python**.

Verbalizing the following distinctions are very important!

*   When a _value evaluates as true_ in a boolean context, say that it **"evaluates to true"** or **"is truthy"**
*   When a _value evaluates as false_ in a boolean context, say that it **"evaluates to false"** or **"is falsy"**.
*   Do NOT say a value "is True" or "is equal to True" unless it's literally the boolean value True.
*   Do NOT say a value "is False" or "is equal to False" unless it's literally False.

```python

name = get_name_from_user()
if name:  # Checks if name is truthy (not empty)
    print(f"Hi {name}")
else:
    print("you must enter your name!")
```

### `None`

`None` is a special object in Python that represents the absence of a value or a null value. It's an important concept to understand for your upcoming assessment.

Key Characteristics of `None`:

1.  ​*It's a singleton object*​: There's only one `None` object in Python.
2.  ​*Data type*​: `None` has its own data type called `NoneType`.
3.  *​Falsy value*​: `None` is considered falsy in boolean contexts.

```python
   if None:
       print("This won't print")
   else:
       print("None is falsy")  # This will print
```

4. *Default return value*​: Functions without an explicit return statement, return `None` by default.

```python
   def no_return():
       pass
   
   result = no_return()
   print(result)  # None
```

## Boolean Logic Gates, Logical Operators, and Short Circuit Evaluation

Boolean logic gates are fundamental components in digital electronics and computer systems that process Boolean values (True and False), which are typically represented as 1 and 0 in computing.

**Basic Logic Gates**

1.  `​AND Gate
   *    Returns `True` only when **both** inputs are `True`.
   *    In Python, this is represented by the `and` operator
```python
   result = True and True  # True
   result = True and False  # False
```

2. ​OR Gate
   *    Returns `True` if at least one input is `True`
   *    In Python, this is the `or `operator
```python
   result = True or False  # True
   result = False or False  # False
```
3.  ​XOR Gate (Exclusive OR)
   •   Returns True when inputs are different
   •   Python doesn't have a built-in XOR operator, but you can create one:
```python
python
   def xor(value1, value2):
    if (value1 and not value2) or (value2 and not value1):
        return True
    return False
```

### Short-Circuit Evaluation

Python's logical operators use short-circuit evaluation. Short-circuiting occurs when Python stops evaluating an expression as soon as it knows what the final result will be. This is a performance optimization that also enables some useful programming patterns.

`and`: If the first operand is `False`, Python **doesn't evaluate the second operand** because the result **must be `False`**. Stated otherwise: `and` stops evaluating when it encounters the first falsy value. **It returns the first falsy value it finds (or the last value if all are truthy)**.

`or`: If the first operand is `True`, Python **doesn't evaluate the second operand** because the result must be `True`. `or` stops evaluating when it encounters the first truthy value. Stated another way: If the first operand is truthy, it returns that value without evaluating the second. If the first operand is falsy, it returns the second operand (regardless of whether it's truthy or falsy). Note that it returns the value of the operand, not that its `True` or `False`. 

Unlike `and` and `or`, the `xor` function can't use short-circuit evaluation since it needs to evaluate both operands to determine the result.

Commit this to memory: `and` and `or` don't return `True` or `False` - **they return the actual values that determine the result**:

```python
print(5 and 7)      # Outputs: 7 (last value since both are truthy)
print(0 and 'hello')  # Outputs: 0 (first falsy value)
print('' or 42)     # Outputs: 42 (first truthy value)
print(0 or '')      # Outputs: '' (last value since both are falsy)
```

Python's logical operators (`and`, `or`, `not`) are designed to return the actual operand values rather than simply `True` or `False` because:

1.  **​It's more versatile​**: This behavior allows for elegant patterns like default values and short-circuit evaluation.
2.  **​It preserves information**​: By returning the actual value instead of just a boolean, you retain the specific value that determined the result.
3.  **​It aligns with Python's truthiness concept**​: Any value in Python can be evaluated in a boolean context.

```python
# For the 'or' operator:
print("hello" or "world")  # Returns "hello" (the first truthy value)
print("" or "world")       # Returns "world" (since "" is falsy)

# For the 'and' operator:
print("hello" and "world") # Returns "world" (the last value since both are truthy)
print("" and "world")      # Returns "" (the first falsy value)
```

#### How `and` works 

|First Result|Second Result|Total Result|
|------------|-------------|------------|
|True        |True         |True        |
|True        |False        |False       |
|False       |N/A (not run)|False       |

#### How `or` works 

|First Result|Second Result|Total Result|
|------------|-------------|------------|
|True	     |N/A (not run)|True        |
|False	     |True	       |True        |
|False	     |False	       |False       |

credit for [table](https://www.pythonmorsels.com/short-circuit-evaluation/)

**Logical Operator Precedence**:

In Python, the logical operators have different precedence levels:

1.  not (highest)
2.  and
3.  or (lowest)

***

## Operators

We've already covered Logical Operators right above. Now for the rest.

### Arithmetic: +, -, *, /, //, %, **

Basic Arithmetic Operators
*   ​Addition (`+`)​: Adds two values
*   Subtraction (`-`)​: Subtracts the right operand from the left
*   Multiplication (`*`)​: Multiplies two values
*   ​Division (`/`)​: Divides the left operand by the right, always returns a float
*   Floor Division (`//`)​: Divides and returns the largest integer less than or equal to the result
*   Modulo (`%`)​: Returns the remainder of division
*   Exponentiation (`**`)​: Raises left operand to the power of right operand

Operator Precedence in Arithmetic Expressions:

Precedence order from high to low:
1.  Parentheses ()
2.  Exponentiation **
3.  Multiplication *, Division /, Floor Division //, Modulo %
4.  Addition +, Subtraction -

According to the Python documentation on operator precedence, expressions like `4 * 5 + 3**2 / 10` are evaluated in this order:
1.  `3**2 = 9` (exponentiation first)
2.  `4 * 5 = 20` (multiplication)
3.  `9 / 10 = 0.9` (division)
4.  `20 + 0.9 = 20.9` (addition last)
`
For clarity, you can use parentheses: `(4 * 5) + ((3**2) / 10)`

Float vs Integer Division
In Python 3, the division operator / always performs floating-point division.
` 7 / 2  # Result: 3.5`

To get integer division (truncating decimal part), use floor division //:
`7 // 2  # Result: 3`. Note that it rounds down!

Floating Point Arithmetic*
Be aware that floating-point calculations may have precision issues:
` 3.141529 - 2.718282  # Result: 0.42324699999999993`

How to handle floating point inaccuracies:

1.  Use the `math.isclose()` function: When comparing floating point numbers, avoid using the equality operator (`==`). Instead, use the `math.isclose() `function. The `math.isclose()` function checks if two values are close enough to be considered equal, taking into account the inherent imprecision of floating point arithmetic.

2.  Round to a specific precision:  When displaying results, round to a specific number of decimal places:
```python
result = 3.141529 - 2.718282  # equals 0.42324699999999993
print(round(result, 6))  # 0.423247
```

3. Use formatted string literals (f-strings): F-strings allow you to control how floating point numbers are displayed:
```python
result = 3.141529 - 2.718282
print(f"{result:.6f}")  # "0.423247"
```

4. Consider using the decimal module
For financial calculations or when precision is critical:
```python

from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 28

# Use Decimal instead of float
result = Decimal('0.3') + Decimal('0.6')
print(result)  # Exactly 0.9
```

5. Be aware of special floating point values: Python has special floating point values like nan (Not a Number). Note that nan values have unique behavior.
```python

nan_value = float("nan")
print(nan_value == float("nan"))  # Returns False!
```

To check for nan values, `use math.isnan()`:
``` python
import math
nan_value = float("nan")
print(math.isnan(nan_value))  # Returns True
```

6. Handle division by zero: When performing division, be aware of potential `ZeroDivisionError`.
``` python
try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Error: Division by zero"
```

### String Concatenation with `+`

In Python, the `+` operator performs string concatenation when used with strings:
```python
str1 = "Hello, "
str2 = "world!"
result = str1 + str2  # "Hello, world!"
```

Key points about string concatenation:
1. The `+ `operator **creates a new string** when combining two strings
2. Both operands must be strings; otherwise, you'll get a `TypeError`.
3. String concatenation is inefficient for multiple operations. For better performance with multiple strings, use `.join()` or f-strings.

### List Concatenation with `+`

The `+` operator also works with lists, merging two lists to create a new one:
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
```
Important characteristics of list concatenation:
1. Like string concatenation, the + operator **creates a new list**
2. The original lists remain unchanged.
3. Both operands must be lists (or other sequence types). You can't combine different types, resulting in a `TypeError`.
4. For a more memory-efficient alternative to repeatedly using `+` for list concatenation, you can use the `.extend()` method to modify a list in-place:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # Modifies list1 in-place
print(list1)  # [1, 2, 3, 4, 5, 6]
```

### Comparison Operators: `==`, `!=`, `<`, `>`, `<=`, `>=`

**Basic Comparison Operators**

* ​Equal (`==`)​: Tests if two values are equal
* Not Equal (`!=`)​: Tests if two values are not equal
* ​Less Than (`<`)​: Tests if left value is less than right value
* ​Greater Than (`>`)​: Tests if left value is greater than right value
* Less Than or Equal (`<=`)​: Tests if left value is less than or equal to right value
* Greater Than or Equal (`>=`)​: Tests if left value is greater than or equal to right value

**Comparing Different Types**

* Numbers of different types (int, float) can be compared directly
* Strings are compared lexicographically (dictionary order)
* Different types (like strings and numbers) follow specific comparison rules
```python
# python

# Comparing different numeric types
3 == 3.0      # True

# String comparison
"apple" < "banana"   # True (alphabetical order)
"apple" < "Apple"    # False (uppercase comes before lowercase in ASCII)

# Different types
"5" == 5      # False (string vs int)
```
**Truthiness vs. Boolean Values**
Remember the distinction between truthiness and actual boolean values:
```python

# These are not the same:
bool(0) == False    # True (0 converts to False)
0 == False          # False (0 and False are different values)

bool("") == False   # True (empty string converts to False)
"" == False         # False (empty string and False are different values)
```

**Chained Comparisons**

Python allows comparison chaining:
```python
# This:
x > y > z

# Is equivalent to:
x > y and y > z
```

**Identity vs. Equality**

Don't confuse `==` (equality) with `is` (identity):
* `==` checks if values are equal
* `is` checks if two variables reference the same object

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b  # True (same values)
a is b  # False (different objects)
a is c  # True (same object)
```

### Identity Operators: `is` and `is not`

As stated above, the `is` and `is not` operators in Python are identity operators that compare memory locations, rather than the values themselves. The `is` operator checks if two variables point to the exact same object in memory. Similarly, `is not` checks if two variables do NOT point to the same object.

Common Use Cases:

1. Checking for `None`: The most common and recommended use of it is for comparing with `None`.
```python
x = None
if x is None:  # Preferred over x == None
    print("x is None")
```

2. Distinguishing Between Identity and Equality: This example demonstrates the difference between `is` and `==`:
```python

empty_list_1 = []
empty_list_2 = []
print(empty_list_1 == empty_list_2)  # True - same values
print(empty_list_1 is empty_list_2)  # False - different objects
```

**Object Interning**

Python might reuse memory addresses for certain immutable objects like small integers or short strings. This is called "interning" and is an implementation detail of Python for optimization.

What Objects Get Interned?
1.  ​Small Integers​: Integers in the range -5 to 256 are interned by default.
2.  ​Short Strings​: String literals without spaces or special characters may be interned.

```python 
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True

# But with string creation at runtime:
s3 = "".join(["h", "e", "l", "l", "o"])
print(s1 is s3)  # Could be False
```
3.  ​Empty Immutable Collections​: Empty tuples and frozensets are typically interned.

Don't use `is` for value comparison:
```python
a = 1000
b = 1000
print(a is b)  # Could be False, despite what you might expect
print(a == b)  # Always True - correct way to compare values
```
** Why is it important?**
1.  **​Behavior of Identity Comparisons**​: When using the is operator, interned objects will return `True` even if they were created separately. However, with non-interned objects, the same comparison would return `False`. If a = b and both = 42, they will be the same object when evaluated with `is`. However, if a = b and both = 1000, they will not. This distinction is crucial when debugging or when you're relying on identit comparisons in your code.

2. **Memory Optimization**

To avoid later problems:
* Use == for value comparison
* Reserve `is` for identity checks, primarily with `None`
* Never rely on interning behavior for critical program logic

### Operator Precedence

As mentioned above, there's a hierarchy. Here's the final boss hierarchy, from highest precedence to lowest:

1.  Parentheses `()`
2.  Exponentiation `**`
3.  Unary operators (+x, -x, ~x)
4.  Multiplication/Division (`*`, `/`, `//`, `%`)
5.  Addition/Subtraction (`+`, `-`)
6.  Comparisons (`<`, `>`, `<=`, `>=`, `==,` `!=`)
7.  Boolean `not`
8.  Boolean `and`
9.  Boolean `or`

Python first evaluates the function calls left-to-right, then applies operator precedence rules. All values are determined before any operations are performed.

***

### Ranges

A range is a built-in sequence type in Python that represents an immutable sequence of numbers, typically used for looping a specific number of times in for loops.

**Creating Ranges**
The `range()` function can be called in three different ways:
1.  `​range(stop)`​: Creates a sequence from 0 to stop-1
    `range(5)  # Represents the sequence 0, 1, 2, 3, 4`
2. `range(start, stop)`​: Creates a sequence from start to stop-1
    `range(2, 7)  # Represents the sequence 2, 3, 4, 5, 6`
3. `range(start, stop, step)`​: Creates a sequence from start to stop-1, incrementing by  step. 
```python
range(1, 10, 2)  # Represents the sequence 1, 3, 5, 7, 9
range(10, 0, -1)  # Represents the sequence 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

Key properties of ranges:

* **Ranges are ​immutable**: you cannot modify them after creation
* **Ranges are ​memory efficient**​: they don't store all values in memory, just start, stop, and step.
* **Ranges are ​lazy evaluated**​: values are generated on demand

Common Operations with Ranges

1.  ​Iterating with a for loop​:
```python
for num in range(5):
       print(num)  # Prints 0, 1, 2, 3, 4
```

2. ​Converting to other sequence types​:
```python
list(range(3, 8))  # [3, 4, 5, 6, 7]
tuple(range(3, 8))  # (3, 4, 5, 6, 7)
```

3. Checking membership:
```python
5 in range(1, 10)  # True
11 in range(1, 10)  # False
```

4.  ​Getting length​:
`len(range(5, 20, 3))  # 5 (represents 5, 8, 11, 14, 17)`

5.  ​Indexing and slicing​:
```python
r = range(0, 10)
r[3]  # 3
r[-1]  # 9
r[2:5]  # range(2, 5)
```

Common use cases:

1. Counting loops:
```python
for i in range(5):
       print(f"Count: {i}")
```

2.  ​Working with list indices​:
```python
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")
```

3. Generating number sequences​:
```even_numbers = list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]```

Lazy evaluation is an evaluation strategy where expressions are not evaluated until their values are actually needed. In Python, this concept appears in several contexts, particularly with ranges. When you create a range in Python, it doesn't immediately compute all the values in that sequence. Instead, it stores only the start, stop, and step parameters and generates values on-demand when you iterate through it or access specific elements.

For example: `r = range(1, 1000000)`. This line doesn't create a list with 999,999 numbers. It just creates a range object that knows how to generate those numbers when needed. This is memory-efficient compared to creating the equivalent list: `huge_list = list(range(1, 1000000))`.

Beyond ranges, Python uses lazy evaluation in other contexts:
1.  ​Generators​: Similar to ranges, generators produce items only when needed.
2.  ​Short-circuit evaluation​: With logical operators and and or, Python only evaluates as much as necessary to determine the result.

Range Boundaries Explained

When you create a range with `range(start, stop)`, it includes:
* The `start` value (inclusive)
* All values up to but NOT including the `stop` value (exclusive)

This behavior is consistent across all range creation patterns:
```python
range(5)         # 0, 1, 2, 3, 4 (no 5)
range(2, 7)      # 2, 3, 4, 5, 6 (no 7)
range(1, 10, 2)  # 1, 3, 5, 7, 9 (no 10)
```

Why This Design Choice?
This "up to but not including" behavior may seem odd at first, but it offers several advantages:
1.  **​Zero-indexing compatibility**​: Since Python uses zero-indexing for sequences, ranges align well with list indices.
2.  **​Length calculation**​: The length of a range is simply `stop - start` (when step is 1).
3.  **​Consecutive ranges**​: Ranges can be concatenated without overlapping
```python
 # These two ranges connect perfectly:
range(0, 5)  # 0, 1, 2, 3, 4
range(5, 10) # 5, 6, 7, 8, 9
```

4. **Empty ranges**​: Easy to represent an empty range by setting start equal to stop.
` range(5, 5)  # Empty range`

Common Mistakes to Avoid

When working with ranges, watch out for these common errors:
1.  ​Assuming the stop value is included​:
```python
# If you need numbers 1-5 inclusive:
range(1, 6)  # Correct: 1, 2, 3, 4, 5
range(1, 5)  # Incorrect: missing 5
```

2.  ​Off-by-one errors in loops​:
```python
 # To iterate through a list:
   my_list = ['a', 'b', 'c']
   for i in range(len(my_list)):  # range(3) is 0, 1, 2
       print(my_list[i])
```

3. Using Negative Steps: With negative steps, the range still excludes the stop value:
`range(10, 0, -1)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (no 0)`


**Understanding the Difference Between range(5) and list(range(5))**

The key differencesare in their type, memory usage, and behavior:

**Type Difference**
•   `range(5)` creates a range object, which is a specific sequence type in Python
•   `list(range(5))` converts the range object into a list type, creating `[0, 1, 2, 3, 4]`
**Memory Usage**
•   `range(5)` is memory-efficient because it only stores the start (0), stop (5), and step (1) values
•   `list(range(5))` stores all elements [0, 1, 2, 3, 4] in memory at once
**Lazy Evaluation**
•   `range(5)` is lazily evaluated - it generates values on demand when you iterate through it
•   `list(range(5))` eagerly evaluates all values immediately when created
**Mutability**
•   `range(5)` is immutable - you cannot modify it after creation
•   `list(range(5))` is mutable - you can add, remove, or change elements

```python
r = range(5)
print(type(r))          # <class 'range'>
print(r)                # range(0, 5)
print(3 in r)           # True (efficiently checked)

l = list(range(5))
print(type(l))          # <class 'list'>
print(l)                # [0, 1, 2, 3, 4]
l.append(5)             # Can modify lists
print(l)                # [0, 1, 2, 3, 4, 5]
```

*** 

## Conditionals and Loops

### Conditionals
Conditionals allow your code to make decisions based on whether certain conditions are true or false. In Python, the main conditional statements are:
```python
# Basic if statement
if condition:
    # code executed if condition is True
    # The code inside the if block only executes when the condition evaluates to a truthy value.

# if-else statement
if condition:
    # code executed if condition is True
else:
    # code executed if condition is False

# if-elif-else statement (for multiple conditions)
if condition1:
    # code executed if condition1 is True
elif condition2:
    # code executed if condition1 is False and condition2 is True
else:
    # code executed if all conditions are False
```

For multiple `if/elif/else` conditions, they are evaluated in order, and only the first truthy condition's block will execute. If no condition is truthy, the `else` block executes.

Truthiness in Python: This means you can use expressions directly in conditions without explicitly comparing them to `True` or `False`:
```python
name = "John"
if name:  # name is truthy because it's a non-empty string
    print(f"Hi {name}")
```

As always 'truthy' does not mean 'equal to `True`.

As of 3.10 there's also match case statements.
```python

animal = 'horse'
match animal:
    case 'dog':
        print('woof')
    case 'cat':
        print('meow')
    case 'horse':
        print('neigh')  # This will be printed
    case _:  # Default case. #Always use a default case!
        print('unknown animal')
```
Use match-case when:
1.  You're comparing a single value against multiple possible patterns
2.  Your code has multiple if-elif-else statements checking the same variable
3.  You want to improve readability for value-based branching logic

Remember that once a matching case is found, the associated block executes and then the program exits the match statement entirely. Only one case block will execute per match statement. Therefore, always have a default case (`case _:`) ready to catch unmatched pairs. Also, place more specific patterns before more general ones. This is especially important when using pattern matching with more complex structures.

### Loops

Loops allow you to execute the same block of code multiple times. Python has two main types of loops: `for` and `while`.

`for` loops are used to iterate over a sequence (like a list, tuple, string) or other iterable objects:
```python
# Iterating over a list
colors = ['red', 'green', 'blue']
for color in colors:
    print(color)

# Using range() to iterate a specific number of times
for i in range(5):  # Generates numbers 0 through 4
    print(i)
```

**`for` Loops Best Practices**
1.  ​Use descriptive variable names in your loop​.
2.  ​Prefer for loops when the number of iterations is known.
3.  ​Use `enumerate()` when you need both index and value​.
4.  ​Use list comprehensions for simple transformations
```python
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]
```

`while` loops continue executing as long as a condition remains True. There are two main ways to use while loops:

1.  ​Standard while loop​ - Tests a condition before each iteration:
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Don't forget this or you'll have an infinite loop!
```
2. `​while True` with break​ - A more flexible approach when you need more complex exit conditions:
```python
while True:
    print('Continue? (y/n)')
    answer = input()
    if answer.lower() == 'n':
        break
```

**`while` loop best practices**:
1. ​Choose between regular while and while True appropriately​.
2. ​Always include a way to exit the loop​, so as to avoid infinite loops.
3. Use `break` to exit early when appropriate.


**Loop control statements**
* `break`: Exits the loop immediately, regardless of the loop condition. Useful in a `while` loop. 
* `continue`: Skips the rest of the current iteration and moves to the next one
* `pass`: Does nothing, acts as a placeholder. It does nothing but can be useful when you need a statement syntactically but don't want any action.

**Nested Loops and Loop Control**

Loop control statements affect only the innermost loop they are placed in:
```python

for i in range(3):
    for j in range(3):
        if j == 1:
            break  # This only breaks out of the inner loop
        print(f"i={i}, j={j}")
```
When to Use Each Control Statement
* Use `break` when you want to exit a loop completely (example: found what you're looking for)
* Use `continue` when you want to skip specific iterations but continue the loop
* Use `pass` when you need a placeholder or an empty block syntactically

Lots of times either loop will do, but it requires careful syntaxing:
```python
# Using a for loop
fish = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
for fish_name in fish:
    if fish_name == 'Nemo':
        print('Found Nemo!')
        break

# Using a while loop (alternative approach)
index = 0
while index < len(fish):
    if fish[index] == 'Nemo':
        print('Found Nemo!')
        break
    index += 1
```

### Ternary Operator

Python's conditional expression (often called the ternary operator) provides a concise way to write simple if-else statements in a single line. It follows this syntax: `true_value if condition else false_value`.

**Basic Usage**
The ternary operator evaluates the condition and returns either the first value (if the condition is truthy) or the second value (if the condition is falsy):

```python
# Traditional if-else
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary equivalent
status = "adult" if age >= 18 else "minor"

# Another, longer example

# Traditional if/else
if idx % 2 == 0:
    number = '1'
else:
    number = '0'

# Equivalent ternary
number = '1' if idx % 2 == 0 else '0'
```

```python
# Simple string formatting
greeting = "Hello, " + (name if name else "Guest")

# Default values
username = user_input if user_input else "Anonymous"

# Quick math
absolute_value = x if x >= 0 else -x

# Choosing between functions
action = save_data if is_valid else show_error
```

The ternary operator is best used when:
* The condition is simple
* Both outcomes are simple expressions (not complex blocks of code)
* You need to assign a value based on a condition

***

## Lists and Dictionaries

### Lists 

Lists in Python are **ordered**, **mutable** collections that can store elements of different data types. They are defined using square brackets `[]`. Because lists are mutable,  you can change their content without creating a new list.

```python
# Creating a list
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", True, 3.14]
nested_list = [1, [2, 3], 4]
```

**List Indexing and Slicing**
Python uses zero-based indexing, which means the first element is at index `0`.

```python
my_list = ['a', 'b', 'c', 'd', 'e']
print(my_list[0])      # 'a'
print(my_list[3])      # 'd'
print(my_list[-1])     # 'e' (negative indices count from the end)
print(my_list[-2])     # 'd'

# Slicing: my_list[start:end:step]
print(my_list[1:4])    # ['b', 'c', 'd'] (end index is exclusive)
print(my_list[:3])     # ['a', 'b', 'c'] (omitting start means from beginning)
print(my_list[2:])     # ['c', 'd', 'e'] (omitting end means to the end)
print(my_list[::2])    # ['a', 'c', 'e'] (step of 2)
print(my_list[::-1])   # ['e', 'd', 'c', 'b', 'a'] (negative step reverses)
```

**List Methods**

**Adding Elements**
* `append(item)`: Adds a single element to the end of the list. This method modifies the list in-place and returns `None`.
* `extend(iterable)`: Adds multiple elements from an iterable (like another list) to the end.
* `insert(index, item)`: Inserts an item at a specific index position. If the index is out of range, it simply appends to the end.

**Removing Elements**
* `pop([index])`: Removes and returns the item at the given index. If no index, it removes the last item.
* `remove(item)`: Removes the **first occurrence** of the specified value, raising a `ValueError` if the item isn't found.
* `clear()`: removes all items from the list.

**Finding Elements**
* `index(item[, start[, end]])`: Returns the index of the **first occurrence** of the given item, raising a `ValueError` if the item isn't found.
* `count(item)`: Returns the number of occurrences of the specified item.

**Ordering Elements**
*   `reverse()`: Reverses the elements in-place, mutating the object, returning `None`. Use when you want to modify the modify the list. 
*   `sort([key=None, reverse=False])`: Sorts the list in-place, optionally using a key function and/or in reverse order.

```python

numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5, 9]

# Sort in reverse order
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 1, 1]

# Sort by length of string
words = ["apple", "banana", "kiwi", "pear"]
words.sort(key=len)
print(words)  # ["kiwi", "pear", "apple", "banana"]
```

**Copying**
* copy():  Creates a shallow copy of the list. Note that nested objects are not deeply copied, just referenced.

**Other _built-in functions_ that work with lists **
* `len(list)`: Returns the number of items in the list.
* `sum()`: returns the sum of all items in a list (numbers only)
* `max()`:  returns the largest item in a list
* `min()`:  returns the smallest item in a list
* `sorted()`:  returns a new sorted list (unlike list.sort() which sorts in-place)
* `reversed(list)`: Creates an iterator that produces the elements in reverse order, 
returning a reverse iterator object, not a list. Preserves the original list.


**List Operators**
```python
# Concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2  # [1, 2, 3, 4] Note: + creates a new list!!!

# Repetition
repeated = list1 * 3      # [1, 2, 1, 2, 1, 2]

# Membership
print(2 in list1)         # True
print(5 in list1)         # False

# Length
print(len(combined))      # 4
```

**List Comprehensions**
List comprehensions provide a concise way to create lists.

```python
# Basic list comprehension
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# With conditional
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]  # [4, 16, 36, 64, 100]
```
***

### Dictionaries

Dictionaries in Python are **unordered collections of key-value pairs**. They're defined using curly braces `{}` with key-value pairs separated by colons. 

**Dictionary Characteristics**

1. **​Keys must be immutable**​:
    * Allowed keys: strings, numbers, tuples (containing only immutable elements), and frozensets
    * Not allowed: lists, sets, dictionaries (mutable objects)
2. **​Values can be any type**​: Strings, numbers, lists, other dictionaries, functions, etc.
3.  **Order**:
    * ​Unordered​ before Python 3.7. Now: dictionaries maintain insertion order
    * Don't rely on order for the assessment
4. You can add, modify, or delete key-value pairs after creation.

**Methods of creating a dictionary**
1. Using Curly Braces (Dictionary Literal). Standard!
```python
# Dictionary with initial key-value pairs
empty_dict = {}  # Empty dictionary

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
}
```
2.  Using the `dict()` Constructor
```python
# Empty dictionary
empty_dict = dict()

# From keyword arguments
person = dict(name='Alice', age=25, city='Portland')

# From a sequence of key-value pairs (tuples)
items = [('type', 'sedan'), ('color', 'blue'), ('mileage', 80_000)]
car = dict(items)
```

3.  Dictionary Comprehensions: For creating dictionaries based on existing data.
```python
# Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
letter_dict = {k: v for k, v in zip(keys, values)}
# Result: {'a': 1, 'b': 2, 'c': 3}
```

**Accessing values in dictionaries**

1. **Using Square Bracket Notation**: The most common way to access dictionary values is using square brackets with the key
    * If the key doesn't exist, Python will raise a `KeyError`.
    * Case sensitivity matters - keys must match exactly.
```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'year': 2003,
}

print(car['color'])  # Outputs: blue
```

2. **Using the `get()` method**: the preferred approach when you're not sure if a key exists in the dictionary.
```python
# Returns the value if key exists
print(car.get('color'))  # blue

# Returns None if key doesn't exist (no error)
print(car.get('model'))  # None

# Returns a default value if the key doesn't exist
print(car.get('model', 'Unknown'))
```

3. **Checking if a Key Exists**: Before accessing a value, you can check if a key exists using the in operator.
```python 
student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student)      # False
print('grade' in student)     # True

# Using it in an if statement
if 'grade' in student:
    print(student['grade'])
else:
    print("Unknown")
```

4. Accessing Values in Nested Dictionaries: for nested dictionaries, chain the square brackets. Additionally, the get() with nested dictionaries approach is particularly useful as it won't raise an error if any level of the nested structure is missing.
```python
vehicles = {
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003,
    },
    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': 1998,
    },
}

# Access a value in a nested dictionary
print(vehicles['car']['color'])  # blue

# Using get() with nested dictionaries
print(vehicles.get('car', {}).get('color', 'Unknown'))  # blue
```

**Modifying Dictionaries**

1. **Adding or Updating Key-Value Pairs**: The simplest way to modify a dictionary is by assigning a value to a key. If the key doesn't exist, Python adds a new key-value pair; if it does exist, Python updates the value.
```python

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
}

# Adding a new key-value pair
car['year'] = 2003

# Updating an existing value
car['color'] = 'red'

print(car)  # {'type': 'sedan', 'color': 'red', 'mileage': 80_000, 'year': 2003}
```

2. **Using the `update()` method:** lets you add or update multiple key-value pairs at once
```python

car = {
    'type': 'sedan',
    'color': 'blue',
}

# Adding/updating multiple key-value pairs
car.update({'year': 2003, 'mileage': 80_000, 'color': 'green'})

print(car)  # {'type': 'sedan', 'color': 'green', 'year': 2003, 'mileage': 80_000}
```

**Removing from dictionaries**:
1.  The `del` Statement: directly removes a key-value pair from a dictionary, mutating the dictionary object. It raises a `KeyError` if a key doesn't exist. No value is returned.
```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
    'year': 2003,
}

del car['mileage']
print(car)  # {'type': 'sedan', 'color': 'blue', 'year': 2003}
```

2. **The `pop()` method**:  removes a key-value pair and returns the value associated with the removed key. It will accept a default value as a second argument to return if the key doesn't exist, however if a key nor a default does not exist, it will raise a `KeyError`. This is a useful method when you know what you are removing.
```python

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
    'year': 2003,
}

mileage = car.pop('mileage')  # mileage = 80_000
print(car)  # {'type': 'sedan', 'color': 'blue', 'year': 2003}

#Example with a default value.
model = car.pop('model', 'not specified')  # model = 'not specified'
```

3. **The `popitem()` method**: removes and returns a key-value pair from the dictionary. This creates a way to process items one by one while simultaneously removing them from the dictionary. It's "destructive" because it permanently modifies the dictionary by removing items as you iterate.

This approach is useful when:
* You need to process each item exactly once
* You want to ensure items are removed as you go (to free memory or prevent duplicate processing)
* You don't need to preserve the original dictionary

```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'year': 2003,
}

last_pair = car.popitem()  # last_pair = ('year', 2003)
print(car)  # {'type': 'sedan', 'color': 'blue'}
```

4. **The `clear()` method**: removes all items from a dictionary, resulting in an empty dictionary. Mutates the original dictionary object and does not return any values.
```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'year': 2003,
}

car.clear()
print(car)  # {}
```
5. Dictionary Comprehension for Selective Removal: To remove multiple items based on a condition, you can use dictionary comprehension.  
```python
car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
    'year': 2003,
    'previous_owners': 2,
}

# Remove all keys that have numeric values
car = {k: v for k, v in car.items() if not isinstance(v, int)}
print(car)  # {'type': 'sedan', 'color': 'blue'}
```
Be sure not to remove while iterating through it, instead create a copy or collect keys to remove first.
```python
# This will cause unexpected behavior and probably unwanted 
words = ['scooby', 'do', 'on', 'channel', 'two']
for word in words:
    print(word)  # prints: scooby, do, on, channel, two (in that order)
    words.remove(word)

print(words)  # Prints: ['do', 'channel']

# Safer approach
car = {'type': 'sedan', 'color': 'blue', 'mileage': 80_000}
keys_to_remove = [k for k in car if k != 'type']
for key in keys_to_remove:
    del car[key]
```

**Dictionary Methods**

* `dict.keys()`: returns a `dict_keys` object containing all the keys in the dictionary, not a list. It is dynamic however, and will update if the dictionary changes. Can be converted to a list using list(car.keys()). Useful for iterating through all keys in a dictionary
```python
python

car = {
    'type': 'sedan',
    'color': 'blue',
    'year': 2003,
}

keys = car.keys()  # dict_keys(['type', 'color', 'year'])
```

**`dict.values()`**: returns a dict_values object containing all the values in the dictionary, and is likewise dynamic like `dict.keys()`. 
`values = car.values()  # dict_values(['sedan', 'blue', 2003])`

Can include duplicate values (unlike keys, which must be unique) and useful when you need to work with all values without their associated keys. 
```python
grades = {'Math': 95, 'Science': 88, 'History': 92}

# Calculate average without needing the subject names
average = sum(grades.values()) / len(grades)
print(f"Average grade: {average}")  # Average grade: 91.67

# Check if a specific value exists
if 88 in grades.values():
    print("Someone got an 88!")
```

**`dict.items()`**: returns a dict_items object containing all key-value pairs as tuples, and is especially useful for iteration, especially over both keys and values.
```python

items = car.items()  # dict_items([('type', 'sedan'), ('color', 'blue'), ('year', 2003)])

# Printing each key-value pair
for key, value in car.items():
    print(f"The car's {key} is {value}.")
umbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(f"A {key} number is {value}.")
```
**`dict.get()`**: retrieves a value associated with a key. It is safer than bracket notation because it doesn't raise `KeyError` for missing keys. It provides a clean way to handle missing keys with default values. Can be chained for nested dictionaries: `data.get('user', {}).get('address', {})`

These usually work together!
```python

# Check if a specific value exists in the dictionary
if 'blue' in car.values():
    print("The car is blue")
    
# Check if a specific key exists
if 'model' not in car.keys():  # or simply: if 'model' not in car:
    car['model'] = 'standard'
```

Here's a quick syntax review:

```python

# Get all keys
keys = car.keys()  # dict_keys(['type', 'color', 'year'])

# Get all values
values = car.values()  # dict_values(['sedan', 'blue', 2003])

# Get all key-value pairs
items = car.items()  # dict_items([('type', 'sedan'), ('color', 'blue'), ('year', 2003)])
```

*** 

### Other Python Collections

1. **Tuples**: Immutable, ordered sequence. Uses `()`.
​
Use Cases​:
* When you need data that shouldn't change (like coordinates, RGB values)
* Dictionary keys (since they must be immutable)
* Returning multiple values from a function

```python
# Creating a tuple
coordinates = (10, 20)
rgb_color = (255, 0, 127)
```

2. **Sets**: Unordered collection, no duplicates, mutable but contains only immutable objects. Uses `{}`

​Use Cases​:
* When you need to ensure uniqueness of elements
* Set operations (union, intersection, difference)
* Membership testing for large collections (faster than list)
```python
# Creating a set
unique_numbers = {1, 2, 3, 4, 5}
tags = {"python", "programming", "tutorial"}
```

Sets in Python are mutable, meaning you can modify them after creation by:
* Adding elements using add() or update()
* Removing elements using remove(), discard(), or pop()
* Clearing all elements with clear()

While sets themselves are mutable, they can only contain hashable objects, which in Python are typically immutable objects. This is because sets use a hash table implementation internally for fast lookups.

These objects can be included in sets:
* Integers: {1, 2, 3}
* Floats: {1.1, 2.2, 3.3}
* Strings: {"apple", "banana"}
* Tuples (if they contain only immutable objects): {(1, 2), (3, 4)}

These objects CANNOT be included in sets:
* Lists: {[1, 2], [3, 4]} 
* Dictionaries: {{1: 'a'}, {2: 'b'}} 
* Sets: {{1, 2}, {3, 4}} 

3. Ranges (See Above)

How to Differentiate Between Collections:

| Collection | Ordered? | Mutable? | Allows Duplicates? | Indexable?     | Syntax             |
| ---------- | -------- | -------- | ------------------ | -------------- | ------------------ |
| List       | Yes      | Yes      | Yes                | Yes            | [1, 2, 3]        |
| Dictionary | Yes*     | Yes      | No (keys)          | No (uses keys) | {'a': 1, 'b': 2} |
| Tuple      | Yes      | No       | Yes                | Yes            | (1, 2, 3)        |
| Set        | No       | Yes      | No                 | No             | {1, 2, 3}        |
| Range      | Yes      | No       | No                 | Yes            | range(1, 4)      |

**When to Use Each Collection**
* ​Lists​: When you need a mutable, ordered collection that can contain duplicate items
* ​Dictionaries​: When you need key-value pairs for quick lookups
* Tuples​: When you want an immutable ordered collection
* Sets​: When you need to ensure uniqueness or perform set operations
* ​Ranges​: When you need a sequence of numbers without storing them all

***

slicing (strings, lists, tuples)

***

variables
naming conventions
initialization, assignment, and reassignment
scope
global keyword
variables as pointers
variable shadowing

***
print() and input()

***
exceptions (when they will occur and how to handle them)

***

expressions and statements

***

Functions:
definitions and calls
return values
parameters vs. arguments
nested functions
output vs. return values, side effects


Parameters are the names assigned to a function's arguments; arguments are the values that get passed to the function.
Variables are not passed to or returned by functions: references to objects are passed.

***


mutability and immutability

***
pass by object reference
