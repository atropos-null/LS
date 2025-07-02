""" 
Problem: Given a dictionary, return its keys sorted by the values associated with each key.
    - input: dictionary
    - output: keys sorted by the values in a list

Example: {'p': 8, 'q': 2, 'r': 6} becomes ['q', 'r', 'p'] as q is value 2, r is value 6 and p is value 8

Data Structure: holding list

Algorithm:
    - sort dictionary with a lambda
    - iterate over sorted items
    - for each tuple:
        - append first element of tuple to the holding list
    - return holding list

"""

def order_by_value(a_dict):
    temp = []
    sorted_items = sorted(a_dict.items(), key=lambda item: item[1])
    for tupled in sorted_items:
        j, k = tupled
        temp.append(j)
    return temp

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True