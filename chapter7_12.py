; Дан список целых чисел, число k и значение C. Необходимо вставить в список 
; на позицию с индексом k элемент, равный C, 
; сдвинув все элементы, имевшие индекс не менее k, вправо.
a = [int(i) for i in input().split()]
n = [int(i) for i in input().split()]
#теперь я знаю, что n[0] индекс, а n[1] это число
idx = n[0]
num = n[1]
a.append(num)
for i in range (idx,len(a)):
    a[len(a)-1], a[idx] = a[idx],a[len(a)-1]
    idx +=1
print (' '.join([str(i)for i in a]))