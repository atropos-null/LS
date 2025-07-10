"""
Problem: Write a function that rotates a list by moving the first element to the end of the list. 
    - input: list of various element types
    - output: a new list where item[0] becomes item[-1]
    - rules:
        - Do not modify the original list; return a new list instead.
        - If the input is an empty list, return an empty list.
        - If the input is not a list, return None.

Example: [7, 3, 5, 2, 9, 1] ==> [3, 5, 2, 9, 1, 7]    

Data Structure: List

Algorithm:

    - if lst is None or Empty not isinstance(lst, list):
    - initalize new list
    - for item in list starting at index 1:
        - new_list.append(item)
        - finally, append first element
            
        
"""

def rotate_list(lst):
    if not isinstance(lst, list):
        return None

    if not lst:  # This handles empty lists
        return []
    
   
    result = []
    for item in lst[1:]:
        result.append(item)
    result.append(lst[0])
    return result
        

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# # the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])