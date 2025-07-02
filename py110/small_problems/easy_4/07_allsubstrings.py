"""
Problem: Write a function that returns a list of all substrings of a string. 
    - input: a string
    - output: a list of substring possibilities
    - to do:
        - Order the returned list by where in the string the substring begins. 
    - rules:
        - This means that all substrings that start at index position 0 should come first, 
        - then all substrings that start at index position 1, and so on. 
        - Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

Example: See the string and expected result

Data Structure: 3 different lists. 1 to be the standard of where we are in the process, 2 to be the final collector of all the substrings
and a 3rd to be the sublist that extends to the final list.

Algorithm:
    - initialize standard, that breaks up the characters in the string and collects in a list.
    - initalize working, the sublist that does the ferrying of substrings to the final list
    - initialize final, the final collection

    - while standard is not empty:
        - get length of the list, but it has to be separate because it will decrement
        - iterate over the length of the list
            - first character from standard goes directly into the working list
            - next character appends to the first character of the standard list
            - next character appends to the previous entry into the working list
            
            - after loop finishes, the first character in the standard list is popped
            - the sublist extends to the final list
            - the sublist is cleared

    - return final list

                
"""

def substrings(string):

    standard = [char for char in string]
    working = []
    final = []
    while standard != []:
        length = len(standard)
        for i in range(length):
            if working == []:
                working.append(standard[0])
            else: 
                working.append(working[-1] + standard[i])
        standard.pop(0)
        final.extend(working)
        working.clear()
    return final


expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",]

print(substrings('abcde') == expected_result)  # True