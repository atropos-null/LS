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
    last_name = working[-1]
    first_name = working[0]
    middle_name = " ".join(working[1:-1])
    if len(working) == 2:
        return f"{last_name}, {first_name}"
    else:        
        return f"{last_name}, {first_name} {middle_name}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals') == "Ragvals, Karl Oskar Henriksson")  # True