import sys
from itertools import permutations

li = sorted([int(sys.stdin.readline().strip()) for _ in range(9)])

subtract = sum(li) - 100
test = (permutations(li, 2))

for x, y in test:
    if x + y == subtract:
        li.remove(li[li.index(x)])
        li.remove(li[li.index(y)])
        break

for i in li:
    print(i)
