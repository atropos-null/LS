# Python "Pass by Assignment" Practice Problems

Practice predicting Python's output and variable behavior for mutable/immutable objects.

---

## Problems

### Problem 1: Immutable Integer
```python
def modify(x):
    x = 10

num = 5
modify(num)
print(num)
```
**What is printed? What happens to `num`?**

<details>
<summary>Solution</summary>

### Answer 1
**Printed:** `5`  
**Explanation:** Integers are immutable. Reassigning `x` inside `modify()` creates a new local variable but leaves `num` unchanged.

</details>

---

### Problem 2: Mutable List (Append)
```python
def append_item(lst):
    lst.append(4)

my_list = [1, 2, 3]
append_item(my_list)
print(my_list)
```
**What is printed? What happens to `my_list`?**

<details>
<summary>Solution</summary>

### Answer 2
**Printed:** `[1, 2, 3, 4]`  
**Explanation:** Lists are mutable. `append()` modifies the original list in-place.

</details>

---

### Problem 3: String Concatenation
```python
def add_greeting(s):
    s += ", World!"

text = "Hello"
add_greeting(text)
print(text)
```
**What is printed? What happens to `text`?**
<details>
<summary>Solution</summary>

### Answer 3
**Printed:** `Hello`  
**Explanation:** Strings are immutable. `s += ...` creates a new string object that isn’t returned or saved.

</details>

---

### Problem 4: List Reassignment
```python
def reassign(lst):
    lst = [10, 20, 30]

numbers = [5, 6, 7]
reassign(numbers)
print(numbers)
```
**What is printed? What happens to `numbers`?**

<details>
<summary>Solution</summary>

### Answer 4
**Printed:** `[5, 6, 7]`  
**Explanation:** Reassigning `lst` inside the function creates a new local list. The original `numbers` remains unchanged.

</details>

---

### Problem 5: Tuple Modification Attempt
```python
def modify_tuple(t):
    t[0] = 99  # Will this work?

my_tuple = (1, 2, 3)
modify_tuple(my_tuple)
print(my_tuple)
```
**What happens? What is printed?**

<details>
<summary>Solution</summary>


### Answer 5
**Printed:** `(1, 2, 3)`  
**Explanation:** Tuples are immutable. Attempting to modify `t[0]` raises a `TypeError`, but the error is caught and ignored.

</details>
---

### Problem 6: Dictionary Update
```python
def update_dict(d):
    d["key"] = "new_value"

data = {"key": "old_value"}
update_dict(data)
print(data)
```
**What is printed? What happens to `data`?**

<details>
<summary>Solution</summary>

### Answer 6
**Printed:** `{'key': 'new_value'}`  
**Explanation:** Dictionaries are mutable. The `update_dict` function modifies the original dictionary in-place.

</details>

---

### Problem 7: Mixed Types
```python
def func(a, b):
    a = 100
    b.append(5)

x = 1
y = [2]
func(x, y)
print(x, y)
```
**What is printed? What happens to `x` and `y`?**

<details>
<summary>Solution</summary>

### Answer 7
**Printed:** `1 [2, 5]`  
**Explanation:** `x` (immutable) remains `1`, but `y` (mutable list) is modified in-place with `append(5)`.

</details>

---

### Problem 8: Nested List Modification
```python
def change_nested(lst):
    lst[1][0] = "modified"

matrix = [[1, 2], [3, 4]]
change_nested(matrix)
print(matrix)
```
**What is printed? What happens to `matrix`?**

<details>
<summary>Solution</summary>

### Answer 8
**Printed:** `[[1, 2], ['modified', 4]]`  
**Explanation:** Nested lists are mutable. The inner list `[3, 4]` is modified in-place.

</details>
---

### Problem 9: Reassign vs Modify
```python
def process(lst):
    lst = lst + [4]  # Reassignment
    # lst += [4]     # What if this line were used instead?

original = [1, 2, 3]
process(original)
print(original)
```
**What is printed? What happens to `original`?**


<details>
<summary>Solution</summary>

### Answer 9
**Printed:** `[1, 2, 3]`  
**Explanation:** `lst + [4]` creates a new list, leaving `original` unchanged. If `lst += [4]` were used, it would modify the original list in-place.

</details>

---

### Problem 10: Default Mutable Argument
```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
```
**What is printed? Why?**

<details>
<summary>Solution</summary>

### Answer 10
**Printed:** `[1]` then `[1, 2]`  
**Explanation:** Default mutable arguments (like `lst=[]`) retain changes between function calls. The same list is reused!

