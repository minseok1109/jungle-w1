n = int(input())

li = [input().split() for _ in range(n)]
for item in li:
    t = int(item.pop(0))
    for string in item[0]:
        print(string * t, end="")
    print()
