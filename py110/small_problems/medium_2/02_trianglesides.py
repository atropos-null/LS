"""
Problem: Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the 
following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.

Example: 3, 3, 3 = equilateral

Data Structure: None

Algorithm: 

if side1 = side2 = side 3:
    return "equilateral

elif side1 = side2 or side1 = side3 or side2 = side3:
    return "isoceles"

elif side1 != side2 != side3:
    return "scalene"

else:
    return "invalid"
"""

def triangle(side1, side2, side3):

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "invalid"
    
    elif side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return "invalid"

    elif side1 == side2 == side3:
        return "equilateral"

    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"

    elif side1 != side2 and side1 != side3 and side2 != side3:
        return "scalene"


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True