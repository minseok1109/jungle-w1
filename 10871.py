n, x = map(int, input().split())
li = list(map(int, input().split()))

for number in li:
    if number < x:
        print(number, end=' ')
