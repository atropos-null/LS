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
    for character in input_string:
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

# Another Version:

def pairs(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) +1
    
    total = 0
    for value in counts.values():
        if value >= 2:
            total += value // 2
    return total
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
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}
   
   result = []
   for word in lst:
      count = 0
      for index, char in enumerate(word.lower()):
            if index == alpha_positions.get(char):
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

#Another Version:

def solve(string):
   vowels = 'aeiou'
   substring = ''
   substrings = []
   
   for char in string:
      if char in vowels:
            substring += char
      else:
         if substring:
            substrings.append(substring)
         substring = ""
    
   substrings.append(substring) #appends the last substring since there's no ending consonant

   final = [len(item) for item in substrings]
   return max(final)
      

print(solve("roadwarriors") == 2) # should return 2
print(solve("suoidea")  == 3) # should return 3
```

</details>

## 6. Odd Number Sub-strings

Write a function that takes a string of integers as input and returns the number of substrings that result in an odd number when converted to an integer. 

Examples:

```python

solve("1341") # should return 6
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

print(solve("1341")) #7 This gives 7 because 1 is counted twice
print(solve("1357")) #10

#Another Version

def solve(str_number):
   result = []
   temp = []
   str_digits = [number for number in str_number]
   for i in range(len(str_digits)+1):    
      for j in range(i+1, len(str_digits)+1):
         temp.append("".join(str_number[i:j]))
   
   for number in temp:
      converted_number = int(number)
      if converted_number % 2 == 1 and converted_number not in result:
         result.append(converted_number)
 
   return len(result)

print(solve("1341") == 6) # should return 7
print(solve("1357") == 10) # should return 10

```
</details>

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

#Another Version:

def nth_char(lst):
    
   result = ""
   for i in range(len(lst)):
      result += lst[i][i]
   return result
   
print(nth_char(['yoda', 'best', 'has'])) # should return 'yes'

```

</details>

## 8. Smallest Substring Repeat

Write a function that takes a non-empty string `s` as input and finds the minimum substring `t` and the maximum number `k`, such that the entire string `s` is equal to `t` repeated `k` times. Had no idea with this one.

Examples:

