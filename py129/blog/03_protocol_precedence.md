# Python Protocols, Dispatch, and Precedence

Exhaustive Reference for Idioms, Hidden Contracts, and Assessment Traps

Moral framing:

> Python is not a bag of syntax.  
> Python is a choreography of protocols.  
> Syntax is how you ask; protocols decide who answers.  


## GLOBAL META-RULES (Read First)

### Meta-Rule 1: Dispatch Always Follows a Fixed Order

Python does not guess. It follows an ordered protocol lookup.  

If you know the order, nothing is mysterious.

### Meta-Rule 2: Objects Collaborate by Contract, Not by Type

Operators do not care what an object is.  
They care whether it responds to the protocol.  

Dunder methods are capabilities, not identities.  

### Meta-Rule 3: “NotImplemented” Is a Hand-Off, Not an Error

Returning `NotImplemented` means: “I decline responsibility — ask the other object.”

### Meta-Rule 4: In-Place ≠ Numeric

`+=` does not mean “do math.”  It means “mutate if possible, otherwise rebind.”


## 1. ATTRIBUTE ACCESS PROTOCOL

`obj.attr`

Dispatch order:
1.	`type(obj).__getattribute__(obj, "attr")`
2.	If `AttributeError`, then: `type(obj).__getattr__(obj, "attr")` (only if defined)

Descriptors may intercept during step 1.

### `obj.attr = value`

1.	`type(obj).__setattr__(obj, "attr", value)`
2.	Descriptor `__set__ `may intercept

### `del obj.attr`
1.	`type(obj).__delattr__(obj, "attr")`
2.	Descriptor `__delete__` may intercept


## 2. CALL PROTOCOL

`obj(...)`

1.	`type(obj).__call__(obj, ...)`

Invariant: Callable ≠ function.  
Any object may be callable.


## 3. TRUTHINESS PROTOCOL

`if obj`:

Dispatch order:

1.	`type(obj).__bool__(obj)` → must return `bool`
2.	If missing: `type(obj).__len__(obj)` → non-zero is truthy
3.	If both missing: `True`


## 4. MEMBERSHIP PROTOCOL (in)

`x in y`

Dispatch order:

1.	`type(y).__contains__(y, x)`
2.	If missing: iteration protocol (`__iter__` → `__next__`)
3.	If missing: sequence fallback via `__getitem__` starting at 0
4.	else: `TypeError`

`x not in y` negates result

Exam trap: `__getitem__` enables membership without `__contains__`.


## 5. ITERATION PROTOCOL

`iter(obj)`

1.	`type(obj).__iter__(obj)`
2.	If missing: sequence fallback via `__getitem__`
3.	else: `TypeError`


`next(it)`  
1.	`type(it).__next__(it)`
2.	Must raise `StopIteration`


`for x in obj` uses `iter(obj)` → repeated `next()`. 

`reversed(obj)`  
1.	`type(obj).__reversed__(obj)`
2.	else: needs both `__len__` and `__getitem__`


## 6. INDEXING & SLICING PROTOCOL

`obj[key]` 
1.	type(obj).__getitem__(obj, key)

Key shape:
* int → indexing
* slice(start, stop, step) → slicing


`obj[key] = value` 
1.	`type(obj).__setitem__(obj, key, value)`


`del obj[key]`
1.	`type(obj).__delitem__(obj, key)`


## 7. LENGTH PROTOCOL

`len(obj)`

1.	`type(obj).__len__(obj)` → must return non-negative int


## 8. REPRESENTATION & FORMATTING

`repr(obj)` 
1.	type(obj).__repr__(obj) → str


`str(obj)` 
1.	`type(obj).__str__(obj)` → str
2.	else fallback: `__repr__`


`f-strings / format(obj, spec)`
1.	`type(obj).__format__(obj, spec)`
2.	Typically delegates to `__str__`

Hidden coordinator: `str.join`, `print`, and f-strings are callers, not formatters.


## 9. COMPARISON PROTOCOLS

