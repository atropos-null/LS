"""
Problem: Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. 

rules: 
- You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. 
- You may also assume that the same calendar will remain in use for the foreseeable future.
input: 4 digit integer
output: integer of how many day are friday the 13th

Example: 1986 => 1

Data Structure: List

Algorithm:
    = initiate empty list
    - get start date
    - get end date
    - set time delta to 1 day
    - make a position to be iterating over the days
    - Iterate over all the days of the given year.
    - use weekday = 4 and day 13
        = append list
    - next function counts the elements in the list and returns to main function.

""" 

import datetime 

def friday_the_13ths(year):

    result = []
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    delta = datetime.timedelta(days=1)
    position = start_date
    while position <= end_date:
        if position.weekday() == 4 and position.day == 13:  # Friday or 13th
            result.append(position)
        position += delta
    
    return get_count(result)

def get_count(list):

    element_count = 0
    for element in list:
        element_count += 1
    return element_count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True