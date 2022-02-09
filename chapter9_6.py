; Условие
; Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы
;  с номерами i и j и выведите результат.

; Программа получает на вход размеры массива n и m, затем элементы массива, 
; затем числа i и j.

; Решение оформите в виде функции swap_columns(a, i, j).



def swap_columns(a, i, j):
    for s in range (n):
        a[s][i],a[s][j] = a[s][j],a[s][i]
        
n, m = [int(s) for s in input().split()] #считали числа 
a = [[int(s) for s in input().split()] for elem in range(n)] #заполнили числами
i, j = [int(s) for s in input().split()] #считали числа i,j

swap_columns(a,i,j)

for row in a:
    print(' '.join([str(elem) for elem in row]))