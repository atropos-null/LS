#Write a function that takes a dictionary and returns a list of all the keys.

student_data = {
    'id': 12345,
    'name': 'Jane Smith',
    'grades': {
        'Python': 95,
        'Math': 87,
        'English': 92,
        'History': 78
    },
    'contact': {
        'email': 'jane.smith@example.com',
        'phone': '555-123-4567'
    },
    'enrolled': True,
    'courses': ['Python 101', 'Data Structures', 'Web Development'],
    'attendance': [True, True, False, True, True],
    'graduation_year': 2024,
    'address': None
}

dict1 = {'a': 1, 'b': 2, 'c': 3}

def get_keys(dictionary):
    keys = dictionary.keys()  # Call keys() directly on the dictionary
    return list(keys)

print(get_keys(dict1))
