# Lesson 2A Quiz: Checking Every Case

Step 10.5 · Discrete math: logic & proofs

- First attempt: 9.5/10 (every answer correct; −0.5 for not writing the number of distinct variables before each trace in Q2–Q5)

Write each case list line by line. When a question has 2 variables, use the order TT, TF, FT, FF. Before every trace, first write how many distinct variables there are.

---

## Q1.

(a) How many cases does an expression with 5 variables have?
- 2^n = 2^5 = 2 * 2 * 2 * 2 * 2 = 32 cases

(b) How many cases does (p and not q) or (q -> p) have? Explain why in one line.
- obviously 4 cases. cause there are 2 variables p and q so 2^n = 2^2 = 4 cases

---

## Q2. Write the case list and classify each one as a tautology, contradiction or contingency.

### (a) (p -> q) or p

cases: TT, TF, FT, FF

```
case TT: (T -> T) or T = T or T = T
case TF: (T -> F) or T = F or T = T
case FT: (F -> T) or F = T or F = T
case FF: (F -> F) or F = T or F = T
```

result: TTTT
- (p -> q) or p is tautology cause every result is T.

### (b) (p xor q) and (p <-> q)

cases: TT, TF, FT, FF

```
case TT: (T xor T) and (T <-> T) = F and T = F
case TF: (T xor F) and (T <-> F) = T and F = F
case FT: (F xor T) and (F <-> T) = T and F = F
case FF: (F xor F) and (F <-> F) = F and T = F
```

result: FFFF
- (p xor q) and (P <-> q) is contradiction cause every result is F.

---

## Q3. Use case lists to show whether not (p or q) and (not p) and (not q) are equivalent.

not (p or q)

cases: TT, TF, FT, FF

```
case TT: not (T or T) = not T = F
case TF: not (T or F) = not T = F
case FT: not (F or T) = not T = F
case FF: not (F or F) = not F = T
```

result: FFFT

(not p) and (not q)

cases: TT, TF, FT, FF

```
case TT: (not T) and (not T) = F and F = F
case TF: (not T) and (not F) = F and T = F
case FT: (not F) and (not T) = T and F = F
case FF: (not F) and (not F) = T and T = T
```

result: FFFT

- we can see same results from the both expression so both are equivalent.

---

## Q4. Show that not (p and q) and (not p) and (not q) are not equivalent, using a single case.

case TF:

```
not (p and q) = not (T and F) = not F = T
(not T) and (not F) = F and T = F
```

- see if we check the case TF for both the result is not same and thats why they are not equivalent.

---

## Q5. Write the full case list for (p and q) -> r (8 cases, standard order) and classify it.

(p and q) -> r

cases: TTT, TTF, TFT, TFF, FTT, FTF, FFT, FFF

```
case TTT: (T and T) -> T = T -> T = T
case TTF: (T and T) -> F = T -> F = F
case TFT: (T and F) -> T = F -> T = T
case TFF: (T and F) -> F = F -> F = T
case FTT: (F and T) -> T = F -> T = T
case FTF: (F and T) -> F = F -> F = T
case FFT: (F and F) -> T = F -> T = T
case FFF: (F and F) -> F = F -> F = T
```

result: TFTTTTTT

- case TTF result is F and rest of the result is T. so the expression is contingency.