```python
print(smallest_substring("ababab")) # should return ["ab", 3]
print(smallest_substring("aaaaaa"))  # Output: ['a', 6]
print(smallest_substring("abcabcabc"))  # Output: ['abc', 3]
print(smallest_substring("abcdef"))  #Output: ['abcdef', 1]
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

#Another Version

def smallest_substring(s):
    
    for i in range(len(s)):
      t = s[:i+1]
      k = len(s) // len(t)
      if s == t * k:
        return [t, k]

print(smallest_substring("ababab")== ["ab", 3]) #True
print(smallest_substring("aaaaaa") == ['a', 6])  #True
print(smallest_substring("abcabcabc") == ['abc', 3])  #True
print(smallest_substring("abcdef") == ['abcdef', 1]) #True

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
def scramble_words(sentence):
    tokens = sentence.split(' ')
    scrambled_tokens = [process_token(token) for token in tokens]
    return ' '.join(scrambled_tokens)

def process_token(token):
    # Find the indices of the first and last alphabetic characters
    first_letter_idx = -1
    for i, char in enumerate(token):
        if char.isalpha():
            first_letter_idx = i
            break

    # If no letters, return token as is
    if first_letter_idx == -1:
        return token

    last_letter_idx = -1
    for i in range(len(token) - 1, -1, -1):
        if token[i].isalpha():
            last_letter_idx = i
            break

    # Extract prefix, core word, and suffix
    prefix = token[:first_letter_idx]
    core_word = token[first_letter_idx : last_letter_idx + 1]
    suffix = token[last_letter_idx + 1 :]

    scrambled_core = scramble_core(core_word)
    return prefix + scrambled_core + suffix

def scramble_core(word):
    # A word needs at least 4 letters to have a middle part to scramble.
    if len(word) < 4:
        return word

    first_char = word[0]
    last_char = word[-1]
    middle_part = word[1:-1]

    # Extract and sort only the letters from the middle part
    middle_letters = sorted([
        char for char in middle_part if char.isalpha()
    ])

    # Reconstruct the middle, preserving non-alphabetic characters
    new_middle = ""
    letter_idx = 0
    for char in middle_part:
        if char.isalpha():
            new_middle += middle_letters[letter_idx]
            letter_idx += 1
        else:
            new_middle += char

    return first_char + new_middle + last_char
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

#Another Version

def top_3_words(string):
   counts = {}
   result = []
   words = string.split()
   for word in words:
      if word.isalpha():
         counts[word] = counts.get(word, 0) +1
   
   top3 = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:3]

   for item in top3:
      result.append(item[0])
   return result

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

#Another Version:

def domain_name(link):
    prefixes = ["http://",  "https://www."]
    suffixes = [".com"]
    for item in prefixes:
        if item in link:
            mid_process = link.replace(item, "")
   
    for item in suffixes:
      if item in mid_process:
         index = mid_process.find(item)

    return mid_process[:index]

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
def kebabize(string):
    final = []
    chars = [char for char in string]
    for char in chars:
        if char.isupper():
            final.append("-")
            final.append(char.lower())
        elif not char.isalpha():
            continue
        else:
            final.append(char)
    
    return "".join(final)

print(kebabize('camelsHaveThreeHumps') == 'camels-have-three-humps') # should return 'camels-have-three-humps'
print(kebabize('myCamelHas3Humps') == 'my-camel-has-humps') # should return 'my-camel-has-humps'
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

#Longer Version:

def song_decoder(string):   
    sliced = "WUB"
    new = string.replace(sliced, " ")
    split_new = new.split()
    return " ".join(split_new)

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")) #"WE ARE THE CHAMPIONS MY FRIEND"
```

</details>

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

#Another Version:

def is_valid_walk(directions):
    
    counts = {}
    for direction in directions:
        counts[direction] = counts.get(direction, 0) +1
    
    values = list(counts.values())
    if sum(values) == 10 and values[0] == values[1]:
        return True
    return False

#All return True
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])  == True) 
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False) 
print(is_valid_walk(['w']) == False) 
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False) 


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

#Another Version

def spin_words(string):

    result = []
    words = string.split()
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)


#All return True
print(spin_words("Hey fellow warriors") == "Hey wollef sroirraw") 
print(spin_words("This is a test") == "This is a test") 
print(spin_words("This is another test") == "This is rehtona test") 
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

#Another Version

def expanded_form(number):

    temp = []
    stringed_number = str(number)
    int_digits = [int(digit) for digit in stringed_number]
    for i in range(len(int_digits)-1, -1, -1):
        temp.append(int_digits[len(int_digits) - 1 - i] * 10**i)

    stringed_list = [str(integer) for integer in temp if integer]
    return " + ".join(stringed_list)
    
#All return True
print(expanded_form(12) == '10 + 2') 
print(expanded_form(42) == '40 + 2') 
print(expanded_form(70304) == '70000 + 300 + 4')
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

#Another Version
def persistence(number):
    
    working_number = number
    holder = 1
    count = 0
    while len(str(working_number)) != 1:
        digits = [int(digit) for digit in str(working_number)]
        for digit in digits:
            holder = holder * digit
        working_number = holder
        holder = 1
        count += 1
        
    return count


print(persistence(39) == 3)# should return 3, because 3*9=27, 2*7=14, 1*4=4 and 4 has only one digit
print(persistence(999) == 4) # should return 4, because 9*9*9=729, 7*2*9=126, 1*2*6=12, and finally 1*2=2
print(persistence(4) == 0) # should return 0, because 4 is already a one-digit number
print(persistence(25) == 2)# should return 2, because 2*5=10, and 1*0=0
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

#Another Version:

