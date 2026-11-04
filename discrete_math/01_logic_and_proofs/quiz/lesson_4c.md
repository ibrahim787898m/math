# Lesson 4C Quiz: Induction

Step 10.5 · Discrete math: logic & proofs

- First attempt: 9.75/10

Rules: use the template; show the base case calculation for both sides; write the goal in full; mark where you use the IH; the conclusion is about n, not k.

---

## Q1. Let P(n): 2 + 4 + 6 + … + 2n = n(n + 1).

### (a) Check P(1), P(2) and P(3) with both sides.

```
p(1)
left side: 2
right side: 1(1 + 1) = 2
true
p(2)
left side: 2 + 4 = 6
right side: 2(2 + 1) = 6
true
p(3)
left side: 2 + 4 + 6 = 12
right side: 3(3 + 1) = 12
true
```

### (b) Write P(k) and P(k + 1) in full.

```
p(k) = 2 + 4 + 6 + ... + 2k = k(k + 1)
p(k + 1) = 2 + 4 + 6 + ... + 2k + 2(k + 1) = (k + 1)(k + 1 + 1)
p(k + 1) = 2 + 4 + 6 + ... + 2k + 2k + 2 = (k + 1)(k + 2)
```

---

## Q2. Prove Q1’s claim by induction for all n ≥ 1.

```
claim: forall n >= 1, 2 + 4 + 6 + … + 2n = n(n + 1).

Base case (n = 1):
- left side = 2 [substitution]
- right side = 1(1 + 1) = 2 [substitution, algebra]
- left = right so p(1) is true [equality]

inductive steps:
- Let k >= 1 be arbitrary. [assumption]
- assume: 2 + 4 + 6 + ... + 2k = k(k + 1) [IH]
- goal: 2 + 4 + 6 + ... + 2k + 2(k + 1) = (k + 1)(k + 2) [inductive goal]
- k(k + 1) + 2(k + 1) [IH]
- (k + 1)(k + 2) [factoring]

so, p(k + 1) is true [inductive step]

conclusion: by mathematical induction, 2 + 4 + 6 + … + 2n = n(n + 1) is true for all n >= 1 [principle of mathematical induction]
```

---

## Q3. Prove by induction: for all n ≥ 0, 1 + 2 + 4 + … + 2ⁿ = 2ⁿ⁺¹ − 1.

```
claim: forall n >= 0, 1 + 2 + 4 + … + 2ⁿ = 2ⁿ⁺¹ − 1.

base case n = 0:
- left side = 1 [substitution]
- right side = 2^(0+1) - 1 = 2 - 1 = 1 [substitution, algebra]
- left = right so p(0) is true [equality]

inductive steps:
- let k >= 0 be arbitrary, [assumption]
- assume: 1 + 2 + 4 + … + 2^k = 2^(k + 1) − 1. [IH]
- goal: 1 + 2 + 4 + … + + 2^k + 2^(k + 1) = 2^((k + 1) + 1) − 1. [inductive goal]
- 1 + 2 + 4 + … + + 2^k + 2^(k + 1)
- 2^(k + 1) - 1 + 2^(k + 1) [IH]
- 2^(k + 2) - 1 [algebra, exponent rule]
- 2^((k + 1) + 1) - 1 [algebra]

so p(k + 1) is true [inductive step]

conclusion: by mathematical induction, 1 + 2 + 4 + … + + 2^n = 2^(n + 1) - 1 for all integers n >= 0 [principle of mathematical induction]
```

---

## Q4. Prove by induction: for all n ≥ 0, 5 | (6ⁿ − 1).

```
claim: forall n >= 0, 5 | (6^n - 1)

base case n = 0 :
- 6^0 - 1 = 1 - 1 = 0 [substitution, algebra]
- 0 = 5 * 0 [calculation]
- so, 5 | 0 [definiiton of divides]
- so p(0) is true [base case]

inductive steps:
- let k >= 0 be arbitrary [assumption]
- assume: 5 | (6^k - 1) [IH]
- so, 6^k - 1 = 5m, where m is an integer [definiiton of divides]
- goal: 5 | (6^(k+1) - 1) [inductive goal]
- 6^(k+1) - 1
- 6.6^k - 1 [exponent rule]
- 6(5m + 1) - 1 [IH]
- 30m + 6 - 1 [algebra]
- 30m + 5 = 5(6m + 1) [algebra, factoring]
- 6m + 1 is an integer [closure under multiplication and addition]
- so 5 | (6^(k+1) - 1) [definiiton of divides]

so p(k + 1) is true [inductive step]

conclusion: by mathematical induction, 5 | (6^n - 1) for all integers n >= 0 [principle of mathematical induction]
```

---

## Q5.

### (a) A friend “proves” that n² + n is odd for all n ≥ 1: “Assume k² + k is odd. Then (k + 1)² + (k + 1) = (k² + k) + 2(k + 1), which is odd + even, so it’s odd. Done.” Find the flaw, and show that the claim is actually false.

The proof is missing the base case. P(1) is false because \(1^2+1=2\), which is even, not odd. Therefore, the original claim is false.

```
friend's claim: n² + n is odd for all n ≥ 1
argument:
- Assume k² + k is odd [assumption]
- (k + 1)² + (k + 1) = (k² + k) + 2(k + 1) [algebra]
- odd + even = odd [definiiton of odd]
so it is odd

now flaw:
base case n = 1:
- 1^2 + 1 = 2 which is even [definiiton of even]
2 is even not odd so the original claim is false.
```

### (b) Look at this function. Explain which part is the base case, and where the code relies on the inductive hypothesis to be sure that power2(n) == 2**n.

```python
def power2(n):
    if n == 0:
        return 1
    return 2 * power2(n - 1)
```

base case is if n == 0 it will immediately return 1 cause 2^0 = 1

the recursive line 2 * power2(n-1) relies on the inductive hypothesis cause for example to get power2(3) it calculates 2 * power2(2) that mean the anser of the power2(2) matters which is IH.
