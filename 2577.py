a = int(input())
b = int(input())
c = int(input())
number = a * b * c
number_list = (list(str(number)))
my_dict = {}

for i in range(10):
    my_dict[i] = 0

for num in number_list:
    my_dict[int(num)] = my_dict[int(num)] + 1

for i in range(10):
    print(my_dict[i])
