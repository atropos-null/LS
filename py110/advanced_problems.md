# PY110/119 Palindrome Specific Practice Problems

## 1. Almost a Palindrome

Write a function that determines if a string can be made a palindrome by deleting at most one character.

```python

def almost_a_palindrome(s):
    """
    Determines if a string can become a palindrome by removing at most one character.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string can be a palindrome by removing 0 or 1 characters,
              False otherwise.
    """
    # Your implementation here
    pass

# Test cases
print(almost_a_palindrome("racecar") == True)      # Already a palindrome
print(almost_a_palindrome("radkar") == True)       # Remove 'k' to get 'radar'
print(almost_a_palindrome("abccdba") == True)      # Remove 'd' to get 'abccba'
print(almost_a_palindrome("abac") == True)         # Remove 'c' to get 'aba'
print(almost_a_palindrome("abca") == True)         # Remove 'b' to get 'aca'
print(almost_a_palindrome("abcdefdba") == False)
print(almost_a_palindrome("a") == True)
print(almost_a_palindrome("ab") == True)

```

<details>
<summary>Show answer</summary>

```python

```
</details>


## 2. Palindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, such that the concatenation of the two words, i.e., words[i] + words[j], is a palindrome.

```python
def palindrome_pairs(words):
    """
    Finds all pairs of indices (i, j) such that words[i] + words[j] is a palindrome.

    Args:
        words (list): A list of unique strings.

    Returns:
        list: A list of lists, where each inner list is a pair of indices [i, j].
              The order of pairs in the output list does not matter.
    """
    # Your implementation here
    pass

# Test cases - The exact order of the sublists in the output doesn't matter.
# For example, for the first test case, [[1, 0], [0, 1]] is also a valid result.
print(palindrome_pairs(["bat", "tab", "cat"]) == [[0, 1], [1, 0]])
print(palindrome_pairs(["dog", "cow", "god"]) == [[0, 2], [2, 0]])
print(palindrome_pairs(["race", "car"]) == [[0, 1]])
print(palindrome_pairs(["a", ""]) == [[0, 1], [1, 0]])
print(palindrome_pairs(["s", "ss"]) == [[0, 1], [1, 0]])
print(palindrome_pairs(["level", "noon", "radar", "kayak"]) == [])
```

<details>
<summary>Show answer</summary>
</details>

## 3. Palindromic Substrings

Write a function that returns a list of all palindromic substrings of a string. Each substring must consist of a sequence of characters that reads the same forward and backward. The substrings in the returned list should be sorted by their order of appearance in the input string. Duplicate substrings should be included multiple times.

For the purpose of this exercise, you should consider all characters and pay attention to case; that is, `'AbcbA'` is a palindrome, but `'Abcba' `and `'Abc-bA'` are not. Single characters are not palindromes.

Hint: You may want to create a helper function that finds all substrings of a string first.

```python
    """
    Finds all palindromic substrings in a string.

    Args:
        text (str): The input string.

    Returns:
        list: A list of palindromic substrings, ordered by appearance.
    """
    # Your implementation here
    pass

# Test cases
print(palindromes('abcd') == [])
print(palindromes('madam') == ['madam', 'ada'])
print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])
print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])
```

<details>
<summary>Show answer</summary>
</details>


## 4.  Palindrome Partitioning

Write a function that takes a string and returns a list of all possible ways to partition the string such that every part of the partition is a palindrome. Each part must be a substring of the original string.

```python
def partition_palindromes(s):
    """
    Partitions a string into all possible combinations of palindromic substrings.

    Args:
        s (str): The input string.

    Returns:
        list: A list of lists, where each inner list represents a valid
              palindrome partition. The order of partitions does not matter.
    """
    # Your implementation here
    pass

# Test cases (the order of the outer list and inner lists may vary)
print(partition_palindromes("aab") == [['a', 'a', 'b'], ['aa', 'b']])
print(partition_palindromes("a") == [['a']])
print(partition_palindromes("racecar") == [['r', 'a', 'c', 'e', 'c', 'a', 'r'], ['r', 'aceca', 'r'], ['racecar']])
```

