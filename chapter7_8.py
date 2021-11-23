# преобразовать в список
# завести счетчик неравных чисел, изначально равный 1
# каждый раз, когда элемет не равен предыдущему, счетчик увелич на 1
a = [int(i) for i in input().split()]
number_of_elements = 1
for i in range (1,len(a)):
    if a[i-1] != a[i]:
        number_of_elements +=1
print (number_of_elements)