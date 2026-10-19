# Lesson 1 Quiz: Propositions & Connectives

Step 10.5 · Discrete math: logic & proofs

- First attempt: 6/10
- Redo (after Lesson 1B): 9/10, then corrected

Questions where my first attempt was wrong show the first attempt and the corrected answer.

---

## Q1. Which of these are propositions? Give a one-line reason for each.

(a) "Toronto is the capital of Canada."
False. So it is a proposition. Because Ottawa is the capital, and the statement is False.

(b) "n is even."
Not proposition. Because we dont know the n, so we dont know whether it is even or not.

(c) "Is 7 prime?"
Not proposition. Because it is a quesion, not true, not false.

(d) "2¹⁰ = 1024."
True. So it is proposition.

(e) "Solve this before Friday."
This is a command, not true or false. So it is not a proposition.

---

## Q2. Let p = "I study discrete math" and q = "I pass the quiz."

### First attempt

(a) Write ¬p ∧ q in English.
I dont study discrete math and I pass the quiz.

(b) Write ¬q → ¬p in English.
I dont pass the quiz and I dont study discrete math.

(c) Write p ↔ q in English.
I study discrete math only if I pass the quiz.

(d) Write "I pass the quiz only if I study discrete math" in symbols.
q <-> p

### Corrected

(a) Write ¬p ∧ q in English.
I dont study discrete math and I pass the quiz.

(b) Write ¬q → ¬p in English.
if i dont pass the quiz, then i dont study discrete math.

(c) Write p ↔ q in English.
I study discrete math if and only if I pass the quiz.

(d) Write "I pass the quiz only if I study discrete math" in symbols.
q -> p

---

## Q3. Find the truth value of each one. Reason line by line.

### First attempt

(a) "If 2 + 2 = 5, then the moon is made of cheese." T

Explain: 2 + 2 = 5 -> False, moon is made of cheese -> False, statement is in implies connective, fist part is p which is false and second part is q which is also false. So, p -> q : T

(b) "If 3 is odd, then 3² is even." F

Explain: 3 is odd -> true, 3^2 is even -> false, statement is in implies connective, first part is p which is true and second part is q which is false. So, p -> q : F

(c) "Either 1 > 2 or 2 > 1, but not both." T

Explain: 1 > 2 -> false, 2 > 1 -> true, statement is in OR connective, first part is p which is false and second part is q which is true. So, p OR q : T, cause if any of the part is true the proposition is true.

(d) "5 < 3 if and only if 10 < 6." F

Explain: 5 < 3 -> false, 10 < 6 -> false, statement is in IFF connective, first part is p which is false and second part is q which is also false. So, p <-> q : F, cause it would be true if the both part has the same truth value but not so it is false.

### Corrected

(a) and (b) unchanged.

(c) "Either 1 > 2 or 2 > 1, but not both." T

Explain: 1 > 2 false, 2 > 1 true -> true, statement is in XOR connective, first part is p which is false and second part is q which is true. so, p XOR q : T causes if either one part is true but not both then the proposition is true.

(d) "5 < 3 if and only if 10 < 6." T

Explain: 5 < 3 false, 10 < 6 false, statement is in IFF connective, first part is p which is false and second part is q which is false. so, p <-> q : T cause both part truth value is false so the proposition is ultimately true.

---

## Q4. Take the statement "If a number is divisible by 4, then it is even." Write its converse, inverse and contrapositive. Say whether each is true. For each false one, give a counterexample.

p = a number is divisible by 4
q = it is even

If a number is divisible by 4, then it is even. p -> q

converse: q -> p: If a number is even, then it is divisible by 4. F -> 2. it is even, but not divisible by 4 so this part is false

inverse: ¬p → ¬q: If a number is not divisible by 4, then it is not even. F -> 2. it is not divisible by 4, but it is even, so this part is false

contrapositive: ¬q → ¬p: If a number is not even, then it is not divisible by 4. T

---

## Q5.

### (a) Let p = T, q = F, r = F. First add parentheses to p ∨ q ∧ ¬r → ¬p using precedence. Then evaluate it step by step.

#### First attempt

```
(p ∨ (q ∧ (¬r → ¬p)))
= (p ∨ (q ∧ (not T -> not Te)))
= (p ∨ (q ∧ (F -> F)))
= (p ∨ (q ∧ (F)))
= (p ∨ (F ∧ F))
= (p ∨ (F))
= (T ∨ F)
= T
```

#### Corrected

```
(p ∨ (q ∧ (¬r))) → (¬p)
= (T OR (F AND (NOT F))) IMPLIES (NOT T)
= (T OR (F AND (T))) IMPLIES (F)
= (T OR F) IMPLIES (F)
= T IMPLIES F
= F
```

### (b) Write a Python expression using only not, and, or that behaves exactly like p → q. Explain line by line why it's False in exactly the right case.

#### First attempt

p -> q : false only one case: p true and q false

```python
not (not (p OR q)) AND q
```

```
1st case: p = T, q = T
= not (not (T OR T)) AND T
= not (not (T)) AND  T
= not F AND T
= T AND T
= T

2nd case: p = T, q = F
= not (not (T OR F)) AND F
= not (not (T)) AND F
= not F AND F
= T AND F
= F

3rd case: p = F, q = T
= not (not (F OR T)) AND T
= not (not (T)) AND T
= not F AND T
= T AND T
= T

4th case: p = F, q = F
= not (not (F OR F)) AND F
= not (not F) AND F
= not T AND F
= F AND F
= F
```

#### Corrected

p -> q : false only one case: p true and q false

```python
not (p and not q) or (p and q)
```

```
first case: p = T, q = T
not (T and not T) or (T and T)
= not (T and F) or T
= not (F) or T
= T or T
= T

second case: p = T, q = F
not (T and not F) or (T and F)
= not (T and T) or F
= not T or F
= F or F
= F

third case: p = F, q = T
not (F and not T) or (F and T)
= not (F and F) or F
= not F or F
= T or F
= T

forth case: p = F, q = F
not (F and not F) or (F and F)
= not (F and T) or F
= not F or F
= T or F
= T
```
