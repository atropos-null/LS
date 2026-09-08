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

### Iterable Unpacking Practice

Generate **20 programming exercises** for students studying **Iterable Unpacking** in Launch School's PY130 course.

Purpose: 

The goal is to develop fluency with iterable unpacking as a programming technique rather than merely testing syntax.

Assume students already know:

- tuple unpacking
- starred unpacking (`*rest`)
- nested unpacking
- unpacking strings
- unpacking in assignment
- swapping variables
- iterable unpacking in general

Do **not** assume knowledge of:

- decorators
- closures
- advanced pattern matching
- typing
- dataclasses
- later PY130 topics

Design Philosophy: The goal is for students to recognize iterable unpacking as a general mechanism for expressing the structure of data, not merely as convenient tuple syntax. Favor implementation problems over output-prediction questions. At least **75%** of the exercises should require writing code.

The exercises should resemble realistic Launch School programming assignments rather than isolated syntax drills.

Desired Exercise Types: 

Include a mixture of:

- implementing small utility functions
- debugging incorrect unpacking
- refactoring code that uses indexing into cleaner unpacking
- unpacking inside `for` loops
- nested unpacking
- starred unpacking
- unpacking function return values
- unpacking dictionary items
- unpacking generator output
- designing concise implementations using unpacking

Limit simple output-prediction questions to **no more than three** exercises.

Avoid producing many variations of:

- "What does this print?"
- "Will this raise an error?"

Instead, require students to use unpacking as part of solving programming problems.

Output Format: 

For each exercise provide:

- Exercise Title
- Problem Statement
- Function Signature (if applicable)
- Complete contract using bullet points beginning with **"The function must..."**
- Complete, ready-to-run `assert` statements

Every exercise must be completely self-contained.

The student should never need to invent:

- sample data
- expected output
- helper functions
- test cases
- setup code

Do **not** provide:

- solutions
- pseudocode
- implementation hints
- algorithm descriptions

Quality Verification: 

Before presenting the exercises:

- mentally execute every unpacking operation;
- verify every assignment binds exactly as Python would;
- verify every expected exception is correct;
- verify every expected output is correct;
- verify every test agrees with the written contract;
- reject and regenerate any exercise that is internally inconsistent.

Progression:  Arrange the exercises from easier to moderately challenging. Each exercise should introduce a new application of iterable unpacking rather than repeating the same pattern with different variable names. The later exercises should combine unpacking with previously learned PY130 concepts where appropriate, while remaining within material already covered.


### Closures Deep Practice

Generate a **20-exercise learning module** for students studying **Closures** in Launch School's PY130 course.

#### Primary Goal

Design these exercises as though you are writing the Closures chapter of a programming textbook.

The goal is **not** to generate twenty independent problems.

The goal is to gradually build the student's intuition for closures until they naturally recognize when a closure is the correct design.

Every exercise should build directly upon previous exercises.

The entire collection should read like one coherent lesson.

#### Assumed Knowledge

Students already know:

- nested functions
- lexical scope
- first-class functions
- higher-order functions
- generators
- iterable unpacking
- arguments and parameters

Do **not** assume knowledge of:

- decorators
- classes as an alternative to closures
- descriptors
- concurrency
- advanced functional programming
- later PY130 topics

#### Learning Progression

Design the module around the following progression.

#### Part 1 — Capturing Configuration (Exercises 1–4)

Students should learn that closures naturally capture configuration.

Examples include:

- configurable mathematical operations
- configurable string processing
- configurable predicates
- configurable formatting

No mutable state.

No `nonlocal`.

No debugging.


#### Part 2 — Persistent State (Exercises 5–8)

Introduce:

- state surviving between calls
- `nonlocal`
- independent closure instances

Only one new idea per exercise.


#### Part 3 — Closures as Design Tools (Exercises 9–12)

Students should begin using closures to build useful abstractions.

Examples include:

- configurable validation
- configurable transformations
- wrappers
- pipelines
- dispatchers
- reusable utilities

The emphasis is **why** a closure is useful.

#### Part 4 — Closure Reasoning (Exercises 13–16)

Practice reading and debugging closures.

Include:

- captured variables
- mutable versus immutable captured objects
- independent closure instances
- missing `nonlocal`
- late binding in loops

Limit output prediction to **three** exercises maximum.

#### Part 5 — Design Recognition (Exercises 17–20)

Present ordinary programming problems.

Do **not** mention:

- closures
- closure
- captured variables
- lexical scope
- nested functions
- inner functions
- function factories
- `nonlocal`

The requirements should naturally lead students to conclude that returning a function is the cleanest design.

These should feel like normal programming assignments.

#### Design Principles

Favor implementation.

At least **85%** of the exercises should require writing code.

