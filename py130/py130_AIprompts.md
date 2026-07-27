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