### Equality

`a == b`  
1.	`type(a).__eq__(a, b)`
2.	If `NotImplemented`: `type(b).__eq__(b, a)`
3.	else: `False`

`a != b` uses `__ne__` if defined, else negates `__eq__`


### Ordering

| Expression | LHS Method   | Fall Back (RHS Method) |
|------------|--------------|------------------------|
| `<`        | `__lt__`     | `RHS.__gt__`           |
| `<=`       | `__le__`     | `RHS.__ge__`           |
| `>`        | `__gt__`     | `RHS.__lt__`           |
| `>=`       | `__ge__`     | `RHS.__le__`           |

If unresolved `TypeError`

## 10. BINARY ARITHMETIC PROTOCOL

General rule: `a OP b`
1.	`type(a).__op__(a, b)`
2.	If `NotImplemented`: `type(b).__rop__(b, a)`
3.	else: `TypeError`

| Syntax | Primary        | Reflected        |
|--------|---------------|------------------|
| +      | `__add__`     | `__radd__`       |
| -      | `__sub__`     | `__rsub__`       |
| *      | `__mul__`     | `__rmul__`       |
| /      | `__truediv__` | `__rtruediv__`   |
| //     | `__floordiv__`| `__rfloordiv__`  |
| %      | `__mod__`     | `__rmod__`       |
| **     | `__pow__`     | `__rpow__`       |
| @      | `__matmul__`  | `__rmatmul__`    |


## 11. IN-PLACE OPERATORS 

`a OP= b`

Dispatch:

1.	`type(a).__iop__(a, b)`
2.	If missing or `NotImplemented`: fallback to` a = a OP b`
3.	Name rebound unless mutated in place

Key Operators

| Syntax | Method        |
|--------|--------------|
| +=     | `__iadd__`   |
| -=     | `__isub__`   |
| *=     | `__imul__`   |
| /=     | `__itruediv__` |
| %=     | `__imod__`   |


Critical invariant:  `__iadd__` means in-place semantics, not numeric addition.

## 12. UNARY OPERATORS

| Syntax   | Method      |
|----------|-------------|
| +a       | `__pos__`   |
| -a       | `__neg__`   |
| ~a       | `__invert__`|
| abs(a)   | `__abs__`   |

## 13. NUMERIC CONVERSION & INDEXING

| Operation          | Method       |
|--------------------|-------------|
| int(a)             | `__int__`   |
| float(a)           | `__float__` |
| complex(a)         | `__complex__` |
| slicing / range()  | `__index__` |

Exam trap: `__index__` ≠ `__int__` 

## 14. CONTEXT MANAGER PROTOCOL

`with obj as x`:  
1.	`type(obj).__enter__(obj)` → bound to x
2.	`type(obj).__exit__(obj, exc_type, exc, tb)`



## 15. HASHING & SET / DICT BEHAVIOR

| Operation     | Method               |
|---------------|---------------------|
| hash(obj)     | `__hash__`          |
| dict lookup   | `__hash__` → `__eq__` |

Invariant: Equal objects must hash equally.

## 16. IDENTITY (NOT OVERRIDABLE)

`a is b`
* Pointer identity
* No dunder
* No dispatch


## SUMMARY: THE CORE CHOREOGRAPHY

Python’s tune is this:
1. Ask left
2. Ask right
3. Fall back by protocol
4. Die loudly if no one answers


### EXAM SURVIVAL HEURISTICS

| When you see… | Think…                                 |
|---------------|----------------------------------------|
| in            | `__contains__` → iteration → `__getitem__`   |
| +=            | `__iadd__` → fallback → rebind         |
| []            | `__getitem__` with int or slice        |
| , ".join(...)"| str coordinating collaborators         |
| f-strings     | `__format__` → `__str__`               |
| comparison    | NotImplemented → swapped method        |

## ONE-LINE MORAL INVARIANT

**Python is a protocol engine, syntax is surface, dispatch is truth.**
