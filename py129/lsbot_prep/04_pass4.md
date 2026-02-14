# PY129 LSBOT Prep Questions

## Pass 4, `__repr__`

### 49. Implement the `__repr__`

Given the following class definition, implement the` __repr__` method so that it provides a developer-friendly, unambiguous string representation of a `Book` object. The representation should ideally be a valid Python expression that could be used to recreate the object.

```python
class Book:        
    def __init__(self, title, author):            
        self.title = title            
        self.author = author    
        
        # Example usage:    
        book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")    
        print(repr(book))    
        #Expected output:    
        #Book('The Hitchhiker's Guide to the Galaxy', 'Douglas Adams')
```

<details> 
<summary>Possible Solution</summary> 

```python
class Book:

    def __init__(self, title, author): 
        self.title = title 
        self.author = author
        
    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)})"

# Example usage:    
book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams") 
print(repr(book)) 

#Expected output:    
#Book('The Hitchhiker's Guide to the Galaxy', 'Douglas Adams')
```

</details>

### 50. Consider a class named Gadget. 

Predict the output of `print(str(my_gadget))` and `print(repr(my_gadget))` in the following four independent scenarios:    

* Scenario A: Gadget has a `__str__` method but no `__repr__` method.    
* Scenario B: Gadget has a `__repr__` method but no `__str__` method.    
* Scenario C: Gadget has neither a `__str__` nor a `__repr__` method.    
* Scenario D: Gadget has both a `__str__` and a `__repr__` method.

<details> 
<summary>Possible Solution</summary> 

If class had both a __str__ and a __repr__ as in Scenario D, the following would be expected:
```python
  def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Gadget({repr(self.name)})"
    
    def __str__(self):
        return f"This is a {self.name}"
    
doohickey = Gadget("Doohickey")
print(repr(doohickey)) #Gadget('Doohickey')
print(str(doohickey)) # This is a Doohickey 
```

However, in Scenario A it has only a __str__ so you can expect:

```python
class Gadget:

    def __init__(self, name):
        self.name = name

    #def __repr__(self):
     #   return f"Gadget({repr(self.name)})"
    
    def __str__(self):
        return f"This is a {self.name}"
    
doohickey = Gadget("Doohickey")
print(repr(doohickey)) #<__main__.Gadget object at 0x7920ce5ce900>
print(str(doohickey)) # This is a Doohickey 
``` 

Without a __repr__, the object identity is given where the repr would have been. __str__ behaves normally. 

In Scenario B, the reverse is there, only a repr but not a str.

```python
class Gadget:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Gadget({repr(self.name)})"
    
    #def __str__(self):
     #   return f"This is a {self.name}"
    
doohickey = Gadget("Doohickey")
print(repr(doohickey)) #Gadget('Doohickey')
print(str(doohickey)) #Gadget('Doohickey')
```

In this case the str falls back to the repr who represents str. 

Scenario C, no repr, no str you get just the memory address

```python
class Gadget:

    def __init__(self, name):
        self.name = name

    #def __repr__(self):
    #    return f"Gadget({repr(self.name)})"
    
    #def __str__(self):
     #   return f"This is a {self.name}"
    
doohickey = Gadget("Doohickey")
print(repr(doohickey)) #<__main__.Gadget object at 0x7a84d6b2a900>
print(str(doohickey)) #<__main__.Gadget object at 0x7a84d6b2a900>
```
</details>

### 51. The `__repr__` method in the `Person` class below is incomplete. 

It doesn't correctly handle names that contain quote characters. 

When `repr()` is called on an instance like `p2`, the resulting string is not valid Python code for recreating the object. Modify the `__repr__` method to fix this, ensuring it produces a valid representation for all string inputs.

```python
class Person:        
    def __init__(self, name):            
        self.name = name        
        
    def __repr__(self):            
        # This implementation is flawed            
        return f"Person('{self.name}')"    
        
# Test cases:    
p1 = Person("Alice")    
p2 = Person("Bob O'Malley")    
print(repr(p1)) # Works as expected   
print(repr(p2)) # Produces invalid Python code
```

