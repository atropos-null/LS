"""
Problem: Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to 
the function
    input: an integer
    output: an integer that's the nth number of that sequence that the input refers to

Example: 12 ==> 144

Data Structure: list

Algorithm

    - if number  < 2 return 1 each time
    - redo the problem example into a function 
        F(n) = F(n - 1) + F(n - 2) 
        
        

"""

def fibonacci(number):
    if number <= 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True