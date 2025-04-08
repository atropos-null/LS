

def stringy(number):

    ones_zeroes = []

    for _ in range(number // 2):
        ones_zeroes.append("1")
        ones_zeroes.append("0")
    
    if number % 2 != 0:
        ones_zeroes.append("1")
               
    string = "".join(ones_zeroes)
    return string
    

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True