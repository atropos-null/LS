

def swap(string):
    words = string.split(" ")
    flipped_words = []
    for word in words:
        if len(word) == 1:
            flipped_words.append(word[0])
        else:
            first_letter = word[0]
            last_letter = word[-1]
            middle = word[1:-1]    
            together = last_letter + middle + first_letter
            flipped_words.append(together)
    sentence = " ".join(flipped_words)
    return sentence


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
