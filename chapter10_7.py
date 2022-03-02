; ; Август и Беатриса играют в игру. Август загадал натуральное число 
; от 1 до n. 
; Беатриса пытается угадать это число, для этого она называет некоторые 
; множества натуральных чисел. Август отвечает Беатрисе YES, 
; если среди названных ей чисел есть задуманное или NO в противном случае. 
; После нескольких заданныъх вопросов Беатриса запуталась в том, 
; какие вопросы она задавала и какие ответы получила 
; и просит вас помочь ей определить, какие числа мог задумать Август.

; В первой строке задано n - максимальное число, которое мог загадать Август.

; Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных
; пробелом) и ответ Августа на этот вопрос.

; Вы должны вывести через пробел, в порядке возрастания, 
; все числа, которые мог задумать Август.


n = int(input())
s = [s for s in range (1,n+1)] #так получается упорядоченный список чисел
all_numbers = set(s)
while True:
    num = input()
    if num == 'HELP':
        break
    answer = input()
    if answer == 'NO':
        all_numbers -= set(num.split())
    if answer == 'YES':
        all_numbers &= set(num.split())
print(' '.join([str(i) for i in all_numbers]))


# решение разработчиков
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))