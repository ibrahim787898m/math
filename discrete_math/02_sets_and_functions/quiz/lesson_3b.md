# Lesson 3B Quiz: Cartesian Products

Step 10.6 · Discrete math: sets & functions

- First attempt: 8/10
- Corrected: Q2(d), Q4(b) and Q5

Questions where my first attempt was wrong show the first attempt and the corrected answer.

Pairs use ( ) and sets use { }, so read the brackets before deciding if something is in A x B. In "why" answers, include the counting step, not just how the pairs are made. In proofs, check that each letter matches the line above, and name the logic law.

---

## Q1. Let A = {p, q, r} and B = {0, 1}. List A x B, one line per first entry with a reason. Then write the full set and check the count with |A| * |B|.

```
list A x B:
first = p: (p, 0), (p, 1) [first from A, second run through B]
first = q: (q, 0), (q, 1) [first from A, second run through B]
first = r: (r, 0), (r, 1) [first from A, second run through B]
A x B = {(p, 0), (p, 1), (q, 0), (q, 1), (r, 0), (r, 1)} [all pair together]
count = 2 + 2 + 2 = 6 = 3 * 2 = |A| * |B| [general rule from section 4]
```

---

## Q2. Let A = {1, 2} and B = {2, 3}. True or false, with a one-line reason each.

### (a) (2, 3) in A x B

```
true - 2 in A and 3 in B so (2, 3) in A x B
```

### (b) (3, 2) in A x B

```
false - 3 notin A so (3, 2) notin A x B
```

### (c) (2, 2) in A x B

```
true - 2 in A and 2 in B so (2, 2) in A x B
```

### (d) {1, 2} in A x B

#### First attempt

```
true - 1 in A and 2 in B so (1, 2) in A x B
```

#### Corrected

```
false - this is a set it cant be inside of cartesian, A x B makes ordered pairs like (1, 2) not set {1, 2}
```

---

## Q3.

### (a) With A = {1, 2} and B = {2, 3}, show A x B != B x A with a counterexample. Name one pair, line by line.

```
counterexample:
- let A = {1, 2} and B = {2, 3} [choose sets]
- 1 in A, 3 in B [listed]
- so (1, 3) in A x B [definition of cartesian product]
- 1 notin B [not listed]
- so (1, 3) notin B x A [definition of cartesian product]
- so A x B != B x A in general [one counterexample is enough]
```

### (b) Is (1, 2) = (2, 1)? Is {1, 2} = {2, 1}? Answer each and explain why the two answers are different.

(1, 2) != (2, 1) - cause they are ordered pairs not sets, so order of numbers matter.

{1, 2} = {2, 1} - they are sets so order of the numbers dont matter if the numbers are same sets are equal.

---

## Q4.

### (a) |A| = 4 and |B| = 5. Find |A x B|, |A x A| and |A x {}|, with a reason for each.

```
|A x B| = |A| * |B| = 4 * 5 = 20 [general rule from section 4]
|A x A| = |A| * |A| = 4 * 4 = 16 [general rule from section 4]
|A x {}| = |A| * |{}| = 4 * 0 = 0 [general rule from section 4]
```

### (b) In your own words (2-3 sentences), explain why |A x B| = |A| * |B|.

#### First attempt

to make a pair you go through the each element of A and B and mathc them together like we match all element of B with the first element of A then again do same for the second element fo A. that why it is |A| * |B| means we are matching each element of A with each element of B.

#### Corrected

to make a pair you go through the each element of A and B and mathc them together like we match all element of B with the first element of A then again do same for the second element fo A. that why it is |A| * |B| means we are matching each element of A with each element of B. so if we have 2 elements of A and 3 elements of B. first A element will make B elements number of pair and second A element will do same. so A number of elements will make B numbers of pair which is exactly |A| * |B|.

---

## Q5. Prove with an iff chain: (A union B) x C = (A x C) union (B x C). Write the claim at the top first. Name the logic law you use.

#### First attempt

```
claim: (A union B) x C = (A x C) union (B x C)
- iff chain (both direction at once)
- let (p, q) any ordered pair [assumption]
(p, q) in (A union B) x C
<-> p in (A union B) and q in C [definition of cartisian product]
<-> (p in A or p in B) and q in C [definition of union]
<-> (p in A and p in C) or (p in B and p in C) [definition of distribution]
<-> (p, q) in A x C or (p, q) in B x C [definition of cartisian product, 2 times]
<-> (p, q) in (A x C) union (B x C) [definition of union]
- Since this holds for any pair (p, q), (A union B) x C = (A x C) union (B x C) [definition of set equality]
```

#### Corrected

```
claim: (A union B) x C = (A x C) union (B x C)
- iff chain (both direction at once)
- let (p, q) any ordered pair [assumption]
(p, q) in (A union B) x C
<-> p in (A union B) and q in C [definition of cartisian product]
<-> (p in A or p in B) and q in C [definition of union]
<-> (p in A and q in C) or (p in B and q in C) [distributive law]
<-> (p, q) in A x C or (p, q) in B x C [definition of cartisian product, 2 times]
<-> (p, q) in (A x C) union (B x C) [definition of union]
- Since this holds for any pair (p, q), (A union B) x C = (A x C) union (B x C) [definition of set equality]
```
