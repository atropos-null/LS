"""
Problem: Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for 
the specified keys.
    - input: dictionary, list of keys
    - output: new dictionary with the reduced keys determined be the list

Example: See Below

Data Structure: new dictionary

Algorithm:
    - dictionary comprehension
    - {key: value 
        for key, values in dictionary.items():
            if key in list of keys}
    - return dictionary


"""

def keep_keys(dictionary, list_of_keys):
    return {key: value for key, value in dictionary.items() if key in list_of_keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True