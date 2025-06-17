"""

Problem: Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that 
contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments 
contain the same number of elements.

    - input: 2 lists
    - output: 1 list with numbers of each list multiplied to each element position
    - rules: arguments have the same number of elements

Data Structure: List

Algorithm:  
    - initialize empty list
    - zip up two lists
    - convert zip to list
    - multiply the elements of the tuple
    - add product to empty list
    - return list


"""

def multiply_list(array1, array2):
    prod_list = []
    temp_list = list(zip(array1, array2))
    for element in temp_list:
        product = element[0] * element[1]
        prod_list.append(product)
    return prod_list

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True


"""
Further Optimization:

def multiply_list(array1, array2):
    prod_list = []
    for a, b in zip(array1, array2):
        prod_list.append(a * b)
    return prod_list

Or:

def multiply_list(array1, array2):
    return [a * b for a, b in zip(array1, array2)]

"""