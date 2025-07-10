""" 
Problem: Write a function that rotates the last count digits of a number. 
    - input: integers, number representing how many index places to go to
    - output: integer with one number changed position
    - rules:
        - move the first of the digits that you want to rotate to the end 
        - and then shift the remaining digits to the left
 
Example: 1200, 3 ==> 1002

Data Structure: No structure

Algorithm:
    - convert the number to a string
    - end = string[-digit]
    - front = string[:-digit]
    - middle = string[-digit:]
    - result = front + middle + end
    - return int(result)


"""

def rotate_rightmost_digits(number, count):
    if count == 1:
        return number
    else: 
        string = str(number)
        end = string[-count]
        front = string[:-count]
        middle = string[-count+1:]
        result = front + middle + end
    
    return int(result)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True