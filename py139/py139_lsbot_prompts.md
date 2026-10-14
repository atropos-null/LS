# PY139 AI Prompts

## # PY139 Assessment Practice — Purity, Side Effects, and Nested Mutable Collections

Generate a focused set of PY139-style exercises about purity and side effects involving nested mutable collections.

## Student Position

The student understands:
- pure functions and side effects;
- mutation versus rebinding;
- object identity and aliasing;
- lists and dictionaries;
- shallow copying with slicing, `list()`, and `.copy()`.

The goal is assessment-level transfer: the relevant mechanism should be derivable from the code and behavioral contract without being explicitly announced in each exercise.

Do not introduce advanced libraries or unrelated algorithms.

## Skill Target

The student should need to reason about the object graph rather than merely whether the outer collection is new.

Exercises should require some combination of:

- identifying which objects are newly created and which are shared;
- tracing aliases between the input and returned structure;
- locating exactly where mutation occurs;
- explaining why a function has a side effect and is therefore impure;
- determining whether a shallow copy is sufficient;
- deciding which level or levels of a nested structure need copying;
- refactoring a function so it returns transformed data without mutating any object reachable from the original argument.

## Required Structural Coverage

Include genuinely different structures covering all of these cases:

1. A function builds a new outer list but reuses dictionaries from the input, then mutates those dictionaries.

2. A list contains dictionaries whose values are immutable objects. Copying each dictionary with `.copy()` is sufficient to prevent mutation of the original object graph.

3. A list contains dictionaries that themselves contain mutable lists or dictionaries. Copying only the outer list and nested dictionary is NOT sufficient because a deeper mutable object remains shared.

4. The student must determine the minimum level of copying required rather than being told to use a particular copying technique.

5. A transformation should return new data while preserving the complete original input object graph unchanged.

6. Include at least one case where mutation occurs through an alias whose relationship to the original argument is not immediately obvious from the line performing the mutation.

7. Include at least one case where some nested objects may safely remain shared because they are immutable, while a particular mutable descendant must be copied.

Do not make every exercise use the same shape or the same mutation operation.

Use lists containing dictionaries and closely related nested structures such as:
- dictionaries containing lists;
- dictionaries containing dictionaries;
- lists containing dictionaries containing lists.

## Assessment Style

Do not identify the relevant concept in the exercise title.

Do not tell the student:
- which object is shared;
- where the side effect occurs;
- whether a shallow copy is sufficient;
- which level needs copying;
- which exact copying operation to use.

The student must derive those conclusions.

Difficulty should come from aliasing, nested mutability, ownership, and object-graph reasoning — not obscure syntax or difficult algorithms.

Ordinary list and dictionary operations may be used as supporting machinery.

## Exercise Types

Mix these task types:

- predict/explain whether the original argument changes;
- identify the shared objects and mutation path;
- explain whether the function is pure or impure and why;
- determine whether a proposed copying strategy is sufficient;
- refactor working code into a pure transformation;
- implement a pure function from a behavioral contract.

Do NOT generate deliberately broken code.

Any supplied implementation should run correctly as written. The challenge is understanding its semantics or refactoring its behavior, not debugging accidental errors.

## Exercise Count

Let meaningful structural coverage determine the count. Aim for approximately 6–8 exercises.

Do not add structurally redundant exercises merely to reach a number.

## Output Format

For each exercise use:

### Exercise N — Neutral Title
**Problem Statement**
**Code** or **Function Signature**
**Task**

For reasoning exercises, provide complete runnable code.

For implementation exercises, provide a complete behavioral contract, function signature, and ready-to-run `assert` tests.

Do not provide solutions, hints, pseudocode, explanations, or comments that reveal the relevant aliasing or copying relationships.

## Validation

Before displaying each exercise, mentally trace the complete object graph.

