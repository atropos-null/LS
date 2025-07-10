""" 
Problem: Write a function that takes an integer as an argument and returns the maximum rotation of that integer. 
    - input: integer
    - output: integer

Example: Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in 
place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to 
get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four 
digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum 
rotation of the original number.

Data structure: String

Algorithm: 
    - i[0] becomes i[-1] 735291 => 352917
    - i[1] becomes i[-1] 352917 => 329175
    - i[2] becomes i[-1] 329175 => 321759
    - i[3] becomes i[-1] 321759 => 3215917
    - i[4] becomes i[-1] 3215917 => 321579

"""

def max_rotation(number):
    string = str(number)
  
    if len(string) == 1:
        return number
        
    else: 
        result = ''
        for i in range(len(string)):
            end = string[i]
            front = string[:i]
            middle = string[i+1:]
            result = front + middle + end
            string = result
        return int(result)
        
    
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
print(max_rotation(105) == 15)                 # True


""" Further Optimization:

def max_rotation(number):
    number_digits = len(str(number))
    for count in range(number_digits, 1, -1):
        number = rotate_rightmost_digits(number, count)

    return number
"""