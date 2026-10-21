"""
Checks whether two logical expressions are equivalent by testing every Boolean case.

Task: Lesson 2A coding challenge

Write a Python function that checks whether two logical expressions
are equivalent by trying every case.

Requirements:
- Write a function equivalent(f, g).
- f and g take p and q (booleans) and return a boolean.
- Loop over all 4 cases in standard order: TT, TF, FT, FF.
- Return True if both functions give the same result in every case.
- Otherwise, return False and print the first case where they differ.

Tests:
1. p xor q vs (p or q) and not (p and q) -> True
2. not (p or q) vs (not p) and (not q) -> True
3. not (p and q) vs (not p) and (not q) -> False, differing case TF
4. p -> q vs q -> p -> False

Hints:
- You can pass a function as an argument.
- For xor on booleans, use p != q.
- For implication, use (not p) or q.
- Use two nested loops over [True, False].

Bonus (optional):
- Extend it to 3 variables and test:
  (p and q) -> r vs p -> (q -> r).
- Extra challenge: make it work for any number of variables using itertools.product.

TODO — Claude's review (2026-10-20)

- [x] Print the first differing case with an f-string.
- [x] Run all four tests and check their expected results.
- [x] Use two nested loops over [True, False].
- [x] Rename res1/res2 to res_f/res_g.
- [x] Replace the challenge text with a short docstring.
- [x] Organize the file and remove unnecessary blank lines.
- [ ] Bonus: support three variables.
- [ ] Extra challenge: support any number of variables using itertools.product.
"""

def main():
    print("Test 1:")
    print(equivalent(xor, one_not_both))

    print("Test 2:")
    print(equivalent(not_or, not_p_and_not_q))

    print("Test 3:")
    print(equivalent(not_and, not_p_and_not_q))

    print("Test 4:")
    print(equivalent(implies, converse))


def equivalent(f, g):
    """Checks if two logical functions are equivalent."""

    values = [True, False]

    for p in values:
        for q in values:
            res_f = f(p, q)
            res_g = g(p, q)

            if res_f != res_g:
                print(f"Functions differ for p={p}, q={q}")
                return False

    return True


def xor(p, q):
    return p != q


def one_not_both(p, q):
    return (p or q) and not (p and q)


def not_or(p, q):
    return not (p or q)


def not_p_and_not_q(p, q):
    return (not p) and (not q)


def not_and(p, q):
    return not (p and q)


def implies(p, q):
    return (not p) or q


def converse(p, q):
    return (not q) or p


if __name__ == "__main__":
    main()