Verify that:
- every claimed alias actually exists;
- every claimed mutation reaches the object described;
- a supposedly pure implementation leaves every object reachable from the original argument unchanged;
- a supposedly insufficient shallow copy genuinely leaves a mutable descendant shared;
- when `.copy()` is intended to be sufficient, no deeper mutable descendant makes that claim false;
- the required refactor can be completed using concepts within PY139 scope and ordinary earlier Python;
- no accidental runtime error masks the intended reasoning problem.

Silently discard and replace any exercise that fails validation.

## # PY139 Final Assessment Prep — Verbalization and Conceptual Precision

Generate 12 interview-style PY139 practice prompts focused on verbal retrieval and conceptual precision.

## Student Position

The student’s implementation/coding is generally strong.

The clearest current weakness is verbal retrieval and explanation: when asked to define or casually explain a concept without code in front of them, they are slower and less precise than when solving code.

The goal of this set is therefore NOT formal textbook definitions.

The goal is to practice giving brief, causal, accurate explanations in ordinary language, similar to a Launch School interview.

## Answer Style to Train

Each answer should be suitable for roughly 20–40 seconds spoken aloud.

The preferred structure is:

**rule → relevant object/binding/state → what happens → why**

Do not require memorized wording if the explanation is accurate.

Prefer questions that invite causal explanation such as:

- What survives?
- What changes?
- Where does that state live?
- What is being retained?
- Why is this considered a side effect?
- What does the name reference afterward?
- When does this happen?

## Required Coverage

Across the 12 prompts, cover all of the following:

- closures
- partial function application
- first-class functions vs higher-order functions
- pure functions
- side effects
- the five course side-effect categories:
  - I/O Operations
  - Global State Modification
  - Object Mutation
  - System Interaction
  - Exception Handling
- shallow copy vs deep copy
- aliasing
- nested mutability
- `nonlocal`
- decorators
- decoration order

Closures and partial function application should each receive direct standalone attention.

Do not treat PFA mainly as a decorator topic.

## Question Design

Generate conversational interview questions, not flashcard prompts.

Avoid prompts like:

“Define closure.”

Prefer prompts like:

“Casually explain what a closure is and what survives after the outer function has finished executing.”

or:

“Why can a function return a new list and still be impure?”

Questions should require explanation, not merely naming a term.

Some prompts may include a very short code fragment if that genuinely improves the conceptual question, but most should be answerable without code.

Do not turn this into a coding exercise set.

## Difficulty and Precision

Start with direct explanation and gradually move toward distinctions that are easy to blur, such as:

- closure retaining access to a binding vs preserving a frozen value
- first-class vs higher-order
- pure return value vs absence of side effects
- shallow copy vs independent nested object graph
- rebinding with `nonlocal` vs mutating an object
- decoration time vs later call time

The difficulty should come from conceptual precision, not obscure terminology.

## Follow-up Design

For each prompt, include at most ONE short follow-up question that could be asked if the initial answer is vague or incomplete.

Examples:

- “What exactly survives?”
- “Where does that state live?”
- “Is the value copied, or is access through a binding retained?”
- “Why is that a side effect?”
- “What does the decorated name refer to afterward?”
- “Which event happens at decoration time, and which happens later?”

Do not include the answer to the follow-up.

## Output Format

Use:

### Prompt N — Neutral Title
**Question**
**Possible Follow-up**

Do not provide:
- answers
- model responses
- definitions
- hints
- grading notes
- difficulty labels
- explanations of what concept is being tested beyond what is naturally necessary in the question

The titles should not reveal the answer.

## Quality Check

Before output, verify that:

- all required topics are represented;
- PFA and closures each appear as standalone concepts;
- the prompts train ordinary-language explanation rather than dictionary definitions;
- the questions are meaningfully distinct;
- the set does not over-focus on decorators;
- shallow copy, deep copy, aliasing, and nested mutability are treated as distinct but related ideas;
- the five side-effect categories are explicitly represented;
- no prompt requires unnecessary coding to answer well.

## # PY139 Final Assessment Prep — Partial Function Application and Closures

