"""

Problem: Create a function that takes two integers as arguments. The first argument is a count, and 
the second is the starting number of a sequence that your function will create. The function should 
return a list containing the same number of elements as the count argument. The value of each element 
should be a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 0. The starting number can 
be any integer. If the count is 0, the function should return an empty list.

    - input: 2 integers
    - output: a list

Example: 5, 1 ==> [1, 2, 3, 4, 5]

Data Structure: List

Algo:
    - def count, start
    - initialize empty list
    - for i in range (start, count+1)
        empty_list.append(i)
    - return list

"""

def sequence(count, start):
    result = []
    stop = (start * count)
    if start < 0:
        for i in range(start, stop - 1, start):
            result.append(i)
    elif start == 0:
        for i in range(count):
            result.append(start)
    else:
        for i in range(start, stop + 1, start):
            result.append(i)

    print(result)
    return result
    
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(5, 3) == [3, 6, 9, 12, 15])         # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True


""" 

Further optimization:

def sequence(count, start_num):
    return [start_num * num for num in range(1, count + 1)]

"""