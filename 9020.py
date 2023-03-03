import math

t = int(input())
li = [int(input()) for _ in range(t)]


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0 or x == 1:
            return False
    return True


# for num in li:
#     answer = None
#     minimum = 100
#     divideNum = num // 2
#     for i in range(1, divideNum+1):
#         if is_prime_number(i) is True and is_prime_number(num - i) is True:
#             if (num - i) - i < minimum:
#                 answer = [i, num - i]
#                 minimum = (num - i) - i
#     print(answer[0], answer[1])

for num in li:
    a, b = num//2, num//2
    while a > 0:
        if is_prime_number(a) and is_prime_number(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
