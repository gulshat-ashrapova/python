; В первой строке входных данных записаны числа N и M — число кубиков у Ани
;  и Бори. В следующих N строках заданы номера цветов кубиков Ани. 
;  В последних M строках номера цветов Бори.

; Найдите три множества: номера цветов кубиков, которые есть в обоих наборах
; ; номера цветов кубиков, которые есть только у Ани и номера цветов кубиков,
;  есть только у Бори. Для каждого из множеств выведите сначала 
;  количество элементов в нем, 
; а затем сами элементы, отсортированные по возрастанию.



N,M = [int(i) for i in input().split()]
anna = set()
boris = set()
both = set()
for i in range(N):
    anna.add(int(input()))
for i in range(M):
    boris.add(int(input()))
both = anna.intersection(boris)
anna_sorted = sorted([int(i) for i in anna.difference(boris)])
boris_sorted = sorted([int(i) for i in boris.difference(anna)])
print(len(both))
print(' '.join([str(elem) for elem in both]))
print(len(anna_sorted))
print(' '.join([str(elem) for elem in anna_sorted]))
print(len(boris_sorted))
print(' '.join([str(elem) for elem in boris_sorted]))