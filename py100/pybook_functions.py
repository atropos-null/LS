#def main():
#    x = float(input("Enter the first number: "))
#    y = float(input("Enter the second number: "))
#    print(f"{x} * {y} = {multiply(x, y)}.")


#def multiply(x, y):
#    product = x * y
#    return product


   # numbers_1 = [0, 1, 2, 3, 4, 5, 6]
   # numbers_2 = [1, 2, 4, 5]
   # numbers_3 = [0, 3, 6]
   # numbers_4 = []

    #print(any(remainders_3(numbers_1)))
    #print(any(remainders_3(numbers_2)))
    #print(any(remainders_3(numbers_3)))
    #print(any(remainders_3(numbers_4)))
      
#def remainders_3(numbers):
    #return [number % 3 for number in numbers]

def main():
    numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
    numbers_3 = [0, 5, 10]
    numbers_4 = []

    print(all(remainders_5(numbers_1)))
    print(all(remainders_5(numbers_2)))
    print(all(remainders_5(numbers_3)))
    print(all(remainders_5(numbers_4)))

def remainders_5(numbers):
    return [number % 5 for number in numbers]

main()