Avoid interview puzzles.

Avoid trick questions.

Avoid repeating the same underlying idea with different names.

Difficulty should increase because students combine closure ideas, not because unrelated Python features are introduced.

Do not introduce:

- pytest
- stdout capture
- io.StringIO
- timing
- randomness
- unrelated imports

unless absolutely necessary.

#### Output Format

Each exercise must include:

- Exercise Title
- Problem Statement
- Function Signature (or state that the student must design it)
- Complete contract beginning with "The function must..."
- Complete ready-to-run assert statements

Every exercise must be completely self-contained.

Students should never need to invent:

- helper functions
- test cases
- sample data
- expected output
- setup code

Do not include:

- solutions
- hints
- pseudocode

#### Validation Pass 1 — Individual Exercises

Before presenting an exercise:

- mentally execute every closure;
- verify captured state behaves correctly;
- verify every expected output;
- verify every assert passes;
- verify the contract, tests, and function signature describe the same API.

If any inconsistency exists, regenerate the exercise.

#### Validation Pass 2 — Entire Learning Module

Before presenting the final collection:

Verify that:

- every exercise appears in an appropriate place in the progression;
- no concept is introduced before prerequisite concepts;
- there are no duplicate exercises disguised with different names;
- each exercise introduces one new closure idea;
- the final four exercises genuinely require students to recognize that a closure is the natural design without being told.

Reject and regenerate any exercise that violates the progression.

The final result should read like a carefully designed chapter from a programming textbook rather than twenty independently generated programming exercises.

### Decorators Practice — Prompt 1: Mechanics and Execution Model

Generate a focused learning-mode practice set for students studying **Python decorators** in Launch School's PY130 course.

#### Primary Goal

The exercises should build a precise operational model of what decorators do. The student should become comfortable reasoning about:

- manual decoration
- `@decorator` syntax
- the equivalence between `@decorator` and function rebinding
- wrapper functions
- forwarding arguments
- what object is passed into a decorator
- what object is returned
- decoration time versus function invocation time
- what code runs once during decoration
- what code runs each time the decorated function is called

This is **Learning Mode**, not assessment preparation.

The exercises should isolate these mechanics before introducing more complex decorator combinations.

#### Assumed Knowledge

Students already know:

- first-class functions
- higher-order functions
- nested functions
- closures
- lexical scope
- `*args`
- `**kwargs`
- basic exception behavior
- normal function calls and return values

Students are currently learning decorators.

#### Do Not Use Yet

Do not require knowledge of:

- decorator factories
- decorators with configurable arguments
- stacked decorators
- class-based decorators
- callable objects as decorators
- advanced `functools.wraps` behavior
- caching
- retries
- logging frameworks
- descriptors
- async functions
- generators as decorator machinery
- metaclasses
- third-party libraries

Simple use of `functools.wraps` should also be excluded from this set. Metadata preservation will be practiced separately.

#### Exercise Count

First, internally identify the distinct reasoning and implementation patterns available within this narrow topic.

Generate **between 6 and 10 exercises**.

Do not add exercises merely to reach 10.

If two proposed exercises have essentially the same reasoning structure and one does not add a meaningful new difficulty or concept, remove one.

The final set may contain fewer than 10 exercises.

#### Progression

The progression must feel intentional:

**isolate → combine → perturb → diagnose → synthesize**

Do not jump unpredictably in difficulty.

#### Early Exercises

Begin with very direct mechanics such as:

- manually applying a decorator
- rewriting `@decorator` syntax as ordinary assignment
- identifying what function object is passed to a decorator
- identifying what function object is ultimately bound to the original function name
- simple wrappers that forward arguments and return values

These exercises should be easy enough that the student can focus entirely on the execution model.

#### Middle Exercises

Gradually introduce combinations such as:

- wrappers using `*args` and `**kwargs`
- code that executes during decoration
- code that executes during invocation
- multiple calls to the same decorated function
- decorators applied to different functions
- distinguishing outer-scope setup from per-call behavior

Difficulty should increase through reasoning about execution order, not through unrelated Python features.

#### Later Exercises

Introduce perturbation and diagnosis:

- code with a subtle incorrect wrapper
- incorrect return forwarding
- incorrect argument forwarding
- confusion between calling a function and returning a function
- confusion between decoration-time execution and invocation-time execution
- manually decorated code whose final binding must be traced

The final one or two exercises should require synthesis of several mechanics from earlier exercises, but should still remain entirely within the scope of basic decorators.

Do not introduce stacked decorators yet.

#### Exercise Types

Use a deliberate mix of:

- code-writing exercises
- trace-the-execution exercises
- rewrite-equivalence exercises
- debugging exercises
- short explanation exercises

At least **60% of the exercises should require the student to write or repair code**.

