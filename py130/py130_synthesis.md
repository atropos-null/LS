# PY130 Synthesis

Kelley Becker | Primary working document | Updated 1 October 2026

This document follows the PY130 learning sequence. Detailed runtime and lesson notes come first, then Modules and Imports, Testing, and Packaging and Distribution. The side quests on Behavior Across Boundaries, Time, and Algorithm Design sit beside the mechanisms and problems they explain. Read the governing questions and synthesis lines as retrieval anchors, then use the detailed explanations and examples for study and later work.

The central model is that Python runtime structures preserve reference paths and state across calls, suspensions, definitions, imports, and repeated execution. Algorithms choose what information must survive a traversal. Tests construct the history needed to check a contract. Packaging carries project code through build, distribution, installation, and later import. `PY130-Synthesis.md` is the primary editable document; `PY130-Synthesis.docx` is its Word copy.

## Detailed Runtime and Lesson Notes

The lesson notes begin with runtime relationships, then follow functions, iteration, generators, files, arguments, closures, decorators, memory, and effects. Side-quest notes appear beside the lesson ideas they clarify.

### First class functions and higher order functions

**Governing question: Who owns the traversal, and who supplies the behavior performed at each step?**

A function object can be assigned to a name, stored in a container, passed as an argument, and returned as a result. That is what first class means here. Writing `square` obtains the callable object; writing `square(5)` asks it to perform a computation. Passing `square` gives another part of the program the ability to call it later. Passing `square(5)` gives that part the result of a call made now.

Keep source code, code object, function object, and execution frame separate. A code object describes compiled computation. A function object associates code with a runtime environment, including globals, defaults, and any closure. An invocation supplies arguments and an execution context. Several function objects can share compiled code while carrying different environments, and repeated calls to one function have separate local execution state unless they deliberately reach shared state.

A higher-order function accepts a function or returns one. Its design value is the separation of a stable process from variable behavior. A traversal can remain fixed while a callback supplies a transformation, predicate, key, or action. The callback's parameter receives the object passed by the higher-order function when it invokes the callback; it does not somehow obtain that argument from the place where the callback was defined.

```python
def select(items, predicate):
    result = []
    for item in items:
        if predicate(item):
            result.append(item)
    return result

unfinished = select(tasks, lambda task: not task.done)
```

Here `select` owns iteration and result construction. The predicate owns the decision about one task. The lambda creates a function; it does not itself perform traversal. A lambda is limited to one expression, whose result becomes its return value. It has the same enclosing-name lookup issues as other functions. Use a named function when the behavior deserves a name, several statements, or its own explanation.

`map(function, iterable)` creates an iterator that transforms inputs as it is consumed. With multiple input iterables, the function receives corresponding values and ordinary `map` stops at the shortest input. `filter(predicate, iterable)` retains items for which the predicate is truthy; `filter(None, iterable)` retains truthy items themselves. Creating these iterators does not eagerly build a list of results. `list(...)`, a loop, or another consumer causes the work to occur.

A comprehension states traversal, transformation, and filtering together. A list comprehension materializes its result; a generator expression defers production. An explicit loop is often clearest when transitions, several pieces of state, or exceptional cases matter. Neither concision nor the label “Pythonic” establishes correctness, and lazy machinery is not automatically faster. Choose according to required lifetime, reuse, input size, early stopping, and readability.

### Side quest: Behavior Across Boundaries

**Governing question: What runtime relationship survives when execution moves into a different context?**

The question underneath much of PY120 was who owns the behavior and how delegation is managed. PY130 shifts the emphasis. Functions become values, execution can stop and resume, closures preserve access after an outer call ends, decorators redirect public names, and modules preserve namespaces. Objects can survive the calls that created them.

The recurring answer is a reference path. **Python runtime structures own storage locations that hold references to Python objects. Execution traverses those reference paths.** A frame, namespace, container, closure cell, module, instance, or generator can participate in that structure. **A reference path is the route by which execution can reach an object through one or more stored references.**

The spreadsheet model remains useful: imagine a namespace as a sheet, a binding or storage slot as a cell, and a reference as a hyperlink to a Python object. This is a conceptual model, not a claim that every runtime structure is a dictionary. Execution creates, follows, replaces, preserves, and releases those links.

For an ordinary Python function call, the caller evaluates argument expressions and the callee receives parameter bindings to the resulting objects. If `person` refers to `"Ada"`, calling `greet(person)` can establish a local parameter `name` that refers to that same string. The object is not copied merely because execution crosses a call boundary. Two storage locations now provide paths to the same object.

A call boundary is the transition into another callable execution context. Caller and callee name the two roles; the important mechanics are the change of execution context and the establishment of parameter bindings.

If caller and callee reach the same list, mutation changes that shared object. Nothing needs to cross back: the caller later follows its existing path and observes the changed state. Rebinding the callee's parameter instead redirects that local binding to another object. It does not redirect the caller's binding. **Mutation changes the object at the end of a path; rebinding changes which object a binding reaches.**

When a call finishes, its local bindings need not remain active for its objects to survive. Other structures may retain references. Frame lifetime, binding lifetime, and object lifetime are distinct. A returned object, a captured cell, or a container reference can preserve what later execution still needs.

### Side quest: Retaining behavior for later

A function is an object. It can be stored, passed, returned, and later called. Passing behavior therefore means making a callable object reachable from another context. The recurring pattern is **reference now, execution later**.

Partial application retains a callable and earlier arguments or configuration for a later call. It preserves references, not an automatic frozen copy of mutable contents. The practical question is: some information arrives now and the rest later; what structure can carry the earlier information until it is needed?

### Side quest: Time and the Temporal Model

**Governing question: What is true now because of something Python did earlier?**

**Present behavior is historical.** A Python result at time t can only be understood by knowing which relevant reference paths and state changes already happened before t. The present computation inherits bindings, mutations, retained objects, and execution state established earlier.

**Source code is spatial; execution is temporal.** Source position is not runtime moment. A definition, retained callable, or generator can appear in one place while the execution it enables occurs much later.

Source expressions compress sequences of runtime events. When a line becomes confusing, expand it into evaluation, lookup, calls, binding, and observation. Short-circuit evaluation can mean that part of an expression never executes. The useful habit is to recover the sequence when it affects the result, rather than treating each written line as one indivisible event.

The graph changes as execution proceeds. The bridge into Time is: **What is true now because of a reference path established earlier?**

### The Todo progression and iterative methods

The Todo work moved from an individual object's state and behavior into a collection that owns references to Todo instances. Adding, locating, marking, and removing items are operations on that collection and its collaborators. A TodoList may delegate an action to the relevant Todo rather than duplicate the Todo's responsibility.

The important shift came with `each` and `select`. In a direct loop, one method owns both traversal and its per-item decision. An `each` method can own traversal and accept the action to perform. `select` can own result construction and accept the predicate. Methods such as `done_todos` and `undone_todos` then supply behavior to that common mechanism.

Follow one item to understand the abstraction: the collection obtains the Todo, `each` passes it to a callback, and the callback's parameter becomes a new local path to that same Todo. If the callback adds it to a result collection, the result normally holds another reference to the existing Todo. Copying a collection of references does not clone its members. The abstraction should make a repeated responsibility reusable; if it obscures a one-off operation, an explicit loop may be the better design.

### Side quest: Identity and accumulated history

Track binding, object identity, and object state separately. A binding can be redirected. An object can retain its identity while its contents change. Several bindings can reach one object, and one of them can later be redirected without changing the others.

Temporal coupling exists when an operation works correctly only because a required event already happened. Initialization, a previous call, or a prior state transition may establish what the present operation assumes. Ask: what had to happen before this could work now?

