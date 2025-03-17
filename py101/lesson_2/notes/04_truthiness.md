# Truthiness

A boolean is a data type whose only purpose is to convey whether it is true or false.
In real code, you wouldn't usually use the `True` or `False` values directly in a conditional expression like `value == True`. Instead, you would merely evaluate an expression that should evaluate as either `True` or `False`. A function doesn't usually return `True` or `False` explicitly. Instead, it returns the result of a conditional expression.

#### The `and` Operator

The `and` operator evaluates as `True` only when both sub-expressions evaluate as `True`.

You can chain as many sub-expressions as you'd like with `and`; the sub-expressions get 
evaluated left to right. If any sub-expression is `False`, the entire and chain evaluates as `False`. The whole expression evaluates as True only when all of the sub-expressions evaluate as `True`.

#### The `or` Operator

`or` operator evaluates as `True` when either of the two sub-expressions evaluates as `True`; it evaluates as `False` when both sub-expressions evaluate as `False`.

#### The `not` Operator

The `not` operator is a bit different than the previous two operators. It simply inverts the truth value of the condition it's applied to. If a condition is `True`, not will make it `False` and vice versa.

#### Short-Circuit Operators

Both `and` and `or` exhibit a behavior called short-circuiting. That means that Python stops evaluating sub-expressions once it can determine the final value. In the case of and, Python short-circuits when it realizes that the entire expression can't be true; that is, when it encounters a false sub-expression. With `or`, it short-circuits when it realizes that the expression can't be false; that is, at least one sub-expression is true.

`and` short-circuits when it encounters the first sub-expression (from left-to-right) that 
evaluates as `False`.

`or` operator short-circuits when it encounters the first `True` sub-expression.

Truthiness differs from boolean values in that Python evaluates almost all values as true. 

##### All of the following memorize as false:

* False
* None
* 0
* 0.0
* 0j
* "" (an empty string)
* [] (an empty list)
* {} (an empty dictionary)
* () (an empty tuple)
* set() (an empty set)
* frozenset() (an empty frozenset)
* range(0) (an empty range)

Notice that we've repeatedly used the phrases evaluated as true and evaluated as false. 
You can also use the terms truthy and falsy to describe the nature of the values. 