"""
Problem: Write a function that...
     
    - input: string
    - determine: left and right parenthesis present.
    - output: True if balanced, false if not balanaced

Example: "What (is) this?" == True; "What is) this?") == False

Data Structure: list for holding

Algo:

    - symbols = ['(', ')']
    - temp = []
    - for char in string:
        if char in symbols:
            temp.append(char)
    - handle empty list
    - check for right parenthesis first
    - check for uneven parenthesis
    - check for left parenthesis last
        

"""

SYMBOLS  = ['(', ')']

def is_balanced(text):
    
    temp = []
    for char in text:
        if char in SYMBOLS:
            temp.append(char)
    if temp == []:
        return True
    elif temp[0] == SYMBOLS[1]:
        return False
    elif temp[-1] == SYMBOLS[0]:
        return False
    elif len(temp) % 2 != 0:
        return False
    else:
        return True


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

"""
Alternative method:

def is_balanced(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:  
            return False
    return count == 0  # Ensures all left parentheses are matched

"""