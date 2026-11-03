# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 40: Count Even and Odd Digits in a Number

### 📝 Problem Statement
Write a program to count the number of even digits and odd digits in a number `n`.

### 🎯 Objective
Use loops, modulus, integer division, and conditional statements to extract digits and count how many are even and odd.

### 💡 Example

**Input:**
```text
Enter any number: 123456
```

**Output:**
```text
Total number of even digits: 3
Total number of odd digits: 3
```

### 📖 Explanation

The number `123456` contains six digits:

- Even digits: `2`, `4`, `6`
- Odd digits: `1`, `3`, `5`

Therefore:
- Total even digits = 3
- Total odd digits = 3

The program repeatedly extracts the last digit using the modulus operator (`% 10`) and checks whether it is divisible by 2.

If the digit is divisible by 2, the even counter is increased. Otherwise, the odd counter is increased.

The last digit is removed using integer division (`// 10`). This process continues until all digits have been checked.

### 🧠 Logic
1. Take an integer `n` as input.
2. Use `abs()` to handle negative numbers.
3. Store the number in a working variable `bc`.
4. Initialize `count1 = 0` for even digits.
5. Initialize `count2 = 0` for odd digits.
6. Use a `while` loop that runs while `bc > 0`.
7. Extract the last digit using `bc % 10`.
8. Remove the last digit using `bc = bc // 10`.
9. Check whether `digit % 2 == 0`.
10. If true, increase the even counter by 1.
11. Otherwise, increase the odd counter by 1.
12. Repeat until `bc` becomes `0`.
13. Handle the special case where `n` is `0`, since zero is an even digit.
14. Display both final counts outside the loop.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements using `if`
- Modulus operator (`%`)
- Integer division (`//`)
- Working variables
- Digit extraction
- Increment operators (`+=`)
- Counting and classification
- Checking even and odd numbers
- Handling negative numbers using `abs()`
- Handling special cases

### 📂 File
`Q40.py`

### 🚀 Challenge Progress
- **Completed:** 40/100 questions
- **Remaining:** 60 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**
