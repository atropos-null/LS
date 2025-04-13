## Python Ternary Operator Practice Problems

Reminder: Basic Syntax is `expression1 if condition else expression2`


1. Basic: Convert the following if/else statement to a ternary operator expression:

```python
if num > 0:
    result = "Positive"
else:
    result = "Non-positive"
```
Solution:
||result = "Positive" if num > 0 else "Non-positive"||

2. Basic: Write a ternary expression that assigns "Even" to the variable number_type if a number is even, and "Odd" if it's odd.

Solution:
||number_type = "Even" if number % 2 == 0 else "Odd"||

3. Intermediate: Convert the following nested if/else statement to a ternary operator:
```python
if score >= 90:
    grade = "A"
else:
    if score >= 80:
        grade = "B"
    else:
        grade = "C"

```

Solution:
||grade = "A" if score >= 90 else "B" if score >= 80 else "C"||

4. Intermediate:  Write a function using a ternary operator that returns the absolute value of a number without using the built-in abs() function.

Solution:
||def absolute_value(num):
    return num if num >= 0 else -num||

5. Basic: Use a ternary operator to assign "Weekend" to day_type if day is "Saturday" or "Sunday", otherwise assign "Weekday".

Solution:
||day_type = "Weekend" if day in ["Saturday", "Sunday"] else "Weekday"||

6. Intermediate: Create a ternary expression that returns the smaller of two numbers.

Solution: 
||smaller = a if a < b else b||

7. Advanced: Write a function that uses a ternary operator to determine if a year is a leap year.

||def is_leap_year(year):
    return True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False||

8. Intermediate: Use a ternary operator to assign "Passing" to result if score is at least 60, otherwise "Failing".

Solution:
||result = "Passing" if score >= 60 else "Failing"||

9. Advanced: Write a function using nested ternary operators that returns "High" if a number is greater than 100, "Medium" if it's between 50 and 100 inclusive, and "Low" otherwise.

Solution:
||def categorize_number(num):
    return "High" if num > 100 else "Medium" if num >= 50 else "Low"||

10. Intermediate: Convert this function to use a ternary operator:

```python
def get_fee(is_member):
    if is_member:
        return 10.0
    else:
        return 20.0
```

Solution:
||def get_fee(is_member):
    return 10.0 if is_member else 20.0||

11. Basic: Use a ternary operator to ensure a number is within the range 0-255 by setting it to 0 if negative or 255 if greater than 255.

Solution:
||clamped = 0 if num < 0 else 255 if num > 255 else num||

12. Intermediate:  Debugging: What's wrong with this ternary expression and how would you fix it?

```python
result = if x > 0 "Positive" else "Negative"
```

Solution:
||result = "Positive" if x > 0 else "Negative"||

13. Basic: Write a ternary expression that returns "Adult" if age is at least 18, otherwise "Minor".

Solution:
||status = "Adult" if age >= 18 else "Minor"||

14. Intermediate: Use a ternary operator to assign the larger of two lists to `larger_list `based on their lengths.

Solution:
||larger_list = list1 if len(list1) >= len(list2) else list2||

15. Advanced: Write a ternary expression to check if a string is a palindrome.

Solution:

||is_palindrome = True if text.lower() == text.lower()[::-1] else False||