Repeating source-level code does not necessarily repeat the same runtime situation. A prior call may have changed a cache, exhausted an iterator, advanced a generator, or mutated shared state. Ask what the previous execution left behind. Idempotence concerns whether repeating an operation has the same effect as performing it once; it is a separate question from whether two calls return equal values.

### Side quest: Algorithm Design

**Governing question: What relationship does the contract require me to observe?**

Behavior Across Boundaries identifies the paths. Time reconstructs their history. Algorithm Design deliberately chooses the state and transitions that will produce the required result. Its starting point is the contract: what must be produced, from which inputs, under which assumptions?

**Let the relationship required by the contract determine the traversal shape.**

### State as the core of an algorithm

**State is the part of the past that the future still needs.** Before choosing variables or containers, describe the information that must survive and what it must mean. Temporary input is used for the current step; surviving state carries information into later steps. That information may summarize all processed input, preserve only nearby context, or describe the current phase.

Keep whole history when later work needs it. Keep compressed history when a sufficient summary will do. An average can be derived from a count and total. The longest run length can be tracked without storing every run. Storing the runs can also be valid when the contract requires their contents or later inspection.

### Multiple pieces of state

Each surviving value needs a distinct job. Summary state describes what has been processed; context state supplies information needed to interpret the next input; best-so-far state records the best qualifying result; phase state identifies where the computation is in its process. Updates must keep those meanings consistent with one another.

**Flags are compressed history.** Ask what yes-or-no fact about the past the next step needs. If it needs the full previous value, preserve that value. If it needs only whether the previous word began with a vowel, a flag can be sufficient. A boolean is insufficient when later decisions require a count or nesting depth.

### Invariants

**State is what survives; an invariant is what must remain true about that surviving state.** Name the checkpoint at which the statement applies, such as after each processed item. Initialization must establish the invariant, and each completed transition must preserve it.

“Choose the smaller current value” is a transition rule. “The result is sorted and contains exactly the values consumed so far” is an invariant. The first says what to do; the second states what the surviving state means. At termination, combine the invariant with the stopping condition to explain why the contract is satisfied.

### State ownership

Give state an owner and lifetime that fit the computation. Locals suit one invocation. Instance attributes suit state belonging to an object across operations. Closure cells suit captured state retained by a callable. A generator suits one suspended computation. Module state has wider sharing and should serve a correspondingly shared purpose.

**Do not give state a longer lifetime or a wider mutation surface than the computation needs.** Independent sensors, counters, or generators should not accidentally share the state that defines their separate histories. Identify the responsible instance or computation, not merely the class or function name.

### Python theory of iteration

**Governing question: How can independently written producers and consumers cooperate without knowing each other's internals?**

Iteration is a protocol, not a special ability of collections. An iterable can supply an iterator. An iterator carries the state of a traversal and supplies successive values. A consumer requests values and decides how much to consume. These are roles; one object can fill more than one role. A generator and a normal file object are both iterables and their own iterators.

The language-level sequence is `iter(obj)`, repeated `next(iterator)`, and exhaustion signaled by `StopIteration`. An iterator's `__iter__` returns itself; `__next__` advances it. A container can instead return a fresh iterator each time. Two list iterators can traverse the same list independently because their positions belong to different iterator objects. Two names referring to one generator share one advancing computation.

```python
items = [10, 20, 30]
left = iter(items)
right = iter(items)
assert next(left) == 10
assert next(left) == 20
assert next(right) == 10
```

A `for` loop obtains an iterator and requests values until it is exhausted. Exhaustion is different from a false value: `0`, `False`, `None`, and an empty string can all be valid yielded values. Once an iterator is exhausted it must continue to signal exhaustion. To repeat a traversal, obtain a new iterator from a reusable iterable or create a new generator; a second loop over the same exhausted generator does not restart it.

The CPython view connects object to type to protocol dispatch. The object's `ob_type` identifies its type. Iteration uses the `tp_iter` and `tp_iternext` slots to obtain and advance iterators; an older sequence-protocol fallback also allows iteration through successive indexed access. These C-level details explain implementation, while `iter`, `next`, and exhaustion are the public contract. A type object is itself a Python object. There is no single universal iterator class: many types implement the iterator role.

A custom iterable can return a dedicated iterator containing its position. It can also delegate: `return iter(self._items)` exposes the internal list's iterator through the collection's public protocol. A generator-based `__iter__` can express a more specialized traversal. The design question is where each traversal's independent state belongs, not which construction looks most elaborate.

Consumers differ in how they drive the same protocol. `list`, `tuple`, `set`, `sorted`, `sum`, and string `join` generally consume their finite input fully. `any` and `all` can stop as soon as the result is determined. `zip`, `enumerate`, `map`, and `filter` create iterators that request upstream input as they themselves are advanced. Membership checks, unpacking, comprehensions, `min`, and `max` also participate. `dict` construction needs keys and values in the format its contract expects; accepting an iterable does not mean accepting arbitrary elements.

The consumer therefore determines whether deferred work runs at all, how far it runs, and when an error or side effect becomes observable. Laziness is a chain property: putting `list` or `sorted` in the middle can introduce materialization. Consumers of an infinite iterator must have an independent stopping rule. Protocol-level encapsulation lets a consumer use iteration without knowing how a list, generator, or file produces its next value.

### Traversal shape

Ask what must be available at the same moment. Current-only traversal suits independent decisions about each item. Previous/current traversal carries local history; current/next traversal provides lookahead. Fixed or sliding windows retain a bounded neighborhood. Run tracking and grouping preserve the active unit and recognize where it ends.

Distinct-pair traversal compares each relevant pair once; Cartesian traversal compares all required combinations across collections. Parallel or lockstep traversal advances corresponding inputs together. Merge-style traversal compares current candidates and advances only the side consumed. Independent multi-stream traversal follows each stream's own advancement and exhaustion rules.

Other recurring patterns include index-dependent decisions, searches restarted at each position, whole-history comparisons, compressed-history summaries, and nested-region processing. Modes can overlay a sequential traversal; nesting may require depth or a stack. These are reusable design families, not an exhaustive taxonomy of every algorithm.

The wording of the contract supplies clues, not a mechanical lookup rule. “Immediately before” suggests previous/current; “next” suggests lookahead; “corresponding” suggests lockstep; “combine sorted inputs” suggests merge-style advancement. A traversal must stop at the last position where its required relationship is defined.

### Boundary detection

**A boundary is often defined by a relationship between current input and surviving context, not by current input alone.** A positive number is a property of current input; a change from a non-positive group to a positive group is a relationship. Boundaries may arise from a value change, delimiter, size limit, failed relationship, or end-of-input.

Boundary handling commonly means finalize, store, then reset or reinitialize. Decide separately where the triggering item belongs. A changed value may begin the next group; a delimiter may belong to neither group; an item that fills a fixed-size chunk belongs to that completed chunk. End-of-input may require explicit finalization because no later item arrives to close the active group.

### Modes and state transitions

**Mode is surviving state that determines how later input should be interpreted.** The same input can require a different action in a different mode. A transition table makes the relationship explicit: current mode plus event determines the action and next mode.

A state transition changes some state. A mode transition changes the behavioral phase. Incrementing a count need not change mode. Likewise, detecting a grouping boundary does not automatically mean the system has changed how it interprets future input. Traversal shape describes movement through data; mode describes interpretation while moving.

### Termination and progress

**Stopping condition and progress rule must be designed together.** The stopping condition says when the computation ends. A progress measure explains why it will get there: remaining input decreases, an unsearched region shrinks, or a smaller subproblem replaces the current one.

**Every possible path through a loop body must preserve progress toward termination.** In an index-controlled loop, `continue` can skip the index update and stall on the same item forever. An increasing value alone does not prove termination if it can overshoot an equality target or be repeatedly reset. Progress must connect to a reachable stopping condition.

