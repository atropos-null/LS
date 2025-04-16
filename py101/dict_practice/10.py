#Write a function named filter_by_value that takes a dictionary and a value as arguments. 
#The function should return a new dictionary that only contains the key-value pairs where 
#the value is equal to the given value.

test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

def filter_by_value(dict, number):
    new_dict = {}
    for key, value in dict.items():
        if value == number:
            new_dict[key] = value
       
    print(new_dict)
    return new_dict

print(filter_by_value(test_dict, 1) == {'a': 1, 'c': 1})
print(filter_by_value(test_dict, 4) == {})
print(filter_by_value({}, 5) == {})




