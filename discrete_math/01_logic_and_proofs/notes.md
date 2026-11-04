# Logic & Proofs — Notes

_Roadmap step 10.5 · Concept notes for Lessons 1–4C · 2026-11-04_

## Terms cheat sheet

Every main term from step 10.5, in lesson order, with a one-line meaning. Keyboard notation: `not` ¬, `and` ∧, `or` ∨, `xor` ⊕, `->` →, `<->` ↔, `==` ≡, `forall` ∀, `exists` ∃.

| Term | Lesson | Meaning in one line |
| --- | --- | --- |
| Proposition | 1 | A statement that is either true or false, never both, never neither. |
| Truth value | 1 | T or F, the value a proposition has. |
| Propositional variable | 1 | A letter (p, q, r) that stands for a proposition. |
| Compound proposition | 1 | Smaller propositions joined by connectives. |
| Connective | 1 | A symbol that joins propositions: not, and, or, xor, ->, <->. |
| Negation (not, ¬) | 1 | True when p is false. |
| Conjunction (and, ∧) | 1 | True only when both parts are true. |
| Disjunction (or, ∨) | 1 | Inclusive or: true when at least one part is true. |
| Exclusive or (xor, ⊕) | 1 | True when exactly one part is true ("but not both"). |
| Implication (->, →) | 1 | p -> q is false only when p is T and q is F. |
| Hypothesis / conclusion | 1 | In p -> q, p is the hypothesis (left side), q the conclusion (right side). |
| Vacuous truth | 1 | p -> q is automatically true when p is false. |
| Biconditional (<->, ↔) | 1 | True when both parts have the same truth value. "if and only if". |
| "q if p" | 1 | p -> q. The part after "if" goes on the LEFT of the arrow. |
| "p only if q" | 1 | p -> q. The part after "only if" goes on the RIGHT of the arrow. |
| Converse | 1 | q -> p. NOT equivalent to p -> q. |
| Inverse | 1 | not p -> not q. NOT equivalent to p -> q. |
| Contrapositive | 1 | not q -> not p. Always equivalent to p -> q. |
| Precedence | 1 | Order connectives apply: not, and, or, ->, <->. The last one is outermost. |
| Case list (truth table) | 2A | Every combination of T/F for the variables, each traced line by line. |
| 2ⁿ cases | 2A | n distinct variables give 2ⁿ cases. Count distinct variables first. |
| Standard order | 2A | TT, TF, FT, FF (and TTT … FFF for 3), like counting in binary. |
| Tautology | 2A | T in every case. Example: p or not p. |
| Contradiction (expression) | 2A | F in every case. Example: p and not p. |
| Contingency | 2A | Some T and some F. |
| Logically equivalent (≡, ==) | 2A | Same result in every case. One differing case proves they are not. |
| Equivalence law | 2B | A known equivalence used to rewrite an expression one step at a time. |
| Law proof | 2B | One step per line, with the law name in brackets on every line. |
| De Morgan's laws | 2B | not (p and q) == not p or not q; not (p or q) == not p and not q. Negate each part and flip and/or. |
| Double negation | 2B | not not p == p. |
| Distributive law | 2B | p and (q or r) == (p and q) or (p and r), and with and/or swapped. Only works on a shared part. |
| Absorption | 2B | p or (p and q) == p; p and (p or q) == p. |
| Implication law | 2B | p -> q == not p or q. |
| Exportation | 2B | (p and q) -> r == p -> (q -> r). |
| Predicate | 3A | A statement with a variable, like P(x): "x > 3". Becomes a proposition once x has a value. |
| Domain | 3A | The set of values a variable may take. The answer can depend on it. |
| Universal quantifier (forall, ∀) | 3A | "for every x". A big and. Python all(). |
| Existential quantifier (exists, ∃) | 3A | "there is at least one x". A big or. Python any(). |
| Example (witness) | 3A | One x that makes an exists true. |
| Counterexample | 3A | One x that makes a forall false. |
| Translation pairing | 3A | "Every A is B" = forall x (A(x) -> B(x)); "Some A is B" = exists x (A(x) and B(x)). |
| Quantifier negation | 3B | not forall x P(x) == exists x not P(x); not exists x P(x) == forall x not P(x). Flip, then negate inside. |
| Negating a comparison | 3B | not (x > 0) is x <= 0; not (x == 0) is x != 0. |
| Nested quantifiers | 3C | Two or more quantifiers, read left to right, like nested loops. |
| Quantifier order | 3C | Same kind can swap; forall and exists mixed cannot. |
| Stronger claim | 3C | The one that demands more. exists y forall x is stronger than forall x exists y. |
| Proof | 4A | A chain of statements where every line has a reason. |
| Direct proof | 4A | Assume p, unpack definitions, algebra, repack, conclude q. |
| Arbitrary | 4A | A value with no special properties, so the proof covers every value. |
| Even | 4A | n = 2k for some integer k. |
| Odd | 4A | n = 2k + 1 for some integer k. |
| Divides (a \| b) | 4A | b = a · k for some integer k. |
| Closure | 4A | Integers stay integers under +, −, ×. Gives the "is an integer" line. |
| Proof by contrapositive | 4B | Prove not q -> not p instead of p -> q. |
| Proof by contradiction | 4B | Assume the opposite, reach R and not R, so the original is true. |
| Rational / irrational | 4B | Rational = a/b with integers a, b and b ≠ 0. Irrational = not rational (√2). |
| Lowest terms | 4B | A fraction whose top and bottom share no factor bigger than 1. |
| Mathematical induction | 4C | Prove P(n) for every n ≥ b with a base case and an inductive step. |
| Base case | 4C | Prove P(b), the first domino, by calculating both sides. |
| Inductive step | 4C | Prove P(k) -> P(k + 1) for an arbitrary k. |
| Inductive hypothesis (IH) | 4C | The assumed P(k) inside the inductive step. Mark where you use it. |
| Loop invariant | 4C | A statement true after every loop iteration, proved by induction. |

