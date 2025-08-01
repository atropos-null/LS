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

Write a function that takes two strings as input, `full_text` and `search_text`, and returns the number of times `search_text` appears in `full_text`. Needed help with this one. 

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

Write a function that takes a string of integers as input and returns the number of substrings that result in an odd number when converted to an integer. Needed help with this one.

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

Write a function that takes a non-empty string `s` as input and finds the minimum substring `t` and the maximum number `k`, such that the entire string `s` is equal to `t` repeated `k` times. Had no idea with this one.

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

Revisit this one!

Examples:
```python
scramble_words('professionals') #'paefilnoorsss'
scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") #"you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."
```

<details>
<summary>Possible Solution</summary>

```python
def get_special_char(word):
    special_char = "" 
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

```python
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
            max_counts = max(count_dicts, key=count_dicts.get) #This line was hard but everything else was ok.
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
```

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
    if set(abc) == set(collection): #Needed a reminder about using uniques
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

Write a function to decode a dubstep string to its original form. The string may begin and end with one or more "WUB"s and there will be at least one (and possibly more) "WUB"s between each word. The input consists of a single non-empty string, consisting only of uppercase English letters. Needed help with this one.

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
        digit = digits[i] * (10**(len(digits) - i - 1)) #Needed help with this line
        if digit == 0:
            continue
        temp.append(str(digit))
    return " + ".join(temp)
  
        
print(expanded_form(12)) # '10 + 2'
print(expanded_form(42)) # '40 + 2'
print(expanded_form(70304)) # '70000 + 300 + 4'
```
</details>

## 18. Multiplicative Persistence
Write a function, persistence, that takes in a positive parameter `num` and returns its multiplicative persistence, which is the number of times you must multiply the digits in `num` until you reach a single digit.

Examples:

```python
persistence(39) # should return 3, because 3*9=27, 2*7=14, 1*4=4 and 4 has only one digit
persistence(999) # should return 4, because 9*9*9=729, 7*2*9=126, 1*2*6=12, and finally 1*2=2
persistence(4) # should return 0, because 4 is already a one-digit number
persistence(25) # should return 2, because 2*5=10, and 1*0=0
```

<details>
<summary>Possible Solution</summary>

```python
def persistence(num):

    digits = [int(num) for num in str(num)]
    count = 0
    while len(digits) > 1:
        product = 1
        for i in range(len(digits)):
            product = product * digits[i] #Needed help with this line
        digits.clear()
        digits.append(product)
        digits = [int(num) for num in str(product)]
        count +=1
    return count

print(persistence(39)) # should return 3, because 3*9=27, 2*7=14, 1*4=4 and 4 has only one digit
print(persistence(999)) # should return 4, because 9*9*9=729, 7*2*9=126, 1*2*6=12, and finally 1*2=2
print(persistence(4)) # should return 0, because 4 is already a one-digit number
print(persistence(25)) # should return 2, because 2*5=10, and 1*0=0
```

</details>

## 19. Title-ize

A string is considered to be in title case if each word in the string is either:
a) Capitalized (that is, only the first letter of the word is in upper case)
b) Considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalized.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

Examples:

```python

title_case('a clash of KINGS', 'a an the of') # should return 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return 'The Wind in the Willows'
title_case('the quick brown fox') # should return 'The Quick Brown Fox'
```

<details>
<summary>Possible Solution</summary>

```python

def title_case(input_string, exceptions=''): #Needed a reminder about defaults
    exceptions = exceptions.lower().split()
    final = []
    temp = input_string.lower().split()
    for word in temp:
        if word in exceptions:
            final.append(word)
        else:
            final.append(word.capitalize())
    popped = final.pop(0)
    final.insert(0, popped.capitalize())
    return " ".join(final)
 
print(title_case('a clash of KINGS', 'a an the of')) # should return 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # should return 'The Wind in the Willows'
print(title_case('the quick brown fox')) # should return 'The Quick Brown Fox'

```
</details>

## 20. Character Count Sorting
Write a function that takes a string as an argument and groups the number of times each character appears in the string as a dictionary sorted by the highest number of occurrences.

