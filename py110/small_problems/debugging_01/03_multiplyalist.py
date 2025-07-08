def multiply_list(lst):
    return [item*2 for item in lst] #the fault was that the value of item *2 wasn't appended to a new list

print(multiply_list([1, 2, 3]) == [2, 4, 6])