# Lesson 3A Quiz: Predicates & Quantifiers

Step 10.5 · Discrete math: logic & proofs

- First attempt: 9/10
- Q4(c) explanation corrected after review

Show every check line by line.

---

## Q1. Let Q(x, y): "x + y == 10", with the domain being the integers.

### (a) Find Q(3, 7), Q(5, 4) and Q(-2, 12). Show the calculation.

```
Q(x, y): "x + y == 10"
x = 3, y = 7: 3 + 7 = 10 == 10 = T
x = 5, y = 4: 5 + 4 = 9 == 10 = F
x = -2, y = 12: -2 + 12 == 10 = T
```

### (b) Is Q(x, 3) a proposition? Explain in one line.

- Q(x, 3) = x + 3 == 10, where we dont know the x and we cant varify the expression so it si not proposition, it is predicate

---

## Q2. Use the domain {2, 4, 6, 8}. Find each truth value, showing your checks (0.5 each):

```
D = {2, 4, 6, 8}
```

### (a) forall x (x is even)

```
x = 2: 2 is even = T
x = 4: 4 is even = T
x = 6: 6 is even = T
x = 8: 8 is even = T
```

- each x gives same truth value so it is T

### (b) forall x (x > 3)

```
x = 2: 2 > 3 = F
```

- counterexample x = 2 which is not greater than 3, so the expression is F cause each result should be T.

### (c) exists x (x * x == 36)

```
x = 4: 6 * 6 = 36 == 36 = T
```

- so when x = 4 the expression is T, so we got at least one case with T, so the expression is T

### (d) exists x (x is odd)

```
x = 2: 2 is odd = F
x = 4: 4 is odd = F
x = 6: 6 is odd = F
x = 8: 8 is odd = F
```

- so each x gives F and we did not get any true value so the expression is F

---

## Q3. The domain changes the answer. Find the truth value of exists x (x * x == x):

### (a) with the domain {2, 3, 4}

```
exists x (x * x == x)
x = 2: 2 * 2 = 4 == 2 = F
x = 3: 3 * 3 = 9 == 3 = F
x = 4: 4 * 4 = 16 == 4 = F
```

- so each value gives F, expression is F

### (b) with the domain {0, 1, 2}

```
exists x (x * x == x)
x = 0: 0 * 0 = 0 == 0 = T
```

- so when x = 0 the expression is T, as we got any result T, the expression is T, no need to check rest.

---

## Q4. Use the domain "all people", with P(x): "x is a programmer" and L(x): "x likes Python". Translate into symbols:

(a) "Every programmer likes Python." forall x (P(x) -> L(x))

(b) "Some programmer does not like Python." exists x (P(x) and not L(x))

(c) "Some programmer likes Python." exists x (P(x) and L(x))

Then explain in one line why you used and and not -> here.

#### First attempt

when we use -> the right side is gonna be vacuously true all the time whatever the left side is so we dont use -> instead we use and cause when we use and that means when left side is true right side will check and as right side is always true the expression is gonna be true.

#### Corrected

so when we use -> and x is not programmer so the left side is false and when left side is false P(x) -> L(x) = T cause the right side does not matter, but the problem is that translation is not correct, when x is not programmer entire expression should come false but as we used -> the expression comes out as true. thats why we use and, and when we use it, if P(x) is false the expression is gonna be exactly F.

---

## Q5. Take nums = [3, -1, 4].

### (a) Write in symbols what all(n % 2 == 1 for n in nums) checks. Then find its value, checking line by line.

```
forall n in nums (n is odd)
n = 3: 3 is odd = T
n = -1: -1 is odd = T
n = 4: 4 is odd = F
```

- when n = 4 the expression is not true, and we needed all T for this expression, as we got one result F, so it is F.

### (b) Explain in one or two lines why all([]) returns True, using the idea of a counterexample.

- in an empty list there is no elements, so there is no counterexample, so vacuously it gives true.
