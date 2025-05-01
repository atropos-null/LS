## Practice Questions for PY109 Assessment

###
Basic Level Questions
1.  ​Basic​: What will the following code output and why?
```python    
    a = 5
    b = a
    a = 10
    print(b)
```

2.  ​Basic​: What will the following code output and why?
```python    
    greeting = "hello"
    def change_greeting():
        greeting = "hi"

    change_greeting()
    print(greeting)
```

3.  ​Basic​: What will the following code output and why?
```python    
    def add_to_list(item, lst=[]):
        lst.append(item)
        return lst

    list1 = add_to_list(1)
    list2 = add_to_list(2)
    print(list1)
```

4.  ​Basic​: What will the following code output and why?
```python    
    x = "5"
    y = 2
    print(x * y)
```

5.  ​Basic​: What will the following code output and why?
```python    
    def greet(name):
        return f"Hello, {name}!"
        print("This won't print")

    result = greet("John")
    print(result)
```

### Intermediate Level Questions
6.  ​Intermediate​: What will the following code output and why?
```python    
    numbers = [1, 2, 3, 4, 5]
    new_numbers = numbers[1:4]
    numbers[2] = 10
    print(new_numbers)
```

7.  ​Intermediate​: What will the following code output and why?
```python    
    def modify_string(s):
        s += " World"

    message = "Hello"
    modify_string(message)
    print(message)
```

8.  ​Intermediate​: What will the following code output and why?
```python    
    def count_down(n):
        if n <= 0:
            return
        print(n)
        count_down(n-1)

    count_down(3)
```

9.  ​Intermediate​: What will the following code output and why?
```python    
    a = [1, 2, 3]
    b = a
    a.append(4)
    b.append(5)
    print(a)
```

10. ​Intermediate​: What will the following code output and why?
```python    
    x = 10
    def test():
        global x
        x += 5
        return x

    print(test())
    print(x)
```

11. ​Intermediate​: What will the following code output and why?
```python    
    a = "hello"
    b = "hello"
    print(a is b)

    c = [1, 2, 3]
    d = [1, 2, 3]
    print(c is d)
```

12. ​Intermediate​: What will the following code output and why?
```python    
    def outer():
        x = 10
        def inner():
            nonlocal x
            x = 20
        inner()
        return x

    print(outer())
```

13. ​Intermediate​: What will the following code output and why?
```python    
    d = {"a": 1, "b": 2}
    d["a"] = 3
    d["c"] = d.get("b", 0) + 1
    print(d)
```

14. ​Intermediate​: What will the following code output and why?
```python    
    numbers = [1, 2, 3, 4, 5]
    result = [num * 2 for num in numbers if num % 2 == 0]
    print(result)
```    
15. Intermediate​: What will the following code output and why?
```python   
    def process_data(data):
        if not data:
            return
        print(data[0])
        process_data(data[1:])

    process_data([10, 20, 30])
```

### Advanced Level Questions
16. ​Advanced​: What will the following code output and why?

```python   
    def strange_function(lst):
        if not lst:
            return []
        return [lst[0]] + strange_function(lst[1:])

    print(strange_function([1, 2, 3, 4]))
```

17. ​Advanced​: What will the following code output and why?
```python   
    a = [1, 2, 3]
    b = a.copy()
    a[0] = 10
    b.append(4)
    print(a)
    print(b)
```

18. ​Advanced​: What will the following code output and why?
```python   
    def confused_function(x):
        if x <= 1:
            return 1
        return x * confused_function(x - 1)

    print(confused_function(4))
```

19. ​Advanced​: What will the following code output and why?
```python   
    data = {"a": 1, "b": [1, 2, 3]}
    copy_data = data.copy()
    data["a"] = 10
    data["b"].append(4)
    print(copy_data)
```

20. ​Advanced​: What will the following code output and why?
```python   
    def make_incrementer(n):
        def increment(x):
            return x + n
        return increment

    add_five = make_incrementer(5)
    print(add_five(10))
```

21. ​Advanced​: What will the following code output and why?
```python   
    items = [1, 2, 3, 4, 5]
    for index, item in enumerate(items):
        if item % 2 == 0:
            items.remove(item)
    print(items)
```

22. ​Advanced​: What will the following code output and why?
```python   
    try:
        print("Step 1")
        x = 10 / 0
        print("Step 2")
    except ZeroDivisionError:
        print("Step 3")
    finally:
        print("Step 4")
    print("Step 5")
```

23. ​Advanced​: What will the following code output and why?
```python   
    def apply_operation(op, x, y):
        return op(x, y)

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    print(apply_operation(add, 5, 3))
    print(apply_operation(multiply, 5, 3))
```

24. ​Advanced​: What will the following code output and why?
```python   
    a = 5
    b = 10

    a, b = b, a + b
    print(a, b)
```

25. ​Advanced​: What will the following code output and why?
```python   
    def tricky_calculation(n):
        result = 0
        for i in range(n):
            result += i
            if i % 2 == 0:
                continue
            result *= 2
        return result

    print(tricky_calculation(5))
```    