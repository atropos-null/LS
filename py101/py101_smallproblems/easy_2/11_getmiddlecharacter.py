def center_of(string):
    length_str = len(string)
    half_way = length_str // 2
    if length_str % 2 == 0:
        slice = string[half_way-1:half_way+1]
        return slice
    else:
        slice = string[half_way]
        return slice


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True