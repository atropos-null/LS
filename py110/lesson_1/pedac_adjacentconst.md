##Sort Strings by Most Adjacent Consonants

>Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains and return the sorted list. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

>**Tasks**
>You are provided with the problem description above. Your tasks for this step are:

>Make notes of your mental model for the problem, including:

>inputs and outputs.

* input: a list of strings
* output: a sorted list of strings

>explicit and implicit rules.

* explicit: if two strings have the same number of highest constants, then their current order in the list persists.
* explicit: for this, x = consonants, y = vowels: 
    * `xxxyx` : `xxx` are adjacent consonants
    * `yxxyx xxy`: `xx`, and then `x xx` are adjacent consonants
* implict: lists maintain insertion order. Copies are needed?
    * `sorted()` preferred as it returns a new object. 
    * `reverse=True` sorts in descending order
* implicit: strings may have more than one word. (Didn't catch this one)


>Write a list of clarifying questions for anything that isn't clear.

* In which order should the list be populated?
* Do you want a new list or the same list?
* what about upper vs lower case?
* Is y a vowel??

Step 2:

```python
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
``` 

Tessa, Analyze:

* strings are all lowercase
* string length range from 2 elements to 7 elements
* there may, or may not be, spaces
* sorts in descending order
* original list placement stays when the number of constants are the same, see the list with the time categories and things that rhyme with yar.
* strings can't be empty
* only one consonant isn't enough to change order


Step 3: Do you have data?

Need a list. Probably need to a sorted list, leaving the original unchanged.

Step 4: Algorithm

* function definition, passing a list
* clean data, removing spaces.
* empty dictionary
* count set to 0
* a string of consonants, lower case:  bcdfghjklmnpqrstvwxyz
* for loop through len(list) 
* check to see if char of the given element is in the consonants list
    * if yes, count += 1
    * elif count only equals one, don't write to the dictionary ??
* write to dictionary element = number of consonants
* reset count to 0
* sort dictionary via the values, with d.items
* create new object of d.keys
* flatten d.keys to a list
* return list


Page Reference: [Sort by Most Adjacent Consonants](https://launchschool.com/lessons/1b66cd61/assignments/8cf7942d)