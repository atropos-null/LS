#PY120 Questions and Answers

<details>
<summary>Show answer</summary>
</details>

### What was the primary motivation for the creation of Object-Oriented Programming (OOP)?

<details>
<summary>Show answer</summary>

The primary motivation for the creation of Object-Oriented Programming (OOP) was precisely to address the complexity and maintainability issues inherent in large programs.

As programs grow in size, they tend to become increasingly difficult to maintain. Without a disciplined structure, software often turns into "one big glob of interdependency and potential for breakage". In such a system, a change in one area can have unforeseen negative consequences—or "ripple effects"—across the entire code base, making development slow and risky.

**The OOP Solution: Modularity and Small Parts**

OOP addresses this by promoting a design philosophy where the entire program is built from smaller, self-contained units. The primary goal is to shift the focus from a single, interdependent entity to an interaction between these smaller parts.

These discreet chunks that OOP utilizes are primarily classes and the objects created from them.

1. **Classes (The Blueprints)**: A class is a blueprint that describes the characteristics of its objects. Classes typically represent concrete (non-abstract) things and are usually named using nouns. A class defines the behaviors for the instance objects of the class.

2. **Objects (The Chunks)**: An object is the product, or instance, of a class. Every object encapsulates two things that define its identity and functionality:
    ◦ **State**: This is the data inside the object, tracked by its instance variables.
    ◦ **Behavior**: These are the actions the object can perform, defined by its instance methods.

**Key Concepts Driving Modularity**

The ability of OOP to deliver modular, maintainable code relies on several fundamental principles:

1. **Encapsulation (Defining Boundaries)**
Encapsulation is the mechanism for hiding data and functionality from the rest of the code base. This is critical for modularity because it defines boundaries and interfaces. By hiding the internal implementation details of an object and only exposing a controlled interface (methods), encapsulation helps manage complexity as programs grow. It ensures that callers use the object's defined interface, meaning that the object's internals can change without ripple effects on the rest of the program, thus supporting safe refactoring.

2. **Inheritance (Promoting Code Reuse)**

Inheritance allows a class (the subclass) to acquire all the behaviors and properties of another class (the superclass). This directly supports maintainability and modularity by:
* Letting programmers define small, reusable classes that hold general, shared behaviors.
* Allowing subclasses to inherit common functionality without duplicating code.

3. **Polymorphism (Flexible Interfaces)**
Polymorphism is the ability for different data types (objects from different classes) to respond to the same interface.
* This principle enhances flexibility and modularity because code can interact with objects based on a common set of methods, even if the objects handle those methods in unique, specialized ways. For instance, a superclass might define a generic harvest() method, but subclasses like Tomato and Wheat can implement their own specific harvest() logic.

To think of this in an operational context, OOP is like designing a large ship by creating specialized, sealed compartments (objects) that interact through standardized procedures (interfaces/methods). If one compartment (module) fails or needs upgrading, you only need to work on that specific part, secure in the knowledge that its well-defined boundaries (encapsulation) prevent the problem from instantly sinking the entire vessel (the program).

</details>

### In OOP, what is the term for a single section with sub-functions that all produce the same type of data object?"

<details>
<summary>Show answer</summary>

A **class**.

Classes are defined as "a single section with sub-functions that all put out the same type of data object". "Every class defines a type, and every type has a class".
* Representation: Classes and the objects created from them typically represent concrete (non-abstract) things. They are conventionally named using Pascal case and are usually discussed using nouns.
* Behavior Blueprint: A class defines the behaviors for the instance objects of the class.

**The Result: The Object (Instance)**

The reason a class is structured as a single section that produces the same type of data object is that it allows for the consistent creation of objects, also known as instances or instance objects.
* Instantiation: Instantiation is the process of creating a new object from a class. When a new object is created from a class, this is referred to as creating a new class instance.
* Distinct Instances: You can instantiate multiple instances of a class. Importantly, these instance objects are distinct from each other.

**Components Within a Class** 
The "sub-functions" mentioned in the flashcard's definition are primarily the instance methods, which define the behavior of the objects the class produces. These behaviors manipulate the object's state (data).

**Initialization and the Constructor**
The process of producing a data object from a class involves a constructor and an initializer:

* **The Constructor**: The statement that creates the class instance, such as GoodDog(), is called the class constructor. The constructor orchestrates instantiation by first calling the static method __new__ (which allocates memory) and then calling the initializer.
* **The Initializer** (`__init__`): The `__init__` method, often called the initializer or instance constructor, initializes a new instance of an object. It does not create the object, but rather receives an already-created instance and initializes its state (e.g., setting instance variables like self.name). Putting setup logic in `__init__` ensures every instance is fully initialized at creation time and always in a valid, uniform state.

