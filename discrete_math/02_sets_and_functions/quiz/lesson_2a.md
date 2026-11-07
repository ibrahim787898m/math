# Lesson 2A Quiz: Set Operations

Step 10.6 · Discrete math: sets & functions

- First attempt: 9/10
- Corrected: Q4 and Q5(a)

Questions where my first attempt was wrong show the first attempt and the corrected answer.

U = {1, 2, ..., 10}, A = {1, 2, 3, 4, 5}, B = {4, 5, 6, 7}, C = {2, 4, 6, 8, 10}.

---

## Q1. Find each set.

(a) A union B = {1, 2, 3, 4, 5, 6, 7}

(b) A inter C = {2, 4}

(c) B - A = {6, 7}

(d) A' = U - A = {6, 7, 8, 9, 10}

---

## Q2. Compute step by step. Write one line per operation, and name each operation.

(a) (A union B)'

```
A union B = {1, 2, 3, 4, 5, 6, 7} [union: in A or in B]
(A union B)' = U - (A union B) = {8, 9, 10} [complement of A union B]
```

(b) (A - C) inter B

```
A - C = {1, 3, 5} [difference: remove 2, 4]
(A - C) inter B = {5} [intersection: in (A - c) and in B]
```

---

## Q3.

### (a) Compute (A inter B)' and A' union B'. Are they equal? Then write one sentence connecting this to a logic law from 10.5.

```
(A inter B)'
(A inter B) = {4, 5} [intersection: in A and in B]
(A inter B)' = {1, 2, 3, 6, 7, 8, 9, 10} [complement of A inter B]

A' union B'
A' = {6, 7, 8, 9, 10} [complement of A]
B' = {1, 2, 3, 8, 9, 10} [compelement of B]
A' union B' = {1, 2, 3, 6, 7, 8, 9, 10} [union: in A' or in B']
```

conclusion: both result is same so (A inter B)' and (A' union B') are equal which is same as de morgans law not (A and B) == not A or not B

### (b) Is A - B = B - A? Compute both, then answer and give a reason.

```
A - B = {1, 2, 3} [difference: remove 4, 5]
B - A = {6, 7} [difference: remove 4, 5]
```

conclusion: both are not same cause the elements of both result sets are different.

---

## Q4.

### (a) Check inclusion-exclusion with A and B: compute both sides and compare.

#### First attempt

```
|A inter B| = |A| + |B| - |A union B| [inclusion exclusion]
            = 5 + 4 - 7 = 2 [substruction]

A inter B = {4, 5} = |{4, 5}| = 2
```

conclusion: so comparing both side we can see inclusion exclusion result of |A inter B| is 2 and it is correct.

#### Corrected

```
LHS = |A union B| = |{1, 2, 3, 4, 5, 6, 7}| = 7

RHS = |A| + |B| - |A inter B| [inclusion exclusion]
= 5 + 4 - 2 = 7 [substitute]
```

conclusion: so comparing both side we can see LHS = RHS.

### (b) There are 40 students in a class. 22 like math, 15 like art, and 7 like both. How many like at least one of the two? How many like neither? Define your letters first, and show each line.

#### First attempt

```
Student likes Math = M, Student likes Art = A [define letters]

|M union A| = |M| + |N| - |M inter N| [inclusion exclusion]
            = 22 + 15 - 7 = 30 [substruction]

neither = total studens - |M union A| [inclusion exclusion]
        = 40 - 30 = 10 [substruction]
```

so, 30 students like at least on of the two and 10 studens like neither.

#### Corrected

```
Student likes Math = M, Student likes Art = A [define letters]

|M union A| = |M| + |A| - |M inter A| [inclusion exclusion]
            = 22 + 15 - 7 = 30 [substitute]

neither = total studens - |M union A| [everyone minus at least one]
        = 40 - 30 = 10 [substitute]
```

so, 30 students like at least on of the two and 10 studens like neither.

---

## Q5. Let U = Z, E = {x in Z | x = 2k for some integer k}, and T = {x in Z | x = 3m for some integer m}.

### (a) Is 9 in T - E? Show it line by line, with a reason on every line.

#### First attempt

```
9 = 3(3), where 3 is integer, so 9 in T [definition of T]
9 = 2(4) + 1, so 9 is odd [definition of odd]
no integer cant be both odd and even so 9 notin E [fact from 10.5]
9 in T and 9 notin E, so 9 in T - E [definition of difference]
```

#### Corrected

```
9 = 3(3), where 3 is integer, so 9 in T [definition of T]
9 = 2(4) + 1, so 9 is odd [definition of odd]
no integer can be both odd and even so 9 notin E [fact from 10.5]
9 in T and 9 notin E, so 9 in T - E [definition of difference]
```

### (b) Is 12 in (E union T)'? Show it line by line, with a reason on every line.

```
12 = 2(6), where 6 is integer, so 12 in E [definition of E]
12 = 3(4), where 4 is integer, so 12 in T [definition of T]
12 in both E and T, so 12 in E union T [definition of union]
12 in E union T, so 12 not in (E union T)' [definition of complement]
```
