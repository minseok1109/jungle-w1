import math

t = int(input())
li = [int(input()) for _ in range(t)]


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0 or x == 1:
            return False
    return True


for num in li:
    a, b = num//2, num//2
    while a > 0:
        if is_prime_number(a) and is_prime_number(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
