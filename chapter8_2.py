; Условие
; Дано действительное положительное число a и целоe число n.

; Вычислите an. Решение оформите в виде функции power(a, n).

; Стандартной функцией возведения в степень пользоваться нельзя.
def power (a, n):
    res = 1
    if n == 0:
        return 1
    elif n > 0:
        for i in range (1, n+1):
            res *= a
        return res
    elif n < 0:
        for i in range (1, abs (n) +1):
            res *= a
        return 1/res    
    
a = float(input())
n = int(input())    

print(power (a, n))     