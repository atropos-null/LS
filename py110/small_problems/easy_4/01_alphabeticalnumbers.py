"""
Problem: Write a function that...
    - input: takes a list of integers between 0 and 19 
    - output: returns a list of those integers sorted based on the English word for each number:
        "zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, 
        fourteen, fifteen, sixteen, seventeen, eighteen, nineteen"

Example:    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ==> 
            8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0

Data Structure: 2 dictionaries to hold values, temporary list for handling

Algorithm:
    - initialize dictionary with {1: 'one'}, etc
    - for loop:
        - for element in passed list
            - look up value in num to string dictionary
            - append element to holding list
    
    - sort holding list
    - for loop:
        - for element in holding list
            - look up value in string to num dictionary
            - append to list
        - return holding list
"""

num_to_string = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
                 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                 17: "seventeen", 18: "eighteen", 19: "nineteen"}

string_to_num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
                 "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
                  "eighteen": 18, "nineteen": 19}

def alphabetic_number_sort(lst):
    
    temp = sorted([num_to_string[element] for element in lst if element in num_to_string.keys()])
    result = [string_to_num[element] for element in temp if element in string_to_num.keys()]
    return result
    

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result) #True