Do not let the set become mostly output-prediction questions.

#### Structural Diversity

Before presenting the set, internally classify each candidate exercise by its primary reasoning structure.

Possible structures include:

- manual decoration
- `@` syntax equivalence
- wrapper implementation
- positional and keyword forwarding
- return-value forwarding
- decoration-time tracing
- invocation-time tracing
- function rebinding
- debugging wrapper behavior
- identifying which function object is currently bound to a name

Do not use the same primary structure more than twice unless the second exercise clearly increases the reasoning demand.

Changing names, domains, or sample values does not create a new exercise architecture.

#### Implementation Exercise Format

For implementation exercises, provide:

- Exercise Title
- Problem Statement
- Complete Function Signature
- Contract
- Ready-to-run tests

The contract should describe observable behavior.

Do not tell the student exactly how to implement the decorator unless the syntax itself is the learning objective.

#### Reasoning Exercise Format

For tracing or explanation exercises, provide:

- Exercise Title
- Problem Statement
- Complete runnable code
- A precise question about what happens and why

Do not provide the answer.

#### Debugging Exercise Rules

If you include a debugging exercise:

- the provided code must genuinely violate the stated contract;
- the bug must arise primarily from decorator mechanics;
- validate the buggy behavior before presenting it;
- do not introduce an unrelated Python bug;
- do not include the corrected implementation anywhere;
- do not reveal the exact fix in comments, tests, or contract wording.

If a proposed debugging exercise is invalid, discard it completely and generate a replacement internally.

Do not display correction commentary such as:

- "Correction"
- "Revised exercise"
- "Actually, the previous code works"
- generation or validation notes

#### Solution Leakage Rule

Never include the student's target implementation in:

- setup code
- tests
- comments
- examples
- contracts
- helper functions

Before displaying each exercise, scan all supplied material for code that directly solves the requested task.

If the solution appears anywhere, discard or rewrite the exercise before presenting it.

Do not encode the solution in the contract through wording such as:

- "use a nested function"
- "return the wrapper"
- "rebind the function"
- "add `*args` and `**kwargs`"

unless that exact syntax is itself what the exercise is explicitly testing.

#### Curriculum Boundary Audit

Before presenting the final set, internally inspect the intended solution to every exercise. Identify every Python mechanism required to solve it. Reject or redesign any exercise whose intended solution depends on material outside the stated assumed knowledge. Do not lower the reasoning difficulty merely because an exercise crosses the curriculum boundary. Instead, redesign the problem so that the same kind of reasoning can be done using only already-learned material.

#### Validation Pass — Individual Exercises

Before displaying an exercise:

- mentally execute all supplied code;
- verify every test;
- verify all function calls bind correctly;
- verify return values match the stated contract;
- verify decoration-time and invocation-time claims;
- verify the function signature, problem statement, contract, and tests all describe one consistent task;
- verify no code accidentally solves the exercise for the student.

Reject and regenerate any exercise that fails validation.

#### Validation Pass — Whole Set

After generating all candidate exercises, audit the entire set.

Verify that:

- difficulty generally rises from beginning to end;
- later exercises are not simpler than substantially earlier ones without a pedagogical reason;
- no exercise architecture is repeated excessively;
- the set covers both implementation and reasoning;
- decoration time versus invocation time is practiced explicitly;
- manual decoration and `@` syntax equivalence are both practiced;
- argument and return forwarding are both practiced;
- at least one exercise requires debugging decorator mechanics;
- no exercise uses stacked decorators;
- no exercise requires later decorator material;
- no exercise exists merely to increase the exercise count.

If two exercises are structurally redundant, remove the weaker one.

Do **not** replace a removed duplicate merely to preserve the original count.

#### Final Output Rule

The final set should feel like a carefully sequenced mini-unit on **how basic decorators actually execute**.

It should move from direct mechanics toward controlled reasoning and diagnosis without sudden jumps in difficulty.

Do not provide solutions, pseudocode, implementation hints, or answer keys.

### Decorators Practice — Prompt 2: Factories and State

Generate exactly **7 Learning Mode exercises** on decorator factories and stateful decorators.

The student already understands basic decorators, wrappers, closures, lexical scope, `*args`, `**kwargs`, argument/return forwarding, and decoration time vs invocation time.

The student is now practicing:

- decorator factories
- persistent state
- `nonlocal` and rebinding
- mutation without rebinding
- independent vs shared state
- state ownership and lifetime

Central question:

**Where does the state live, when is it created, who shares it, and what changes it?**

#### Required Progression

Each exercise has a distinct learning job:

1. **Factory mechanics** — Implement a decorator factory with configuration. No changing state yet.

