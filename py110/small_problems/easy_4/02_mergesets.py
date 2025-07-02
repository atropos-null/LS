"""
Problem: Given two lists, convert them to sets and return a new set which is the union of both sets.
    - input: 2 lists
    - output: a new, third set
    - to do: 
        - convert lists to sets
        - union the sets

Example: [3, 5, 7, 9] and [5, 7, 11, 13] become {3, 5, 7, 9, 11, 13}

Data Structures: None required

Algorithm:
    - reassign list variable by converting list to set
    - third set = union set 1 to set 2
    - return third set

"""

def merge_sets(lst1, lst2):
    return set(lst1) | set(lst2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13}) #True