# IS211 – Assignment 14  
### Recursion

This project implements three recursive algorithms in Python as required by the IS211 Assignment 14 instructions.

---

## 📘 Overview

The assignment focuses on using recursion to solve three classic problems:

1. **Fibonacci Sequence (`fibonnaci`)**  
   Returns the *n-th* number in the Fibonacci sequence using pure recursion.

2. **Euclid’s GCD Algorithm (`gcd`)**  
   Computes the greatest common divisor of two integers using the recursive Euclidean algorithm.

3. **String Comparison (`compareTo`)**  
   Recursively compares two strings lexicographically.  
   The function returns:  
   - Negative number → `s1 < s2`  
   - `0` → `s1 == s2`  
   - Positive number → `s1 > s2`

All functions are located in **recursion.py**.

---
# PART I — Fibonacci Sequence  
### Function: `fibonnaci(n)`

**Goal:**  
Implement a recursive function that returns the *n-th* Fibonacci number, where:

- F(0) = 0  
- F(1) = 1  
- F(n) = F(n−1) + F(n−2)

**Implementation:**  
The function uses pure recursion with base cases for 0 and 1.  
Negative inputs raise a `ValueError`.

**Location:**  
`recursion.py`

**Example:**
```
fibonnaci(7)     # 13
fibonnaci(10)    # 55
```
# PART II — Euclid’s GCD Algorithm  
### Function: `gcd(a, b)`

**Goal:**  
Implement the recursive form of Euclid’s Algorithm to compute the *greatest common divisor (GCD)* of two integers, where:

- If `b == 0` → return `a`  
- Otherwise → `gcd(a, b) = gcd(b, a % b)`  

**Implementation:**  
The function applies Euclid’s reduction rule recursively until the remainder becomes zero, at which point the GCD is found.

**Location:**  
`recursion.py`

**Example:**
```
gcd(100, 75)     # 25
gcd(270, 192)    # 6
```
# PART III — String Comparison (Recursive)  
### Function: `compareTo(s1, s2)`

**Goal:**  
Write a recursive function that compares two strings *lexicographically*. The function must return:

- Negative number → `s1 < s2`  
- `0` → `s1 == s2`  
- Positive number → `s1 > s2`  

**Implementation:**  
The function compares the first character of both strings.  
- If the characters differ, it returns the ASCII difference.  
- If the characters match, the function recursively compares the remaining substring.  
- Includes edge-case handling when one or both strings are empty.

**Location:**  
`recursion.py`

**Example:**
```
compareTo("abc", "abc")     # 0
compareTo("abc", "abd")     # negative number
compareTo("z", "a")         # positive number
compareTo("", "abc")        # negative number
compareTo("abc", "")        # positive number
```
# PART IV — Testing the Recursive Functions  
### File: `test_recursion.py`

**Goal:**  
Ensure that all recursive functions work correctly by validating their outputs using Python’s built-in `unittest` framework.

**Implementation:**  
A dedicated test file (`test_recursion.py`) was created to verify:

- **Fibonacci (`fibonnaci`)**
  - Base cases (0 and 1)
  - Recursive growth for larger values
  - Error handling for invalid (negative) input

- **Euclid’s GCD (`gcd`)**
  - Simple GCD cases (e.g., gcd(10, 5))
  - Mixed and more complex pairs  
  - Proper recursive reduction to remainder zero

- **String Comparison (`compareTo`)**
  - Equal strings  
  - Lexicographical ordering (less than / greater than)
  - Empty-string edge cases

Run the full test suite using:

```
python -m unittest -v o python -m unittest -v test_recursion.py
```
<img width="724" height="199" alt="image" src="https://github.com/user-attachments/assets/3514bf96-06cd-451c-87d8-d16a51897630" />

# How to Run the Program

Follow these steps to run the recursive functions and the test suite.

---

## 1. Activate the Virtual Environment

If you created a virtual environment (`venv/`):

