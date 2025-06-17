"""

Problem: Write a function that 
    - input: a list of positive integers as input 
        - multiplies all of the integers together
        - divides the result by the number of entries in the list 
    - output: returns the result as a string with the value rounded to three decimal places. {:.3f}

Example: [3, 5] ==> "7.500"

Data Structure:  list is passed as an argument, otherwise just an integer.

Algorithm:
    - result set to 1
    - for loop multipling the element to the result and saving that as the new result
    - divide result by len(list)
    - convert the integer to a string with an f-string to {result:.3f}


"""

def multiplicative_average(lists):

    temp_result = 1
    for element in lists:
        temp_result = element * temp_result
    new_result = float(temp_result / len(lists))
    return f"{new_result:.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")