The characters should be sorted alphabetically, and you should ignore spaces, special characters, and count uppercase letters as lowercase ones. Note: Struggled with appending a list to a dictionary value.

Examples:

```python

get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}
```

<details>
<summary>Possible Solution</summary>

```python

def get_char_count(input_string):
    chars = [char for char in input_string.lower() if char.isalnum()]
    counts = {}
    final = {}
    sorted_final = {}
    for char in chars:
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count in final:
            final[count].append(char) #How to append a list as a dictionary value.
        else:
            final[count] = [char]
    for count in final:
        final[count].sort(reverse=True)
    for count in sorted(final.keys(), reverse=True):
        sorted_final[count] = final[count]
    
    return sorted_final
```

</details>

## 21. Mine Location

You've just discovered a square (NxN) field and you notice a warning sign. The sign states that there's a single bomb in the 2D grid-like field in front of you.

Write a function `mine_location` that accepts a 2D array, and returns the location of the mine. The mine is represented as the integer 1 in the 2D array. Areas in the 2D array that are not the mine will be represented as 0s.

The location returned should be an array where the first element is the row index, and the second element is the column index of the bomb location (both should be 0 based). All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array. Note: Struggled with this one.

Examples:
```python

mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) # should return [1, 1]
mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) # should return [2, 1]
mine_location([[1, 0], [0, 0]]) # should return [0, 0]
mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) # should return [2, 2]

```
<details>
<summary>Possible Solution</summary>

```python

def mine_location(matrix):
    result = []
    for row_index, lst in enumerate(matrix):
        if 1 in lst:
            result.append(row_index)
        for col_index, item in enumerate(lst):
            if 1 == item:
                result.append(col_index)
    return result 
               
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]])) # should return [0, 0]
print(mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # should return [1, 1]
print(mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]])) # should return [2, 1]
print(mine_location([[1, 0], [0, 0]])) # should return [0, 0]
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]])) # should return [0, 0]
print(mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])) # should return [2, 2]
```

## 22. Substring is Anagram?

Write a function `scramble(str1, str2)` that returns `True` if a portion of `str1` characters can be rearranged to match `str2`, otherwise returns `False`.

Notes:
- Only lower case letters will be used (a-z). No punctuation or digits will
	be included.
- Performance needs to be considered.
- Input strings `str1` and `str2` are null terminated.

Examples:
```python
scramble('rkqodlw', 'world') # should return True
scramble('cedewaraarossoqqyt', 'carrot') # should return True
scramble('katas', 'steak') # should return False
scramble('scriptjava', 'javascript') # should return True
scramble('scriptingjava', 'javascript') # should return True
```

<details>
<summary>Possible Solution</summary>

```python
def scramble(str1, str2):
    string_1 = [char for char in str1]
    string_2 = [char for char in str2]
    length_2 = len(str2)
    count = 0

    for char in string_2:
        if char in string_1:
            count += 1

    if count == length_2:
        return True
    else:
        return False

print(scramble('rkqodlw', 'world')) # should return True
print(scramble('cedewaraarossoqqyt', 'carrot')) # should return True
print(scramble('katas', 'steak')) # should return False
print(scramble('scriptjava', 'javascript')) # should return True
print(scramble('scriptingjava', 'javascript')) # should return True
```

</details>

## 23. Longest alphabetical substring

Write a function `longest(s)` that finds and returns the longest substring of `s` where the characters are in alphabetical order. Note: Struggled with this one. Completely whiffed this one.

Example:
```python
longest('asd')                  # should return 'as'
longest('nab')                  # should return 'ab'
longest('abcdeapbcdef')         # should return 'abcde'
longest('asdfaaaabbbbcttavvfffffdf') # should return 'aaaabbbbctt'
longest('asdfbyfgiklag')        # should return 'fgikl'
longest('z')                    # should return 'z'
longest('zyba')                 # should return 'z'
```
<details>
<summary>Possible Solution</summary>

