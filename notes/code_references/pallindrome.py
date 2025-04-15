def is_palindrome(string):
    cleaned_str = clean_string(string)
    middle = len(cleaned_str) // 2
    if len(cleaned_str) % 2 == 0:
        if cleaned_str[0:middle] == cleaned_str[-1:middle-1:-1]:
            return True
        return False

    
    else:
        middle = len(cleaned_str) // 2
        if cleaned_str[0:middle+1] == cleaned_str[-1:middle-1:-1]:
            return True
        return False

def clean_string(string):
    cleaned_string = string.lower().replace(" ", "")
    for punctuation in ',.?;"-!':
        cleaned_string = cleaned_string.replace(punctuation, "")
    return cleaned_string

print(is_palindrome('CIVIC')) #True
print(is_palindrome('racecar!')) #True
print(is_palindrome('abba')) #True
print(is_palindrome('radar')) #True
print(is_palindrome('kayak')) #True
print(is_palindrome('No lemon, no melon')) #True
print(is_palindrome('did')) #True