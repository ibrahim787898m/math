# Lesson 1B Quiz: Subsets

Step 10.6 · Discrete math: sets & functions

- First attempt: 8.25/10
- Corrected: Q3, Q4 and Q5

Questions where my first attempt was wrong show the first attempt and the corrected answer.

---

## Q1. Let A = {1, {2}, {1, 2}}. Answer true or false, with a one-line reason for each.

(a) {2} in A
true cause {2} is listed

(b) {2} subset A
false cause 2 sits inside of a box in set A

(c) {1} subset A
true cause 1 is listed in A

(d) {{2}} subset A
true cause {2} is in set A

---

## Q2. Answer true or false, with a one-line reason for each.

(a) {} subset {5}
true cause empty set is the subset of all sets

(b) {} in {5}
false cause empty set is not listed

(c) {3, 4} psubset {3, 4}
false cause both sets are equal

(d) {x in Z | 0 < x < 4} psubset {1, 2, 3, 4}
true {1, 2, 3} is subset and psubset cause is not equal to {1, 2, 3, 4}

---

## Q3.

### (a) Write A subset B using forall and ->. Then write its negation, pushing the not all the way in, with a reason on each line.

#### First attempt

```
forall x {x in A -> x in B}
- not forall x (x in A -> x in B)
- exists x not (x in A -> x in B) [negation of forall]
- exists x (x in A and x in B) [negation of ->]
```

#### Corrected

```
forall x (x in A -> x in B)
- not forall x (x in A -> x in B)
- exists x not (x in A -> x in B) [negation of forall]
- exists x (x in A and x notin B) [negation of ->]
```

### (b) Use your negation from (a) to show that {1, 2, 3} is not a subset of {1, 3, 5}, line by line.

#### First attempt

so using the negation from a we need to find an element which is in {1, 2, 3}, not in {1, 3, 5}

```
- 2 is in {1, 2, 3} [listed]
- 2 is not in {1, 3, 5} [not listed]
- so {1, 2, 3} is not a subset of {1, 3, 5}
```

#### Corrected

so using the negation from a we need to find an element which is in {1, 2, 3}, not in {1, 3, 5}

```
- 2 is in {1, 2, 3} [listed]
- 2 is not in {1, 3, 5} [not listed]
- so {1, 2, 3} is not a subset of {1, 3, 5} [definition of subset]
```

---

## Q4. Let A = {x in Z | x = 6k for some integer k} and B = {x in Z | x = 3m for some integer m}.

### (a) Prove A subset B by element-chasing.

#### First attempt

```
- let x is an element of A [assumption]
- x = 6k where k is integer [definition of A]
- x = 3(2k) [arithmetic]
- 2k is an integer [closure under multiplication]
- so x = 3m where m = 2k which is integer [line 3 and 4]
- x is in B [definition of B]
- as x is the element of A, A is the subset of B. [definition of subset ]
```

#### Corrected

```
- direct proof [element chasing]
- let x is an element of A [assumption]
- x = 6k where k is integer [definition of A]
- x = 3(2k) [arithmetic]
- 2k is an integer [closure under multiplication]
- so x = 3m where m = 2k which is integer [line 4 and 5]
- x is in B [definition of B]
- any x is the element of A, A is the subset of B. [definition of subset ]
```

### (b) Show B is not a subset of A with a counterexample, line by line.

#### First attempt

```
- 3 = 3(1) 1 is an integer so 3 is in B
- if 3 in A, 3 = 6k -> k = 1/2 [definition of A]
- 1/2 is not an integer, so 3 notin A [contradiction with "k is integer"]
- so x = 3 in B but notin A, so B is not subset of A [negation of subset]
```

#### Corrected

```
- 3 = 3(1) 1 is an integer so 3 is in B [definition of B]
- if 3 in A, 3 = 6k -> k = 1/2 [definition of A]
- 1/2 is not an integer, so 3 notin A [contradiction with "k is integer"]
- so x = 3 in B but notin A, so B is not subset of A [negation of subset]
```

---

## Q5. Let A = {x in Z | x = 2k for some integer k} and B = {x in Z | x = 2m + 2 for some integer m}. Prove A = B. Do both directions, then write a conclusion line.

### First attempt

```
A subset of B:
- let x is an element of A [assumption]
- x = 2k where k is integer [definition of A]
- x = 2k - 2 + 2 = 2(k - 1) + 2 [arithmetic]
- k - 1 is integer [closure under substruction]
- so x = 2m + 2 where m = k - 1 which is integer [line 3, 4]
- so x in B [definition of B]
- as x is element of A, A subset B [definition of subset]

B subset of A:
- let y is an element of B [assumption]
- y = 2m + 2 where m is integer [definition of B]
- y = 2(m + 1) [arithmetic]
- m + 1 is integer [closure under addition]
- so x = 2k where k = m + 1 which is integer [line 3, 4]
- so x in A [definition of A]
- as x is element of B, B subset A [definition of subset]

conclusion: A subset B, B subset of A, so A = B [definition of set equality]
```

### Corrected

```
A subset of B:
- direct proof [element chasing]
- let x is an element of A [assumption]
- x = 2k where k is integer [definition of A]
- x = 2k - 2 + 2 = 2(k - 1) + 2 [arithmetic]
- k - 1 is integer [closure under substruction]
- so x = 2m + 2 where m = k - 1 which is integer [line 4, 5]
- so x in B [definition of B]
- any x is element of A, A subset B [definition of subset]

B subset of A:
- direct proof [element chasing]
- let y is an element of B [assumption]
- y = 2m + 2 where m is integer [definition of B]
- y = 2(m + 1) [arithmetic]
- m + 1 is integer [closure under addition]
- so y = 2k where k = m + 1 which is integer [line 4, 5]
- so y in A [definition of A]
- any y is element of B, B subset A [definition of subset]

conclusion: A subset B, B subset of A, so A = B [definition of set equality]
```
