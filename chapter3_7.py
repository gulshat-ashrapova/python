a = int(input())
b = int(input())
n = int(input())
summ_rub = a * n + ((b * n)//100)
summ_kopeika = (b * n) % 100
print (summ_rub, summ_kopeika)