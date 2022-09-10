from fractions import Fraction as F
from itertools import combinations_with_replacement, permutations, product
from collections import Counter
import time

start = time.time()


lowdig, highdig = 1, 9
binary_ops = [lambda x,y: x+y, lambda x,y: x-y, lambda x,y: x*y, lambda x,y: x/y]

# I believe there are essentially only five binary graphs on four items
#   ((A B) (C D)), ((A B) C) D), ((C (A B)) D), (D ((A B) C)), (D (C (A B)))
# We consider all possible ways to fill operators on the internal nodes
# and all possible ways to fill values on the leaves

def evaluate_groupings(x):
    r = set()
    for op1, op2, op3 in product(binary_ops, repeat=3):
        for f in [
                lambda x: op3(op1(F(x[0]),F(x[1])), op2(F(x[2]), F(x[3]))),
                lambda x: op3(op2(op1(F(x[0]),F(x[1])), F(x[2])), F(x[3])),
                lambda x: op3(op2(F(x[2]), op1(F(x[0]),F(x[1]))), F(x[3])),
                lambda x: op3(F(x[3]), op2(op1(F(x[0]),F(x[1])), F(x[2]))),
                lambda x: op3(F(x[3]), op2(F(x[2]), op1(F(x[0]),F(x[1])))),
        ]:
            try:
                result = f(x)
                if result.denominator == 1:
                    r.add(result.numerator)
            except ZeroDivisionError:
                pass
    return r


possible = {}
                
for x in combinations_with_replacement(range(lowdig, highdig+1), 4):
    r = set()
    for perx in permutations(x):
        # This will lead to much redundant work when there are repeated digits
        # But performnace isn't an issue for four digits taken from 1-9
        # Only 11880 instances at this level
        r.update(evaluate_groupings(perx))
    possible[x] = r

ngames = Counter()
nresults = Counter()
for x, r in possible.items():
    nresults[x] = len([1 for i in r if i > 0])
    for i in r:
        ngames[i] += 1

print(f"A 'puzzle' is a combination of four digits ({lowdig}-{highdig}) with replacement/repetition")
print()
print(f"{len(possible)} possible puzzles")

for n, cnt in ngames.most_common(32):
    print(f"{cnt} puzzles can achieve {n}")

print()
print(f"There are {len(nresults)} possible positive integers achievable from puzzles")

for n, cnt in nresults.most_common(32):
    print(f"{cnt} positive integers can be made from the puzzle {n}")

end = time.time()
print()
print(f"Running time was {end - start:.2f} seconds")