```
source venv/bin/activate
```
## 2. Run the Program Interactively

Open the Python interpreter:

```
python
```
<img width="767" height="58" alt="image" src="https://github.com/user-attachments/assets/050d6a05-4c56-4893-a0b2-0e53091579db" />

Import the recursive functions:
```
from recursion import fibonnaci, gcd, compareTo
```
<img width="766" height="78" alt="image" src="https://github.com/user-attachments/assets/474c57b3-d639-4ccd-8e32-957e1db41bf4" />

## Test Function 1: Fibonacci (fibonnaci)
Run these:
```
fibonnaci(0)
fibonnaci(1)
fibonnaci(5)
fibonnaci(7)
fibonnaci(10)
fibonnaci(15)
```
<img width="862" height="240" alt="image" src="https://github.com/user-attachments/assets/ffef9cc4-d311-4934-bd52-83dc16f207ab" />

## Test Function 2: GCD (gcd)
Run:
```
gcd(10, 5)      # 5
gcd(20, 8)      # 4
gcd(100, 75)    # 25
gcd(270, 192)   # 6
```
<img width="201" height="153" alt="image" src="https://github.com/user-attachments/assets/8501e819-9bc4-4fbb-a2f1-f1ca656d5d3b" />

## Test Function 3: compareTo (compareTo)
Run: 
```
compareTo("abc", "abc")     # 0
compareTo("abc", "abd")     # negative number
compareTo("b", "a")         # positive number
compareTo("apple", "banana") # negative
compareTo("zebra", "yak")    # positive
compareTo("", "abc")        # negative
compareTo("abc", "")        # positive
```
Expected behavior:

- 0 → equal

- Negative → first string is smaller

- Positive → first string is greater

## How the `compareTo` Function Works

The `compareTo` function compares two strings **one character at a time**, recursively, to determine their lexicographical (alphabetical) order.

---

## ✔ Character-by-Character Comparison

The function examines the first character of each string:

```
s1[0]   and   s2[0]
```
It converts these characters to their ASCII values:
```
ord(s1[0]) - ord(s2[0])
```
ASCII Examples:
- 'a' = 97
- 'b' = 98
- 'c' = 99

Example: "abc" vs "abd"

Compare:
- 'c' → 99
- 'd' → 100
```
99 - 100 = -1
```
A negative result means:
```
"abc" < "abd"
```
## Base Case #1 — Both Strings Are Empty
```
if s1 == "" and s2 == "":
    return 0
```
Two empty strings are equal → return 0.

## Base Case #2 — One String Is Empty
```
if s1 == "":
    return -1    # empty string is smaller
if s2 == "":
    return 1     # non-empty string is larger
```
Examples:
- compareTo("", "abc") → -1
- compareTo("abc", "") → 1

This follows lexicographic rules:
If all previous characters matched, the shorter string is considered smaller.

## Recursive Case — First Characters Match

If the first characters are equal:
```
return compareTo(s1[1:], s2[1:])
```

This means:

- Remove the first character from both strings
- Compare the rest recursively

Example: compareTo("apple", "apply")
- 'a' == 'a' → compare "pple" vs "pply"
- 'p' == 'p' → compare "ple" vs "ply"
- 'p' == 'p' → compare "le" vs "ly"
- 'l' == 'l' → compare "e" vs "y"
- 'e' < 'y' → return a negative number

## When Characters Differ

If the first characters do not match:
```
return ord(s1[0]) - ord(s2[0])
```
Example 1: "b" vs "a"
- 'b' → 98
- 'a' → 97
```
98 - 97 = 1
```
Positive → "b" > "a"

Examples of actual results:
```
0
-1
1
-1
1
-1
1
```
<img width="255" height="215" alt="image" src="https://github.com/user-attachments/assets/b2612d6f-4d0d-48be-bdf1-580ecc941b85" />

## Step 4 — Exit Python
```
exit()
```