The fact that classes define a fixed set of state attributes and behaviors (methods) ensures that all resulting objects of that class are of the same type and operate consistently, achieving the goal of making large programs modular.

</details>

### What is the product of a class called?

<details>
<summary>Show answer</summary>

An object. Also known as an instance.
</details>

### What is the convention casing style for naming classes in Python?


<details>
<summary>Show answer</summary>
PascalCase.
</details>

### "Classes and objects typically represent _____ (nouns/verbs), while many methods represent _____ (nouns/verbs)."

<details>
<summary>Show answer</summary>

Classes and objects represent nouns, while many methods represent verbs (actions). Classes and the objects created from them are fundamentally conceptualized as nouns because they represent the "things" or entities within a program. OOP supports abstraction by encouraging you to think in terms of nouns (objects). The objects created from classes are specific instances of the class nouns.

Methods are the functions defined within a class that allow objects to perform actions or manipulate their internal data. Therefore, methods are naturally associated with verbs. Many, but not all, methods are named with verbs because they represent actions and behaviors.

</details>

### "What is the term for the process of creating a new object from a class?"

<details>
<summary>Show answer</summary>

"Instantiation."

1. ** Defining Instantiation and Its Product**

Instantiation is defined as the process of creating a new object.

**The Product**: The object created through this process is the product of a class. Objects are also referred to as instances or instance objects. When a new object is created from a class, "we say that we created a new class instance". Objects and instances are often interchangeable terms.

2. The Mechanics of Instantiation (The Constructors)

The process of creating and initializing an instance object is orchestrated by two primary methods: the class constructor and the initializer method.

**The Class Constructor (The Orchestrator)**
* The statement that creates the class instance, such as GoodDog(), is called the class constructor.
* The constructor orchestrates the instantiation of an instance object.
* It performs the first step in instantiation by calling the static method `__new__`.

**The __new__ Method (Memory Allocation)**
* The `__new__` method is a static method that is called first.
* Its job is to allocate memory for the object and return an uninitialized object to the constructor.

**The `__init__ Method` (The Initializer)**
* The `__init__` method, which is a "magic method" (or dunder method), is properly called the initializer method or instance constructor.
* The uninitialized object returned by `__new__ `is then passed to `__init__`.
* The initializer receives an already-created instance and initializes its state. For example, it sets instance variables like `self.name`.
* Ensuring Validity: Putting setup logic in `__init__` ensures every instance is fully initialized at creation time—meaning "you can't forget to run setup"—so that objects are always in a valid, uniform state.

Instantiation is akin to pressing the "print" button on a 3D printer. The class is the digital file or design blueprint, which holds all the instructions. Instantiation is the act of running that process. The object (or instance) is the specific, tangible item that comes off the printing bed, fully assembled and ready to use, complete with its unique details (state) but adhering to the shared design functions (methods).

</details>

### "What is the OOP principle of hiding data and functionality from the rest of the code base, defining boundaries and interfaces?"

<details>
<summary>Show answer</summary>

"Encapsulation."

Encapsulation is the term for hiding data and functionality from the rest of the code base, defining boundaries and interfaces.

This principle is one of the pillars of Object-Oriented Programming (OOP) and is crucial for making large programs more modular and easier to maintain, as it prevents the code from becoming "one big glob of interdependency and potential for breakage".

Encapsulation explicitly defines boundaries and interfaces. These boundaries help you manage complexity as programs grow.

Encapsulation supports abstraction by allowing you to think in terms of nouns (objects) and verbs (methods), rather than scattered implementation details. The internal workings (the data and helper logic) are hidden, and the external world only sees the defined actions (the methods).

It allows you to enforce invariants and refactor safely. Because callers rely solely on the object's defined interface (methods), the object's internals can change without ripple effects on the rest of the program.

In Python, encapsulation is implemented through convention rather than strict enforcement:

**Symbolic, Not Actual**: In Python, encapsulation is considered more symbolic than actual. It relies on the choice of the programmer not to have aspects interact, and it is not inherently "firewalled".

**Discouraging Direct Access**: Since Python does not prevent unrestricted access to instance variables, the simplest approach to discouraging users from modifying "private" attributes is to rely on a convention.

**The Underscore Convention**: The convention for marking instance variables and methods for internal use is by naming them with a single leading underscore (e.g., _name). This underscore signals to the user that they are playing with fire and messing with something they shouldn't.

**Controlled Access via Getters and Setters**: Because the underscore convention is only a warning and does not prevent access, a best practice for controlled encapsulation is to provide specific method interfaces through getter and setter methods. These are methods that provide controlled access to an object's attributes.

