def clean_up(string):
    clean_text = ''
    
    for idx, char in enumerate(string):
        if char.isalpha():
            clean_text += char
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '
            
    return clean_text


print(clean_up("---what's my +*& line?") == " what s my line ") # True