Generate 6 PY139-style practice problems focused on partial function application and closures.

## Student Position

The student’s general implementation ability is strong.

The clearest remaining coding weakness is partial function application.

Closures should also receive direct standalone practice because they are an important assessment topic in their own right.

Do not treat either topic mainly as a decorator subtopic.

## Central PFA Contract

Use this as the governing model:

**creation stores the callable and fixed arguments → later invocation supplies the remaining arguments and initiates the call**

Problems should require the student to track:

- which callable is stored;
- which positional or keyword arguments are fixed in advance;
- which arguments are still missing;
- how later arguments bind;
- when the underlying callable actually executes;
- what the resulting callable returns.

## Closure Model

For closures, emphasize:

- what enclosing bindings or state remain accessible;
- what survives after the outer call ends;
- when late binding matters;
- the difference between retaining access to a binding and capturing a value through an ordinary parameter/default argument;
- independent closure state created by separate outer-function calls.

Do not unnecessarily combine closures with decorators.

## Required Coverage

Across the 6 problems, include:

1. Simple `functools.partial` with one positional argument fixed in advance.

2. Partial application with multiple arguments fixed, including at least one keyword argument.

3. PFA interacting with positional and keyword binding.

4. Predicting the behavior of a resulting partial callable across more than one invocation.

5. A standalone closure problem involving retained state and what survives after the outer function returns.

6. One mixed-transfer problem combining PFA or closure behavior with ordinary Python operations without making the problem obscure.

The set should give PFA slightly more weight than closures.

## Difficulty Progression

Use:

**understanding → binding analysis → repeated invocation → mixed transfer → implementation/explanation**

Keep syntax ordinary.

Difficulty should come from:

- argument binding;
- timing;
- retained state;
- what is already fixed versus supplied later;
- what survives;
- which callable eventually executes.

Do not introduce unrelated algorithms or advanced libraries.

## Problem Types

Mix:

- prediction/tracing;
- short explanation;
- small implementation;
- mixed application.

At least one problem should require the student to implement or configure a partial callable.

At least one problem should require the student to explain a closure’s retained state in ordinary language after tracing the code.

## Assessment Style

Do not announce the exact mechanism in every problem title.

Do not provide hints such as:

- “this is testing late binding”
- “notice the keyword override”
- “the closure retains X”

The student should derive the relevant relationship from the code and task.

Any supplied code must be intended to work correctly as written.

Do not generate deliberately broken code or debugging exercises.

## Pre-Answer Pacing

For the harder problems, include this brief check before the task:

**Before answering, check:**
- What is requested?
- Which arguments are already bound?
- Which arguments arrive later?
- What state or binding survives?
- When does execution actually occur?
- What object/value is returned?

## Output Format

For each problem use:

### Problem N — Neutral Title
**Problem Statement**
**Code** or **Function Signature**
**Task**

For implementation problems, include ready-to-run `assert` tests.

Do not provide solutions, hints, pseudocode, or difficulty labels.

## Validation

Before displaying each problem, verify that:

- the argument binding is valid;
- stored positional and keyword arguments behave as claimed;
- later keyword arguments override stored partial keywords only where Python permits;
- the underlying callable executes only when the partial is invoked;
- closure state and binding behavior are internally consistent;
- no accidental `TypeError`, binding conflict, or unrelated runtime error masks the intended reasoning task.

Silently discard and replace any problem that fails validation.

## # PY139 Final Assessment Prep — Purity, Copying, and Nested Mutability

Generate 4 PY139-style assessment-prep problems focused on purity, side effects, aliasing, and copying nested mutable collections.

## Student Position

The student already understands the basic definitions of:

- pure functions and side effects;
- mutation versus rebinding;
- aliasing;
- shallow copying;
- nested mutable collections.

The student has already practiced basic examples where a new outer list still contains shared dictionaries.

Do not spend the set reteaching those basics.

The goal is assessment-level transfer: accurately track an object graph, determine where sharing remains, identify whether mutation escapes into the caller's data, and make the minimum structural changes needed to preserve purity.

