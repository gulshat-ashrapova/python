num = int(input())
max = 0
n_of_max = 0
while num != 0:
    if max < num:
        max = num
        n_of_max = 1
    elif num == max:
        n_of_max += 1
    num = int(input())
print(n_of_max) #найти количество максимальных элементов