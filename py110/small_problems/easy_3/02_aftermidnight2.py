"""
Instructions: Write two functions that each take a time of day in 24 hour format, and return the number of minutes 
before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

Problem: Two functions, one that adds from midnight and one that subtracts from midnight
    - input: string in "HH:MM" format
    - output: integer 

Example: 
    after_midnight("12:34") == 754
    before_midnight("12:34") == 686

Data structure: list for holding

Algo: 
    - initialize empty list
    - numbers = split string at ":"
    - convert numbers to int
    - add numbers together to get final integer
    - handle 24:00 or 0:00

"""

HOURS = 60
TOTAL_DAILY = 1440

def after_midnight(time):
    temp_list = []
    numbers = time.split(":")
    for num in numbers:
        temp_list.append(int(num))
    converted_hours = temp_list[0] * HOURS
    after_time = converted_hours + temp_list[1]
    if after_time == TOTAL_DAILY:
        return 0
    return after_time
    

def before_midnight(time):
    temp_list = []
    numbers = time.split(":")
    for num in numbers:
        temp_list.append(int(num))
    converted_hours = temp_list[0] * HOURS
    before_time = TOTAL_DAILY - (converted_hours + temp_list[1])
    if before_time == TOTAL_DAILY:
        return 0
    return before_time
    
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True