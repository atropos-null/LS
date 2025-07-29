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

## 10. Most Frequent Words

Write a function that, given a string of text, returns a list of the top-3 most
occurring words, in descending order of the number of occurrences.

Assumptions:
- A word is a string of letters (A to Z) optionally containing one or more apostrophes (').
- Matches should be case-insensitive.
- Ties may be broken arbitrarily.
- If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty list if a text contains no words.

Examples:

```python

top_3_words(" , e .. ") # ["e"]
top_3_words(" ... ") # []
top_3_words(" ' ") # []
top_3_words(" ''' ") # []
top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""") # should return ["a", "of", "on"]
```
<details>
<summary>Possible Solution</summary>

def make_dictionary(input_string):
    to_count = []
    counts = {}
    split_elements = input_string.split()
    
    for element in split_elements:
        if element.isalpha():
            to_count.append(element)

    for element in to_count:
        if element not in counts:
            counts[element] = 1
        else:
            counts[element] += 1
    return counts

def top_3_words(counts):
    final = []
    count_dicts = make_dictionary(counts) 
    if not count_dicts:
        return []
    for _ in range(3):
        if len(count_dicts) == 1:
            for key in count_dicts.keys():
                final.append(key)
            break
        else:
            max_counts = max(count_dicts, key=count_dicts.get)
            final.append(max_counts)
            count_dicts.pop(max_counts)
    return final

print(top_3_words(" , e .. ")) # ["e"]
print(top_3_words("hi how are you hi how hi"))
print(top_3_words(" ... ")) # []
print(top_3_words(" ' ")) # []
print(top_3_words(" ''' ")) # []
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, 
a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.""")) # should return ["a", "of", "on"]
</details>

## 11. Extract the domain name from a URL

Write a function that, given a URL as a string, parses out just the domain name and returns it.

Examples:

```python

domain_name("http://github.com/carbonfive/raygun") # should return "github"
domain_name("https://www.cnet.com") # should return "cnet"
```

<details>
<summary>Possible Solution</summary>

```python
def domain_name(input_string):
    half_way = strip_prefix(input_string)
    final = strip_suffix(half_way)
    return final

def strip_prefix(input_string):
    prefixes = ["http://", "https://www."]
    for prefix in prefixes:
        if input_string.startswith(prefix):
            half_cleaned = input_string.removeprefix(prefix)
    return half_cleaned

def strip_suffix(half_clean_string):
    listed = half_clean_string.split(".")
    return listed[0]

print(domain_name("http://github.com/carbonfive/raygun")) # should return "github"
print(domain_name("https://www.cnet.com")) # should return "cnet"
```
</details>

## 12. Detect the Pangram
A pangram is a sentence that contains every single letter of the alphabet at least once. Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Examples:
```python
print(is_panagram("The quick brown fox jumps over the lazy dog.")) # should return True
print(is_panagram("This is not a pangram.")) # should return False
```

<details>
<summary>Possible Solution</summary>

```python

def is_panagram(input_string):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    chars = [char for char in input_string.lower()]
    collection = []
    for char in chars:
        if char in abc:
            collection.append(char)
    if set(abc) == set(collection):
        return True
    else:
        return False

print(is_panagram("The quick brown fox jumps over the lazy dog.")) # True
print(is_panagram("This is not a pangram.")) #False

```
</details>

## 13. Kebabize a String

Modify the kebabize function so that it converts a camel case string into a kebab case. Kebab case separates words with dashes '-'; camel case identifies separate words by upcasing the first character in each new word.

Examples:

```python

kebabize('camelsHaveThreeHumps') # should return 'camels-have-three-humps'
kebabize('myCamelHas3Humps') # should return 'my-camel-has-humps'
```

<details>
<summary>Possible Solution</summary>

```python
def kebabize(input_string):
    holding = []
    split_string = [char for char in input_string]
    for char in split_string:
        if char.isupper():
            holding.append("-")
        holding.append(char.lower())
    return "".join(holding)

print(kebabize('camelsHaveThreeHumps')) # 'camels-have-three-humps'
print(kebabize('myCamelHas3Humps')) #'my-camel-has-humps'
```
</details>

## 14. Dubstep

Write a function to decode a dubstep string to its original form. The string may begin and end with one or more "WUB"s and there will be at least one (and possibly more) "WUB"s between each word. The input consists of a single non-empty string, consisting only of uppercase English letters.

Examples:
```python

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")) # should return "WE ARE THE CHAMPIONS MY FRIEND"
```

<details>
<summary>Possible Solution</summary>

```python

def song_decoder(input_string):
    return ' '.join(input_string.replace('WUB', ' ').split())

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")) #"WE ARE THE CHAMPIONS MY FRIEND"
```

## 15. Take a Walk

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- every time you press the button it sends you a list of one-letter strings representing directions to walk (e.g., ['n', 's', 'w', 'e']). You always walk only a single block in a direction, and you know it takes you one minute to traverse one city block. Create a function that will return `True` if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return `False` otherwise.

Note: You will always receive a valid list containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty list (that's not a walk, that's standing still!).

Examples:

```python

is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) # should return True
is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) # should return False
is_valid_walk(['w']) # should return False
is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) # should return F
```

<details>
<summary>Possible Solution</summary>

```python

def is_valid_walk(directions):

    if len(directions) % 10 == 0:
        if 'n' and 's' in directions:
            if directions.count('n') == directions.count('s'):
                return True
            return False
        elif 'e' and 'w' in directions:
            if directions.count('e') == directions.count('w'):
                return True
            return False
    
    return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # True
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # False
print(is_valid_walk(['w'])) # False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # False
```

</details>

## 16. Spin Words
Write a function that takes in a string of one or more words and returns the same string, but with all words of five or more letters reversed. Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

```python

spin_words("Hey fellow warriors") # should return "Hey wollef sroirraw"
spin_words("This is a test") # should return "This is a test"
spin_words("This is another test") # should return "This is rehtona test"
```

<details>
<summary>Possible Solution</summary>

```python

def spin_words(input_string):
    temp = input_string.split()
    for index, word in enumerate(temp):
        if len(word) >= 5:
            new_word = word[::-1]
            temp.insert(index, new_word)
            temp.pop(index+1)
    return " ".join(temp)


print(spin_words("Hey fellow warriors")) # "Hey wollef sroirraw"
print(spin_words("This is a test")) # "This is a test"
print(spin_words("This is another test")) # "This is rehtona test"
```

</details>

## 17. Expanded Form of Number

You will be given a number, and you need to return it as a string in expanded form. For example:

```python

expanded_form(12) # should return '10 + 2'
expanded_form(42) # should return '40 + 2'
expanded_form(70304) # should return '70000 + 300 + 4'
```

Note: All numbers will be whole numbers greater than 0.

<details>
<summary>Possible Solution</summary>

```python

def expanded_form(num):
    digits = [int(num) for num in str(num)]
    temp = []
    for i in range(len(digits)):
        digit = digits[i] * (10**(len(digits) - i - 1))
        if digit == 0:
            continue
        temp.append(str(digit))
    return " + ".join(temp)
  
        
print(expanded_form(12)) # '10 + 2'
print(expanded_form(42)) # '40 + 2'
print(expanded_form(70304)) # '70000 + 300 + 4'
```
</details>