## Lesson 1: Propositions and connectives

A proposition is a statement with exactly one truth value, T or F; connectives build bigger propositions from smaller ones.

### What is and isn't a proposition

- "7 is prime" (T) and "2 + 2 = 5" (F) are propositions. A false statement is still a proposition.
- "x + 1 = 2" is not: it depends on x. That's a predicate (Lesson 3A).
- "Close the door" (command), "Is it raining?" (question) and "This sentence is false" (paradox) are not.

### The six connectives

- **not p**: true when p is false.
- **p and q**: true only when both are true.
- **p or q**: inclusive; true when at least one is true, including both.
- **p xor q**: true when exactly one is true.
- **p -> q**: false in only one case, p true and q false.
- **p <-> q**: true when p and q have the same truth value.

### Implication as a promise

Think of "If you finish your work (p), I'll pay you (q)."

- Finish and paid: promise kept, T.
- Finish and not paid: promise broken, **F**.
- Don't finish, paid anyway: no promise broken, T.
- Don't finish, not paid: no promise broken, T.

When p is false, p -> q is automatically true. That's **vacuous truth**. An implication says nothing about cause: "If 2 + 2 = 4, then Toronto is in Canada" is true.

### Ways to say p -> q

- if p, then q
- p implies q
- q if p
- p only if q (this is NOT q -> p)
- p is sufficient for q
- q is necessary for p

### "if" vs "only if" vs "if and only if" (Lesson 1B)

- **"only if"** is one arrow. The part after "only if" goes on the **right** side. "You can vote only if you are 18+" = vote -> 18+.
- **"if"** in the middle of a sentence is also one arrow. The part after "if" goes on the **left** side. "The ground is wet if it rains" = rain -> wet.
- **"if and only if"** is both arrows: <->.
- "p only if q" and "q if p" both mean p -> q.

Worked example, r = "it rains", s = "I stay home":

```
"I stay home only if it rains"
"only if" introduces the right side, so "it rains" goes on the right
answer: s -> r
```

### Converse, inverse, contrapositive

From p -> q:

- **Converse:** q -> p
- **Inverse:** not p -> not q
- **Contrapositive:** not q -> not p

The contrapositive always has the same truth value as the original. The converse and inverse match each other, but can differ from the original.

Example: "If a number is divisible by 4, then it is even." Converse "if even, then divisible by 4" is F (counterexample 2). Inverse "if not divisible by 4, then not even" is F (counterexample 2). Contrapositive "if not even, then not divisible by 4" is T.

### OR vs XOR

- "or" alone is or: true if at least one part is true.
- "but not both", "exactly one", "either … or … but not both" make it xor.

```
"Either 2 > 1 or 3 > 1, but not both."
connective: xor. rule: true when exactly one part is true
2 > 1 = T
3 > 1 = T
both are true, so F
```

### Always write the rule, then plug in

