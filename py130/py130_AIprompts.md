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