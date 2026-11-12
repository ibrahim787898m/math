# Lesson 2C Quiz: Algebraic Proofs and Counterexamples

Step 10.6 · Discrete math: sets & functions

- First attempt: 8.5/10
- Corrected: Q4(a), Q4(b) and Q5(b)

Questions where my first attempt was wrong show the first attempt and the corrected answer.

In algebraic proofs, write one law per line with its name, and no x. In counterexamples, give a reason on every line and name one element.

---

## Q1. Prove algebraically: A union (A' inter B) = A union B.

```
algebraic proof (set laws):
A union (A' inter B)
= (A union A') inter (A union B) [distributive law]
= U inter (A union B) [complement law]
= (A union B) inter U [commutative law]
= A union B [identity law]

conclusion:
so A union (A' inter B) = A union B
```

---

## Q2. Prove algebraically: (A - B)' = A' union B.

```
algebraic proof (set laws):
(A - B)'
= (A inter B')' [Difference law]
= A' union (B')' [de morgans law]
= A' union B [double complement]

conclusion:
so (A - B)' = A' union B
```

---

## Q3. Prove algebraically: (A inter B) union (A inter B') = A.

```
algebraic proof (set laws):
(A inter B) union (A inter B')
= A inter (B union B') [distributive law, backwards]
= A inter U [complement law]
= A [identity law]

conclusion:
so (A inter B) union (A inter B') = A
```

---

## Q4. Each statement is false. Show it with a counterexample.

### (a) (A union B) inter C = A union (B inter C)

#### First attempt

```
translate:
- left: (x in A or x in B) and x in C
- right: x in A or (x in B and x in C)

disagree:

case 1: x in A, x in B, x in C
- left: (T or T) and T = T and T = T
- right: T or (T and T) = T or T = T
- dont disagree

case 2: x notin A, x in B, x in C
- left: (F or T) and T = T and T = T
- right: F or (T and T) = F or T = T
- dont disagree

case 3: x in A, x in B, x notin C
- left: (T or T) and F = T and F = F
- right: T or (T and F) = T or F = T
- disagree

counterexample:
- let A = {1}, B = {1}, C = {}
- left: (A union B) inter C = ({1} union {1}) inter {} = {1} inter {} = {} [definition of union and intersection]
- right: A union (B inter C) = {1} union ({1} inter {}) = {1} union {} = {1} [definition of intersection and union]
- 1 in A union (B inter C), 1 notin (A union B) inter C [listed in line 285, not listed in 284]

conclusion:
so (A union B) inter C = A union (B inter C) is false in general [one counterexample is enough]
```

#### Corrected

```
translate:
- left: (x in A or x in B) and x in C
- right: x in A or (x in B and x in C)

disagree:

case 1: x in A, x in B, x in C
- left: (T or T) and T = T and T = T
- right: T or (T and T) = T or T = T
- dont disagree

case 2: x notin A, x in B, x in C
- left: (F or T) and T = T and T = T
- right: F or (T and T) = F or T = T
- dont disagree

case 3: x in A, x in B, x notin C
- left: (T or T) and F = T and F = F
- right: T or (T and F) = T or F = T
- disagree

counterexample:
- let A = {1}, B = {1}, C = {} [choose sets]
- left: (A union B) inter C = ({1} union {1}) inter {} = {1} inter {} = {} [definition of union and intersection]
- right: A union (B inter C) = {1} union ({1} inter {}) = {1} union {} = {1} [definition of intersection and union]
- 1 in A union (B inter C), 1 notin (A union B) inter C [listed in line 285, not listed in 284]

conclusion:
so (A union B) inter C = A union (B inter C) is false in general [one counterexample is enough]
```

### (b) (A - B) union B = A

#### First attempt

```
translate:
- left: (x in A and x notin B) or x in B
- right: x in A

disagree:

case 1: x in A, x in B
- left: (T and F) or T = F or T = T
- right: T
- dont disagree

case 2: x in A, x notin B
- left: (T and T) or F = T or F = T
- right: T
- dont disagree

case 3: x notin A, x in B
- left: (F and F) or T = F or T = T
- right: F
- agree

counterexample:
- let A = {}, B = {1}
- left: (A - B) union B = ({} - {1}) union {1} = {} union {1} = {1} [definition of difference and union]
- right: A = {} [line 315]
- 1 in (A - B) union B, 1 notin A [listed in line 316, not listed in line 317]

conclusion:
so (A - B) union B = A is false in general [one counterexample is enough]
```

#### Corrected

```
translate:
- left: (x in A and x notin B) or x in B
- right: x in A

disagree:

case 1: x in A, x in B
- left: (T and F) or T = F or T = T
- right: T
- dont disagree

case 2: x in A, x notin B
- left: (T and T) or F = T or F = T
- right: T
- dont disagree

case 3: x notin A, x in B
- left: (F and F) or T = F or T = T
- right: F
- disagree

counterexample:
- let A = {}, B = {1} [choose sets]
- left: (A - B) union B = ({} - {1}) union {1} = {} union {1} = {1} [definition of difference and union]
- right: A = {} [line 315]
- 1 in (A - B) union B, 1 notin A [listed in line 316, not listed in line 317]

conclusion:
so (A - B) union B = A is false in general [one counterexample is enough]
```

---

## Q5. Decide whether each is true or false. If it's true, prove it algebraically. If it's false, give a counterexample.

