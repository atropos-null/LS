"""

Problem: 
    - Write a function that takes a string
    - doubles every character in the string
    - returns the result as a new string.

    - input: string
    - output: string

Example: 'Hello' => "HHeelllloo"

Data Structure: Lists for holding 

Algo:
    - initialize holding list
    - initalize chars list
    - for char in string, append char to list
    - for char in chars
        - holding_list.append(char * 2)
    - join holding list
    - return string

"""

def repeater(text):
    temp_list = []
    chars = []
    for char in text:
        chars.append(char)
    for char in chars:
        temp_list.append(char * 2)
    result = "".join(temp_list)
    return result

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True


"""

Further Optimization:

def repeater(text):
    temp_list = []
    for char in text:
        temp_list.append(char * 2)
    result = "".join(temp_list)
    return result

"""