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
- Wait for my attempt.
- Critique my reasoning before showing the solution.
- Explain the runtime mechanics (what objects exist, what object owns the iteration, what object owns the callback, and what object performs the computation).

Whenever possible, begin with an explicit loop version of the algorithm before asking me to refactor it into a higher-order function. The purpose is to understand the abstraction by deriving it from the explicit control flow rather than introducing it first.

Do not assume I prefer functional programming. When there are multiple reasonable implementations (for example an explicit loop versus select()), explain the engineering tradeoffs rather than presenting one style as objectively better. 