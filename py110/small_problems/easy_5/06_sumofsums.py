"""
Problem: Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that 
list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.

    - input: list, elements are numbers
    - output: integer, sum of all the sums of each leading subsequence
    - rules: No empty lists

Example: [3, 5, 2] => 21

Data Structure: List

Algorithm:
    - initialize empty list
    - first element of list goes into empty list
    - sum number and append to working list
    - sum the list 
    - return

Other version:
    - initialize a counter to 0
    - initialize a second counter to 0
    - for number in list,
        - add to second counter
    - add second counter to first counter
  
"""

def sum_of_sums(lst): 
    temp = []
    for number in lst:
        if temp == []:
            temp.append(lst[0])
        else: 
            temp.append(temp[-1] + number)
    return sum(temp)    
            

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True