Encapsulation is like the dashboard and engine bay of a modern car. The engine and complex internal wiring (data and internal functionality) are hidden away and inaccessible to the driver, preventing accidental tampering. The steering wheel, gas pedal, and brake (methods/interfaces) are the only defined ways the driver (the rest of the code) is allowed to interact with the vehicle. This means the mechanics of the engine can be totally changed or refactored (e.g., swapping a combustion engine for an electric one), but as long as the dashboard controls (the interface) remain the same, the driver doesn't need to learn a whole new way to drive.

</details>

### The ability for different data types to respond to the same interface is known as _____.

<details>
<summary>Show answer</summary>

"Polymorphism."

Polymorphism (which literally means "many forms") is a core principle of Object-Oriented Programming (OOP) that enables code flexibility and promotes modularity by allowing various objects to be treated uniformly based on a shared set of behaviors.

Polymorphism is supported by inheritance, which lets programmers define small, reusable classes (like Plant) and smaller, more specific classes (like Tomato or Wheat) for fine-grained, detailed behaviors.

This flexible structure helps in OOP's primary motivation: to make large programs more modular and easier to maintain. By treating different objects through a single interface, you avoid the need for lengthy conditional checks (e.g., "if object is a Tomato, do this; if object is a Wheat, do that"), making the program less of "one big glob of interdependency and potential for breakage".

Polymorphism works like a universal remote control. The interface (the method name, like 'Play' or 'Power') is the same button on the remote, regardless of what device it's pointed at. Whether you point it at a DVD player, a TV, or a stereo (the different data types), the device responds to the same interface ('Play'), but the actual behavior (playing a movie, starting a broadcast, or spinning a CD) is specialized and unique to the object being commanded.

</details>

### In OOP, what principle allows a class to acquire all the behaviors and properties of another class?

<details>
<summary>Show answer</summary>

"Inheritance."

Inheritance establishes a relationship between two classes, creating a hierarchy.
* **Subclass (Inheriting Class)**: The class that acquires the behaviors and properties is called the subclass (or derived class).
* **Superclass (Inherited Class)**: The class whose behaviors and properties are acquired is called the superclass (or base class).
* **"Is-A" Relationship**: Inheritance describes the `"is-a"` relationship between classes. For example, if a Car class inherits from a Vehicle class, then a Car object is a Vehicle object, or a "Car is a Vehicle". 
* **Transitivity**: This relationship is transitive. If class Z subclasses class Y, and Y subclasses class X, then Z indirectly inherits from X, and a Z object is considered an instance of Z, Y, and X simultaneously.

**Why do this?**

**Code Reuse**: Inheritance allows subclasses to acquire all the common functionality from the superclass without duplicating code. For instance, a superclass like Pet can hold a general `__init__ `method, which is then used by subclasses like Dog and Cat.

**Specialization**: It allows programmers to define small, reusable classes for general, shared behaviors (the superclass) and then define smaller, more specific classes for fine-grained, detailed behaviors (the subclasses). Subclasses can add their own unique behaviors or override inherited ones to suit specific needs. For example, Dog and Cat inherit the general `__init__` from Pet but define their own specific speak methods.

Inheritance functions like a family tree in biological classification. The superclass (like "Mammal") provides the fundamental, shared characteristics—such as having hair and warm blood—that are automatically passed down. The subclass (like "Dog") automatically receives these core traits (acquiring behaviors and properties) but is free to add specialized characteristics, like barking and rolling over, without having to redefine what it means to be a Mammal.

</details>

### The data inside an object, collectively defined by its instance variables, is known as the object's _____.

<details>
<summary>Show answer</summary>

State.

State refers to the data associated with an individual class instance. Collectively, the data inside an object defines its state. An object's state is given by its instance variables, which are the variables that store the object's data. Instance variables keep track of information about the state of an object.

Instance variables live on each individual object, not the class, meaning they are not shared between instances. For example, self.name and self.age are instance variables, and every GoodDog object will have appropriate values for these variables. Two instances from the same class will have the same behaviors but may contain different states.

Instance variables can be initialized, accessed, replaced, or mutated through the class's instance methods and also from outside the class.

**Object Scope**: Every method can access the object's instance variables, but an object can only access its own state. We must access instance variables through the object reference, conventionally named self, because instance variables live on the object, not in the method's local scope.

**Initialization**: The state is typically initialized when an object is created. The `__init__` method (the initializer) receives an already-created instance and initializes its state. This setup ensures every instance is fully initialized at creation time so objects are always in a valid, uniform state.