2. **Scalar state + rebinding** — Persistent scalar state requiring rebinding and `nonlocal`. Do not use a call counter.

3. **Mutable state** — Persistent list/dictionary state changed through mutation. Do not tell the student whether `nonlocal` is needed.

4. **Independent state** — Separate applications of the same decorator/factory must maintain independent state. Do not use call counting.

5. **Shared state** — Two decorated functions intentionally share state, **without stacked decorators**. The student must determine how to arrange the state so sharing occurs.

6. **State ownership and lifetime** — Give working code containing multiple closures or decorator applications. Ask the student to trace which functions share state and which have independent state, and predict observable results. The supplied code must be correct; do not manufacture deliberately buggy code.

7. **Synthesis** — The hardest exercise. Combine at least three mechanisms from Exercises 1–6. State requirements primarily as observable behavior and let the student design the closure/state structure.

Difficulty should generally rise:

**isolate → distinguish → compare → reason → synthesize**

Later exercises should provide less implementation guidance than earlier ones.

#### Diversity Rules

Exercises 2–6 must differ primarily in **state ownership, lifetime, rebinding, or mutation**, not merely in what the state represents.

No more than two exercises may use:

**scalar/boolean state → inspect → change → conditionally behave**

Counters, limiters, run-once gates, toggles, attempt trackers, etc. count as the same broad architecture.

Do not create thematic reskins of the same solution.

#### Scope

Do not use:

- stacked decorators
- `functools.wraps`
- class-based or callable-object decorators
- caching or retries
- complex exception-handling decorators
- descriptors, async, metaclasses
- third-party libraries

Synthesis means combining mechanisms already practiced, not introducing a new decorator topic.

#### Output

For implementation exercises provide:

- Title
- Problem Statement
- Complete Function Signature
- Ready-to-run tests

For reasoning exercises provide complete runnable code and a precise question.

Do not include a Contract section. Add clarifications only when necessary.

Do not provide solutions, hints, pseudocode, or answer keys.

#### Quality Control

Before displaying the exercises:

- mentally solve each exercise and verify all tests and expected outputs;
- use only deterministic tests — no randomness;
- verify each exercise performs its assigned learning job;
- verify state ownership, persistence, sharing, mutation, rebinding, and `nonlocal` behavior are correct;
- verify no excluded mechanisms appear;
- verify Exercises 2–6 are structurally different.

For Exercise 6 specifically, trace each call to an enclosing function and determine which state object each resulting closure captures. Only present the exercise if the predicted sharing and independence follow from the supplied code.

Finally ask:

**What reasoning is the student supposed to perform?**

Do not give away that reasoning in the problem statement, comments, tests, or supplied code.

If an exercise fails its assigned learning job or validation, silently replace it.

Do not provide generation commentary.

### Decorators Practice — Prompt 3: Persistent State with Collection Operations

Generate a Learning Mode practice set combining decorators and closure state with ordinary Python collection operations.

The student already understands decorators, decorator factories, closures, lexical scope, `nonlocal`, `*args`/`**kwargs`, and basic persistent state.

The student also knows ordinary list, dictionary, tuple, string, iteration, and collection-processing operations from earlier Python study.

#### Goal

Every exercise should test two layers:

1. **State semantics:** Where does persistent state live? When is it created? Who owns or shares it?
2. **Collection semantics:** How must that state be correctly initialized, accessed, mutated, accumulated, or updated?

The advanced Python mechanism should determine **where state lives or how behavior is routed**. Ordinary Python operations should determine **how that state changes**.

Do not make the collection work an unrelated algorithm puzzle. Difficulty should come from correctly coordinating these two layers.

#### Exercise Design

Generate 6–8 exercises with increasing difficulty and decreasing scaffolding.

Use varied state structures such as:

- dictionary → list of tuples
- dictionary → counts or accumulated values
- list → dictionaries/records
- nested dictionaries/lists
- separate collections owned by separate decorated functions
- one shared collection partitioned by key

Include both implementation and debugging/repair problems.

Across the set, exercise realistic mistakes such as:

- replacing a list when it should be mutated
- resetting a dictionary entry on every call
- appending at the wrong nesting level
- accidentally sharing one list across several keys
- overwriting accumulated values instead of updating them
- using the wrong dictionary key
- confusing `args`, `[args]`, and `list(args)`
- confusing tuple structure inside a list
- initializing persistent state inside the wrapper
- mutating the correct object at the wrong time
- using a local temporary where persistent state is required
- accumulating globally when state should be per-decorated-function
- making state independent when it should be shared

Do not identify the bug category in the problem statement. The student must diagnose it from the required and actual behavior.

Avoid producing several exercises that differ only in story or variable names.

#### Scope

