"""

Problem: Write a function that checks if the string arrugment is a palindrome, or isn't. 
    - input: a string
    - output: return True or return False
    - explicit rule 1: case matters
    - explicit rule 2: all characters matter

Example: A palindrome reads the same forwards and backwards. 
    - example 1: 'madam'
    - example 2: '356653'

Data Structure:
    - empty string

Algorithm:
    - iterate over string in reverse
    - add reversed character to string
    - compare string to reverse string
    - return true or false


"""

def is_palindrome(string):
    comparison_string = ""
    for char in string[::-1]:
        comparison_string += char

    if comparison_string != string:
        return False
    else:
        return True
    

# All of these examples should print True

print(is_palindrome('madam') == True)  #True
print(is_palindrome('356653') == True) #True
print(is_palindrome('356635') == False) #True

# case matters
print(is_palindrome('Madam') == False) #True

# all characters matter
print(is_palindrome("madam i'm adam") == False) #True

""" 

A more pythonic method:

def is_palindrome(string):
   return string == string[::-1]

or:

def is_palindrome(string):
    comparison_string = ""
    for char in string[::-1]:
        comparison_string += char
    return comparison_string == string

"""