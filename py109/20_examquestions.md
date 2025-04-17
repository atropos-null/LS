### Written Exam-Style Questions (14)


1. Explain the difference between mutable and immutable data types in Python. Provide examples of each.

2. What is the difference between `==` and `is` operators in Python? Provide an example where they give different results.

3.  ​Intermediate​: What will the following code print and why?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```
4.  Describe the concept of truthiness in Python. List at least 5 values that evaluate to False in a boolean context.

5.  What is the purpose of Python's list comprehension syntax? Rewrite the following code using a list comprehension:

```python
 numbers = [1, 2, 3, 4, 5]
   squared = []
   for num in numbers:
       if num % 2 == 0:
           squared.append(num ** 2)
```

6. Explain how variable scope works in Python. What is the difference between local and global variables?

7. What will the following code output and why?

```python
def outer():
    x = 10
    def inner():
        print(x)
    inner()
    x = 20
   
outer()
```

8. Explain the concept of pass-by-reference vs. pass-by-value in Python. How are arguments passed to functions in Python?
9. What is the purpose of the `enumerate()` function? Provide an example of how it might be used in a for loop.

10. Debug the following code. What is the issue and how would you fix it?
```python

    def calculate_total(items):
        total = 0
        for item in items:
            total += item['price']
        return total
    
    products = [
        {'name': 'Apple', 'price': 1.20},
        {'name': 'Orange', 'price': 0.85},
        {'name': 'price': 2.50}
    ]
    
    print(calculate_total(products))
    
```
11. Explain the purpose of Python's try/except statement and how it's used to handle exceptions.

12. What does the `*args` and `**kwargs` syntax mean in function definitions? Provide an example of a function that uses both.

13.  How do you convert between different data types in Python? Provide examples of converting:
    - A string to an integer
    - An integer to a string
    - A string to a list
    - A list to a string


14. What are Python modules and how do you import them? Describe different ways to import modules and the differences between them.

### Verbal Exam-Style Questions (6)

1.  Describe how strings work in Python. What are some common string methods, and how would you perform basic string manipulation?
2. Explain how dictionaries work in Python. What are their key characteristics, and how do they differ from lists?
3. Explain how Python's variable assignment works. What happens when you assign a value to a variable, and how does this differ between mutable and immutable objects? Provide examples to illustrate your explanation.
4. What are the main control flow structures in Python? Provide examples of when you would use each one.
5.  Explain how functions work in Python. What is a function definition vs. a function call? How do you use return values?
6.  Walk me through how you would debug a Python program that's producing unexpected output. What tools and techniques would you use?