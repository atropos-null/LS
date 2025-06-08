"""
Problem: Write a function that takes a list of numbers and returns a list with the same number of elements, 
but with each element's value being the running total from the original list

    - input: list of integers
    - output: list of summed integers
    - explicit rules: empty list returns empty list

Example: [2, 5, 13]) == [2, 7, 20], ([]) == []

Data Structure: A list

Algorithm:

- create empty list
- iterate over elements of the list
- add number to the previous number
- append empty list with value
- return new list

"""

def running_total(list):
    running_totals = []
    if not list:
        return []
    running_totals.append(list[0])
    for i in range(1, len(list)):
        running_totals.append(list[i] + running_totals[-1])    
      
    return running_totals


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
       == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True