### (a) A - (B inter C) = (A - B) union (A - C)

```
translate:
- left: x in A and (x noin B or x notin C)
- right: (x in A and x notin B) or (x in A and x notin C)

disagree:

case 1: x in A, x in B, x in C
- left: T and (F or F) = T and F = F
- right: (T and F) or (T and F) = F or F = F
- dont disagree

case 2: x in A, x in B, x notin C
- left: T and (F or T) = T and T = T
- right: (T and F) or (T and T) = F or T = T
- dont disagree

case 3: x notin A, x in B, x in C
- left: F and (F or F) = F and F = F
- right: (F and F) or (F and F) = F or F = F
- dont disagree

case 4: x in A, x notin B, x in C
- left: T and (T or F) = T and T = T
- right: (T and T) or (T and F) = T or F = T
- dont disagree

case 5: x in A, x notin B, x notin C
- left: T and (T or T) = T and T = T
- right: (T and T) or (T and T) = T or T = T
- dont disagree

case 6: x notin A, x in B, x notin C
- left: F and (F or T) = F and T = F
- right: (F and F) or (F and T) = F or F = F
- dont disagree

case 7: x notin A, x notin B, x in C
- left: F and (T or F) = F and T = F
- right: (F and T) or (F and F) = F or F = F
- dont disagree

case 8: x notin A, x notin B, x notin C
- left: F and (T or T) = F and T = F
- right: (F and T) or (F and T) = F or F = F
- dont disagree

so they agree for all the cases, we will do the algebraic proof to show the true.

algebraic proof (set laws):
A - (B inter C)
= A inter (B inter C)' [difference law]
= A inter (B' union C') [de morgans law]
= (A inter B') union (A inter C') [distributive law]
= (A - B) union (A - C) [difference law, reverse]

conclusion:
so A - (B inter C) = (A - B) union (A - C)
```

### (b) A union (B - C) = (A union B) - C

#### First attempt

```
Translate:
left: x in A or (x in B and x notin C)
right: (x in A or x in B) and x notin C

disagree:

case 1: x in A, x in B, x in C
left: T or (T and F) = T or F = T
right: (T or T) and F = T and F = F
disagree

case 2: x in A, x in B, x notin C
left: T or (T and T) = T or T = T
right: (T or T) and T = T and T = T
dont disagree

case 3: x notin A, x in B, x in C
left: F or (T and F) = F or F = F
right: (F or T) and F = T and F = F
dont disagree

case 4: x notin A, x in B, x notin C
left: F or (T and T) = F or T = T
right: (F or T) and T = T and T = T
dont disagree

case 5: x in A, x notin B, x in C
left: T or (F and F) = T or F = T
right: (T or F) and F = T and F = F
disagree

case 6: x in A, x notin B, x notin C
left: T or (F and T) = T or F = T
right: (T or F) and T = T and T = T
dont disagree

case 7: x notin A, x notin B, x in C
left: F or (F and F) = F or F = F
right: (F or F) and F = F and F = F
dont disagree

case 8: x notin A, x notin B, x notin C
left: F or (F and T) = F or F = F
right: (F or F) and T = F and T = F
dont disagree

counterexample:
Let:
A = 1
B = 2
C = 1

Left side:
A union (B - C)
= 1 union (2 - 1)
= 1 union 2
= 12

Right side:
(A union B) - C
= (1 union 2) - 1
= 2 - 1
= 2

Conclusion:
Since 2 is not equal to 2, the statement is false.
```

#### Corrected

```
Translate:
left: x in A or (x in B and x notin C)
right: (x in A or x in B) and x notin C

disagree:

case 1: x in A, x in B, x in C
left: T or (T and F) = T or F = T
right: (T or T) and F = T and F = F
disagree

case 2: x in A, x in B, x notin C
left: T or (T and T) = T or T = T
right: (T or T) and T = T and T = T
dont disagree

case 3: x notin A, x in B, x in C
left: F or (T and F) = F or F = F
right: (F or T) and F = T and F = F
dont disagree

case 4: x notin A, x in B, x notin C
left: F or (T and T) = F or T = T
right: (F or T) and T = T and T = T
dont disagree

case 5: x in A, x notin B, x in C
left: T or (F and F) = T or F = T
right: (T or F) and F = T and F = F
disagree

case 6: x in A, x notin B, x notin C
left: T or (F and T) = T or F = T
right: (T or F) and T = T and T = T
dont disagree

case 7: x notin A, x notin B, x in C
left: F or (F and F) = F or F = F
right: (F or F) and F = F and F = F
dont disagree

case 8: x notin A, x notin B, x notin C
left: F or (F and T) = F or F = F
right: (F or F) and T = F and T = F
dont disagree

counterexample:
- let A = {1}, B = {2}, C = {1} [choose sets]
- left: A union (B - C) = {1} union ({2} - {1}) = {1} union {2} = {1, 2} [definition of difference and union]
- right: (A union B) - C = ({1} union {2}) - {1} = {1, 2} - {1} = {2} [definition of union and difference]
- 1 in A union (B - C), and 1 notin (A union B) - C [listed in line 461 and not listed in line 462]

conclusion:
since 1 in A union (B - C), and 1 notin (A union B) - C, A union (B - C) = (A union B) - C is a false statement in general [one example is enough]
```
