# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 35: Sum of All Digits

### 📝 Problem Statement
Write a program to find the sum of all digits of a number `n`.

### 🎯 Objective
Use loops, modulus, integer division, and a running total to extract and add all digits of a number.

### 💡 Example

**Input:**
```text
Enter any number: 583
```

**Output:**
```text
The sum of all digits of a number n: 16
```

### 📖 Explanation

The number `583` contains three digits: `5`, `8`, and `3`.

Their sum is:

`5 + 8 + 3 = 16`

The program repeatedly extracts the last digit using the modulus operator (`% 10`), adds it to a running total, and removes the last digit using integer division (`// 10`). This process continues until no digits remain.

### 🧠 Logic
1. Take an integer `n` as input.
2. Store the number in a working variable `bc`.
3. Initialize `total = 0`.
4. Use a `while` loop that runs while `bc > 0`.
5. Extract the last digit using `bc % 10`.
6. Add the extracted digit to `total`.
7. Remove the last digit using `bc = bc // 10`.
8. Repeat until `bc` becomes `0`.
9. Display the final sum.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Modulus operator (`%`)
- Integer division (`//`)
- Running totals and accumulation
- Working variables
- Digit extraction and basic arithmetic

### 📂 File
`Q35.py`

### 🚀 Challenge Progress
- **Completed:** 35/100 questions
- **Remaining:** 65 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**