</details>

### Functions that operate on instances of a class and are shared by all instances are called _____.

<details>
<summary>Show answer</summary>

Instance methods.

 Instance methods are often called behaviors. They represent actions and behaviors and are frequently named using verbs. Examples include `move()`, `attack()`, `gain_xp()`, `speak()`, and `roll_over()`.  Instance methods are functions that operate **on instances of the class** and are **shared by all class instances**. All instances of the same type can access the same methods.

 The Required self Parameter
A crucial characteristic of instance methods is the mandatory inclusion of the self parameter in their definition:
• Method Definition Requirement: When you define an instance method, you must include a parameter to receive the calling instance.
• Convention: By strong convention, this first parameter is always named self.
• The Calling Object: self always represents the object that the method was called on. Inside an instance method, self is the calling object, allowing you to invoke other instance methods on that same object with self.other_method(...).
3. How Instance Methods Access State
Instance methods are the primary way to access and modify an object's state (instance variables):
• Accessing Instance Variables: Instance variables (the object's state) live on the object itself, not in the method's local scope. Therefore, every method can access the object's instance variables.
• Using self: We must access instance variables through the object reference (self). For example, inside the speak method, self.name is used to access the instance variable belonging to that specific object.
• Automatic Passing: When you call the method on an instance (e.g., sparky.speak()), you don't provide an argument for the self parameter. Python automatically passes the instance object (sparky in this case) as the first argument. The call sparky.speak() is essentially syntactic sugar for GoodDog.speak(sparky).

Instance methods are the core building blocks that enable an object, the product of a class, to execute its defined functionality and interact with other objects in a modular system

</details>

### "What is the distinction between an 'instance variable' and an 'attribute' in Python?"

<details>
<summary>Show answer</summary>

"Instance variables are tied to an instance, whereas attributes include all instance variables and instance methods."

The term **attribute** serves as the collective name for all the capabilities and data points associated with an object. Attributes are the set of components that define an object's structure and functionality, encompassing both its data and its actions.
</details>

### "What is a 'property' in Python?"

<details>
<summary>Show answer</summary>

"A special kind of method that enables syntax that makes it look and act like an instance variable."

Properties are considered a more Pythonic way to create getters and setters. They are essential in Object-Oriented Programming (OOP) for maintaining encapsulation and providing a stable interface for managing an object's state.

Properties are primarily used to manage and control access to an object's internal state (its instance variables) while presenting a simple, variable-like interface to the user.

Properties allow you to retain the flexibility of getter and setter methods while giving callers a simple variable-access syntax. Even if the underlying logic changes later (e.g., the value is computed dynamically or fetched from elsewhere), the external code accessing obj.name does not need to change.

Read-Only Attributes: You can create a read-only attribute by having a getter decorated with `@property` without defining a corresponding setter. Trying to assign a value to a property without a setter will raise an AttributeError.

You should use properties in your Python classes when:
1. You want to strongly discourage misuse of the instance variables.
2. You want to validate data when your instance variables receive new values.
3. You have dynamically computed attributes (values that need to be calculated every time they are accessed).
4. You need to refactor your code in a manner incompatible with the existing interface.
5. You want to improve your code readability.

</details>

### "What is the special name for the initializer method in a Python class that sets the initial state of a new instance?"

<details>
<summary>Show answer</summary>

"The __init__ method."

The special name for the initializer method in a Python class that sets the initial state of a new instance is the `__init__` method. This method is central to the process of instantiation and ensuring that every object created from a class starts in a valid and functional condition.


1. **Terminology and Identity**
The `__init__` method is a magic method (or dunder method), which means its name begins and ends with a double underscore. Magic methods are called implicitly by Python in response to specific language constructs, such as object creation.
While it is frequently called the constructor, the source material suggests better names are the initializer method and the instance constructor.

2. **Role in Instantiation**
The `__init__` method is the final step in the process of creating a new object (instantiation). Importantly, the initializer doesn't create the object. Instead, it receives an already-created instance and sets up its data.

The full orchestration of object creation involves three steps:

**Class Constructor Call**: The statement that creates the class instance, such as `GoodDog()`, is called the class constructor.

**Memory Allocation (`__new__`)**: The constructor first calls the static method `__new__`. This method allocates memory for the object and returns an uninitialized object.

**State Initialization (`__init__`)**: The uninitialized object is then passed to the `__init__ `method, where it initializes its state (e.g., sets instance variables like `self.name`).

3. **Setting the Initial State**
The primary responsibility of `__init__` is to initialize the object's state. The object's state is defined by its instance variables, which store the object's data.

* Instance Variables: These variables, like `self.name` and `self.level` in a `Character` class, are created and assigned initial values within `__init__`.

* Ensuring Validity: Putting setup logic in `__init__` ensures every instance is fully initialized at creation time. This is important because it means "you can’t forget to run setup," ensuring that objects are always in a valid, uniform state.

* Explicit Data: It also makes required data explicit via `__init__`parameters.

4. Required `self` Parameter

Like all instance methods, `__init__` requires the special `self` parameter:
* The definition of `__init__` requires `self` to receive the calling instance.
* `self` automatically refers to the newly created object (the instance) that is being initialized.
* For example, in `__init__(self, name)`, `self` is the newly created GoodDog instance, and name is the argument provided when calling the constructor (e.g., 'Sparky').

5. **Interaction with Inheritance**

The `__init__` method also plays a key role in the inheritance hierarchy:

* If a subclass defines its own `__init__` method, it should almost always call `super().__init__` before it does anything else. This ensures that the superclass part of the object is fully initialized first, especially if the superclass requires initialization arguments.
* If a subclass omits the `__init__` method, Python automatically calls the `__init__` method from the superclass (if one exists).

The __init__ method is effectively the gatekeeper of object integrity, ensuring that when an object is manufactured (instantiated), it is immediately given its full identity (state) before it can be used by the rest of the program.
</details>


### "What does the self parameter in an instance method represent?"

<details>
<summary>Show answer</summary>

"It refers to the instance object on which the method was called."

`self` serves as the crucial link between the method (the behavior) and the specific object it is meant to operate on (the state).

The `self` parameter is the mechanism Python uses to ensure that an instance method always operates on the correct object.

Required Parameter: When you define an instance method (a function that operates on instances of the class), you must include a parameter to receive the calling instance.

* Convention: By strong convention, this first parameter is always named `self`.
* Consistency: The first parameter defined for any instance method always represents the calling object, no matter what name you use.

When you call the method on an instance, you don't provide an argument for the `self` parameter. Python handles passing the calling object to an instance method automatically. Because `self` refers to the current instance, it grants the method full access to everything belonging to that object.

In essence, `self` is the explicit pointer that ensures that when you instruct one specific object to perform an action  the method uses the object's unique data (state) to execute that shared action (behavior).

</details>

### "What is the purpose of the code `type(self).__name__` inside an instance method?"

<details>
<summary>Show answer</summary>

"To programmatically get the name of the instance's class as a string."

The overall effect of the line `type_name = type(self).__name__` is to effectively say: "Get the current object, find out its class, and then get the name of that class as a string."

Think of this code snippet as a library card scanner being used on a book (the object). The self is the book itself, type(self) is the scanner reading the ISBN to identify the book's category (the class), and `.__name__` is the system printing out the simple, human-readable name of that category, such as "Fiction" or "Biography" (the class name string).

</details>

### "An object's _____ refers to the methods and instance variables it can access."

<details>
<summary>Show answer</summary>

"scope"

Object scope determines all the functionalities (behaviors) and data (state) available to a specific instance of a class.
Object scope has two main components that define what the object can access:

1. **The Methods in the Class**: This component grants access to all defined behaviors. This includes any methods acquired by the class via inheritance or mix-ins. This ensures that an instance of a subclass can use methods defined in its superclass, fulfilling the `"is-a"` relationship.
2. **The Instance Variables Associated with the Object**: This grants access to the object's unique state. This includes any instance variables acquired via inheritance. Instance variables keep track of the object's state.

The nature of OOP ensures that objects can utilize their scope effectively to manage their state and execute behaviors:
* ** Accessing Behavior**: Any object can call any method the class provides. Instance methods are functions that operate on instances of the class and are shared by all class instances.
* **Accessing State**: Instance variables belong to the object, and every method can access the object's instance variables. However, an object can only access its own state.
* **The Role of `self`**: Inside an instance method, the required `self` parameter refers to the current instance object. It is through this `self` reference that the method accesses the object's state (e.g., `self.name`) and invokes other methods within its scope (e.g., `self.other_method(...)`).

Inheritance plays a significant role in expanding an object's scope. If a class D inherits from class B (D is the subclass, B is the superclass):

* The instances of D acquire the methods and properties defined in B.
* Even though instance variables cannot be technically inherited from the class, subclass objects acquire the same instance variables as superclass instances.
* The scope of an object is transitive: an instance of subclass Z is considered an instance of all its superclasses (Y and X) simultaneously, and its scope includes the methods and instance variables from all ancestors.

Object scope is like a character's inventory and skill list in a video game. The methods (skills like attack() or move()) are the actions the object knows how to perform, often gained through training (inheritance). The instance variables (items like health or experience) are the unique data points it carries. The object's scope defines the entire set of tools and data that character (the instance) can readily access and use in its immediate environment.

</details>

### "What are 'getter' and 'setter' methods in OOP?"

<details>
<summary>Show answer</summary>

"They are methods that provide controlled access to retrieve (get) and assign (set) an object's attribute values."

This practice is deeply rooted in the Object-Oriented Programming (OOP) principle of Encapsulation, which aims to hide data and functionality from the rest of the code base, thereby defining boundaries and interfaces.

In Python, instance variables can be reassigned or mutated directly from outside the class, as Python doesn't prevent unrestricted access. This lack of "guardrails" can lead to problems such as unexpected instance variable values, incorrect behavior, or unanticipated security problems.

To mitigate these issues, providing getter and setter methods is considered the next best approach to managing instance variables that a user might want to access or modify.

Getters and setters define the public interface through which an object's internal state (tracked by instance variables) is read or modified. Getters retrieve attribute values. They run when you read the attribute. Data flows from inside the object to the outside. Setters assign attributes to new values. They run when you assign a new value to the attribute. Data flows from outside the object to the inside.

Outside code uses the getter (e.g., name()) as the public way to read the value. This creates a stable interface, meaning you are free to change how the value is stored (e.g., rename the internal variable or compute it dynamically) without breaking external code (callers). Setters are critical because their logic allows you to validate the incoming value before updating the internal state. For example, a setter for age can check that the input is an integer and not negative, raising a TypeError or ValueError otherwise.

**Why is this helpful?**

* Read-Only Access: By exposing only a getter (and no setter), you communicate that the value should not be reassigned.
* Future Logic: You can easily add complex logic, transformation, caching, or logging to the methods later without changing callers.

While you can define explicit methods like `name()` and `set_name()`, Python offers a more elegant mechanism using the `@property` decorator:

* Properties are a special kind of method that enables syntax that makes the property look and act like an instance variable.
* The method decorated with `@property` becomes the getter.
* The associated setter method uses a secondary decorator (e.g., @name.setter).
* Using properties means you no longer need parentheses when accessing the getter (e.g., print(sparky.name) instead of sparky.name()) or when assigning values (e.g., sparky.name = 'Fido').

In summary, when instance variables are marked for internal use (often with a single leading underscore, e.g., self._name), getters and setters (or the more Pythonic properties) serve as the public, controlled interface that protects the object's integrity while providing flexible access to its state.

</details>

### "If a method name is decorated with @property, what is the name of the secondary decorator used to create its setter?"

<details>
<summary>Show answer</summary>

 "`@name.setter`"

The Role of the `@property Decorator` (**The Getter**)

The process starts by defining a method and decorating it with `@property`. This method serves as the getter for the attribute.

* **Functionality**: The method decorated with `@property` defines the mechanism for reading the attribute's value. Its job is to retrieve the underlying data, possibly format it, or compute it on the fly before returning it.

* **Syntax**: When the @property decorator is applied to a method named `foo`, Python recognizes that `foo` is now a property, and accessing `obj.foo` automatically triggers the getter method.

* **Creation of the Setter Decorator**: When you apply `@property` to a method (e.g., `name`), the `@property` decorator automatically creates a secondary decorator named `@name.setter`.

The Role of the `@name.setter` Decorator (**The Setter**)

The secondary decorator is then used to define the method that handles write operations (assignment) to the attribute. The method decorated with `@name.setter` is the setter. Its job is to validate the incoming value and then update the internal state (the instance variable). Data flows from outside the object to the inside. This method runs automatically anytime you use the assignment operator (=), like in sparky.name = 'Fido'.

Setters are essential for ensuring data integrity, as they allow you to check the data type or value (e.g., ensuring name is a string or age is a non-negative integer) and raise exceptions before updating the instance variable.

Although the getter and setter methods have the same name (e.g., name in the examples), the decorators make them distinct functionalities.

* **Getter (Reading)**: When you read the attribute (`print(sparky.name)`), the `@property` method runs.
* **Setter (Writing)**: When you assign to the attribute (`sparky.name = 'Fido'`), the `@name.setter` method runs.
The operations of the getter and setter are fundamentally different: the Getter reads internal state and returns a value, while the Setter receives an external value, validates it, and updates internal state.

This mechanism powerfully demonstrates that the getter and setter are separate functionalities. You can have a getter without a setter to create a read-only attribute. If the setter method is removed, trying to assign a new value will raise an AttributeError, while the getter functionality remains intact.

</details>

### "What decorator is used to define a class method in Python?"

<details>
<summary>Show answer</summary>

"`@classmethod`"

Class methods are class-level methods that provide general services for the class as a whole rather than the individual objects. Class methods are typically where you put functionality that doesn't deal with class instances. Since the method has no reason to use instance variables (the state of a specific object), a class method is used instead.

Class methods are defined using the `@classmethod` decorator. They have a unique requirement for their first parameter:

* **The `cls` Parameter**: The first parameter of a class method is conventionally named `cls`.
* **Reference**: This `cls` parameter always represents a class. It refers to the calling class.
* **Analogy to `self`**: The `cls` parameter is described as being "nearly identical to self in almost all respects," but it conventionally references a class rather than an ordinary object. Inside a class method, `cls` refers to the calling class, allowing you to access class variables with `cls.variable`.
* **Convention**: It is conventional to use `cls` when defining a class method, just as `self `is used for instance methods.

While class methods operate on the class, they can be called in various ways, though a specific convention is preferred.
You should usually use the class to invoke the method (e.g., `GoodCat.what_am_i()`).

Class methods are therefore the dedicated structure for encapsulating behaviors related to the class definition as a whole, allowing you to manage shared information (like a count of all objects) without having to rely on any single instance's state.

</details>

### "A _____ is a variable that is shared by the class and all of its instances."

<details>
<summary>Show answer</summary>

The variable that is shared by the class and all of its instances is correctly called a **class variable**. It is shared by the class and all of its instances. This means there is the same storage for every instance unless shadowed. A class variable is initialized at class definition time, in the class body (e.g., counter = 0 at the top of the class), these are often constants. It exists before any instances are created. Class variables capture information about the class, as opposed to instance variables, which capture information related to specific class instances. 

A class variable is like a community whiteboard in an apartment building. Everyone in the building (all the instances) sees and shares the same information written on that board (the class variable value), and the building management (the class) controls where the board is placed. If one tenant reads the total number of apartments (a class variable tracking instance count), they see the same total as every other tenant, because that number applies to the building as a whole, not just to their individual apartment (the instance variable).

</details>

### "What type of method belongs to a class but does not require access to any class or instance attributes, and thus has neither self nor cls as a parameter?"

<details>
<summary>Show answer</summary>

"A static method."

To define a static method, you use the `@staticmethod` decorator followed by a function definition that doesn't use a self or cls parameter. Static methods do not need access to any class or instance attributes. This is why they do not require the mandatory `self` (for instance attributes/state) or `cls` (for class attributes) arguments that other method types require. Static methods are primarily used for utility and helper functions associated with the class, but which are logically self-contained.

If there is a reasonable chance that a static method may one day require access to instance or class state, then the method may not be suitable for use as a static method, as it can't be easily converted to an instance method without requiring code changes elsewhere.

If a function performs a calculation or task that is logically related to the class but doesn't depend on the specific state of any object derived from that class (or the class itself), it is an ideal candidate for a static method.

A static method is like a calculator located in the main lobby of a large office building (the class). It's available for use by anyone in the building (all the instances and other methods), but to perform a calculation (the method's function), you don't need to know which floor you're on (`cls`) or the specific contents of your desk (`self`). The function is self-sufficient and universally useful, regardless of the user's specific identity or location within the building.


