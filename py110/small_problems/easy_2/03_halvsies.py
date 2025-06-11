"""
Problem: Write a function that takes a list as an argument and returns a list that contains two elements, 
both of which are lists. Put the first half of the original list elements in the first element of the return 
value and put the second half in the second element. If the original list contains an odd number of elements, 
place the middle element in the first half list.

    - input: a list
    - output: a list that contains two nested lists
    - explicit rule: first half of the inputted lists goes in sublist 1, other half goes in sublist 2
    - explicit rule: if list is odd numbered, the greater list is the first list

    - what to do with 1 element lists or empty lists??

Example: [1, 2, 3, 4]) --> [[1, 2], [3, 4]]

Data Structure: Nested lists

Algorithm:
    - initialize new_list as empty
    - slice list passed as argument into a sublist and append to new_list
        - +1 if its odd since it needs to shift
        - regular if even
    - return new list

"""

def halvsies(my_lst):
    new_list = []
    if len(my_lst) % 2 == 1:
        new_list.append(my_lst[:len(my_lst)//2 + 1]) 
        new_list.append(my_lst[len(my_lst)//2 + 1:])
    else:
        new_list.append(my_lst[:len(my_lst)//2]) 
        new_list.append(my_lst[len(my_lst)//2:])

    return new_list

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])


"""
Optimization:

   def halvsies(my_lst):
       midpoint = (len(my_lst) + 1) // 2  # This handles both odd and even lengths
       return [my_lst[:midpoint], my_lst[midpoint:]]
    
"""