def title_case(string, exceptions=[]):

    if not exceptions:
        all_caps = [word.capitalize() for word in string.split()]
        return " ".join(all_caps)
    
    else:
        new_exceptions = [word.lower() for word in exceptions.split()]
        result = []
        split_string = string.split()
        result.append(split_string[0].capitalize())
        for i in range(1, len(split_string)):
            if split_string[i].casefold() in new_exceptions:
                result.append(split_string[i].lower())
            else:
                result.append(split_string[i].capitalize())
    
        return " ".join(result)
                          
print(title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings') # should return 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows') # should return 'The Wind in the Willows'
print(title_case('the quick brown fox') == 'The Quick Brown Fox') # should return 'The Quick Brown Fox'

```
</details>

## 20. Character Count Sorting
Write a function that takes a string as an argument and groups the number of times each character appears in the string as a dictionary sorted by the highest number of occurrences.

The characters should be sorted alphabetically, and you should ignore spaces, special characters, and count uppercase letters as lowercase ones. Note: Good to revisit for sorting practice.

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

#Another Version:

def get_char_count(string):
    counts = {}
    for char in [char for char in string.lower() if char.isalnum()]: 
        counts[char] = counts.get(char, 0) +1
    
    final = {}
    for key, value in counts.items():
        if value in final:
            final[value].append(key)
        else:
            final[value] = [key]

    sorted_final = {}
    sorting_keys = sorted(final.keys(), reverse= True)
    
    for value in sorting_keys:
        sorted_final[value] = sorted(final[value], reverse=False)
    
    print(sorted_final)
    return sorted_final

print(get_char_count("Mississippi") == {4: ['i', 's'], 2: ['p'], 1: ['m']}) # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
print(get_char_count("Hello. Hello? HELLO!!") == {6: ['l'], 3: ['e', 'h', 'o']}) # should return {6: ['l'], 3: ['e', 'h', 'o']}
print(get_char_count("aaa...bb...c!") == {3: ['a'], 2: ['b'], 1: ['c']}) # should return {3: ['a'], 2: ['b'], 1: ['c']}
print(get_char_count("aaabbbccc") == {3: ['a', 'b', 'c']}) # should return {3: ['a', 'b', 'c']}
print(get_char_count("abc123") == {1: ['1', '2', '3', 'a', 'b', 'c']}) # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

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

#Another Version:

def mine_location(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                return [i, j]
            
#All return True
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0]) 
print(mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [1, 1]) 
print(mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) == [2, 1]) 
print(mine_location([[1, 0], [0, 0]]) == [0, 0]) 
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0]) 
print(mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == [2, 2]) 

```
</details>

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

# Another Version:

def scramble(str1, str2):

    return set(str2).issubset(set(str1))

#All should return True
print(scramble('rkqodlw', 'world') == True) 
print(scramble('cedewaraarossoqqyt', 'carrot') == True) 
print(scramble('katas', 'steak') == False) 
print(scramble('scriptjava', 'javascript') == True)
print(scramble('scriptingjava', 'javascript') == True) 
```

</details>

## 23. Longest alphabetical substring

Write a function `longest(s)` that finds and returns the longest substring of `s` where the characters are in alphabetical order. Note: Completely whiffed this one.

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

#Another Version, still a slog

def longest(string):

    if not string:
        return ""

    max_substring = string[0]
    current_substring = string[0]
    for i in range(1,len(string)):
        if ord(string[i]) >= ord(string[i-1]):
            current_substring += string[i]
        else:
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
            current_substring = string[i]
    
    if len(current_substring) > len(max_substring):
        max_substring = current_substring
            
    return max_substring

print(longest('asd') == 'as')   
print(longest('nab')  == 'ab')                
print(longest('abcdeapbcdef') == 'abcde')     
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag') ==  'fgikl')
print(longest('z') ==  'z')
print(longest('zyba') == 'z')
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

#Another Version

def generate_hashtag(string):

    TAG = "#"
    split_text = string.split()

    if not string or not split_text:
        return False
    
    capped_text = [word.capitalize() for word in split_text]
    joined_text = "".join(capped_text)
    complete_text = TAG+joined_text
    
    if len(complete_text) <= 140:
        return complete_text
    return False 

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

```python
[1, 2, 3], [4, 5, 6] --> 9 because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2] --> 16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1] --> 1 because (1 + 1) / 2
```

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

#Another Version

def solution(lst1, lst2):
    
    temp = []
    for i in range(len(lst1)):
        working_number = abs(lst1[i] - lst2[i]) ** 2
        temp.append(working_number)
    return sum(temp) / len(temp)

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


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])
print(anagrams('laser', ['lazing', 'lazy', 'lacer']) == [])
```


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

