import math

c = int(input())

scores = [list(map(int, input().split())) for _ in range(c)]
averages = []
for score in scores:
    n = score.pop(0)
    sum_ = sum(score)
    average = sum_ / n
    count = 0
    for i in score:
        if i > average:
            count += 1
    print(f"{'{:.3f}'.format(round((count / n)*100, 3))}%")
