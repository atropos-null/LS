# PEDAC Process: A Structured Approach to Programming Problems

This document outlines the PEDAC process, a structured method for solving programming problems. PEDAC's primary goal is to encourage programmers to code with intent and avoid common pitfalls that arise from jumping directly into coding without proper planning. This summary focuses on a "lighter" version of PEDAC, particularly relevant for interview assessments, with an emphasis on understanding the problem, designing data structures, and crafting algorithms.

---

## Key Themes and Concepts

### Coding with Intent

**Core Principle:** Move beyond writing code impulsively; solve problems with a deliberate plan. PEDAC's "primary goal is to help you identify and avoid pitfalls that you may encounter when you don't code with intent."

### Structure for Problem Solving: What is PEDAC?
PEDAC provides a clear, step-by-step framework:
* **P:** Understand the Problem
* **E:** Examples / Test Cases (briefly discussed in this version)
* **D:** Data Structure
* **A:** Algorithm
* **C:** Code (briefly discussed in this version)

### Saving Time and Efficiency

Investing time in planning (especially for complex problems) "saves time and lets you solve complex problems efficiently." Simple problems may not require the full PEDAC process, but more involved ones (e.g., finding palindromic substrings) benefit greatly from this method.

***

## Detailed Steps

### 1. Understanding the Problem (P)
* **Actions:**
  - Read the problem description.
  - Check provided test cases.
  - Clarify unclear aspects by asking questions.

**Importance:** Failing to fully understand the problem can result in "losing 10–15 minutes struggling with the wrong problem."

### 2. Identifying Explicit and Implicit Requirements
* **Explicit Requirements:** Clearly stated in the problem description.
* **Implicit Requirements:** Inferred from examples or the absence of information (e.g., handling empty strings).
* Test cases are valuable for surfacing implicit requirements.

### 3. Data Structure (D) and Algorithm (A) are Paired
* "Data structures influence your algorithm"—these steps are closely related.
* Choosing a data structure is often straightforward; designing a detailed algorithm is generally more challenging.

### 4. Detail in Algorithms
* Avoid high-level algorithms that overlook the "hard" parts.
    - Example: Finding palindromic substrings requires breaking down the process of generating all substrings.
* Use helper functions (e.g., `substrings`, `is_palindrome`) for complex problems.

### 5. Using Concrete Examples to Develop Algorithms
* Simplify the problem with a small, concrete example to identify patterns and steps.

### 6. From Informal to Formal Pseudocode (Optional)
* **Informal Pseudocode:** Descriptive language.
* **Formal Pseudocode:** Structured, closer to actual code. Sometimes helpful as an intermediate step.

### 7. Verifying Assumptions
* Always verify assumptions by reviewing test cases or asking clarifying questions.
* Incorrect assumptions about inputs, outputs, or requirements can waste time and lead to incorrect solutions.

***

## Additional Notes and Examples

| Objective | Step | Description|
| :--- | :---  | :-----      |
| Process the Problem | Understand the Problem | <ul><li>Identify expected input and output</li><li>Make the requirements explicit</li><li>Identify rules</li><li>Mental model of the problem (optional)</li></ul> |
| | Examples/Test Case | Validate understanding of the problem |
| | Data Structure | How we represent data that we will work with when converting the input to output. |
| | Algorithm | Steps for converting input to output |
| Code with Intent | Code | Implementation of Algorithm |


***

### Example Problem 1: `change_me` Function

```python

"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.
"""

change_me("We will meet at noon")           # "We will meet at NOON"
change_me("No palindromes here")            # "No palindromes here"
change_me("")                               # ""
change_me("I LOVE mom and dad equally")     # "I LOVE MOM and DAD equally"
```

<details>
<summary>Solution</summary>
Answer:

```
input: string
output: string (not the same object)
rules:
  Explicit requirements:
    - Every palindrome in the string must be converted to uppercase.
      (Reminder: a palindrome is a word that reads the same forwards
      and backward).
    - Palindromes are case sensitive. ("dad" is a palindrome, but "Dad" is not.)

  Implicit requirements:
    - If the string is an empty string, the result is an empty string.
```
</details>


### Example Problem 2: `palindrome_substrings` Function

```python
"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

palindrome_substrings("abcddcbA")                   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome")                 # []
palindrome_substrings("")                           # []
palindrome_substrings("repaper")                    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]
```

<details>
<summary>Solution</summary>
Answer:

Some questions you might have?
1. What is a substring?
2. What is a palindrome?
3. Will inputs always be strings?
4. What does it mean to treat palindrome words case-sensitively?

input: string
output: a list of substrings
rules:
  Explicit requirements:
    * Return only substrings which are palindromes.
    * Palindrome words should be case sensitive; "abBA" is not a
      palindrome.

  Implicit requirements:
    * If the string is an empty string, the result should be an
      empty list.

Algorithm:

* Create an empty list, `result`, for the required substrings.
* Initialize a `start_index` variable to 0 for the first character of
  the substring.
* Iterate over the string from `start_index` to length of string - 2.
    * Initialize a `num_chars` variable to `2` for the initial
      substring length.
    * Iterate from `num_chars` to length of string - `start_index`:
        * Extract substring of length `num_chars` from `string`
          starting at `start_index`.
        * Append the extracted substring to `result`.
        * Increment `num_chars` by `1`.
    * End of inner loop.
    * Increment `start_index` by `1`.
* End of outer loop.
* Return the `result` list.

</details>

***

### Concrete Example for Substring Generation

Given `"halo"`, the substrings of length 2 or more are:
```
['ha', 'hal', 'halo', 'al', 'alo', 'lo']
```

***

### Might need this later: Python String Slicing for Reversal

- To reverse a string: `string[::-1]` (e.g., used in `is_palindrome` function).

***

## Notes from Ewa

**Problem** 
* reread, rewrite in my own words
* what gets printed/returned

**Examples**
* analyze ALL!

**Data Structure**
* what goes in / what comes out


## Conclusion

The PEDAC process provides a valuable introduction to structured problem-solving. It emphasizes the importance of understanding the problem and designing detailed algorithms before coding. Using concrete examples and breaking down complex tasks into smaller parts are key strategies. While this summary focuses on the "P," "D," and "A" steps, it lays a solid foundation for approaching programming challenges efficiently, especially in time-constrained situations like interviews.

Page References: [Introduction to the PEDAC Process](https://launchschool.com/lessons/1b66cd61/assignments/44ff1dd2)