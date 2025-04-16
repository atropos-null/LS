#Write a function that takes a nested dictionary and flattens it into a 
#single-level dictionary. The keys in the flattened dictionary should be joined 
# with a dot (e.g., {'a': {'b': 1}} becomes {'a.b': 1}). 

# I did not code this, this was lsbot. This was too hard for py109.

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

def flatten_dict(d, parent_key='', sep='.'):
    """
    Flattens a nested dictionary into a single-level dictionary.

    Args:
        d (dict): The nested dictionary to flatten.
        parent_key (str): The base key to use for recursion (used internally).
        sep (str): Separator to join keys.

    Returns:
        dict: A flattened dictionary.
    """

    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


flattened = flatten_dict(nested_dict)
print(flattened)