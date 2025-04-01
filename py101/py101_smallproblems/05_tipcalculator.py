amount = float(input("What is the amount of the bill? "))
tip_amount = float(input("What is the tip percentage? ")) / 100
tip_to_leave = amount * tip_amount
total = amount + tip_to_leave
print(f"The tip is ${tip_to_leave:.2f}")
print(f"The total is ${total:.2f}")