#Another Version:

def anagrams(string, lst):
    
    result = []
    for element in lst:
        if set(string) == set(element):
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

#Another Version

def solution(string):
    
    result = []
    chars = [char for char in string]
    if len(chars) % 2 == 1:
        chars.append("_")
    
    for i in range(0, len(chars), 2):
        sliced = chars[i] + chars[i+1]
        result.append(sliced)
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


#Another Version

def anagram_difference(str1, str2):

    set1 = set(str1)
    set2 = set(str2)

    if set1 == set2:
        return 0
    
    elif set1 != set2:
        length_diff = abs(len(str1) - len(str2))
        if set1.isdisjoint(set2) is True:
            return len(str1) + len(str2)
        return length_diff 

print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0)
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2)
print(anagram_difference('a', 'aab') == 2)
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

## 31. Highest Scoring Word

Find the highest scoring word in a string. Each letter scores points based on its position in the alphabet: a = 1, b = 2, c = 3, ... z = 26. Return the highest scoring word. If two words score the same, return the word that appears earliest in the string.

Examples:

```python

high('man i need a taxi up to ubud') == 'taxi'
high('what time are we climbing up the volcano') == 'volcano'
high('take me to semynak') == 'semynak'
high('aaa b') == 'aaa'
```

<details>
<summary>Possible Solution</summary>

```python
def high(string):
   
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    abc_values = {}
    count = 1
    for char in alphabet:
        abc_values[char] = count
        count += 1
    
    split_str = string.split()
    word_values = {}
    for word in split_str:
        value_tmp = []
        for char in word:
            value_tmp.append(abc_values.get(char))
        total = sum(value_tmp)
        word_values[word] = total    
    highest = max(word_values, key=word_values.get)
    return highest


print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
print(high('aaa b') == 'aaa')
```

</details>

## 32. Replace Char with Score

Given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.

Examples:

```python
alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
alphabet_position("-.-'") == ""
```

<details>
<summary>Possible Solution</summary>

```python
def alphabet_position(string):
   
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    abc_values = {}
    count = 1
    for char in alphabet:
        abc_values[char] = count
        count += 1
    
    cleaned = [char for char in string.lower() if char.isalpha()]
    value_tmp = []
    for char in cleaned:
            value_tmp.append(str(abc_values.get(char)))
    return " ".join(value_tmp)

print(alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
print(alphabet_position("-.-'") == "")

```

</details>

## 33. Find the Suspect

Sherlock has to find suspects on his latest case. He will use your method. Suspect in this case is a person which has something not allowed in his/her pockets. Allowed items are defined by an array of numbers. Pockets contents are defined by map entries where key is a person and value is one or few things represented by an array of numbers (can be nil or empty array if empty).

Restated: If an item is in the allowed items array (the second argument), then it is allowed. If a person has only allowed items in their pockets, they are not a suspect. If a number is not in the allowed items array (the second argument), but it is in the dictionary, then it is not allowed, and the person is a suspect. The allowed items array defines which items are allowed, and any item not in that array is considered not allowed.

