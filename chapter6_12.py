num = int(input())
max = 0
smax = 0
while num != 0:
    if num > max:
        smax = max
        max = num
    else:        
        if num > smax:
            smax = num
    num = int(input())
print (smax) #второе по величине число