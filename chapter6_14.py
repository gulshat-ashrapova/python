; Дана последовательность натуральных чисел, завершающаяся числом 0. 
; Определите, какое наибольшее число подряд идущих элементов этой
; последовательности равны друг друг

curr_elem = int(input())
max_seq_len = 1
cur_seq_len = 1
prev_elem = 0

while curr_elem != 0:
    if curr_elem == prev_elem:
        cur_seq_len += 1
    else:
        if cur_seq_len > max_seq_len:
            max_seq_len = cur_seq_len
        prev_elem = curr_elem
        cur_seq_len = 1
    curr_elem = int(input())

if cur_seq_len > max_seq_len:
    max_seq_len = cur_seq_len
print(max_seq_len)
