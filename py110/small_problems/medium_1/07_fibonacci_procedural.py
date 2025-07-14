"""
Problem: Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to 
the function
    input: an integer
    output: an integer that's the nth number of that sequence that the input refers to

Example: 12 ==> 144

Data Structure: list

Algorithm

    - sequence = [0, 1, 1,]
    - for i in range(number-2):
        sequence.append(i+sequence[-1])
        

"""

def fibonacci(number):
    sequence = [1, 1] #I prefer using [0,1]
    for _ in range(number):
        sequence.append(sequence[-2]+sequence[-1])
    return sequence[number-1] #and then sequence[number]
                   

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True