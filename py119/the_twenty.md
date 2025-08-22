## The Twenty

### Problem 1

Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

```python

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2]) #True
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0]) #True
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3]) #True
print(smaller_numbers_than_current([1]) == [0]) #True

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result) #True

```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 2

Create a function that takes a list of integers as an argument. The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return `None`.

```python

print(minimum_sum([1, 2, 3, 4]) is None) #True
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9) #True
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15) #True
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16) #True
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10) #True

```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 3

Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

```python

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected) #True

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected) #True

print(to_weird_case('aaA bB c') == 'aaA bB c') #True

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected) #True

```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 4

Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

```python
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11)) #True
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27)) #True
print(closest_numbers([12, 22, 7, 17]) == (12, 7)) #True
```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 5

Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.

```python

print(most_common_char('Hello World') == 'l') #True
print(most_common_char('Mississippi') == 'i') #True
print(most_common_char('Happy birthday!') == 'h') #True
print(most_common_char('aaaaaAAAA') == 'a') #True

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p') #True

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e') #True

```


<details>
<summary>Possible Solution</summary>

</details>

### Problem 6

Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.

```python

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected) #True

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected) #True

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected) #True

print(count_letters('x') == {'x': 1}) #True
print(count_letters('') == {}) #True
print(count_letters('!!!') == {}) #True

```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 7

Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in `[1, 2, 3, 2, 1]` is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For instance, for `[1, 1, 1, 1]` and `[2, 2, 2, 2, 2]`, the function should return 2. The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

```python

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3) #True
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4) #True
print(pairs([]) == 0) #True
print(pairs([23]) == 0) #True
print(pairs([997, 997]) == 1) #True
print(pairs([32, 32, 32]) == 1) #True
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3) #True

```

### Problem 8

Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".

```python

print(longest_vowel_substring('cwm') == 0) #True
print(longest_vowel_substring('many') == 1) #True
print(longest_vowel_substring('launchschoolstudents') == 2) #True
print(longest_vowel_substring('eau') == 3) #True
print(longest_vowel_substring('beauteous') == 3) #True
print(longest_vowel_substring('sequoia') == 4) #True
print(longest_vowel_substring('miaoued') == 5) #True

```

<details>
<summary>Possible Solution</summary>

</details>


### Problem 9

Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. Note that overlapping strings don't count: `'babab'` contains 1 instance of `'bab'`, not 2.

You may assume that the second argument is never an empty string.

```python

print(count_substrings('babab', 'bab') == 1) #True
print(count_substrings('babab', 'ba') == 2) #True
print(count_substrings('babab', 'b') == 3) #True
print(count_substrings('babab', 'x') == 0) #True
print(count_substrings('babab', 'x') == 0) #True
print(count_substrings('', 'x') == 0) #True
print(count_substrings('bbbaabbbbaab', 'baab') == 2) #True
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2) #True
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1) #True

```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 10

Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of `'1432'`, the even-numbered substrings are `'14'`, `'1432'`, `'4'`, `'432'`, `'32'`, and `'2'`, for a total of 6 substrings. Identical to Triangular Iteration #3.

If a substring occurs more than once, you should count each occurrence as a separate substring.

```python

print(even_substrings('1432') == 6) #True
print(even_substrings('3145926') == 16) #True
print(even_substrings('2718281') == 16) #True
print(even_substrings('13579') == 0) #True
print(even_substrings('143232') == 12) #True

```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 11

Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to each other such that `s == t * k`. The values of `t` and `k` should be the shortest possible substring and the largest possible repeat count that satisfies this equation. Identical to SPOT Wiki #8.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

```python

print(repeated_substring('xyzxyzxyz') == ('xyz', 3)) #True
print(repeated_substring('xyxy') == ('xy', 2)) #True
print(repeated_substring('xyz') == ('xyz', 1)) #True
print(repeated_substring('aaaaaaaa') == ('a', 8)) #True
print(repeated_substring('superduper') == ('superduper', 1)) #True
```

<details>
<summary>Possible Solution</summary>

</details>


### Problem 12

Create a function that takes a string as an argument and returns `True` if the string is a pangram, `False` if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

```python

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True) #True
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False) #True
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True) #True
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False) #True
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True) #True

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True) #True
```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 13

Create a function that takes two strings as arguments and returns `True` if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return `False`.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

```python

print(unscramble('ansucchlohlo', 'launchschool') == True) #True
print(unscramble('phyarunstole', 'pythonrules') == True) #True
print(unscramble('phyarunstola', 'pythonrules') == False) #True
print(unscramble('boldface', 'coal') == True) #True
print(unscramble('olc', 'cool') == False) #True
```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 14

Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

```python

print(seven_eleven(10) == 7) #True
print(seven_eleven(11) == 7) #True
print(seven_eleven(12) == 18) #True
print(seven_eleven(25) == 75) #True
print(seven_eleven(100) == 1153) #True
print(seven_eleven(0) == 0) #True
print(seven_eleven(-100) == 0) #True

```

<details>
<summary>Possible Solution</summary>

</details>


### Problem 15

Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

```python

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6 #True
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6 #True
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8 #True
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6 #True
```

<details>
<summary>Possible Solution</summary>

</details>


### Problem 16

Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

```python

print(distinct_multiples('xyz') == 0)               # (none) #True
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z #True
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z #True
print(distinct_multiples('unununium') == 2)         # u, n #True
print(distinct_multiples('multiplicity') == 3)      # l, t, i #True
print(distinct_multiples('7657') == 1)              # 7 #True
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9 #True
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5 #True

```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 17

Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equals the closest prime number that is greater than the current sum of the numbers. For example, the numbers in `[1, 2, 3]` sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

```python

# All print to True
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

```

<details>
<summary>Possible Solution</summary>

</details>

### Problem 18
Create a function that takes a list of integers as an argument. Determine and return the index N for which all numbers with an index less than N sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.

```python

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3) #True
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1) #True
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0) #True
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1) #True

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0) #True

```
<details>
<summary>Possible Solution</summary>

</details>

### Problem 19

Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. There will always be exactly one such integer in the input list.

```python

print(odd_fellow([4]) == 4) #True
print(odd_fellow([7, 99, 7, 51, 99]) == 51) #True
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7) #True
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6) #True
print(odd_fellow([0, 0, 0]) == 0) #True

```

<details>
<summary>Possible Solution</summary>

</details>


### Problem 20

Create a function that takes a list of numbers, all of which are the same except one. Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers, and there will always be exactly one number that is different.

```python
print(what_is_different([0, 1, 0]) == 1) #True
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7) #True
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11) #True
print(what_is_different([3, 4, 4, 4]) == 3) #True
print(what_is_different([4, 4, 4, 3]) == 3) #True
```

<details>
<summary>Possible Solution</summary>

</details>