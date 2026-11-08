# Day 45: Display All Prime Numbers from 1 to N

## 🎯 Problem Statement

Write a Python program to read a number `n` and display all prime numbers between 1 and `n`.

### 🧪 Example

**Input:**
```text
Enter a number: 20
```

**Output:**
```text
Prime numbers between 1 and 20:
2 3 5 7 11 13 17 19
```

### 💡 Approach

The problem combines loops, conditional statements, and prime-number checking.

1. Read the upper limit `n` from the user.
2. Use an outer loop to iterate through every number from 2 to `n`.
3. For each number, assume it is prime initially.
4. Use an inner loop to check whether it is divisible by any number from 2 up to that number minus 1.
5. If a divisor is found, mark the number as not prime.
6. If no divisor is found, display the number.
7. Repeat until all numbers up to `n` have been checked.

### 🧠 Concepts Practiced

- Nested loops
- Prime number identification
- Conditional statements (`if-else`)
- Modulo operator (`%`)
- Boolean flags
- Divisibility and factors
- Basic algorithmic problem-solving

### 📂 File

`Q45.py`

### 📈 Progress

**45 / 100 Questions Completed**

55 questions remaining.

> Learning to solve one problem is good. Learning to apply that logic repeatedly is how problem-solving skills develop. 🚀
