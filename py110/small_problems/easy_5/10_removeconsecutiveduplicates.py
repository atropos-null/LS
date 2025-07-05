"""
Problem:  Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the 
initial occurrence. Return the refined sequence.
    - input: list of integers
    - output: list of integers with duplicates removed

    - problem: converting list to set does not preserve original order
    - second problem: list comprehension doesn't work here

Example: [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4] => [1, 2, 6, 5, 3, 4]

Data Structure: List

Algorithm:
    - initalize empty list
    - for element in original_list
        if element not in empty list:
            empty_list.append(element)
        

"""

def unique_sequence(original_list):
    result = []
    for element in original_list:
        if element not in result:
            result.append(element)
    return result
    

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True