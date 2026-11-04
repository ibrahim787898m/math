# Logic & Proofs — Practice Questions

_Roadmap step 10.5 · Every quiz and drill question, extra practice and related LeetCode problems · 2026-11-04_

## How to use this set

Every quiz question from step 10.5, plus new extra questions, grouped by lesson. Questions only, no answers: my graded answers are in `quiz/lesson_N.md`, and `notes.md` has the methods.

- **Quiz** questions are the ones I already answered once. Redo them without looking.
- **Extra** questions are new, at the same level or a step harder (marked ★).
- Write every proof line by line with a reason on each line, and run the checklist at the end of `notes.md` before checking.

## Lesson 1: Propositions and connectives

### Quiz

1. Which are propositions? Give a one-line reason for each. (a) "Toronto is the capital of Canada." (b) "n is even." (c) "Is 7 prime?" (d) "2¹⁰ = 1024." (e) "Solve this before Friday."
2. Let p = "I study discrete math", q = "I pass the quiz". (a) Write not p and q in English. (b) Write not q -> not p in English. (c) Write p <-> q in English. (d) Write "I pass the quiz only if I study discrete math" in symbols.
3. Find the truth value, line by line: (a) "If 2 + 2 = 5, then the moon is made of cheese." (b) "If 3 is odd, then 3² is even." (c) "Either 1 > 2 or 2 > 1, but not both." (d) "5 < 3 if and only if 10 < 6."
4. For "If a number is divisible by 4, then it is even", write the converse, inverse and contrapositive, say whether each is true, and give a counterexample for each false one.
5. (a) With p = T, q = F, r = F, add parentheses to p or q and not r -> not p, then evaluate step by step. (b) Write a Python expression using only not, and, or that behaves like p -> q, and trace all four cases.

### Drill (Lesson 1B)

Use r = "it rains", s = "I stay home".

6. Write in English: (a) s -> r (b) r xor s
7. Write in symbols: (a) "It rains only if I stay home." (b) "I stay home if it rains." (c) "It rains if and only if I stay home."
8. Find the truth value: (a) "Either 2 > 5 or 3 > 1, but not both." (b) "4 is odd if and only if 7 is even."
9. Add parentheses only: (a) not p or q and r (b) p and q -> not r or p

### Extra

10. Which are propositions? (a) "x² ≥ 0 for every real x." (b) "Run the tests." (c) "0 is even." (d) "This password is strong."
11. Let a = "the build passes", b = "I deploy". Write in symbols: (a) "I deploy only if the build passes." (b) "The build passing is necessary for me to deploy." (c) "I deploy if the build passes." Which two say the same thing?
12. For "If it is Sunday, then I review my notes", write the converse, inverse and contrapositive in English. Which one is equivalent to the original?
13. Find the truth value: (a) "If 10 is prime, then 3 + 3 = 7." (b) "7 > 2 xor 7 > 3." (c) "not (5 > 2) <-> (1 == 2)"
14. With p = F, q = T, r = T, add parentheses and evaluate: (a) not p and q or r (b) p or q -> r and not q (c) p -> q <-> not r
15. ★ Write "You get a refund if and only if you return the item within 30 days and you have the receipt" in symbols. Define your letters.
16. ★ Write "if I finish the lesson and the quiz, I will take a break and listen to music or play a game only if I am not tired" in symbols. Define your letters and add all parentheses.

## Lesson 2A: Checking every case

### Quiz

1. (a) How many cases does an expression with 5 variables have? (b) How many cases does (p and not q) or (q -> p) have? Explain in one line.
2. Write the case list and classify as tautology, contradiction or contingency: (a) (p -> q) or p (b) (p xor q) and (p <-> q)
3. Use case lists to show whether not (p or q) and (not p) and (not q) are equivalent.
4. Show that not (p and q) and (not p) and (not q) are not equivalent, using a single case.
5. Write the full case list for (p and q) -> r (8 cases, standard order) and classify it.

### Drill

6. How many cases does an expression with 4 variables have? List the 8 cases for 3 variables in standard order.
7. Write case lists for p xor q and (p or q) and not (p and q). Are they equivalent?
8. Classify: (a) p -> p (b) (p and q) and not p (c) p or q -> p
9. Show p <-> q and p -> q are not equivalent with a single case.

### Reading implications (find the false cases first, then check with a case list)

10. (a) (p xor q) -> r (b) p -> (q -> r)

### Extra

