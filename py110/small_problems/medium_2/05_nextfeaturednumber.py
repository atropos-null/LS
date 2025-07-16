"""
Problem: Write a function that takes an integer as an argument and returns the next 
featured number greater than the integer. Issue an error message if there is no next featured number.

- input: integer
- output: integer or an error message

- rules:
    - has to be an odd number
    - has to be divisble by 7
    - all digits only occur once in the sequence
    - The largest possible featured number is 9876543201

Example: 12 => 21

Data Structure: none

Algorithm:

 - initiate max end
 - num = integer + 1 to start the count, so it doesn't count the integer passed to the function
 - while num <= max end:
    if num % 2 == 1 and num % 7 = 0
- check the set of the string to the length of the string

"""

def next_featured(integer):

    MAX_END = 9876543201
    num = integer + 1

    # Find the next odd multiple of 7
    while num <= MAX_END:
        if num % 2 == 1 and num % 7 == 0:
            # Check if all digits are unique
            if len(set(str(num))) == len(str(num)):
                return num
        num += 1

    return "There is no possible number that fulfills those requirements."


print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True