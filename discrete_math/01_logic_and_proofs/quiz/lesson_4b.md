# Lesson 4B Quiz: Contrapositive and Contradiction

Step 10.5 · Discrete math: logic & proofs

- First attempt: 9/10

Rules: line 1 names the method ("Direct proof", "We prove the contrapositive: …" or "Assume, for contradiction, …"); a reason on every line; in a contradiction proof, name the lines that clash; the last line states the original claim.

---

## Q1. Take the statement “If a program passes all tests, then it has no syntax errors.”

### (a) Write its contrapositive and its converse in English.

- if a program has syntax error, then it does not passes all tests.
- if a program has no syntax error, then it passes all tests.

### (b) Which one is equivalent to the original? Give a one-line reason from Lesson 2A or 2B.

contrapositive one, i forgot the reasoning cause i took a long break after lesson 4a and did not revise the previous part.

---

## Q2. Prove by contrapositive: if 5n + 3 is even, then n is odd. The domain is the integers.

```
- We prove the contrapositive: if n is even, then 5n+3 is odd. [contrapositive]
- Let n be an arbitrary even integer. [assumption]
- n = 2k, where k is an integer [definition of even]
- 5n+3=5(2k)+3=10k+3. [substitution and algebra]
- 10k + 3 = 10k + 2 + 1 = 2(5k + 1) + 1 [algebra]
- 5k+1 is an integer. [closure of integers under multiplication and addition]
- therefore, 5n + 3 is odd [definition of odd]
- Thus, if 5n+3 is even, then n is odd. [contrapositive equivalence]
```

---

## Q3. Prove by contrapositive: if n³ is even, then n is even. The domain is the integers.

```
- contrapositive: if n is odd, then n^3 is odd. [contrapositive]
- let n be an arbitrary odd integer [assumption]
- n = 2k + 1 where k is an integer [definition of odd]
- n^3 = (2k + 1)^3 = 8k^3 + 12k² + 6k + 1 = 2(4k^3 + 6k^2 + 3k) + 1 [algebra]
- 4k^3 + 6k^2 + 3k is an integer [closure under multiplication and addition]
- n^3 is odd [definition of odd]
- so, if n^3 is even, then n is even [contrapositive equivalence]
```

---

## Q4. Prove by contradiction: there are no integers m, n with 2m + 4n = 7.

```
- assume: there exists integers m, n with 2m + 4n = 7 [assumption]
- 2m + 4n = 2(m + 2n) [algebra]
- m + 2n is integer [closure under multiplication and addition]
- 2(m + 2n) is even [definition of even]
- 7 is odd [definition of odd]
- Lines 4 and 5 contradict each other because an integer cannot be both even and odd. [contradiction]
- Therefore, there are no integers m, n with 2m+4n=7. [original claim]
```

---

## Q5. Prove by contradiction: there is no largest even integer.

```
- assume: there exists largest even integer n [assumption]
- n = 2k where k is an integer [definition of even]
- n + 2 = 2k + 2 = 2(k + 1) [substitution and algebra]
- k + 1 is an integer [closure under addtion]
- n + 2 is even [definition of even]
- but n + 2 > n [property of integers]
- line 1 and line 6 contradict each other cause we assumed n is the largest even integer but n + 2 is a largest integer [contradiction]
- so there is no largest even integer [original claim]
```