Keep decorators/closures as the advanced mechanism for this set. Do not introduce stacked decorators, class-based decorators, caching, retries, async, descriptors, metaclasses, or third-party libraries.

Earlier Python operations may be mixed freely when they are routine rather than the primary new challenge.

#### Output

Use identical formatting for every exercise.

Use fenced Python code blocks for all code and prose outside them.

Prefer `assert` tests. Use `print()` only when printed output is itself required behavior. No decorative output, difficulty labels, Contracts, solutions, hints, pseudocode, or answer keys.

#### Validation

Before displaying each exercise, mentally execute it and verify:

- the intended state actually persists;
- sharing/independence matches the specification;
- collection initialization occurs at the correct time;
- each mutation/update produces the stated structure;
- tests and expected values are correct;
- the exercise genuinely requires both state reasoning and collection reasoning.

For debugging exercises, verify the supplied bug actually produces the claimed failure.

Do not reveal the reasoning the student is supposed to perform.

### Decorators Practice - Prompt 4: Stacked Decorators

Generate 6–8 Learning Mode exercises on stacked decorators.

The student already understands basic decorators, wrappers, decorator factories, closures, persistent state, `nonlocal`, `*args`/`**kwargs`, argument forwarding, decoration vs invocation time, and ordinary list/dictionary/string operations.

This is the student's first focused practice set on STACKING decorators.

#### Goal

Teach the student to reason accurately when two decorators are applied to the same function.

The student should learn to track:

1. how stacked `@decorator` syntax expands into ordinary function calls;
2. which decorator is applied first at decoration time;
3. the resulting nested callable structure;
4. which wrapper executes first at invocation time;
5. how arguments travel inward through the wrappers;
6. how return values travel outward through the wrappers;
7. how one decorator's behavior can affect what another decorator receives or observes;
8. why changing decorator order can change program behavior.

Difficulty should come from composing mechanisms the student already knows, not from introducing new Python features.

#### Progression

Across the set, move roughly through these reasoning jobs:

- manually expand a two-decorator stack and reason about the resulting callable;
- trace decoration time separately from invocation time;
- trace arguments moving through two wrappers;
- trace a return value transformed at more than one layer;
- combine stacking with simple persistent state or ordinary collection/string operations;
- compare the observable behavior of the same two decorators in opposite orders;
- diagnose an incorrect stacked-decorator implementation or ordering;
- synthesize a small two-decorator solution from behavioral requirements.

Do not force all eight jobs if doing so would create weak or structurally repetitive exercises.

Early exercises may explicitly discuss decorator order. Later exercises should increasingly specify observable behavior and require the student to determine what the stack does.

Use TWO decorators per stack for this Learning Mode set. Do not escalate to three or more decorators yet.

#### Structural Diversity

Do not generate a set consisting primarily of "predict the print order" exercises.

Across the batch, vary what the decorators actually do. Appropriate mechanisms include:

- transforming arguments before forwarding them;
- transforming return values;
- recording information in a list or dictionary;
- maintaining simple persistent state;
- conditionally deciding whether to call the wrapped function;
- observing values at different wrapper layers.

Ordinary earlier-Python list, dictionary, tuple, string, iteration, and collection operations may be used as supporting machinery.

Different stories or variable names do not count as structural diversity.

#### Scope

Do not use `functools.wraps`, class-based/callable-object decorators, descriptors, async, generators, metaclasses, third-party libraries, randomness, or three-or-more-decorator stacks.

Do not make caching, retries, or complex exception handling the primary mechanism. Those belong to later decorator practice.

All required mechanisms must already be within the stated curriculum boundary.

#### Output

Use identical formatting for every exercise:

#### Exercise N — Title
**Problem Statement**

For implementation exercises:
**Function Signature**
**Tests**

For reasoning/debugging exercises:
**Code**
**Question**

Put all Python in fenced Python blocks and prose outside them.

Prefer `assert` tests. Use `print()` only when printed output itself is required behavior.

Do not include difficulty labels, decorative separators, Contracts, solutions, hints, pseudocode, answer keys, or implementation instructions that reveal the reasoning the student must perform.

For debugging exercises, do not mark suspicious lines or identify where the bug is.

#### Validation

Before displaying each exercise, mentally execute it.

Verify:

- the stacked `@` syntax corresponds to the intended nested function calls;
- decoration order is correct;
- invocation order is correct;
- arguments and return values pass through the intended layers;
- persistent/shared state has the intended owner and lifetime;
- collection operations produce the exact required structure;
- reversing decorator order actually produces the claimed difference when relevant;
- tests match the API actually returned by the decorators;
- debugging exercises contain the intended bug and no accidental secondary bug;
- no exercise requires an excluded or later mechanism.

Ask internally: "What reasoning must the student perform?"

