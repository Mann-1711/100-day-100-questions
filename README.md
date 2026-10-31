# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 37: Reverse a Number

### 📝 Problem Statement
Write a program to reverse a number `n`.

### 🎯 Objective
Use loops, modulus, integer division, and a running result to reverse the digits of a number.

### 💡 Example

**Input:**
```text
Enter any number: 1234
```

**Output:**
```text
Reversed number: 4321
```

### 📖 Explanation

The number `1234` contains four digits. Reversing their order gives `4321`.

The program repeatedly extracts the last digit using the modulus operator (`% 10`), adds it to the reversed number after shifting the existing result one decimal place using multiplication by `10`, and removes the last digit using integer division (`// 10`).

This process continues until all digits have been extracted.

### 🧠 Logic
1. Take an integer `n` as input.
2. Initialize `rev = 0` to store the reversed number.
3. Store the original number in a working variable `bc`.
4. Handle the special case where `n` is `0`.
5. Use a `while` loop that runs while `bc > 0`.
6. Extract the last digit using `bc % 10`.
7. Shift the current reversed number one decimal place to the left using `rev = rev * 10`.
8. Add the extracted digit to `rev`.
9. Remove the last digit using `bc = bc // 10`.
10. Repeat until `bc` becomes `0`.
11. Display the reversed number.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements using `if` and `else`
- Modulus operator (`%`)
- Integer division (`//`)
- Running results and accumulation
- Working variables
- Digit extraction
- Number manipulation

### 📂 File
`Q37.py`

### 🚀 Challenge Progress
- **Completed:** 37/100 questions
- **Remaining:** 63 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**