11. Write the number of distinct variables, then the case list, then classify: (a) (p and q) -> p (b) p -> (p or q) (c) (p -> q) and (p and not q)
12. Are p -> (q and r) and (p -> q) and (p -> r) equivalent? Use case lists (8 cases).
13. Show (p -> q) -> r and p -> (q -> r) are not equivalent with one case.
14. Without a full case list, find every false case of: (a) (p and q) -> (r or s) (b) (p or q) -> (p and q)
15. ★ In Python, which of these conditions is dead code (a contradiction) and which is always true (a tautology)? (a) `x > 5 and x < 3` (b) `x > 5 or x <= 5` (c) `x > 5 or x > 3`. Explain in one line each.
16. ★ Coding: finish the bonus in `code/equivalent.py`: support 3 variables, then any number of variables with itertools.product. Use it to check your answers to 12 and 13.

## Lesson 2B: Equivalence laws

One step per line, law name in brackets on every line.

### Quiz

1. Name the law: (a) p or (p and q) == p (b) not (p and q) == not p or not q (c) p and (q or r) == (p and q) or (p and r) (d) p and not p == F
2. Remove the outer not and simplify fully: (a) not (not p and not q) (b) not (p -> not q)
3. Use laws to prove p -> (p or q) is a tautology.
4. Simplify (p or q) and not p as much as possible.
5. Rewrite without any not in front of parentheses: `not (is_admin or (logged_in and not expired))`

### Drill

6. Name the law: (a) not (p or q) == not p and not q (b) p and (p or q) == p (c) p -> q == not p or q (d) p or F == p
7. Use De Morgan then double negation: (a) not (p and not q) (b) not (not p or q)
8. Prove p -> q == not q -> not p using only Implication, Commutative and Double negation.
9. Simplify (p or q) and (p or not q) to a single variable.
10. Rewrite without the outer not: `not (age < 18 or banned)`

### Extra

