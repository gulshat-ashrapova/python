# найти место в строю для Петра
# Программа получает на вход невозрастающую последовательность 
# натуральных чисел, означающих рост каждого человека в строю. 
# После этого вводится число X – рост Пети. 
# Все числа во входных данных натуральные и не превышают 200.
# Выведите номер, под которым Петя должен встать в строй. 
# Если в строю есть люди с одинаковым ростом, таким же, как у Пети,
# то он должен встать после них.
# переводим первое значение в целые числа в строке
# второе значение в целое число piter
# проверяем меньше ли число piter каждого числа в строке Len(a)
# с каждым числом индекс увеличивается на единицу
a = [int(i) for i in input().split()]
piter = int(input())
index_of_piter = 0
for i in range (0,len(a)):
    if a[i] >= piter:
        index_of_piter += 1
print (index_of_piter + 1)        