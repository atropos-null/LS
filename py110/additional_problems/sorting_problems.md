## PY 110 Sorting Problems

### 1. Sort Students by Average Grade

**Difficulty**:​ Intermediate

Create a function that takes a list of dictionaries, where each dictionary represents a student with 'name' and 'grades' keys. The 'grades' key contains a list of numerical grades. Return a new list of dictionaries with the same structure, but sorted by the average grade in descending order.

```python

def sort_by_average(students):
    """
    Sort students by average grade in descending order.
    Args:
        students (list): A list of dictionaries with 'name' and 'grades' keys

    Returns:
        list: A new list of dictionaries sorted by average grade in descending order
    """
    # Your implementation here
    pass

# Test cases
students = [
    {'name': 'Alice', 'grades': [85, 90, 88]},
    {'name': 'Bob', 'grades': [70, 80, 75]},
    {'name': 'Charlie', 'grades': [90, 92, 91]}
]
expected = [
    {'name': 'Charlie', 'grades': [90, 92, 91]},
    {'name': 'Alice', 'grades': [85, 90, 88]},
    {'name': 'Bob', 'grades': [70, 80, 75]}
]
print(sort_by_average(students) == expected)

students = [
    {'name': 'David', 'grades': [100, 95]},
    {'name': 'Eve', 'grades': [100, 95]}
]
expected = [
    {'name': 'David', 'grades': [100, 95]},
    {'name': 'Eve', 'grades': [100, 95]}
]
print(sort_by_average(students) == expected)
```

<details>
<summary>Possible Solution</summary>

```python

def sort_by_average(students_dict):
    return sorted(students_dict, key=lambda student: sum(student['grades'])/len(student['grades']), reverse=True)


# Test cases
students = [
    {'name': 'Alice', 'grades': [85, 90, 88]},
    {'name': 'Bob', 'grades': [70, 80, 75]},
    {'name': 'Charlie', 'grades': [90, 92, 91]}
]
expected = [
    {'name': 'Charlie', 'grades': [90, 92, 91]},
    {'name': 'Alice', 'grades': [85, 90, 88]},
    {'name': 'Bob', 'grades': [70, 80, 75]}
]
print(sort_by_average(students) == expected)

students = [
    {'name': 'David', 'grades': [100, 95]},
    {'name': 'Eve', 'grades': [100, 95]}
]
expected = [
    {'name': 'David', 'grades': [100, 95]},
    {'name': 'Eve', 'grades': [100, 95]}
]
print(sort_by_average(students) == expected)
```

</details>

### 2. Longest Consecutive Sequence

**Difficulty**:​ Intermediate

Create a function that takes a list of integers and returns the length of the longest consecutive elements sequence. 

```python
def longest_consecutive(arr):
    """
    Find length of longest consecutive sequence.
    Args:
        numbers (list): A list of integers

    Returns:
        int: The length of the longest consecutive elements sequence
    """
    # Your implementation here
    pass

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]) == 4) # The sequence is [1, 2, 3, 4]
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 9, 1]) == 10)
print(longest_consecutive([]) == 0)
print(longest_consecutive([1, 1, 2, 2, 3, 3]) == 3)
```

<details>
<summary>Possible Solution</summary>

```python

def longest_consecutive(arr):

    if not arr:
       return 0
    else:
       
        temp = []
        sorted_list = sorted(arr)
        temp.append(sorted_list[0])
        for i in range(1, len(sorted_list)):
            if sorted_list[i] - 1 == sorted_list[i-1]:
                temp.append(sorted_list[i])
        return len(temp)

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]) == 4) # The sequence is [1, 2, 3, 4]
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 9, 1]) == 10)
print(longest_consecutive([]) == 0)
print(longest_consecutive([1, 1, 2, 2, 3, 3]) == 3)

```

</details>


### 3. Smaller Numbers Count

**Difficulty**:​ Intermediate

Create a function that takes a list of integers and returns a list where each element represents the number of elements in the original array that are smaller than the current element. Count unique values only.