```
"3 > 1 if and only if 2 > 5."
connective: <->. rule: true when both parts have the same truth value
3 > 1 = T
2 > 5 = F
different, so F
```

### Precedence

Order: **not, and, or, ->, <->**. Each connective grabs its neighbours in that order. The one that goes last ends up **outermost** and splits the expression into a left half and a right half.

```
not p and q -> r or s
1. not grabs only p:   (not p) and q -> r or s
2. and goes next:      ((not p) and q) -> r or s
3. or goes next:       ((not p) and q) -> (r or s)
4. -> goes last, so it is the main connective

with p = F, q = T, r = F, s = F:
not p = T
(not p) and q = T and T = T      left side T
r or s = F or F = F              right side F
T -> F = F
```

### In Python

`not`, `and`, `or` are not, and, or. `^` on booleans is xor. Every `if` condition is a proposition. Python has no `->`: `(not p) or q` behaves exactly like p -> q.

## Lesson 2A: Checking every case

To know how an expression behaves everywhere, list every combination of T/F and trace each one; two expressions are equivalent when every case matches.

### How many cases

Each variable is T or F, so n **distinct** variables give **2ⁿ** cases: 1 gives 2, 2 give 4, 3 give 8. Count distinct variables first: p -> p has only one variable, so only 2 cases.

### Standard order

- 2 variables: TT, TF, FT, FF
- 3 variables: TTT, TTF, TFT, TFF, FTT, FTF, FFT, FFF

Like counting in binary: the last variable flips every line, the one before it every 2 lines.

### Worked example: not (p and q)

```
Case p=T, q=T: not (T and T) = not T = F
Case p=T, q=F: not (T and F) = not F = T
Case p=F, q=T: not (F and T) = not F = T
Case p=F, q=F: not (F and F) = not F = T
results: F, T, T, T
```

### Three kinds of expressions

- **Tautology:** T in every case. p or not p.
- **Contradiction:** F in every case. p and not p.
- **Contingency:** some T, some F. not (p and q) above.

In code, a contradiction condition (`if x > 5 and x < 3:`) is dead code, and a tautology condition makes the `if` pointless.

### Logical equivalence

1. List all cases for A.
2. List all cases for B, in the same order.
3. Compare case by case. All match: A == B. Any one differs: not equivalent.

```
p -> q:                       not q -> not p:
TT: T -> T = T                TT: F -> F = T
TF: T -> F = F                TF: T -> F = F
FT: F -> T = T                FT: F -> T = T
FF: F -> F = T                FF: T -> T = T
T, F, T, T  ==  T, F, T, T    so they are equivalent (the contrapositive)
```

Showing **not** equivalent needs just one case, like a counterexample:

```
p -> q vs q -> p, case p=F, q=T:
p -> q = F -> T = T
q -> p = T -> F = F
different, so not equivalent
```

### Reading implications fast: find the false case

A -> B is false only where the left side is T and the right side is F. Find those cases; everything else is T.

- `(p and q) -> r`: false only in TTF.
- `(p or q) -> r`: false in TTF, TFF, FTF.
- `p -> (q or r)`: false only in TFF.
- `p -> (q and r)`: false in TTF, TFT, TFF.

A stronger condition on the left (and) means fewer false cases; a demanding result on the right (and) means more. Same trick: and is true in only one case, or is false in only one case.

### Coding link: equivalence checker

`code/equivalent.py` loops over every case with nested loops over `[True, False]`, calls both expression functions, and returns False with the first differing case.

## Lesson 2B: Equivalence laws

Equivalence laws let you prove or simplify by rewriting one step at a time, instead of listing 2ⁿ cases. T and F stand for "always true" and "always false".

### Group A: the obvious ones (each comes as an and/or pair)

| Law | and version | or version |
| --- | --- | --- |
| Identity | p and T == p | p or F == p |
| Domination | p and F == F | p or T == T |
| Idempotent | p and p == p | p or p == p |
| Negation | p and not p == F | p or not p == T |
| Commutative | p and q == q and p | p or q == q or p |
| Associative | (p and q) and r == p and (q and r) | same with or |

Watch the pair: F dominates with **and**, T dominates with **or**. "F or X" is Identity (gives X), not Domination.

### Group B: the ones that do most of the work

