# Lesson 3B Quiz: Negating Quantifiers

Step 10.5 · Discrete math: logic & proofs

- First attempt: 7.5/10
- Q3, Q4 and Q5(b) corrected after review

Rules: one step per line with the law name in brackets; write the original and the "Negation:" on separate lines (no == between them); say what each predicate means.

---

## Q1. Push the not inside. The domain is the integers (1 point each):

### (a) not exists x (x < 0)

```
== forall x (not x < 0) [quantifier negation]
== forall x (x >= 0) [negating a comparison]
```

### (b) not forall x (x * x != 4)

```
== exists x (not (x * x != 4)) [quantifier negation]
== exists x (x * x == 4) [negating a comparison]
```

---

## Q2. Use S(x): "x is a student" and P(x): "x passed". Simplify fully, then say what it means in English:

```
not forall x (S(x) -> P(x))
== exists x (not (S(x) -> P(x))) [quantifier negation]
== exists x (not (not S(x) or P(x))) [implication]
== exists x (not not S(x) and not P(x)) [de morgan]
== exists x (S(x) and not P(x)) [double negation]
```

- some student did not pass.

---

## Q3. Same predicates. Simplify fully, then say what it means in English:

### First attempt

```
not exists x (S(x) and not P(x))
== forall x (not (S(x) and P(x))) [quantifier negation]
== forall x (not S(x) or not P(x)) [de morgan]
```

- every student did not pass.

### Corrected

```
not exists x (S(x) and not P(x))
== forall x (not (S(x) and not P(x))) [quantifier negation]
== forall x (not S(x) or not not P(x)) [de morgan]
== forall x (not S(x) or P(x)) [double negation]
== forall x (S(x) -> P(x)) [implication]
```

- every student passe.

---

## Q4. For each sentence, write the original in symbols, then the negation, push the not inside, and finish with a natural English sentence (1 point each):

### (a) "Every function in my code has a docstring."

#### First attempt

```
forall f (C(f) or D(f))
negation: not forall f (C(f) or D(f))
== exists f (not (C(f) or D(f))) [quantifier negation]
== exists f (not C(f) and not D(f)) [de morgan]
```

- some function did not have docstring.

#### Corrected

```
C(f) - function is code
D(f) - docstring in function
forall f (C(f) -> D(f))
negation: not forall f (C(f) -> D(f))
== exists f (not (C(f) -> D(f))) [quantifier negation]
== exists f (not (not C(f) or D(f))) [implication]
== exists f (not not C(f) and not D(f)) [de morgan]
== exists f (C(f) and not D(f)) [double negation]
```

- some function did not have docstring.

### (b) "Some LeetCode problem is easy."

#### First attempt

```
exists p (L(p))
negation: not exists p (L(p))
== forall p (not L(p)) [quantifier negation]
```

- every leetcode problem is not easy.

#### Corrected

```
E(p) - leetcode problem is easy
exists p (E(p))
negation: not exists p (E(p))
== forall p (not E(p)) [quantifier negation]
```

- every leetcode problem is not easy.

---

## Q5.

### (a) Rewrite not all(len(name) > 0 for name in names) without a not in front of all.

```
not all(len(name) > 0 for name in names)
== any(not len(name) > 0 for name in names) [quantifier negation]
== any(len(name) <= 0 for name in names) [negating a comparison]
```

### (b) In one or two lines, explain why the negation of "all tests passed" is not "all tests failed". Use an example with 3 tests.

#### First attempt

```
"all tests passed"
forall t (P(t))
negation: not forall t (P(t))
== exists t (not P(t)) [quantifier negation]
```

- some test did not pass
- so when we do the negation of this statement quantifier changes and the meaning of the sentence also changes.

#### Added after review (the 3-test example)

```
tests = {pass, fail, pass}
all test passed? no - F
all test failed? no - F
- both have same truth value
*now try with the correct negation one
all test passed? no - F
some test did not pass? yes - T
- see now the quantifier negation one and the orginal one differs with their truth value.
```
