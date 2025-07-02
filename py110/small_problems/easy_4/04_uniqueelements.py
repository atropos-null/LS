""" 
Problem: From two list arguments, determine the elements that are unique to the first list. The return value should be a set.
    - input: 2 lists
    - output: 1 set
    - to do:
        what elements are unique to list 1?

Example: [3, 6, 9, 12] and [6, 12, 15, 18] result in {9, 3}

Data Structure: None

Algorithm:
    - convert list to sets
    - use sets in difference operation

"""

def unique_from_first(list1, list2):
    return set(list1) - set(list2)


list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})