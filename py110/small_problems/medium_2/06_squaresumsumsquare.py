"""
Problem: Write a function that computes the difference between the square of the sum of the first count positive integers 
and the sum of the squares of the first count positive integers.

Example: 3 == > 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

Data Structure: two holding lists

Algorithm:
    - initiate temp list
    - initiate second temp list
    - using range(1, number+1)
        - append number to temp
    - first = sum(temp) ** 2
    - second, iterate over items in temp
        - item ** 2
        - sum the second list

    - result = first - second

"""

def sum_square_difference(number):
    temp = []
    temp_2 = []
    for i in range(1, number+1):
        temp.append(i)

    first = sum(temp) ** 2

    for item in temp:
        temp_2.append(item ** 2)
    second = sum(temp_2)

    result = first - second
    return result



print(sum_square_difference(3) == 22)          # True
print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True