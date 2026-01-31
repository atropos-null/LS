# In the Beginning

Python is brutally honest about contracts.
Humans are not.

So when I struggle with implicit assumptions under time pressure (aka an oral exam), that’s not confusion — that me abiding by my brain's integrity. My brain wants the contract named before execution. Timed questions, however, love implicit contracts (“*of course* you’d assume X”), and my brain is politely asking, “Cool, where was X stated?” It's hard to realize at the time when the question is asked that my demand for explicitness isn't a deficit; it’s a mismatch between how tests smuggle assumptions and how I correctly prefer to reason.

I do understand legacy and cultural inheritance, however. From what I can determine by asking a lot of AI questions Python sits at the intersection of three traditions:

1. From procedural programming Python keeps:

* Clear control flow
* Readable execution order
* Explicitness over cleverness

I found this refreshing. I loved living here.

2. From object-oriented thinking (Smalltalk lineage, specifically), Python adopts a very specific OO philosophy:

Programs are societies of objects, not sequences of steps, which means that
* Objects own state
* Objects refuse responsibility they shouldn’t have
* Behavior emerges from collaboration, not orchestration

And what do you mean I have to deal with this now? I was trying not to deal with this!!!

3. From functional / Lisp-like thinking 

Python also quietly absorbs ideas from Lisp/Scheme:
* Functions are values
* Behavior can be passed around
* Protocols matter more than types
* Meaning comes from composition, not hierarchy

Python rewards abstraction literacy more than memorization; it is less concerned with what happens next and more concerned with who is allowed to know what.

Procedural code says
```
Do A
Then do B
Then do C
```

Idiomatic Python says:
```
A knows how to do A.
B knows how to do B.
C knows how to cooperate if asked.
```

That’s why things like `__str__`, `__iadd__`, iterables, protocols, and collaborators suddenly matter. They’re not features. They’re social contracts and design, ultimately, is about making future mistakes cheaper.

In Python terms, this results in responsibility pushed downward, coordination is kept thin, and protocols are preffered over conditionals. And when things fail, they fail loudly. What I'm having to groom in myself is the ability to think like a system caretaker. I wish someone had been explicit about that.

What I have struggled to understand is that Python programs are not instructions. They are in fact, agreements between parts.
There may be multiple correct next steps, and correctness depends on social contracts, not logic alone.

### The Whys of Python

Python exists to help humans think clearly about programs that change over time. Python was not designed to be the fastest, safest or most elegant language. It was designed to answer this question: How can a human express an idea to a computer, read it later, and still understand what they meant?

As such it has a lot less guardrails as other languages. Python is not trying to prevent us from making mistakes, encode all correctness at compile time, force us into one paradigm, or protect us from ambiguity. Other languages try very hard to do those things. Python is executable pseudocode that grew teeth.

### OOP: how behavior flows through objects over time.

In Python, all behavior is resolved through objects at runtime via attribute lookup and binding. Everything else is scaffolding:

* Classes exist to create objects and participate in lookup. 
* Methods only matter when bound to an object.
* Responsibility is enforced at the moment a message is sent (method call)

Ultimately, Python optimizes for human comprehension over theoretical purity. Can a human read this, reason about it, and change it later without breaking everything?

Python is pragmatic, not ideological. While many languages start with a belief system,
- Java: “Everything is an object.”
- Haskell: “Everything is a function.”
- C: “Everything is memory.”

Python says “Use whatever model helps you think clearly right now.”

That’s why Python simultaneously supports procedural code, functional patterns, OOP, and metaprogramming
without declaring any of them morally superior. OOP in Python is a tool, not a religion.

OOP in Python exists to localize responsibility.  Not to model reality perfectly. Not to mimic “real-world objects.”
Not to enforce abstraction for its own sake. But to answer questions like: "Who owns this data?", "Who is allowed to change it?", "Where does this behavior live so future-me can find it?" But ultimately, Objects are passive until invoked.

Python objects feel actor-like because (again!): they have identity, they respond to messages, they carry history (state),
and they persist through time. But Python never forgets that objects are passive until invoked.

In fact, Python could have forced everything through classes more aggressively, but it didn't. Because classes are not where meaning lives. Meaning lives in runtime behavior, protocols being honored, and objects cooperating successfully, which is why Python takes one of its deepest philosophical positions through Duck Typing. It is a moral stance.

The foundation of Duck Typing then implies that identity is secondary to behavior, labels matter less than capability,and contracts are implicit but testable. This puts *me* in a bad position.

Python methods are not conversations between actors, but callable affordances exposed under a name. Human Conversations require shared meaning. **Python requires shared interfaces**. An object in Python is something that comes into existence, has identity, can be acted upon, and persists through time until it’s no longer referenced. Objects are code infants that exist to carry state forward through time, so behavior doesn’t have to be recomputed from scratch every moment.

OOP in Python exists because state persists, responsibilities need names, and as a human-derived language, humans like to group related things. Not because: “everything is an object” (that’s marketing), or because the real world is object-shaped.
OOP is optional but convenient. You use it when time matters, identity matters, history matters. Otherwise, Python is happy with functions.

Python is a language designed to make the human understanding of a program the primary artifact — not the program’s formal properties.

