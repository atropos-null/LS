"""

Problem: Write a function that combines two lists passed as arguments and returns a
new list that contains all elements from both list arguments, with each element taken in alternation.
    - input: two lists,
    - output: one list
    - explicit rule: elements alternated

Example: 
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

Data Structure: None

Algorithm:
    - initialize list as empty
    - zip function between two arguments
    - convert tuple to a list
    - use extend to populate the empty list

"""

def interleave(lst1, lst2):
    final_list = []
    new_list = list(zip(lst1, lst2))
    for item in new_list:
        final_list.extend(item)
    return final_list
    

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True