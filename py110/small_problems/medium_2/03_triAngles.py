"""
Problem: Write a function that takes the three angles of a triangle as arguments and returns one of the following 
four strings representing the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

    - input: integers
    - output: string saying 'right', 'acute', 'obtuse', or 'invalid'

Example: 60, 70, 50 ==> 'acute'

Data Structure: List

Algorithm:
    - collect angles into a list
    - first check: sum the list to see if its greater than 180, and an all check if everthing is greater than 0
    - subcheck:
        - if an angle is right
        - if an angle is acute
        - if an angle is obtuse
    


"""

def triangle(angle1, angle2, angle3):
    
    all_angles = [angle1, angle2, angle3]
    if sum(all_angles) == 180 and all(angle > 0 for angle in all_angles):
        if any(angle == 90 for angle in all_angles):
            return 'right'
        elif all(angle < 90 for angle in all_angles):
            return 'acute'
        elif any(angle > 90 for angle in all_angles):
            return 'obtuse'
    else:
        return 'invalid'


print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True