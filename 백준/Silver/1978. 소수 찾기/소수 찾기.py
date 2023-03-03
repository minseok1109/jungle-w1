import math
n = int(input())
li = list(map(int, input().split()))
count = 0


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for i in li:
    if i == 1:
        continue
    if is_prime_number(i):
        count += 1

print(count)
