"""
Problem: Write a function that takes a string and returns a dictionary containing the following three properties:

    - the percentage of characters in the string that are lowercase letters
    - the percentage of characters that are uppercase letters
    - the percentage of characters that are neither

    - input: string
    - output: a dictionary with a string:string pair
    - Rules:
         -  All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", 
            respectively. Each value should be rounded to two decimal points.
        -   You may assume that the string will always contain at least one character.

Example: See Below

Data Structure: Dictionary

Algorithm:

- letter_percentages(input_string)

    - divisor: get length of string
    - initiate lower_count = 0
    - initiate upper_count = 0
    - initiate other_count = 0
    - for char in string:
        - if char.islower():
            lower_count += 1
        - elif char.isupper():
            upper_count += 1
        - else:
            other_count += 1
        
    lowercase_percent = str(lower_count / divisor)
    uppercase_percent = str(upper_count / divisor)
    neither_percent = str(other_count / divisor)

    return make_dictionary(lowercase_percent, uppercase_percent, neither_percent)

- make_dictionary(lcp, ucp, np)

    return {'lowercase': lcp,  'uppercase': ucp, 'neither': np}

"""

def letter_percentages(input_string):
    divisor = len(input_string)
    lower_count = 0
    upper_count = 0
    other_count = 0
    for char in input_string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            other_count += 1
        
    lowercase_percent = f"{(lower_count / divisor) * 100:.2f}"
    uppercase_percent = f"{(upper_count / divisor) * 100:.2f}"
    neither_percent = f"{(other_count / divisor) * 100:.2f}"

    dictionary = make_dictionary(lowercase_percent, uppercase_percent, neither_percent)
    return dictionary


def make_dictionary(lcp, ucp, np):

    return {'lowercase': lcp,  'uppercase': ucp, 'neither': np}

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)