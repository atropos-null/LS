"""
Problem: Write a function that takes... 
    - input: a list 
    - to do: reverse the list 
    - output: same list, No new id.
    - rules:
        - no reverse()
        - no slicing

Example: [1, 2, 3, 4] ==> [4, 3, 2, 1]

Data Structure: A list, already provided

Algo:
    - get length of list
    - for loop, range(length of list // 2)
    -   list[i], list[-(i+1)] == list[-(i+1)], list[i]
    - return list

"""

def reverse_list(lst):

    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]

    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])              # True
print(list1 is result)                     # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True