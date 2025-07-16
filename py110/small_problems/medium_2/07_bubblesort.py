""" 

Problem: Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm. 
The sorting should be done "in-place" -- that is, the function should mutate the list. You may assume that the list 
contains at least two elements.

Example: [5,3] = > [3,5]

Data Structure: List

Algorithm = 

    - get length of list
    - for loop, i  range (n-1):
        - nested for loop, j range (n-i-1)
        - temp = lst[j]
        - lst[j] = lst[j+1]
        - lst[j+1] = temp

"""

# Bubble Sort pseudocode

def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        # Last i elements are already sorted
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                # Swap arr[j] and arr[j+1]
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

    return lst


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True


""" Further Optimization:

a while loop with a swapped flag:

def bubble_sort(lst):
    n = len(lst)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                swapped = True
        n -= 1  # After each pass, the largest element is at the end
    print(lst)
    return lst
    

"""