"""
Problem: Using the transactions_for as basis,  write a function that returns True or False based on whether or not an 
inventory item (an ID number) is available. As before, the function takes two arguments: an item ID and a list of 
transactions. The function should return True only if the sum of the quantity values of the item's 
transactions is greater than zero. Notice that there is a movement property in each transaction object. 
A movement value of 'out' will decrease the item's quantity.

    - input: an item number as integer, a list of transactions
    - output: True or False

Example: See Below

Data Structure: 1 list to hold relevant transactions.

Algorithm:
    - use transactions_for() in previous problem to get the relevant transactions
    - initialize amount to 0
    - find the in and out movements, credit or debit the amount
    - return true or false if greater than 0
    
"""

def transactions_for(id, transactions):
    return [transaction for transaction in transactions if id == transaction['id']]

def is_item_available(id, transactions):
    transactions = transactions_for(id, transactions)
    amount = 0
    for transaction in transactions:
        if transaction['movement'] == 'in':
            amount += transaction['quantity']
        else:
            amount -= transaction['quantity']
    if amount > 0:
        return True
    else: 
        return False


    


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

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True