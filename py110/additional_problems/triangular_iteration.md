# PY110-119 Triangular Iteration Problems

## 1. Count Subarray Sums

**Difficulty:​ Intermediate**

Create a function that takes a list of integers and a target sum. The function should return the number of contiguous subarrays that sum to the target value.

```python
def count_subarray_sums(arr, target_sum):

    """
    Count contiguous subarrays that sum to target.
    """
    
    # Your implementation here
    pass

# Test cases
print(count_subarray_sums([1, 2, 3, 4, 5], 9) == 2)     # [4, 5] and [2, 3, 4]
print(count_subarray_sums([1, 1, 1], 2) == 2)           # [1, 1] occurs twice
print(count_subarray_sums([1, -1, 1, -1], 0) == 4)      # [1, -1], [1, -1], [-1, 1], [1, -1, 1, -1]
print(count_subarray_sums([10, 5, 0, 2, 3, -5, 7], 5) == 6)
print(count_subarray_sums([4, 2, 22, 8, 5], 30) == 1)
```

<details>
<summary>Possible Solution</summary>

```python
def count_subarray_sums(arr, target_sum):
    
    count = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == target_sum:
                count += 1
    return count
                
print(count_subarray_sums([1, 2, 3, 4, 5], 9) == 2)     # [4, 5] and [2, 3, 4]
print(count_subarray_sums([1, 1, 1], 2) == 2)           # [1, 1] occurs twice
print(count_subarray_sums([1, -1, 1, -1], 0) == 4)      # [1, -1], [1, -1], [-1, 1], [1, -1, 1, -1] 
print(count_subarray_sums([10, 5, 0, 2, 3, -5, 7], 5) == 6)
print(count_subarray_sums([4, 2, 22, 8, 5], 30) == 1)

#Another Version:

def count_subarray_sums(arr, target_sum):

    final = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i:j+1]) == target_sum:
                final.append(arr[i:j+1])   
    return len(final)

```
</details>

## 2. Longest Palindrome Length

**Difficulty:​ Intermediate**

Create a function that takes a string as an argument and returns the length of the longest palindrome substring in that string. A palindrome reads the same forward and backward.

```python
def longest_palindrome(string):
    """
    Find the length of the longest palindrome substring.
    Args:
        s (str): The input string to analyze

    Returns:
        int: The length of the longest palindrome substring
    """
    # Your implementation here
    pass

# Test cases
print(longest_palindrome("babad") == 3) # "bab" or "aba"
print(longest_palindrome("cbbd") == 2) # "bb"
print(longest_palindrome("a") == 1) # "a"
print(longest_palindrome("") == 0)
print(longest_palindrome("racecar") == 7) # "racecar"
print(longest_palindrome("programming") == 2) # "mm"
print(longest_palindrome("launchschool") == 2) # "oo"
```

<details>
<summary>Possible Solution</summary>

```python
def longest_palindrome(string):
    if not string:
        return 0
    
    elif len(string) == 1:
        return len(string)
    
    else:
        temp = []
      
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                if string[i:j] == string[i:j][::-1]:
                    temp.append(string[i:j])
        
        max_length = len(max(temp, key=len))
        return max_length


print(longest_palindrome("babad") == 3) # "bab" or "aba"
print(longest_palindrome("cbbd") == 2) # "bb"
print(longest_palindrome("a") == 1) # "a"
print(longest_palindrome("") == 0)
print(longest_palindrome("racecar") == 7) # "racecar"
print(longest_palindrome("programming") == 2) # "mm"
print(longest_palindrome("launchschool") == 2) # "oo"

## Another Version

def longest_palindrome(string):
  
    if not string:
        return 0
    
    result = []

    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                result.append(string[i:j+1])
    
    lengths = [len(substring) for substring in result]
    return max(lengths)

```

</details>

## 3. Even Substrings Count

**Difficulty:​ Advanced**

Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. If a substring occurs more than once, count each occurrence as a separate substring.

