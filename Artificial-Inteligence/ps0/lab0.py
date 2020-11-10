# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

from algebra_utils import distribution, encode_sumprod, decode_sumprod
from algebra import Sum, Product, simplify_if_possible


def cube(x):
    return x ** 3


def factorial(x):
    if x <= 0:
        raise Exception
    s = 1
    for k in range(2, x+1):
        s = s * k

    return s


def count_pattern(pattern, lst):
    count = 0
    for i in range(len(lst)):
        tag = 0
        for j in range(len(pattern)):
            if i+j < len(lst) and lst[i+j] == pattern[j]:
                tag = tag + 1
        if tag == len(pattern):
            count = count + 1

    return count


# Problem 2.2: Expression depth

def depth(expr):
    if not isinstance(expr, (list, tuple)):
        return 0

    c0 = 0
    c1 = 1
    for k in expr:
        c0 = 1 + depth(k)
        c1 = max(c0, c1)

    return c1


# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    out = tree
    for k in index:
        out = out[k]
    return out


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.


# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = ""

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = ""

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = ""

# How many hours did this lab take?
HOURS = ""
