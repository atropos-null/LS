# SPOT Wiki PY119

Same problems as the original [SPOT Problems](https://github.com/The-SPOT-Hub/SPOT-Wiki/blob/main/Lesson%20Materials%20%26%20Code/PY110/Python110_ProblemSets.md) but with it cleaned up.

## 1. Count the letters in a string

Write a function that takes a string as input and counts the occurrences of each
lowercase letter in the string. Return the counts in a dictionary where the
letters are keys and their counts are values.

```python
letter_count('launchschool') #Expected Result:  {'l': 2, 'a': 1, 'u': 1, 'n': 1, 'c': 2, 'h': 2, 's': 1, 'o': 2}
```

<details>
<summary>Possible Solution</summary>

```python
def letter_count(input_string):
    result = {}
    working = [character for character in input_string]
    for character in working:
        result[character] = result.get(character, 0) + 1
    return result
```

</details>

## 2. Count of Pairs

Write a function that takes a list of integers as input and counts the number of
pairs in the list. A pair is defined as two equal integers separated by some
other integer(s).

```python

pairs([1, 2, 5, 6, 5, 2]) # ==> 2
pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) #==> 4

```

<details>
<summary>Possible Solution</summary>

```python

def pairs(lst):
    temp = []
    for i in range(len(lst)-1):
        if lst[i] not in temp:
            temp.append(lst[i])
        elif lst[i] == lst[i-1]:
            temp.append(lst[i])
        else:
            continue
    return len(lst) - len(temp)
```
</details>

## 3. Count Substring Instances

Write a function that takes two strings as input, `full_text` and `search_text`, and returns the number of times `search_text` appears in `full_text`.

```python

print(solution('abcdeb','b')) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb')) # should return 1

```

<details>
<summary>Possible Solution</summary>

```python
def solution(full_text, search_text):
    return full_text.count(search_text)
```

</details>

## 4. Alphabet Symmetry

Write a function that takes a list of words as input and returns a list of integers. Each integer represents the count of letters in the word that occupy their positions in the alphabet.

Examples:

```python

print(solve(["abode","ABc","xyzD"])) #[4, 3, 1]
print(solve(["abide","ABc","xyz"])) # [4, 3, 0]

```

<details>
<summary>Possible Solution</summary>

```python

def solve(lst):

    alpha_positions = {
    "a": 1,
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
    "y": 26,
    "z": 26
}
    result = []
   
    for string in lst:
        count = 0
        for index, char in enumerate(string.casefold()):
            if index + 1 == alpha_positions.get(char):
                count += 1
        result.append(count)
    return result
```

</details>


## 5. Longest Chain of Vowels

Write a function that takes a lowercase string as input and returns the length of the longest substring that consists entirely of vowels (a, e, i, o, u).

Examples:

```python
solve("roadwarriors") # should return 2
solve("suoidea") # should return 3
```

<details>
<summary>Possible Solution</summary>

```python
def solve(input_string):
    temp = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(input_string) - 1):
        count = 0
        if input_string[i] in vowels and input_string[i+1] in vowels:
            count += 1
            temp.append(count)
        else:
            continue
    return sum(temp)

print(solve("roadwarriors"))# should return 2
print(solve("suoidea"))# should return 3
```

</details>

## 6. Odd Number Sub-strings

Write a function that takes a string of integers as input and returns the number of substrings that result in an odd number when converted to an integer.

Examples:

```python

solve("1341") # should return 7
solve("1357") # should return 10

```

<details>
<summary>Possible Solution</summary>

```python

def solve(string):

    temp = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if int(substring) % 2 == 1:
                temp.append(substring)
    return len(temp)

print(solve("1341")) #7
print(solve("1357")) #10

```

## 7. The Nth Char

Write a function that takes a list of words and constructs a new word by concatenating the `nth` letter from each word, where `n` is the position of the word in the list.

Example:

```python
nth_char(['yoda', 'best', 'has']) # should return 'yes'
```

<details>
<summary>Possible Solution</summary>

```python

def nth_char(lst):
    new_string = ''
    for index, element in enumerate(lst):
        new_string += element[index]
    return new_string


print(nth_char(['yoda', 'best', 'has'])) # 'yes'
```

</details>

## 8. Smallest Substring Repeat

Write a function that takes a non-empty string `s` as input and finds the minimum substring `t` and the maximum number `k`, such that the entire string `s` is equal to `t` repeated `k` times.

Examples:

```python
print(f("ababab")) # should return ["ab", 3]
```

<details>
<summary>Possible Solution</summary>

```python

def smallest_substring(s):
    n = len(s)
    for i in range(1, n + 1):
        t = s[:i]
        k = n // i
        if t * k == s:
            return [t, k]
    # If no substring found, s itself is the answer
    return [s, 1]

# Example usage:
print(smallest_substring("ababab"))  # Output: ['ab', 3]
print(smallest_substring("aaaaaa"))  # Output: ['a', 6]
print(smallest_substring("abcabcabc"))  # Output: ['abc', 3]
print(smallest_substring("abcdef")) 
```
</details>

## 9. Typoglycemia Generator

Write a function that generates text following a pattern where:
1) the first and last characters of each word remain in their original place
2) characters between the first and last characters are sorted alphabetically
3) punctuation should remain at the same place as it started

Examples:
```python
scramble_words('professionals') #'paefilnoorsss'
scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") #"you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."
```

<details>
<summary>Possible Solution</summary>

```python
def get_special_char(word):
    special_char = "" #
    for char in word:
        if not char.isalnum():
            special_char = char
    return special_char

def get_special_char_index(word, special_char):
    return word.index(special_char)

def clean_word(word):
    cleaned_word = ""
    for char in word:
        if char.isalnum():
            cleaned_word += char

    return cleaned_word


def process_word(word):
    if len(word) < 4:
        return word
    elif word.isalnum():
            beginning, middle, end = word[0], word[1:-1], word[-1]
            sorted_middle = sorted(list(middle))
            word = list(beginning) + sorted_middle + list(end)
            return "".join(word)
    elif not word.isalnum():
        special_char = get_special_char(word)
        special_char_idx = get_special_char_index(word, special_char)
        cleaned_word = clean_word(word)
        beginning = list(cleaned_word[0])
        middle = list(cleaned_word[1:-1])
        end = list(cleaned_word[-1])
        sorted_middle = sorted(middle)
        word = beginning + sorted_middle + end
        word.insert(special_char_idx, special_char)
        return "".join(word)
            
def scramble_words(s):
    if " " not in s:
        result = process_word(s)
        return result
    else:
        list_of_words = s.split(" ")
        result = []
        for one_word in list_of_words:
            processed_word = process_word(one_word)
            result.append(processed_word)
        
        return " ".join(result)
```
</details>