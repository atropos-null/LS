# Reoccuring struggles with PY110/PY119 problems

## 1, Sorting with Extra Steps Part 1

How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?

```python
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
```

<details>
<summary>Possible Solution</summary>

```python
def get_published_year(book):
    return int(book['published'])

sorted_books = sorted(books, key=get_published_year)
print(sorted_books)

#Alternative take:

sorted_books = sorted(books, key=lambda book: int(book['published']))

print(sorted_books)
```
</details>

## 2. Sorting With Extra Steps, Part 2

Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

```python
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

#Expected Result: [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
```

<details>
<summary>Possible Solution</summary>

```python
def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

result = [transform_item(item) for item in dict1.values()]
print(result) 


```

</details>

## 3. Sorting with Extra Steps, Part 3

Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.

```python

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

#Expected result: [{'e': [8], 'f': [6, 10]}]
```

<details>
<summary>Possible Solution</summary>

```python
def list_is_even(number_list):
    return all(num % 2 == 0 for num in number_list)

def all_even(dictionary):
    return all(list_is_even(lst) for lst in dictionary.values())

result = [d for d in lst if all_even(d)]
```
</details>

## 4. Sorting with Extra Steps, Part 4

Given the following dictionary, create a new dictionary where each key maps to a list of words from the original value that have more than 4 characters.

Expected result: `{'morning': ['quick', 'brown', 'jumps'], 'afternoon': ['sleeping'], 'evening': ['under', 'bright', 'starry']}`

```python
sentences = {
    'morning': 'the quick brown fox jumps',
    'afternoon': 'over the lazy dog sleeping',
    'evening': 'under the bright starry sky'
}
```

<details>
<summary>Possible Solution</summary>

```python

def get_4(dict1):
    result = {}
    for key, values in sentences.items():
        tmp = []
        words = values.split()
        for word in words:
            if len(word) >= 4:
                tmp.append(word)
    return tmp

new_dict = {key: get_4(value) for key, value in sentences.items()}
print(new_dict)

```

</details>

## 5. Nested Data Structure Comprehensions with Dictionaries, Part 1 

I did get this to work the second pass but it wasn't elegant. 

Task:​ Extract all book titles from all categories. Expected Result:​ ['1984', 'Brave New World', 'Cosmos', 'Brief History']

```python
library = {
    'fiction': {
        'books': [
            {'title': '1984', 'author': 'Orwell', 'pages': 328},
            {'title': 'Brave New World', 'author': 'Huxley', 'pages': 268}
        ]
    },
    'science': {
        'books': [
            {'title': 'Cosmos', 'author': 'Sagan', 'pages': 365},
            {'title': 'Brief History', 'author': 'Hawking', 'pages': 256}
        ]
    }
}
```

<details>
<summary>Possible Solution</summary>

```python
titles = [book['title'] for category in library.values() for book in category['books']]
print(titles)
```
</details>

## 6. Nested Data Structure Comprehensions with Dictionaries, Part 2

Task:​ Extract all team leads from all departments. Expected Result:​ `['Alice', 'Charlie', 'Eve', 'Grace']`

```python
company = {
    'engineering': {
        'teams': {
            'frontend': {'members': ['Alice', 'Bob'], 'lead': 'Alice'},
            'backend': {'members': ['Charlie', 'Diana'], 'lead': 'Charlie'}
        }
    },
    'marketing': {
        'teams': {
            'digital': {'members': ['Eve', 'Frank'], 'lead': 'Eve'},
            'print': {'members': ['Grace'], 'lead': 'Grace'}
        }
    }
}
```

<details>
<summary>Possible Solution</summary>

```python
leads = [people['lead'] for teams in company.values() for groups in teams.values() for people in groups.values()]
print(leads)
```
</details>

## 7. PY110-119 Spot Wiki Problems, 9 Typoglycemia Generator

Write a function that generates text following a pattern where:
- the first and last characters of each word remain in their original place
- characters between the first and last characters are sorted alphabetically
- punctuation should remain at the same place as it started

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

## 8. PY110-119 Spot Wiki Problems, 20 Character Count Sorting

Write a function that takes a string as an argument and groups the number of times each character appears in the string as a dictionary sorted by the highest number of occurrences.

The characters should be sorted alphabetically, and you should ignore spaces, special characters, and count uppercase letters as lowercase ones.

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
def get_char_count(input_str):
    chars = [char.lower() for char in input_str if char.isalpha()]
    count_dicts = {}
    for char in chars:
        count_dicts[char] = count_dicts.get(char, 0) + 1
    final_dict = {}
    sorted_final = {}
    for char, count in count_dicts.items():
        if count in final_dict:
            final_dict[count].append(char) #How to append a list as a dictionary value.
        else:
            final_dict[count] = [char]
    for count in final_dict:
        final_dict[count].sort(reverse=True)
    for count in sorted(final_dict.keys(), reverse=True):
        sorted_final[count] = final_dict[count]
    
    return sorted_final
```

</details>

## 9. PY110-119 Spot Wiki Problems, 23 Longest alphabetical substring

Write a function `longest(s)` that finds and returns the longest substring of s where the characters are in alphabetical order. 

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

## 10. PY110-119 Spot Wiki Problems, 48 Reverse and combine text

Your task is to Reverse and Combine Words. Input: String containing different "words" separated by spaces

More than one word? Reverse each word and combine first with second, third with fourth and so on... (odd number of words => last one stays alone, but has to be reversed too)

Start it again until there's only one word without spaces

Return your result

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