#Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise.

import random

number = random.randint(1, 1000)

def isnt_it_odd(number):
    if abs(number) % 2 == 1:
        return True
    else:
        return False

print(number, isnt_it_odd(number))