```python
pockets = {
    'bob': [1],
    'tom': [2, 5],
    'jane': [7]
}

find_suspects(pockets, [1, 2]) == ['tom', 'jane']
find_suspects(pockets, [1, 7, 5, 2]) == None
find_suspects(pockets, []) == ['bob', 'tom', 'jane']
find_suspects(pockets, [7]) == ['bob', 'tom']

```


<details>
<summary>Possible Solution</summary>

```python

pockets = {
    'bob': [1],
    'tom': [2, 5],
    'jane': [7]
}


def find_suspects(possessed_contents, allowed_items):
    suspects = []
    for candidate, contents in possessed_contents.items():
        for content in contents:
            if content not in allowed_items and candidate not in suspects:
                suspects.append(candidate)
    if not suspects:
        return None
    return suspects
    
print(find_suspects(pockets, [1, 2]) == ['tom', 'jane'])
print(find_suspects(pockets, [1, 7, 5, 2]) == None)
print(find_suspects(pockets, []) == ['bob', 'tom', 'jane'])
print(find_suspects(pockets, [7]) == ['bob', 'tom'])
```

</details>

## 34. Do the Wave

Create a function that turns a string into a Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.

Example:
```python 

wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
wave("") == []
wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
wave(" gap ") == [" Gap ", " gAp ", " gaP "]
```

<details>
<summary>Possible Solution</summary>

```python
def wave(input_str):
    if not input_str:
        return []
    else:
        result = []
        for i in range(len(input_str)):
            if input_str[i].isspace():
                continue
            element = input_str[:i] + input_str[i].upper() + input_str[i+1:]    
            result.append(element)
        return result


print(wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
print(wave("") == [])
print(wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"])
print(wave(" gap ") == [" Gap ", " gAp ", " gaP "])
```


</details>

## 35. Delete a Digit

Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

Examples:

```python

delete_digit(152) == 52
delete_digit(1001) == 101
delete_digit(10) == 1

```

<details>
<summary>Possible Solution</summary>

```python

def delete_digit(num):
    str_digits = [digit for digit in str(num)]
    digits = [int(digit) for digit in str_digits]
    minimum = min(digits)
    digits.remove(minimum)
    restring = [str(digit) for digit in digits]
    result = "".join(restring)
    return int(result)


print(delete_digit(152) == 52)
print(delete_digit(1001) == 101)
print(delete_digit(10) == 1)

```
</details>

## 36. Largest Product in a series

Complete the greatest_product method so that it'll find the greatest product of five consecutive digits  in the given string of digits.

Example:

```python

greatest_product("123834539327238239583") == 3240
greatest_product("395831238345393272382") == 3240
greatest_product("92494737828244222221111111532909999") == 5292
greatest_product("92494737828244222221111111532909999") == 5292
greatest_product("02494037820244202221011110532909999") == 0

```

<details>
<summary>Possible Solution</summary>

Note! First use of sliding window technique.

```python

def greatest_product(str_num):

    products = []
    holding = []
    str_digits = [digit for digit in str_num]
    digits = [int(digit) for digit in str_digits]
    k = 5
    for i in range(len(digits) - k + 1):
        holding.append(digits[i:i+k])

    for sublst in holding:
        product = 1
        for digit in sublst:
            product = product * digit
        products.append(product)
    
    return max(products)

print(greatest_product("123834539327238239583") == 3240)
print(greatest_product("395831238345393272382") == 3240)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("02494037820244202221011110532909999") == 0)

```

</details>

## 37. Encode Duplicates

The goal of this exercise is to convert a string to a new string where each character in the new string is `(` if that character appears only once in the original string, or `)` if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:
```python
duplicate_encode("din") == "((("
duplicate_encode("recede") == "()()()"
duplicate_encode("Success") == ")())())"
duplicate_encode("(( @") == "))(("
```

<details>
<summary>Possible Solution</summary>

