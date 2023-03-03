n = int(input())

li = [input() for _ in range(n)]
for ox in li:
    sum_ = 0
    num = 0
    for letter in ox:
        if letter == 'O':
            num += 1
            sum_ += num
        else:
            num = 0
    print(sum_)
