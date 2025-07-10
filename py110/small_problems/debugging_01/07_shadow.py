def summation(numbers, factor):  # the original definition name was sum, which is another built in module. 
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(summation(numbers, 2) == 20) #change the name of the definition and it works.