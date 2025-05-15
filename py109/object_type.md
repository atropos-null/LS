## Mutabilty and Immutability

Objects in Python consist of three key components:

* **Identity**: Unique identifier of the object, remaining constant throughout the object's lifetime. 
* **Type**: Defines the type of the object (e.g., int, str, list). **Type is where the immutability/mutability rests**.
* **Value**: The actual data stored in the object.

A mutable object is an object whose value can change. For mutable objects (like lists, dictionaries, sets, custom classes), operations that modify the object will affect the original object outside the function.

An immutable object is "an object with a fixed value."  Once you create an immutable object, its contents cannot change for the duration of the program. For immutable objects (like integers, strings, tuples, numbers, frozen sets), operations that appear to modify the object actually create a new object, leaving the original unchanged. 

```python
text = "Hello, World!"
print(id(text)) #124799425931952
print(type(text)) #<class 'str'>

list1 = ["H","e","l","l","o"," ", "W","o","r","l","d", "!"]
print(id(list1)) #128993598267456
print(type(list1)) #<class 'list'>
```


```python
def modify_list(lst):
    lst.append(4)   
    lst = [7, 8, 9] 
    return lst      

my_list = [1, 2, 3]
new_list = modify_list(my_list) 


print(my_list) 
print(new_list)
```

<details>
<summary>Solution</summary>

```python
print(my_list) #[1,2,3,4]
print(new_list) #[7,8,9]
```

</details>

<details>
<summary>What happened?</summary>

```python
def modify_list(lst):
    lst.append(4)   #modifies "my_list" in place
    lst = [7, 8, 9] #list is reassigned
    return lst      #reassigned list is passed to new_list in the global scope

my_list = [1, 2, 3]
new_list = modify_list(my_list) #modify_list is called, passing my_list but reassigned list is returned and reassigned to new_list

print(my_list) #[1,2,3,4]
print(new_list) #[7,8,9]
```
</details>

### Augmented Assignment 

#### `+=` Operator

* `For Immutable Objects`: When you use `+=` on an immutable object, a new object is created with the result of the addition. The variable is then updated to reference this new object.

```python
x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

s = "Hello"
s += " World"
print(s)  # Output: "Hello World"
```

* `For Mutable Objects`: When you use `+=` on a mutable object, the object itself is modified in place, and no new object is created.

```python
lst = [1, 2, 3]
lst += [4, 5]  # Equivalent to lst.extend([4, 5])
print(lst)  # Output: [1, 2, 3, 4, 5]
```




Further References:

[Gruppetta, S. (2024a, January 18). My neighbours are moving house • Mutating the immutable tuple (Sort of). The Python Coding Stack.](https://www.thepythoncodingstack.com/p/mutating-the-immutable-python-tuples)


