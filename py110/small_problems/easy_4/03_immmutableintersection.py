"""
Problem: Transform two lists into frozen sets and find their common elements.
    - input: 2 lists
    - output: 1 frozen set

Example: [2, 4, 6, 8] and [1, 3, 5, 7, 8] become frozenset({8})

Data Structure: None

Algorithm:
    - convert list to set
    - intersection the set: & symbol
    - convert to frozen set

"""


def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True