## Governing Invariant

Use this as the central rule:

**The original object graph must remain unchanged unless mutation is explicitly part of the contract.**

The key reasoning questions are:

- Which objects are new?
- Which references still reach shared objects?
- Which shared objects are mutable?
- Where does mutation occur?
- Can that mutation reach the original object graph?
- Which reference path must be severed to prevent the side effect?

## Required Coverage

Across the 4 problems, include all of the following:

1. **New outer collection, shared nested objects**

   The returned outer structure is new, but some nested mutable objects are still shared with the input.

   Require the student to trace the relevant aliases and determine whether the function is pure.

2. **When `.copy()` is sufficient**

   Use a structure such as a list of dictionaries where copying each dictionary is sufficient because the values that remain shared are immutable.

   Require the student to explain WHY shallow copying is sufficient rather than merely observing that it works.

3. **When shallow copying is insufficient**

   Use a dictionary or list containing another mutable descendant, such as:

   - dictionary containing a list;
   - dictionary containing another dictionary;
   - list containing dictionaries containing lists.

   A shallow copy should leave a deeper mutable object shared.

   Require the student to identify the exact surviving reference path.

4. **Selective-copy implementation**

   Give a behavioral contract requiring a pure transformation.

   The student must determine which levels of the object graph need to become independent and which objects may safely remain shared.

   Do not tell the student exactly what to copy.

   Require the function to return transformed data without mutating the input.

## Shallow Copy vs Deep Copy

At least one problem must require the student to explain the difference between shallow and deep copying in the context of the actual object graph.

Do not make `copy.deepcopy()` the automatic solution.

The important skill is deciding what must become independent.

Where appropriate, a selective shallow-copy strategy should be preferable to copying the entire graph.

## Purity and Side Effects

Problems should require reasoning about whether a function is pure based on what happens to externally reachable state.

A function is not automatically pure merely because:

- it returns a new outer container;
- it creates some new nested containers;
- the mutation occurs through an alias with a different local variable name.

Include at least one problem where the mutation line does not directly mention the original argument, so the student must trace an indirect alias.

## Problem Types

Use a mixture of:

- code tracing and explanation;
- determining whether a function is pure;
- identifying shared versus independent objects;
- deciding whether a copying strategy is sufficient;
- one implementation/refactoring problem.

Do not generate deliberately broken code.

All supplied implementations must be intended to run correctly as written.

## Assessment Style

Do not identify the answer in the problem title.

Do not tell the student:

- which object is shared;
- where the side effect occurs;
- whether `.copy()` is sufficient;
- which level needs copying;
- whether the function is pure.

The student must derive those conclusions.

Difficulty should come from object ownership, aliasing, mutability, and reference paths—not obscure syntax or difficult algorithms.

Use ordinary lists, dictionaries, strings, numbers, and booleans.

## Pre-Answer Pacing

For the more complex problems, include:

**Before answering, check:**
- What is requested?
- Which containers are new?
- Which references are shared?
- Which shared objects are mutable?
- Which object actually changes?
- Can that mutation reach the original input?

## Output Format

For each problem use:

### Problem N — Neutral Title
**Problem Statement**
**Code** or **Function Signature**
**Task**

For the implementation problem, include ready-to-run `assert` tests.

Do not provide solutions, hints, pseudocode, difficulty labels, or comments that reveal the relevant aliasing relationship.

## Validation

Before displaying each problem, mentally trace the complete object graph and verify that:

- every claimed object relationship actually exists;
- every shallow copy behaves as Python shallow copying actually behaves;
- any intended shared mutable descendant is genuinely shared;
- when `.copy()` is sufficient, no deeper mutable descendant makes it insufficient;
- supplied code has no accidental runtime error;
- the original object graph changes only when the semantics actually imply that it does;
- the implementation problem can be solved by selectively copying the necessary parts of the graph.

Silently discard and replace any problem that fails validation.

