"""
Problem: Write a function that returns a list of all palindromic substrings of a string. That is, each substring must 
consist of a sequence of characters that reads the same forward and backward. The substrings in the returned list should 
be sorted by their order of appearance in the input string. Duplicate substrings should be included multiple times.

- input: a string
- output: a list
- rules:
    - each substring can be read forward and backward
    - sorted in order of appearance in the input string
    - duplicate strings can be included

- Example: 'madam' ==> ['madam', 'ada']

- Data structure: Holding lists, 2 probabaly

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

    - is palindrome algorithm if length of word is greater than 1 AND its the same read one way and in reverse string[::-1]

    - main function: list of the resut of substrings that went through is_palindromes


"""

def palindromes(string):
      return [substring for substring in substrings(string) if is_palindrome(substring)]
 

def is_palindrome(word):
    return len(word) > 1 and word == word[::-1]

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
   



print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True