```python

def duplicate_encode(input_str):
    tmp = []
    counts = {}
    chars = [char for char in input_str.lower()]
    for char in chars:
        counts[char] = counts.get(char, 0) + 1

    for char in chars:
        if counts[char] == 1:
            tmp.append('(')
        else:
            tmp.append(')')

    return "".join(tmp)

print(duplicate_encode("din") == "(((")
print(duplicate_encode("recede") == "()()()")
print(duplicate_encode("Success") == ")())())")
print(duplicate_encode("(( @") == "))((")

```

</details>

## 38. Update string

Assume `#` is like a backspace in string. This means that string `"a#bc#d"` actually is `"bd"`. Your task is to process a string with `#` symbols and return the final state of the string.

Examples:

```python
clean_string('abc#d##c') == "ac"
clean_string('abc####d##c#') == ""
```

<details>
<summary>Possible Solution</summary>

```python

def clean_string(input_string):
    result = []
    chars = [char for char in input_string]
    for char in chars:
        if char.isalpha():
            result.append(char)
        else:
            if len(result) > 0:
                result.pop()
            else:
                return ""
    
    return "".join(result)
   
print(clean_string('abc#d##c') == "ac")
print(clean_string('abc####d##c#') == "")

```
</details>

## 39. Sort Arrays (Case-Insensitive)

Sort the given strings in alphabetical order, case insensitive.

Example:

```python
sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"]
sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"]
```

<details>
<summary>Possible Solution</summary>

```python

def sortme(lst1):
   
   return sorted(lst1, key=str.lower)
              
print(sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"])
print(sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"])

```
</details>


## 40. Difference of Sum from Next Prime Number

Given a List `[]` of `n` integers, find the minimum number to be inserted in the list, so that the sum of all elements of the list should equal the closest prime number.

```python

minimum_number([3,1,2]) == 1
minimum_number([5,2]) == 0
minimum_number([1,1,1]) == 0
minimum_number([2,12,8,4,6]) == 5
minimum_number([50,39,49,6,17,28]) == 2
```

<details>
<summary>Possible Solution</summary>

```python
 PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    current_sum = sum(lst1)
    for number in PRIMES:
        if number >= current_sum:
            difference = number - current_sum
            break
    
    return difference

#Note: Prime is not found dynamically. If it needs to be, research "Sieve of Eratosthenes"
```
</details>

## 41. Counting Duplicate

Write a function that will return the count of distinct case-insensitive, alphabetic characters and numeric digits that occur more than once in the input string.

```python

duplicate_count("") == 0
duplicate_count("abcde") == 0
duplicate_count("abcdeaa") == 1
duplicate_count("abcdeaB") == 2
duplicate_count("Indivisibilities") == 2
```

<details>
<summary>Possible Solution</summary>

```python

def duplicate_count(input_str):

    if not input_str:
        return 0
    else:
        counts = {}
        chars = [char for char in input_str.lower()]
        for char in chars:
            counts[char] = counts.get(char, 0) + 1
        
        number_dupes = 0
        for value in counts.values():
            if value > 1:
                number_dupes += 1
        return number_dupes
    
print(duplicate_count("") == 0)
print(duplicate_count("abcde") == 0)
print(duplicate_count("abcdeaa") == 1)
print(duplicate_count("abcdeaB") == 2)
print(duplicate_count("Indivisibilities") == 2)

```
</details>

## 42. Find the Parents

Originally stated problem:

Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.

Legend:

- Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
- Function input: String contains only letters, uppercase letters are unique.

What to actually do: The problem is asking you to sort the input string in a specific way. The uppercase letters (mothers) should come first, followed by their corresponding lowercase letters (children). The letters should be sorted alphabetically, with the uppercase letter followed by all its corresponding lowercase letters.

For example, in the string "abBA", the sorted string would be "AaBb". The uppercase 'A' comes first, followed by its lowercase 'a', then the uppercase 'B', followed by its lowercase 'b'.

Example:

