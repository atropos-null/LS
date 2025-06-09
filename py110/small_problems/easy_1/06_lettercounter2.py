"""
Problem: Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary 
that shows the number of words of different sizes.
    - input: string, sentence structure
    - output: dictionary, character counts
    - explicit rules: Words consist of any sequence of non-space characters
    - explicit rules: punctuation does not count towards character count

Example: 'Four score and seven.' == {4: 1, 5: 1, 3: 1, 6: 1}

Data Structure: List to collect and Dictionary for final counts

Algorithm:

- split string at spaces
- remove punctuation
- iterate over the list, placing results in the dictionary
- return the dictionary

"""

def word_sizes(text):
    word_dict = {}
    for char in ["'", ",", "-", "@", "!", "?", "."]:
        text = text.replace(char, "")
    split_string = text.split()   
    for element in split_string:
        word_dict[len(element)] = word_dict.get(len(element), 0) + 1
    return word_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})


"""
Optimization:

   def word_sizes(text):
       word_dict = {}
       words = text.split()
       for word in words:
           # Keep only alphabetic characters
           clean_word = ''.join(char for char in word if char.isalpha())
           if clean_word:  # Skip empty strings
               word_dict[len(clean_word)] = word_dict.get(len(clean_word), 0) + 1
       return word_dict

"""