""" Option 1: iterate over a list version of the set and delete the set elements"""

data_set = {1, 2, 3, 4, 5}
new_set = list(data_set)

for item in new_set:
    if item % 2 == 0:
        data_set.remove(item)

""" Option 2: Create a new set with a set comprehension"""

data_set = {item for item in data_set if item % 2 != 0}