```python

def even_substrings(string):
    """
    Count the number of even-numbered substrings that can be formed from a string of digits.

    Args:
        string: A string containing only digits

    Returns:
        An integer representing the count of even-numbered substrings
    """
    # Your solution here
    pass

# Test cases
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
```

<details>
<summary>Possible Solution</summary>

```python
def even_substrings(string):
    evens = []
    str_digits = [char for char in string]
    for i in range(len(str_digits) + 1 ):
        for j in range(i+1, len(str_digits) + 1):
            slice = str_digits[i:j]
            joined = "".join(slice)
            digits = int(joined)
            if digits % 2 == 0:
                evens.append(digits)
    return len(evens)
   
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

##Another Version

def even_substrings(string):

    result = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            if int(string[i:j+1]) % 2 == 0:
                result.append(string[i:j+1])
    return len(result)

```

</details>

## 4. Longest Monotonic Substring*

**Difficulty:​ Intermediate**

Create a function called `longest_monotonic` that takes a list of integers and returns the length of the longest monotonic (either entirely non-increasing or entirely non-decreasing) substring.

```python
def longest_monotonic(arr):
    """
    Find the length of the longest monotonic substring.
    Args:
        numbers (list): A list of integers

    Returns:
        int: The length of the longest monotonic subsequence
    """
    # Your implementation here
    pass

# Test cases
print(longest_monotonic([1, 2, 3, 4, 3, 2, 1]) == 4) # [1, 2, 3, 4] is monotonic increasing
print(longest_monotonic([5, 4, 3, 2, 1]) == 5) # The entire array is monotonic decreasing
print(longest_monotonic([1, 1, 2, 3, 3, 4, 5, 4]) == 7) # [1, 1, 2, 3, 3, 4, 5] is monotonic increasing
print(longest_monotonic([9, 8, 8, 7, 6, 7, 8]) == 5) # [9, 8, 8, 7, 6] is monotonic decreasing
print(longest_monotonic([1, 2, 1, 2, 1]) == 2) # Multiple monotonic subarrays of length 2
print(longest_monotonic([]) == 0) # Empty array
print(longest_monotonic([5]) == 1) # Single element is always monotonic
```

<details>
<summary>Possible Solution</summary>

```python

def longest_monotonic(arr):
    if not arr:
        return 0

    non_decreasing = 1
    non_increasing = 1
    max_length = 1

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            non_decreasing += 1
            non_increasing = 1
        elif arr[i] < arr[i-1]:
            non_increasing += 1
            non_decreasing = 1
        elif arr[i] == arr[i-1]:
            non_increasing += 1
            non_decreasing += 1

        if max_length < non_decreasing:
            max_length = non_decreasing

        elif max_length < non_increasing:
            max_length = non_increasing

    return max_length

## Another Version

def longest_monotonic(arr):
    if len(arr) <= 1:
        return len(arr)

    max_len = 1
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            subarray = arr[i:j+1]

            is_non_decreasing = True
            is_non_increasing = True
            for k in range(len(subarray) - 1):
                if subarray[k] > subarray[k+1]:
                    is_non_decreasing = False
                
                if subarray[k] < subarray[k+1]:
                    is_non_increasing = False

            is_monotonic = is_non_decreasing or is_non_increasing
        

            if is_monotonic:
                if len(subarray) > max_len:
                    max_len = len(subarray)
            else:
                break
                
    return max_len

#A third version:

def _find_longest_run(arr, comparison):

    if not arr:
        return 0

    max_len = 1
    current_len = 1
    for i in range(1, len(arr)):
        if comparison(arr[i], arr[i-1]):
            current_len += 1
        else:
            current_len = 1
        max_len = max(max_len, current_len)
    return max_len

def longest_monotonic(arr):
    if not arr:
        return 0
        
    # Longest non-decreasing (e.g., [1, 2, 2, 3])
    longest_non_decreasing = _find_longest_run(arr, lambda a, b: a >= b)
    
    # Longest non-increasing (e.g., [5, 4, 4, 2])
    longest_non_increasing = _find_longest_run(arr, lambda a, b: a <= b)

    return max(longest_non_decreasing, longest_non_increasing)
```

