# Определите стандартное отклонение для данной последовательности натуральных 
# чисел, завершающейся числом 0.

from math import sqrt

num = int(input())
len = 0
sum = 0
sums = 0
while num != 0:
    len += 1
    sum += num
    sums += num ** 2
    num = int(input())
sigma = sqrt((sums - sum ** 2/len) / (len-1))