```python
find_children("abBA") == "AaBb"
find_children("AaaaaZazzz") == "AaaaaaZzzz"
find_children("CbcBcbaA") == "AaBbbCcc"
find_children("xXfuUuuF") == "FfUuuuXx"
find_children("") == ""
```

<details>
<summary>Possible Solution</summary>

```python

def find_children(input_str):
    if not input_str:
        return ""

    else:
        chars = [char for char in input_str]
        new_chars = sorted(chars, key=sort_the_kids)
        return "".join(new_chars)
    
def sort_the_kids(lst):
    for element in lst:
        return (element.upper(), element)

print(find_children("abBA") == "AaBb")
print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
print(find_children("CbcBcbaA") == "AaBbbCcc")
print(find_children("xXfuUuuF") == "FfUuuuXx")
print(find_children("") == "")

```
</details>

## 43. Digit Play

Some numbers have funny properties. For example:
```
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.

In other words:
Is there an integer `k` such as : `(a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k`? If it is the case we will return `k`, if not return `-1`. Note: `n` and `p` will always be given as strictly positive integers.

I gave it to the duck, because what?

It sounds like the problem is asking you to find a specific integer ( `k` ) given two positive integers ( `n` ) and ( `p` ). **The problem involves the digits of ( `n` ) and powers of ( `p `)**.

Here's a breakdown of the problem:

You have a number ( `n` ) with digits.
You also have a positive integer ( `p` ).

You need to calculate the sum of the digits of ( `n` ), each raised to successive powers starting from ( `p` ). For example, the first digit is raised to the power of ( `p` ), the second digit to the power of ( `p+1` ), and so on.
You then check if this sum is equal to ( n ) multiplied by some integer ( `k` ).
If such a ( `k` ) exists, you return it. If not, you return `-1`.

```python
dig_pow(89, 1) == 1
dig_pow(92, 1) == -1
dig_pow(46288, 3) == 51
dig_pow(695, 2) == 2
```
<details>
<summary>Possible Solution</summary>

```python

def dig_pow(number, power):
    temp = []
    digits = [int(char) for char in str(number)]
    power_count = 0
    for digit in digits:
        temp.append(digit ** (power+power_count))
        power_count += 1
    result = sum(temp)
    k = result // number
    if result == k * number:
        return k
    else:
        return -1


print(dig_pow(89, 1) == 1)
print(dig_pow(92, 1) == -1)
print(dig_pow(46288, 3) == 51)
print(dig_pow(695, 2) == 2)

```
</details>

## 44. Squared Array Check

Given two arrays `a` and `b` write a function `comp(a, b)` that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in `b` are the elements in `a` squared, regardless of the order.

``` python
comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True
comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False
comp(None, [1, 2, 3]) == False
comp([1, 2], []) == False
comp([1, 2], [1, 4, 4]) == False
```

<details>
<summary>Possible Solution</summary>

```python

def comp(a, b):
    if not a or not b:
        return False
    else:
        if len(a) == len(b):
            comparison = [number ** 2 for number in a]
            if set(comparison) == set(b):
                return True
            return False
        return False

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True)
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False)
print(comp(None, [1, 2, 3]) == False)
print(comp([1, 2], []) == False)
print(comp([1, 2], [1, 4, 4]) == False)

