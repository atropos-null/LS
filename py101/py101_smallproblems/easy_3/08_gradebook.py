def get_grade(number1, number2, number3):

    gross_score = number1 + number2 + number3
    grade = gross_score / 3
    
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >=60:
        return "D"
    else:
        return "F"


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True