Make sure the problem statement, comments, setup, and tests have not already performed that reasoning for the student.

Silently discard and replace any exercise that fails validation.

### Decorators Practice - Prompt 5: Metadata and Control Flow

Generate 6–8 Learning Mode exercises.

The student understands decorators, factories, closures/state, `nonlocal`, `*args`/`**kwargs`, argument forwarding, decoration vs invocation time, stacked decorators, and ordinary list/dict/string operations.

Current topics:
- metadata loss through wrapping
- `functools.wraps`
- functions as objects and wrapper attributes
- validation and early return
- raising, catching, and propagating exceptions
- whether/when the wrapped function executes

#### Required Coverage

Build a progressive set drawing from these distinct reasoning areas:

1. Observe metadata loss and repair it with `functools.wraps`.
2. Read/write state exposed through a wrapper attribute such as `.calls`, `.history`, or `.last_result`.
3. Validation that may prevent the wrapped function from executing.
4. A decorator that raises an exception according to a behavioral contract.
5. A wrapped function whose exception propagates through a decorator.
6. A decorator that catches ONE specified exception and handles it.
7. State that changes only when execution succeeds.
8. Synthesis combining metadata preservation with simple execution control.

Generate 6–8 exercises. You do not need to cover every item above. Prioritize strong, structurally distinct exercises over complete coverage or repetition.

Progress from explicit mechanism → behavioral specification. Difficulty should generally increase.

Use ordinary list/dict/string operations as supporting machinery where useful, but not as unrelated puzzles.

#### Scope

Allowed: `functools.wraps`, `__name__`, `__doc__`, wrapper attributes, simple persistent state, factories, two-decorator stacks, validation, early return, raise, narrowly specified `except`, routine collection operations.

Do NOT use class-based decorators/callable objects, caching, retries, broad `except:`, async, descriptors, metaclasses, third-party libraries, randomness, or 3+ decorator stacks.

#### Exercise Quality

Vary the actual execution/state structure, not merely the story.

For debugging problems:
- exactly one intended primary bug;
- do not identify the suspicious line or bug category;
- verify the supplied code genuinely fails for the stated reason.

Do not leak the reasoning the student is meant to perform.

#### Output

Use:
#### Exercise N — Title
**Problem Statement**
**Function Signature**
**Tests**

For reasoning/debugging:
**Code**
**Question**

Python fenced; prose outside.
Use ordinary ASCII spaces only—no tabs or Unicode/non-breaking whitespace.
Prefer asserts for implementation tests.
For prediction exercises, include a simple `print(...)` at the END so the student can predict first and then run it to verify.
No solutions, hints, pseudocode, answer keys, Contracts, decorative separators, or difficulty labels.

#### Validation

Mentally execute every exercise before output.

Verify:
- factory → decorator → wrapper → result structure;
- metadata and wrapper attributes belong to the correct returned object;
- argument/return flow;
- whether the wrapped function actually executes;
- exception raise/catch/propagation behavior;
- state ownership and timing;
- collection/data shape;
- tests match the actual API;
- no excluded mechanism is required.

Silently replace invalid exercises.

### Decorators Practice - Prompt 6: Class-Based Decorators and Callable Objects

Generate 6–8 Learning Mode exercises.

The student already understands:

- functions as first-class objects
- higher-order functions
- closures and persistent state
- ordinary function-based decorators
- decorator factories
- `*args` / `**kwargs`
- stacked decorators
- `functools.wraps`
- wrapper attributes
- validation, early return, and simple exception flow
- Python classes, instances, instance attributes, and `__init__`

Current topics:

- callable objects
- `__call__`
- state stored on callable instances
- class-based decorators
- how class-based decorators correspond to function/closure-based decorators
- construction time versus invocation time
- which object the decorated name refers to

This is Learning Mode. Build understanding and near transfer rather than assessment-style pressure.

#### Goal

The student should learn to reason about objects that participate in function-like behavior through `__call__`.

Across the set, develop these ideas:

1. An ordinary class instance can become callable by defining `__call__`.
2. State can persist naturally in instance attributes between calls.
3. A class can act as a decorator by receiving a function and returning a callable instance.
4. Decoration constructs an object; later function syntax invokes that object's `__call__`.
5. Arguments must still be forwarded correctly to the original function.
6. State may belong to one decorator instance rather than to a closure.
7. Separate decorator applications normally create separate instances and therefore separate state.
8. Function-based and class-based decorators can implement equivalent observable behavior using different state structures.

Generate 6–8 exercises. You do not need to cover every item above. Prioritize strong, structurally distinct exercises over complete coverage or repetition.

Progress from explicit `__call__` mechanics toward behavioral specifications where the student must determine the correct object/state arrangement.

#### Useful Exercise Structures

