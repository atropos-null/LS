## "What's Wrong With This Code" Practice Problems for PY109 Exam


Here are 15 debugging exercises to help you prepare for your PY109 assessment. Each problem contains code with an error or issue for you to identify and explain.

1.  ​Basic​: What's wrong with this code?

```python
def greet(name):
        print("Hello, " + name + "!")
        
    greeting = greet("Sarah")
    print(greeting.upper())
```

2. ​Basic​: What's wrong with this code?

```python 
    def greet(name):
        print("Hello, " + name + "!")
        
    greeting = greet("Sarah")
    print(greeting.upper())

```

3.  ​Basic​: What's wrong with this code?

```python   
    number = input("Enter a number: ")
    result = number + 10
    print(result)
```

4.  ​Basic​: What's wrong with this code?

```python   
    my_list = [1, 2, 3, 4, 5]
    print(my_list[5])
```

5.  ​Intermediate​: What's wrong with this code?

```python   
    def modify_string(text):
        text = text.upper()
        
    message = "hello world"
    modify_string(message)
    print(message)
```

6.  ​Intermediate​: What's wrong with this code?

```python

    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return
            print("Number is odd")
```


7.  ​Intermediate​: What's wrong with this code?

```python    
    numbers = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers.remove(numbers[i])
    print(numbers)
```
8.  ​Intermediate​: What's wrong with this code?

```python   
    def update_dictionary(dict):
        dict = {"new": "value"}
        
    my_dict = {"old": "data"}
    update_dictionary(my_dict)
    print(my_dict)

```
9.  ​Intermediate​: What's wrong with this code?

```python   
    numbers = [1, 2, 3]
    squares = []

    for num in numbers:
        square = num ** 2
    squares.append(square)

    print(squares)
```

10.  ​Advanced​: What's wrong with this code?

```python  
    total = 0

    def add_to_total(num):
        total += num
        return total
        
    print(add_to_total(5))
```

11. ​Advanced​: What's wrong with this code?

```python  
    def create_multiplier(x):
        return lambda n: x + n
        
    double = create_multiplier(2)
    print(double(5))
```


12. ​Advanced​: What's wrong with this code?

```python  
    names = ["Alice", "Bob", "Charlie"]
    filtered_names = filter(lambda x: len(x) > 4, names)
    print(filtered_names[0])
```

13. ​Basic​: What's wrong with this code?

```python
    def get_list():
        result = []
        for i in range(3):
            result.append(i)
        return
        return result

    print(get_list())
```

14. ​Intermediate​: What's wrong with this code?

```python  
    count = 0
    while count < 5:
        if count == 3:
            continue
        print(count)
        count += 1
```

15. ​Intermediate​: What's wrong with this code?

```python    
    def process_list(items):
        if len(items) = 0:
            return "Empty list"
        return "List has items"
        
    print(process_list([]))
```

16. Advanced​: What's wrong with this code?

```python

    def calculate_average(numbers):
        total = sum(numbers)
        count = len(numbers)
        return total / count
        
    result = calculate_average([])
    print(f"The average is {result}")
```

17.  ​Intermediate​: What's wrong with this code?

```python  
    def add_numbers(a, b):
        result = a + b
        
    total = add_numbers(5, 10)
    print(f"The total is {total}")

```

18.  ​Intermediate​: What's wrong with this code?

```python  
    my_dict = {"a": 1, "b": 2}
    my_dict["c"].append(3)
    print(my_dict)
```

19.  ​Advanced​: What's wrong with this code?

```python
  
    def join_strings(strings):
        result = ""
        for i in range(len(strings)):
            if strings[i].lower() = "stop":
                break
            result += strings[i] + " "
        return result
        
    print(join_strings(["Hello", "world", "STOP", "now"]))
```

19.  ​Advanced​: What's wrong with this code?

```python  
    def modify_list(items):
        for i in range(len(items)):
            if items[i] % 2 == 0:
                items.remove(items[i])
        return items
        
    numbers = [1, 2, 3, 4, 5, 6]
    print(modify_list(numbers))

```

20.  ​Intermediate​: What's wrong with this code?
```python  
    def get_full_name(first, last, middle):
        if middle:
            return f"{first} {middle} {last}"
        else:
            return f"{first} {last}"
            
    print(get_full_name("John", "Smith"))
```

21.  ​Advanced​: What's wrong with this code?

```python  
    def average(numbers):
        total = 0
        count = 0
        for num in numbers:
            if isinstance(num, (int, float)):
                total += num
                count += 1
        return total / count
        
    print(average([1, 2, "3", 4, None, 5]))
```

22.  ​Intermediate​: What's wrong with this code?

```python
    data = {'a': 1, 'b': 2}

    def update_data(key, value):
        if key in data:
            data[key] = value
        else:
            return f"Key {key} not found"

    result = update_data('c', 3)
    print(f"Updated value: {result}")
```

23.  ​Advanced​: What's wrong with this code?

```python  
    def nested_sum(numbers):
        result = 0
        for item in numbers:
            if type(item) == list:
                result += sum(item)
            result += item
        return result
        
    print(nested_sum([1, [2, 3], 4]))
```

24.  ​Intermediate​: What's wrong with this code?

```python  
    def process_dict(my_dict):
        for key in my_dict:
            if my_dict[key] < 0:
                del my_dict[key]
        return my_dict
        
    numbers = {"a": 1, "b": -2, "c": 3, "d": -4}
    print(process_dict(numbers))
```

25. Advanced​: What's wrong with this code?

```python
    def reverse_words(sentence):
        words = sentence.split()
        result = ""
        for i in range(len(words) - 1, -1, -1):
            result += words[i]
        return result
        
    print(reverse_words("Hello world"))

```   

26. ​Advanced​: What's wrong with this code?

```python 
    def count_elements(nested_list):
        count = 0
        for element in nested_list:
            if isinstance(element, list):
                count += count_elements(element)
            count += 1
        return count
        
    print(count_elements([1, [2, 3], [4, [5, 6]]]))
```

27. ​Intermediate​: What's wrong with this code?

```python
    def max_value(dictionary):
        values = dictionary.values()
        return max(values)
        
    print(max_value({"a": -10, "b": -20, "c": -30}))
```

28. ​Advanced​: What's wrong with this code?

```python 
    def find_duplicates(items):
        seen = {}
        duplicates = []
        for item in items:
            if item in seen:
                duplicates.append(item)
            seen[item]
        return duplicates
        
    print(find_duplicates([1, 2, 3, 2, 1, 4, 5, 4]))
```

29. ​Intermediate​: What's wrong with this code?

```python 
    def safe_divide(a, b):
        try:
            return a / b
        except:
            print("Error: Division by zero")
            
    result = safe_divide(10, 0)
    print(f"Result: {result * 2}")
```

30. ​Advanced​: What's wrong with this code?

```python 
    def deep_copy(obj):
        if isinstance(obj, list):
            return [deep_copy(item) for item in obj]
        if isinstance(obj, dict):
            return {key: deep_copy(value) for key, value in obj.items}
        return obj
        
    original = {"a": [1, 2, 3], "b": {"c": 4}}
    copy = deep_copy(original)
    print(copy)
``` 