```python

def longest(input_string):
    if not input_string:
        return ""
    s = [char for char in input_string]
    max_sub = [s[0]]
    curr_sub = [s[0]]
    for i in range(1, len(s)):
        if ord(s[i]) >= ord(s[i-1]):
            curr_sub.append(s[i])
        else:
            if len(curr_sub) > len(max_sub):
                max_sub = curr_sub[:]
            curr_sub = [s[i]]
    if len(curr_sub) > len(max_sub):
        max_sub = curr_sub[:]
    return ''.join(max_sub)


print(longest('asd'))                # should return 'as'
print(longest('nab'))                 # should return 'ab'
print(longest('abcdeapbcdef'))        # should return 'abcde'
print(longest('asdfaaaabbbbcttavvfffffdf')) # should return 'aaaabbbbctt'
print(longest('asdfbyfgiklag'))       # should return 'fgikl'
print(longest('z'))                   # should return 'z'
print(longest('zyba'))                 # should return 'z'
```
</details>


## 24. Generate Hashtags
Write a function `generate_hashtag(s)` that generates a hashtag from the given string `s`.

Rules:
- The hashtag must start with a '#' symbol.
- All words in the hashtag must start with a capital letter.
- If the resulting hashtag is longer than 140 characters, the function should return `False`.
- If the input string or the resulting hashtag is an empty string, the function should return `False`.

Examples:

```python

generate_hashtag("")                       # should return `False`
generate_hashtag(" " * 200)                # should return `False`
generate_hashtag("Do We have A Hashtag")   # should return "#DoWeHaveAHashtag"
generate_hashtag("Nice To Meet You")       # should return "#NiceToMeetYou"
generate_hashtag("this is a test")         # should return "#ThisIsATest"
generate_hashtag("this is a very long string" + " " * 140 + "end")  # should return "#ThisIsAVeryLongStringEnd"
generate_hashtag("a" * 139)                # should return "#A" + "a" * 138
generate_hashtag("a" * 141)                # should return `False`

```

<details>
<summary>Possible Solution</summary>

```python
def generate_hashtag(input_string):
    if not input_string or input_string.isspace():
        return False
    else:
        temp = []
        new_string = input_string.split()
        lengths = [char for char in input_string]
        for char in lengths:
            if char.isspace():
                lengths.remove(char)
        if len(lengths) < 140:
            for word in new_string:
                temp.append(word.capitalize())
            result = "".join(temp)
            return f"#{result}"
        else:
            return False
        
print(generate_hashtag(""))                     # should return `False`
print(generate_hashtag(" " * 200))                # should return `False`
print(generate_hashtag("Do We have A Hashtag"))   # should return "#DoWeHaveAHashtag"
print(generate_hashtag("Nice To Meet You"))      # should return "#NiceToMeetYou"
print(generate_hashtag("this is a test"))         # should return "#ThisIsATest"
print(generate_hashtag("this is a very long string" + " " * 140 + "end"))  # should return "#ThisIsAVeryLongStringEnd"
print(generate_hashtag("a" * 139))                # should return "#A" + "a" * 138
print(generate_hashtag("a" * 140))                # should return `False`
```
</details>

## 25. How many cakes can the baker make?

Pete is baking cakes and needs help calculating how many he can make with his recipes and available ingredients. Write a function `cakes()` that takes two dictionaries: the recipe and the available ingredients. Return the maximum number of cakes Pete can bake. Notes: Some struggle with this one. See below.

Rules:
- Ingredients not present in the objects can be considered as 0.

```python
# must return 2
cakes({"flour"=>500, "sugar"=>200, "eggs"=>1},{"flour"=>1200, "sugar"=>1200, "eggs"=>5, "milk"=>200}) == 2

# must return 11
cakes({"cream"=>200, "flour"=>300, "sugar"=>150, "milk"=>100, "oil"=>100},{"sugar"=>1700, "flour"=>20000,
"milk"=>20000, "oil"=>30000, "cream"=>5000}) == 11

# must return 0
cakes({"apples"=>3, "flour"=>300, "sugar"=>150, "milk"=>100, "oil"=>100},{"sugar"=>500, "flour"=>2000,
"milk"=>2000}) == 0

# must return 0
cakes({"apples"=>3, "flour"=>300, "sugar"=>150, "milk"=>100, "oil"=>100},{"sugar"=>500, "flour"=>2000,
"milk"=>2000, "apples"=>15, "oil"=>20}) == 0

# must return 0
cakes({"eggs"=>4, "flour"=>400},{}) == 0

# must return 1
cakes({"cream"=>1, "flour"=>3, "sugar"=>1, "milk"=>1, "oil"=>1, "eggs"=>1},{"sugar"=>1, "eggs"=>1, "flour"=>3,
"cream"=>1, "oil"=>1, "milk"=>1}) == 1
```

