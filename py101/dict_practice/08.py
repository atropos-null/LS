#Create a function that filters a dictionary to only include key-value pairs 
#where the value meets a certain condition (e.g., is a string, is greater than 10, etc.)

mixed_data = {
    'name': 'Project X',
    'duration': 45,
    'participants': 12,
    'location': 'Room 302',
    'completed': False,
    'score': 87.5
}

def filter_pairs(dicts):
    new_dict = {}
    for key, value in dicts.items():
        if value == False:
            new_dict[key] = value
    return new_dict

print(filter_pairs(mixed_data))