- **Double negation:** not not p == p.
- **De Morgan:** not (p and q) == not p or not q; not (p or q) == not p and not q. To push a not inside, negate each part **and flip and/or**.
- **Distributive:** p and (q or r) == (p and q) or (p and r); p or (q and r) == (p or q) and (p or r). Like a × (b + c), but works both ways. Only use it when both groups share the same part.
- **Absorption:** p or (p and q) == p; p and (p or q) == p.
- **Implication:** p -> q == not p or q.
- **Contrapositive:** p -> q == not q -> not p.
- **Exportation:** (p and q) -> r == p -> (q -> r).

### How to prove with laws

1. Start from the left side.
2. One step per line.
3. Law name in brackets at the end of every line.
4. Stop when you reach the right side.

Laws work in both directions, and any letter can stand for a whole expression. Treat a group like `(q and not p)` as one block X.

### Worked examples

```
not (p -> q)
== not (not p or q)         [Implication]
== not not p and not q      [De Morgan]
== p and not q              [Double negation]
```

```
(p and q) or (p and not q)
== p and (q or not q)       [Distributive, right to left]
== p and T                  [Negation]
== p                        [Identity]
```

```
not (p and not q) or (p and q)          my Lesson 1 Q5(b) answer
== (not p or not not q) or (p and q)    [De Morgan]
== (not p or q) or (p and q)            [Double negation]
== not p or (q or (p and q))            [Associative]
== not p or (q or (q and p))            [Commutative]
== not p or q                           [Absorption]
== p -> q                               [Implication]
```

```
(p or q) and (p or not q)
== p or (q and not q)       [Distributive, right to left: pull out the shared p]
== p or F                   [Negation]
== p                        [Identity]
```

### Sanity check after simplifying

Test one case on both the original and your answer. If they differ, a step is wrong. Example: (p or q) and not p with p = F, q = T gives T, so "always F" can't be right; the correct answer is q and not p.

### Circuit link

This is the Boolean algebra from school ICT: and is A·B, or is A + B, not is A'. De Morgan: (A·B)' = A' + B'. Simplifying a circuit is simplifying an expression.

### In Python

`if not (x > 0 and y > 0):` is the same as `if x <= 0 or y <= 0:`.

## Lesson 3A: Predicates and quantifiers

A predicate is a statement with a blank; a quantifier (forall or exists) fills the blank for a whole domain and turns it into a proposition.

### Predicates

P(x): "x > 3" works like a Python function that returns a bool. P(5) = T, P(2) = F. Before x has a value, it is not a proposition (Lesson 1: "n is even"). A predicate can have several variables: Q(x, y): "x + y == 10".

### The domain

The set of values x may take. Always state it, because the answer can change: "x² ≥ x" is true for every integer, but false for the real number 0.5.

### The two quantifiers

**forall x P(x)**: P(x) is true for every x. Like `all(P(x) for x in domain)`.

- Show T: every x works (check each one in a small domain).
- Show F: one counterexample.

**exists x P(x)**: P(x) is true for at least one x. Like `any(...)`.

- Show T: one example.
- Show F: no x works (check all).

For a domain {a, b, c}: forall x P(x) = P(a) and P(b) and P(c); exists x P(x) = P(a) or P(b) or P(c).

### Worked examples, domain {1, 2, 3, 4}

```
forall x (x < 5)
x=1: 1 < 5 = T
x=2: 2 < 5 = T
x=3: 3 < 5 = T
x=4: 4 < 5 = T
every x works, so T

forall x (x is even)
x=1: 1 is even = F
counterexample x=1, so F

exists x (x * x == 9)
x=3: 3 * 3 == 9 = T
example x=3, so T

exists x (x > 4)
x=1: F   x=2: F   x=3: F   x=4: F
no x works, so F
```

forall is quick to prove false, exists is quick to prove true. The opposite answer means checking everything.

### Translating English: the pairing rule

Domain "all animals", D(x): x is a dog, B(x): x barks.

- "All dogs bark" = forall x (D(x) -> B(x)). **forall pairs with ->.** Using and would claim every animal is a barking dog.
- "Some dog barks" = exists x (D(x) and B(x)). **exists pairs with and.**

Why exists with -> is wrong: for a cat, D(cat) is F, so D(cat) -> B(cat) is T by vacuous truth. A non-dog satisfies it. In a world where no dog barks, "some dog barks" is F but exists x (D(x) -> B(x)) is still T because of the cat. With and, only a dog that barks can make it true.

### In Python

```python
all(n > 0 for n in nums)        # forall n in nums: n > 0
any(n % 2 == 0 for n in nums)   # exists n in nums: n is even
```

