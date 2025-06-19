"""
Problem: Write a function that ...
    - input: a string with first name, a space, and a last name. 
    - output:  a new string consisting of the last name, a comma, a space, and the first name.

Example: 'Joe Roberts' ==> "Roberts, Joe"

Data structure: list for holding

Algo:
    - holding_list = split string
    - return f"{holding_list[1]}, {holding_list[0]}

"""

def swap_name(name):
    working = name.split()
    return f"{working[1]}, {working[0]}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True