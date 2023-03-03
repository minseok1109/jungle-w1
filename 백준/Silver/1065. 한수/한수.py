n = int(input())

hansu = 0
for num in range(1, n+1):
    num_list = list(map(int, str(num)))
    if num < 100:
        hansu += 1
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        hansu += 1
print(hansu)