<details>
<summary>Show answer</summary>
</details>

## 5. Longest "Real" Palindrome*

Write a function that finds the longest substring that is a "real" palindrome. A "real" palindrome is determined by ignoring case and non-alphanumeric characters. The function should return the original substring from the input string, not the cleaned-up version. If there's a tie for the longest, return the one that appears first.

```python
def longest_real_palindrome(s):
    """
    Finds the longest substring which is a case-insensitive, alphanumeric palindrome.

    Args:
        s (str): The input string.

    Returns:
        str: The original substring that forms the longest "real" palindrome.
    """
    # Your implementation here
    pass

# Test cases
print(longest_real_palindrome("Madam, I'm Adam") == "Madam, I'm Adam")
print(longest_real_palindrome("a race's car") == "a race's car")
print(longest_real_palindrome("Was it a car or a cat I saw?") == "a car or a cat I saw")
print(longest_real_palindrome("ab-A_c_d_c_b_a-de") == "ab-A_c_d_c_b_a")
print(longest_real_palindrome("12321") == "12321")
print(longest_real_palindrome("forgeeksskeegfor") == "geeksskeeg")
```

<details>
<summary>Show answer</summary>
</details>

## 6. Palindromic Number

Write a function that takes an integer and returns True if the integer is a palindrome, and False otherwise. You may ​not​ convert the integer to a string to solve this problem.

Note:
* Negative numbers are not considered palindromes.
* Any number that ends in 0 (and is not 0 itself) cannot be a palindrome (e.g., 10, 120).

```python
def is_palindrome_number(x):
    """
    Checks if an integer is a palindrome without converting it to a string.

    Args:
        x (int): The integer to check.

    Returns:
        bool: True if the integer is a palindrome, False otherwise.
    """
    # Your implementation here
    pass

# Test cases
print(is_palindrome_number(121) == True)
print(is_palindrome_number(-121) == False)
print(is_palindrome_number(10) == False)
print(is_palindrome_number(0) == True)
print(is_palindrome_number(123454321) == True)
print(is_palindrome_number(12344321) == True)
print(is_palindrome_number(123) == False)
```

<details>
<summary>Show answer</summary>
</details>

## 7. Shortest Palindrome Prefix

Write a function that takes a string s and transforms it into a palindrome by adding characters in front of it.

Your function should return the shortest possible palindrome that can be formed this way.

```python

def shortest_palindrome_prefix(s):
    """
    Finds the shortest palindrome by adding a prefix to the string.

    Args:
        s (str): The original string.

    Returns:
        str: The shortest palindrome created by adding characters to the front.
    """
    # Your implementation here
    pass

# Test cases
print(shortest_palindrome_prefix("aacecaaa") == "aaacecaaa") # Add "aa" to the front
print(shortest_palindrome_prefix("abcd") == "dcbabcd")     # Add "dcb" to the front
print(shortest_palindrome_prefix("race") == "ecarace")     # Add "eca" to the front
print(shortest_palindrome_prefix("a") == "a")
print(shortest_palindrome_prefix("level") == "level")
```

<details>
<summary>All rights reserved</summary>

```python

def to_palindrome(string):

    if string.lower() == string[::-1].lower():
            return string
    
    for i in range(len(string)):
        front = string[:i]
        back = string[i+1:]
        snippet = front + back
        if snippet.lower() == snippet[::-1].lower():
             return snippet

    
print(to_palindrome('reviver') == 'reviver')
print(to_palindrome('wow!') == 'wow')
print(to_palindrome('woW') == 'woW')
print(to_palindrome('madame') == 'madam')
print(to_palindrome('abcdEFGgfedccbA') == 'abcdEFGgfedcbA')
print(to_palindrome('00 11 22 33 44 33 22 191 00') == '00 11 22 33 44 33 22 11 00')
print(to_palindrome('Step On Not Pets') == 'Step On No Pets')
print(to_palindrome('Clearly this cannot be a palindrome') == None)
```
</details>