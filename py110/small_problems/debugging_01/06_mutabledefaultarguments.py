def append_to_list(value, lst=None):
    if lst == None:         #default lists are only created once
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2]) #this run appends to the list that already has [1] in it, making it [1,2] 
        