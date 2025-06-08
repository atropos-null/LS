"""

Problem:  Write a function to returns True or False of a string is a palindrome.
 - input: string
 - output: return True or return False
 - explicit rule 1: case-insensitive
 - explicit rule 2: ignore all non-alphanumeric characters
 - implict rule: can use previous code

Example: 
 - 123ab321' == False
 - 'Madam' == True

Data Structure:
 - Empty string for comparison

Algorithm:
 - clean string
    - check if character isalpha
        - if isalpha, append
        - if not isalpha, ignore
 - create empty string 

 - loop to iterate clean string, in reverse
 - compare two strings
 - return True or False

"""

def is_real_palindrome(string):
    clean_string = ""
   
    for char in string.casefold():
        if char.isalnum():
            clean_string += char

    return clean_string == clean_string[::-1]

print(is_real_palindrome('madam') == True)         # True
print(is_real_palindrome('356653') == True)        # True
print(is_real_palindrome('356635') == False)       # True
print(is_real_palindrome('356a653') == True)       # True
print(is_real_palindrome('123ab321') == False)      # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)          # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

