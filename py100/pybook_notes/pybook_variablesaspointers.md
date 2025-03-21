# Variables as Pointers

You can say that a variable points to or references an object in memory, and you can also 
say that the pointers stored in variables are references. 

In Python, all variables are pointers to objects. If you assign the same object to multiple variables, every one of those variables references (points to) the same object. They act like aliases for the object.

When you reassign a variable, Python changes what object the variable references. 
Reassignment doesn't alter the old or new object; it simply changes which object the 
variable references.

When a reassignment involves the creation of a new object, Python first creates the new 
object. It then changes the variable's stack item to point to the new object. This does not alter the object.

Things get a little messier when mutating objects through a variable. If a variable points
to a mutable object and you do something to mutate that object, Python doesn't change the 
variable; it changes the object. Every variable that references that object will immediately see the object's new state.

```
numbers = [1, 2, 3, 4]
numbers[2] = 3333
```

This is not a reassignment of the numbers variable. It's a mutation of the list object 
referenced by numbers. Technically, it's also a reassignment of the list object element 
at index 2, but it is not a mutation of that element. 

When using variables, it's essential to remember that some operations mutate objects while 
others do not. For instance, list.sort mutates a list, but sorted(list) does not.

```
x = [1, 2, 3, 4, 5]
x = [1, 2, 3] #reassignment to a new value
x[2] = 4 #reassignment and mutates the list
```

_From Claude on augmented assignments_:

An augmented assignment is a type of operator that combines a binary operation (like 
addition, subtraction, multiplication, etc.) with an assignment in a single statement. 
These operators perform an operation and assign the result back to the original variable 
in one step.

When the variable on the left side references an immutable value, augmented assignment acts like reassignment. However, if the variable on the left references a mutable value, the augmented assignment is usually mutated.

### Variables and Objects

At the most basic level, variables are named locations in a computer's memory. 

The space allocated for a single variable is small. On modern computers in 2023, that's 
typically 64 bits (or 8 bytes). Objects often far exceed that size. Thus, objects usually 
aren't stored on the stack. Instead, Python allocates the memory it needs for an object 
from the heap. Heap blocks can be pretty much any size, provided sufficient memory is 
available.

Once Python allocates heap space, it creates and stores the object at that location. The 
address of that object is then copied to the variable's stack location.

Thus, when you access a variable, Python first determines where the variable is on the 
stack. It then takes the object's heap address from the stack item and uses it to find 
the object. The variable is a pointer to a stack location, and the stack location is a 
pointer to the object.

Check it for yourself:

```python
print(id(numbers) == id(numbers2))      # True
print(numbers is numbers2)              # True
```

Two variables can and often do point to the singular object in the heap. But two lists
with the same list contents will still be two different objects. While the lists
may pass the == test, they wouldn't pass the 'is' test.

#### Shallow vs Deep Copies

Most copies created by Python programs are shallow copies. Deep copies just aren't 
needed all that often. The copy.copy and copy.deepcopy functions from the built-in 
copy module are Python's primary ways to create shallow and deep copies, respectively.
Therefore, using a changing an element in a shallow results in changing the original.

`[[1, 2], 3, 4]` #this mfer

As we discussed earlier, this object gets created in the heap. However, we assumed that 
Python would put all 3 elements in the heap memory allocated for the list object. We now 
have a nested list, though. That list, `[1, 2]`, can't be stored directly in the `[[1, 2], 3, 4]` list. Instead, Python allocates additional memory on the heap for the inner list `([1, 2])`. Instead of storing `[1, 2]` in the memory allocated for `[[1, 2], 3, 4]`, it stores a pointer to the `[1, 2]` object. The actual memory picture is more complicated than this. The integers from both lists are also stored as separate objects. 

A shallow copy of an object is a duplicate of the original object's outermost (topmost) 
level. Any nested objects within the copied object aren't duplicated; they still reference 
the nested objects from the original object. Thus, if you mutate the nested objects in the 
original, those mutations will be visible in the duplicate.

A deep copy of an object is an exact duplicate of the original object at the outermost (or 
topmost) level and every nested object, no matter how deeply nested. There's basically 
nothing you can do to the original object that can be seen in the duplicate or vice versa.

Note that `copy.deepcopy()` doesn't duplicate everything; in most cases, it only duplicates mutable objects. Since immutable objects don't change, there's no need to copy them - references are enough to ensure a deep copy that works.

Shallow copies work best when:

* working with objects that are not collections, e.g., integers and booleans.
* working with immutable objects with no mutable components, e.g., strings.
* working with collections that have no mutable elements, e.g., tuples that don't 
contain mutable elements.
* needed for performance reasons. 

Shallow copies are always faster . You don't care if the mutable components of an object are shared.

You should use deep copies when shallow copies are not okay. In particular, they work best 
when working with collections that have mutable elements, e.g., nested lists.

To reiterate on deep vs shallow copy:

Referencing this code:
```python
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
```

A deep copy makes a duplicate of every item in an existing list. In particular, it creates 
completely new instances of any nested objects in the source. If we performed a deep copy 
on `my_list1`, using a `deepcopy()` function we would have two different lists and four 
separate dictionaries.

We'll only have 3 integers, however, due to optimizations performed by Python with 
immutable values. We'll talk about what that is in a later course.

A shallow copy only makes a duplicate of the outermost values in an object. If we perform 
a shallow copy on `my_list1`, we end up with two different lists, but we still only have 
one occurrence each of `{ first: 42 }` and `{ second: 'value2' }`. In this case, both 
`my_list1[0]` and `my_list2[0]` point to the same dictionary in memory. Likewise, 
`my_list1[1]` and `my_list2[1]` point to the `{ second: 'value2' }` dictionary.

The `copy()` function performs shallow copies. 