```python
def smaller_numbers_than_current(arr):
    """
    Count how many unique numbers are smaller than each element.
    Args:
        numbers (list): A list of integers

    Returns:
        list: A list where each element is the count of unique numbers smaller than the current element
    """
    # Your implementation here
    pass

# Test cases
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
```

<details>
<summary>Possible Solution</summary>

```python
def smaller_numbers_than_current(arr):

    result = []
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j] and arr[j] != arr[j-1]:
                count += 1
        result.append(count)
        count = 0

    return result   


# Test cases
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
```
</details>

### Closest Numbers

**Difficulty**:​ Advanced

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
    difference = {}
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] != numbers[j]:
                closest = abs(numbers[i] - numbers[j])
                if closest not in difference:
                    difference[closest] = (numbers[i], numbers[j])

    min_key = min(difference)
  
    return difference[min_key]
    
# Test cases
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 7, 17]) == (12, 7))
```

</details>

## 5. Group Anagrams

**Difficulty**:​ Advanced

Implement a function that takes a list of strings and groups anagrams together. Anagrams are words that have the same characters but in a different order.

```python
def group_anagrams(words):
    """
    Group words that are anagrams of each other.
    Args:
       words (list): A list of strings

    Returns:
       list: A list of lists where each sublist contains anagrams grouped together
    """
    # Your implementation here
    pass

# Test cases
result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(sorted([sorted(group) for group in result1]) == sorted([sorted(group) for group in expected1]))

result2 = group_anagrams(["listen", "silent", "enlist"])
expected2 = [["listen", "silent", "enlist"]]
print(sorted([sorted(group) for group in result2]) == sorted([sorted(group) for group in expected2]))
```

<details>
<summary>Possible Solution</summary>

```python
def group_anagrams(words):
    groups = []

    for word in words:
        groups_found = False
        for group in groups:
            if set(word) == set(group[0]):
                group.append(word)
                groups_found = True
                break
        if not groups_found:
            groups.append([word])
    print(groups)
    return groups

# Test cases
result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
expected1 = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(sorted([sorted(group) for group in result1]) == sorted([sorted(group) for group in expected1]))

result2 = group_anagrams(["listen", "silent", "enlist"])
expected2 = [["listen", "silent", "enlist"]]
print(sorted([sorted(group) for group in result2]) == sorted([sorted(group) for group in expected2]))
```

</details>

## 6. Unscramble Words

**Difficulty**:​ Beginner

Create a function that determines if the first string can be rearranged to form the second string.

```python
def unscramble(string1, string2):
    """
    Check if string1 can be rearranged to form string2.
    Args:
       str1 (str): The first string to be rearranged
       str2 (str): The target string to form

    Returns:
       bool: True if str1 can be rearranged to form str2, False otherwise
    """
    # Your implementation here
    pass

# Test cases
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == False)
print(unscramble('puelyontshr', 'pythonrules') == True)
print(unscramble('boldface', 'coalfbmd') == False)
```

<details>
<summary>Possible Solution</summary>

```python
def unscramble(string1, string2):
    return set(string1) == set(string2)

# Test cases
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == False)
print(unscramble('puelyontshr', 'pythonrules') == True)
print(unscramble('boldface', 'coalfbmd') == False)
```

</details>

## 7. Longest Common Prefix

**Difficulty**:​ Advanced

Create a function that takes a list of strings and returns the longest common prefix.

```python
def longest_common_prefix(strings):
    """
    Find the longest common prefix among all strings.
    Args:
       strings (list): A list of strings

    Returns:
       str: The longest common prefix of all strings
    """
    # Your implementation here
    pass