11. Simplify, then sanity-check one case: (a) p or (not p and q) (b) (p and q) or (p and not q) or (not p and q)
12. Prove with laws: (p -> q) and (p -> r) == p -> (q and r).
13. Prove with laws that (p and q) -> p is a tautology.
14. Prove with laws that p and (not p or q) == p and q.
15. Simplify not (p -> (q or not r)).
16. Rewrite the condition without any not in front of parentheses: `not (x > 0 and (y > 0 or z == 0))`
17. ★ Circuit: a circuit computes (A·B) + (A·B'). Simplify it to a single input and name each law.
18. ★ Prove exportation with laws: (p and q) -> r == p -> (q -> r).

## Lesson 3A: Predicates and quantifiers

### Quiz

1. Let Q(x, y): "x + y == 10", domain integers. (a) Find Q(3, 7), Q(5, 4), Q(−2, 12). (b) Is Q(x, 3) a proposition? Explain.
2. Domain {2, 4, 6, 8}. Find each truth value with checks: (a) forall x (x is even) (b) forall x (x > 3) (c) exists x (x * x == 36) (d) exists x (x is odd)
3. Find the truth value of exists x (x * x == x) for (a) domain {2, 3, 4} (b) domain {0, 1, 2}.
4. Domain all people, P(x): x is a programmer, L(x): x likes Python. Translate: (a) "Every programmer likes Python." (b) "Some programmer does not like Python." (c) "Some programmer likes Python", and explain why and, not ->.
5. nums = [3, −1, 4]. (a) Write in symbols what `all(n % 2 == 1 for n in nums)` checks, then evaluate it line by line. (b) Explain why `all([])` is True using counterexamples.

### Drill

6. P(x): "x * x < 10", integers. Find P(3), P(4), P(−3).
7. Domain {1, 2, 3, 4, 5}: (a) forall x (x + 1 > x) (b) forall x (x is odd) (c) exists x (x * 2 == 8) (d) exists x (x > 5)
8. Domain all people, S(x): student, C(x): knows coding. Translate: (a) "Every student knows coding." (b) "Some student knows coding." (c) "Some student does not know coding."
9. Write in symbols: `all(n > 0 for n in nums)` and `any(n % 2 == 0 for n in nums)`.
10. Explain why exists x (D(x) -> B(x)) is a bad translation of "Some dog barks", using a domain where no dog barks.

### Extra

11. Domain {−2, −1, 0, 1, 2}: (a) forall x (x * x >= 0) (b) forall x (x * x > 0) (c) exists x (x + 3 == 1) (d) exists x (x * x == 3)
12. Show the domain changes the answer: find a domain where forall x (x * x >= x) is T and one where it is F.
13. Domain all functions in a codebase, T(f): f has a test, D(f): f is documented. Translate: (a) "Every function has a test." (b) "Every documented function has a test." (c) "Some function is documented but has no test."
14. Write Python with all/any for: (a) "every word in words is lowercase" (b) "some score in scores is above 90" (c) "every even number in nums is positive".
15. ★ Why is forall x (S(x) and C(x)) a wrong translation of "Every student knows coding"? Give a domain where the two give different answers.

## Lesson 3B: Negating quantifiers

Write the original and the "Negation:" on separate lines, define every predicate, and name a law on each line.

### Quiz

1. Push the not inside, domain integers: (a) not exists x (x < 0) (b) not forall x (x * x != 4)
2. S(x): student, P(x): passed. Simplify and say it in English: not forall x (S(x) -> P(x))
3. Same predicates: not exists x (S(x) and not P(x))
4. Original, negation, push inside, English: (a) "Every function in my code has a docstring." (b) "Some LeetCode problem is easy."
5. (a) Rewrite `not all(len(name) > 0 for name in names)` without not in front of all. (b) Explain with 3 tests why the negation of "all tests passed" is not "all tests failed".

### Drill

6. Domain integers: (a) not forall x (x > 0) (b) not exists x (x == 0)
7. P(x): programmer, L(x): likes Python. Simplify not exists x (P(x) and not L(x)) and say it in English.
8. Write the negation as a natural English sentence: (a) "Every student submitted the homework." (b) "Some test failed." (c) "No number in the list is negative."
9. Rewrite without not in front of all/any: (a) `not all(score >= 50 for score in scores)` (b) `not any(word == "" for word in words)`

### Extra

10. Negate and simplify, domain integers: (a) not forall x (x >= 1) (b) not exists x (x * x == 2) (c) not forall x (x is even or x is odd)
11. Write the negation in natural English: (a) "Every app on my phone is updated." (b) "Some student got 10/10." (c) "No bug is critical." (d) "All tests pass and the build is green."
12. U(x): x is a user, A(x): x is an admin, V(x): x is verified. Negate and simplify: forall x (U(x) and A(x) -> V(x)). Say the result in English.
13. Rewrite without not in front of all/any: `not any(age < 0 or age > 150 for age in ages)`
14. ★ Before negating, decide if the original is T or F, then check that the negation has the opposite value: domain {1, 2, 3}, forall x (x < 4).

## Lesson 3C: Nested quantifiers

### Quiz

1. Domain {0, 1, 2}: (a) forall x exists y (x * y == 0) (b) exists y forall x (x * y == 0)
2. Domain {1, 2, 3}: (a) forall x exists y (x != y) (b) exists y forall x (x != y)
3. Domain integers. (a) Push the not inside: not forall x exists y (x + y == 10). (b) Is the original true? Then is your answer to (a) T or F, and why?
4. Domain all people, T(x, y): x teaches y. (a) Write exists x forall y T(x, y) and forall y exists x T(x, y) in English. (b) Which is stronger, and why?
5. Domain indices of nums. (a) Symbols for "every element has a different position with an equal value". (b) The same with all(...) and any(...).

### Drill

6. Domain {1, 2, 3}: (a) forall x exists y (x + y == 4) (b) exists y forall x (x + y == 4)
7. F(x, y): x is friends with y. English for forall x exists y F(x, y) and exists y forall x F(x, y). Which is stronger?
8. Push the not inside and decide the truth value: not exists x forall y (x * y == 0), domain integers.
9. Domain indices of nums. Symbols and Python for "nums contains two different positions with equal values".

### Extra

10. Domain {1, 2, 3, 4}: (a) forall x exists y (y == x + 1) (b) forall x exists y (x * y == 4) (c) exists x forall y (x <= y) (d) exists x forall y (x * y == y)
11. Domain integers. True or false, with a reason: (a) forall x exists y (y > x) (b) exists y forall x (y > x)
12. Negate fully, then say it in English: forall s exists c (Enrolled(s, c)), where s ranges over students and c over courses.
13. Write in symbols over the indices of nums, then as Python with all/any: (a) "nums is sorted in non-decreasing order" (b) "some value appears at least twice" (c) "every value has a larger value somewhere in nums"
14. ★ Two Sum: write "some pair of different positions sums to target" in symbols. How many checks does the nested-loop version make for an array of length n, and why?

## Lesson 4A: Direct proof

Reason on every line, [assumption] on line 1, different letters, the "is an integer" line before the conclusion.

### Quiz

1. Prove: if n is even, then 3n + 2 is even.
2. Prove: if m and n are even, then m · n is even.
3. Prove: if a | b, then a | 3b.
4. Prove: if n is odd, then n² − 1 is even.
5. Claim: for every integer n ≥ 0, n² + n + 41 is prime. (a) Does checking n = 0, 1, 2, 3 prove it? (b) Find a counterexample and show it is not prime.

### Drill

6. Write the definitions of odd and of a | b.
7. Prove: if n is odd, then n² is odd.
8. Prove: if n is even and m is odd, then n + m is odd.
9. Find the mistake: "m = 2k and n = 2k, so m + n = 4k = 2(2k), which is even."
10. Is "1 + 1 = 2, 3 + 5 = 8, 7 + 9 = 16 are even, so odd + odd is always even" a proof? What can examples do?

### Extra

11. Prove: if m and n are odd, then m · n is odd.
12. Prove: if n is even, then n² + 4n is divisible by 4. Hint: write it as 4 · (integer).
13. Prove: if a | b and a | c, then a | (b + c).
14. Prove: if a | b, then a | b².
15. Prove: the sum of any three consecutive integers is divisible by 3. Hint: call them n, n + 1, n + 2.
16. Disprove with a counterexample: "if n² is divisible by 4, then n is divisible by 4."
17. ★ Prove: if n is odd, then 8 | (n² − 1). Hint: k(k + 1) is always even.

## Lesson 4B: Contrapositive and contradiction

Line 1 names the method, a reason on every line, name the lines that clash, last line states the original claim.

### Quiz

1. "If a program passes all tests, then it has no syntax errors." (a) Write its contrapositive and converse. (b) Which is equivalent to the original, and why?
2. Prove by contrapositive: if 5n + 3 is even, then n is odd.
3. Prove by contrapositive: if n³ is even, then n is even.
4. Prove by contradiction: there are no integers m, n with 2m + 4n = 7.
5. Prove by contradiction: there is no largest even integer.

### Drill

6. Write the contrapositive: (a) "If n² is odd, then n is odd." (b) "If x + y ≥ 10, then x ≥ 5 or y ≥ 5."
7. Prove by contrapositive: if n² is odd, then n is odd.
8. Prove by contrapositive: if x + y ≥ 10, then x ≥ 5 or y ≥ 5 (real numbers).
9. Prove by contradiction: there is no smallest positive rational number.
10. Which method would you use, and why? (a) "If n is odd, then n + 2 is odd." (b) "If n³ is even, then n is even." (c) "There are no integers m, n with 2m + 4n = 7."

### Extra

11. Prove by contrapositive: if 7n + 4 is odd, then n is odd.
12. Prove by contrapositive: if n² is not divisible by 2, then n is not divisible by 2. Then explain why this is the same as drill question 7.
13. Prove by contrapositive: if a · b is even, then a is even or b is even. Hint: De Morgan on the conclusion.
14. Prove by contradiction: there are no integers m, n with 6m + 9n = 100. Hint: 3 divides the left side.
15. Prove by contradiction: there is no smallest positive real number.
16. Prove by contradiction: if n² is even, then n is even. (Start with "Assume, for contradiction, n² is even and n is odd.")
17. ★ Prove that √3 is irrational. You may use: if n² is divisible by 3, then n is divisible by 3.

## Lesson 4C: Induction

Use the template: base case with both sides, goal written in full, [IH] marked, conclusion about n.

### Quiz

1. P(n): 2 + 4 + 6 + … + 2n = n(n + 1). (a) Check P(1), P(2), P(3) with both sides. (b) Write P(k) and P(k + 1) in full.
2. Prove that claim by induction for all n ≥ 1.
3. Prove: for all n ≥ 0, 1 + 2 + 4 + … + 2ⁿ = 2ⁿ⁺¹ − 1.
4. Prove: for all n ≥ 0, 5 | (6ⁿ − 1).
5. (a) Find the flaw in "Assume k² + k is odd; then (k + 1)² + (k + 1) = (k² + k) + 2(k + 1) is odd + even, so odd", and show the claim is false. (b) For `power2(n)` (returns 1 if n == 0, else 2 * power2(n − 1)), name the base case and where the code relies on the IH.

### Drill

6. P(n): 1 + 3 + 5 + … + (2n − 1) = n². Check P(1), P(2), P(3) with both sides, and write P(k), P(k + 1).
7. Prove that claim by induction for all n ≥ 1.
8. Prove: for all n ≥ 0, 2 | (n² + n).
9. What's wrong with "Assume k = k + 1; adding 1 gives k + 1 = k + 2; so by induction n = n + 1 for all n"?
10. For the `total` loop that adds i for i = 1 to n, state what total equals after i runs from 1 to k, and which proof shows the loop is correct.

### Extra

11. Prove: for all n ≥ 1, 1² + 2² + … + n² = n(n + 1)(2n + 1)/6.
12. Prove: for all n ≥ 1, 1 + 3 + 9 + … + 3ⁿ⁻¹ = (3ⁿ − 1)/2.
13. Prove: for all n ≥ 0, 3 | (n³ − n). Hint: expand (k + 1)³ − (k + 1) and find k³ − k inside.
14. Prove: for all n ≥ 1, 2ⁿ ≥ n + 1.
15. Prove: for all n ≥ 0, 7 | (8ⁿ − 1).
16. Write a recursive Python function `sum_to(n)` that returns 1 + 2 + … + n (with sum_to(0) = 0), then explain its base case and where it relies on the IH to be correct.
17. ★ Prove: for all n ≥ 4, 2ⁿ ≥ n². Check why the claim fails for n = 3, and why that means the base case must be n = 4.

## Mixed review

Each question uses ideas from more than one lesson. Good for a revision session after a long break.

1. Translate "Every even number greater than 2 is not prime" into symbols (domain integers; define E(n), P(n)). Then negate it, simplify, and say the negation in English. Is the original true? Prove it, or give a counterexample.
2. Prove with laws that not (p -> q) or (p -> q) is a tautology. Then explain in one line why you didn't need to know what p and q mean.
3. Prove that p -> q and not q -> not p are equivalent in two ways: (a) with case lists, (b) with laws. Then use this to explain why proof by contrapositive is valid.
4. Domain integers. Decide true or false and prove it: (a) forall n (n² + n is even) (b) exists n (n² + n is odd) (c) forall n exists m (m > n²)
5. A friend writes: "Claim: forall n ≥ 1, n² ≥ n. Check: 1 ≥ 1, 4 ≥ 2, 9 ≥ 3. Proven." (a) What's wrong with this as a proof? (b) Write a real proof, using any method from Lesson 4.
6. Prove that for every integer n, n is even if and only if n² is even. Hint: an <-> needs two directions; use a different method for each.
7. This function claims to return True exactly when every element of nums is positive. Find the input where it fails, and say which lesson's idea the bug breaks:

```python
def all_positive(nums):
    for n in nums:
        if n > 0:
            return True
    return False
```

8. ★ Prove by induction that for all n ≥ 1, the number of cases in a case list for n variables is 2ⁿ. Hint: how does adding one more variable change the list?

## Related LeetCode problems

All Easy. For each one, before coding, write the condition in symbols (forall / exists, and / or / ->) and say which lesson idea it uses.

| Problem | Lesson | Logic or proof idea |
| --- | --- | --- |
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | 3C | exists i exists j (i != j and nums[i] + nums[j] == target): nested exists = nested loops. |
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 3C | exists i exists j (i != j and nums[i] == nums[j]). |
| [1346. Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/) | 3C | exists i exists j (i != j and arr[i] == 2 · arr[j]). |
| [896. Monotonic Array](https://leetcode.com/problems/monotonic-array/) | 3A, 2B | forall i (a[i] <= a[i+1]) or forall i (a[i] >= a[i+1]); the negation tells you when to stop early. |
| [1550. Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds/) | 3A, 4A | exists i (arr[i], arr[i+1], arr[i+2] are all odd), using the definition of odd. |
| [1822. Sign of the Product of an Array](https://leetcode.com/problems/sign-of-the-product-of-an-array/) | 3A | exists i (nums[i] == 0) decides 0; otherwise count negatives (even or odd). |
| [136. Single Number](https://leetcode.com/problems/single-number/) | 1, 2B | xor: x xor x == 0 and x xor 0 == x, like the laws in 2B. |
| [268. Missing Number](https://leetcode.com/problems/missing-number/) | 4C | The sum formula n(n + 1)/2 you proved by induction. |
| [1523. Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | 4A | Definitions of even and odd; prove your formula works for every case. |
| [2413. Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/) | 4A | Divides: if n is even, the answer is n; otherwise 2n. Prove both cases. |
| [231. Power of Two](https://leetcode.com/problems/power-of-two/) | 4C | 2ⁿ and the recursive power2 idea; prove your loop or recursion with an invariant. |
| [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | 4C | Recursion = induction: base cases F(0), F(1), and the IH for smaller n. |
