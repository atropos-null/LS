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