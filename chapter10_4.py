; Во входной строке записана последовательность чисел через пробел. 
; Для каждого числа выведите слово YES (в отдельной строке),
;  если это число ранее встречалось в последовательности
;  или NO, если не встречалось.
 
A = [int(elem) for elem in input().split()]
res = set()
for elem in A:
    if elem in res:
        print('YES')
    else:
        print('NO')
        res.add(elem)    