## # PY139 Final Assessment Prep — Decorators

Generate 4 PY139-style assessment-prep problems focused on decorators.

## Student Position

The student already understands basic decorator syntax and has practiced decorators extensively.

The goal is not to relearn decorators from scratch.

The goal is to refresh the runtime relationships involved in:

- function decorators;
- decoration time versus call time;
- return propagation through wrappers;
- classes used as decorators;
- persistent state in class-based decorators.

Keep decorator syntax straightforward.

Do not overcomplicate the set with elaborate decorator factories, many stacked layers, or obscure wrapper signatures unless directly necessary.

## Central Runtime Model

For an ordinary function decorator, use this model:

**function object is created → decorator is called at decoration time → decorator returns an object → the decorated name is rebound to that returned object → later calls use whatever object the name now references**

For a class used as a decorator, use this model:

**function object is created → decorator class is called → class instance is created → original function is stored by that instance → decorated name now refers to the instance → later call invokes the instance’s `__call__`**

## Required Coverage

Across the 4 problems, include all of the following:

1. **Basic function decorator runtime trace**

   Require the student to explain:

   - what object is passed to the decorator;
   - when the decorator runs;
   - what object it returns;
   - what the decorated name references afterward;
   - what happens on a later call.

2. **Decoration order and call-time return propagation**

   Use a small stacked-decorator example.

   Require the student to distinguish:

   - decoration-time order;
   - later call-time wrapper order;
   - how the return value moves back outward through the wrappers.

   Keep the decorators simple.

3. **Class used as a decorator**

   Require the student to trace:

   **decoration time → class instance creation → where the original function is stored → what the decorated name now references → later call → `__call__`**

   This should be a direct refresher, not a trick problem.

4. **Stateful class decorator**

   Use a class-based decorator that stores persistent state such as:

   - call count;
   - history;
   - simple configuration.

   Require the student to identify:

   - where the persistent state lives;
   - why it survives across calls;
   - where the original function is stored;
   - what object the decorated name references.

## Difficulty

Use:

**runtime understanding → order/return propagation → class-based decorator → stateful class-based decorator**

The difficulty should come from tracking references, rebinding, execution order, and persistent state.

Do not make the difficulty come from:

- complicated `*args/**kwargs` gymnastics;
- deeply nested decorator factories;
- obscure syntax;
- intentionally broken code;
- unrelated algorithms.

## Problem Types

Mix:

- prediction/tracing;
- short causal explanation;
- one small implementation or completion task if useful.

At least one problem should require predicting a returned value through more than one decorator layer.

At least one problem must use a class as a decorator.

## Assessment Style

Do not explain the answer in comments or titles.

Do not say things like:

- “remember that decoration happens bottom-up”
- “the decorated name now refers to the instance”
- “the count lives on the decorator object”

Those are conclusions the student should produce.

Any supplied code must be intended to work correctly as written.

Do not generate deliberately broken code or debugging exercises.

## Pre-Answer Pacing

For the more complex problems, include:

**Before answering, check:**
- What object exists at decoration time?
- What object is passed to what?
- What object is returned?
- What does the decorated name reference afterward?
- What executes later when the decorated name is called?
- What value comes back outward?
- What state survives between calls?

## Output Format

For each problem use:

### Problem N — Neutral Title
**Problem Statement**
**Code** or **Function Signature**
**Task**

Do not provide solutions, hints, pseudocode, difficulty labels, or explanatory comments that reveal the runtime relationships.

## Validation

Before displaying each problem, verify that:

- all decorator calls occur in the correct order;
- the decorated name references the correct returned object;
- wrapper return values propagate correctly;
- class-based decorators instantiate correctly;
- `__call__` is invoked only when the decorated instance is later called;
- persistent state lives on the intended object;
- no accidental binding or runtime error masks the intended reasoning problem.

Silently discard and replace any problem that fails validation.

## # PY139 Final Assessment Prep — Mixed Assessment Transfer

