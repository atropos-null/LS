def triangle(number):

    asterisks = 0
    spaces = 0

    for i in range(number):
        asterisks += 1
        spaces = number - i
        print(f'{" " * spaces}{"*" * asterisks}')
     

triangle(5)
triangle(9)