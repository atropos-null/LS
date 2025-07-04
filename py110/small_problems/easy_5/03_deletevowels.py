"""
Problem: Write a function that takes a list of strings and returns a list of the same string values, 
but with all vowels (a, e, i, o, u) removed.
    - input: list of strings
    - output: list of strings with vowels removed

Example: ['green', 'YELLOW', 'black', 'white'] =>  ['grn', 'YLLW', 'blck', 'wht']

Data Structure: List

Algorithim:
    - initalize temp list
    - initialize word list
    - for element in list of strings:
        for char in element
            if char not in vowels
                append char to word
                join word
        append word to final list


    
"""

def remove_vowels(list_of_strings):
    final = []
    for element in list_of_strings:
        word = []
        for char in element:
            if char not in 'aeiouAEIOU':
                word.append(char)
        no_vowels = "".join(word)
        final.append(no_vowels)
    return final


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True