</details>

###  "The `__str__` dunder method is intended to return what kind of string representation of an object?"

<details>
<summary>Show answer</summary>

"A human-readable representation."

If you do not define `__str__`, printing the object will result in a default representation that is not very informative. It typically shows the class name and the object's memory address (e.g., `<__main__.Cat object at 0x...>`), providing "nothing about its actual state".

`__str__`: Human-readable representation, displaying output to the end-user (via `print()`, `f-strings`).
`__repr__`: Unambiguous, official representation, primarily used as developers and debugging tools, the goal of shich is to to return valid Python code that can recreate the object.

If a class defines `__repr__ `but not `__str__`, what happens when `str()` is called on an instance?: Python falls back to using the `__repr__` method."

When Python attempts to get a string representation of an object, it follows a specific search order to ensure it gets the best available representation:

1. Search for `__str__`: When `str(obj)` is called (or implicitly via `print()` or `f-strings`), Python first looks for a `__str__` method in the object's class.
2. Search Inheritance: If `__str__` is not found in the class, Python searches inherited classes for a `__str__` method.
3. Fallback to `__repr__`: If Python cannot find a `__str__` method anywhere in the class or its inheritance chain, it next looks for a `__repr__` method, using the same inheritance search mechanism.
4. Final Default: If neither `__str__` nor `__repr__ `is found, Python ultimately calls the base `object.__str__`, which returns a default, less informative string showing the class name and memory address.

