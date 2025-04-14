# Write a function that merges two dictionaries. If there are duplicate keys, 
# the value from the second dictionary should overwrite the value from the first.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}


def new_pythonmerge(dictionary1, dictionary2):

    return dictionary1 | dictionary2

def slow_merge(dictionary1, dictionary2):

    new_dict = {} 
    for key, values in dictionary1.items():
       new_dict[key] = values
    for key, values in dictionary2.items():
       new_dict[key] = values
    return new_dict

def old_pythonmerge(dictionary1,dictionary2):

    # For older Python versions
    result = dictionary1.copy()  # Create a copy to avoid modifying original
    result.update(dictionary2)   # Update with values from dictionary2
    return result


print(new_pythonmerge(dict1, dict2))
print(slow_merge(dict1, dict2))
print(old_pythonmerge(dict1,dict2))