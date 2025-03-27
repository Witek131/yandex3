# c∧(a∨d)∧(d→b) FaLSE

from itertools import product, permutations


def f(a, b, c, d):
    return c and (a or b) and (d >= b)


for a in product([0, 1], repeat=6):
    rows = [(a[0], a[1], a[2], 0), (a[3], 1, 0, a[4]), (0, a[5], 1, 0)]
    val = [1, 1, 1]
    if len(set(rows)) != len(rows):
        continue
    for per in permutations('abcd'):
        if all([f(**dict(zip(per, row))) == va for row, va in zip(rows, val)]):
            print(per)
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if c and (a or b) and (d >= b):
                    print(a, b, c, d)