Vary the reasoning structure. Good possibilities include:

- predict behavior of a simple callable instance;
- implement a callable object with persistent state;
- trace construction versus later calls;
- convert a simple function-based decorator into a class-based decorator;
- maintain state on a decorator instance;
- compare two separately decorated functions and determine whether state is shared;
- debug argument forwarding through `__call__`;
- inspect attributes on the decorated callable object;
- synthesize a small class-based decorator from behavioral requirements.

Ordinary list/dict/string operations may support these exercises but should not become unrelated algorithm puzzles.

#### Scope

Allowed:

- classes and instances
- `__init__`
- `__call__`
- instance attributes
- `*args` / `**kwargs`
- ordinary function decoration
- simple decorator factories already learned
- simple persistent list/dict/scalar state
- previously learned validation or exception behavior when useful

Do NOT use:

- descriptors
- custom `__get__`
- metaclasses
- decorating instance methods in ways that require descriptor knowledge
- async
- generators as the primary mechanism
- third-party libraries
- caching
- retries
- complex logging frameworks
- inheritance hierarchies created only to increase difficulty
- mechanisms outside the stated curriculum boundary

#### Exercise Quality

Difficulty should come from reasoning about:

- what object exists;
- when it is created;
- what the decorated name refers to;
- where persistent state lives;
- which calls share that state;
- how arguments and return values move through `__call__`.

Do not create several exercises that are merely "increment a counter" with different stories.

For debugging problems:

- include exactly one intended primary bug unless explicitly asking for several;
- do not identify the suspicious line or bug category;
- verify the supplied program genuinely fails for the stated reason.

Do not leak the reasoning the student is meant to perform.

#### Output

Use:

#### Exercise N — Title

**Problem Statement**

For implementation exercises:

**Function Signature**

**Tests**

For reasoning/debugging exercises:

**Code**

**Question**

Put all Python inside fenced Python code blocks and prose outside them.

Use ordinary ASCII spaces only. Do not use tabs, non-breaking spaces, or Unicode whitespace.

Prefer `assert` tests.

For prediction exercises, include a simple executable `print(...)` reveal at the end so the student can predict first and then run the program.

No solutions, hints, pseudocode, answer keys, Contracts, decorative separators, or difficulty labels.

#### Validation

Mentally execute every exercise before displaying it.

Verify:

- object construction and `__init__` behavior;
- exactly what object the decorated name refers to;
- when `__call__` executes;
- instance-state ownership and lifetime;
- independent versus shared decorator instances;
- argument forwarding;
- return values;
- wrapper/decorator attributes are inspected on the object actually returned;
- tests match the real API;
- any claimed failure genuinely occurs;
- no descriptor behavior or other excluded mechanism is secretly required.

Internally ask:

"What reasoning must the student perform?"

Ensure that the statement, comments, setup, and tests have not already performed that reasoning.

Silently discard and replace invalid exercises.

### Decorators Practice - Prompt 7: Synthesis and Diagnosis

Generate a Learning Mode practice set that synthesizes ONLY the mechanisms explicitly listed below.

For this prompt, the following list defines the student's complete decorator practice scope. Do not assume knowledge of decorator mechanisms not listed here.

The student has practiced:

- function-based decorators
- decorator factories
- closures and persistent state
- mutation versus rebinding
- independent and shared state
- state stored in lists and dictionaries
- `*args` / `**kwargs`
- decoration time versus invocation time
- two-decorator stacks
- arguments moving inward and results moving outward
- `functools.wraps`
- wrapper attributes
- validation and early return
- raising, catching, and propagating exceptions
- callable objects and `__call__`
- class-based decorators
- ordinary Python list/dict/tuple/string processing

The purpose of this set is to recombine these familiar mechanisms into unfamiliar arrangements.

Do NOT introduce a new decorator feature.

This is Learning Mode: synthesis and diagnosis without timed assessment pressure.

#### Exercise Count

First identify the number of genuinely distinct exercise structures available within this scope.

Generate one strong exercise per distinct structure, up to 8 exercises.

The final count may be 4, 5, 6, 7, or 8.

Do NOT default to 7.

Do NOT add an exercise merely to reach a target count.

If two candidate exercises require essentially the same reasoning or solution architecture, keep the stronger one and discard the other.

#### Synthesis Requirement

Every exercise must combine at least TWO distinct semantic dimensions from this list:

- when a value/configuration is determined;
- where persistent state lives;
- who owns or shares state;
- decoration-time versus invocation-time execution;
- argument flow through wrappers;
- return-value flow through wrappers;
- short-circuiting / whether the next callable executes;
- exception propagation or handling;
- wrapper/function attributes;
- function-based versus class-based decorator structure;
- mutable object identity and collection updates.

