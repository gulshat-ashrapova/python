n = int(input())
mult = 1
sum = 0
for i in range (1, n+1):
    mult *= i
    sum += mult
print (sum)
