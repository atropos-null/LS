# Create a function that counts the frequency of each character in a string and 
# returns the result as a dictionary.

text = "Launch School is a great place to learn programming"

def count_string(string):
    result = {}
    cleaned_text = clean_string(string)
    for character in cleaned_text:
        if character not in result:
            result[character] = 1
        else:
            result[character] += 1
    return result

def clean_string(string):
    cleaned_string = string.lower().replace(" ", "")
    for punctuation in ',.?;"-!':
        cleaned_string = cleaned_string.replace(punctuation, "")
    return cleaned_string


print(count_string(text))



# How to do it with count()
    
#def count_string(string):
    # result = {}
    # cleaned_text = clean_string(string)
    # for character in cleaned_text:
    #     result[character] = cleaned_text.count(character)
    # return result

# How to do it with get()
# def count_string(string):
#     result = {}
#     cleaned_text = clean_string(string)
#     for character in cleaned_text:
#         # Use get() method with default value
#         result[character] = result.get(character, 0) + 1
#     return result