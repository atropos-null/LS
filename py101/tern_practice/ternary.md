## Python Ternary Operator Practice Problems

Reminder: Basic Syntax is `expression1 if condition else expression2`

1. Basic: Convert the following if/else statement to a ternary operator expression:

```python
if num > 0:
    result = "Positive"
else:
    result = "Non-positive"
```

<details>
<summary>Solution</summary>

```python
result = "Positive" if num > 0 else "Non-positive"
```
</details>

2. Basic: Write a ternary expression that assigns "Even" to the variable number_type if a number is even, and "Odd" if it's odd.

<details>
<summary>Solution</summary>

```python
number_type = "Even" if number % 2 == 0 else "Odd"
```
</details>

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

<details>
<summary>Solution</summary>

```python
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```
</details>

4. Intermediate: Write a function using a ternary operator that returns the absolute value of a number without using the built-in abs() function.

<details>
<summary>Solution</summary>

```python
def absolute_value(num):
    return num if num >= 0 else -num
```
</details>

5. Basic: Use a ternary operator to assign "Weekend" to day_type if day is "Saturday" or "Sunday", otherwise assign "Weekday".

<details>
<summary>Solution</summary>

```python
day_type = "Weekend" if day in ["Saturday", "Sunday"] else "Weekday"
```
</details>

6. Intermediate: Create a ternary expression that returns the smaller of two numbers.

<details>
<summary>Solution</summary>

```python
smaller = a if a < b else b
```
</details>

7. Advanced: Write a function that uses a ternary operator to determine if a year is a leap year.

<details>
<summary>Solution</summary>

```python
def is_leap_year(year):
    return True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False
```
</details>

8. Intermediate: Use a ternary operator to assign "Passing" to result if score is at least 60, otherwise "Failing".

<details>
<summary>Solution</summary>

```python
result = "Passing" if score >= 60 else "Failing"
```
</details>

9. Advanced: Write a function using nested ternary operators that returns "High" if a number is greater than 100, "Medium" if it's between 50 and 100 inclusive, and "Low" otherwise.

<details>
<summary>Solution</summary>

```python
def categorize_number(num):
    return "High" if num > 100 else "Medium" if num >= 50 else "Low"
```
</details>

10. Intermediate: Convert this function to use a ternary operator:

```python
def get_fee(is_member):
    if is_member:
        return 10.0
    else:
        return 20.0
```

<details>
<summary>Solution</summary>

```python
def get_fee(is_member):
    return 10.0 if is_member else 20.0
```
</details>

11. Basic: Use a ternary operator to ensure a number is within the range 0-255 by setting it to 0 if negative or 255 if greater than 255.

<details>
<summary>Solution</summary>

```python
clamped = 0 if num < 0 else 255 if num > 255 else num
```
</details>

12. Intermediate: Debugging: What's wrong with this ternary expression and how would you fix it?

```python
result = if x > 0 "Positive" else "Negative"
```

<details>
<summary>Solution</summary>

```python
result = "Positive" if x > 0 else "Negative"
```
</details>

13. Basic: Write a ternary expression that returns "Adult" if age is at least 18, otherwise "Minor".

<details>
<summary>Solution</summary>

```python
status = "Adult" if age >= 18 else "Minor"
```
</details>

14. Intermediate: Use a ternary operator to assign the larger of two lists to `larger_list` based on their lengths.

<details>
<summary>Solution</summary>

```python
larger_list = list1 if len(list1) >= len(list2) else list2
```
</details>

15. Advanced: Write a ternary expression to check if a string is a palindrome.

<details>
<summary>Solution</summary>

```python
is_palindrome = True if text.lower() == text.lower()[::-1] else False
```
</details>