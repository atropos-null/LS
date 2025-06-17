"""
Write a function that counts the number of occurrences of each element in a given list. Once counted, 
print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

Problem: Count the number of occurences an element in a list occurs. Once counted, print each element alongisde occurences.
    - input: list of strings
    - output: looped f string with number of occurences.

Data Structure: Dictionary

Algorithm:
    - initialize dictionary
    - for element in list:
        print f-string, element, count
    
"""

def count_occurrences(list1):
    result = {}
    for element in list1:
         result[element] = result.get(element, 0) + 1
    for key, value in result.items():
         print(f"{key} ==> {value}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