For a merge, only one input position need advance per comparison. The total unconsumed input still decreases. The comparison phase ends when either input is exhausted; consuming the remaining tail completes the computation.

### Generators as resumable computation

**Governing question: What survives when execution pauses, and who causes it to resume?**

A generator function is a function whose body contains `yield`. Calling it creates a generator object, with arguments bound for that particular execution, but does not run the body through its first yield. Advancing the generator begins the body. Each subsequent advancement resumes the same execution until it yields again, returns, or raises an exception. Calling the generator function again creates a separate generator; calling `next` again does not.

```python
def running_totals(values):
    total = 0
    for value in values:
        total += value
        yield total

g = running_totals([2, 3, 5])
assert next(g) == 2
assert next(g) == 5
assert list(g) == [10]
assert list(g) == []
```

At suspension, the generator retains enough execution state to continue: local bindings, its current place in the computation, relevant evaluation state, and references to objects still needed. It does not run in the background while paused. The consumer drives it. An upstream generator may hold a list or file iterator, so the small size of the generator object alone does not prove that little memory is retained.

Yield transfers one value outward and suspends. It does not copy the value. If a generator repeatedly yields the same mutable list and later clears or mutates it, a consumer that saved those references can see the changes. For independent groups, yield the completed list and rebind the active group to a new list, or deliberately create an appropriate copy.

Return completes a generator. Falling off the body also completes it. A return value becomes the value associated with generator termination, not another yielded element. An ordinary loop consumes values and handles `StopIteration`; it does not expose that completion value. To finish a generator normally, use `return` or reach the end, rather than raising `StopIteration` manually inside the body.

### Generator runtime machinery

The seminar's runtime model separates the compiled code, the generator-function object, each generator object, and the execution state owned by that generator. CPython recognizes generator code during compilation and uses a generator-specific creation and resumption path. Modern CPython can embed interpreter-frame storage within the generator object rather than allocate the entire execution as an independently exposed Python frame object.

The durable distinction is ownership: a `PyGenObject` carries resumable execution. The `_PyInterpreterFrame` is internal execution machinery; a Python-visible frame object is an inspection interface with its own representation. The frame stores execution data; it does not move its own instruction pointer. The interpreter's evaluation loop dispatches instructions, updates execution position and stack state, follows jumps, and handles suspension or completion.