<details>
<summary>Possible Solution</summary>

First you have to change all the `=>` to `:` because that was dumb.

```python

def cakes(dict1, dict2):
    needs = dict(sorted(dict1.items()))
    haves = dict(sorted(dict2.items()))
    length_needs = len(needs)
    length_haves = len(haves)
    maximums = []
    for ingredient, amount in needs.items():
        if length_needs > length_haves:
            return 0
        if ingredient in haves:
            amount2 = haves[ingredient] #was missing this line. See below.
            if amount:
                result = amount2 // amount
                maximums.append(result)
    if not maximums:
        return 0

    return min(maximums)
                

#All return True
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2)

print(cakes({"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 1700, "flour": 20000,
  "milk": 20000, "oil": 30000, "cream": 5000}) == 11)

print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000,
  "milk": 2000}) == 0)

print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000,
   "milk": 2000, "apples": 15, "oil": 20}) == 0)

print(cakes({"eggs": 4, "flour": 400}, {}) == 0)

print(cakes({"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1}, {"sugar": 1, "eggs": 1, "flour": 3,
  "cream": 1, "oil": 1, "milk": 1}) == 1)
```

That line looks up the value in haves that corresponds to the current key (which you are iterating over, usually from needs). It assigns that value to the variable amount2, so you can use it in calculations or comparisons.

</details>

## 26. Mean Square

Create a function that takes two integer arrays of equal length, compares the value of each member in one array to the corresponding member in the other, squares the absolute value difference between those two values, and returns the average of those squared absolute value differences between each member pair.

Examples:

[1, 2, 3], [4, 5, 6] --> 9 because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2] --> 16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1] --> 1 because (1 + 1) / 2

```python
solution([1, 2, 3], [4, 5, 6]) == 9
solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5
solution([-1, 0], [0, -1]) == 1
```

<details>
<summary>Possible Solution</summary>

```python

def solution(lst1, lst2):
  tmp = [abs(lst1[i] - lst2[i]) ** 2 for i in range(len(lst1))]
  return sum(tmp) / len(tmp)

#All print True
print(solution([1, 2, 3], [4, 5, 6]) == 9)
print(solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5)
print(solution([-1, 0], [0, -1]) == 1)
```

</details>

## 27. Write a function that finds all the anagrams of a word from a list. Two words are anagrams of each other if they both contain the same letters.

Examples

```python
'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
```

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])
print(anagrams('laser', ['lazing', 'lazy', 'lacer']) == [])


<details>
<summary>Possible Solution</summary>

```python

def anagrams(input_string, lst):
    
    result = []

    s_chars = [char for char in input_string]
    input_dict = {}
    for char in s_chars:
        count = s_chars.count(char)
        input_dict[char] = count
    sorted_input = dict(sorted(input_dict.items()))
   
    for element in lst:
      lst_dict = {}
      for char in element:
        element_count = element.count(char)
        lst_dict[char] = element_count
      sorted_lst = dict(sorted(lst_dict.items()))    

      if sorted_input == sorted_lst:
        result.append(element)
        
    return result
            
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])
print(anagrams('laser', ['lazing', 'lazy', 'lacer']) == [])

```
</details>

## 28. Group by 2 chars

Write a function that splits the string into pairs of two characters. If the string contains an odd number of characters, replace the missing second character of the final pair with an underscore `('_')`.

Examples:

```python

solution('abc') == ['ab', 'c_']
solution('abcdef') == ['ab', 'cd', 'ef']
solution("abcdef") == ["ab", "cd", "ef"]
solution("abcdefg") == ["ab", "cd", "ef", "g_"]
solution("") == []
```

