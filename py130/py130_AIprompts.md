# PY130 AI Prompts

## Lesson 1 Practice Prompt

I am studying Launch School PY130 and am currently working only on Lesson 1 (First-Class Functions, Higher-Order Functions, each, select, map, filter, and simple lambdas). Generate 10 practice problems that gradually increase in difficulty.

Requirements:

- The problems should focus on understanding higher-order functions through object-oriented design, similar to the `TodoList` project.
- The goal is to practice recognizing when an explicit loop can be replaced by an existing higher-order method such as `each()` or `select()`.
- Please do not introduce closures, nested functions that capture variables, decorators, generators, partial functions, or any concepts from later lessons.


Include a mixture of:

- writing an explicit loop
- refactoring an explicit loop into each() or select()
- writing appropriate lambda callbacks
- deciding when an explicit loop is clearer than introducing another abstraction
- tracing control flow through callbacks
- predicting the result of code using each, select, map, and filter.

Please avoid one-line trick questions. Each problem should teach one important idea.

For every problem:

- Give the problem statement.
- Do not give the solution immediately.
- Critique my reasoning before showing the solution.
- Explain the runtime mechanics (what objects exist, what object owns the iteration, what object owns the callback, and what object performs the computation).
- Do not ask whether I am ready. Do not add transition messages. 
- Do not repeat these instructions. 
- After reviewing Problem 10, give me a short overall assessment of which concepts appear solid and which need more practice.

Whenever possible, begin with an explicit loop version of the algorithm before asking me to refactor it into a higher-order function. The purpose is to understand the abstraction by deriving it from the explicit control flow rather than introducing it first.

Do not assume I prefer functional programming. When there are multiple reasonable implementations (for example an explicit loop versus select()), explain the engineering tradeoffs rather than presenting one style as objectively better. 

### Practice Prompt for Lambdas

I am studying Launch School PY130 and want to become completely fluent writing simple lambda expressions before moving on to the next lesson.

Generate 30 exercises whose only purpose is to practice writing lambda expressions.

Requirements:

Stay strictly within PY130 Lesson 1.
Do not introduce closures, generators, decorators, partial functions, nested functions, recursion, or any later-course concepts.
The only thing I should write is the lambda.

For each exercise provide:

A short description of the desired behavior.
The surrounding code already written.
A blank where only the lambda belongs.

Example: `filter( __________ , tasks) #Keep only unfinished tasks.`

or ` tasks.sort(key = __________) #Sort by priority`

or `select( __________ ) #Keep only tasks assigned to "Alice"`

or `map( __________ , numbers) # Return each number squared`

Include a wide variety of situations:

boolean predicates
attribute lookup
object properties
string methods
dictionary access
tuple access
arithmetic
sorting with key=
sorted()
max(key=...)
min(key=...)
map
filter
custom collection methods like select
combining conditions with and
combining conditions with or
using not

Keep every lambda to a single expression.

Avoid trick questions.

Do not provide hints.

Do not provide solutions.

Do not tell me whether my answers are correct as I work.

After all 30 exercises, stop.

Wait until I explicitly say:

"Show me all solutions."

Only then provide the complete answer key with brief explanations.

### Practice Prompt for Generators

You are my Launch School PY130 practice partner. I am studying generators in Python. Your job is to help me become fluent by writing code, not by lecturing.
Overall Structure. Create 20 generator programming exercises appropriate for the PY130/PY139 level.

The problems should progress from straightforward to moderately challenging.The emphasis is on writing generators correctly and recognizing situations where generators are preferable to lists. Do not ask me whether I am ready before continuing. Present all 20 exercises in one response.

For each exercise include:

1. Problem Statement
- Describe a realistic programming problem.
- Avoid trivial "yield numbers from 1 to 10" unless it serves as an introductory warm-up.
- Prefer practical problems involving:

    - sequences
    - filtering
    - transformations
    - file-like processing
    - pipelines
    - infinite generators
    - generator expressions
    - `yield from`
    - lazy computation


2. Function Signature
Provide the function signature only. Example: `def even_numbers(iterable):` Do not provide the implementation.

3. Test Cases
Provide several assertions. Example: `assert list(even_numbers([1,2,3,4])) == [2,4]` Use enough tests to completely specify the required behavior.
Include edge cases where appropriate.

