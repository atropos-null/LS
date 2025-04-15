#Write a function that inverts a dictionary (swapping keys and values). Assume all values 
# are unique.

grades = {'Python': 95, 'Math': 87, 'English': 92, 'History': 78}

def swap_keysandvalues(dictionary):     
    new_dictionary = {}
    for key, value in dictionary.items():
        new_dictionary[value] = key
    return new_dictionary

print(swap_keysandvalues(grades))


# With a dictionary comprehension:

# def swap_keysandvalues(dictionary):
#     new_dictionary = {value: key for key, value in dictionary.items()}
#     return new_dictionary