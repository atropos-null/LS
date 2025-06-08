"""

Problem: Write a program that solicits six (6) numbers from the user and prints a message that 
describes whether the sixth number appears among the first five.

Example: 

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Data: List

Algorithm:

1) Iterate over a 6 numbers in a for loop, asking for user input
2) User input is collected into the list
    2.a) input the correct suffix on the printed input.
3) if last number in list, print out that it is in the list plus the contents of the list
4) if last number not in list, print out that its not in the list plus the contents of the list


"""

selection = []
suffixes = {1: "st",
          2: "nd",
          3: "rd",
          4: "th",
          5: "th",
}

for round in range(1,6):
    suffix = suffixes.get(round)
    user_number = input(f"Enter the {round}{suffix} number: ")
    selection.append(user_number)

last_number = input("Enter the last number: ")

if last_number in selection:
    print(f"{last_number} is in {','.join(selection)}.")
else:
    print(f"{last_number} isn't in {','.join(selection)}.")