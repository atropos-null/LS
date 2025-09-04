# Given two words, how many letters do you have to remove from them to make them anagrams?
# anagram: a word or phrase that's formed by rearranging the letters of another word or phrase.


def anagram_difference(str1, str2):
    if not str1 and not str2:
        return 0
    
    elif (str1 and not str2) or (str2 and not str1):
        return 1
    
    else:
        dict1 = make_dict(str1)
        total1 = sum(dict1.values())
        
        dict2 = make_dict(str2)
        total2 = sum(dict2.values())
        
        common_keys = dict1.keys() & dict2.keys()
        dict3 = {key: min(dict1[key], dict2[key]) for key in common_keys}
        total3 = sum(dict3.values())

        half1 = abs(total1 - total3)
        half2 = abs(total2 - total3)
        return half1+half2
    
def make_dict(string):
    dictionary = {}
    for char in string:
        dictionary[char] = dictionary.get(char, 0) + 1
    return dictionary
    
    
print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0 )
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2 )
print(anagram_difference('a', 'aab') == 2 )
print(anagram_difference('codewars', 'hackerrank') == 10 )
print(anagram_difference("oudvfdjvpnzuoratzfawyjvgtuymwzccpppeluaekdlvfkhclwau", "trvhyfkdbdqbxmwpbvffiodwkhwjdjlynauunhxxafscwttqkkqw") == 42)
print(anagram_difference("fcvgqognzlzxhmtjoahpajlplfqtatuhckxpskhxiruzjirvpimrrqluhhfkkjnjeuvxzmxo", "qcfhjjhkghnmanwcthnhqsuigwzashweevbegwsbetjuyfoarckmofrfcepkcafznykmrynt") == 50)