4. Instructor Verification
After writing the tests, verify that:

- every expected value is correct
- every edge case is correct
- the tests are internally consistent
- the tests accurately match the problem statement
- If you discover a mistake, fix it before presenting the exercise.

Difficulty Progression: Structure the problems approximately like this:

- Questions 1–5
    - basic generators
    - simple yield
    - finite sequences

- Questions 6–10
    - filtering
    - transformations
    - generator expressions
    - composing generators

- Questions 11–15
    - yield from
    - infinite generators
    - stateful generators
    - multiple generators working together

- Questions 16–20
    - realistic programming exercises
    - streaming data
    - lazy processing pipelines
    - more open-ended design problems appropriate for PY130

Important Constraints:
- Do not provide solutions.
- Do not explain how to solve the problems.
- Do not hint at the algorithm.

Only provide:
- the problem statement
- the function signature
- the verified test cases

The goal is to simulate Launch School-style practice where the tests define the contract and I write the implementation.


### Practice Prompt for Generators, two people

Create 20 generator-writing exercises for two Launch School students working together at the PY130/PY139 level. We will take turns choosing a problem, writing a solution, reviewing each other’s code, and running the supplied tests. Present all 20 exercises at once so we can select and assign them ourselves.
These should be concrete programming exercises rather than broad discussion prompts. Each problem must have a clear, testable contract. Keep the exercises appropriate for students who have just studied:

- generator functions and yield
- generator expressions
- lazy evaluation
- filtering and transforming values
- nested iteration
- combining iterables
- simple delegation with `yield from`

Use ordinary Python data such as:

- lists
- tuples
- strings
- dictionaries
- ranges
- nested collections
- arbitrary finite iterables
- simple domain objects represented by dictionaries or small classes

Avoid:

- Fibonacci sequences
- prime-number generation
- permutations and combinations
- random-number generators
- dates and calendars
- infinite generators
- recursion
- files and streaming data
- networking
- concurrency
- async generators
- `send()`, `throw()`, and `close()`
- advanced algorithms
- LeetCode-style puzzles

Favor practical collection-processing tasks that resemble Launch School exercises. Examples might involve selecting records, transforming values, traversing nested collections one level deep, producing running state, repeating or skipping items, combining finite iterables, and reimplementing simple iterable tools.

For each exercise, provide:

- Exercise title
- Problem statement
- Required function signature
- A precise behavioral contract
- Comprehensive test cases using assert
- A brief note stating what each group of tests verifies

Before presenting an exercise, verify the tests yourself. Make sure:
- every expected result is correct;
- the tests agree with the written contract;
- the function signature supports the required behavior;
- edge cases are defined consistently;
- the exercise is solvable at the stated level;
- no test accidentally depends on consuming the same generator twice;
- tests convert generators to lists only when verifying their yielded values;
- tests do not incorrectly compare a generator object directly with a list;
- tests account for one-pass exhaustion where relevant.

Include tests for:

- normal input;
- empty input;
- a small boundary case;
- ordering of yielded values;
- preservation of duplicates where applicable;
- behavior with arbitrary iterables rather than only lists, when the contract claims to accept an iterable.

Do not use:

- collections.abc.Iterator
- itertools
- any third-party libraries

The tests should only rely on features already introduced in PY130.

Test Summary: After the tests, include a brief note explaining what the tests verify.

Use fresh generator instances in separate tests. Do not reuse an exhausted generator unless exhaustion itself is being tested. When a problem asks for a generator expression rather than a generator function, clearly state that requirement and provide tests appropriate to the returned generator expression.

Do not provide:

- solutions;
- partial implementations;
- pseudocode;
- algorithmic hints;
- step-by-step guidance;
- hidden assumptions about how the problem should be solved.
- The two students should be able to determine the implementation from the contract and tests alone.
 
Arrange the exercises in a gradual progression:

- Exercises 1–5: basic yielding, filtering, and transformation
- Exercises 6–10: nested loops, stateful finite generators, and arbitrary iterables
- Exercises 11–15: combining, alternating, grouping, and delegating with yield from
- Exercises 16–20: richer finite collection-processing problems with multiple contract requirements
- Avoid merely producing twenty versions of “yield values that satisfy a condition.” Vary the movement of data and the state that must be preserved between yields.

### Bridge Prompt: Generators and Files

