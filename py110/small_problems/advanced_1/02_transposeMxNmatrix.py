"""
Problem: Modify your transpose function from the previous exercise so that it works with any MxN matrix with at least one row and one column. 

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

def transpose(matrix):
    transposed = []
    new_rows_count = len(matrix[0])

    for _ in range(new_rows_count):
        transposed.append([])

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            transposed[col_idx].append(matrix[row_idx][col_idx])

    return transposed


# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)


"""
Further Optimization:

def transpose_comprehension(matrix):
    num_cols = len(matrix[0]) # Assumes all rows have the same length
    num_rows = len(matrix)
    return [[matrix[row][col] for row in range(num_rows)] for col in range(num_cols)]
    
"""