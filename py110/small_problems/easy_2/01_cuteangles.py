"""

Problem: Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns 
a string representing that angle in degrees, minutes, and seconds. 
    - input: float between 0 and 360
    - output: angle as a string in degrees, minutes strings.
    - explicit rules: (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. 
    - implicit rules: There are 60 minutes in a degree, and 60 seconds in a minute.
    - Note: You can use the following constant to represent the degree symbol: DEGREE = "\u00B0"

Example: 30 results in "30°00'00\""

Data Structure: None
Algorithm:

- initalize empty list
- initialize degree variable 
    - degree equals floated_num coerced to int
    - append degree to working list
- initialize minutes variable
    - fractional_minutes equals floated_num minus degree multiplied by 60 *need this later
    - minutes equals fractional_minutes type coerced to int
    - append minutes to working list
- initialize second variable
    - seconds equals (minutes minus fractional_minutes) multiplied by 60
    - append seconds to working list

- concatenate the three elements in the list with the symbols in an f string and return

return f string
"""

DEGREE_SYMBOL = "\u00B0"

def dms(floated_num):

    degree = int(floated_num)
    fractional_minutes = (floated_num - degree) * 60
    minutes = int(fractional_minutes)
    seconds = int((fractional_minutes - minutes) * 60)

    return f"{degree}{DEGREE_SYMBOL}{minutes:02}'{seconds:02}\"" #Note the format for leading zeroes

# All of these examples should print True

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")