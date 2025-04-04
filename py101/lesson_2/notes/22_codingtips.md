## Coding Tips

**Variable names should describe the content of the variable**. Typically, you don't want to hardcode possible values into a variable name because of future uncertainty. Instead, try to capture the intent of the variable.

Names that follow the naming conventions in the Python style guide are referred to as 
**idiomatic names**. In particular, whether a name is idiomatic or not depends on what kind of name we're describing. 

A **magic** number is a number (or other simple value) that appears in your program without any information that describes what that number represents. **The way to avoid magic numbers is to use constants.** Another consideration when defining constants is whether the meaning of the number is clear. 

Constants are values that remain unchanged throughout the program's execution. In Python, 
you should avoid mutating (changing) constants to ensure the integrity of your code's 
logic. **Use SCREAMING_SNAKE_CASE to indicate constants**, and treat them as read-only 
values.

***

#### Function Guidelines

Make sure that the function does one thing, and that its responsibility is limited. 
That implies that your functions should be short (say, 10 lines or less). If it's more 
than 15 lines long, consider splitting it into 2 or more functions.

A function is said to have side effects if it does any of the following:

* It reassigns any non-local variable. Reassigning a variable in the outer scope would be 
a side effect.

* It modifies the value of any data structure passed as an argument, or accessed directly from the outer scope. Mutating an object, such as appending an element to a list argument, is an example of a side effect.

* It reads from or writes to a file, network connection, browser, or the system hardware. 
Side effects like this include printing and reading input from the terminal.

* It raises an exception without handling it.

* It calls another function that has side effects.

Most functions should return a useful value or they should have a side effect, but 
not both. 

Function names should reflect whether side effects may occur.

**Function Names Should Reflect What They Do.**