<details>
<summary>Possible Solution</summary>

```python

def solution(input_string):
    result = []
    if not input_string:
        return []
    
    else:
        if len(input_string) % 2 == 0:
            for char in range(0,len(input_string)-1, 2):
                pair = input_string[char]+input_string[char+1]
                result.append(pair)
        else:
            chars = [char for char in input_string]
            chars.append("_")
            for char in range(0, len(chars)-1, 2) :
                pair = chars[char]+chars[char+1]
                result.append(pair)
    return result

print(solution('abc') == ['ab', 'c_'])
print(solution('abcdef') == ['ab', 'cd', 'ef'])
print(solution("abcdef") == ["ab", "cd", "ef"])
print(solution("abcdefg") == ["ab", "cd", "ef", "g_"])
print(solution("") == [])

```
</details>

## 29. Anagram Difference Count

Given two words, determine the number of letters you need to remove from them to make them anagrams.

Example:

```python
anagram_difference('', '') == 0
anagram_difference('a', '') == 1
anagram_difference('', 'a') == 1
anagram_difference('ab', 'a') == 1
anagram_difference('ab', 'ba') == 0
anagram_difference('ab', 'cd') == 4
anagram_difference('aab', 'a') == 2
anagram_difference('a', 'aab') == 2
```

<details>
<summary>Possible Solution</summary>

```python

# The first was my successfull but bloated solution. 

def anagram_difference(str1, str2):
    needed_chars = []
    count = 0

    if not str1:
        for char in str2:
            needed_chars.append(char)
        return len(needed_chars)
    elif not str2:
        for char in str1:
            needed_chars.append(char)
        return len(needed_chars)   
    
    elif len(str1) > len(str2) and str1[0] != str1[1]:
        for char in str1:
            if char not in str2:
                needed_chars.append(char)
    
    elif len(str2) > len(str1) and str2[0] != str2[1]:
        for char in str2:
            if char not in str1:
                needed_chars.append(char)         

    elif len(str1) > len(str2) and str1[0] == str1[1]:
        for char in str1:
            if char not in str2:
                needed_chars.append(char)
                needed_chars.append(str1[1])
    
    elif len(str2) > len(str1) and str2[0] == str2[1]:
        for char in str2:
            if char not in str1:
                needed_chars.append(char)
                needed_chars.append(str2[1])

    else:
        if set(str1) == set(str2):
            return 0
        else:
            for char in str1:
                if char not in str2:
                    needed_chars.append(char) 
            for char in str2:
                if char not in str1:
                    needed_chars.append(char) 

    return len(needed_chars)
    
print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0)
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2)
print(anagram_difference('a', 'aab') == 2)

#Co Pilot's solution that's significantly less terrible

def anagram_difference(str1, str2):
    # Convert to lists for mutability
    l1 = list(str1)
    l2 = list(str2)
    
    # Remove matching characters one by one
    i = 0
    while i < len(l1):
        char = l1[i]
        if char in l2:
            l2.remove(char)
            l1.pop(i)
            # Do not increment i, as the next char shifted into position i
        else:
            i += 1
    # The leftovers are the difference
    return len(l1) + len(l2)
```

</details>

## 30. Is anagram?

Write a function to determine if two words are anagrams of each other.

Examples:

```python
is_anagram('Creative', 'Reactive') == true
is_anagram("foefet", "toffee") == true
is_anagram("Buckethead", "DeathCubeK") == true
is_anagram("Twoo", "WooT") == true
is_anagram("dumble", "bumble") == false
```

<details>
<summary>Possible Solution</summary>

```python
def is_anagram(str1, str2):
    if set(str1.lower()) == set(str2.lower()):
        return True
    else:
        return False
    

print(is_anagram('Creative', 'Reactive') == True)
print(is_anagram("foefet", "toffee") == True)
print(is_anagram("Buckethead", "DeathCubeK") == True)
print(is_anagram("Twoo", "WooT") == True)
print(is_anagram("dumble", "bumble") == False)
```
</details>