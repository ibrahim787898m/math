# Lesson 3C Quiz: Nested Quantifiers

Step 10.5 · Discrete math: logic & proofs

- First attempt: 10/10

Rules: evaluate line by line. For proofs, one step per line, with the law on each line.

---

## Q1. Use the domain {0, 1, 2}. Evaluate (1 point each):

### (a) forall x exists y (x * y == 0)

```
x = 0, y = 0: 0 * 0 = 0 == 0 = T
x = 1, y = 0: 1 * 0 = 0 == 0 = T
x = 2, y = 0: 2 * 0 = 0 == 0 = T
each x has a y so T
```

### (b) exists y forall x (x * y == 0)

```
Try y = 0:
    x = 0: 0 * 0 = 0 == 0 = T
    x = 1: 1 * 0 = 0 == 0 = T
    x = 2: 2 * 0 = 0 == 0 = T
```

- y = 0 works for all x so T

---

## Q2. Use the domain {1, 2, 3}. Evaluate (1 point each):

### (a) forall x exists y (x != y)

```
x = 1, y = 2: 1 != 2 = T
x = 2, y = 1: 2 != 1 = T
x = 3, y = 1: 3 != 1 = T
```

- each x has a different y so T

### (b) exists y forall x (x != y)

```
Try y = 1:
    x = 1: 1 != 1 = F
Try y = 2:
    x = 2: 2 != 2 = F
Try y = 3:
    x = 3: 3 != 3 = F
```

- no y works for all x so F

---

## Q3. Use the domain: integers.

### (a) Push the not inside: not forall x exists y (x + y == 10)

```
not forall x exists y (x + y == 10)
== exists x not exists y (x + y == 10) [quantifier negation]
== exists x forall y not (x + y == 10) [quantifier negation]
== exists x forall y (x + y != 10) [negating a comparison]
```

### (b) Is the original (without not) true? Give a one-line reason. Then say whether your answer to (a) is T or F, and why.

- yes true for origianl without not. cause for every integer we can choose y = 10 - x and then we can check x + y == 10 and it will be true

- anser of the a must be false casue it is the negation of the orginal without not. so as orginal without not is true the negation answer will give false value.

---

## Q4. Use the domain "all people", with T(x, y): "x teaches y".

### (a) Write exists x forall y T(x, y) and forall y exists x T(x, y) in plain English.

```
exists x forall y T(x, y) - there is one person who teaches everyone.
forall y exists x T(x, y) - everyone has one person who teaches.
```

### (b) Which one is stronger? Explain using "if one is true, is the other automatically true?"

- the first one is stronger because if one person teaches everyone, then everyone has a teacher, but everyone having a teacher does not mean the same person teaches everyone.

---

## Q5. Use the domain: the indices of nums.

### (a) Write in symbols: "every element has a different position with an equal value". Hint: this is the "every element has a duplicate" example.

```
forall i exists j (i != j and nums[i] == nums[j])
```

### (b) Write it as a Python expression using all(...) and any(...).

```
all(any(i != j and nums[i] == nums[j] for j in D) for i in D)
```
