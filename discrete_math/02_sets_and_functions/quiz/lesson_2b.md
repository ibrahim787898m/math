# Lesson 2B Quiz: Proving Set Laws

Step 10.6 · Discrete math: sets & functions

- First attempt: 8/10
- Corrected: Q1(b), Q1(c), Q1(d), Q3 and Q5(b)

Questions where my first attempt was wrong show the first attempt and the corrected answer.

Write every proof line by line: a method line first, a reason on every line, and a final line that states the claim. Use exactly the set letters given, and a new element letter for each direction.

---

## Q1. Translate into logic, using x in and x notin with parentheses. Where there's a not in front of brackets, push it all the way in.

### (a) x in A inter B'

```
x in A inter B'
<-> x in A and x in B' [definition of intersection]
<-> x in A and not (x in B) [definition of complement]
<-> x in A and x notin B [notation]
```

### (b) x in (A union B) - C

#### First attempt

```
x in (A union B) - C
<-> x in (A union B) and x notin C [definition of difference]
<-> x in A or x in B and x notin C [definition of union]
```

#### Corrected

```
x in (A union B) - C
<-> x in (A union B) and x notin C [definition of difference]
<-> (x in A or x in B) and x notin C [definition of union]
```

### (c) x in (A' union B)'

#### First attempt

```
x in (A' union B)'
<-> not (x in (A' union B)) [definition of complement]
<-> not (x in A' or x in B) [definition of union]
<-> not (not (x in A) or x in B) [definition of complement]
<-> not (x notin A or x in B) [notation]
<-> not x notin A and not x in B [de morgans]
<-> x in A and x notin B [notation]
```

#### Corrected

```
x in (A' union B)'
<-> not (x in (A' union B)) [definition of complement]
<-> not (x in A' or x in B) [definition of union]
<-> not (not (x in A) or x in B) [definition of complement]
<-> not (x notin A or x in B) [notation]
<-> not (x notin A) and not (x in B) [de morgans]
<-> x in A and x notin B [double negation]
```

### (d) x in A union (B inter C)

#### First attempt

```
x in A union (B inter C)
<-> x in A or x in (B inter C) [definition of union]
<-> x in A or x in B and x in C [definition of intersection]
```

#### Corrected

```
x in A union (B inter C)
<-> x in A or x in (B inter C) [definition of union]
<-> x in A or (x in B and x in C) [definition of intersection]
```

---

## Q2. Prove (A inter B)' = A' union B' by element-chasing in both directions, then write a conclusion line.

part 1: (A inter B)' subset A' union B'

```
- direct proof (element-chasing)
- let x be any element of (A inter B)' [assumption]
- x notin (A inter B) [definition of complement]
- not x in (A inter B) [notation]
- not (x in A and x in B) [definition of intersection]
- x notin A or x notin B [de morgans]
- x in A' or x in B' [definition of complement]
- x in (A' union B') [definition of union]
- since x was any element of (A inter B)', (A inter B)' subset A' union B' [definition of subset]
```

part 2: A' union B' subset (A inter B)'

```
- direct proof (element-chasing)
- let y be any element of A' union B' [assumption]
- y in A' or y in B' [definition of union]
- y notin A or y notin B [definition of complement]
- not y in A or not y in B [notation]
- not (y in A and y in B) [de morgans]
- not (y in A inter B) [definition of intersection]
- y notin A inter B [notation]
- y in (A inter B)' [definition of complement]
- since y was any element of A' union B', A' union B' subset (A inter B)' [definition of subset]
```

conclusion: both subsets hold, so (A inter B)' = A' union B' [definition of set equality]

---

## Q3. Prove A inter (B union C) = (A inter B) union (A inter C) with an iff chain. Name the logic law you use.

#### First attempt

```
- iff chain (both direction at once)
- let x be any element of U [assumption]
x in A inter (B union C)
<-> x in A and x in (B union C) [definition of intersection]
<-> x in A and x in B or x in C [definition of union]
<-> (x in A and x in B) or (x in A and x in C) [distribution]
<-> x in (A inter B) or x in (A inter C) [definition of intersection]
<-> x in (A inter B) union (A inter C) [definition of union]
- since x in A inter (B union C) <-> x in (A inter B) union (A inter C) for any x, A inter (B union C) = (A inter B) union (A inter C) [definition of set equality]
```

#### Corrected

```
- iff chain (both direction at once)
- let x be any element of U [assumption]
x in A inter (B union C)
<-> x in A and x in (B union C) [definition of intersection]
<-> x in A and (x in B or x in C) [definition of union]
<-> (x in A and x in B) or (x in A and x in C) [distribution]
<-> x in (A inter B) or x in (A inter C) [definition of intersection]
<-> x in (A inter B) union (A inter C) [definition of union]
- since x in A inter (B union C) <-> x in (A inter B) union (A inter C) for any x, A inter (B union C) = (A inter B) union (A inter C) [definition of set equality]
```

---

## Q4. Prove (A - B) - C = A - (B union C) with an iff chain.

Hint: when you reach the middle, you'll have three "x ..." pieces joined by and. Look at section 1's worked example and think about which law turns x notin B and x notin C into a statement about B union C.

```
- iff chain (both direction at once)
- let x be any element of U [assumption]
x in (A - B) - C
<-> x in (A - B) and x notin C [definition of difference]
<-> x in A and x notin B and x notin C [definition of difference]
<-> x in A and not (x in B or x in C) [de morgans]
<-> x in A and not x in (B union C) [definition of union]
<-> x in A and x notin (B union C) [notation]
<-> x in A - (B union C) [definition of difference]
- since x in (A - B) - C <-> x in A - (B union C) for any x, (A - B) - C = A - (B union C) [definition of equality]
```

---

## Q5.

### (a) Prove A inter B subset A union B by element-chasing. Mark the one-way step.

```
- direct proof (element-chasing)
- let x be any element of A inter B [assumption]
- x in A and x in B [definition of intersection]
- so x in A [simplification: p and q, so p]
- so x in A or x in B [addition: p, therefore p or q]
- x in A union B [definition of union]
- since x was any element of A inter B, A inter B subset A union B [definition of subset]
```

### (b) Show that A union B subset A inter B is not always true. Give specific small sets, compute both sides, and name the element that breaks it.

#### First attempt

```
- direct proof (element-chasing)
- let x be any element of A union B [assumption]
- x in A or x in B [definition of union]

A = {1, 2}
B = {2, 3}
A union B = {1, 2, 3}
A inter B = {2}

- 1 and 3 in A union B [listed line 150]
- 1 and 3 notin A inter B [not listed line 151]
- since 1 and 3 notin A union B and notin A inter B, A union B is not subset A inter B [definition of subset]
```

#### Corrected

```
A = {1, 2} [assumption]
B = {2, 3} [assumption]
A union B = {1, 2, 3} [definition of union]
A inter B = {2} [definition of intersection]

- 3 in A union B [listed line 146]
- 3 notin A inter B [not listed line 147]
- since 3 in A union B and notin A inter B, A union B is not subset A inter B [definition of subset]
```
