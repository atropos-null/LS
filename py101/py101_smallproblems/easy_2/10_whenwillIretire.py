import datetime


age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))
year = datetime.date.today().year
how_many = retirement_age - age
what_year = year + how_many

print(f"It's {year}. You will retire in {what_year}.")
print(f"You only have {how_many} years to go!")