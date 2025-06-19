"""
Problem: Write a function that takes... 
    - input: integer 
    - output: returns a list containing all integers between 1 and the argument (inclusive), in ascending order
    - rules: integers are always positive.

Example: 5 ==> [1, 2, 3, 4, 5]

Data Structure: List

Algo:
    - range (1, number +1)
    - append list
    - return list

"""

def sequence(number):
    number_list = []
    for i in range (1, number+1):
        number_list.append(i)
    return number_list
        

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True


"""
Further Optimization:

def sequence(number):
   return list(range(1, number + 1))
   
"""