The bytecode names discussed in the seminar included `RETURN_GENERATOR`, `RESUME`, `YIELD_VALUE`, and return instructions. They are useful evidence for a particular CPython version, not a fixed cross-version recipe. The important sequence is creation, first entry, execution, suspension, resumption, and completion. A suspension records where execution can continue; a later `next(g)` reaches that retained state through the iterator machinery. See the [Python bytecode documentation](https://docs.python.org/3/library/dis.html) when checking an exact disassembly.

**The frame is resumed, not recreated.** Two generators made from one function can share the code object while preserving different local values and execution positions. A completed generator cannot be restarted. References to suspended state can prolong the lifetime of objects and resources; that is part of the design cost of keeping unfinished work available.

### Generator control and delegation

`next(g)` resumes with `None`; `g.send(value)` resumes with a supplied value. In `received = yield outgoing`, the outgoing value reaches the consumer when execution suspends. When it later resumes, the yield expression produces the incoming value and assignment to `received` continues. A newly created generator must first be advanced with `next(g)` or `g.send(None)` before it can receive a non-None value.

```python
def exchange():
    incoming = yield "ready"
    yield incoming.upper()

g = exchange()
assert next(g) == "ready"
assert g.send("hello") == "HELLO"
```

`throw` resumes a suspended generator by raising an exception at the suspension point. Its exception handling can catch the error and continue, or the error can propagate outward. `close` requests termination with `GeneratorExit`; entered `finally` blocks can perform cleanup. Yielding another value while responding to closure is an error. Closing a never-started generator does not first execute its body to establish cleanup blocks. The method contracts are documented in [Generator iterator methods](https://docs.python.org/3/reference/expressions.html#generator-iterator-methods).

`yield iterable` yields that object as one value. `yield from iterable` delegates to it and forwards its produced values. For simple production, a loop that yields each element expresses the basic idea. Full delegation also handles the generator communication protocol, and `result = yield from child()` can receive a subgenerator's completion value. When the delegate is itself a generator, the outer and inner computations retain distinct execution state. Delegation is not one giant merged frame.

A generator expression, such as `(word.upper() for word in words if word)`, is compact syntax for lazy production. Its leftmost iterable is evaluated and its iterator acquired at expression creation; filtering and result production occur as it is advanced. Later work can observe changed state. Parentheses do not freeze the source, and generator expressions have the same one-pass consumption behavior as other generator objects.

### Generator applications and the difficult practice problems

Generators fit incremental transformation, filtering, running totals, grouping, and streams where the consumer may stop early. They can avoid constructing an entire result collection, but only if the algorithm and downstream consumers permit it. A generator that first sorts or collects all its input still performs that materialization. If results need random access or repeated independent traversal, a stored collection may be appropriate.

The temperature pipeline separated splitting lines, discarding irrelevant input, extracting a field, converting it, and consuming the results. Each stage received an iterable and produced an iterable. The chain became active only when a final consumer requested output. A parsing error could consequently surface during consumption, after the pipeline objects had already been constructed.

Interleaving two inputs required separate iterator state and an explicit exhaustion policy. If one ends first, the contract must say whether to stop or continue with the other. Advancing two iterators in lockstep without considering independent exhaustion can lose the remainder. This was a traversal-design difficulty expressed through generators.

Grouping consecutive equal items required an active group and a comparison value. A changed value finalizes one group and begins another. End-of-input must flush any non-empty final group because no next value arrives to reveal the boundary. Two yield sites can therefore serve two distinct causes of completion: a detected change and input exhaustion.

Grouping dictionaries by a key introduced another contract distinction: consecutive equal-key runs are different from one global group for every distinct key. A single streaming run tracker solves the first. Unsorted global grouping generally needs retained buckets or another organization strategy. The word “group” alone does not determine which problem is intended.

### Side quest: Suspended work and future computation

A generator preserves unfinished execution. Suspension at `yield` retains execution position and relevant local state so the computation can resume. Calling a generator function creates the generator; advancing it runs or resumes its body. Return completes an execution; yield suspends one.

Creating something now and doing its work now are different events. Eager computation performs work at the relevant evaluation point. Deferred work is scheduled or retained for later execution; lazy computation performs work as results are demanded. A generator, partial, closure, or stored callable can exist now as the means for future computation.

### Worked traces and causal debugging

**Debugging often means finding the first step where the state stops meaning what it was supposed to mean.** Trace from initialization and check the intended meaning after each relevant transition. A final wrong answer is evidence; the first invariant violation points toward its cause.

For a previous/current comparison, assigning `previous = current` before comparing destroys the required relationship. For grouping, replacing the active group before storing it loses the completed group. For a longest-run computation, failing to reconsider the best-so-far value can violate its meaning on the first qualifying item, before any boundary occurs.

Ask whether state changed too early, too late, or not at all; whether a boundary was missed; whether finalization is absent; whether a branch bypasses progress; or whether the traversal never exposed the required relationship. Distinguish a contract error, design error, Python-semantics error, and syntax mistake so the repair addresses the actual cause.

### Synthesis and worked designs

**CONTRACT → RELATIONSHIP → TRAVERSAL SHAPE → STATE → INVARIANT → TRANSITIONS / BOUNDARIES / MODES → TERMINATION → CODE**

This is a diagnostic scaffold. A simple sum does not need an elaborate mode model. A grouping problem does need boundary handling. Choose the categories that make the computation explicit, then choose syntax that implements them.

For the longest strictly increasing consecutive run, the local relationship is whether the current value exceeds the previous one. Preserve `previous`, `current_length`, and `max_length`. After each processed value, current length describes the increasing run ending there and maximum length describes the best run in the processed prefix. Increment the current length when `current > previous`; otherwise reset it to one. Reconsider the maximum, then update previous. Equality breaks a strictly increasing run. Define empty-input behavior in the contract before choosing initialization.

For collecting ordinary elements between `START` and `END`, use a sequential pass with an OUTSIDE or INSIDE mode and a result collection. START enters the collecting mode; END leaves it; ordinary elements are appended only inside. The delimiters are events, not an “END mode.” The invariant connects the mode to the active region and the result to qualifying elements processed so far. Nesting or malformed delimiters require additional contract decisions and possibly richer state.

For merging two sorted lists, the relationship is which current unconsumed value should come next. Preserve two independent positions and the result. The result must stay sorted and contain exactly the consumed values; those values form the next prefix of the merged ordering. Append the smaller candidate and advance its side. On equality, preserve both values unless the contract says otherwise. When either input ends, append the remaining tail. Each consumption reduces total remaining work.

**An algorithm is the controlled movement of state through the traversal shape required by the contract.**

### Files and resource ownership

**Governing question: Which object owns the position and resource, and when does that resource stop being usable?**

A path names a location. `open` returns a Python file object that mediates access to an operating-system resource. A normal text-file stack separates text encoding and decoding, buffering, and raw I/O: `TextIOWrapper`, a buffered layer, and `FileIO` collaborate. Buffering can obtain more bytes than one requested line and retain the rest for later operations. Python-level read size and operating-system read size are different concepts.

The open file object has mutable state even in read-only mode: reading changes its position. `other = file` creates another reference to the same object and position. Two separate normal calls to `open(path)` create distinct Python file objects with independently managed positions. The path being the same does not make them one object.

`read()` consumes the remaining contents; `read(n)` requests up to the specified amount. `readline()` reads one line, normally retaining its newline. `readlines()` materializes the remaining lines as a list. Iteration yields lines from the current position, and `iter(file) is file` for ordinary file objects. Mixing `next(file)` and a loop continues one shared traversal. At end-of-file, text reads return an empty string; iteration signals exhaustion. `seek(0)` on a seekable file returns to the beginning. Text positions should not generally be treated as arbitrary character indexes.

Mode `r` reads an existing file, `w` truncates or creates for writing, `a` appends or creates, and `x` requests exclusive creation. Binary mode uses bytes; text mode uses strings and an encoding. A `+` adds updating capability to the chosen base mode. Specify an encoding when the text format is known. Appending adds exactly what is written; it does not invent a separating newline.

`write(text)` performs the write and returns a character count for a text stream. It does not return the written string. `writelines(strings)` writes those strings without inserting newlines. Flushing moves buffered data onward but should not be mistaken for a universal guarantee of physical disk persistence. Reading, writing, and opening can raise exceptions; `FileNotFoundError` is one example, not the only possible failure.

The context-manager protocol separates access from cleanup. `with open(...) as file` enters the context and arranges exit handling. On leaving an entered block, including by exception, the file context manager closes the stream before control continues outward. The file object can remain bound afterward, but `file.closed` is true and I/O operations cannot continue normally. A context manager can suppress an exception by its exit result; the usual file context manager does not suppress it.

### Connecting files and generators through pipelines

Files and generators compose because they share iteration. A file produces lines, a generator transforms or filters them, another stage interprets the result, and a consumer requests output. Each component can have one responsibility and depend on the next component's public iteration interface rather than its concrete implementation.

```python
def nonempty_lines(lines):
    for line in lines:
        text = line.strip()
        if text:
            yield text

with open("notes.txt", encoding="utf-8") as source:
    for text in nonempty_lines(source):
        print(text)
```

Here consumption occurs while the file context is active. Returning a lazy pipeline from inside a `with` block can leave it referring to a file that has already been closed. If a generator itself owns the `with`, the resource can remain open while that generator is suspended. Stopping iteration early does not mean that all upstream resources have necessarily been closed; ownership and explicit cleanup need to remain clear.

### Arguments and parameters

**Governing question: How are the caller's supplied objects matched to the callee's parameter bindings?**

Arguments belong to a call; parameters belong to a function signature. Positional arguments are matched by position. Keyword arguments are matched by name. A parameter with a default can be omitted, but having a default does not by itself make that parameter keyword-only. Names between `/` and `*` are positional-or-keyword. Names before `/` are positional-only; named parameters after `*` or `*args` are keyword-only. The separators are syntax markers, not parameters receiving objects.

Default expressions are evaluated when the definition executes. A retained mutable default can therefore accumulate changes across later calls. Use a sentinel such as `None` and create a fresh object inside when fresh-per-call state is the contract. `if value is None` distinguishes that sentinel from other false values when the distinction matters.

At definition time, `*args` names a tuple collecting surplus positional arguments; `**kwargs` names a dictionary collecting surplus keyword arguments. These names are conventions. A supplied argument that fills an explicit parameter does not also appear among the extras. With no extras, the corresponding tuple or dictionary is empty. Once inside the body, use ordinary tuple and dictionary operations: indexing, iteration, `.items()`, `.get()`, `.update()`, and so on.

```python
def inspect_call(a, /, b=2, *args, required, option=0, **kwargs):
    return a, b, args, required, option, kwargs

assert inspect_call(1, 3, 4, required=5, extra=6) == (
    1, 3, (4,), 5, 0, {"extra": 6}
)
```

At a call site, `*iterable` expands elements into positional arguments and `**mapping` supplies keyword arguments whose keys must be strings. Passing a dictionary as `f(data)` is one positional argument; `f(**data)` uses its entries for keyword binding. A receiving `**kwargs` dictionary is a new outer dictionary, while contained objects can still be shared. Forwarding `func(*args, **kwargs)` expands the collected values again so the next callable can bind them under its own signature.

Duplicate values for one parameter, missing required arguments, unexpected keywords, and prohibited positional or keyword forms can raise `TypeError`. An invalid signature or an ordinary positional argument written after a keyword argument can instead be a `SyntaxError`. Positional-only names have a subtle consequence: with `def f(name, /, **kwargs)`, a keyword named `name` can be collected in `kwargs` without binding the positional-only parameter.

| Signature form | Binding rule |
|---|---|
| `def f(a, b)` | Both parameters are positional-or-keyword |
| `def f(a, b=2)` | Omitted b uses the retained default |
| `def f(a, /, b)` | a is positional-only; b remains flexible |
| `def f(a, *, b)` | b is required and keyword-only |
| `def f(a, *args, b=2)` | Extra positionals become a tuple; b is keyword-only |
| `def f(a, **kwargs)` | Unmatched keywords become a dictionary |

The five uploaded Arguments and Parameters pages cover positional and keyword calls, defaults, `/`, `*`, variable positional and keyword arguments, and signature ordering. The signature's positional parameters precede `*args`; explicit keyword-only parameters follow it; `**kwargs` is last. Required keyword-only parameters may follow optional ones, so a rule about positional defaults should not be overextended to every parameter category. Built-ins can offer similar public call shapes without literally being implemented with Python `*args` source syntax.

### Iterable unpacking

**Governing question: Is this star expanding values or collecting them, and what destinations must be filled?**

Unpacking consumes an iterable and distributes its elements. `a, b = iterable` requires exactly two elements. Nested targets require the corresponding nested structure. Too few or too many elements produce a `ValueError`; a non-iterable source produces a `TypeError`. Unpacking is not limited to lists and tuples: it can consume generators, which changes their remaining state.

A starred assignment target collects the unmatched elements into a new list. In `first, *middle, last = values`, the fixed targets must still receive values, while `middle` may be empty. There can be one starred target at a given unpacking level. In `*items, = iterable`, the comma makes an unpacking target list, and the starred target collects all the elements. A bare `*items = iterable` is not that valid assignment form.

The star is the Uno Reverse card: call-side `f(*values)` expands one iterable into many arguments; assignment-side `first, *rest = values` collects many remaining elements into one list. In a function definition, `*args` collects extra positional arguments into a tuple. Context determines the operation and the resulting container.

Unpacking also occurs in loop and comprehension targets. `for key, value in records` distributes each record into two local targets; `for key, value in mapping.items()` does the same for key-value pairs. Iterating a dictionary alone yields keys. A dictionary comprehension can overwrite an earlier value when a later record supplies the same key.

The practice problems added two useful contract checks. Path decomposition must distinguish variable directory depth from the filename and its extension; splitting at every period can fail for names containing periods, so the intended final separator matters. Sales aggregation for `(product_id, amount, *discounts)` can use the empty discounts list directly because `sum([])` is zero. Aggregate repeated product IDs rather than replacing earlier totals.

### Closures and the surviving environment

**Governing question: The outer call has finished; what concrete path still reaches the enclosed binding?**

A closure combines a function with access to bindings from an enclosing function scope. Returning the inner function makes the survival visible, but a nested function need not escape to use enclosing bindings. A global lookup is not the same route as a closure cell, and merely nesting a function does not mean it captures every local variable.

```python
def make_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply

times_3 = make_multiplier(3)
times_10 = make_multiplier(10)
assert times_3(4) == 12
assert times_10(4) == 40
```

`factor` is local to the outer function and needed by inner code. It is a cell variable from the outer code's perspective and a free variable from the inner code's perspective. `value` is a local parameter of the inner function. The code object's metadata describes the names and layout the computation requires; the function object's closure supplies cells belonging to a particular execution environment.

In CPython terms, `co_cellvars` identifies captured local names and `co_freevars` identifies the inner code's free-variable names. `function.__closure__` exposes its tuple of cells, or `None` if there are none. Free-variable names correspond positionally to those cells. The metadata strings do not themselves point to the runtime values, and a bytecode operand is not universally identical to an index in `co_freevars` across versions. The executing frame's layout connects the operation to the right cell.

The wire trace is: compiler scope classification, code metadata and access instructions, function construction with this invocation's cells, frame access to those cells, and finally the referenced object. `LOAD_DEREF` illustrates reading through a cell-backed binding; `STORE_DEREF` illustrates rebinding one. `LOAD_FAST` illustrates ordinary local access in relevant CPython versions. Cell creation and function-attachment instructions vary with version, so inspect the actual disassembly rather than memorizing offsets.

### Cells and reference paths

A cell is a real Python object used to support shared access to an enclosing binding. In the CPython model explored in the seminar, a `PyCellObject` has an object header and an `ob_ref` reference to its current contents. The function retains the closure tuple; the tuple retains the cell; the cell retains its contents. The inner function therefore need not retain an eternally active outer frame. The [Cell Objects documentation](https://docs.python.org/3/c-api/cell.html) describes the cell interface.

```text
times_3 → function → closure tuple → cell → 3
```

`cell.cell_contents` is the Python inspection interface for the current contents, not another intervening container. The cell can remain the same while the object it references changes. That indirection is what allows several functions to share a changing binding.

**A closure preserves a route to a binding, not a frozen copy of its value.** Separate outer calls normally create distinct cells for their own captured locals. Functions created within one outer call can share one cell. Two multipliers can therefore share a code object while retaining different factors; a deposit function and a balance reader from one account factory can share one balance binding.

Do not let the `ob_ref` joke flatten the model. `ob_ref` names the cell's contents field in this implementation; it is not a universal field holding every object's value. `ob_type` points to a type, and `ob_refcnt` concerns reference counting. Tuple entries, instance attributes, module bindings, and closure cells can all carry references through different structures. The edges have different meanings and can have different lifetimes.

### Nonlocal and shared state

`nonlocal` directs assignment to an existing binding in an enclosing function scope. Without it, an assignment in the inner function generally makes that name local there; reading it before local assignment can cause `UnboundLocalError`. `nonlocal` is a binding declaration, not permission to mutate an object. `items.append(value)` mutates the reached list without rebinding `items`; `items = new_list` changes the binding. Augmented assignment also performs assignment, even if the underlying object supports in-place mutation.

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

first = make_counter()
second = make_counter()
assert (first(), first(), second()) == (1, 2, 1)
```

Here integers do not mutate. Each increment computes a new integer and redirects the shared cell's contents. The next call follows the same cell and obtains the new value. If a factory returns both a writer and a reader, each can retain that same cell. If the cell holds a mutable collection, both functions can also observe mutations of that collection through their shared route.

### Loop bindings and late lookup

A `for` loop rebinds its target in the surrounding scope; it does not create a new lexical binding for every iteration. If nested functions capture that loop variable, they can all retain the same cell. Invoked after the loop, they read what the cell holds then. The loop did not freeze a separate value for each function. At module scope, analogous late lookup can occur through a global name instead of a closure cell.

```python
def make_readers():
    readers = []
    for x in [10, 20, 30]:
        readers.append(lambda: x)
    return readers

assert [read() for read in make_readers()] == [30, 30, 30]
```

The default-argument solution changes the route. In `lambda x=x: x`, the right-hand `x` is evaluated when the lambda is created and its resulting object is retained as a default. The left-hand `x` is the lambda's own parameter, and the body reads that local parameter on a later call. The default can be overridden by an explicit argument and is still a reference, not a deep snapshot of mutable contents.

Another solution calls a factory once per iteration. Each call creates a separate enclosing binding for its returned function. Adding `lambda` by itself is not a fix; both lambdas and `def` functions can perform late lookup. The diagnostic is which cell or default each function retains, and when the relevant object is obtained.

### Partial application and callable objects

Partial application fixes some arguments now to produce a callable needing fewer arguments later. A closure can do this by capturing configuration. `functools.partial` packages the callable and earlier arguments in a dedicated callable object. Both retain references to supplied objects. The design is the same broad pattern of staged information arrival, while the storage mechanism differs.

A closure and a callable instance can both pair behavior with persistent state. A closure keeps selected state in captured bindings; a callable object usually keeps it in instance attributes and implements `__call__`. Use a closure for a compact configured behavior and an object when multiple operations, visible state, or a richer interface better express the responsibility. Neither choice eliminates the need to decide who owns the state.

Classes are callable because their metaclass provides call behavior, usually constructing and initializing an instance. A particular instance is callable when its type supplies the appropriate call protocol. `callable(obj)` indicates call capability; it does not guarantee that an arbitrary argument list is valid. Special-method dispatch is governed by the type, so assigning an attribute named `__call__` to one ordinary instance is not a general way to install the protocol.

### Closure practice and pipelines of functions

A pipeline of functions has different state from a generator pipeline. A stored tuple or list contains callable objects, and an execution loop applies them to an evolving value. The correct transition is `current_value = func(current_value)`. Repeatedly passing the original input discards the previous stage's result; adding results is a different contract from composition.

In a pipeline builder, the builder retains the collection of functions and a returned runner later traverses it. The loop variable `func` is simply each callable obtained from that collection. Decide whether an already-created runner observes later builder changes or receives a snapshot of the function list. This is the same snapshot-versus-live-path question, now expressed as an interface decision.

### Side quest: Captured paths and live state

A closure preserves access to captured bindings through closure cells after the enclosing call has finished. The whole outer frame does not have to remain active. A closure is a callable retaining access to captured state beyond the active lifetime of the context that established it. The frame is dead; long live the cell. `nonlocal` identifies an enclosing binding when the inner function needs to rebind it.

Persistence has a carrier. A function and its closure cells preserve captured access; a generator preserves suspended execution; a module retains a namespace; a cache retains entries. **Scope determines where a name can be resolved; persistence depends on what runtime structure still carries a reference path.** State includes execution position and retained bindings, not only the contents of mutable objects.

**Establishment and traversal are different moments.** Ask whether Python preserved an earlier result or reference, or preserved a route that will be followed later. A retained reference to a mutable object fixes the referenced identity at that point; it does not freeze the object's contents. A fresh lookup can also reach a different object if an intervening rebinding changed the route.

**A preserved path does not preserve the state at its destination.** Observation reflects what is reached when the relevant lookup, read, call, or resumption happens. The important question is which state existed when this observer followed its path.

For example, a closure that reads `settings["mode"]` later can observe a change made to that dictionary after the closure was created. Preserving access to `settings` did not preserve the old mode value. To reason about the result, identify the retained binding, any intervening mutation or rebinding, and the eventual read.

### Decorators and responsibility

**Governing question: What policy belongs around an operation, and what object receives the public name afterward?**

A decorator lets behavior be registered, modified, or surrounded by reusable policy at definition time. Common responsibilities include validation, logging, access checks, timing, caching, retrying, and result transformation. A decorator need not return a new function and need not wrap at all: it can register an object, attach information, return it unchanged, or return a different callable. Its actual contract determines what happens.

For a wrapper-based decorator, the outer call receives the original callable and returns a wrapper. Later calls to the public name reach that wrapper. The wrapper controls whether, when, how often, and with which arguments the original is called, and which result or exception the caller receives. This is policy around an operation, with extra reference traversal.

```python
from functools import wraps

def count_successes(func):
    count = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        result = func(*args, **kwargs)
        count += 1
        wrapper.successes = count
        return result
    wrapper.successes = count
    return wrapper
```

The original call precedes the count update here because success means returning without raising. An attempt counter would update at a different point. Returning `wrapper` builds the decorated callable; returning `result` inside the wrapper completes one invocation. Confusing those two return levels produces a different object at the public interface.

### Decoration time and call time

Decorator expressions are evaluated when the definition executes. For `@outer` above `@inner`, the function is transformed as `outer(inner(original))`. Later entry into wrapper code starts at the outer wrapper and proceeds inward if each wrapper delegates. Successful return then unwinds outward. An exception can bypass ordinary post-call statements; `finally` is the place for work that must run on either route.

A decorator factory adds configuration before decoration. Its three stages are factory receives configuration, decorator receives function, and wrapper receives runtime call arguments. Recognize a factory by information that must arrive before the function is supplied. The factory returns the decorator; the decorator returns the replacement; the wrapper returns the invocation result. Three moments are hidden behind a small amount of syntax: the children-in-a-trench-coat model has earned its place.

Ordering is a behavioral decision. Logging outside validation can record rejected attempts; logging inside validation may see only accepted calls. Authorization outside a cache prevents the cache from bypassing an authorization check. A wrapper that short-circuits can stop the entire inner chain. Always expand a stack manually before tracing calls or making claims about effects.

### Metadata and state carriers

`functools.wraps` preserves selected descriptive metadata and establishes `__wrapped__` for inspection and unwrapping. It does not make wrapper and original one object, restore every behavior automatically, or eliminate the effects of wrapper order. Inspecting a familiar name is not proof of identity.

State can live in closure cells, wrapper attributes, a shared external registry, a decorator function's attributes, or a callable instance. Put it where its required lifetime and sharing belong. A list made inside the wrapper is normally fresh for each invocation. A list made once during decoration can accumulate per-decorated-function history. A shared registry supplied to a factory can combine information from several decorated functions.

Attaching `wrapper.call_log = log` can expose the same mutable object retained by the closure. Mutating that object through either path is visible through the other. Rebinding an attribute to a new object does not automatically redirect a distinct closure binding. An immutable numeric attribute copied from closure state also does not update itself when the cell is later rebound; it must be refreshed or made the single authoritative state location.

Storing `args` records a tuple of references. Nested mutable objects can change afterward. A shallow copy of a list or dictionary copies the outer container, not all nested contents. Whether a log represents live references or a snapshot must be part of its contract, especially when another decorator mutates inputs before or after logging.

### Callable decorators and decorated classes

A class used as a decorator commonly receives the original callable in its initializer, retains it as an attribute, and implements invocation in `__call__`. The public function name then refers to a callable instance. Persistent counters or call-once state belong on that instance and should be initialized explicitly. Assigning `self.call_count` on a path that runs only after a prior read cannot supply the missing initial value.

Decorating a class is a different operation: the decorator receives a class object and returns the object bound to the class name. Returning the same class after modifications preserves that identity; replacing it with a function or other object changes what the name denotes. Construction behavior, introspection, and type-based assumptions need to match the intended interface.

Functions used as class attributes participate in method binding. An arbitrary callable wrapper object does not automatically reproduce every aspect of that descriptor behavior. Distinguish using a callable object as a decorator from promising transparent behavior in every method context.

### Familiar decorators and design limits

`staticmethod` changes attribute access so that a function is not automatically bound to an instance. `classmethod` binds the class. `property` creates managed attribute access through a descriptor. `dataclass` generates class behavior from declared fields. `lru_cache` reuses results for suitable calls, which raises questions about hashable arguments, retained references, side effects, and freshness. These illustrate different uses of definition-time transformation; they are not all logging-style wrappers.

Framework decorators can register routes, tests, handlers, or commands as definitions execute. Registration may be the central effect even when calling the function looks ordinary afterward. That connects decorators to import-time work and persistent registries.

Use decorators when reusable policy belongs at a call or definition boundary and the resulting interface remains understandable. Prefer explicit composition or an object with methods when several responsibilities and state transitions need to remain visible. Deep stacks, hidden side effects, altered signatures, and implicit control flow can make debugging expensive. The relevant question is what callers are entitled to rely on after decoration.

### Decorator practice findings

Validation must enforce the actual contract. A signature can enforce positional-only or keyword-only binding before the body runs. A wrapper validating types must decide whether it checks only positional arguments or the full signature; pairing values and types with `zip` can silently ignore a length mismatch unless the design handles it.

Raising an error and catching an error are opposite responsibilities. A validation decorator may need to let its error escape. An error-handling factory can retain an exception class and a default result, catch that class, and return the default. A wrapper's second print or count update is skipped if the delegated call raises before reaching it.

Collection operations caused several apparent decorator problems. Recording a call usually means appending to existing history rather than replacing the old list. Accumulating keyword values can mean `update`, whose replacement behavior for repeated keys must fit the contract. Tallying results requires first calling the function and then inspecting its output, not its input tuple. A function name used as a registry key can collide with another function's name; the registry contract decides whether that is acceptable.

Tagging and status tracking combine attributes, stacking, and timing. Determine which object receives the tag, which object the tracking wrapper reads, and whether metadata was available before the read. Remember to call a factory with its configuration: `@tag("pipeline")` supplies a different object from bare `@tag`. The context-enforcement decorator problem was retained for later assessment practice rather than treated as completed study.

### Side quest: Decorator boundaries

A decorator receives the original function and returns an object to which the public function name is bound. Often that object is a wrapper that retains access to the original callable. The path becomes `name → wrapper → original`. Replacement and retained access are separate facts: the public name changes, while the original may remain reachable. Decorator factories distinguish configuration time, decoration time, and later call time.

### Garbage collection and memory ownership

**Governing question: What still keeps this object reachable, and what does reclaiming it actually mean?**

Names and objects are distinct. Python manages object storage; ending the call that created an object does not automatically end the object's lifetime. The seminar's compact orientation was stack for active execution context, heap for dynamically lived objects, with the qualification that interpreter frames and exposed frame objects have implementation-specific storage. The “managed garage” metaphor describes persistence without equating it to a particular allocator layout.

In the ordinary CPython reference-counting model, owned strong references affect `ob_refcnt`. Binding another name, inserting into a container, assigning an attribute, retaining closure contents, and preserving generator locals can acquire references. Deleting or replacing those owners releases references. A reference-count increase is not a copy of the object. `del name` removes that binding; it is not an instruction to destroy the reached object regardless of other owners.

Frames, modules, lists, dictionaries, instances, functions, defaults, cells, generators, and runtime structures can all retain objects. Counting only visible variable names misses much of the graph. Diagnostic counts may include temporary references introduced by the inspection itself, and implementation features such as immortal objects mean the simple classroom counter should not be mistaken for every CPython object's literal behavior.

Reference counting alone cannot reclaim a cycle whose members keep each other's counts above zero. A cycle is a reference path that eventually returns to an object already on that path. A cycle is not automatically garbage: external live state may still reach it. The relevant question is whether the group remains reachable from live program roots.

CPython's cyclic collector uses supported traversal information to reason about references among tracked objects and identify eligible unreachable groups. Container types expose relevant edges through traversal machinery such as `tp_traverse`, and clearing machinery can break references during collection. Weak references do not keep an object alive. Finalization, resurrection, and collector details complicate any simplistic “last name deleted, immediately gone” story.

Object reclamation, allocator reuse, and returning memory to the operating system are different events. Freed object storage may remain available to Python's allocator, so process memory need not drop as soon as an object dies. Garbage collection manages memory; deterministic resource cleanup belongs with constructs such as context managers, not a guessed finalization time.

### Side quest: Reachability and lifetime

Garbage collection is the lifetime version of the reference model. Strong references can keep objects alive, but an unreachable cycle can contain internal references without being reachable from live program state. In CPython, reference counting handles many ordinary cases and cyclic garbage collection addresses eligible unreachable cycles. This implementation model does not establish a portable promise about the exact moment an object will be finalized or memory returned to the operating system.

### Side quest: Guaranteed order and uncertain timing

Use the language contract to place events on the timeline. Useful topics to revisit include expression evaluation and short-circuiting, default-argument evaluation, decorator application, argument binding, generator suspension and resumption, context-manager entry and exit, and exception handling with `finally`. Exact garbage-collection or finalization timing should not be inferred from a name disappearing.

The final model is a runtime reference graph shaped by earlier events. Paths are established; structures survive; state changes; later execution traverses the resulting graph. The master diagnostic is:

**What happened earlier, what survived, what changed in between, and what path is being traversed now?**

### Side effects and pure functions

The course discussion used five broad side-effect categories: nonlocal reassignment, mutation observable outside the call, I/O, exceptions escaping the call, and effects propagated through called functions. Keep that course vocabulary available while distinguishing external reads from external changes. The same higher-order mechanism can behave differently depending on the callback supplied.

A pure function has no side effects and gives the same result for the same inputs. Depending on the clock, randomness, or changing external state breaks that input-only relationship even without mutating a shared object. Keeping calculation separate from interaction usually makes the contract easier to understand and test. A useful return value plus side effects can be legitimate, but it creates multiple observable channels that must be specified.

### Side quest: Observable effects

A side effect is an externally observable interaction or change beyond a function's returned result, such as mutation of shared state or I/O. A pure function's result depends on its inputs and it does not produce externally observable side effects. Reading changing external state can break purity even without mutating it: the current time is not determined by the function's arguments. Dependence on external state and mutation of external state are distinct reasons to inspect a function's behavior.

### Mechanisms in one view

| Mechanism | What happens to the path or state |
|---|---|
| Argument passing | Parameter bindings refer to evaluated argument objects |
| Packing and unpacking | Values are collected or expanded for binding and calls |
| First-class functions | References to callable objects can be retained and passed |
| Partial application | Earlier arguments and configuration remain available for later calls |
| Closures | Captured bindings remain accessible after the enclosing call ends |
| Generators | Execution state survives suspension |
| Decorators | A public binding is redirected; access to earlier behavior may survive |
| Modules | Reference paths extend across namespaces |
| Garbage collection | Strong references and reachability affect object lifetime |
| Side effects | Changes or interactions become observable beyond the local computation |

Ownership needs a precise object. Who owns the binding? Who holds the reference? Where does persistent state live? Who controls the next step? Who else can observe the object? These questions concern different relationships and should not be collapsed into one vague idea of ownership.

**Reference path + time = Python behavior.**

### Retrieval and Practice Anchors

When a feature looks mysterious, ask where execution starts, which edge it follows, what determines that edge, when it stops, and which object or state it reaches. When the result depends on history, add the moment each path was established and the state present when it was traversed.

The recurrent practice needs are recognizing the required relationship under changed wording; keeping context, current, and best-so-far state distinct; preserving information until its last use; placing updates and boundary handling in the right order; choosing sufficient flags or depth; and distinguishing semantics from a container-operation mistake. Practice should move from understanding to mixed transfer, implementation, causal debugging, and eventually timed work.

The important diagnostic distinction is between knowing a language mechanism and designing the algorithm that uses it. Interleaving, grouping, pipelines, decorator registries, and late lookup often combine both. Identify the first wrong assumption or transition before deciding which topic needs more practice.

The study sequence remains central model, explicit rule or contract, worked example, practice, then debugging and synthesis. The conceptual order remains runtime, protocol, design, then tradeoffs. Future assessment work should build on the vocabulary here and distinguish understanding, transfer, implementation, debugging, and performance under time pressure.

## Modules and Imports

**Governing question: Which namespace owns this family of behavior, and which reference path does the importer acquire?**

A module is an object with a namespace. Ordinary imports use the import machinery and `sys.modules` cache; a newly loaded Python module executes top-level code to establish its contents. The module is inserted into the cache before execution completes, which helps explain partially initialized modules during circular imports. Later ordinary imports usually reuse the cached object rather than reset its state.

`import module` preserves the namespace qualifier. `from module import name` creates a direct binding in the importer. Aliases change local spelling, not the imported object. Later imports can overwrite earlier local bindings, and wildcard imports obscure provenance. Mutating a shared module-level object differs from rebinding the module's attribute; a directly imported old object can remain independently reachable.

The `if __name__ == "__main__": main()` guard separates entry-point work from ordinary import. It does not prevent unguarded top-level statements from running during import. Design modules with a coherent responsibility, high cohesion, low coupling, and a small public interface. Leading underscores and `__all__` communicate intent; they do not create hard privacy. Circular dependencies and extensive access to another module's internals can indicate poorly separated responsibilities.

Packages, absolute and relative imports, `__init__.py`, and namespace packages extend this organization and are a bridge to later Packaging work. Keep module-level mutable state deliberate: its broad sharing can produce temporal coupling between callers and tests.

### Side quest: Reference paths across namespaces

With `import module`, the importing namespace gains a path to the module object and its namespace. With `from module import x`, the importing namespace binds its own name directly to the object obtained then. Both paths can initially reach the same object. A later mutation of that shared object may be visible through either path; rebinding `module.x` does not automatically retarget the separately imported name.

## Testing

**Governing question: What observable evidence would show that the contract holds?**

A test creates a controlled runtime world, triggers behavior, observes a result or state, and compares that observation with a contractual expectation. Passing means observed behavior matched the expectation in that particular test world. Failing means actual and expected behavior diverged; the failure alone does not locate the fault. Testing carries the earlier models forward: the contract identifies the relationship, setup creates the needed history, and an assertion observes the state reached after the action.

### Design from the contract

Begin with the contract rather than `unittest` syntax. The design pipeline is **contract → behavior partitions → required state or history → action → required change and invariants → observation → assertion relationship → plausible wrong implementation → code**. At each step, ask what evidence would distinguish the required behavior from a realistic mistake. The contract determines both which behavior deserves a test and which relationship the assertion must express.

Behavior partitions are meaningfully different categories required by the contract. They are not every possible input. Boundary cases matter because they mark where one contractual category becomes another. Depending on the behavior, partitions may include empty and nonempty input, valid and invalid values, true and false predicate outcomes, equality, exhaustion, or the state before and after a transition.

A strong test makes plausible wrong implementations fail. Check more than a convenient output when the contract also constrains structure, state, or unaffected objects. A collection's length may be right while its members or order are wrong. One boolean example cannot establish both branches. Identical fixture values can hide a swapped or misdirected update. Ask: **What plausible wrong implementation still passes this test?** Then strengthen the setup or observation where the contract warrants it.

### Controlled history and SEAT

Launch School's SEAT model is Setup, Execute, Assert, Teardown. In runtime terms, control the relevant past, trigger one behavior, observe its consequence, and clean up external or shared state that could survive into later tests. In `unittest`, `setUp()` creates a fresh test world before each `test_` method. Test methods call the object under test; assertion methods belong to the `TestCase`. A minimal shape is:

```python
import unittest

class TestThing(unittest.TestCase):
    def setUp(self):
        self.thing = Thing()

    def test_behavior(self):
        result = self.thing.do_something()
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
```

Here `Thing` and `expected` stand for the actual class and contractual result supplied by the particular test. The framework shape comes after deciding what state, action, and expected relationship matter.

Stateful behavior needs tests of both change and non-change. For a targeted operation, verify the target's required transition and the relevant invariants of other objects. For a whole-collection operation, verify that every required target changed. Historical behavior needs the prior state that makes the transition meaningful. A test of `mark_undone`, for example, should first make the object done; otherwise a no-op implementation may pass. **State is the part of the past that the future still needs.** Test isolation determines which past may survive from one test to another.

### Assertions and exceptional outcomes

Assertions express relationships. `assertEqual` checks value equality, potentially through a custom `__eq__`; `assertIs` checks whether two references reach the same object. `assertTrue` and `assertFalse` check boolean state, `assertIn` checks membership, and `assertIsNone` checks for `None`. `assertRaises` checks an expected exceptional control-flow path. Choose the narrowest assertion that directly expresses the contract, and keep an `assertRaises` context narrow enough that the intended action clearly caused the exception. Invalid TodoList additions and indexes are examples of contractual exception paths.

Equality and identity must not be interchanged. Two distinct Todo objects may compare equal under their class's equality rule, while `assertIs` requires one exact object. Conversely, identity says nothing by itself about the object's current contents. Select the relationship the caller is entitled to rely on.

### TodoList testing shapes

The TodoList exercises reduce to reusable behavior shapes: observation, partitions, exception paths, targeted mutation, whole-collection mutation, structural mutation, state-to-representation, traversal, and predicate-based selection. For each, establish the necessary initial objects and statuses, perform one action, and observe the relationship that defines the contract. When testing a selection, varied fixture values make an incorrect predicate or traversal visible. When testing a transition, verify the relevant unchanged state as well as the changed target.

### Coverage, failures, and diagnosis

Coverage records where execution traveled. Even 100% measured line coverage establishes only that those lines ran during the tests; it does not prove that boundaries, partitions, assertions, or behavioral relationships were adequate. A test suite can visit every line while allowing a plausible wrong implementation to pass.

A failed test is causal evidence, not a diagnosis. The mismatch may begin in contract interpretation, setup, the chosen action, a state transition, observation, expected value, isolation, or production code. Find the earliest state that became wrong, then inspect the transition that produced it. This applies the temporal model to debugging: reconstruct the relevant past before changing the code.

For an exam or a new problem, ask in order: What is the contract? Which behavior shape is involved—observation, partition, transition, history, exception, or traversal? What state must exist first? What action triggers the behavior? What must change and remain unchanged? What can be observed? Does the relationship require equality, identity, boolean state, membership, or an exception? What obvious wrong implementation still passes? Then write the test.

**Create the past the contract requires, trigger one behavior, observe the relationship that matters, and make wrong behavior difficult to hide.**

## Packaging and Distribution

**Governing question: Which actor owns each step between a source project and code running in another environment?**

Packaging takes code developed in one project and makes it possible to build, distribute, install, and later import that code elsewhere. It is a chain of responsibilities, not one action performed by one tool. The project owns source and configuration. Build tooling turns the project into standard distribution artifacts. A repository stores those artifacts. An installer places them in a particular Python environment. A later Python process imports the installed code and uses it at runtime. Poetry can coordinate several of these stages.

### Repository, installer, environment, and import

PyPI, the Python Package Index, is a public repository for Python distributions. PyPI stores and serves artifacts; `pip` installs distributions into an environment; Python's import machinery makes importable code available inside a running process. **PyPI stores, pip installs, Python imports.** The separate actors matter because success at one stage does not perform the next stage automatically.

Installation changes persistent environment state. A command such as `pip install requests` makes a distribution available to the targeted environment. A later process using that environment may execute `import requests`. That import is a runtime event: it finds and loads code and establishes paths in the current process. **Present behavior is historical** here too: the successful import may depend on an earlier installation. `pip list`, `pip install`, and `pip uninstall` concern packages installed in the environment addressed by that `pip` invocation.

Installed packages belong to a particular environment. A package present in virtual environment A need not be present in virtual environment B. When an import fails after an apparent installation, ask which Python interpreter runs the program and which environment the installer changed. “I installed it” leaves out the ownership fact that matters. The environment determines what is available to that Python setup.

A package may contain modules and subpackages. Its importable structure creates paths such as a top-level package, a nested package, and a module within it. The project directory can contain much more than that importable tree. Tests, documentation, licensing, configuration, and build material are part of the development project, while the package source is the code intended for installation and import.

### Describing and building a project

Launch School's example uses a `src/` layout for importable package code, alongside files such as `README.md`, `LICENSE`, tests, and `pyproject.toml`. The layout makes the boundary between the development project and its importable package visible. It is a useful arrangement, not a rule that every Python project must use `src/`.

The `pyproject.toml` file records machine-readable project facts used by packaging tools. Depending on the project's configuration, these include its name, version, Python requirement, dependencies, and build setup. The purpose is to declare the information required by the packaging workflow rather than rely on assumptions about a developer's machine. A dependency merely installed locally is different from a dependency declared by the project for other environments to reproduce.

Building transforms the development form of the project into standard distribution artifacts. The lesson presents a source distribution, often a `.tar.gz` archive, and a wheel, a `.whl` file. The source tree is arranged for development; the artifacts are arranged for distribution and installation. At this level, the useful contract is **source project in, distribution artifacts out**. Wheel internals, platform tags, and binary compatibility are beyond the central model needed here.

Publishing uploads built artifacts to a repository. The lesson uses TestPyPI to practice that flow before publishing to PyPI. The author-side path is **source project → declared metadata → build → source distribution and wheel → repository**. The consumer-side path is **repository → installer → local environment → later import → runtime use**. Building and publishing change what another environment can obtain; installing changes what a specific environment contains; importing changes what a running process has loaded and bound.

### Poetry and reproducible project state

Poetry is a higher-level tool that coordinates project setup, dependencies, managed environments, building, and publishing. It works within the same packaging ecosystem rather than creating a separate kind of Python import. The lesson uses Poetry to initialize or manage a project, add dependencies, run code in its environment, build distributions, and publish them.

Dependency management connects a project declaration to an environment. “This package happens to be installed here” is different from “this project declares that it needs the package.” Recording the dependency gives another environment the information needed to reproduce the project's requirements. A command such as `poetry run ...` runs in the environment Poetry manages for that project, making the environment boundary explicit.

**Project describes → build packages → PyPI stores → pip installs → environment owns → Python imports → runtime uses.**
