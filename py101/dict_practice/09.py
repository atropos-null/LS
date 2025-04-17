# Write a function that groups a list of dictionaries by a specified key and returns 
# a dictionary of lists.

# Sample for grouping dictionaries (Q9)
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 75000},
    {'name': 'Bob', 'department': 'HR', 'salary': 65000},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 80000},
    {'name': 'Diana', 'department': 'Marketing', 'salary': 70000},
    {'name': 'Eve', 'department': 'HR', 'salary': 68000}
]

def dict_of_lists(list, key):
    new_dict = {}
    for dictionary in list:
        group_value = dictionary[key]
        if group_value not in new_dict:
            new_dict[group_value] = []
        new_dict[group_value].append(dictionary)
    return new_dict
        

print(dict_of_lists(employees, 'department'))
print(dict_of_lists(employees, 'name'))
print(dict_of_lists(employees, 'salary'))
