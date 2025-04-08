def twice(number):
    s = str(number)
    if (len(s) % 2 == 0) and (s[0] == s[(int(len(s))//2)]):
        return int(s)
        
    else:
        return (int(s) * 2)

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True