# Lesson 1A Quiz: Sets Basics

Step 10.6 · Discrete math: sets & functions

- First attempt: 9/10
- Corrected: Q3(b) and Q5(b)

Questions where my first attempt was wrong show the first attempt and the corrected answer.

---

## Q1. Let B = {0, {1}, {1, 2}, {}}. Answer true or false, with a one-line reason for each.

(a) 1 in B
no cause 1 is inside of another box {1} like this

(b) {1} in B
yes cuase {1} is inside of the first box

(c) {} in B
yes this is an empty list which is inside of B

(d) 2 in B
no cause 2 is inside of another set of B set with 1 like {1, 2}

---

## Q2. Write in roster form.

(a) {x in Z | -3 < x <= 2}
= {-2, -1, 0, 1, 2}

(b) {x in N | x is odd and x < 10}
= {1, 3, 5, 7, 9}

---

## Q3. Write in set-builder form (either shape). Then add a "check:" line listing what your set-builder produces.

(a) {5, 10, 15, 20}

filter form: {x in Z | x = 5k where k is integer and 5 <= x <= 20}

```
check:
k = 0 -> x = 5*0 = 0 is not set element cause not in the range 5 <= x <= 20
k = 1 -> x = 5*1 = 5 is set element cause it is in the range
k = 2 -> x = 5*2 = 10 is set element cause it is in the range
k = 3 -> x = 5*3 = 15 is set element cause it is in the range
k = 4 -> x = 5*4 = 20 is set element cause it is in the range
k = 5 -> x = 5*5 = 25 is not set element cause not in the range
so for k = {1, 2, 3, 4} x = {5, 10, 15, 20}
```

(b) {..., -3, -1, 1, 3, 5, ...}

### First attempt

build form: {x is odd | x in Z}

### Corrected

build form: {2k + 1 | k in Z}

```
check:
...
x = -4 is not odd so not the set element
x = -3 is odd so is the set element
x = -2 is not odd so not the set element
x = -1 is odd so is the set element
x = 0 is not odd so not the set element
x = 1 is odd so is the set element
x = 2 is not odd so not the set element
x = 3 is odd so is the set element
x = 4 is not odd so not the set element
x = 5 is odd so is the set element
...
```

---

## Q4. Find each cardinality.

(a) |{2, 2, 2, 5}| = 2

(b) |{{}, {{}}}| = 2

(c) |{x in Z | x^2 = 9}| = 2

(d) |{1, {1}, {1, {1}}}| = 3

---

## Q5.

### (a) Is {4, 5, 6} = {6, 5, 4, 4}? Answer yes or no, then explain why.

yes cause we have same element 4, 5, 6 for both set although with one repetition.

### (b) Let O = {x in Z | x = 2k+1 for some integer k}. Decide whether 15 in O and whether -4 in O. Justify each line by line, with a reason on every line.

#### First attempt

```
15 in O?
- 15 is an integer [given]
- 2(7) + 1 [arithmetic]
- 7 is an integer so k = 7 works [definition of O]
- so 15 is in O

-4 in O?
- -4 is an integer [given]
- 2(-2) [arithmetic]
- -2 is an integer so -4 is even [definition of even]
- so -4 is not odd and not in O
```

#### Corrected

```
15 in O?
- 15 is an integer [given]
- 15 = 2(7) + 1 [arithmetic]
- 7 is an integer so k = 7 works [definition of O]
- so 15 is in O

-4 in O?
- -4 is an integer [given]
- -4 = 2(-2) [arithmetic]
- -2 is an integer so -4 is even [definition of even]
- no integer is both even and odd [fact from 10.5]
- so -4 is not odd and not in O
```
