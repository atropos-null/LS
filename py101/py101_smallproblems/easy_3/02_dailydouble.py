
def crunch(string):
    cleaned_list = []
    if string == '':
        return string
    
    else:
        for i in range(len(string) - 1):
            if string[i] != string[i+1]:
                cleaned_list.append(string[i])
            elif string[i] == ' ':
                cleaned_list.append(string[i])
        cleaned_list.append(string[-1]) #to handle the last string element
        cleaned_string = "".join(cleaned_list)
   
    return cleaned_string


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')