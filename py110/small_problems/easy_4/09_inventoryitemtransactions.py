"""
Problem: Write a function that takes two arguments, an inventory item ID and a list of transactions, 
and returns a list containing only the transactions for the specified inventory item.

    - input: an integer representing an item in inventory, and a list of a dictionary of transactions
    - output: a list of a dictionary of transactions

Example: See Below

Data Structure: New list

Algorithm:
    - list comprehension
        - for transaction in transactions:
        -   if id in transaction['id']:
            return transaction


"""

def transactions_for(id, transactions):
    id_activity = [transaction for transaction in transactions if id == transaction['id']]
    return id_activity

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) == [
    {"id": 101, "movement": "in",  "quantity":  5}, 
    {"id": 101, "movement": "in",  "quantity": 12}, 
    {"id": 101, "movement": "out", "quantity": 18}]) # True