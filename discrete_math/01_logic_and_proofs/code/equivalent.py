# Challenge: equivalence checker

# Write a Python function that checks whether two logical expressions are equivalent by trying every case. It automates what you've been doing by hand in your case lists.

# Requirements
# Write a function equivalent(f, g).
# f and g are Python functions that take p and q (booleans) and return a boolean.
# Loop over all 4 cases in standard order: TT, TF, FT, FF.
# Return True if f and g give the same result in every case. Otherwise return False.
# If they're not equivalent, print the first case where they differ. That's your single-case counterexample, like in Q4.
# Hints (only if you get stuck)
# You can pass a function as an argument. Define the expressions with def or lambda, which you saw in CS50P.
# Python has no -> or xor for booleans:
# For ->, use your own Lesson 1 Q5(b) expression.
# For xor on booleans, p != q works.
# Use two nested loops over [True, False] to get the standard order.
# Test it with your own results

# Your checker should agree with what you proved by hand:

# p xor q vs (p or q) and not (p and q) should give True (Drill D2)
# not (p or q) vs (not p) and (not q) should give True (Quiz 2A Q3)
# not (p and q) vs (not p) and (not q) should give False, with a differing case of TF (Q4)
# p -> q vs q -> p should give False (Lesson 2A)
# Bonus (optional)

# Extend it to 3 variables and test that (p and q) -> r vs p -> (q -> r) gives True. That's the equivalence you just discovered.

# Extra challenge: make it work for any number of variables. Look up itertools.product in the Python docs.

# ---------------------------------------------------------------
# TODO (from Claude's review, 2026-10-20) — do these next:
#
# 1. Requirement 4: when f and g differ, print the case where they
#    differ (p and q) with an f-string, just before `return False`.
#
# 2. Run all 4 tests, not just one:
#    - write a separate, clearly named pair of functions for each test
#      (e.g. xor_a / xor_b, implies / converse) instead of only f and g
#    - call equivalent(...) four times in main()
#    - check the outputs match the expected results above
#      (the Q4 test should print case TF)
#
# 3. Replace the hardcoded `cases` list with two nested loops over
#    [True, False], so it scales to 3+ variables (needed for the bonus).
#
# Small things:
# - rename res1 / res2 to say where each came from (e.g. res_f / res_g)
# - replace the pasted challenge text above with a short docstring
#   at the top of the file saying what this file does
#
# Bonus (optional): 3 variables, then any number of variables
# (itertools.product).
# ---------------------------------------------------------------

def main():
    print(equivalent(f, g))

def equivalent(f, g):
    cases = [
        [True, True],
        [True, False],
        [False, True],
        [False, False]
    ]
    for p, q in cases:
        res1 = f(p, q)
        res2 = g(p, q)
        if res1 != res2:
            return False

    return True

def f(p, q):
    return not (p or q)

def g(p, q):
    return (not p) and (not q)

if __name__ == "__main__":
    main()