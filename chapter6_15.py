n = int(input())
preview = 0
res = 1
if n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    while n > 1:
        res, preview = res+preview, res
        n -= 1
    print(res) #посчитать число фибоначчи