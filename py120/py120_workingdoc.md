# Python 120 Working Document

<a name="top"></a>

## Notes from Object Oriented Programming with Python Book

- [Notes from Object Oriented Programming with Python Book](#notes-from-object-oriented-programming-with-Python-Book)
- [Flexible by Design: Advocating Composition Over Inheritance in Python](#flexible-by-design-advocating-composition-over-inheritance-in-python)

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

- **Semantic Naming:**  
  Classes are nouns (e.g., `Character`). Methods represent actions (verbs), e.g., `move()`, `attack()`.

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

To make custom objects behave like native types, implement dunder ("double underscore") methods.

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

***

### Conclusion

While classical inheritance is a fundamental concept in object-oriented programming and a useful tool for modeling stable, clear hierarchies, it is not a universal solution. This paper has argued that the "Composition Over Inheritance" principle should be the default guiding philosophy for building robust, scalable, and maintainable software in Python. By favoring "has-a" relationships over "is-a" relationships, we design systems with loosely coupled components, clear separation of concerns, and enhanced flexibility. Embracing composition and its related patterns, such as mix-ins and delegation, leads to systems that are not only easier to reason about and test but are also fundamentally more adaptable to the inevitable reality of future change.

[Back to the top](#top)
***