`all([])` is True: no element means no counterexample, so it is vacuously true.

## Lesson 3B: Negating quantifiers

To push a not past a quantifier, flip the quantifier and negate the inside.

### The two rules [Quantifier negation]

- not forall x P(x) == exists x (not P(x))
- not exists x P(x) == forall x (not P(x))

Why: forall over {a, b, c} is P(a) and P(b) and P(c). De Morgan turns not (P(a) and P(b) and P(c)) into not P(a) or not P(b) or not P(c), which is exists x (not P(x)).

### In English

- "Not every student passed" = "some student didn't pass".
- "No student cheated" = "every student didn't cheat".
- The negation of "all students passed" is **not** "all students failed". One failing student is enough.

A negation must have the opposite truth value. Quick test: can the original and your answer both be true at once? If yes, it isn't a negation. With tests {pass, fail, pass}: "all passed" is F and "all failed" is also F, so "all failed" can't be the negation; "some test did not pass" is T, the real negation.

### Worked examples

```
not forall x (x > 0)
== exists x (not (x > 0))       [Quantifier negation]
== exists x (x <= 0)            [negating a comparison]
```

```
not forall x (S(x) -> C(x))
== exists x not (S(x) -> C(x))           [Quantifier negation]
== exists x not (not S(x) or C(x))       [Implication]
== exists x (not not S(x) and not C(x))  [De Morgan]
== exists x (S(x) and not C(x))          [Double negation]
"Not every student knows coding" = "some student doesn't know coding"
```

```
not exists x (S(x) and C(x))
== forall x not (S(x) and C(x))      [Quantifier negation]
== forall x (not S(x) or not C(x))   [De Morgan]
== forall x (S(x) -> not C(x))       [Implication, right to left]
"No student knows coding" = "every student doesn't know coding"
```

The 3A pairing survives negation: forall with -> becomes exists with and, and the reverse.

### Writing a negation

1. Define each predicate and the domain.
2. Write the original in symbols (every A is B uses ->).
3. Write "Negation:" on a new line. Never put == between a statement and its negation.
4. Push the not inside, one law per line.
5. If you reach not A or B, finish with Implication: A -> B.
6. Read it back in natural English.

### In Python

```python
not all(n > 0 for n in nums)   ==   any(n <= 0 for n in nums)
not any(n == 0 for n in nums)  ==   all(n != 0 for n in nums)
```

## Lesson 3C: Nested quantifiers

Each variable needs its own quantifier; read them left to right like nested loops, and remember that mixed quantifiers can't be swapped.

### Reading and the loop picture

forall x exists y (x + y == 0), domain integers: "for every x there is a y with x + y == 0". T, pick y = −x. y may depend on x.

```python
all(any(x + y == 0 for y in D) for x in D)
```

The outer quantifier is the outer loop.

### Order matters

exists y forall x (x + y == 0) says one y works for every x. y is chosen first, so it can't depend on x. F.

- forall x exists y M(y, x): "everyone has a mother". T
- exists y forall x M(y, x): "someone is everyone's mother". F

Same kind swaps freely (forall forall, exists exists). Mixed (forall and exists) can't be swapped.

### Stronger claim

exists y forall x is **stronger** than forall x exists y: it demands more. If one person is everyone's friend, then everyone has a friend; the reverse doesn't follow. Stronger means harder to be true, not more likely.

### Strategy for a small domain

- Outer forall x: go through every x and find a y for each. One x with no y = counterexample, F.
- Outer exists y: find one y that works for every x. For each y you try, stop at the first x that fails.

Worked examples, domain {1, 2, 3}:

```
forall x exists y (x < y)
x=1: y=2 gives T
x=2: y=3 gives T
x=3: y=1 F, y=2 F, y=3 F, no y works
counterexample x=3, so F

forall x exists y (x <= y)
x=1: y=1, x=2: y=2, x=3: y=3, every x has a y, so T

exists y forall x (x <= y)
try y=3: x=1 T, x=2 T, x=3 T
y=3 works for every x, so T   ("there is a largest element", what max() finds)

exists y forall x (y < x)
y=1: x=1 gives F; y=2: x=1 F; y=3: x=1 F
no y works, so F
```

### Negating nested quantifiers

Apply Quantifier negation once per quantifier, from the outside in:

```
not forall x exists y P(x, y)
== exists x not exists y P(x, y)    [Quantifier negation]
== exists x forall y not P(x, y)    [Quantifier negation]
```

