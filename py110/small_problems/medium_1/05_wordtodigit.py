"""
Problem: Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" 
-- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding 
digit character. You may assume that the string does not contain any punctuation.

    - input: a string that has a number word or words in it
    - output: a string that keeps the regular words but converts the number words to number type words.
    - rules:
        - not actual integers

Example: See below, there is only one test

Data Structure: Dictionary, empty dictionary for holding

Algorithm:
    - initialize dictionary with key as number words and values as digits
    - empty dictionary for holding
    - for word in string:
        - if word not in dictionary
        - append word as is to holding list
        - if word in dictionary,
            append value to holding list
        - join the holding list
        - return string

"""

def word_to_digit(message):
    
    word_digit_dict = {'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'}

    temp = []
    for keys, values in word_digit_dict.items():
        for word in message:
            if word not in keys:
                temp.append(word)
            else:
                temp.append(values)
    converted_string = ",".join(temp)
    print(converted_string)
    return converted_string
    

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True