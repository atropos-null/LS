"""
Problem: Given two lists of integers of the same length, return a new list where each element is the product of 
the corresponding elements from the two lists.
    - input: two lists
    - output: new list with elements of previous list multiplied
    - rules:
        - list lengths are the same
        - multiply by the position

Example: See Below

Data Structure: Lists

Algorithm: 
    - list comprehension:
        [x * y 
        for x, y in zip(list1, list2)]


"""

def multiply_items(list1, list2):
    return [x * y for x, y in zip(list1, list2)]


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True