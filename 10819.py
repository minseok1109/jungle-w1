import sys
from itertools import permutations

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().strip().split()))


def sumAll(list_):
    sum_ = 0
    for i in range(len(list_) - 1):
        cal = abs(list_[i] - list_[i + 1])
        sum_ += cal
    return sum_


max_ = 0
for item in (list(permutations(li, n))):
    v = sumAll(item)
    if max_ < sumAll(item):
        max_ = v

print(max_)
