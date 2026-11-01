# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 38: Find the Largest Digit in a Number

### 📝 Problem Statement
Write a program to find the largest digit in a number `n`.

### 🎯 Objective
Use loops, modulus, integer division, and conditional statements to extract digits and identify the largest digit in a number.

### 💡 Example

**Input:**
```text
Enter any number: 5832
```

**Output:**
```text
The largest digit in the number is: 8
```

### 📖 Explanation

The number `5832` contains four digits: `5`, `8`, `3`, and `2`.

The largest among these digits is `8`.

The program repeatedly extracts the last digit using the modulus operator (`% 10`) and compares it with the current largest digit.

If the extracted digit is greater than the current largest digit, the largest value is updated.

The last digit is then removed using integer division (`// 10`). This process continues until all digits have been checked.

### 🧠 Logic
1. Take an integer `n` as input.
2. Use `abs()` to handle negative numbers.
3. Store the number in a working variable `bc`.
4. Initialize `largest = 0` to track the largest digit.
5. Use a `while` loop that runs while `bc > 0`.
6. Extract the last digit using `bc % 10`.
7. Compare the extracted digit with `largest` using an `if` statement.
8. If `digit > largest`, update `largest = digit`.
9. Remove the last digit using `bc = bc // 10`.
10. Repeat until `bc` becomes `0`.
11. Display the largest digit.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements using `if`
- Modulus operator (`%`)
- Integer division (`//`)
- Working variables
- Digit extraction
- Comparison operators (`>`)
- Finding maximum values
- Handling negative numbers using `abs()`

### 📂 File
`Q38.py`

### 🚀 Challenge Progress
- **Completed:** 38/100 questions
- **Remaining:** 62 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**
