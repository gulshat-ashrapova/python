num = int(input())
len = 0
sum = 0
while num != 0:
    len += 1
    sum += num
    num = int(input())
print(sum/len) #среднее арифметическое последовательности чисел до 0