</details>

## 5. Find Sum Pairs

**Difficulty:​ Intermediate**

Write a function that finds all unique pairs in a list that sum to a target value.

```python
def find_pairs(numbers, target_sum):
    """
    Find all unique pairs in a list that sum to a target value.

    Args:
        lst (list): The list of numbers to search
        target (int/float): The target sum value

    Returns:
        list: A list of tuples representing pairs that sum to the target
    """
    # Your implementation here
    pass

# Test cases
print(find_pairs([1, 2, 3, 4, 5], 6) == [(1, 5), (2, 4)])
print(find_pairs([5, 5, 5, 5], 10) == [(5, 5)])
print(find_pairs([1, 2, 3, 4, 5], 10) == [])
print(find_pairs([-1, 0, 1, 2], 1) == [(-1, 2), (0, 1)])
```

<details>
<summary>Possible Solution</summary>

```python
def find_pairs(numbers, target_sum):

    tupled = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                pair = (numbers[i], numbers[j])
                if pair not in tupled:
                    tupled.append(pair)
    return tupled

print(find_pairs([1, 2, 3, 4, 5], 6) == [(1, 5), (2, 4)])
print(find_pairs([5, 5, 5, 5], 10) == [(5, 5)])
print(find_pairs([1, 2, 3, 4, 5], 10) == [])
print(find_pairs([-1, 0, 1, 2], 1) == [(-1, 2), (0, 1)])
```

</details>

## 6. Longest Palindromic Substring

**Difficulty:​ Advanced**

Implement a function that finds the longest palindromic substring in a given string. A palindrome is a string that reads the same backward as forward.

```python
def longest_palindromic_substring(string):
    """
    Find the longest palindromic substring.
    Args:
       s (str): The input string to search for palindromes

    Returns:
       str: The longest palindromic substring
    """
    # Your code here
    pass

# Test cases
print(longest_palindromic_substring("babad") == "bab") # "aba" would also be valid
print(longest_palindromic_substring("cbbd") == "bb")
print(longest_palindromic_substring("a") == "a")
print(longest_palindromic_substring("ac") == "a") # Single characters are palindromes
print(longest_palindromic_substring("racecar") == "racecar")
print(longest_palindromic_substring("abcdefgfedcba") == "abcdefgfedcba")


```

<details>
<summary>Possible Solution</summary>

```python
def longest_palindromic_substring(string):

    if not string:
        return 0
    
    elif len(string) == 1 or len(string) == 2:
        return string[0]
    
    else:
        temp = []
      
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                if string[i:j] == string[i:j][::-1]:
                    temp.append(string[i:j])
        
        max_length = max(temp, key=len)
        return max_length

   
print(longest_palindromic_substring("babad") == "bab") # "aba" would also be valid
print(longest_palindromic_substring("cbbd") == "bb")
print(longest_palindromic_substring("a") == "a")
print(longest_palindromic_substring("ac") == "a") # Single characters are palindromes
print(longest_palindromic_substring("racecar") == "racecar")
print(longest_palindromic_substring("abcdefgfedcba") == "abcdefgfedcba")

## Slightly different version:

def longest_palindromic_substring(string):
 
    result = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                result.append(string[i:j+1])

    max_length = max(result, key=len)
   
    return max_length
```

</details>

## 7. Subarray Sum Indices
**Difficulty:​ Advanced**

Write a function that takes a list of integers and a target sum. Return a list containing the indices of the first subarray found whose elements sum to the target. If no such subarray exists, return an empty list.

```python
def sub_array_sum(array, target_sum):
    """
    Find indices of first subarray that sums to target.
    """
    # Your implementation here
    pass

# Test cases
print(sub_array_sum([1, 2, 3, 4, 5], 9) == [1, 3])    # elements at indices 1,2,3 (values 2,3,4) sum to 9
print(sub_array_sum([10, 5, 1, 2, 3, 4], 15) == [0, 1]) # elements at indices 0,1 (values 10,5) sum to 15
print(sub_array_sum([3, 2, 5, 4, 1], 10) == [0, 2])    # elements at indices 0,1,2 (values 3,2,5) sum to 10
print(sub_array_sum([1, 2, 3, 4], 20) == [])
```

