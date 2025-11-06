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

```python

```
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

```python

```
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

```python

```
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

```python

```
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

```python

```
</details>


## 7. Lexicographically Smallest Palindrome

Given a string s, determine if its characters can be rearranged to form a palindrome. If they can, return the lexicographically smallest palindrome that can be formed. If not, return the string "not possible".

The lexicographically smallest string is the one that would appear first in a dictionary.

```python

def smallest_palindrome(s):
    """
    Rearranges a string to form the lexicographically smallest palindrome.

    Args:
        s (str): The input string of lowercase letters.

    Returns:
        str: The smallest palindrome or "not possible".
    """
    # Your implementation here
    pass

# Test cases
print(smallest_palindrome("aabbc") == "abcba")
print(smallest_palindrome("aabbcd") == "not possible")
print(smallest_palindrome("zyxwzxy") == "wxyzxyw")
print(smallest_palindrome("racecar") == "acecrace")
print(smallest_palindrome("level") == "elvle")
print(smallest_palindrome("a") == "a")
```

<details>
<summary>Show answer</summary>

```python

```
</details>

## 8. Longest Palindrome from Two-Letter Words

You are given a list of strings, where each string consists of two lowercase English letters. Create a function to find the length of the longest palindrome that can be built by concatenating some of the elements from the list. Each string can be used at most once.

```python

def longest_palindrome_from_words(words):
    """
    Finds the length of the longest palindrome by concatenating two-letter words.

    Args:
        words (list): A list of two-letter strings.

    Returns:
        int: The length of the longest possible palindrome.
    """
    # Your implementation here
    pass

# Test cases
# "lc" + "gg" + "cl" = "lcggcl"
print(longest_palindrome_from_words(["lc", "cl", "gg"]) == 6)
# "ty" + "lc" + "cl" + "yt" = "tylcclyt"
print(longest_palindrome_from_words(["ab", "ty", "yt", "lc", "cl", "ab"]) == 8)
# "cc", "ll", "oo", "dd" can't form pairs, but one can be a center.
# "ab" and "ba" form a pair. "abccba"
print(longest_palindrome_from_words(["cc", "ll", "ab", "ba"]) == 6)
print(longest_palindrome_from_words(["zz","zz"]) == 4)
```

<details>
<summary>Show answer</summary>

```python

```
</details>

## 9.  Next Palindromic Time

Write a function that takes a time string in "HH:MM" format and returns the next closest palindromic time. A time is palindromic if its string representation (ignoring the colon) reads the same forwards and backwards. For example, "05:50" is palindromic because "0550" is a palindrome. The function should correctly handle rollovers into the next day.

```python

def next_palindromic_time(time_str):
    """
    Finds the next palindromic time after the given time.

    Args:
        time_str (str): The start time in "HH:MM" format.

    Returns:
        str: The next palindromic time in "HH:MM" format.
    """
    # Your implementation here
    pass

# Test cases
print(next_palindromic_time("23:50") == "00:00")
print(next_palindromic_time("01:20") == "01:10") # Typo in example, should be "02:20"
# Correcting logic based on "next closest"
print(next_palindromic_time("01:20") == "02:20")
print(next_palindromic_time("05:30") == "05:50")
print(next_palindromic_time("15:10") == "15:51")
print(next_palindromic_time("20:00") == "20:02")
print(next_palindromic_time("12:12") == "12:21")
print(next_palindromic_time("23:59") == "00:00")
```

<details>
<summary>Show answer</summary>

```python

```
</details>

## 10. Palindrome Permutation

Write a function that takes a string and determines if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. For this problem, character case and non-alphanumeric characters should be ignored.

```python

def is_palindrome_permutation(s):
    """
    Checks if a string can be rearranged to form a palindrome.

    Args:
        s (str): The input string.

    Returns:
        bool: True if any permutation of the string is a palindrome.
    """
    # Your implementation here
    pass

# Test cases
# "Tact Coa" can be rearranged to "taco cat", "atco cta", etc.
print(is_palindrome_permutation('Tact Coa') == True)
print(is_palindrome_permutation('aabbc') == True)
print(is_palindrome_permutation('aabbcd') == False)
print(is_palindrome_permutation('a') == True)
print(is_palindrome_permutation('Able was I ere I saw Elba') == True)
print(is_palindrome_permutation('Launch School') == False)
```

<details>
<summary>Show answer</summary>

```python

```
</details>

## 11. Numerical Palindrome

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. 
Examples of numerical palindromes are:

```
2332 
110011 
54322345
```

You'll be given 2 numbers as arguments: `(num, s)`. 

Write a function which returns a list of `s` number of numerical palindromes that come after `num`. If `num` is a palindrome itself, it should be included in the count. 

Single digit numbers will NOT be considered numerical palindromes. 

```python

def palindrome(num, s):
    ...

print(palindrome(6,4) == [11,22,33,44]) # True
print(palindrome(75,1) == [77]) # True
print(palindrome(101,2) == [101,111]) # True
print(palindrome(0,4) == [11,22,33,44]) # True
```

<details>
<summary>Show answer</summary>

```python

def palindrome(num, s):

    if not s:
        return []
    
    result = []
    while len(result) < s:
        converted = str(num)
        if len(converted) > 1 and converted == converted[::-1]:
            result.append(num)
        num += 1
    
    return result

print(palindrome(6,4) == [11,22,33,44]) # True
print(palindrome(75,1) == [77]) # True
print(palindrome(101,2) == [101,111]) # True
print(palindrome(0,4) == [11,22,33,44]) # True

#Version 2:

def is_palindrome(n):
    converted = str(n)
    return len(converted) > 1 and converted == converted[::-1]

def palindrome(num, s):
    if not s:
        return []
    
    result = []
    while len(result) < s:
        if is_palindrome(num):
            result.append(num)
        num += 1
    
    return result

```
</details>