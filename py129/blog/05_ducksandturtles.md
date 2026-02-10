# On Ducks and Turtles

> My opponent's reasoning reminds me of the heathen, who, being asked on what the world stood, replied, "On a tortoise." But on what does the tortoise stand? "On another tortoise." With Mr. Barker, too, there are tortoises all the way down. (Vehement and vociferous applause.). — "Second Evening: Remarks of Rev. Dr. Berg"


Duck typing was introduced to me as a way to model Object Oriented design, and it was contrasted with Inheritance Design principles and Interface inheritance design principles. But as I started to struggle with the design principles itself I started asking more questions about how Python itself is structured. And what I learned is that Duck Typing is the operating principle under the hood.

Duck typing is not merely an OOP style choice in Python. **It is the operational principle of the interpreter itself**. Python’s interpreter uses duck typing to decide what to do at runtime. Like literally, duck typing is how Python executes code!

The following is a semantic model of Python, not a literal transcription of CPython’s implementation. Python implementations may optimize, inline, or shortcut internally, but they must behave as if the interpreter follows these rules. This model describes what the language guarantees and what programmers are entitled to rely on.

The interpreter does not consider declared types, class hierarchies, interfaces, and advance guarantees like in other languages. It asks instead:

1. Does this object respond to this operation right now?
2. If I try this method lookup, does it succeed?
3. If not, what is the next fallback?

Duck typing is the execution strategy. In EVERY case this happens, when Python sees:

`a + b` it asks, “Can I call a.__add__(b)? If not, can I call b.__radd__(a)?”

`a += b` it asks, “Can I call a.__iadd__(b)? If not, can I fall back to a + b?”

`print(x)` it asks, “Can I call x.__str__()?”

`len(x)` it asks, “Can I call x.__len__()?”

In every case the interpreter tries behavior, success continues execution, failure raises a concrete error. 


Duck typing is not a pattern one opts into, its the default logic of the runtime. OOP in Python is primarily a human-facing organizational tool for grouping and reusing behaviors.  Classes are not the point. Inheritance is not the point. Objects are very much the point, however, because it is the unit of meaning that leads to behavioral availability at the moment of use. Objects are meaningful only through the behaviors they expose and the contexts that invoke them.

What do you mean classes and inheritance are not the point?? Classes and inheritance are not the source of meaning in Python, but they are the primary mechanisms for organizing and reusing behavior. They exist to make the exposure of methods predictable and legible to humans; **the interpreter itself only cares about whether attributes are present when asked.**

Python is objects all the way down. But — and this is the subtlety —  meaning emerges only when objects are asked to act.

There is no Python beneath objects. There is only objects asking or answering or refusing when it cannot answer. The interpreter is always the one doing the asking, even when the question is expressed through syntax, a builtin, or another object. **Objects never spontaneously act. They only respond.**

And importantly, Objects do not “negotiate” with each other. They do not inspect each other’s types, negotiate protocols, decide what operations mean globally, or introspect and adapt socially. They just reveal their attributes (methods) and execute code when called.  The logic of when those attributes are looked up is entirely the interpreter’s job. 

And when there is a failure is not a side effect, but how Python communicates absence of capability. Errors are part of the voice, not accidents.

The interpreter defines the questions. Objects define the answers. So who is in control? The interpreter. And then, the interpreter uses dispatch by mapping syntax and operations to method lookups on objects, following a fixed, ordered set of rules.

Dispatch in Python is runtime method selection, not message passing in the OO-theory sense, and not type-based overloading.
In Python, dispatch means "given an operation and some objects, decide which function (method) to call, and then call it."

The first step in dispatch comes from identifying the operation context. This comes from syntax (`+`, `for`, `==`, `[]`, `()`), keywords (`in`, `is`), builtins (`len`, `str`, `iter`), all to answer "What question am I asking?

The second step is to translate that context into method names. Each context maps to specific dunder names. For example:

`a + b` → `__add__`, `__radd__`  

`a += b` → `__iadd__`, fallback to `__add__`  

`for x in y` → `__iter__`, `__next__`  

`a == b` → `__eq__`  

`len(a)` → `__len__`  

`a[b]` → `__getitem__`  

This is the dispatch table at the language level.

The third step is to perform attribute lookup in a fixed order.  Now the interpreter asks objects, in order: “Do you have this method?” That lookup follows deterministic rules:

1. instance attributes
2. class attributes
3. base classes (MRO)
4. fallbacks (like reverse methods)

If a method is found, it is bound and called. (Binding is Python fixing the instance (`self`) to a function; calling is executing that function with arguments.) If not, the interpreter either tries the next rule or raises a specific exception

Python uses single dispatch; not multiple-dispatch, not pattern-matching, not type-directed. It is only single-dispatch on the left operand, with explicit fallbacks.

This is why dunder methods like `__radd__` exists, coercion is asymmetric, and most importantly, why order matters

Of course you can call a method yourself and bypass dispatch. When you write `a.__add__(b)` there is no dispatch! You have already decided which object, which method, which function to call.  Dispatch only happens when syntax or builtins defer the decision to the interpreter.

Python is best understood not as a collection of types or abstractions, but as a runtime system that continuously asks questions of objects and proceeds based on their answers. Syntax exists to trigger those questions; dunder methods exist to answer them; dispatch exists to select which answer applies. This model does not explain everything about Python’s implementation, but it explains everything that Python promises. When reasoning at this level, Python stops being a bag of special cases and becomes a coherent system governed by a small number of explicit rules.

This model is not how Python is usually taught, but it is how Python actually operates. Many introductory explanations obscure these mechanics in favor of approachability, delaying the moment when dispatch, binding, and protocol-based execution become explicit. Making these rules visible does not complicate Python; it stabilizes it. Once the interpreter’s role is clearly understood, apparent surprises resolve into predictable outcomes.

*** 

Bibliography:

Abelson, Harold, and Gerald Jay Sussman. Structure and Interpretation of Computer Programs. 2nd ed. Cambridge, MA: MIT Press, 1996.

Berg, J. F., & Barker, J. (1854). Great discussion on the origin, authority, and tendency of the Bible.

Bessis, David. Mathematics as a Creative Art. Translated by Stephen S. Wilson. Cambridge, MA: Harvard University Press, 2022.

Gamma, Erich, Richard Helm, Ralph Johnson, and John Vlissides. Design Patterns: Elements of Reusable Object-Oriented Software. Reading, MA: Addison-Wesley, 1994.

Peters, Tim. “PEP 20 – The Zen of Python.” Python Enhancement Proposals. Last modified August 2004. [https://peps.python.org/pep-0020/](https://peps.python.org/pep-0020/)


Ramalho, Luciano. Fluent Python: Clear, Concise, and Effective Programming. 2nd ed. Sebastopol, CA: O’Reilly Media, 2022.

van Rossum, Guido, and the Python Software Foundation. The Python Language Reference. Python Software Foundation. Accessed [2026-02-10].[https://docs.python.org/3/reference/](https://docs.python.org/3/reference/)