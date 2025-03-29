import sys

NATO = {
    "a": "Alfa",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliet",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sera",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "Xray",
    "y": "Yankee",
    "z": "Zulu"
    }

def clean_data(phrase):
    cleaner_phrase = phrase.lower()
    cleaned_list = [''.join(char for char in s if char.isalpha()) for s in cleaner_phrase]
    return cleaned_list

def convert_to_nato(cleaned_list):
    for item in cleaned_list:
        if item in NATO:
            print(NATO[item])
    
try:
    phrase = sys.argv[1]
    cleaned_list = clean_data(phrase)
    convert_to_nato(cleaned_list)
    
except IndexError:
    prompted_phrase = input("Text to spell out: ")
    cleaned_list = clean_data(prompted_phrase)
    convert_to_nato(cleaned_list)