# Test cases
print(longest_common_prefix(["flower", "flow", "flight"]) == "fl")
print(longest_common_prefix(["dog", "racecar", "car"]) == "")
print(longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters")
print(longest_common_prefix(["throne", "dungeon"]) == "")
print(longest_common_prefix(["throne"]) == "throne")
```

<details>
<summary>Possible Solution</summary>

```python
def longest_common_prefix(strings):
    if not strings:
        prefix = ""
    else:
        prefix = strings[0]
        for string in strings[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    break
    return prefix

# Test cases
print(longest_common_prefix(["flower", "flow", "flight"]) == "fl")
print(longest_common_prefix(["dog", "racecar", "car"]) == "")
print(longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters")
print(longest_common_prefix(["throne", "dungeon"]) == "")
print(longest_common_prefix(["throne"]) == "throne")
```

</details>


## 8. Symmetric Difference

**Difficulty**:​ Advanced

Create a function that takes two lists as arguments and returns a new list containing elements that are in one list but not both. The returned list should have no duplicate values and be sorted in ascending order.

```python
def symmetric_difference(arr1, arr2):
    """
    Find elements that are in one array but not both.
    Args:
       list1 (list): The first list
       list2 (list): The second list

    Returns:
       list: A sorted list of elements that are in one list but not both, with no duplicates
    """
    # Your implementation here
    pass

# Test cases
print(symmetric_difference([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5])
print(symmetric_difference([1, 2, 2, 3], [3, 3, 4, 5]) == [1, 2, 4, 5])
print(symmetric_difference([], [1, 2, 3]) == [1, 2, 3])
print(symmetric_difference([1, 2, 3], [1, 2, 3]) == [])
```

<details>
<summary>Possible Solution</summary>

```python

def symmetric_difference(arr1, arr2):

    if not arr1 or not arr2:
        return arr2 or arr1

    elif arr1 == arr2:
       return []
    
    else:
      commonalites = set(arr1) & set(arr2)
      for item in commonalites:
        if item in arr1:
           list1 = [number for number in arr1 if number != item] 
        if item in arr2:
            list2 = [number for number in arr2 if number != item]
        return list(set(list1) | set(list2)) 
   
# Test cases
print(symmetric_difference([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5])
print(symmetric_difference([1, 2, 2, 3], [3, 3, 4, 5]) == [1, 2, 4, 5])
print(symmetric_difference([], [1, 2, 3]) == [1, 2, 3])
print(symmetric_difference([1, 2, 3], [1, 2, 3]) == [])
```

</details>

## 9. All Palindromic Substrings

**Difficulty**:​ Advanced

Create a function that finds all substrings in a string that are palindromes. Return a list of all unique palindromic substrings sorted by length (shortest to longest).

```python

def palindromic_substrings(string):
    """
    Find all palindromic substrings and return them sorted by length.
    Args:
       s (str): The input string to search for palindromes

    Returns:
       list: A list of all unique palindromic substrings sorted by length
    """
    # Your code here
    pass

# Test cases
print(palindromic_substrings('abcd') == ['a', 'b', 'c', 'd'])
print(palindromic_substrings('madam') == ['a', 'd', 'm', 'ada', 'madam'])
print(palindromic_substrings('hello') == ['e', 'h', 'l', 'o', 'll'])
print(palindromic_substrings('knitting') == ['g', 'i', 'k', 'n', 't', 'tt', 'itti', 'nittin'])
print(palindromic_substrings('racecar') == ['a', 'c', 'e', 'r', 'cec', 'aceca', 'racecar'])

```

<details>
<summary>Possible Solution</summary>

```python

def palindromic_substrings(string):
    temp = []
    result = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                temp.append(string[i:j+1])

    for element in temp:
        if element and element not in result:
            result.append(element)

    final = sorted(result, key=lambda x: (len(x), x))
    return final

print(palindromic_substrings('abcd') == ['a', 'b', 'c', 'd'])
print(palindromic_substrings('madam') == ['a', 'd', 'm', 'ada', 'madam'])
print(palindromic_substrings('hello') == ['e', 'h', 'l', 'o', 'll'])
print(palindromic_substrings('knitting') == ['g', 'i', 'k', 'n', 't', 'tt', 'itti', 'nittin'])
print(palindromic_substrings('racecar') == ['a', 'c', 'e', 'r', 'cec', 'aceca', 'racecar'])

```

</details>

## 10. Most Common Word

**Difficulty**:​ Intermediate

Create a function that takes a list of strings and returns the most common word. If there's a tie, return the word that appears first in the list.

```python

def most_common_word(words):
    """
    Find the most frequently occurring word in the list.
    If multiple words have the same highest frequency, return the one that appears first.
    Treat words case-insensitively (e.g., "Hello" and "hello" are the same word).

    Args:
       words (list): A list of strings

    Returns:
       str: The most common word, or the first one in case of a tie

    Example:
    most_common_word(['apple', 'orange', 'apple', 'banana']) -> 'apple'
    """
    # Your implementation here
    pass

# Test cases
print(most_common_word(['apple', 'orange', 'apple', 'banana']) == 'apple')
print(most_common_word(['a', 'b', 'c', 'a', 'b', 'a']) == 'a')
print(most_common_word(['Hello', 'hello', 'HELLO']) == 'Hello')
print(most_common_word(['one', 'two', 'three']) == 'one')

```

<details>
<summary>Possible Solution</summary>

```python
def most_common_word(words):
  
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    return max(counts, key=counts.get)

# Test cases
print(most_common_word(['apple', 'orange', 'apple', 'banana']) == 'apple')
print(most_common_word(['a', 'b', 'c', 'a', 'b', 'a']) == 'a')
print(most_common_word(['Hello', 'hello', 'HELLO']) == 'Hello')
print(most_common_word(['one', 'two', 'three']) == 'one')
```

</details>

## 11. Count Identical Pairs

**Difficulty**:​ Intermediate

Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in `[1, 2, 3, 2, 1]` is 2: occurrences each of both 2 and 1. If the list is empty or contains exactly one value, return 0. If a certain number occurs more than twice, count each complete pair once.

```python

def pairs(lst):
    """
    Count identical pairs in the list.
    Args:
        numbers (list): A list of integers

    Returns:
        int: The number of identical pairs
    """
    # Your implementation here
    pass

# Test cases
print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 3)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

```

<details>
<summary>Possible Solution</summary>

```python
def pairs(lst):
    
    if not lst or len(lst) == 1:
        return 0
    
    else:
        counts = {}
        for num in lst:
            counts[num] = counts.get(num, 0) + 1
        return sum([value // 2 for value in counts.values()])
    
# Test cases
print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
```

</details>



## 12. Odd Fellow

**Difficulty**:​ Intermediate

Create a function that finds the integer that appears an odd number of times in a list. The input array will always contain exactly one such integer.

```python

def odd_fellow(arr):
    """
    Find the number that appears an odd number of times.
    Args:
        numbers (list): A list of integers

    Returns:
        int: The integer that appears an odd number of times
    """
    # Your implementation here
    pass

# Test cases
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)

```

<details>
<summary>Possible Solution</summary>

```python
def odd_fellow(arr):

    counts = {}
    for number in arr:
        counts[number] = counts.get(number, 0) + 1
   
    for key, value in counts.items():
        if value % 2 == 1:
            return key

# Test cases
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
```

</details>

## 13. Find Doubles

**Difficulty**:​ Advanced

Create a function that takes a list of integers as an argument and returns a list of all the integers that appear exactly twice in the original list. The integers in the returned list should appear in the same order as they first appear in the original list.

```python

def find_doubles(array):
    """
    Find all numbers that appear exactly twice.
    Args:
       numbers (list): A list of integers

    Returns:
       list: A list of integers that appear exactly twice, in order of first appearance
    """
    # Your implementation here
    pass

# Test cases
print(find_doubles([1, 2, 3, 1, 2, 3, 4, 5]) == [1, 2, 3])
print(find_doubles([1, 2, 3, 4, 5]) == [])
print(find_doubles([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5])
print(find_doubles([1, 1, 1, 2, 2, 3]) == [2])
print(find_doubles([5, 10, 15, 10, 5, 15, 10, 5]) == [15])

```

<details>
<summary>Possible Solution</summary>

```python
def find_doubles(array):
    
    counts = {}
    result = []

    for number in array:
        counts[number] = counts.get(number, 0) + 1
   
    for key, value in counts.items():
        if value == 2:
            result.append(key)
    return result

# Test cases
print(find_doubles([1, 2, 3, 1, 2, 3, 4, 5]) == [1, 2, 3])
print(find_doubles([1, 2, 3, 4, 5]) == [])
print(find_doubles([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5])
print(find_doubles([1, 1, 1, 2, 2, 3]) == [2])
print(find_doubles([5, 10, 15, 10, 5, 15, 10, 5]) == [15])
```

</details>

## 14. Find Sum Pairs

**Difficulty**:​ Intermediate

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

    result = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            to_compare = (numbers[i], numbers[j])
            if sum(to_compare) == target_sum and to_compare not in result:
                result.append(to_compare)

    return result

# Test cases
print(find_pairs([1, 2, 3, 4, 5], 6) == [(1, 5), (2, 4)])
print(find_pairs([5, 5, 5, 5], 10) == [(5, 5)])
print(find_pairs([1, 2, 3, 4, 5], 10) == [])
print(find_pairs([-1, 0, 1, 2], 1) == [(-1, 2), (0, 1)])
```

</details>

## 15. Group By Frequency

**Difficulty**:​ Intermediate

Create a function that takes an array of numbers and returns an array of arrays, where each inner array contains all numbers that appear the same number of times in the original array.

```python

def group_by_frequency(array):
    """
    Group numbers by their frequency of occurrence.
    Args:
        numbers (list): A list of numbers

    Returns:
        list: A list of lists, where each inner list contains numbers with the same frequency
    """
    # Your code here
    pass

# Test cases
print(group_by_frequency([1, 2, 2, 3, 3, 3]) == [[1], [2, 2], [3, 3, 3]])
print(group_by_frequency([5, 5, 5, 8, 8, 9, 2, 1]) == [[5, 5, 5], [8, 8], [9, 2, 1]])
print(group_by_frequency([1, 1, 2, 2, 3, 3]) == [[1, 1, 2, 2, 3, 3]])
print(group_by_frequency([]) == [])

```

<details>
<summary>Possible Solution</summary>

```python

def group_by_frequency(array):

    if not array:
        return []

    # Pass 1: Count frequency of each number
    frequencies = {}
    for num in array:
        frequencies[num] = frequencies.get(num, 0) + 1

    # Pass 2: Group numbers based on their frequency
    groups = {}
    for num, freq in frequencies.items():
        if freq not in groups:
            groups[freq] = []
        
        groups[freq].extend([num] * freq)

    return list(groups.values())

# Test cases
print(group_by_frequency([1, 2, 2, 3, 3, 3]) == [[1], [2, 2], [3, 3, 3]])
print(group_by_frequency([5, 5, 5, 8, 8, 9, 2, 1]) == [[5, 5, 5], [8, 8], [9, 2, 1]])
print(group_by_frequency([1, 1, 2, 2, 3, 3]) == [[1, 1, 2, 2, 3, 3]])
print(group_by_frequency([]) == [])
```

</details>

## 16. Bouncy Count

**Difficulty:** Intermediate

Some numbers have only ascending digits, like 123, 3445, 2489, etc. Some numbers have only descending digits, like 321, 5443, 9842, etc.

A number is "bouncy" if it has both ascending and descending digits, like 313, 92543, etc.
Write a method that takes a list of numbers and counts how many of them are bouncy.

Problem: determine if an integer is neither descending nor ascending, 
but increase in number value or decrease in number value as we iterate over it

```python
print(bouncy_count([]) == 0)
print(bouncy_count([11, 0, 345, 21]) == 0)
print(bouncy_count([121, 4114]) == 2)
print(bouncy_count([176, 442, 80701644]) == 2)
```

<details>
<summary>Possible Solution</summary>

```python
#version with sorted()

def is_bouncy(n):
    s = list(str(n))
    return s != sorted(s) and s != sorted(s, reverse=True)

def bouncy_count(numbers):
    return sum(1 for num in numbers if is_bouncy(num))

#version without sorted

def is_bouncy(n):
    s = str(n)
    if len(s) <= 2:
        return False

    has_increased = False
    has_decreased = False

    for i in range(len(s) - 1):
        if s[i] < s[i+1]:
            has_increased = True
        elif s[i] > s[i+1]:
            has_decreased = True

        # If we've found both an increase and a decrease,
        # we know it's bouncy and can stop early.
        if has_increased and has_decreased:
            return True

    return False

def bouncy_count(numbers):
    count = 0
    for num in numbers:
        if is_bouncy(num):
            count += 1
    return count
```

</details>


