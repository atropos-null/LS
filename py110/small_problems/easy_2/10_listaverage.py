"""
Problem: Write a function that takes one argument, a list of integers, and returns the average of all the integers in the 
list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be 
positive integers.
    - input: list of integers
    - output: integer that is the average of all the integers rounded down to an integer.
    - rules: 
        - lists are never empty
        - integers are always positive

Example: [1, 5, 87, 45, 8, 8] == 25

Data Structure: none, just an updating integer

Algorithm
    - sum = 1
    - for element in list:
        - sum += element
    - return mean = sum / len(list)

"""

def average(list1):
    sum = 1
    if len(list1) == 1:
        return list1[0]
    for element in list1:
        sum += element
    mean = int(sum / len(list1))
    return mean

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True