It is crucial to note that this fallback is unidirectional: when a program calls `repr()` on an object, Python never searches for `__str__`. The fallback only happens when a string is requested for human consumption (`str()`) but the developer hasn't provided the intended human-readable representation (`__str__`).

</details>

### "What is a 'mix-in' in Python?"

<details>
<summary>Show answer</summary>

"A class, typically not instantiated, that provides a common set of behaviors (methods) to other unrelated classes through inheritance."

Mix-ins are an essential design pattern in Python, particularly because they offer a way to achieve code reuse and polymorphism without forcing rigid, artificial hierarchies onto unrelated classes.  

* Mix-ins are never instantiated. They are not meant to create objects themselves, but rather to be "mixed into" other classes. 
* Mix-ins are often described as interface inheritance because you are inheriting interfaces (behaviors), not object types. 
* Mix-ins are associated with the `"has-a"` relationship, as opposed to the `"is-a"` relationship used in standard inheritance. An object of class A is said to have the behaviors provided by the mix-in B.
* It is a common Python convention to name mix-in classes with a Mixin suffix (e.g., ColorMixin). This ensures that users of the mix-in know that it is a mix-in, not an ordinary class that can be instantiated.

Using mix-ins in preference to deep inheritance trees is considered safer and more flexible. This pattern clearly separates concerns (a car is a vehicle, color a car could be is separate) and handles scalability issues more elegantly than complex multiple inheritance or rigid single inheritance.

