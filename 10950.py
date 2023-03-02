t = int(input())
list_ = []
for i in range(t):
    numbers = list(map(int, input().split()))
    list_.append(numbers)

for num1, num2 in list_:
    print(num1 + num2)
