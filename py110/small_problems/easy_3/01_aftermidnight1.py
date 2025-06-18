"""
Problem: The time of day can be represented as the number of minutes before or after midnight. 
If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, 
the time is before midnight.

    input: integer, positive or negative
    output: HH:MM in string, so imagine an f-string
    rules: 
        - no datetime module!
        - may go over just one single 24 hour time period

Example: -3 => "23:57"

Data Structure: None

Algo:
    - TOTAL_DAILY: 1440
    
    while abs(number) is greater than 1440: 
        - number = number - 1440

    
    - if number is 0:
        return "00:00"
    - elif number < 0
        - number = 1440 - number
        - hours = number // 60 
        - minutes = number % 60
        return f"{hours:02}:{minutes:02}"

    - else:
        - hours = number // 60 
        - minutes = number % 60
        return f"{hours:02}:{minutes:02}"
"""

def time_of_day(number):
    
    TOTAL_DAILY = 1440
    TOTAL_HOUR = 60

    abs_number = abs(number)

    while abs_number > TOTAL_DAILY: 
        abs_number = abs_number - TOTAL_DAILY
    
    if number == 0:
        return "00:00"
    elif number < 0:
        abs_number = TOTAL_DAILY - abs_number 
    hours = abs_number // TOTAL_HOUR
    minutes = abs_number % TOTAL_HOUR
    return f"{hours:02}:{minutes:02}"


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True