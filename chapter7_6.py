# Дан список чисел. Выведите значение наибольшего элемента
# в списке, а затем индекс этого элемента в списке. 
# Если наибольших элементов несколько, 
# выведите индекс первого из них.
a = [int(i) for i in input().split()]
index_of_max = 0
print (max(a), a.index(max(a)))
for i in range (1,len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print (a[index_of_max], index_of_max)  