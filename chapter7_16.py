; Известно, что на доске 8×8 можно расставить 8 ферзей так, 
; чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
; определите, есть ли среди них пара бьющих друг друга.
; Программа получает на вход восемь пар чисел, каждое 
; число от 1 до 8 — координаты 8 ферзей. 
; Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

r_lst = []
c_lst = []
for i in range(8):
    r, c = [int(s) for s in input().split()]
    r_lst.append(r)  # сделать список из рядов
    c_lst.append(c)  # сделать список из колонок
correct = True
for i in range(8):
    for j in range(i+1, 8): #начинаю сравнивать первую с каждой
        if r_lst[i] == r_lst[j] or c_lst[i] == c_lst[j] or abs(
                c_lst[i] - c_lst[j]) == abs(r_lst[i] - r_lst[j]):
            correct = False
if correct:
    print('NO')
else:
    print('YES')