Shortcut: flip every quantifier, then negate the inside. Check the original's truth value first: the negation must have the opposite one. Example: exists x forall y (x * y == 0) is T (x = 0), so its negation forall x exists y (x * y != 0) must be F, and x = 0 is the counterexample.

### In code

- Two Sum: exists i exists j (i != j and nums[i] + nums[j] == target). Two nested exists = two nested loops, the O(n²) brute force.
- Every element has a duplicate: forall i exists j (i != j and nums[i] == nums[j]), which is `all(any(...) ...)`.

## Lesson 4A: Direct proof

A proof is a chain where every line has a reason; a direct proof of "if p, then q" assumes p for an arbitrary value and works step by step to q.

### Allowed reasons

An assumption, a definition, algebra, or a fact already proven.

### Definitions (learn exactly)

- **Even:** n = 2k for some integer k.
- **Odd:** n = 2k + 1 for some integer k.
- **Divides:** a | b means b = a · k for some integer k.
- **Closure:** integers are closed under +, −, ×.

### The template

1. Assume p for an arbitrary n. [assumption]
2. Unpack p with its definition.
3. Algebra.
4. Repack the result into the exact form of q's definition.
5. The "is an integer" line. [closure]
6. Conclude q.

Only p needs assuming: p -> q is automatically true when p is false (Lesson 1). Arbitrary: you're proving a forall, so pick an n with no special properties.

### Worked examples

```
If n is even, then n² is even.
1. Let n be an arbitrary even integer.          [assumption]
2. n = 2k for some integer k.                   [definition of even]
3. n² = (2k)² = 4k²                             [algebra]
4. n² = 2(2k²)                                  [algebra]
5. 2k² is an integer.                           [integers closed under ×]
6. So n² is even.                               [definition of even]  ∎
```

```
If m and n are odd, then m + n is even.
1. Let m and n be arbitrary odd integers.       [assumption]
2. m = 2k + 1 for some integer k.               [definition of odd]
3. n = 2j + 1 for some integer j.               [definition of odd]
4. m + n = 2k + 2j + 2 = 2(k + j + 1)           [algebra]
5. k + j + 1 is an integer.                     [integers closed under +]
6. So m + n is even.                            [definition of even]  ∎
```

```
If a | b and b | c, then a | c.
1. Assume a | b and b | c.                      [assumption]
2. b = a·k for some integer k.                  [definition of divides]
3. c = b·j for some integer j.                  [definition of divides]
4. c = (a·k)·j = a·(k·j)                        [substitute, algebra]
5. k·j is an integer.                           [integers closed under ×]
6. So a | c.                                    [definition of divides]  ∎
```

### Common mistakes

- **Examples are not a proof** of a forall. n² + n + 41 is prime for n = 0 to 39, then n = 40 gives 1681 = 41 × 41. But one counterexample does disprove a forall.
- **Same letter for different numbers.** m = 2k and n = 2k forces m = n.
- **Starting from q.** Always start from p.
- **Missing the "is an integer" line**, or giving the wrong reason for it (k + j needs +; 3k + 1 needs × and +).
- **"Not prime" needs a factorization** a × b with both factors bigger than 1. 1 × n shows nothing.

### Why it matters in code

Tests check a few inputs; a proof covers all of them.

## Lesson 4B: Contrapositive and contradiction

When the direct route gets stuck, prove the equivalent not q -> not p instead, or assume the opposite and reach something impossible.

### When direct gets stuck

"If n² is even, then n is even": from n² = 2k you'd get n = √(2k), which says nothing useful about n.

### Proof by contrapositive

p -> q == not q -> not p (proved by cases in 2A and by laws in 2B). So prove not q -> not p.

1. "We prove the contrapositive: if not q, then not p."
2. Assume not q.
3. Direct-proof steps to not p.
4. Last line: the original claim [contrapositive equivalence].

The contrapositive is not q -> not p. Not the converse (q -> p), not the inverse (not p -> not q). Fact used: an integer that isn't even is odd, and the reverse.

```
If n² is even, then n is even.
We prove the contrapositive: if n is odd, then n² is odd.
1. Let n be an arbitrary odd integer.            [assumption]
2. n = 2k + 1 for some integer k.                [definition of odd]
3. n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1           [algebra]
4. 2k² + 2k is an integer.                       [closed under × and +]
5. So n² is odd.                                 [definition of odd]
6. So if n² is even, then n is even.            [contrapositive equivalence]  ∎
```

