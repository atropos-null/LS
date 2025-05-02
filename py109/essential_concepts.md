## PY109 Essential Concepts

Assignment statements in the local function cannot change variables defined outside the function.

While you can access global variables from inside functions, you cannot reassign them without using the global keyword.

When you pass a variable to a function, the function parameter becomes a new reference to the same object that the argument variable points to, not the variable itself. An independent copy of that variable is not created.  Whether modifications inside the function affect the original object depends on whether the object is mutable or immutable.