Generate 10 programming exercises that bridge the concepts of Generators and Files in Launch School's PY130 course.

Purpose: These exercises are intended to help students discover how generator functions naturally operate on sequences of lines and prepare them to recognize that file objects are iterable.

Assume students know:
* opening files with open
* context managers (with)
* iterating over file objects
* generator functions
* `yield`
* generator expressions
* lazy evaluation
* simple uses of `yield from`

Do not assume knowledge of:
* itertools
* io.StringIO
* decorators
* closures
* recursion
* regular expressions
* asynchronous generators
* `send`, `throw`, or `close`

Exercise Design: Treat every exercise as if it were completed inside a single Python file in an online coding environment such as CoderPad.

Do not require students to:
* create external files
* create additional Python files
* copy text into data files
* download resources
* perform any setup outside the supplied code
* Instead, whenever an exercise involves "file contents", provide the input as an iterable of strings.

For example:
```python
lines = [
    "Apple",
    "Banana",
    "Cherry",
    "Apple Pie",
]
```

```python
or
lines = (
    "Alice,95",
    "Bob,81",
    "Carol,90",
)
```

Students should write generators that operate on these iterables exactly as they would operate on a file object.

Desired Concepts

Across the ten exercises, naturally introduce ideas such as:
* consuming an iterable of lines
* transforming yielded lines
* filtering yielded lines
* skipping selected lines
* composing multiple generators
* building lazy processing pipelines
* separating reading from processing
* passing one generator into another

The exercises should naturally lead students toward designs similar to:

```python
def matching_lines(lines, pattern):
    for line in lines:
        if pattern in line:
            yield line
```

without reproducing the same functions directly.

Output Format: For each exercise provide:
* Title
* Problem Statement
* Function Signature
* Complete contract using bullet points beginning with "The function must..."
* Complete, ready-to-run assert statements
* Every exercise must be completely self-contained.

The students should never need to invent:
* sample data
* test cases
* expected output
* helper functions
* debugging code

Do Not Include
* solutions
* pseudocode
* implementation hints
* algorithm descriptions

Before presenting the exercises, verify that:
* every exercise is internally consistent
* every expected output is correct
* every exercise can be solved using only the concepts listed above
* each exercise builds naturally toward understanding generators over file-like data.

## Lesson 2 Practice Prompts

### Arguments & Parameters Deep Practice

Generate 15 programming exercises for students studying Arguments and Parameters in Launch School's PY130 course. Purpose: These exercises 
should develop a deep understanding of Python's argument binding rules rather than simply practicing the syntax.

Assume students already know:
* positional arguments
* keyword arguments
* default values
* positional-only parameters (/)
* keyword-only parameters (*)
* *args
* **kwargs

Do not assume knowledge of decorators, typing, dataclasses, or other later PY130 topics.

Design Philosophy: The goal is to make students reason about how Python matches arguments to parameters.Favor exercises that require students to think about valid and invalid function calls, API design, and function signatures. Avoid repetitive "write another function that accepts *args" problems. Whenever possible, make the central challenge understanding how Python binds arguments to parameters at function call time, rather than memorizing syntax.

Desired Exercise Types
Include a mixture of:
* writing function signatures
* implementing functions
* correcting incorrect signatures
* predicting which function calls succeed
* identifying why particular calls raise TypeError
* designing APIs with positional-only and keyword-only parameters
* choosing appropriate parameter kinds for a given contract
* refactoring an existing function signature to improve usability
* implementing small utility functions using *args or **kwargs
* combining multiple parameter kinds correctly

Output Format

Each exercise must include:
* Title
* Problem Statement
* Function Signature (or indicate that the student must design it)
* Complete contract
* Ready-to-run assert statements
* If the exercise concerns invalid calls, include the example calls directly.

For example:
```python
foo(1, 2)
foo(a=1, b=2)
foo(1, b=2)
```

The student should determine which succeed and why. Do not require students to invent test cases. Every exercise must be self-contained.

Difficulty: Arrange the exercises from easier to moderately challenging. The final exercises should require combining several parameter kinds correctly.

Do Not Include
* solutions
* pseudocode
* implementation hints

Before presenting the exercises, verify that:
* every valid call is actually valid;
* every invalid call genuinely raises a TypeError;
* every function signature matches the stated contract;
* every exercise is internally consistent.

