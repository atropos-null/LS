# Create a function that takes a list of dictionaries and a key name, and returns a new list sorted 
# based on that key's values.

products = [
    {'name': 'Laptop', 'price': 1200, 'stock': 10},
    {'name': 'Phone', 'price': 800, 'stock': 25},
    {'name': 'Tablet', 'price': 500, 'stock': 5},
    {'name': 'Headphones', 'price': 200, 'stock': 50}
]

def sort_dict(list_of_dicts, key_name):
    return sorted(list_of_dicts, key=lambda x: x[key_name])

# Example usage:
print(sort_dict(products, "price"))  # Sort by price
print(sort_dict(products, "stock"))  # Sort by stock