## Python Belief System

1. Python believes humans are the bottleneck.  Python consistently chooses runtime clarity over compile-time certainty,explicit behavior over cleverness, debuggability over purity. The unstated belief is that humans need to see what’s going on to think clearly.

2. **Python distrusts hidden magic (but tolerates controlled magic)**. Python allows magic — but only if you can: inspect it override it, or remove it. For example, dunder methods are explicit. Metaclasses exist, but are rare and visible. Monkey patching is allowed (wild, but honest). The belief is that if something affects behavior, you should be able to find it. This is why Python feels “transparent” compared to many OO languages.

3. **Python assumes change is inevitable**. Python is built for evolving requirements, partial understanding, refactoring later. So it delays decisions until runtime, allows flexible interfaces, and avoids freezing structure too early. The belief is that the first design will be wrong — and that’s okay.

4. **Python prefers social contracts over legal ones**. Python does not enforce strict encapsulation, access modifiers, or  interface declarations (at runtime). Instead it relies on naming conventions, documentation, shared understanding. The founders believe that programmers are adults who can negotiate responsibility. Of course that assumes a good faith approach by the developers. Which, YMMV.

5. **Python is comfortable with partial failure**. Python doesn’t try to prevent all errors. It assumes that some mistakes are unavoidable, and that catching them early is enough. Errors are part of reality, not moral failures.

6. **Time is real**. Programs live in time, not on a blackboard.

7. **Python optimizes for readability**. Reading includes future-you, tired-you, stressed-you, and especially someone who doesn’t share your assumptions.

8. **Python avoids totalizing worldviews**. Python refuses to say:

* “Everything is an object”
* “Everything is functional”
* “Everything is static”

Wait, you might remember as I do how many education materials say '(Almost) Everything IS an object!' “Everything is an object” is technically true in Python’s implementation. What Python refuses to say is: “You must model, design, and reason about your program as if everything were an object. Yes, everything is an object at runtime - but you don’t have to care most of the time.”

The quiet moral stance Python ultimately takes is that "Complex systems survive through cooperation, not control." This shows up in duck typing, a softer OOP approach than other languages, convention over enforcement, readable error messages, and community norms. Python doesn’t try to save you from yourself.

What **I** must learn are what assumptions Python itself makes, vs which assumptions humans layer on top.

### “If Python refuses to impose meaning, how do I decide where meaning lives?”

And how do I even start to know where to stand? If nothing tells me where to stand, how do I even place my feet?

> You don’t start by standing somewhere. You start by watching what moves.

**Stand where state persists**. Anything that survives across function calls, accumulates history, can be corrupted over time is a place meaning belongs. That’s where objects naturally appear. 

**Stand where change would be dangerous** “If this changes unexpectedly, what breaks?” That answer tells you where responsibility lives, what deserves an interface, what needs protection or clarity.

Stand where humans must coordinate.

Python says look how we readable we are and then you realize its a bag of cats. Python smiles warmly, hands you a cup of tea, says “readability counts”… and then you open the cupboard and it’s just cats. Everywhere. Different sizes. Some feral. Some very polite. All technically valid.

Because I am sensitive to implicit structure, I can't just skim, pattern-match and rely on vibes. I want the invariant, the contract named, and to know which cats are load-bearing.

Python doesn’t label the cats.

So your brain goes:
“Cool, but which of these will bite me under pressure?”

Python just winks and giggles, but the hidden rule Python never states:  Python code is readable when responsibility boundaries are obvious, not when syntax is simple. Most Python code is syntactically readable and structurally unreadable.

That’s the bag.

### A guide for the perplexed

Use a function when:

* you’re transforming inputs to outputs
* state does not persist
* you don’t need identity
* you want clarity under time pressure

Use a class/object when:

* state persists and must remain coherent
* operations must preserve an invariant
* identity matters (this specific instance)
* you want to bundle data + behavior to reduce coordination overhead

Use composition when:

* you want interchangeable parts
* you can describe the thing as “has-a”
* you want to avoid inheritance traps

Use inheritance when:

* you genuinely have a stable “is-a” relationship
* you expect polymorphism across variants and the base class represents a real shared contract, not code reuse

In Python, inheritance is often the wrong cat for code reuse. Composition is the calmer cat. (Still allergic, but calmer.)

### “Right cat” examples in one-liners

These are heuristics you can literally memorize:

* If you can’t name the invariant → function first
* If state persists → object owns it
* If you’re reusing code → composition before inheritance
* If misuse should be impossible → raise early
* If future-you must find it fast → localize responsibility

***

References


Goldberg, A. (1983). Smalltalk-80: The Language and Its Implementation.
[The Python Language reference. (n.d.). Python Documentation.](https://docs.python.org/3/reference/index.html)
Thomas, D., & Hunt, A. (2019). The pragmatic programmer: Your journey to mastery, 20th Anniversary Edition. Addison-Wesley Professional.
[Zaczyński, B. (2023, June 2). What exactly is the Zen of Python?](https://realpython.com/zen-of-python/#:~:text=The%20Zen%20of%20Python%20consists,Simple%20is%20better%20than%20complex.())