1. Write a program that asks the user for two numbers and divides the first number by the second number. Handle any potential `ZeroDivisionError` or `ValueError` exceptions (there is no need to retry inputs in this problem).

```python

try:
    num_a = int(input("First number: "))
    num_b = int(input("Second number: "))
    result = int(num_a / num_b)
    print(f"The value is {result}")

except ValueError:
    print("An integer please")   

except ZeroDivisionError:
    print("The second number has to be greater than 0")
```

2. Expand your answer to the previous program so it prints the result only when no exceptions are raised. You should also print End of the program regardless of whether an exception is raised.

```python

try:
    num_a = int(input("First number: "))
    num_b = int(input("Second number: "))
    result = int(num_a / num_b)
    
except ValueError:
    print("An integer please")   

except ZeroDivisionError:
    print("The second number has to be greater than 0")

else:
    print(f"The value is {result}")

finally:
    print("The End")

```

3. Modify your answer to the previous problem so it handles both `ZeroDivisionError` and `ValueError` with a single exception handler. The output for both exception types can be obtained from the exception object.

```python

try:
    num_a = int(input("First number: "))
    num_b = int(input("Second number: "))
    result = int(num_a / num_b)
  
except (ValueError, ZeroDivisionError) as e:
    print(e)

else:
    print(f"The value is {result}")

finally:
    print("The End")
```

4. Write a program that asks the user for a number. If the input isn't a number, let Python raise an appropriate exception. If the number is negative, raise a ValueError with an appropriate error message. If the number isn't negative, print a message that shows its value.

```python
num = int(input("Give me a number: "))
if num < 0:
    raise ValueError("The number has to be greater than 0")
print(f"The value is {num}")
```

5. Modify your answer from the previous problem to raise a custom exception named `NegativeNumberError` instead of an ordinary `ValueError` exception.

```python

class NegativeNumberError(ValueError):
    pass

num = int(input("Give me a number: "))
if num < 0:
    raise NegativeNumberError("Number has to be greater than 0")
print(f"The value is {num}")

```

6. Write a function that takes a list of numbers and returns the inverse of each number (if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur. Hint: Write a function that takes a list of numbers and returns the inverse of each number (if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur.

```python
def invert_it(lst):

    temp = []
    for number in lst:
        try:
            temp.append((1/number))
        except (ValueError, ZeroDivisionError) as e:
            print(e)
        finally:
            continue

    return temp


list_1 = [10, 100, 1000]
list_2 = [10, "a", 1000]

print(invert_it(list_1)) #[0.1, 0.01, 0.001]
print(invert_it(list_2)) #[0.1, 0.001]
```

7. Which of the following code snippets would raise a ZeroDivisionError?

```python
a) 5 / 2
b) 3 // 0
c) 8 % (1 - 1)
d) 7 / (3 + 4)
```
Answer: B and C

8. Given the following global dictionary: `students = {'John': 25, 'Jane': 22, 'Doe': 30}`

Write a Python function get_age(name) that takes a student's name as an argument and returns their age. If the student's name isn't in the dictionary, the function should return 'Student not found'.

```python
def get_age(name):
    try:
        return students[name]
    except KeyError:
        return 'Student not found'


students = {'John': 25, 'Jane': 22, 'Doe': 30}
for name in students.keys():
    age = get_age(name)
    print(name, age)

```

9. Given the following list: `numbers = [1, 2, 3, 4, 5]`

Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. In both cases, the function should return None when the element isn't found.

```python
def do_lbyl(lst):
    
    if len(lst) < 6:
        return None
    return lst[5]

def do_afnp(lst):
    
    try:
        return lst[5]
    except IndexError:
        return None

numbers = [1, 2, 3, 4, 5]

print(do_lbyl(numbers))
print(do_afnp(numbers))
```

10. Which of the following code snippets would raise an AttributeError?

```python
a) 'hello'.upper()
b) [1, 2, 3].push(4)
c) {'key': 'value'}.get('key')
d) (12345).length()
```
Answer B & D

