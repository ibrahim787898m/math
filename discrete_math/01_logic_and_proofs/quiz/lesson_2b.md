# Lesson 2B Quiz: Equivalence Laws

Step 10.5 · Discrete math: logic & proofs

- First attempt: 8.75/10
- Q4 corrected after review

Rules: one step per line, and the law name in brackets on every line.

---

## Q1. Name the law (0.5 each):

(a) p or (p and q) == p - Absorption law

(b) not (p and q) == not p or not q - De Morgan law

(c) p and (q or r) == (p and q) or (p and r) - Distributive law

(d) p and not p == F - Negation law

---

## Q2. Remove the outer not and simplify fully:

### (a) not (not p and not q)

```
== (not not p) or (not not q) [De Morgan]
== p or q [Double Negation]
```

### (b) not (p -> not q). Hint: get rid of -> first.

```
== not (not p or not q) [Implication]
== (not not p) and (not not q) [De Morgan]
== p and q [Double Negation]
```

---

## Q3. Use laws to prove that p -> (p or q) is a tautology, meaning it simplifies to T.

```
p -> (p or q)
== (not p) or (p or q) [Implication]
== (not p or p) or q [Associative]
== T or q [Negation]
== T [Domination]
```

- tautology means we will get T for every result and after simplifying the expression we can see it.

---

## Q4. Simplify (p or q) and not p as much as possible. Hint: this time use Distributive left to right.

### First attempt

```
(p or q) and not p
== (p and not p) or (q and not p) [Distributive left to right]
== F or (q and not p) [Negation]
== F [Domination]
```

### Corrected

```
(p or q) and not p
== (p and not p) or (q and not p) [Distributive left to right]
== F or (q and not p) [Negation]
== (q and not p) or F [Commutative]
== q and not p [Identity]
```

---

## Q5. Rewrite this Python condition without any not in front of parentheses:

```
not (is_admin or (logged_in and not expired))
== (not is_admin) and (not (logged_in and not expired)) [De Morgan]
== (not is_admin) and (not logged_in or (not not expired)) [De Morgan]
== (not is_admin) and ((not logged_in) or expired) [Double Negation]
```
