"""
Problem: Write a function that takes a list of lists that represents a 3x3 matrix and returns the transpose of the matrix. 

    - input: list of lists
    - output: list of lists with elements switched

    - rules:
        - return a new list, don't modify in place
        - no external libraries

Example: 

1  5  8
4  7  2
3  9  6

Becomes:

1  4  3
5  7  9
8  2  6

Data Structure: Lists!

Algorithm:

- initiate empty list
- for loop, column
    - initiate sublist
    - for loop again, row
        - append element
    - append sublist
    
"""

def transpose(lst):
    new_list = []

    for i in range(len(lst)):
        sub_list = []
        for j in range(len(lst)):
            sub_list.append(lst[j][i])
        new_list.append(sub_list)

    return new_list

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True