```
</details>

## 45. Count Digit Occurences

Your goal is to write the `group_and_count` method, which should receive a list as a unique parameter and return a hash. Empty or no input must return `None` instead of a hash. This hash returned must contain as keys the unique values of the list, and as values the counting of each value.

```python
group_and_count([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1}
group_and_count([]) == None
group_and_count(None) == None
group_and_count([1, 7, 5, -1]) == {1: 1, 7: 1, 5: 1, -1: 1}
```

<details>
<summary>Possible Solution</summary>

```python

def group_and_count(lst1):
    if not lst1 or None:
        return None
    else:
        counts = {}
        for number in lst1:
            counts[number] = counts.get(number, 0) + 1
        return counts

print(group_and_count([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1})
print(group_and_count([]) == None)
print(group_and_count(None) == None)
print(group_and_count([1, 7, 5, -1]) == {1: 1, 7: 1, 5: 1, -1: 1})

```
</details>


## 46. Triple double

Write a function `triple_double(num1, num2)` which takes numbers `num1` and num2 and returns `1` if there is a straight triple of a number at any place in `num1` and also a straight double of the same number in `num2`. If this isn't the case, return 0.

```python
triple_double(12345, 12345) == 0
triple_double(666789, 12345667) == 1 # 3 straight 6's in num1, 2 straight 6's in num2
```

<details>
<summary>Possible Solution</summary>

```python

def triple_double(num1, num2):
    
    digits1 = [int(char) for char in str(num1)]
    digits2 = [int(char) for char in str(num2)]
    temp = []
    
    for i in range(len(digits1) - 2):
        if digits1[i] == digits1[i+1] == digits1[i+2]:
            temp.append(1)
            break
    for i in range(len(digits2) - 1):
        if digits2[i] == digits2[i+1]:
            temp.append(1)
            break
    if temp:
        return temp[0]
    else:
        return 0
print(triple_double(12345, 12345) == 0)
print(triple_double(666789, 12345667) == 1) # 3 straight 6's in num1, 2 straight 6's in num2

```
</details>

## 47. Find the missing letter

Write a method that takes a list of consecutive (increasing) letters as input and that returns the missing letter in the list. You will always get a valid list. And it will be always exactly one letter be missing. The length of the array will always be at least 2. The array will always contain letters in only one case.

Example:

```
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
```
```python
p find_missing_letter(['a','b','c','d','f']) == 'e'
p find_missing_letter(['O','Q','R','S']) == 'P'
```

<details>
<summary>Possible Solution</summary>

```python

def find_missing_letter(abc_lst):
    abc_lower = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    abc_upper = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    
    temp = []
    k = len(abc_lst)
    start_value = abc_lst[0]

    if abc_lst[0].islower():
        start_index = abc_lower.index(start_value)
        temp.extend(abc_lower[start_index: start_index + k +1])
        for char in temp:
            if char not in abc_lst:
                return char
    
    elif abc_lst[0].isupper():
        start_index = abc_upper.index(start_value)
        temp.extend(abc_upper[start_index: start_index + k + 1])
   
        for char in temp:
            if char not in abc_lst:
                return char

print(find_missing_letter(['a','b','c','d','f']) == 'e')
print(find_missing_letter(['O','Q','R','S']) == 'P')
```

</details>

## 48. Reverse and combine text

Your task is to Reverse and Combine Words. Input: String containing different "words" separated by spaces

1. More than one word? Reverse each word and combine first with second, third with fourth and so on...
(odd number of words => last one stays alone, but has to be reversed too)

2. Start it again until there's only one word without spaces
3. Return your result…

Struggled with this one!

```python
reverse_and_combine_text("abc def") == "cbafed"
reverse_and_combine_text("abc def ghi jkl") == "defabcjklghi"
reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed"
reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") ==
"trzwqfdstrteettr45hh4325543544hjhjh21lllll"
reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf"
```

<details>
<summary>Possible Solution</summary>

```python

def reverse_and_combine_text(input_str):
    words = input_str.split()
    while len(words) > 1:
        # Reverse each word
        words = [word[::-1] for word in words]
        # Combine each pair of words
        combined = []
        i = 0
        while i < len(words):
            if i + 1 < len(words):
                combined.append(words[i] + words[i+1])
            else:
                combined.append(words[i])
            i += 2
        words = combined
    return words[0]


print(reverse_and_combine_text("abc def") == "cbafed")
print(reverse_and_combine_text("abc def ghi jkl") == "defabcjklghi")
print(reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed")
print(reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") == "trzwqfdstrteettr45hh4325543544hjhjh21lllll")
print(reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf")

```
</details>
