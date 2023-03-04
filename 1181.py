import sys

n = int(sys.stdin.readline())

li = [sys.stdin.readline().strip() for _ in range(n)]

sorted(li, key=len).sort()

for i in li:
    print(i)
