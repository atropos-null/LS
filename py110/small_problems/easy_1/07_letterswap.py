"""
Problem: Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.
    - input: string
    - output: string
    - explicit: first and last letters swapped
    - explicit: string is 1 character or greater
    - explicit: no empty strings
    - implicit: no cleaning the string of punctuation or extra spaces 

Example: 'Abcde' == "ebcdA"

Data Structure: List to hold the intermediate steps

Algorithm:
    - split string into elements
    - create empty list to hold the worked on characters
    - iterate over the elements of the list.
        - if the element is one character, just append to the list.
        - else 
            - the first character is sliced from word[0] and saved into a variable
            - the last character is sliced from word[-1] and saved into a variable
            - middle characters are sliced out [1:-1] and saved into a variable
            - a final variable rearranges the order: last + middle + first
            - final variable appended to list
        
        - new string from the joining of the working list

"""

def swap(string):
    words = string.split(" ")
    flipped_words = []
    for word in words:
        if len(word) == 1:
            flipped_words.append(word[0])
        else:
            first_letter = word[0]
            last_letter = word[-1]
            middle = word[1:-1]    
            together = last_letter + middle + first_letter
            flipped_words.append(together)
    sentence = " ".join(flipped_words)
    return sentence


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True


"""
Optimization:

def swap(string):
    words = string.split(" ")
    flipped_words = []
    for word in words:
        first_letter = word[0]
        last_letter = word[-1]
        middle = word[1:-1] if len(word) > 2 else ""
        together = last_letter + middle + first_letter
        flipped_words.append(together)
    return " ".join(flipped_words)

    
"""