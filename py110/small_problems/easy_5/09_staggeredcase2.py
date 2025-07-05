"""

Problem: Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether 
it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; 
they just don't count when toggling the desired case.

     - input: string
        - may have:
            - spaces
            - digits
            - non_alphanumeric characters
            = but these are not to be included in the count
    - output: string
        - every other character upper cased if an alphabetic character

        Data Structure:  empty string

Algorithm:

    - empty string
    - if not string:
            return " "
    - initialize a position counter to 0
    - for char in string

        - if not char.isalpha():
            empty_string += char
        - else:
            position += 1
            if position % 2 == 0:
                empty_string += char.upper()
            else:
            empty_string += char.lower()

"""

def staggered_case(original_string):
    if not original_string:
        return ""
    swapped_string = ""
    position = 0
    for char in string:
        if not char.isalpha():
            swapped_string += char
        else:
            position += 1
            if position % 2 == 0:
                swapped_string += char.lower()
            else:
                swapped_string += char.upper()

    return swapped_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True