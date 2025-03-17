## Preventing Errors

#### LBYL: Look Before You Leap

The LBYL approach typically uses one or more guard clauses to ensure that data meets 
the specific preconditions a function expect.

Guard clauses are best used when a function cannot assume that its arguments are valid. 
Invalid arguments can have incorrect types, structures, values, or properties.

#### EAFP: It's Easier to Ask Forgiveness than Permission

The EAFP approach involves trying an operation and handling any exceptions that arise. 
This approach assumes that the code will execute successfully and handles exceptions only 
if something goes wrong. 

Exception handling often arises in EAFP code due to its nature of trying operations without explicit checks.

#### Detecting Edge Cases:

To identify edge cases that could potentially disrupt your program, begin by analyzing the 
inputs to your code. In most functions, these inputs are typically the arguments. Each 
argument may have certain values that can lead to unexpected behavior.