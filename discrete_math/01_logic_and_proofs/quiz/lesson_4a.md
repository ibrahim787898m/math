# Lesson 4A Quiz: Direct Proof

Step 10.5 · Discrete math: logic & proofs

- First attempt: 9/10
- Q5(b) corrected after review

Rules: every proof line by line with a reason on every line (including [assumption] on line 1); different letters for different numbers; include the "is an integer" line before the conclusion.

---

## Q1. Prove: if n is even, then 3n + 2 is even.

```
- let n is an even arbitrary number [assumption]
- n = 2k, where k is an integer [definition of even]
- 3n + 2 = 3(2k) + 2 [algebra]
- 3n + 2 = 6k + 2 [algebra]
- 3n + 2 = 2(3k + 1) [algebra]
- 3k + 1 is an integer [integer closed under *]
- 2 * integer is even [definition of even]
- so 3n + 2 is even [definition of even]
```

---

## Q2. Prove: if m and n are even, then m · n is even.

```
- let m and n be an arbitrary even number [assumption]
- m = 2k, where k is an integer [definition of even]
- n = 2j, where j is an integer [definition of even]
- m . n = 2k . 2j [algebra]
- m . n = 2(2kj) [algebra]
- 2kj is an integer [integer closed under *]
- 2 . integer is even [definition of even]
- so m . n is even [definition of even]
```

---

## Q3. Prove: if a | b, then a | 3b.

```
- assume a | b [assumption]
- b = a.k [definiiton of devides]
- 3b = 3ak [algebra]
- 3b = a.3k [algebra]
- here 3k is an integer [integer closed under *]
- so a | 3b [definition of devides]
```

---

## Q4. Prove: if n is odd, then n² − 1 is even.

```
- let n be an arbitrary odd number [assumption]
- n = 2k + 1, where k is an integer [definition of odd]
- n^2 - 1 = (2k + 1)^2 - 1 [algebra]
- n^2 - 1 = 4k^2 + 4k + 1 - 1 [algebra]
- n^2 - 1 = 4k^2 + 4k [algebra]
- n^2 - 1 = 4k(k + 1) [algebra]
- n^2 - 1 = 2 . 2k(k + 1) [algebra]
- here 2k(k + 1) is an integer [integer is closed under * and +]
- 2 . integer is even [definition of even]
- so n^2 - 1 is even [definition of even]
```

---

## Q5. Consider the claim "for every integer n ≥ 0, n² + n + 41 is prime".

### (a) Someone checks n = 0, 1, 2, 3 and gets 41, 43, 47 and 53. All of them are prime. Does that prove the claim? Explain in one line.

- this is a example check. he picks few numbers and this values with the expression and it showed the results are prime, does not mean all rest of the values will give the same result prime.

### (b) Find a counterexample. Hint: try n = 40 or n = 41, and show the calculation that proves the result is not prime.

#### First attempt

```
try n = 40
- 40^2 + 40 + 1
= 1641 (not a prime number)

try n = 41
- 41^2 + 40 + 1
= 1681 (not a prime number)
```

- so just checking with few example you cant prove that an expression is true.

#### Corrected

```
try n = 40
- 40^2 + 40 + 41
= 1,681 (not a prime number)
= 1 * 1681
= 41 * 41

try n = 41
- 41^2 + 41 + 41
= 1,763 (not a prime number)
= 41 * 43
```

- so just checking with few example you cant prove that an expression is true.
