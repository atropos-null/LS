"""
Problem: Write a function that takes a string argument and returns a list of substrings of that string. 
Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.
    - input: a string
    - output: a list of substrings from the original string
    - rules:
        - first letter of the original string is the first letter of all strings
        - sorted by increasing length

Example: 'xyzy' becomes  'x', 'xy', 'xyz', 'xyzy'

Data Structure: 2 Lists, temp1, temp 2

Algorithm:
    - Get individual characters
        - initialize temp list, temp1
        - for char in string
        - append char to temp list
    - initialize temp list 2, temp2
    - for loop:
        for i in range(len(list)):
            if temp2 is empty:
                append first character
            else:
                append last element in temp 2 with next element in temp 1




"""

def leading_substrings(string):
    temp1 = [char for char in string]
    temp2 = []
    for i in range(len(string)):
        if temp2 == []:
            temp2.append(temp1[0])
        else: 
            temp2.append(temp2[-1] + temp1[i])
    return temp2

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])