# Python Operator Precedence Exercises

Practice evaluating logical operator expressions. Click the **Solution** dropdown to check your answer.

---

### Logical Operator Exercises  
1. `print('' or 0 and [])`  
<details><summary>Solution</summary>  
`0`  
</details>  

2. `print(0 or 'Python' and None)`  
<details><summary>Solution</summary>  
`None`  
</details>  

3. `print([] and {} or 42)`  
<details><summary>Solution</summary>  
`42`  
</details>  

4. `print(100 or 'Hello' and 0)`  
<details><summary>Solution</summary>  
`100`  
</details>  

5. `print('False' and True or 0)`  
<details><summary>Solution</summary>  
`True`  
</details>  

6. `print(None or 'Exist' and 42)`  
<details><summary>Solution</summary>  
`42`  
</details>  

7. `print(0 and 'Zero' or 'Not Zero')`  
<details><summary>Solution</summary>  
`Not Zero`  
</details>  

8. `print([1, 2] or 'List' and {})`  
<details><summary>Solution</summary>  
`[1, 2]`  
</details>  

9. `print('' or [] and 'Empty')`  
<details><summary>Solution</summary>  
`[]`  
</details>  

10. `print(False and 'No' or 'Yes')`  
<details><summary>Solution</summary>  
`Yes`  
</details>  

---

### Mixed Data Types  
11. `print('Hello' and '' or 'World')`  
<details><summary>Solution</summary>  
`World`  
</details>  

12. `print(0.0 or () and 'text')`  
<details><summary>Solution</summary>  
`()`  
</details>  

13. `print('Apple' and 0 or 'Banana')`  
<details><summary>Solution</summary>  
`Banana`  
</details>  

14. `print(not True and False or True)`  
<details><summary>Solution</summary>  
`True`  
</details>  

15. `print((None or 'Valid') and 100)`  
<details><summary>Solution</summary>  
`100`  
</details>  

16. `print('' and 'Python' or 'Fallback')`  
<details><summary>Solution</summary>  
`Fallback`  
</details>  

17. `print(True or False and 'ShortCircuit')`  
<details><summary>Solution</summary>  
`True`  
</details>  

18. `print(100 and 0.0 or 'Number')`  
<details><summary>Solution</summary>  
`Number`  
</details>  

19. `print('' or 0j and 'Complex')`  
<details><summary>Solution</summary>  
`0j`  
</details>  

20. `print('Python' and [] or 'Empty')`  
<details><summary>Solution</summary>  
`Empty`  
</details>  

---

### Parentheses for Precedence  
21. `print({} or () and 'NonEmpty')`  
<details><summary>Solution</summary>  
`()`  
</details>  

22. `print(False or (1, 2) and [])`  
<details><summary>Solution</summary>  
`[]`  
</details>  

23. `print('0' and 0 or 'Final')`  
<details><summary>Solution</summary>  
`Final`  
</details>  

24. `print([False] and 'Truthy' or 'Falsy')`  
<details><summary>Solution</summary>  
`Truthy`  
</details>  

25. `print(0.0 or '' and 100)`  
<details><summary>Solution</summary>  
`''`  
</details>  

26. `print('Text' and None or 'Default')`  
<details><summary>Solution</summary>  
`Default`  
</details>  

27. `print(42 and '' or 3.14)`  
<details><summary>Solution</summary>  
`3.14`  
</details>  

28. `print(False and {} or ())`  
<details><summary>Solution</summary>  
`()`  
</details>  

29. `print('' or 0.0 and 'Zero')`  
<details><summary>Solution</summary>  
`0.0`  
</details>  

30. `print(None and 'Skip' or 'Proceed')`  
<details><summary>Solution</summary>  
`Proceed`  
</details>  

---

### Advanced Combinations  
31. `print(('' or 'A') and 'B')`  
<details><summary>Solution</summary>  
`B`  
</details>  

32. `print('A' or ('B' and 'C'))`  
<details><summary>Solution</summary>  
`A`  
</details>  

33. `print((0 or 1) and (1 or 0))`  
<details><summary>Solution</summary>  
`1`  
</details>  

34. `print((None and 'X') or 'Y')`  
<details><summary>Solution</summary>  
`Y`  
</details>  

35. `print(('True' or False) and 'Result')`  
<details><summary>Solution</summary>  
`Result`  
</details>  

36. `print(('' and 'Empty') or 'Full')`  
<details><summary>Solution</summary>  
`Full`  
</details>  

37. `print(([] or {}) and 'Valid')`  
<details><summary>Solution</summary>  
`Valid`  
</details>  

38. `print(('Apple' and 0) or 'Orange')`  
<details><summary>Solution</summary>  
`Orange`  
</details>  

39. `print((False or []) and 'Value')`  
<details><summary>Solution</summary>  
`[]`  
</details>  

40. `print((100 and 0) or 'NonZero')`  
<details><summary>Solution</summary>  
`NonZero`  
</details>  

41. `print(not '' and 'Valid' or 'Invalid')`  
<details><summary>Solution</summary>  
`Valid`  
</details>  

42. `print(not 0 or 'Zero' and 'NonZero')`  
<details><summary>Solution</summary>  
`NonZero`  
</details>  

43. `print('A' and 'B' or 'C' and 'D')`  
<details><summary>Solution</summary>  
`B`  
</details>  

44. `print(1 < 2 and 'Math' or 'Logic')`  
<details><summary>Solution</summary>  
`Math`  
</details>  

45. `print(5 + 3 and 0 * 10)`  
<details><summary>Solution</summary>  
`0`  
</details>  

46. `print(0 in [0] or 'Not Found')`  
<details><summary>Solution</summary>  
`True`  
</details>  

47. `print(len('') and 'Empty' or 'NonEmpty')`  
<details><summary>Solution</summary>  
`Empty`  
</details>  

48. `print(3.14 and '' or 'Pi')`  
<details><summary>Solution</summary>  
`Pi`  
</details>  

49. `print(True and not False or 'Confusion')`  
<details><summary>Solution</summary>  
`True`  
</details>  

50. `print((lambda: 'Func')() or 'Default')`  
<details><summary>Solution</summary>  
`Func`  
</details>  