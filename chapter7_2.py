; ; Выведите все четные элементы списка. 
; При этом используйте цикл for, 
; перебирающий элементы списка, а не их индексы!
a = input().split( )
k = []
for symbol in a:
    if int(symbol) % 2 == 0:
        k.append(symbol)
print (' '.join(k))