Generate 6 PY139-style mixed-transfer problems.

## Student Position

The student has completed the PY130 curriculum and a 104-problem assessment bank.

Implementation is generally strong.

The main remaining goals are:

- maintain conceptual precision under mixed conditions;
- track state, references, binding, and execution timing;
- avoid small contract/detail errors caused by moving too quickly;
- practice unfamiliar arrangements of familiar PY139 mechanisms.

Do not generate isolated beginner exercises for topics the student already knows.

## Scope

Use only PY139 material and ordinary earlier-course Python.

Relevant PY139 mechanisms include:

- partial function application;
- closures;
- first-class and higher-order functions;
- argument and parameter binding;
- decorators;
- pure functions and side effects;
- shallow copying and aliasing;
- generators;
- file handling;
- testing concepts where natural;
- modules where natural.

Do not introduce unrelated advanced libraries, obscure language features, or difficult algorithms.

## Difficulty Model

Make the problems meaningfully difficult, but NOT obscure or trick-based.

Difficulty should come from interactions such as:

- PFA + argument binding;
- closure state + mutation;
- copying + purity/aliasing;
- higher-order functions + side effects;
- decorators + return propagation;
- files + iterator/resource lifetime.

Use ordinary syntax.

The student should encounter:

**unfamiliar arrangements of familiar mechanisms**

rather than unfamiliar mechanisms.

## Required Coverage

Across the 6 problems, include all of these combinations:

1. PFA + argument binding
2. Closure state + mutation or rebinding
3. Copying + purity/aliasing
4. Higher-order functions + side effects
5. Decorators + return propagation
6. Files + iterator/resource lifetime

Do not label the problems with those combinations.

## Core Reasoning Questions

Problems should force the student to track:

- who owns the relevant state;
- which references are shared;
- when values or bindings are established;
- which arguments are already bound;
- which arguments arrive later;
- what survives after a call returns or execution suspends;
- what object is returned;
- what is printed versus returned;
- when execution stops;
- whether a resource is still alive.

## Problem Types

Mix:

- tracing/prediction;
- implementation;
- short explanation;
- contract-driven reasoning.

At least two problems should require writing code.

At least two should require tracing working code and explaining the result.

At least one should involve a file or generator lifetime question.

Do not generate intentionally broken code.

Do not ask “find the bug.”

All supplied code must be intended to work correctly as written.

## Pre-Answer Pacing Protocol

Before each problem, include this exact checklist:

**Before answering, check:**
- What is requested?
- What is returned versus printed?
- Which object or binding changes?
- Which arguments bind where?
- What state survives?
- When does execution stop?

## Post-Solution Rule

After each problem, include:

**State the governing rule aloud in one or two sentences.**

The student should explain the underlying mechanism in ordinary language after solving.

## Assessment Style

Do not identify the mechanism being tested in the title.

Do not provide hints such as:

- “this is a closure problem”
- “remember shallow copy”
- “notice that this is a partial”
- “the file remains open here”

The student must identify the relevant mechanism.

Do not make story/theme complexity part of the difficulty.

Use neutral, ordinary programming contexts.

## Output Format

For each problem use:

### Problem N — Neutral Title
**Problem Statement**
**Code** or **Function Signature**
**Task**

For implementation problems, include complete ready-to-run `assert` tests.

Do not provide:
- solutions;
- hints;
- pseudocode;
- mechanism labels;
- difficulty labels;
- explanatory comments that reveal the intended reasoning.

## Validation

Before displaying each problem, mentally execute the code and verify that:

- all argument binding is valid;
- all aliases and shared references actually exist;
- all mutations occur where intended;
- return and print behavior are accurate;
- decorator call and return order is correct;
- closure state behaves as claimed;
- generator suspension/resumption behavior is correct;
- file/resource lifetime is internally consistent;
- no accidental runtime error masks the intended reasoning;
- every required mechanism remains within PY139 scope and ordinary earlier Python.

Silently discard and replace any problem that fails validation.