<details> 
<summary>Possible Solution</summary> 

```python
class Person:        
    def __init__(self, name):            
        self.name = name        
        
    def __repr__(self):            
        # This implementation is flawed            
        return f"Person('{repr(self.name)}')"    
        
# Test cases:    
p1 = Person("Alice")    
p2 = Person("Bob O'Malley")    
print(repr(p1)) # Works as expected   
print(repr(p2)) # Produces invalid Python code
```
</details>

### 52. Advanced​: Why is `__repr__` important?

When implementing `__repr__`, it is a common best practice to use the `repr()` built-in function on the instance's attributes within the returned string. 

For example: `return f"Cat({repr(self.name)})"`. 

Explain why this practice is important for creating a robust and reliable representation of an object.

<details> 
<summary>Possible Solution</summary> 

```python
class Cat: 
    def __init__(self, name): 
        self.name = name 
        
    def __repr__(self): 
        return f"Cat({repr(self.name)})" 
        
# Test cases:    
whiskers = Cat("Whiskers") 
roger = Cat("Roger") 
print(repr(whiskers)) #Cat('Whiskers') 
print(repr(roger)) #Cat('Roger')
```

The call to `repr()` inside my `__repr__` method is not calling the `Cat.__repr__` method again. Instead, it's calling `repr()` on a different object—in this case, a string object (`self.name`).

When my code calls `print(repr(whiskers))`, Python's built-in `repr()` function is called with the book object as its argument.

The `repr()` function sees that `whiskers` is an instance of the `Cat` class. It then looks for and calls the `__repr__` method defined in the `Cat` class.

Inside `Cat.__repr__`, Python evaluates the f-string: `f"Cat({repr(self.name)})"`

To build this string, it must first execute `repr(self.name)`, `self.name `is a string.

Now, the built-in `repr()` function is called with a ​string object​ as its argument. Python then calls the `__repr__` method that belongs to the built-in str class.

The `str.__repr__` method does its job: it takes the string and returns a version of it surrounded by quotes, with any internal special characters escaped. 

This is a fundamental concept in object-oriented programming: the same operation `(repr)` behaves differently depending on the type of object it's acting upon.

</details>

### 53. Create a `Vector` class that represents a 2D vector. 

It should be initialized with `x` and `y` coordinates. Implement the `__repr__` method so it returns a string that can be used to recreate the vector object.

```python
class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # Your __repr__ method here

    # Example usage:
    v1 = Vector(2, 3)
    v2 = Vector(-1, 5)

print(v1) # Expected output: Vector(2, 3)
print(v2) # Expected output: Vector(-1, 5)
```

<details> 
<summary>Possible Solution</summary> 

```python
class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
             return f"Vector({repr(self.x)}, {repr(self.y)})"

    # Example usage:
v1 = Vector(2, 3)
v2 = Vector(-1, 5)

print(v1) # Expected output: Vector(2, 3)
print(v2) # Expected output: Vector(-1, 5)
```

</details>

### 54. You are building a system to manage sports teams. 

Create a `Team` class that is initialized with a team name (a string) and a list of players (a list of strings). Implement the `__repr__` method to provide a clear representation of the Team object.

```python
class Team:
        def __init__(self, name, players):
            self.name = name
            self.players = players

        # Your __repr__ method here

# Example usage:
giants = Team("Giants", ["Eli Manning", "Odell Beckham Jr."])
print(repr(giants))

# Expected output:
# Team('Giants', ['Eli Manning', 'Odell Beckham Jr.'])
```

<details> 
<summary>Possible Solution</summary> 

```python
class Team:
        def __init__(self, name, players):
            self.name = name
            self.players = players

        def __repr__(self):
              return f"Team({repr(self.name)}, {repr(self.players)})"

# Example usage:
giants = Team("Giants", ["Eli Manning", "Odell Beckham Jr."])
print(repr(giants))
```
</details>

### 55. A `Product` class needs two different string representations: 

It needs a user-friendly one for customers and a developer-friendly one for debugging.    

