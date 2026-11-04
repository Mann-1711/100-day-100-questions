# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 41: Check Whether a Number Is a Palindrome

### 📝 Problem Statement
Write a program to check whether a number `n` is a palindrome (reads the same reversed).

### 🎯 Objective
Use loops, modulus, integer division, and conditional statements to reverse a number and compare it with the original number.

### 💡 Example

**Input:**
```text
Enter any number: 121
```

**Output:**
```text
This number is palindrome.
```

**Another Example:**

**Input:**
```text
Enter any number: 123
```

**Output:**
```text
This number is not a palindrome.
```

### 📖 Explanation

A palindrome number reads the same forward and backward.

For example:
- `121` reversed is `121`, so it is a palindrome.
- `123` reversed is `321`, so it is not a palindrome.

The program repeatedly extracts the last digit using the modulus operator (`% 10`), builds the reversed number by multiplying the current result by 10 and adding the extracted digit, and removes the last digit using integer division (`// 10`).

After reversing the number, it compares the reversed value with the original number.

If both values are equal, the number is a palindrome. Otherwise, it is not.

### 🧠 Logic
1. Take an integer `n` as input.
2. Use `abs()` to handle negative numbers according to the program's chosen interpretation.
3. Initialize `rev = 0` to store the reversed number.
4. Store the original number in a working variable `bc`.
5. Use a `while` loop that runs while `bc > 0`.
6. Extract the last digit using `bc % 10`.
7. Shift the reversed number one decimal place using `rev = rev * 10`.
8. Add the extracted digit to `rev`.
9. Remove the last digit using `bc = bc // 10`.
10. Repeat until `bc` becomes `0`.
11. Compare `rev` with the original absolute value of `n`.
12. If both are equal, print that the number is a palindrome.
13. Otherwise, print that it is not a palindrome.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements using `if` and `else`
- Modulus operator (`%`)
- Integer division (`//`)
- Working variables
- Digit extraction
- Number reversal
- Comparison operators (`==`)
- Boolean conditions
- Reusing an algorithm to solve a new problem

### 📂 File
`Q41.py`

### 🚀 Challenge Progress
- **Completed:** 41/100 questions
- **Remaining:** 59 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**
