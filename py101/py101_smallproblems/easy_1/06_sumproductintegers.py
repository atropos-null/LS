#Write a program that asks the user to enter an integer greater than 0, then asks whether 
#the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

def sum_it_up(num):
    to_total = []
    for i in range(1, num+1):
        to_total.append(i)
    sum_total = sum(to_total)
    return sum_total

def multiply_num(num):
    product_total = 1
    for i in range(1, num):
        product_total += product_total * i
    return product_total

while True:
    try:
        num = int(input("Please enter an integer greater than 0: "))
        if num <= 0:
            print("The number must be greater than 0.")
            continue
        methodology = input("Enter 's' to compute the sum, or 'p' to compute the product. ")


        if methodology == 's':
            sum_total = sum_it_up(num)
            print(f"The sum of the integers between 1 and {num} is {sum_total}")
            break
        elif methodology == 'p':
            product_total = multiply_num(num)
            print(f"The product of the integers between 1 and {num} is {product_total} ")
            break
        else:
            print("Invalid choice. Please enter 's' for sum or 'p' for product.")
    
    except ValueError:
        print("Invalid choice. Please enter 's' for sum or 'p' for product. ")
