#Write a function that takes a dictionary and returns a new dictionary 
#with the same keys but with all string values converted to uppercase.

user_profile = {
    'username': 'pythondev',
    'email': 'dev@example.com',
    'role': 'developer',
    'active': True,
    'login_count': 42
}

def upper_dict(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        if isinstance(value, str):
            new_dict[key] = value.upper()
        else:
            new_dict[key] = value
    return new_dict

print(upper_dict(user_profile))