<details>
<summary>Possible Solution</summary>

```python

def sub_array_sum(array, target_sum):
    indices = []
   
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if current_sum == target_sum:
                indices.append(i)
    return indices
   
print(sub_array_sum([1, 2, 3, 4, 5], 9) == [1, 3])    # elements at indices 1,2,3 (values 2,3,4) sum to 9
print(sub_array_sum([10, 5, 1, 2, 3, 4], 15) == [0, 1]) # elements at indices 0,1 (values 10,5) sum to 15
print(sub_array_sum([3, 2, 5, 4, 1], 10) == [0, 2])    # elements at indices 0,1,2 (values 3,2,5) sum to 10
print(sub_array_sum([1, 2, 3, 4], 20) == [])

## Another Version

def sub_array_sum(array, target_sum):

    indices = []
   
    for i in range(len(array)):
        for j in range(i, len(array)):
            if sum(array[i:j+1]) == target_sum:
                indices.append(i)
                indices.append(j)
                return indices
    
    if not indices:
        return []
```

</details>

## 8. Maximum Subarray Sum

**Difficulty:​ Advanced** 

Create a function that finds the contiguous subarray with the largest sum and returns that sum. A subarray must contain at least one element.

```python
def find_max_subarray_sum(array):
    """
    Find the maximum sum of any contiguous subarray.
    Args:
       numbers (list): A list of integers

    Returns:
       int: The sum of the contiguous subarray with the largest sum
    """
    # Your implementation here
    pass

# Test cases
print(find_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6) # subarray [4, -1, 2, 1]
print(find_max_subarray_sum([1]) == 1)
print(find_max_subarray_sum([-1, -2, -3]) == -1)
print(find_max_subarray_sum([5, -3, 5]) == 7)
```
<details>
<summary>Possible Solution</summary>

```python
def find_max_subarray_sum(array):
    max_sum = 0
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if abs(current_sum) > abs(max_sum):
                max_sum = current_sum

    return max_sum

# Test cases
print(find_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6) # subarray [4, -1, 2, 1]
print(find_max_subarray_sum([1]) == 1)
print(find_max_subarray_sum([-1, -2, -3]) == -1)
print(find_max_subarray_sum([5, -3, 5]) == 7)

# Another Version:

def find_max_subarray_sum(array):

    current_max = array[0]
    for i in range(len(array)):
        for j in range(i, len(array)):
            summed = sum(array[i:j+1])
            if summed > current_max:
                current_max = summed
    
    return current_max
```

</details>

## 9. Longest Unique Substring

**Difficulty:​ Advanced**

Create a function that takes a string and returns the longest substring that contains unique characters (no duplicates). If there are multiple such substrings of the same length, return the one that appears first in the string. Struggled with this one!

```python
def longest_unique_substring(string):
    """
    Find the longest substring with unique characters.
    Args:
       s (str): The input string

    Returns:
       str: The longest substring with unique characters
    """
    # Your implementation here
    pass

# Test cases
print(longest_unique_substring("abcabcbb") == "abc")
print(longest_unique_substring("bbbbb") == "b")
print(longest_unique_substring("pwwkew") == "wke")
print(longest_unique_substring("dvdf") == "vdf")
print(longest_unique_substring("abcdeafbdgcbb") == "eafbdgc")
```

<details>
<summary>Possible Solution</summary>

```python
def has_unique_characters(substring):
    return len(set(substring)) == len(substring)

def substrings(string):
    results = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            results.append(string[i:j+1])
    return results

def longest_unique_substring(string):
    if not string:
        return ""

    all_substrings = substrings(string)
    longest_so_far = ''

    for sub in all_substrings:
        if has_unique_characters(sub):
            if len(sub) > len(longest_so_far):
                longest_so_far = sub
    
    return longest_so_far

print(longest_unique_substring("abcabcbb") == "abc")
print(longest_unique_substring("bbbbb") == "b")
print(longest_unique_substring("pwwkew") == "wke")
print(longest_unique_substring("dvdf") == "vdf")
print(longest_unique_substring("abcdeafbdgcbb") == "eafbdgc")

#Another Version:

def longest_unique_substring(string):
    
    result = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if len(substring) == len(set(substring)):
                result.append(substring)
    return max(result, key=len)

```

