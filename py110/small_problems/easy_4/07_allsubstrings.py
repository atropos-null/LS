"""
Problem: Write a function that returns a list of all substrings of a string. 
Order the returned list by where in the string the substring begins. 
This means that all substrings that start at index position 0 should come first, 
then all substrings that start at index position 1, and so on. 
Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.
"""

def substrings(string):

    temp1 = [char for char in string]
    sublist = []
    temp2 = []
    while temp1 != []:
        length = len(temp1)
        for i in range(length):
            if sublist == []:
                sublist.append(temp1[0])
            else: 
                sublist.append(sublist[-1] + temp1[i])
        temp1.pop(0)
        temp2.extend(sublist)
        sublist.clear()
    return temp2


expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",]

print(substrings('abcde') == expected_result)  # True