Later exercises should usually combine THREE or more dimensions.

Do not count ordinary story changes as synthesis.

#### Avoid Repeating Earlier Exercise Templates

Do NOT make any of these the primary structure of an exercise:

- simple call counter;
- call limiter;
- call-once decorator;
- simple wrapper history/audit log;
- basic metadata-preservation exercise;
- simple selective exception fallback;
- basic mutation-versus-rebinding comparison;
- simple independent-state comparison;
- simple before/after logging;
- basic two-decorator print-order trace;
- caching or memoization;
- retries.

These mechanisms may appear only as supporting pieces inside a genuinely different synthesis problem.

#### Desired Exercise Types

Prefer problems such as:

- two decorators where one changes what the other observes;
- shared external state combined with separate per-decorator state;
- decoration-time registration combined with invocation-time behavior;
- wrapper attributes whose meaning depends on success/failure or decorator order;
- a class-based decorator interacting with a function-based decorator;
- state updated at different layers of a stack;
- validation or short-circuiting that changes whether outer/inner state is updated;
- debugging where the decorator mechanism is correct but ordinary collection/control-flow logic is wrong;
- debugging where state ownership, object identity, ordering, forwarding, or return flow is the real issue;
- implementation from behavioral requirements without naming which decorator mechanism to use.

At least one exercise should involve mutable list/dict object identity across decorator layers.

At least one exercise should involve decoration time and invocation time in the same problem.

At least one exercise should require distinguishing decorator mechanics from ordinary Python collection/control-flow logic.

At least one exercise should involve a class-based decorator or callable object as part of a larger composition, not as an isolated `__call__` exercise.

#### Difficulty Progression

Progress roughly:

1. controlled combination of familiar mechanisms;
2. less explicit composition;
3. state/ownership/order interaction;
4. diagnosis of unfamiliar arrangement;
5. synthesis from observable behavioral requirements.

Do not manufacture difficulty by making specifications enormous or by importing new Python features.

The desired feeling is:

"I have not seen this exact arrangement before, but I know every mechanism involved."

#### Scope

Allowed:

- all mechanisms explicitly listed above;
- two-decorator stacks;
- simple factories;
- closure state;
- wrapper attributes;
- class-based decorators / callable objects;
- `functools.wraps`;
- validation and short-circuiting;
- narrowly specified exception handling;
- routine list/dict/tuple/string operations.

Do NOT use:

- descriptors
- metaclasses
- async
- third-party libraries
- three-or-more-decorator stacks
- caching/memoization
- retries
- complex logging frameworks
- elaborate algorithms
- `time.sleep`
- mechanisms outside the stated scope

#### Debugging Exercises

For every debugging exercise:

- the program must genuinely violate the stated behavioral contract;
- include exactly one intended primary bug unless explicitly asking for multiple bugs;
- do not mark suspicious lines;
- do not identify the bug category;
- do not provide corrected code;
- ensure the test interface matches the actual object returned by the decorator.

Before output, mentally execute:

1. factory creation, if any;
2. decoration;
3. wrapper or callable-object creation;
4. stack construction;
5. invocation;
6. argument flow;
7. state access/mutation;
8. wrapped-function execution or short-circuit;
9. exception flow;
10. return flow.

When mutable lists or dictionaries cross decorator layers, trace OBJECT IDENTITY as well as values.

#### Output

Use identical formatting:

#### Exercise N — Title

**Problem Statement**

For implementation exercises:

**Function Signature**

**Tests**

For reasoning/debugging exercises:

**Code**

**Question**

All Python must be in fenced Python blocks.

Use ordinary ASCII spaces only. No tabs, non-breaking spaces, or Unicode whitespace.

Prefer `assert` tests.

For prediction exercises, include a simple executable `print(...)` reveal at the end so the student can predict first and then run the code.

Do not include:

- difficulty labels
- concept labels
- decorative separators
- Contract sections
- solutions
- hints
- pseudocode
- answer keys
- comments identifying suspicious lines
- expected-output explanations that reveal the reasoning

#### Validation

Mentally solve every exercise before displaying it.

Verify:

- every required mechanism is inside the stated scope;
- each exercise is structurally distinct from the others;
- each exercise combines at least two semantic dimensions;
- later exercises generally combine three or more;
- decorator/factory/callable structure is valid;
- state ownership and lifetime are correct;
- stack order produces the claimed behavior;
- argument and return flow are correct;
- exception behavior is exact;
- mutable object identity is handled correctly;
- collection operations produce the required data shape;
- metadata and attributes belong to the correct returned object;
- tests are runnable and match the real API;
- debugging failures occur for the intended reason;
- the problem has not leaked the reasoning it is supposed to test.

Silently discard and replace any exercise that fails validation.

