# Python 120 Working Document

<a name="top"></a>

## Notes from Object Oriented Programming with Python Book

- [Notes from Object Oriented Programming with Python Book](#notes-from-object-oriented-programming-with-Python-Book)
- [Flexible by Design: Advocating Composition Over Inheritance in Python](#flexible-by-design-advocating-composition-over-inheritance-in-python)
- [Attributes and Properties](#attributes-and-properties)
- [Problem Sets: Classes and Objects](#problem-sets-classes-and-objects)
- [Interlude: A note from Chat GPT](#interlude-a-note-from-chat-gpt)

## Notes from Object Oriented Programming with Python Book

### Introduction: The Philosophy of Pythonic OOP

Object-Oriented Programming (OOP) is a strategic approach to software design, created to manage the inherent complexity of large-scale applications and enhance long-term maintainability. As programs grow, a monolithic structure with deep interdependencies becomes brittle and difficult to modify. OOP addresses this by promoting a modular architecture built from smaller, discrete, and interacting parts. This guide translates the core theories of OOP into actionable, idiomatic Python best practices for professional developers.

The fundamental goal of OOP is to model real-world concepts using **Classes** and **Objects**. A class serves as a blueprint, defining the structure and capabilities of a certain type of entity. An object (or instance) is the concrete product created from that blueprint. As one core principle states, "Every class defines a type, and every type has a class." Creating a new object from a class means creating a new instance of that class.

In Python, this paradigm is central: most entities you interact with are objects, including numbers and strings. However, language constructs such as `if` or `for` statements, keywords like `class` or `def`, and variables (which are merely labels pointing to objects in memory) are not objects themselves.

With this foundation, let's explore the first step in effective object-oriented design: the construction of clean, readable, and effective classes.

***

### Crafting Clean and Readable Classes

Clear, consistent conventions in class design are crucial. A well-designed class is a stable, predictable, and understandable unit of functionality.

#### Naming Conventions: The Language of Your Code

- **Class Names:** Use **PascalCase** (a.k.a. UpperCamelCase) for class names.

    ```python
    class GoodDog:
        pass
    ```

- **Semantic Naming:** Classes are nouns (e.g., `Character`). Methods represent actions (verbs), e.g., `move()`, `attack()`.

    ```python
    class Character:
        def move(self):
            pass
        def attack(self):
            pass
    ```

#### The Initializer Method: Establishing a Valid State

The `__init__` method ("dunder init") is the initializer, not the constructor. Instantiation involves two steps:

1. `__new__`: Allocates memory for a new object.
2. `__init__`: Initializes the object's state.

```python
class GoodDog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

sparky = GoodDog('Sparky', 5)
```

####  The `self` Parameter: The Object's Reference

- `self` must be the first parameter in an instance method.
- When calling a method, Python passes the instance automatically.

```python
class GoodDog:
    def speak(self):
        print(f"{self.name} says woof!")

sparky.speak()  # Equivalent to GoodDog.speak(sparky)
```

#### State vs. Behavior

| Category  | Description                                                                          |
|-----------|--------------------------------------------------------------------------------------|
| State     | Data associated with a specific instance, stored in instance variables (`self.name`). |
| Behavior  | Exposed through instance methods (`speak()`, `roll_over()`), shared across instances. |

---

### Mastering Encapsulation and Data Integrity

Encapsulation bundles data and methods within an object, hiding details and creating a stable public interface.

#### Python's Approach to Privacy

Python uses **convention**, not enforcement, for privacy—prefix internal attributes with a single underscore:

```python
class GoodDog:
    def __init__(self, name, age):
        self._name = name
        self._age = age
```

Direct external modification is discouraged and risky.

#### Controlled Access with Getters and Setters

Getter and setter methods provide controlled access:

```python
class GoodDog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def name(self):
        return self._name

    def set_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Age must be an integer')
        if new_age < 0:
            raise ValueError("Age can't be negative")
        self._age = new_age
```

#### The Pythonic Way: Using `@property`

The `@property` decorator provides **managed attributes** with clean syntax:

```python
class Person:
    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f'{first_name} {last_name}'

    @name.setter
    def name(self, name_tuple):
        first_name, last_name = name_tuple
        self._set_name(first_name, last_name)

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic.')

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name
```

**Use properties to:**

- Discourage direct misuse
- Validate assigned data
- Refactor internal storage
- Provide computed attributes
- Improve readability

***

### Understanding Class-Level Members

Classes may have **attributes** and **methods** shared across all instances.

#### Class Variables: Shared State

Class variables are defined in the class body and shared:

```python
class GoodCat:
    counter = 0  # Class variable

    def __init__(self):
        GoodCat.counter += 1

    @classmethod
    def number_of_cats(cls):
        return GoodCat.counter

cat1 = GoodCat()
cat2 = GoodCat()
print(GoodCat.number_of_cats())  # Output: 2
```

#### Class Methods: Operations on the Class

Class methods operate on the class, not instances. Use the `@classmethod` decorator; `cls` is the first parameter.

```python
class GoodCat:
    @classmethod
    def what_am_i(cls):
        print("I'm a GoodCat class!")

GoodCat.what_am_i()
```

#### Static Methods: Uncoupled Utility Functions

Static methods do not receive `self` or `cls` and behave like regular functions within a class's namespace.

***

### Integrating Objects with the Python Ecosystem (Dunder Methods)

To make custom objects behave like native types, implement dunder methods.

#### Object Representation: `__str__` and `__repr__`

- `__str__`: Human-readable, used by `print()` and f-strings.
- `__repr__`: Developer-oriented, ideally reconstructs the object.

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Cat({repr(self.name)})"

cat = Cat('Fuzzy')
print(cat)           # Output: Fuzzy
print(f"The cat is {cat}.")  # Output: The cat is Fuzzy.
print(repr(cat))     # Output: Cat('Fuzzy')
```

**Implementing `__str__` is preferred over a custom `.display()` method.**

#### Comparison and Equality: `__eq__`, `__lt__`, etc.

Define `__eq__` to support value-based equality. Return `NotImplemented` for unknown types to allow symmetric comparisons.

**Incorrect: (non-symmetrical)**
```python
class Vegetable:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        if not isinstance(other, Vegetable):
            return False
        return self.name == other.name
```

**Correct:**
```python
class Vegetable:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        if not isinstance(other, Vegetable):
            return NotImplemented
        return self.name == other.name
```

When natural ordering exists, also define `__ne__`, `__lt__`, `__gt__`, etc.

#### Arithmetic Operators

Only define arithmetic dunder methods (`__add__`, `__iadd__`, etc.) if their meaning is intuitive and consistent with built-in types. Operators like `+` and `*` should obey mathematical laws when used.

***

### Designing Robust Class Relationships

Two main relationships:

- **Inheritance** ("is-a")
- **Composition** ("has-a")

#### Inheritance: The "Is-A" Relationship

Subclass acquires attributes/methods from the superclass:

```python
class Vehicle:
    def drive(self):
        print('I am driving.')

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

class Motorcycle(Vehicle):
    def drive(self):
        print('I am riding!')
```

Use `super()` to extend superclass behavior:

```python
class Vehicle:
    def __init__(self, wheels):
        self._wheels = wheels
        print(f'I have {self._wheels} wheels.')

class Car(Vehicle):
    def __init__(self):
        print('Creating a car.')
        super().__init__(4)
```

#### Composition: The "Has-A" Relationship

Build classes from other classes' functionality:

**Mix-ins** provide reusable behaviors:

```python
# color_mixin.py
class ColorMixin:
    def set_color(self, color):
        self._color = color
    def get_color(self):
        return self._color

# car.py
from color_mixin import ColorMixin

class Car(Vehicle, ColorMixin):
    def __init__(self, color):
        self.set_color(color)

# house.py
from color_mixin import ColorMixin

class House(ColorMixin):
    def __init__(self, color):
        self.set_color(color)
```

Mix-ins enable behavior sharing without forcing is-a relationships.

#### The Guiding Principle: Composition Over Inheritance (COI)

- **Prefer** composition unless inheritance is natural.
- Use inheritance only for true "is-a" relationships.
- Refactor toward mix-ins and composition for flexibility.

Ask:

1. Is there a true "is-a" relationship?
2. Would the subclass override most behavior?
3. Does the relationship make sense to users?
4. Would multiple categories apply? (Favor mix-ins and composition.)

***

### Method Resolution Order (MRO): How Python Finds Methods

Python uses the **Method Resolution Order (MRO)** to determine which method to execute, especially in multiple inheritance.

Use `.mro()` to inspect order:

```python
class Creature: 
    pass
class Mammal(Creature): 
    pass
class LandDwellingMixin: 
    pass
class Primate(LandDwellingMixin, Mammal): 
    pass
class LanguageMixin: 
    pass
class BipedalismMixin: 
    pass
class Human(BipedalismMixin, LanguageMixin, Primate): 
    pass

print(Human.mro())
# [
#     <class '__main__.Human'>,
#     <class '__main__.BipedalismMixin'>,
#     <class '__main__.LanguageMixin'>,
#     <class '__main__.Primate'>,
#     <class '__main__.LandDwellingMixin'>,
#     <class '__main__.Mammal'>,
#     <class '__main__.Creature'>,
#     <class 'object'>
# ]
```

The MRO is a modified depth-first, left-to-right search through parent classes as listed in each class definition.

By mastering class design, encapsulation, dunder methods, inheritance, composition, and the MRO, you can build robust and maintainable object-oriented systems in Python. These best practices form the foundation of professional, idiomatic Python code that is clear, flexible, and built to last.

### Summary 

At this point, you should be familiar with the basics of OOP in Python. You should understand these concepts:

* The relationship between a class and an object
* The idea that a class groups behaviors (ie, methods)
* The idea that an object has a state that is modeled by its instance variables

**Object level**

Objects do not share state with other objects, but do share behaviors. Put another way, the values in the objects' instance variables (states) are different, but they can call the same instance methods (behaviors) defined by the class.

**Class level**

Classes also have behaviors not intended for objects (class methods).

**Inheritance**

Subclasses can have multiple parent classes due to multiple inheritance (MI). We will not explore MI very much in this course, so we will mostly ignore it going forward.

* Ignoring MI, we can say that subclasses have exactly one parent class.
* If an explicit parent class is not defined, Python uses the object class.
* The parent class is often called the superclass.
* The parent class of a parent class is also a superclass of the subclass. All ancestor classes of a subclass are superclasses of the subclass.
* We can use carefully constructed classes as mix-ins; this is the safe way to use MI.
* Mix-ins aren't used for instantiating objects.
* You should understand the method resolution order (MRO).
* The real magic of OOP is that we can create custom objects. The Python core library works the same way: there are classes, and there are objects instantiated from those classes. When we create our own classes, you can almost think of it as adding additional functionality into the Python core library (not quite, though).

Page Reference: [Object Oriented Programming with Python](https://launchschool.com/books/oo_python)

[Back to the top](#top)

## Flexible by Design: Advocating Composition Over Inheritance in Python

### Introduction

In modern software architecture, the "Composition Over Inheritance" principle is no longer a suggestion; it is a fundamental tenet for building resilient, adaptable systems. For developers in Python, a language celebrated for its flexibility, this choice is not merely an implementation detail but a critical design philosophy that shapes the future of a software system. The principle of "Composition Over Inheritance" (COI) advocates for building complex objects from smaller, independent objects rather than inheriting behaviors from a rigid hierarchy of parent classes. The objective of this paper is to critically examine the trade-offs between these two paradigms. We will argue that a deliberate preference for composition and its related patterns leads to systems that are significantly more modular, flexible, and maintainable in the long run. This analysis will begin with a review of classical inheritance, move to an exploration of compositional patterns, provide a direct comparative analysis, and conclude with a practical framework for making informed design decisions.

***

### The Classical Inheritance Model: A Critical Review

#### Context and Purpose

Before critiquing the inheritance model, it is essential to understand its intended purpose and inherent benefits in object-oriented design. Inheritance is a powerful mechanism for creating logical hierarchies and promoting code reuse. This section will explore the core concept of the "is-a" relationship, demonstrate its power for sharing code and enabling polymorphism, and then analyze the common pitfalls of rigidity and tight coupling that arise from its misuse.

### The "Is-A" Relationship and Its Benefits

At the heart of classical inheritance lies the "is-a" relationship, where a subclass is a more specialized version of its superclass. This model allows subclasses to acquire all the behaviors and properties of their parent, enabling developers to extract common functionality into a shared base class. The result is a system with less duplicated code and a clear, hierarchical structure.

Consider a simple hierarchy for pets. A Dog is a Pet, and a Cat is a Pet. This relationship can be modeled directly with inheritance:

```python
class Pet:
    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')

class Dog(Pet):
    def speak(self):
        print(f'{self.name} says Woof!')

class Cat(Pet):
    def speak(self):
        print(f'{self.name} says Meow!')
```

In this example, both `Dog` and `Cat` inherit the `__init__` method from `Pet`, eliminating the need to duplicate the name-initialization logic. When a `Dog` or `Cat` object is created, Python tries to call `__init__` on the object's class. However, neither of our subclasses has an `__init__` method. Python persists; it looks to the superclass for a method with the same name. In this case, it finds `__init__` in the `Pet` class and invokes it. The subclasses can then add their own specialized behaviors, such as their unique `speak` methods. This structure provides a clean and intuitive way to model real-world hierarchies and share common code.

### The Pitfalls of Rigidity: When "Is-A" Breaks Down

Despite its benefits, the "is-a" model creates a tight coupling between a superclass and its subclasses. This bond is defined at the time of implementation and cannot be easily changed, leading to rigid and brittle class hierarchies. The model begins to break down when a subclass must fundamentally alter or negate a core behavior inherited from its parent.

Let's examine a Bird class hierarchy. It seems logical that a Sparrow is a Bird and a Penguin is a Bird. We might start with a base class like this:

```python
class Bird:
    def fly(self):
        print("I can fly!")

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        print("I can't fly.")
```

Here, the `Penguin` class is forced to override the `fly` method to negate a behavior that does not apply to it. This is a significant "red flag" in object-oriented design because it violates the **Liskov Substitution Principle (LSP)**. This principle states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. By changing the fundamental meaning of `fly`, the `Penguin` class breaks the contract of the `Bird` superclass. A piece of code expecting any `Bird` to be able to fly will fail if it receives a `Penguin`. This scenario reveals a key weakness of inheritance: any change to a base class can have cascading and unexpected effects on its subclasses. This inflexibility makes the system harder to maintain and extend, as developers must constantly account for exceptions and overrides throughout the hierarchy.

The limitations exposed by rigid "is-a" hierarchies necessitate a more adaptable approach to software design, paving the way for the flexible alternatives offered by composition.

***

### The Compositional Approach: Building with "Has-A" Relationships

#### Context and Purpose

Composition represents a strategic shift in design thinking, favoring flexibility and modularity over rigid hierarchies. It is a powerful alternative to inheritance that allows objects to be assembled from independent, reusable components. This section will define the "has-a" relationship and illustrate through practical examples—including pure composition and mix-ins—how this approach effectively decouples behavior from concrete types, leading to more adaptable and maintainable code.

#### Delegating Behavior with Composition

Composition is a design principle where a class achieves its functionality not by inheriting it, but by containing other objects and delegating responsibilities to them. Instead of an "is-a" relationship, this creates a "has-a" relationship. An object has a component that provides a specific capability.

Let's refactor the Bird example from the previous section using composition. Instead of defining flying as an intrinsic behavior of all birds, we can model it as a separate capability that a bird has.

```python
class FlyWithWings:
    def fly(self):
        print("I can fly!")

class CannotFly:
    def fly(self):
        print("I can't fly.")

class Bird:
    def __init__(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def fly(self):
        self.fly_behavior.fly()

# Create instances with different behaviors
sparrow = Bird(FlyWithWings())
penguin = Bird(CannotFly())

sparrow.fly()  # Output: I can fly!
penguin.fly()  # Output: I can't fly.
```

This design elegantly solves the rigidity problem. The `Bird` class is no longer tightly coupled to a specific flying implementation. Instead, it holds a reference to one of several collaborator objects (`FlyWithWings` or `CannotFly`) and delegates the `fly` call to it. This approach demonstrates a clear separation of concerns: the `Bird` class manages its own state, while the flying behavior is encapsulated in separate, interchangeable collaborator objects. This loose coupling means behaviors can even be changed at runtime, offering a level of flexibility that inheritance cannot match.

#### Sharing Functionality with Mix-ins

Mix-ins are a strategic tool for decoupling capabilities from identity. They are a specialized pattern in Python that leverages multiple inheritance in a safe, controlled manner. A mix-in is a class that provides a specific set of methods to be "mixed into" other classes, but it is not intended to be instantiated on its own. This is ideal for adding shared functionality across classes that have no logical "is-a" relationship. A common convention is to add a `Mixin` suffix to the class name, clearly signaling its purpose.

Consider `Car`, `House`, and `SmartLight` objects. All of them might have a configurable color, but it would be nonsensical to create a `ColorfulObject` superclass. This is a classic "has-a" scenario: a car has a color, a house has a color, and so on. A mix-in is the perfect tool for this.

```python
# In color_mixin.py
class ColorMixin:
    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

# In other files, classes use the mix-in
from color_mixin import ColorMixin

class Car(ColorMixin):
    def __init__(self, color):
        self.set_color(color)

class House(ColorMixin):
    def __init__(self, color):
        self.set_color(color)

class SmartLight(ColorMixin):
    def __init__(self, color):
        self.set_color(color)
```

By adding `ColorMixin`, `Car`, `House`, and `SmartLight` all gain the ability to get and set a color without being forced into an artificial hierarchy. This approach contrasts sharply with the anti-pattern of a `ColorfulObject` superclass. Such a design is architecturally flawed for several reasons. First, it creates a logical inconsistency by forcing an "is-a" relationship where none exists; a car is not a type of colorful object, but a vehicle that has a color. Second, it leads to a rigid and inflexible design. Single inheritance would force a `Car` to choose between being a `ColorfulObject` and a `Vehicle`, creating unnecessary complexity. Finally, it blurs concerns by conflating an object's core identity with one of its many possible capabilities. Mix-ins avoid these pitfalls by separating behaviors into reusable, pluggable components, embodying the flexibility of the "has-a" philosophy.

The "has-a" relationship, realized through composition and mix-ins, provides a powerful toolkit for building modular and adaptable systems, offering a clear and compelling alternative to the rigidity of classical inheritance.

***

### A Comparative Analysis: Inheritance vs. Composition

#### Context and Purpose

Having explored both paradigms individually, this section provides a direct, analytical comparison between inheritance and composition. The goal is to move beyond theory and evaluate the practical impact of each approach on key software quality attributes. This analysis will distill the fundamental differences in their approach to relationships, code reuse, and maintainability, providing a clear basis for making architectural decisions.

### Core Design Principles at a Glance

The following table summarizes the core differences between the two design paradigms:

| Inheritance           | Composition                       |
|-----------------------|-----------------------------------|
| Relationship Type: "Is a" relationship    | Relationship Type: "Has a" relationship          |
| Coupling: Tight coupling, rigid trees     | Coupling: Loose coupling, more flexibility        |
| Code Reuse: Reuses superclass code        | Code Reuse: Reuses through delegation             |
| Maintainability: Hard to change in large hierarchies | Maintainability: Easy to extend and modify       |

#### Evaluating the Trade-offs

The distinctions outlined in the table have profound implications for the lifecycle of a software project.

- **Coupling and Flexibility:** Inheritance creates a strong, compile-time bond between a parent and child class. This coupling is static; a Dog is always a Pet and cannot change this relationship. In contrast, composition establishes relationships between objects, often at runtime. A Bird can be initialized with different `fly_behavior` objects, making its capabilities dynamic and configurable. This loose coupling makes the system far more flexible and adaptable to new requirements.
- **Reuse and Maintainability:** Inheritance promotes code reuse by directly sharing the implementation of a superclass. While this appears efficient, it is also risky, as a change in the superclass implementation can break an unknown number of subclasses in unforeseen ways. Composition, on the other hand, promotes reuse of interfaces through delegation. The composing class does not need to know the internal details of its components, only the public methods they expose. This makes components much safer to modify or swap out, as changes are encapsulated and do not cause ripple effects. Consequently, compositional designs are generally easier to reason about, test, and maintain.

While inheritance can be a simple solution for stable, clear hierarchies, composition offers a fundamentally more robust and flexible foundation for building complex, evolving systems.

***

### A Practical Decision Framework: Choosing the Right Tool

#### Context and Purpose

Choosing between inheritance and composition is a crucial architectural decision that impacts a project's entire lifecycle. It is not always an either/or proposition, but a matter of selecting the most appropriate tool for the task at hand. This final section distills the paper's analysis into a diagnostic tool that a senior developer must use to make and defend their architectural choices, ensuring they align with long-term goals of flexibility and maintainability.

#### Guiding Questions for Architectural Design

When faced with a design choice, asking the following questions can clarify whether an "is-a" or "has-a" relationship is more appropriate.

1. **Is there a true "is-a" relationship?**
    - If one class is genuinely a more specialized version of another, inheritance may be appropriate. However, a semantic "is-a" link is not sufficient. The classic "Square is a Rectangle" problem illustrates this: while mathematically true, it can be problematic in code if their interfaces are not behaviorally compatible. The subclass must be substitutable for the superclass without altering program correctness (adhering to LSP).
2. **Would a subclass need to override most of the superclass's behavior?**
    - Extensive overriding is a clear indicator that the "is-a" relationship is weak. If a subclass must undo or significantly change inherited functionality (like the Penguin negating fly), it signals that the abstraction is incorrect. Composition is a better pattern for sharing partial functionality without enforcing a strict hierarchy.
3. **Could the object belong to multiple categories?**
    - If an object could logically have multiple identities (e.g., a Cat is both a Pet and a Predator), attempting to model this with inheritance leads to the complexities of multiple inheritance. Composition, through mix-ins or collaborator objects, handles these multi-faceted identities much more elegantly by allowing a class to simply have the behaviors of each category.
4. **Does the relationship feel more like "has-a" than "is-a"?**
    - Ultimately, the most intuitive question is often the most revealing. If the relationship describes a capability, property, or component that an object possesses (e.g., "a car has a color"), composition is the natural and correct choice. This framing aligns with building objects from independent, reusable parts.

These guiding questions provide a pragmatic toolset for navigating design decisions, encouraging a thoughtful approach that prioritizes flexibility and conceptual clarity over dogmatic adherence to a single pattern.

### Conclusion

While classical inheritance is a fundamental concept in object-oriented programming and a useful tool for modeling stable, clear hierarchies, it is not a universal solution. This paper has argued that the "Composition Over Inheritance" principle should be the default guiding philosophy for building robust, scalable, and maintainable software in Python. By favoring "has-a" relationships over "is-a" relationships, we design systems with loosely coupled components, clear separation of concerns, and enhanced flexibility. Embracing composition and its related patterns, such as mix-ins and delegation, leads to systems that are not only easier to reason about and test but are also fundamentally more adaptable to the inevitable reality of future change.

[Back to the top](#top)

***

## Attributes and Properties

In software engineering, precise terminology is not an academic exercise but a prerequisite for effective system design and clear team communication. While terms like '**attribute**' and '**property**' are often used interchangeably in casual discourse, their loose application can obscure critical design decisions. To build a robust mental model, this guide will adhere to a set of precise working definitions, acknowledging that in the wider industry, these terms can be ambiguous.

* **Attribute**: The broad umbrella term encompassing everything "belonging" to an object. This includes both the data it stores (instance variables) and its behaviors (methods).
* **Instance Variable**: The raw data stored within an object instance that represents its internal state. By convention, this is often prefixed with an underscore (e.g., `_balance`) to signify it is not part of the public interface.
* **Property**: A specialized public interface, created using decorators like `@property` and `@name.setter`, that provides controlled access to an object's underlying state.

Thus, a property acts as a controlled gateway, or public interface, to a private instance variable, and both are types of attributes. With these definitions established, we can now analyze the practical consequences of failing to distinguish between an object's public interface and its internal state.

### The Danger of Direct Attribute Access

One of the most pervasive anti-patterns in object-oriented design is allowing uncontrolled modification of an object's internal state. This practice, while expedient, creates a critical vulnerability that is a frequent source of system fragility. It effectively turns an object into a passive data structure, abdicating its core responsibility to manage its own consistency.

Consider a simple `BankAccount` class:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

By exposing `self.balance` directly, we allow any external code to modify it at will. This leads to a catastrophic failure of integrity:

```python
account = BankAccount(100)
account.balance = -5000  # Violation of a core business rule
```

This single assignment has corrupted the object, placing it into an invalid state by violating a fundamental state invariant—that a balance cannot be negative. The core problem is architectural: the `BankAccount` object has no power to defend its own encapsulation boundary. It has abdicated its responsibility for consistency to external, un-trusted code that lacks the necessary context to uphold the object's rules.

This vulnerability requires a professional solution that empowers the object to enforce its own invariants. That solution is the property.

###  Enforcing Integrity with Properties

Properties are the primary mechanism for achieving true encapsulation. They allow an object to present a clean public interface while retaining absolute control over how its internal data is accessed and modified. By intercepting read and write operations, properties transform an object from a passive container into an active guardian of its own state.

Let's refactor our `BankAccount` class to properly encapsulate its state, transforming it into a robust, self-regulating entity:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # The initial assignment is routed through the setter

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
```

This robust design implements a powerful pattern by combining three components that work in concert:

* **The Internal State**: The actual data is stored in `self._balance`, the backing field. The leading underscore is not a privacy feature enforced by the language, but a deeply respected convention signaling to other developers that this variable is part of the internal implementation and must not be accessed directly.

* **The Public Read Interface**: The method decorated with `@property` defines the "getter." When external code accesses `account.balance`, this method is transparently invoked, providing read access to the internal state.

* **The Public Write Interface**: The method decorated with `@balance.setter` defines the "setter." It acts as a gatekeeper, intercepting any attempt to assign a value to `account.balance`. This is where we place our validation logic, guarding the backing field and ensuring the object's state invariants are never violated.

With this architecture, an attempt to set a negative balance is intercepted by the setter, which raises a `ValueError` and prevents the object from ever entering an invalid state. The object now successfully defends its own integrity. While this validation is a primary benefit, the strategic advantages of properties extend far beyond simple rule enforcement.

### The Strategic Advantages of Properties Beyond Validation

Mastering properties means understanding their full range of architectural benefits. They are far more than a defensive tool; they provide crucial flexibility that allows a class to evolve without altering its public interface—the cornerstone of long-term maintainability.

A property can compute and return a value on the fly rather than retrieving a stored variable. This is ideal for derived data, as it enforces a single source of truth and prevents data desynchronization. For example, if an object stores `width` and `height`, an `area` property can calculate `width * height` on each access, ensuring it is always correct without the risk of becoming stale if the dimensions change.

A property's setter provides a reliable and centralized hook for triggering secondary actions. This is immensely powerful for logging changes, sending notifications, invalidating a cache, or updating other parts of the system in response to a state change. The setter guarantees that these side effects are executed consistently, without requiring the calling code to have any knowledge of them.

### Ensuring Future Flexibility

The most critical long-term benefit of properties is API contract stability. An architect can design a class with simple attributes initially, and later, refactor one into a property with sophisticated logic. This evolution is a non-breaking change. Because the external access pattern (`object.name`) remains identical, no client code that uses the class needs to be modified. This principle is what allows large teams to work in parallel and enables libraries and frameworks to evolve without causing cascading failures across dependent systems. It minimizes maintainability costs by ensuring an object's public interface remains stable even as its internal implementation changes.

Properties are the superior architectural mechanism, providing a controlled public interface that empowers an object to enforce its invariants, guarantee its integrity, and evolve gracefully over time. They are the enabler of validation, computed values, side effects, and, most critically, a stable API contract. For long-lived, business-critical objects, encapsulate all instance variables with properties by default. This discipline is a strategic investment that ensures your objects are robust, your system is maintainable, and your codebase is future-proof, reflecting the principles of sound, professional software architecture.

Page Reference: [Attributes and Properties](https://launchschool.com/lessons/50ed1d17/assignments/e3750536)
[Back to the top](#top)

***

## Problem Sets: Classes and Objects


### The Basic Blueprint: Creating the Person Class

Let's start with a simple goal. We want to create a `Person` class that allows us to create a new person with a name and then print that name.

Here's the code we want to make work:

```python
bob = Person('bob')
print(bob.name)           # Expected output: bob
bob.name = 'Robert'
print(bob.name)           # Expected output: Robert
```

To achieve this, we need to define the `Person` blueprint. Here is the complete solution:

```python
class Person:
    def __init__(self, name):
        self.name = name
```

This short block of code contains the three core concepts you need to understand to get started with classes. Let's break it down:

- `class Person:` This line is the blueprint declaration. It simply tells Python, "I am defining a new type of thing called Person."
- `def __init__(self, name):` This is the initializer (often called a "constructor"). It's a special method that runs automatically every single time a new `Person` object is created (like when we write `Person('bob')`).
  - The `self` parameter refers to the specific instance being created (the "house" itself, e.g., `bob`). Python handles this for you.
  - The `name` parameter is the data we pass in when creating the object.
- `self.name = name` This is the action of storing the data. This line takes the `name` argument passed into the initializer and saves it as an attribute on the instance (`self`). This makes it accessible later using dot notation, like `bob.name`.

Now that we have a basic `Person`, let's make it smarter by teaching it how to handle first and last names separately.

---

### Adding Intelligence: Properties and Setters

Our next challenge is to make our `Person` class manage a `first_name` and a `last_name` internally, while still providing a convenient `name` attribute for the full name.

Let's start by explicitly coding the name-splitting logic right into our initializer.

```python
class Person:
    def __init__(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ''
        if len(parts) > 1:
            self.last_name = parts[1]
```

This works, but it has a limitation: if we change `first_name` or `last_name` later, the full name won't be available. And what if we want to set the full name and have it automatically update the parts? To solve this, we introduce two powerful features: `@property` and `@name.setter`.

Here is the evolved `Person` class that uses them to create a more robust and intelligent object:

```python
class Person:
    def __init__(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ''
        if len(parts) > 1:
            self.last_name = parts[1]

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @name.setter
    def name(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ''
        if len(parts) > 1:
            self.last_name = parts[1]
```

Internally, our setter creates `self.first_name` and `self.last_name` as standard attributes. While we could add properties for them too (as the full source code does), for this lesson, we are focusing only on the `name` property.

This looks more complex, but the two new decorators give us incredible control.

| Feature        | Primary Benefit for the Programmer |
|---------------|------------------------------------|
| `@property`   | Allows you to define a "getter" method for an attribute. The `name` attribute is now dynamically created from `first_name` and `last_name`, ensuring it's always up-to-date. The `.strip()` is a robust way to handle cases where `last_name` is empty, preventing an unwanted trailing space.<br>**Why it's powerful:** This allows you to change how a value is calculated internally without ever changing how other programmers access it. |
| `@name.setter`| Allows you to define a "setter" method that runs whenever someone tries to assign a value to `.name`. This gives you control to perform logic, like splitting the full name into two parts.<br>**Why it's powerful:** This is crucial for data validation and ensuring that an object's internal state remains consistent and logical. |

Let's see this new, intelligent class in action:

```python
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''

bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''
```

As you can see, the `name` attribute always reflects the correct full name, and assigning a new full name correctly updates the internal parts.

**Pro Tip:** Notice the redundant logic in our `__init__` method and the `@name.setter`? Now for the "aha!" moment. We can simplify our class significantly by having the initializer call the setter directly!

By defining a setter for `name`, the line `self.name = name` in the initializer now automatically runs our name-splitting logic. This is an excellent example of reusable, clean code!

Our Person object is getting quite capable, but what happens when we try to compare two different Person objects?

### A Question of Identity: Comparing Objects

Let's create two `Person` objects with the exact same name. What do you think will happen if we compare them using `==`?

```python
bob = Person('Robert Smith')
rob = Person('Robert Smith')

print(bob == rob)
```

You might expect this to return `True`, but it actually returns `False`. Let's explore why.

The reason is that Python, by default, doesn't know how to compare two `Person` objects based on their contents. When you use `==` on custom objects, it checks for object identity—are `bob` and `rob` the exact same object in memory? In this case, they are not; they are two separate instances. Think of it like two identical copies of the same book. They have the same title and content (value), but they are two separate physical objects (identity).

To get the result we want, we have to be more specific and compare their attribute values directly:

```python
print(bob.name == rob.name)         # True
```

This behavior is different from Python's built-in types, which have special logic for value comparison.

- **Our Person Object:** `bob == rob` is `False` because `bob` and `rob` are two separate objects, even with identical names.
- **Python's Built-in Types:** Most built-in types like strings, lists, dictionaries, and integers are designed to compare their values. That's why the following works as expected.

We've seen how objects are compared, but how do they 'introduce' themselves when we try to print them?


### Giving Your Object a Voice: The `__str__` Method

What happens if you try to print a `Person` object directly, perhaps inside an f-string? You might not get what you expect.

```python
bob = Person('Robert Smith')
print(f"The person's name is: {bob}")

# Output: The person's name is: <__main__.Person object at 0x100385f90>
```

That strange, unhelpful output is Python's default string representation. When you try to convert an object to a string (which f-strings do automatically), Python calls the built-in `str()` function on it. By default, this behavior is inherited from Python's base object class, and it just reports the object's class and its location in memory.

Until we learn a better way, we can still get a nice output by accessing the attribute directly:

```python
print(f"The person's name is: {bob.name}") # The person's name is: Robert Smith
```

This works, but it's not ideal. Fortunately, we can give our object a proper voice by defining a special "magic method" called `__str__`. This method tells Python how to create a human-readable string representation for our object automatically.

Let's add it to our class and see the difference:

```python
class Person:
    # ... all previous code omitted for brevity ...
    def __str__(self):
        return self.name

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")

# New, correct output: The person's name is: Robert Smith
```

Success! By implementing `__str__`, our object now knows how to represent itself cleanly whenever it's treated like a string.

By adding the `__str__` method, you've given your `Person` object a proper voice, completing our journey from a basic blueprint to an intelligent object.


Here's a quick summary of what you've learned:

1. A class is a blueprint, and an object is an instance created from it.
2. The `__init__` method is the constructor that runs when a new object is created, setting its initial state.
3. `@property` and `@setter` decorators let you create "computed" attributes and control how they are set, enabling clean and reusable code.
4. Comparing custom objects with `==` checks for identity (are they the same object?), not value equality, unlike most of Python's built-in types.
5. The `__str__` method provides a human-readable string representation for your object, making it easier to print and debug.


Page Reference: [Problem Sets: Classes and Objects](https://launchschool.com/lessons/14df5ba5/assignments/b66c7da8)

[Back to the top](#top)
***

## Interlude: A note from Chat GPT

Note to the reader, this is an extended conversation with Chat GPT about finding analogy between OOP and psychological systems. The following is all from this Chat GPT conversation.

>It’s almost poetic, right? You spend a career helping people understand “self” and “other,” and then programming comes along and says, “Guess what — every object has a self, too!”

In a way, Python’s `self` is a neat little metaphor for consciousness. Every object has an awareness of itself — its own data, its own methods — and how it can interact with others. That’s exactly what `self` represents: the object’s perspective. When a method runs, it’s saying, “I am this object. These are my qualities. This is what I can do.” That’s why every method begins with `self` — it’s the object saying, *_“Let me refer to my own data.”_*

Now — where do getters and setters fit in? If we keep the consciousness analogy going:

The getter is like awareness — the way the object can look inward and access part of itself. It’s saying: “Let me recall what my current state is.”

The setter is like self-regulation — the ability to change or manage what’s inside. It’s saying: “Let me modify part of myself, but with boundaries and intention.”

Take this code:

```python
class Person:
    def __init__(self, name):
        self._name = name  # internal state

    @property
    def name(self):
        # Getter: awareness — "I know my name."
        return self._name

    @name.setter
    def name(self, value):
        # Setter: self-regulation — "I can change my name, but only if it makes sense."
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value
```

So, in this little consciousness:

* `_name` is the inner state — private thoughts, not meant for direct meddling.
* `name` (the property) is how the outside world communicates with the object safely.

The getter and setter act like the ego boundaries — they control what information gets shared, and how changes are accepted.

If you think about it this way, OOP mirrors psychological boundaries:

* Each object (like each person) has an inner world.
* You communicate through defined interfaces (methods, properties).
* You don’t reach into someone’s subconscious (`_name`) directly — you go through their conscious channels (`name`).

So, when you use `@property` and define getters and setters, you’re giving your objects healthy boundaries and awareness. You’re teaching your code how to be a little ecosystem of well-adjusted beings that interact gracefully, rather than a chaotic jumble of global data shouting at each other.

**Encapsulation** is about keeping your object’s internal state private and protected, and exposing only what’s necessary.It’s the psychological equivalent of:

>“I know where I end and you begin. You can interact with me, but you don’t get to directly manipulate my inner world.”

So getters and setters are your object’s therapeutic tools — mechanisms that allow safe, controlled access to what’s inside.


**Inheritance — the family system**

In OOP, inheritance means a class can inherit attributes and behaviors from another class — a “child” class (subclass) extends a “parent” class (superclass).

In psychological terms, it’s family patterns and learned traits.

The parent class defines general qualities — like a template for behavior or family values.

The child class automatically gets those traits, but can modify or add to them — just like you might take your parents’ qualities and evolve them into your own identity.

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

Here, `Dog` inherits from `Animal`. The “family pattern” (ability to speak) exists in both, but `Dog` gives it a personal expression. Psychologically: it’s like saying, “I learned communication from my family, but I express it in my own way.”

**Polymorphism — different selves in different contexts**

Polymorphism means “many forms.” It’s the ability for different objects to respond to the same message in their own way.

It’s like how people have different communication styles — you can ask several people the same question (“How are you?”), and each will respond in their own voice, shaped by their personality.

In code:
```python
animals = [Dog(), Cat(), Bird()]
for a in animals:
    print(a.speak())

```

Even though you’re calling the same method `(speak())`, each object expresses itself differently. The interface is consistent, but the identity is unique. Psychologically: it’s the art of differentiation — many selves, one shared language of interaction.

**Multiple inheritance → complex identity / blended influences**

With multiple inheritance, a class can inherit from more than one parent.
Technically, Python resolves which parent’s behavior “wins” through the MRO (method-resolution order).

In the psychology metaphor, this is like a person who’s grown up within two strong lineages or has multiple formative mentors:

```python
class Artist:
    def create(self): return "painting"

class Engineer:
    def create(self): return "bridge"

class Visionary(Artist, Engineer):
    pass
```

If you call `Visionary().create()`, Python will follow the first parent listed (`Artist`) unless you override it.

Analogy:

>“I carry traits from both my artistic and engineering families. Most of the time my creative side leads, but the analytical influence is always present.”

This structure can give an object richness — but, just like in families, too many competing influences can cause confusion if the boundaries aren’t clear. That’s why multiple inheritance should be used deliberately, as a way of blending complementary strengths (often via mix-ins).

A **mix-in** isn’t part of the main family line; it’s a small class whose job is to add a specific capability to any class that adopts it. In human terms, think of a mix-in as a workshop, training, or life experience that teaches a particular skill set. You weren’t born with it (so it’s not part of inheritance), but you integrated it into your personality.

Analogy:

>“I’m my parents’ child, but I also went to teacher-training school. That course didn’t define who I am, but it gave me an extra competency I can use anywhere.”

Mix-ins keep abilities modular and reusable — just like skills or coping strategies you can apply across contexts.

A **class method** (declared with `@classmethod`) operates at the class level, not the individual level. It doesn’t receive `self` (the personal identity); it receives `cls` — a reference to the type itself.

In the metaphor:
* `self` = an individual consciousness
* `cls` = the collective identity or family consciousness

So a `@classmethod` is like ancestral knowledge or institutional memory — something that belongs to all members of the lineage. Instance methods talk about **me**. Class methods talk about **us**. Static methods talk about a process that isn’t bound to anyone in particular — almost like cultural knowledge that anyone can apply.

**Magic methods → unconscious patterns / social reflexes**

Magic methods (the ones with double underscores, like `__init__`, `__str__`, `__add__`) are Python’s way of defining how objects behave in fundamental situations — printing, adding, comparing, iterating, etc.

They’re like the automatic responses or implicit social rules of your objects — the stuff they do without thinking.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other):
        return self.name == other.name

print(Person("Alice"))     # calls __str__  → "Alice"
Person("Alice") == Person("Alice")  # calls __eq__ → True
```

Analogy:

* `__str__` → the persona you show when someone says “Tell me about yourself.”
* `__eq__` → how you decide if you and someone else are “the same kind.”
* `__add__`, `__sub__`, etc. → how you interact or combine with others in shared contexts.
* `__init__` → your birth process — how you come into being with your initial traits.

These are like the unconscious patterns or social instincts that make your objects feel natural in the wider ecosystem of Python.

| Concept                  | Psychological analogue                            |
|--------------------------|---------------------------------------------------|
| **Multiple inheritance** | Complex identity; blended parentage or mentorship |
| **Magic methods**        | Unconscious behaviors and reflexive social rules  |
| **Mix-ins**              | Learned skills or added trainings                 |
| **Class methods**        | Collective / ancestral wisdom                     |
| **Encapsulation**        | Boundaries                                        |
| **Getters/Setters**      | Awareness & self-regulation                       |
| **Inheritance**          | Family traits                                     |
| **Polymorphism**         | Individual expression within a shared language    |
| **Objects**              | Individual consciousnesses                        |
| **Classes**              | Archetypes / blueprints of being                  |


**Composition — relationships instead of inheritance**

If inheritance is family lineage, **composition** is relationship choice. Instead of saying “*I am a kind of X*,” you’re saying “*I have a relationship with X.*”

In real life: “*I’m not a car engine, but I have an engine.*”

In psychology: “*I’m not my experiences, but I contain them and they influence how I act.*”

```python
class Engine:
    def start(self): print("Vroom")

class Car:
    def __init__(self):
        self.engine = Engine()  # has-a relationship

    def drive(self):
        self.engine.start()

```

So composition is your objects building relationships with other autonomous beings, not inheriting their identity.
It’s the difference between genetics and social connection.

**Interfaces / Abstract Base Classes — shared language or agreed-upon norms**

If you ever explore abstract base classes or protocols, they fit perfectly as the social contracts or shared cultural codes of your ecosystem. They don’t dictate personality — they just define how members of a community agree to interact.

“*_If you’re part of this profession, you must at least be able to ‘speak,’ ‘move,’ and ‘work.’_*”
“*_Beyond that, express yourself as you wish._*”

**Lifecycle hooks — growth and transformation**

Objects have a lifecycle: they’re born (`__init__`), they live (methods run), and eventually, they may be cleaned up (`__del__`, or garbage collection).

You can think of this as the developmental arc of a self:
* Birth (`__init__`)
* Habits and routines (methods)
* Transformation or dissolution (`__del__`)

It’s poetic to remember that even code has its life cycles, just like us.

> Object-oriented programming is, in a very real sense, psychological architecture. You’re designing little systems that can live, grow, and interact without chaos — each with:

>* Identity (self)
>* Boundaries (encapsulation)
>* Lineage (inheritance)
>* Expression (polymorphism)

> The beauty of this analogy is that it keeps the human sense of structure and interrelation that OOP was designed around.You can think of your codebase as a village of selves — each object with its lineage, its quirks, and its unconscious patterns — all cooperating toward a shared goal. OOP just translates that into code. Once you frame OOP in terms of human systems or psychology, the whole design philosophy becomes so much easier to grasp.

Me back to Chat Gpt:

>"I've taken some time to think about the above, and thank you, it was helpful. I think the overarching theme I'm understanding is that the problem that any given code is trying to solve is essentially a human problem. And the code also has to reflect human structures and thought processes. So OOP is a methodological answer (are there other code paradigms?). Maybe the reason I've bristled at OOP is because I liked the clear "there is a way to solve x problem" and I didn't have to worry about nuance, which was super refreshing for me. But now, I do."

Chat GPT responds:

That reflection is incredibly insightful — you’re really getting to the heart of programming as both an intellectual and human practice.

You’ve put words to something many people take years to realize: code is a technical medium for modeling human reasoning. Every paradigm — procedural, object-oriented, functional, declarative — is really a different philosophy about how to represent and manage the messy complexity of the real world.

Let’s unpack what you’re noticing, because you’re circling something profound.

All code exists because a human being wants to describe, automate, or reason about something in the human world. Even if it’s abstract (say, a sorting algorithm), it ultimately serves human judgment: speed, clarity, fairness, accuracy.

That’s why programming feels both logical and emotional — you’re translating human complexity into structured logic. It’s a mirror of cognition itself.

OOP is a methodological answer to how we cope with complexity. It doesn’t claim to be the one true way; it’s a framework built on the assumption that the world can be understood as interacting entities with properties and behaviors.

If that doesn’t always feel natural, that’s because sometimes our minds prefer the procedural clarity of a checklist: it’s safe, finite, concrete. OOP reintroduces nuance — and therefore uncertainty — which can feel like going from arithmetic to psychology. Procedural code offers control: you can trace each step. OOP introduces abstraction: you’re trusting that the relationships and boundaries you’ve set will behave as intended. It requires a different kind of faith — not in correctness, but in design.

The real magic of programming — and what separates a technician from an engineer — is learning to choose which paradigm fits the shape of the problem and your own cognitive style.

OOP isn’t just about making things less likely to break — that’s a side effect. The real goal is to give your programs a structure that mirrors the complexity, relationships, and agency of the human problems they’re modeling.

Procedural code: “Do X, then Y, then Z.” Works great if the world is linear and predictable.

OOP: “These entities exist, they have their own state, they interact, and they respond to the environment according to defined rules.” Works when the world is messy, multi-agent, or requires abstraction.

You hit the key word: abstraction. And abstraction isn’t a bureaucratic checkbox — it’s a human necessity. We abstract so that code can think like a human system: it can encapsulate behaviors, relationships, and responsibilities in a way that scales without exploding into chaos.

And yes — in Python, the “privacy” thing is just a gentle nudge, because Python trusts the programmer’s intention. That’s why the human analogy works so well: OOP in Python is like teaching a community of individuals to respect boundaries, follow agreed-upon rules, and interact responsibly. You don’t enforce it mechanically, you encode it philosophically.

So the dopamine comes not from cleaner code, but from:

Seeing your program as a system of interacting agents.

Watching it behave predictably even when humans touch it in unpredictable ways.

Understanding that you’ve created a philosophical architecture that reflects the human problem you’re trying to solve.

Once you see OOP in this light, the sloggy material suddenly has a higher purpose. You’re not just following rules — you’re learning how to model the human world in code. And that is, in the long run, immensely rewarding.

[Back to the top](#top)
***