</details>

## 10. Closest Numbers

**Difficulty:​ Advanced**

Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

```python
def closest_numbers(numbers):
    """
    Find the pair of numbers with the smallest difference.
    Args:
       numbers (list): A list of integers

    Returns:
       tuple: A tuple of two numbers that are closest together in value
    """
    # Your implementation here
    pass

# Test cases
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 7, 17]) == (12, 7))
```

<details>
<summary>Possible Solution</summary>

```python
def closest_numbers(numbers):
    
    lookups = {}
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            pair = (numbers[i], numbers[j])
            lookups[pair] = difference

    minimums = min(lookups, key=lookups.get)
    return minimums

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 7, 17]) == (12, 7))

#Another Version:

def closest_numbers(numbers):
  
    counts = {}
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            counts[difference] = counts.get(difference, (numbers[i], numbers[j]))
    
    min_key = min(counts.keys())
    return counts[min_key]

```
</details>

## 11. Easy-4 All Substrings from Small Problems.

Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

```python
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
```

<details>
<summary>Possible Solution</summary>

```python
def substrings(input_string):
    tmp = []
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            tmp.append(input_string[i:j+1])
    return tmp

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
```
</details>

## 12. Lo Numbers

Write a function that accepts a string and outputs a list of strings. 

* The first string in the output list should be the concatenation of the first and 
* last letter of the string.  Each subsequent string should 'move inwards' 
* towards the center of the string. 

```python
LO_NUMBERS = {
    'pa' : '1',
    'vo' : '4',
    'ze' : '7',
    're' : '2',
    'mu' : '5',
    'bi' : '8',
    'ci' : '3',
    'xa' : '6',
    'so' : '9',
    'no' : '0',
}

print(convert_lojban('renonore') == 2002)  # 2002
```

<details>
<summary>Possible Solution</summary>

```python

def convert_lojban(string):
    temp = []
    final = []
    k = 2
    for i in range(len(string)-1):
        temp.append(string[i:i+k])
    
    for element in temp:
        for keys in LO_NUMBERS.keys():
            if element in keys:
                final.append(LO_NUMBERS[keys])
        
    return int("".join(final))
```
</details>

## 13. Either Ends

Write a function that slices off the first and last letters of a string and combines them into a returned list. Note: This does not use a nested for loop. But its important to know when to use one and when not to. And when not to, how to slice appropriately. 

```python

string = 'lorem ipsum'
print(either_end(string) == ['lm', 'ou', 'rs', 'ep', 'mi', ' '])

string = 'helloworld'
print(either_end(string) == ['hd', 'el', 'lr', 'lo', 'ow',])

string = '1234'
print(either_end(string) == ['14', '23'])

string = ''
print(either_end(string) == [])
```

<details>
<summary>Possible Solution</summary>

```python

def either_end(input_str):

    if not input_str:
        return []

    result = []
  
    for i in range((len(input_str) + 1) // 2):
        if len(input_str) %2  == 1:
            if i == (len(input_str) - 1) // 2:
                result.append(input_str[i])
            else:
                snippet = input_str[i]+input_str[-(i+1)]
                result.append(snippet)

        else:
            snippet = input_str[i]+input_str[-(i+1)]
            result.append(snippet)
    return result

#Another Version

def either_end(input_str):
    list_result = []
    split_words = [char for char in input_str]
    while len(split_words) > 1:
        front = split_words[0]
        back = split_words[-1]
        list_result.append(front+back)
        split_words.pop(0)
        split_words.pop(-1)
    
    if len(split_words) == 1:
        list_result.append(split_words[0])
    
    return list_result

```
</details>