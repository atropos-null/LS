"""
A prime number is a positive number that is evenly divisible only by itself and 1. 
Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not prime since it has divisors of 
1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.

Problem: Write a function that...
    - input:  takes a positive integer as an argument
    - output: returns True if the number is prime, False if it is not prime.
    - rules: You may not use any of Python's add-on packages to solve this problem. 
    
Example 1 == False

Data Structure: None

Algorithm:
    - handle out what happens with 1
    - for i in range(2, whatever number)
        - does integer  % 1 == 0?
            return False if so
    - Return True

"""

def is_prime(integer):
    if integer == 1:
        return False
    for i in range(2, integer):
        if integer % i == 0:
            return False
    return True


print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True