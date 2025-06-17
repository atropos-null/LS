"""
Alphabet Symmetry

Consider the word "abode".
The letter `a` is in position 1 and `b` is in position 2.
In the alphabet, `a` and `b` are also in positions 1 and 2.

The letters `d` and `e` in "abode" occupy the positions they would occupy in the alphabet, which are positions 4 and 5. 

Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) // [4, 3, 1]

Input will consist of alphabetic characters, both uppercase and lowercase. No spaces.


roblem: in a given string, which is an element in a list, find if the letter position meets its alphabetic position, if so, count how many letters meet the requirement, return the number count in a list

    - input: list, of strings
    - output: list, of integer
    - explicit: make it case insensitive
    - explicit: don't have to worry about spaces

Example: ["abode","ABc","xyzD"]) ==> [4, 3, 1]

Data Structure: Dictionary

Algorithm:
    - initialize empty list, result
    - initialize a dictionary carrying letter and position number
    - counter, integer set to 0
    - loop over element in list 
        - loop over the characters in the element, 
        for character in range(1, len(list)+1)
            - if character[i+1] == dictionary.get(character)
                - increment count by 1
        - append list with count
        - reset count back to 0
        
    - return result list

"""


def solve(lst):

    abc = {"a": 1,
        "b": 2,
        "c": 3, 
        "d": 4, 
        "e": 5, 
        "f": 6, 
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
        }

    result = []
    count = 0

    for element in lst:
        for index, character in enumerate(element.casefold()):
            if index + 1 == abc.get(character):
                count += 1
        result.append(count)
        count = 0
    
    return result

print(solve(["abode","ABc","xyzD"]) == [4,3,1]) # True
print(solve(["abide","ABc","xyz"]) == [4,3,0]) # True
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]) == [6,5,7]) # True
print(solve(["encode","abc","xyzD","ABmD"]) == [1, 3, 1, 3]) # True
