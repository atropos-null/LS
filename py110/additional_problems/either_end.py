""" Iterate over a string taking the first and last character and creating a new substring, appending to a list. 
Then move inwards towards the center until you run out of string. Return the list. 

string = 'lorem ipsum'
print(either_end(string) == ['lm', 'ou', 'rs', 'ep', 'mi', ' '])

string = 'helloworld'
print(either_end(string) == ['hd', 'el', 'lr', 'lo', 'ow',])

string = '1234'
print(either_end(string) == ['14', '23'])

string = ''
print(either_end(string) == [])

"""

def either_end(input_str):
    
    # if not input_str:
    #     return []

    # result = []
  
    # for i in range((len(input_str) + 1) // 2):
    #     if len(input_str) %2  == 1:
    #         if i == (len(input_str) - 1) // 2:
    #             result.append(input_str[i])
    #         else:
    #             snippet = input_str[i]+input_str[-(i+1)]
    #             result.append(snippet)

    #     else:
    #         snippet = input_str[i]+input_str[-(i+1)]
    #         result.append(snippet)
    # return result

    list_result = []
    split_words = [char for char in input_str]
    while len(split_words) > 1:
        front = split_words[0]
        back = split_words[-1]
        list_result.append(front+back)
        split_words.pop(0)
        split_words.pop(-1)
    
    if len(split_words) == 1:
        list_result.append(split_words[0])
    
    return list_result
   
# TESTS
string = 'cavt'
print(either_end(string) == ['ct', 'av'])

# LS tests
string = 'lorem ipsum'
print(either_end(string) == ['lm', 'ou', 'rs', 'ep', 'mi', ' '])

string = 'helloworld'
print(either_end(string) == ['hd', 'el', 'lr', 'lo', 'ow',])

string = '1234'
print(either_end(string) == ['14', '23'])

string = ''
print(either_end(string) == [])


"""
def either_end(input_str):

    list_result = []
    split_words = [char for char in input_str]
    while len(split_words) > 1:
        front = split_words[0]
        back = split_words[-1]
        list_result.append(front+back)
        split_words.pop(0)
        split_words.pop(-1)
    
    if len(split_words) == 1:
        list_result.append(split_words[0])
    
    return list_result

"""