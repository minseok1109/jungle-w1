import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().strip().split())
li = list(map(int, sys.stdin.readline().strip().split()))
max_ = 0
for item in list(permutations(li, 3)):
    sum_ = sum(item)
    if sum_ > m:
        continue
    elif sum_ == m:
        max_ = m
    elif max_ < sum_:
        max_ = sum_

print(max_)