```
If 3n + 1 is even, then n is odd.
We prove the contrapositive: if n is even, then 3n + 1 is odd.
1. Let n be an arbitrary even integer.           [assumption]
2. n = 2k for some integer k.                    [definition of even]
3. 3n + 1 = 6k + 1 = 2(3k) + 1                   [algebra]
4. 3k is an integer.                             [closed under ×]
5. So 3n + 1 is odd.                             [definition of odd]
6. So if 3n + 1 is even, then n is odd.          [contrapositive equivalence]  ∎
```

Negating an or in a contrapositive uses De Morgan: "if x + y ≥ 10, then x ≥ 5 or y ≥ 5" has contrapositive "if x < 5 and y < 5, then x + y < 10".

### Proof by contradiction

1. "Assume, for contradiction, not S."
2. Reason until you reach a statement R and its negation not R. R and not R == F (Negation law), so the assumption was wrong.
3. Name the lines that clash.
4. Last line: S is true.

```
There is no largest integer.
1. Assume, for contradiction, there is a largest integer N.  [assumption]
2. N + 1 is an integer.                                       [closed under +]
3. N + 1 > N.                                                 [algebra]
4. So N is not the largest integer.                           [lines 2, 3]
5. Lines 1 and 4 contradict each other.                       [contradiction]
6. So there is no largest integer.  ∎
```

```
√2 is irrational.  (rational = a/b, integers, b ≠ 0, can be reduced to lowest terms)
1.  Assume, for contradiction, √2 is rational.                [assumption]
2.  √2 = a/b, a, b integers, b ≠ 0, in lowest terms.          [definition of rational]
3.  2 = a² / b²                                               [square both sides]
4.  a² = 2b²                                                  [algebra]
5.  a² is even.                                               [definition of even]
6.  a is even.                                                [contrapositive proof above]
7.  a = 2k for some integer k.                                [definition of even]
8.  2b² = 4k², so b² = 2k²                                    [substitute, algebra]
9.  b² is even, so b is even.                                 [definition of even, proof above]
10. a and b are both divisible by 2.                          [lines 6, 9]
11. Line 10 contradicts "lowest terms" in line 2.             [contradiction]
12. So √2 is irrational.  ∎
```

Every link must be written. Example: "2m + 4n = 2(m + 2n) is even" and "7 is odd" only clash after the line "7 = 2(m + 2n), so 7 is even [lines 1, 4]".

### Choosing a method

- **Direct:** p gives you something to compute with (n is even gives n = 2k).
- **Contrapositive:** not q is a better start. Typical sign: p is about n² or n³, q is about n.
- **Contradiction:** the claim says something doesn't exist or can't happen: "no …", "not …", "irrational", "infinitely many".

### In code

"You can't find the max of an unsorted list without looking at every element": assume an algorithm skips one; that element could be the max; contradiction. Arguments like this prove no faster algorithm exists.

## Lesson 4C: Induction

Induction proves P(n) for every n ≥ b with two parts: a base case (the first domino falls) and an inductive step (each domino knocks over the next).

### Why it works

P(0) is true. P(0) -> P(1) gives P(1). P(1) -> P(2) gives P(2), and so on forever, so every n is reached.

### The template

```
Claim: for all n ≥ b, P(n).

Base case (n = b):
  calculate both sides and show P(b) is true.

Inductive step:
  Let k ≥ b be arbitrary.
  Assume P(k).                     [inductive hypothesis, IH]
  Goal: P(k + 1), written out in full.
  Start from the left side of P(k + 1), use the IH, simplify to the right side.
  So P(k + 1) is true.

Conclusion: by induction, P(n) is true for all n ≥ b.  ∎
```

Assuming P(k) isn't cheating: the step proves the implication P(k) -> P(k + 1), and you prove an implication by assuming its left side (4A), for one arbitrary k.

### Worked example: the sum formula

```
Claim: for all n ≥ 1, 1 + 2 + … + n = n(n + 1)/2.

Base case (n = 1):
  left side  = 1
  right side = 1(1 + 1)/2 = 1
  equal, so P(1) is true.                       [calculation]

Inductive step:
  Let k ≥ 1 be arbitrary.
  Assume 1 + 2 + … + k = k(k + 1)/2.            [IH]
  Goal: 1 + 2 + … + k + (k + 1) = (k + 1)(k + 2)/2

  1 + 2 + … + k + (k + 1)
  = k(k + 1)/2 + (k + 1)                        [IH]
  = (k(k + 1) + 2(k + 1)) / 2                   [algebra]
  = (k + 1)(k + 2) / 2                          [algebra: factor out (k + 1)]
  That's the goal, so P(k + 1) is true.

Conclusion: by induction, the formula holds for all n ≥ 1.  ∎
```