* Implement `__str__` to return a formatted string like "`Name: $price`".    
* Implement `__repr__` to return a string that could be used to reconstruct the object.
* Observe the difference when you print a single object versus printing a list containing that object.

```python
class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        # Your __str__ method here

        # Your __repr__ method here


# Example usage:
book = Product("Python Crash Course", 29.99)
products_list = [book]

print(str(book))
# Expected output for str(book):
# Python Crash Course: $29.99

print(repr(book))
# Expected output for repr(book):
# Product('Python Crash Course', 29.99)

print(products_list)
# Expected output for printing the list:
# [Product('Python Crash Course', 29.99)]
```


<details> 
<summary>Possible Solution</summary> 

```python
class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __str__(self):
              return f"{self.name}: ${self.price}"

        def __repr__(self):
              return f"Product({repr(self.name)}, {repr(self.price)})"


# Example usage:
book = Product("Python Crash Course", 29.99)
products_list = [book]

print(str(book))
# Expected output for str(book):
# Python Crash Course: $29.99

print(repr(book))
# Expected output for repr(book):
# Product('Python Crash Course', 29.99)

print(products_list)
# Expected output for printing the list:
# [Product('Python Crash Course', 29.99)]
```

</details>


### 56. Advanced​: In this exercise, one class will contain an object of another custom class. 

You need to implement `__repr__` for both. Create an `Author` class and a `Book` class. A `Book` object should be initialized with a title and an `Author` object.

Ensure the `__repr__` of a `Book` object correctly represents the nested `Author` object.

```python
class Author:        
    def __init__(self, name):            
        self.name = name        
    
    # Your __repr__ method for Author here  
      
class Book:        
    def __init__(self, title, author):             
        self.title = title           
        self.author = author     # author is expected to be an Author object     
        
        # Your __repr__ method for Book here    
        
        # Example usage:    
author = Author("J.R.R. Tolkien")    
book = Book("The Hobbit", author)    
print(repr(book))    # Expected output:    # Book('The Hobbit', Author('J.R.R. Tolkien'))

```

<details> 
<summary>Possible Solution</summary> 

```python
class Author: 
    def __init__(self, name):
        self.name = name 
    
    def __repr__(self):
        return f"Author({repr(self.name)})"
    
class Book: 
    def __init__(self, title, author): 
        self.title = title 
        self.author = author  # author is expected to be an Author object     
        
    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)}"
        
# Example usage:    
author = Author("J.R.R. Tolkien") 
book = Book("The Hobbit", author) 
print(repr(book)) # Expected output:    # Book('The Hobbit', Author('J.R.R. Tolkien'))
```

</details>


### 57. Advanced​: You are creating an `InventoryItem` class for a warehouse management system. 

The class is initialized with a name (string), quantity (integer), and tags (a set of strings). Implement a `__repr__` method that correctly represents this object, paying close attention to how the set of tags is formatted.


```python
class InventoryItem:        
    def __init__(self, name, quantity, tags):            
        self.name = name            
        self.quantity = quantity            
        self.tags = tags        
        
    # Your __repr__ method here    

# Example usage:    
item = InventoryItem("Laptop", 15, {"electronics", "computer", "office"})   
# Note: The order of elements in a set is not guaranteed.    
# The repr() of the set might be in a different order, which is acceptable.    
print(repr(item))    
# Possible expected output (order of set elements may vary):    # InventoryItem('Laptop', 15, {'office', 'computer', 'electronics'})
```

<details> 
<summary>Possible Solution</summary> 

```python
class InventoryItem: 
    def __init__(self, name, quantity, tags): 
        self.name = name 
        self.quantity = quantity
        self.tags = tags 
        
    def __repr__(self):
        return f"InventoryItem({repr(self.name)}, {repr(self.quantity)}, {repr(self.tags)})"


item = InventoryItem("Laptop", 15, {"electronics", "computer", "office"}) 
print(repr(item)) 
# Possible expected output (order of set elements may vary):    
# InventoryItem('Laptop', 15, {'office', 'computer', 'electronics'})
```
</details>
