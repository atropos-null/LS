# Create a function that takes a dictionary and returns the sum of all the values 
# (assuming all values are numbers).

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}

def sum_values(dictionary):
    return sum(dictionary.values())

print(sum_values(dict2))
