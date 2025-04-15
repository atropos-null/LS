#Write a function that takes a nested dictionary and flattens it into a 
#single-level dictionary. The keys in the flattened dictionary should be joined 
# with a dot (e.g., {'a': {'b': 1}} becomes {'a.b': 1}).

nested_dict = {
    'user': {
        'personal': {
            'name': 'John',
            'age': 30
        },
        'settings': {
            'theme': 'dark',
            'notifications': True
        }
    },
    'app_version': '2.3.1'
}