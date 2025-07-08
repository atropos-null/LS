def reverse_string(string):
    new_string = "" #there was no string to capture the new order
    for char in string:
        new_string = char + new_string 
        
    return new_string #or, string[::-1]

print(reverse_string("hello") == "olleh")