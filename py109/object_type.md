## Mutabilty and Immutability

Objects in Python consist of three key components:

* **Identity**: Unique identifier of the object, remaining constant throughout the object's lifetime. 
* **Type**: Defines the type of the object (e.g., int, str, list). **Type is where the immutability/mutability rests**.
* **Value**: The actual data stored in the object.

For mutable objects (like lists, dictionaries, sets, custom classes), operations that modify the object will affect the original object outside the function.

For immutable objects (like integers, strings, tuples, numbers, frozen sets), operations that appear to modify the object actually create a new object, leaving the original unchanged.

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