Key move: find P(k) inside P(k + 1). The sum to k + 1 is the sum to k plus one more term.

### Worked example: divisibility

```
Claim: for all n ≥ 0, 3 | (4ⁿ − 1).

Base case (n = 0): 4⁰ − 1 = 0 = 3 · 0, so 3 | 0.      [definition of divides]

Inductive step:
  Let k ≥ 0 be arbitrary.
  Assume 4ᵏ − 1 = 3m for some integer m.            [IH, definition of divides]
  Goal: 3 | (4ᵏ⁺¹ − 1)
  4ᵏ⁺¹ − 1 = 4 · 4ᵏ − 1                           [exponent rule]
           = 4(3m + 1) − 1                          [IH]
           = 12m + 3 = 3(4m + 1)                    [algebra]
  4m + 1 is an integer.                             [closed under × and +]
  So 3 | (4ᵏ⁺¹ − 1).                               [definition of divides]

Conclusion: by induction, 3 | (4ⁿ − 1) for all n ≥ 0.  ∎
```

### Common mistakes

- **Skipping the base case.** "Assume k = k + 1, add 1, so k + 1 = k + 2" has a working step, but P(1) says 1 = 2. No first domino, nothing falls. Same for "n² + n is odd": the step works, but 1² + 1 = 2 is even.
- **Never using the IH**, or not marking where you use it.
- **Starting from the goal.** Start from the left side of P(k + 1).
- **Conclusion about k.** k was just the step variable; the conclusion is about n.
- **Checking only one side** in the base case or in numeric checks.

### In code: loops and recursion

```python
total = 0
for i in range(1, n + 1):
    total += i
```

Loop invariant: after running for i = 1 up to k, total = 1 + … + k = k(k + 1)/2. Base: after i = 1, total is 1. Step: adding k + 1 keeps it true.

```python
def power2(n):
    if n == 0:          # base case: 2^0 = 1
        return 1
    return 2 * power2(n - 1)
```

IH: assume power2(n − 1) returns 2ⁿ⁻¹. Then 2 * power2(n − 1) = 2 · 2ⁿ⁻¹ = 2ⁿ. The recursion's base case is the induction's base case.

## Proof-writing rules and my mistakes checklist

Run through this list before submitting any answer; every item comes from a mistake I actually made in a quiz.

### Rules for every proof

- [ ] Line 1 names the method: "Direct proof", "We prove the contrapositive: …", "Assume, for contradiction, …", or "Base case / Inductive step".
- [ ] A reason in brackets on every line, including [assumption] on line 1.
- [ ] Different letters for different numbers (k, j, m).
- [ ] The "is an integer" line, with the right closure (+, ×, or both).
- [ ] Contradiction: name the lines that clash, and write every link between them.
- [ ] Induction: base case with both sides, goal in full, [IH] marked, conclusion about n.
- [ ] Last line states the original claim.

### Habits that cost me points

- [ ] **Reread the question.** Did I define the predicates, give the example it asked for, explain "why"? (3B Q4, Q5; 4B D5)
- [ ] **Use the given letters and meanings** exactly. (1B drill)
- [ ] **"only if"**: the part after it goes on the right of the arrow. (Quiz 1 Q2(d))
- [ ] **Write the rule line** before plugging in: "Connective: xor. Rule: exactly one is true." (Quiz 1 Q3)
- [ ] **Count distinct variables first.** p -> p has 2 cases, not 4. (2A drill)
- [ ] **"Every A is B" uses ->, never or.** (3B drill and Q4)
- [ ] **Compare each line with the one above** for copy slips, like a dropped not or a wrong substitution. (3B Q3, 4A Q5)
- [ ] **Sanity-check one case** after simplifying, and check the original's truth value before negating. (2B Q4, 3C drill)
- [ ] **No == between a statement and its negation.** Write "Negation:" instead. (3B drill)
- [ ] **Know the and/or pair** of each law: F dominates with and, "F or X" is Identity. (2B Q4)
- [ ] **Examples are not proofs** of a forall; a factorization (not 1 × n) proves "not prime". (4A drill, 4A Q5)
- [ ] **Read once before sending** for spelling ("exits" for "exists").
