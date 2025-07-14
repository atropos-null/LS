"""
Problem: Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to 
the function
    input: an integer
    output: an integer that's the nth number of that sequence that the input refers to

Example: 12 ==> 144

Data Structure: Dictionary

Algorithm
    - dictionary comprehension = 
        
        

"""

fib_nums = {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    6: 8,
    7: 13,
    8: 21,
    9: 34,
    10: 55,
    11: 89,
    12: 144,
    13: 233,
    14: 377,
    15: 610,
    16: 987,
    17: 1597,
    18: 2584,
    19: 4181,
    20: 6765,
}

def fibonacci(number):
    if number <= 20:
        return fib_nums[number]
    else:
        if number not in fib_nums:
            fib_nums[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return 


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True