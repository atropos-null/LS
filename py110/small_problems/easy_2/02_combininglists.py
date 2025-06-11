"""
Problem: Write a function that takes two lists as arguments and returns a set that contains the union of the values from 
the two lists. You may assume that both arguments will always be lists.
    - input: two lists
    - output: set
    - explicit rule: lists always assigned


Example: ([1, 3, 5], [3, 6, 9]) ==  {1, 3, 5, 6, 9})

Data Structure: None

Algorithm
    - convert lists to sets
    - use | to join the set
    - return new set

"""

def union(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1 | set2

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True


"""
Optimized:

def union(lst1, lst2):
    return set(lst1) | set(lst2)

"""