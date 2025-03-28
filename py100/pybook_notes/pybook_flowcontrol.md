# Flow Control

The simplest conditionals use a combination of if statements with comparison and logical operators(`<`, `>`, `<=`, `>=`, `==`, `!=`, `and`, `or`, and `not`) to direct traffic. They use the keywords `if`, `elif`, and `else`.

Avoid nested if statements when possible. They quickly become difficult to read with multiple levels of nesting or longish code blocks. However, don't get twisted up trying to avoid them entirely. Keep the nesting to a modest 2 or 3 levels deep and use functions to isolate some of the more complex code.

You can have as many `elif` blocks as you need, but they all need to be after the if block and, if the code has one, before the `else` block. The elif conditionals are evaluated in the order they appear in the code.

Every once in a while, you may want to create a block in an `if` statement that does nothing. We usually do this for readability purposes. However, blocks can't be empty. Instead, you have to use a `pass` statement. Adding a comment to a `pass` is good practice so future programmers know why it is there.

### Comparisons:

The expressions to the left and right of an operator are its operands.

#### `==` 

The equality operator returns `True` when the operands have equal values, `False` otherwise. In most cases, operands must have the same type and value to be equal. Thus, `5` is not equal to `'5'`. Comparisons with strings are case-sensitive. Thus, `'abc'` is not equal to `'aBc'`.

Other tips: While `casefold()` is only needed when working with non-US characters, it's best practice in Python to use `casefold` instead of `lower` or `upper`, especially when comparing strings.

#### `!=` 

The inequality operator, `!=`, is `==`'s inverse: It returns `False` when `==` would return `True`, and `True` when `==` would return `False`. It returns `False` when the operands have the same type and value, `True` otherwise.

#### `<` and `<=`

The less than operator (`<`) returns `True` when the value of the left operand has a value that is less than the value on the right, `False` otherwise. The less than or equal to operator (`<=`) is similar, but it also returns `True` when the values are equal; `<` returns `False` when the operands are equal.

#### `>` and `>=`

The greater than operator (`>`) returns `True` when the value of the left operand has a value that is greater than the value on the right, `False` otherwise. The greater than or equal to operator (`>=`) is similar, but it also returns `True` when the 
values are equal; `>` returns `False` when the operands are equal.

### Logical Operators:

#### not

The `not` operator returns `True` when its operand is `False` and returns `False` when the operand is `True`. That is, it negates its operand. Unlike most operators, `not` takes a single operand; it appears to the operator's right. Operators that take only one operand are called unary operators. Operators that take two operands are binary operators, though you'll rarely hear that term.

#### `and` and `or`

The `and` operator returns `True` when both operands are `True`. It returns `False` when either operand is `False`. The `or` operator returns `True` when either operand is `True` and `False` when both operands are `False`.

The following truth table shows how `True` and `False` interact with the and and or operators. You should memorize this table:

**A	    B	    A and B	A or B**
True	True	True	True
True	False	False	True
False	True	False	True
False	False	False	False


### Truthiness

It can evaluate every object's truthiness. Note that these terms are not synonymous with `True`, `False`, and `Boolean`. In addition, truthy and falsy are not actual objects or values. Instead, they are terms that describe how specific objects behave in a Boolean context.

So, which values are truthy? Which are falsy? **The built-in falsy values are as follows**:

* `False`, `None`
* all numeric `0` values (integers, floats, complex)
* empty strings: `''`
* empty collections: `[]`, `()`, `{}`, `set()`, `frozenset()`, and `range(0)`
* Custom data types can also define additional falsy value(s).

Okay, now that we know what's falsy, what's truthy? **Everything else**.

Use "truthy" and "falsy" when speaking of truthiness, `True` and `False` when talking of booleans,and true and false when discussing truths and falsehoods.

#### Truthiness and Short-Circuit Evaluation:

`is_ok = bool(foo or bar)`

### Logical Operator Precedence:

The following list shows the precedence of the comparison operators from highest (top) to 
lowest (bottom).

`==`, `!=`, `<=`, `<`,`>`, `>=` - Comparison
`not` - Logical NOT
`and` - Logical AND
`or` - Logical OR

Avoid mixing and and or in a single expression unless you use parentheses to control the 
order of evaluation.

### Match/case Statement

```python

value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default case
        print('value is neither 5 nor 6')
# value is 5

value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _: # default case
        print('value is not 1, 2, 3, 4, 5, or 6')
# value is 5 or 6
```

### Ternary Expressions:

Ternary expressions have the following structure: `value1` if condition else `value2`.

Like: 

`print("Triangle" if shape.sides() == 3 else "Square")`

Ternaries should almost always be extremely simple and fit entirely on one 79-column line of code.