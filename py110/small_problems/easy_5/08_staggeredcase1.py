"""
Problem: Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme.
Every other character, starting from the first, should be capitalized and should be followed by a lowercase or 
non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for 
determining when to switch between upper and lower case.

    - input: string
        - may have:
            - spaces
            - digits
            - non_alphanumeric characters
    - output: string
        - every other character upper cased if an alphabetic character
    
Example: 
    - 'I Love Launch School!' => "I LoVe lAuNcH ScHoOl!" 
    - 'ALL_CAPS' => "AlL_CaPs"

Data Structure:  empty string

Algorithm:

    - empty string
    - if not string:
            return " "
    - for i, char in enumerate(string)

        - elif char.isspace() or char.isdigit() or not char.isalpha():
            empty_string += char
        - elif i  % 2 == 0:
            empty_string += char.upper()
        - elif i  % 1 == 0:
            empty_string += char.lower()
       
    return string 
        
"""

def staggered_case(original_string):
    if not original_string:
        return ""
    swapped_string = ""
    for i, char in enumerate(original_string):
        if not char.isalpha():
            swapped_string += char
        elif i % 2 == 0:
            swapped_string += char.upper()
        else:
            swapped_string += char.lower()
    return swapped_string


string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True