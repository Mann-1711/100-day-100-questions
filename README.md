# Day 44: Check Whether a Number Is Prime or Not

## 🎯 Problem Statement

Write a Python program to read a number and check whether it is prime or not.

### 🧪 Example

**Input:**
```text
Enter a number: 7
```

**Output:**
```text
7 is a prime number.
```

**Another Example:**
```text
Enter a number: 10
```

**Output:**
```text
10 is not a prime number.
```

### 💡 Approach

A prime number is a natural number greater than 1 that has exactly two factors: 1 and itself.

1. Read a number from the user.
2. Check whether the number is less than or equal to 1. Such numbers are not prime.
3. Use a loop to check whether any number from 2 up to the number minus 1 divides it completely.
4. Use the modulo operator (`%`) to check for a remainder of zero.
5. If a divisor is found, the number is not prime.
6. If no divisor is found, the number is prime.

### 🧠 Concepts Practiced

- Conditional statements (`if-else`)
- `for` or `while` loops
- Modulo operator (`%`)
- Divisibility and factors
- Boolean flags
- Basic number theory
- Algorithmic problem-solving

### 📂 File

`Q44.py`

### 📈 Progress

**44 / 100 Questions Completed**

56 questions remaining.

> Every problem strengthens the ability to turn mathematical logic into working code. Keep building! 🚀