</details>

---

### Problem 11: In-Place Operator
```python
def increment(n):
    n += 1

value = 5
increment(value)
print(value)
```
**What is printed? What happens to `value`?**

<details>
<summary>Solution</summary>

### Answer 11
**Printed:** `5`  
**Explanation:** Integers are immutable. `n += 1` creates a new integer object that isn’t returned or saved.

</details>

---

### Problem 12: Set Modification
```python
def add_to_set(s):
    s.add(4)

my_set = {1, 2, 3}
add_to_set(my_set)
print(my_set)
```
**What is printed? What happens to `my_set`?**

<details>
<summary>Solution</summary>

### Answer 12
**Printed:** `{1, 2, 3, 4}`  
**Explanation:** Sets are mutable. `add(4)` modifies the original set in-place.

</details>
---

### Problem 13: Return and Modify
```python
def manipulate(lst):
    lst.append(4)
    return lst

original = [1, 2, 3]
result = manipulate(original)
print(original, result)
```
**What is printed? Are `original` and `result` the same object?**

<details>
<summary>Solution</summary>

### Answer 13
**Printed:** `[1, 2, 3, 4] [1, 2, 3, 4]`  
**Explanation:** Both `original` and `result` point to the same list object. Modifying one affects both.

</details>

---

### Problem 14: Multiple Function Calls
```python
def add_element(a_list):
    a_list.append(len(a_list))

lst = []
add_element(lst)
add_element(lst)
print(lst)
```
**What is printed? What happens to `lst`?**

<details>
<summary>Solution</summary>

### Answer 14
**Printed:** `[0, 1]`  
**Explanation:** Each call to `add_element()` appends the current length of the list (which grows after each append).

</details>

---

### Problem 15: Immutable in Mutable
```python
def change_element(lst):
    lst[0] = 100

data = [1, 2, 3]
change_element(data)
print(data)
```
**What is printed? What happens to `data`?**

<details>
<summary>Solution</summary>

### Answer 15
**Printed:** `[100, 2, 3]`  
**Explanation:** Lists are mutable. The first element is reassigned in-place.

</details>

---

### Problem 16: Slice Assignment
```python
def slice_change(lst):
    lst[:] = [7, 8, 9]

numbers = [4, 5, 6]
slice_change(numbers)
print(numbers)
```
**What is printed? What happens to `numbers`?**

<details>
<summary>Solution</summary>

### Answer 16
**Printed:** `[7, 8, 9]`  
**Explanation:** Slice assignment (`lst[:] = ...`) modifies the original list in-place.

</details>
---

### Problem 17: Global Variable Shadowing
```python
x = 10

def func():
    x = 20  # Is this modifying the global x?

func()
print(x)
```
**What is printed? What happens to the global `x`?**

<details>
<summary>Solution</summary>

### Answer 17
**Printed:** `10`  
**Explanation:** `x = 20` inside `func()` creates a local variable. The global `x` remains unchanged.

</details>
---

### Problem 18: Reassigning a String
```python
def reassign_str(s):
    s = "new string"

text = "old string"
reassign_str(text)
print(text)
```
**What is printed? What happens to `text`?**

<details>
<summary>Solution</summary>

### Answer 18
**Printed:** `old string`  
**Explanation:** Strings are immutable. Reassigning `s` inside the function doesn’t affect the original `text`.

</details>

---

### Problem 19: Mutable Return Value
```python
def create_list():
    return [1, 2, 3]

lst1 = create_list()
lst2 = create_list()
lst1.append(4)
print(lst1, lst2)
```
**What is printed? Are `lst1` and `lst2` the same object?**

<details>
<summary>Solution</summary>

### Answer 19
**Printed:** `[1, 2, 3, 4] [1, 2, 3]`  
**Explanation:** `create_list()` returns a new list each time. `lst1` and `lst2` are separate objects.

</details>



---

### Problem 20: Exception Handling with Immutable
```python
def modify_tuple(t):
    try:
        t[0] = 99
    except TypeError:
        pass

my_tuple = (1, 2, 3)
modify_tuple(my_tuple)
print(my_tuple)
```

**What is printed? What happens to `my_tuple`?**

<details>
<summary>Solution</summary>

### Answer 20
**Printed:** `(1, 2, 3)`  
**Explanation:** Tuples are immutable. The modification attempt fails silently due to the `try-except` block.

</details>


---

**Tip:** Try solving all problems before checking the answers!  
**Good luck on your exam!**