# Lesson 3A Quiz: Power Sets

Step 10.6 · Discrete math: sets & functions

- First attempt: 6.5/10
- Corrected: Q1, Q2(b), Q2(d), Q3(b), Q4(b) and Q5

Questions where my first attempt was wrong show the first attempt and the corrected answer.

Give every line a reason, including count lines, and answer true or false before the reason. In power-set proofs, cite known facts as facts (not assumptions), count proof lines from the method line, and check that the last line states the claim you were asked to prove.

---

## Q1. List P({x, y, z}) by size, one line per size with a reason. Then write the full P(...) set and check the count with 2^n.

#### First attempt

```
size 0 = {} [empty set is a subset of every set]
size 1 = {x}, {y}, {z} [one element each]
size 2 = {x, y}, {x, z}, {y, z} [every pair]
size 3 = {x, y, z} [a set is a subset of itself]
P({x, y, z}) = {{}, {x}, {y}, {z}, {x, y}, {y, z}, {x, z}, {x, y, z}} [all subset together]
count = 1 + 3 + 3 + 1 = 8 = 2^3
```

#### Corrected

```
size 0 = {} [empty set is a subset of every set]
size 1 = {x}, {y}, {z} [one element each]
size 2 = {x, y}, {x, z}, {y, z} [every pair]
size 3 = {x, y, z} [a set is a subset of itself]
P({x, y, z}) = {{}, {x}, {y}, {z}, {x, y}, {y, z}, {x, z}, {x, y, z}} [all subset together]
count = 1 + 3 + 3 + 1 = 8 = 2^3 [if |A| = n -> |P(A)| = 2^n]
```

---

## Q2. Let A = {1, 2}. Answer true or false, with a one-line reason for each.

### (a) {2} in P(A)

```
true cause {2} is a subset of A
```

### (b) 2 in P(A)

#### First attempt

```
the element of P(A) are sets and the number 2 is not one of them
```

#### Corrected

```
false cause the element of P(A) are sets and the number 2 is not one of them
```

### (c) {} subset P(A)

```
true cause empty set is a subset of every set
```

### (d) {{1}, {2}} subset P(A)

#### First attempt

```
true, cause {{1}, {2}} is an element of P(A)
```

#### Corrected

```
true, cause {1} and {2} are in P(A)
```

---

## Q3.

### (a) List P({}) and give |P({})|.

```
size 0 = {} [empty set is a subset of every set]
P({}) = {{}} [one subset]
|P({})| = 1 [one set only]
```

### (b) List P({{}}) and give |P({{}})|.

#### First attempt

```
size 0 - {} [empty set is a subset of every set]
size 1 - {{}} [the subset holding one element {}]
P({{}}) = {{}, {{}}} [all subset together]
|P({{}})| = 2
```

#### Corrected

```
size 0 - {} [empty set is a subset of every set]
size 1 - {{}} [the subset holding one element {}]
P({{}}) = {{}, {{}}} [all subset together]
|P({{}})| = 2 [n = 1 -> 2^1 = 2 element including empty set]
```

---

## Q4.

### (a) If |A| = 6, find |P(A)|. If |P(B)| = 128, find |B|. Show each step.

```
|A| = 6 -> |P(A)| = 2^6 = 2 * 2 * 2 * 2 * 2 * 2 = 64
|P(B)| = 128 -> 2^|B| = 128 -> |B| = log2(128) = 7 -> 2 * 2 * 2 * 2 * 2 * 2 * 2 = 128
```

### (b) In your own words (2-3 sentences), explain why |P(A)| = 2^n when |A| = n.

#### First attempt

```
when n = 1 -> sequence = 1
when n = 2 -> sequence = 1 + 2 + 1
when n = 3 -> sequence = 1 + 3 + 3 + 1
when n = 4 -> sequence = 1 + 4 + 6 + 4 + 1

there is a sequence i can see. but exactly i dont know.
```

#### Corrected

so to build a subset of A you check each element of A if it is in the subset or not so there are 2 choices. now if there are n elements, it is like 2 * 2 * 2 ... * 2 = 2^n. like the truth table, it can be only T or F.

---

## Q5. Prove that P(A inter B) subset P(A) by element-chasing. You may use "A inter B subset A" (from 2B) and transitivity of subset as facts, citing each one.

#### First attempt

```
direct proof (element chasing):
- assume A inter B subset A [assumption]
- let X be any element of P(A inter B) [assumption]
- X subset A inter B [definition of power set]
- X subset B [line 3 and 1, transitivity of subset]
- X in P(B) [definition of power set]
- since X was any element of P(A inter B), P(A inter B) subset P(B) [definition of subset]
```

#### Corrected

```
direct proof (element chasing):
- assume A inter B subset A [fact from 2b]
- let X be any element of P(A inter B) [assumption]
- X subset A inter B [definition of power set]
- X subset A [line 4 and 2, transitivity of subset]
- X in P(A) [definition of power set]
- since X was any element of P(A inter B), P(A inter B) subset P(A) [definition of subset]
```
