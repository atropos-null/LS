# It's a trap! Hidden Traps & What They’re Really Testing

These notes are a conceptual exploration of Python’s operator and protocol dispatch model, written for my own understanding after encountering unexpected behavior during study. Examples are intentionally abstract and non-specific. The goal is to name underlying invariants and failure modes so learners can reason more clearly about Python’s object model.

Can you identify **which protocol is active** and **who is coordinating whom**, under mild obfuscation?  

## Trap 1: “Looks Like Arithmetic, Isn’t Arithmetic”

Pattern

Using += on a non-numeric object to extend or modify internal state.

Example:

```python

class Playlist:
    def __init__(self):
        self.tracks = []

    def __iadd__(self, track):
        self.tracks.append(track)
        return self

p = Playlist()
p += "Song A"
p += "Song B"
```

What we are thinking incorrectly: 
* “`+=` is just shorthand for +”
* “Augmentation always creates a new object”
* “This is numeric behavior applied elsewhere”

What actually happens (protocol-level)

```
obj += other
```

This performs protocol dispatch in this order:
1.	Call `obj.__iadd__(other)` if it exists
2.	else fall back to `obj = obj.__add__(other)`
3.	else `raise TypeError`

What isn't obvious:

* `__iadd__` may mutate internal state
* `__iadd__` is allowed to return: self (mutating) or a new object
* The caller assumes immutability at their peril.

OMFG Why are you testing me? Because it quietly tests three things at once:
1.	Do you know that `+=` is a protocol, not syntax sugar?
2.	Do you understand the difference between mutation vs rebinding?
3.	Can you reason about state change across time, not just return values?


Where we typically mess up:
* Expecting `+=` to behave like numbers
* Forgetting to return `self` from `__iadd__`
* Assuming `+=` creates a new object
* Missing that **state changed in place**

Spidey senses, look out for these words: 
* “add”
* “include”
* “extend”
* “update”
* “accumulate”
* “collect”


Moral invariant:  `+=` asks an object whether it wants to absorb the change; if it says “yes,” mutation is the point, not the exception.


## Trap 2: “The Output Is a String — But Nobody Said How”

Pattern:
```python
print(container)
```

What we think is happening: `print` formats objects automatically

What is actually happening: 
1. `print` calls `str(container)`
2. `container.__str__` becomes the coordinator
3. It may delegate `str()` calls to collaborators

Where it can go wrong:
* Collaborator returns a non-string
* Collaborator prints instead of returning
* Collaborator introduces layout (e.g., newlines)

What’s am I actually tested on?:
* Understanding of collaboration contracts
* Ownership of formatting responsibility

## Trap 3: “Iteration Without a Loop”

Pattern
```python
x in obj
```

What we think is happening:
* `in` requires `__contains__`
* `in`requires explicit iteration

The actual dispatch order:
1.	`obj.__contains__(x)`
2.	else `obj.__iter__()`
3.	else repeated `obj.__getitem__(index)`

Why does this matter? Tests one's
* knowledge of protocol precedence
* do we understand that protocols overlap

## Trap 4: “The List Comprehension That Freezes People” aka "You can do that??"

Pattern

``` python
", ".join(str(x) for x in items)
```

What we assume:
* we simply wouldn't think about it because it seems too complex
* think that we must write a loop first

So you can do that? 

* Shape transformation: many objects that result in many strings  has to be collapsed into one string
* `str` is the coordinator
* `join` delegates responsibility

What’s actually being tested:
* can you recognize bridge patterns? 
* can you collapse shapes? 

## Trap 5: “`super()` Is Not ‘My Parent’”

Pattern

```python
super().method()
```

Understandable, but false belief that the mro calls the parent class method.

Actual rule about the MRO:
* The next class in the Method Resolution Order (MRO) is called
* Order depends on the the order of classes listed in the subclass (left then right gets called)

What’s being tested
* Mental execution of MRO
* Cooperative multiple inheritance

## Trap 6: “The Conatiner's `__str__` delegaes, so collaborators must be string complain”


A container object builds its string representation by assembling representations of its elements.

Pattern:

```python

class SensorReading:
    def __init__(self, label, value):
        self.label = label
        self.value = value

    def __str__(self):
        return f"{self.label} = {self.value}"

class Dashboard:

    def __init__(self):
        self.readings = []

    def add (self, reading):
        self.readings.append(reading)

    def __str__(self):
        return "Readings: " + ", ".join(str(r) for r in self.readings)

d = Dashboard()
d.add(SensorReading("temp", 21))
d.add(SensorReading("humidity", 55))
print(d)
```

We assume:
* "If the elements are objets, `join` will figure it out"
* "If objects have `__str__`, it will be used automatically. 

What actually is happening:
* `Dashboard.__str__ `is the coordinator.
* It must produce a single `str`
* Dashboard delegates conversion to collaborators by explicitly calling `str(r)`
* `join` requires strings only.

Hidden invariant:
* `__str__ `must return a `str`
* if `join` is in the mix, the `join` input must be an iterable str.

Why is this happening to you?
* Can you distinguish between producing output vs fulfilling a contract?

The moral invariant:  When a container formats its contents, it becomes a coordinator, and coordinator must either enforce collaborator contracts or perform the coercion themselves.


