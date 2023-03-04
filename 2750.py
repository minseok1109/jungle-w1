n = int(input())

li = [int(input()) for _ in range(n)]


def bubbleSort(a):
    n = len(a)
    for i in range(n - 1):
        exchange = 0
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchange += 1
        if exchange == 0:
            break


bubbleSort(li)
for i in li:
    print(i)
