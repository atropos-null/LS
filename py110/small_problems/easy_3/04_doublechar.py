"""
Problem: Write a function that...
    - input: string
    - action:  doubles every consonant in the string
    - output: returns the result as a new string. 
    
    - Rules: The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

Example: 'Hello-World!' => "HHellllo-WWorrlldd!"

Data Structure: List for holding

Algo:
    - string for holding consonants
    - list for temporary holds before joining
    - for char in text:
        if char in consonants list
            append.(char*2)
        else:
            append(char)
    - new string as join list
    - return  new string
    
"""

def double_consonants(text):
    CONSONANTS = 'bcdfghjklmnpqrstvwxzy'
    temp_list = []
    for char in text:
        if char.casefold() in CONSONANTS:
            temp_list.append(char * 2)
        else:
            temp_list.append(char)
    result = "".join(temp_list)
    return result

# All of these examples should print True

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")