</details>

### "Given that `Car` and `Truck` both inherit from Vehicle, why does isinstance(car, Truck) evaluate to False?"

<details>
<summary>Show answer</summary>

"Because `Car` and `Truck` are separate 'sibling' classes in the hierarchy; inheritance only goes up towards the superclass, not sideways."

Inheritance defines an `"is-a"` relationship between classes. This relationship establishes a hierarchy where an instance of a subclass is also considered an instance of all its superclasses.

* **Upward Inheritance**: Inheritance relationships are transitive and move up the hierarchy towards ancestors (superclasses).
* **Example**: Given the hierarchy where both `Car` and `Truck` inherit from `Vehicle`, a `Car` object is a `Car`, and it is also a `Vehicle`. Similarly, a `Truck` object is a `Truck`, and it is also a Vehicle.

`Car` and `Truck` are often referred to as sibling classes because they share the same direct parent (`Vehicle`) but have no direct inheritance relationship with each other.

* No Sideways Inheritance: Inheritance only flows in one direction—up the hierarchy.
* Lack of Connection: Even though both classes inherit from `Vehicle`, their shared parent doesn't make them instances of each other. A `Car` object is not a `Truck`.


</details>

### "What is the term for the distinct lookup path Python follows to find a method in an inheritance hierarchy?"

