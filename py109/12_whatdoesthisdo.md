## What will this code do?
1. 
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[2:] + numbers[:2])
```

2. 
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.insert(1, 'kiwi')
fruits.pop(0)
print(fruits)
```

3. 
```python

x = 10
y = 5
result = x > y and "x is greater" or "y is greater"

```

4. 
```python
def modify_list(lst):
       lst = lst + [4, 5, 6]
       return lst
   
   my_list = [1, 2, 3]
   new_list = modify_list(my_list)
   print(my_list)
   print(new_list)
```

5. 
```python
numbers = [1, 2, 3, 4]
result = numbers.pop()
numbers.append(result * 2)
print(numbers)
```

6. 
```python
def change_value(x):
       x = x + 5
       return x
   
num = 10
new_num = change_value(num)
print(f"num: {num}, new_num: {new_num}")
```

7. 
```python
a = 0
b = "hello"
c = []
   
result = a or b and c or "default"
print(result)
```
8. 
Pay attention to variable scope and the global keyword:

```python

   x = 10
   
   def outer_function():
       x = 20
       
       def inner_function():
           global x
           x = 30
           print("inner x:", x)
       
       inner_function()
       print("outer x:", x)
   
   outer_function()
   print("global x:", x)
```

9. 

```python

numbers = [1, 2, 3]
result = numbers.extend([4, 5]) 
print(f"Result: {result}, Numbers: {numbers}")
```

10. 

```python

person = {'name': 'Alex', 'age': 30}
info = person
info['city'] = 'Seattle'
del person['age']
print(person)
```

11. 
```python

text = "Python"
result = ""
for char in text:
    result = char + result
print(result)
```

12. 
```python
def check_number(num):
    return "Positive" if num > 0 else "Zero" if num == 0 else "Negative"

x = 0
y = -5
print(check_number(x))
print(check_number(y))
print(check_number(x or y))
```