"""
Problem: Write a function that ...
    - input: a string with first name, a space, and a last name. 
    - output:  a new string consisting of the last name, a comma, a space, and the first name.

Example: 'Joe Roberts' ==> "Roberts, Joe"

Data structure: list for holding

Algo:
    base problem:
    - holding_list = split string
    - last_name = holding[-1]
    - return f"{last_name}, {first_name}"
    further exploration: 
    - middle names = join middle names
    - if len(holding_list) == 2:
        - return f"{last_name}, {first_name}"
    - else
        - return f"{last_name}, {first_name} {middle_name}"


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

"""

Further Optimization:
def swap_name(name):
    working = name.split()
    last_name = working[-1]
    first_name = working[0]
    middle_name = " ".join(working[1:-1])

    if middle_name:
        return f"{last_name}, {first_name} {middle_name}"
    return f"{last_name}, {first_name}"

"""