<details>
<summary>Show answer</summary>

"Method Resolution Order (MRO)."

The search path is determined by a complex, modified "depth first" search that considers all classes listed in the inheritance hierarchy.

* **Left-to-Right Search**: The MRO is determined by going through the items in the inheritance list from left-to-right.
* **Exploring Ancestors**: For each item in the inheritance list, Python explores all of that item's superclasses and mix-ins.
* **Mix-ins**: Mix-ins, which provide common sets of behaviors to other unrelated classes, are included in the search path. The search considers all items listed in the inheritance list, even those that are being used as mix-ins. In the pseudocode provided, mix-ins are explored before moving up to the superclass.

* **Ultimate Superclass**: Every Python class ultimately inherits from the object class, which is included as the final class in the MRO list (except for object itself, which has no superclass). The search continues until the method is found or the object class has been searched without finding the method.

**How to View the MRO**

The MRO is a class method defined by the type metaclass, which is the class that creates other classes. Developers can view the precise lookup path by calling the `.mro()` method on a class (e.g., `Human.mro()`). The output is a list showing the ordered sequence of classes that Python will search.

**Importance in Inheritance and super()**:

The MRO is vital for method overriding and the functionality of `super()`. When a subclass overrides a method present in a superclass, Python uses the MRO. It checks for the method in the current class first; if it finds one, it invokes that method instead of checking the superclass.

The **super()** function relies entirely on the MRO to return a placeholder object (a proxy object) that allows you to call methods from the next class in the MRO that contains the desired method. This is essential for ensuring that base functionality is initialized or executed before subclass specialization.

The MRO acts as the map or blueprint for the inheritance chain, defining the rules Python must follow to maintain consistent behavior and resolve potential conflicts (especially in multiple inheritance) by ensuring methods are found in a deterministic order.


</details>